"""
One-off fix for the 2 oversized chunks that never got embedded.

Root cause: chunking.py refused to split any chunk containing HTML
(<table/<div/<ul), so these two came out at 33,616 and 9,866 tokens and
embed.py skipped them (its limit is 8,000).

This script splits ONLY those two chunks: it strips their embedded HTML to
markdown text, re-splits them into <=500-token sub-chunks (ids _1_0, _1_1, ...),
and updates chunks.json, embeddings.json, and graph_documents_full.jsonl.
Every other chunk is left untouched.

Run with the system python3 (has langchain_experimental):
    python3 rag/archive/test.py
"""

import json
import re
import time
from pathlib import Path

import tiktoken
from dotenv import load_dotenv
from openai import OpenAI
from markdownify import markdownify as to_md
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DIR = BASE_DIR / "json"
load_dotenv(BASE_DIR / ".env", override=True)

client = OpenAI()
encoder = tiktoken.get_encoding("cl100k_base")

CHUNK_SIZE = 500
TARGET_IDS = [
    "corporate/systems/_index.md_1",
    "corporate/team/_index.md_1",
]


def count_tokens(text):
    return len(encoder.encode(text))


def html_to_text(text):
    # convert embedded HTML (tables/divs/lists) to markdown text
    text = to_md(text, heading_style="ATX", bullets="-")
    text = re.sub(r"\n{3,}", "\n\n", text)  # collapse extra blank lines
    return text.strip()


def split_text(text):
    """Split a block into <=CHUNK_SIZE token pieces (paragraph-aware, line fallback)."""
    if "<table" in text or "<div" in text or "<ul" in text:
        text = html_to_text(text)

    if count_tokens(text) <= CHUNK_SIZE:
        return [text]

    # first pass: pack paragraphs (split on blank lines)
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    packed, current = [], []
    for para in paragraphs:
        if current and count_tokens("\n\n".join(current + [para])) > CHUNK_SIZE:
            packed.append("\n\n".join(current).strip())
            current = [para]
        else:
            current.append(para)
    if current:
        packed.append("\n\n".join(current).strip())

    # second pass: anything still too big (e.g. a converted table) -> split by lines
    result = []
    for piece in packed:
        if count_tokens(piece) <= CHUNK_SIZE:
            result.append(piece)
            continue
        lines = [ln for ln in piece.split("\n") if ln.strip()]
        cur = []
        for ln in lines:
            if cur and count_tokens("\n".join(cur + [ln])) > CHUNK_SIZE:
                result.append("\n".join(cur).strip())
                cur = [ln]
            else:
                cur.append(ln)
        if cur:
            result.append("\n".join(cur).strip())
    return result


def generate_summary(text, breadcrumb):
    # same prompt the pipeline uses, so summaries stay consistent
    if count_tokens(text) < 30:
        return ""
    prompt = f"""You are helping build a RAG (Retrieval Augmented Generation) system for a security chatbot.

                Your job is to write a one-sentence summary of a policy section that will be stored as metadata.
                This summary will be used during retrieval — when a user asks a question, their question is
                compared against your summary to find the most relevant policy section.

                So your summary must:
                - Use plain everyday language a user would actually use when asking a question
                - Capture the core policy rule or procedure in the section
                - Be specific — mention the tool, process, or policy name if present
                - Avoid formal policy language like "this section outlines" or "this pertains to"

                Section location: {breadcrumb}

                Section content:
                {text}

                Write only the one sentence summary. Nothing else.
                """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0,
    )
    time.sleep(0.1)
    return response.choices[0].message.content.strip()


# graph transformer, same config as build_graph.py
ADDITIONAL_INSTRUCTIONS = """
Follow these patterns, based on this specific handbook:

1. Numbers derived from a formula (e.g. "Bug Bounty Budget is 10% of Cost of
   Compromise") become a DERIVED_FROM relationship between two metric-style
   nodes. The dollar value itself is a "value" property on the node, never
   its own node.

2. If a named person appears only as a contact or titleholder, extract the
   ROLE as the node, not the person's name. Roles are stable, people change.

3. Job titles (Engineer, Manager, Analyst, DRI) must be Role entities
   connected via HAS_ROLE. Never make the job title itself a relationship
   type.

4. Step-by-step instructional text rarely has rich relationships. Extract
   only the system or process and what it REQUIRES.

5. Never extract UI actions (click, navigate to, add a field, check a box)
   as relationships or entities.

6. If the text is a placeholder page with no real content, return empty
   nodes and relationships. Don't invent structure from navigation text.
"""


