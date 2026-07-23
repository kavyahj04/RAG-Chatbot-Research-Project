"""
Produce a cleaned graph file for Neo4j ingestion, WITHOUT modifying the source.

Reads : graph_documents_full.jsonl   (never written to)
Writes: graph_documents_clean.jsonl  (new file)

Three fixes:
1. Node-type casing -> normalized to the schema's canonical Title Case.
2. Recoverable dangling endpoints -> node added using the type it has elsewhere.
3. Unrecoverable dangling endpoints -> node added with a type inferred by an LLM
   (constrained to the 26 schema types; falls back to 'Taxonomy Concept').

After this, every relationship endpoint exists as a typed node in its document.

Run with the system python3:  python3 rag/pipeline/clean_graph.py
"""

import json
from pathlib import Path
from collections import Counter
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DIR = BASE_DIR / "json"
load_dotenv(BASE_DIR / ".env", override=True)

IN_PATH = JSON_DIR / "graph_documents_full.jsonl"
OUT_PATH = JSON_DIR / "graph_documents_clean.jsonl"

client = OpenAI()
BATCH = 25

schema = json.load(open(JSON_DIR / "consolidated_schema.json", encoding="utf-8"))
CANON = [n["name"] for n in schema["node_types"]]
CANON_LC = {name.lower(): name for name in CANON}
FALLBACK = "Taxonomy Concept"


def classify_batch(items):
    """items: list of (entity_name, [context lines]) -> dict {name: schema_type}."""
    listing = []
    for idx, (name, ctx) in enumerate(items, 1):
        rels = "; ".join(ctx[:5])
        listing.append(f'{idx}. "{name}" — appears in: {rels}')
    prompt = (
        "You are classifying entities from a GitLab security handbook knowledge graph.\n"
        "Assign each entity to EXACTLY ONE of these node types:\n"
        + ", ".join(CANON)
        + "\n\nEntities and the relationships they appear in:\n"
        + "\n".join(listing)
        + '\n\nReturn a JSON object mapping each entity name (exact string) to one type '
        "from the list above. Use only those types."
    )
    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"},
    )
    return json.loads(resp.choices[0].message.content)


def main():
    gdocs = [json.loads(l) for l in open(IN_PATH, encoding="utf-8")]
    print(f"Loaded {len(gdocs)} graph docs (read-only)")

    # 1) normalize node-type casing to canonical
    recased = 0
    for g in gdocs:
        for n in g["nodes"]:
            canon = CANON_LC.get(n["type"].lower())
            if canon and canon != n["type"]:
                n["type"] = canon
                recased += 1
    print(f"Casing normalized: {recased} node types re-cased")

    # global map of id -> majority type (after casing) to recover known entities
    global_types = {}
    for g in gdocs:
        for n in g["nodes"]:
            global_types.setdefault(n["id"], Counter())[n["type"]] += 1

    # 2) find dangling endpoints; split into recoverable vs. needs-LLM
    recoverable = {}          # name -> majority type
    unrec_ctx = {}            # name -> [relationship context strings]
    for g in gdocs:
        ids = {n["id"] for n in g["nodes"]}
        for r in g["relationships"]:
            for e in (r["source"], r["target"]):
                if e in ids:
                    continue
                if e in global_types:
                    recoverable[e] = global_types[e].most_common(1)[0][0]
                else:
                    line = (f'{e} -[{r["type"]}]-> {r["target"]}'
                            if r["source"] == e
                            else f'{r["source"]} -[{r["type"]}]-> {e}')
                    unrec_ctx.setdefault(e, []).append(line)
    print(f"Dangling: {len(recoverable)} recoverable, {len(unrec_ctx)} need LLM")

    # 3) LLM-infer types for unrecoverable entities (batched)
    inferred = {}
    items = list(unrec_ctx.items())
    for i in range(0, len(items), BATCH):
        batch = items[i:i + BATCH]
        try:
            result = classify_batch(batch)
        except Exception as exc:
            print(f"  batch {i} failed ({exc}); using fallback for it")
            result = {}
        for name, _ in batch:
            t = result.get(name)
            inferred[name] = t if t in CANON else FALLBACK
        print(f"  classified {min(i + BATCH, len(items))}/{len(items)}")

    missing_type = {**recoverable, **inferred}

    # 4) add the missing endpoint nodes into each doc
    added = 0
    for g in gdocs:
        ids = {n["id"] for n in g["nodes"]}
        need = set()
        for r in g["relationships"]:
            for e in (r["source"], r["target"]):
                if e not in ids:
                    need.add(e)
        for e in need:
            g["nodes"].append({
                "id": e,
                "type": missing_type.get(e, FALLBACK),
                "properties": {},
            })
            added += 1
    print(f"Added {added} previously-missing endpoint nodes")

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        for g in gdocs:
            f.write(json.dumps(g) + "\n")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