def build_transformer():
    schema = json.load(open(JSON_DIR / "consolidated_schema.json", encoding="utf-8"))
    return LLMGraphTransformer(
        llm=ChatOpenAI(model="gpt-4.1-mini", temperature=0),
        allowed_nodes=[n["name"] for n in schema["node_types"]],
        allowed_relationships=[r["name"] for r in schema["relationship_types"]],
        node_properties=["value"],
        additional_instructions=ADDITIONAL_INSTRUCTIONS,
        strict_mode=False,
    )


def main():
    chunks = json.load(open(JSON_DIR / "chunks.json", encoding="utf-8"))
    by_id = {c["metadata"]["chunk_id"]: c for c in chunks}

    # 1) build sub-chunks for each oversized parent
    new_by_parent = {}
    for pid in TARGET_IDS:
        parent = by_id[pid]
        meta = parent["metadata"]
        pieces = split_text(parent["text"])
        subs = []
        for k, piece in enumerate(pieces):
            m = dict(meta)  # inherit headings/url/title/breadcrumb/source_file
            m["chunk_id"] = f"{pid}_{k}"
            m["chunk_index"] = k
            m["token_count"] = count_tokens(piece)
            m["section_summary"] = generate_summary(piece, meta["breadcrumb"])
            subs.append({"text": piece, "metadata": m})
        new_by_parent[pid] = subs
        print(f"  {pid}: {meta['token_count']} tok -> {len(subs)} sub-chunks")

    all_new = [s for subs in new_by_parent.values() for s in subs]

    # 2) rewrite chunks.json (replace each parent in place with its sub-chunks)
    rebuilt = []
    for c in chunks:
        cid = c["metadata"]["chunk_id"]
        rebuilt.extend(new_by_parent[cid]) if cid in new_by_parent else rebuilt.append(c)
    json.dump(rebuilt, open(JSON_DIR / "chunks.json", "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print(f"chunks.json: {len(chunks)} -> {len(rebuilt)}")

    # 3) embeddings — parents were never embedded, so just append the new ones
    emb = json.load(open(JSON_DIR / "embeddings.json", encoding="utf-8"))
    resp = client.embeddings.create(
        model="text-embedding-3-large",
        input=[s["text"] for s in all_new],
    )
    for s, item in zip(all_new, resp.data):
        emb.append({"chunk_id": s["metadata"]["chunk_id"], "embedding": item.embedding})
    json.dump(emb, open(JSON_DIR / "embeddings.json", "w", encoding="utf-8"))
    print(f"embeddings.json: +{len(all_new)} -> {len(emb)}")

    # 4) graph docs — drop stale parent entries, extract for the new sub-chunks
    transformer = build_transformer()
    docs = [Document(page_content=s["text"],
                     metadata={"chunk_id": s["metadata"]["chunk_id"]}) for s in all_new]
    graph_documents = transformer.convert_to_graph_documents(docs)

    path = JSON_DIR / "graph_documents_full.jsonl"
    kept = [json.loads(l) for l in open(path, encoding="utf-8")
            if json.loads(l)["chunk_id"] not in TARGET_IDS]
    for gd in graph_documents:
        kept.append({
            "chunk_id": gd.source.metadata["chunk_id"],
            "nodes": [{"id": n.id, "type": n.type, "properties": n.properties}
                      for n in gd.nodes],
            "relationships": [{"source": r.source.id, "type": r.type, "target": r.target.id}
                              for r in gd.relationships],
        })
    with open(path, "w", encoding="utf-8") as f:
        for g in kept:
            f.write(json.dumps(g) + "\n")
    print(f"graph_documents_full.jsonl: -> {len(kept)}")
    print("Done.")


if __name__ == "__main__":
    main()
