"""
Generate a Q&A evaluation dataset from chunks.json.

Produces qa_dataset.json with three question types:
  - single_hop   : answered from one chunk
  - multi_hop    : requires combining two related chunks
  - example_based: asks for a concrete example from the policy

Run: python3 generate_qa.py
"""

import json
import random
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
client = OpenAI()

CHUNKS_PATH = "chunks.json"
OUTPUT_PATH = "qa_dataset.json"

# how many of each type to generate
N_SINGLE   = 15
N_MULTI    = 10
N_EXAMPLE  = 10

# ── Load chunks ───────────────────────────────────────────────────────
with open(CHUNKS_PATH) as f:
    chunks = json.load(f)

# only use chunks with a real summary and enough text
rich = [
    c for c in chunks
    if len(c["text"].strip()) > 150
    and c["metadata"].get("section_summary", "").strip()
]
print(f"Rich chunks available: {len(rich)}")

random.seed(99)


# ── LLM helpers ──────────────────────────────────────────────────────

def generate_single_hop(chunk: dict) -> dict | None:
    breadcrumb = chunk["metadata"]["breadcrumb"]
    text = chunk["text"][:1200]

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": (
                "You are building an evaluation dataset for a security policy RAG chatbot.\n"
                "Given the policy excerpt below, write ONE specific factual question that can be "
                "answered from this excerpt alone, and provide the correct answer.\n"
                "The question should be phrased as a real employee would ask it — casual, practical.\n\n"
                f"Section: {breadcrumb}\n\nExcerpt:\n{text}\n\n"
                "Respond in JSON with exactly these keys:\n"
                '{"question": "...", "answer": "..."}'
            )
        }],
        temperature=0.7,
        max_tokens=300,
        response_format={"type": "json_object"},
    )
    data = json.loads(resp.choices[0].message.content)
    return {
        "type": "single_hop",
        "question": data["question"],
        "expected_answer": data["answer"],
        "source_chunks": [chunk["metadata"]["chunk_id"]],
        "breadcrumbs": [breadcrumb],
    }


def generate_multi_hop(chunk_a: dict, chunk_b: dict) -> dict | None:
    bc_a = chunk_a["metadata"]["breadcrumb"]
    bc_b = chunk_b["metadata"]["breadcrumb"]
    text_a = chunk_a["text"][:700]
    text_b = chunk_b["text"][:700]

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": (
                "You are building an evaluation dataset for a security policy RAG chatbot.\n"
                "Given TWO policy excerpts below, write ONE question that requires information "
                "from BOTH excerpts to answer fully. The question should feel natural — like "
                "a real employee asking in one go.\n"
                "Provide the correct answer that combines both excerpts.\n\n"
                f"Excerpt A — {bc_a}:\n{text_a}\n\n"
                f"Excerpt B — {bc_b}:\n{text_b}\n\n"
                "Respond in JSON:\n"
                '{"question": "...", "answer": "..."}'
            )
        }],
        temperature=0.7,
        max_tokens=400,
        response_format={"type": "json_object"},
    )
    data = json.loads(resp.choices[0].message.content)
    return {
        "type": "multi_hop",
        "question": data["question"],
        "expected_answer": data["answer"],
        "source_chunks": [chunk_a["metadata"]["chunk_id"], chunk_b["metadata"]["chunk_id"]],
        "breadcrumbs": [bc_a, bc_b],
    }


def generate_example_based(chunk: dict) -> dict | None:
    breadcrumb = chunk["metadata"]["breadcrumb"]
    text = chunk["text"][:1200]

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": (
                "You are building an evaluation dataset for a security policy RAG chatbot.\n"
                "Given the policy excerpt below, write ONE question that asks for a specific "
                "example, scenario, or illustration mentioned or implied in the policy. "
                "The answer should include a concrete example from the text.\n\n"
                f"Section: {breadcrumb}\n\nExcerpt:\n{text}\n\n"
                "Respond in JSON:\n"
                '{"question": "...", "answer": "..."}'
            )
        }],
        temperature=0.7,
        max_tokens=300,
        response_format={"type": "json_object"},
    )
    data = json.loads(resp.choices[0].message.content)
    return {
        "type": "example_based",
        "question": data["question"],
        "expected_answer": data["answer"],
        "source_chunks": [chunk["metadata"]["chunk_id"]],
        "breadcrumbs": [breadcrumb],
    }


# ── Generate Q&A pairs ────────────────────────────────────────────────

qa_pairs = []

# --- single hop ---
print(f"\nGenerating {N_SINGLE} single-hop questions...")
single_pool = random.sample(rich, N_SINGLE * 2)
count = 0
for chunk in single_pool:
    if count >= N_SINGLE:
        break
    try:
        qa = generate_single_hop(chunk)
        qa_pairs.append(qa)
        count += 1
        print(f"  [{count}/{N_SINGLE}] {qa['question'][:80]}")
        time.sleep(0.3)
    except Exception as e:
        print(f"  Skipped: {e}")

# --- multi hop ---
print(f"\nGenerating {N_MULTI} multi-hop questions...")

# group chunks by page_title so we can pair related sections
from collections import defaultdict
by_title = defaultdict(list)
for c in rich:
    by_title[c["metadata"]["page_title"]].append(c)

# pick titles with multiple chunks for intra-page multi-hop
multi_title_pool = [title for title, cs in by_title.items() if len(cs) >= 2]
cross_title_pool = [title for title, cs in by_title.items() if len(cs) >= 1]

count = 0
attempts = 0
while count < N_MULTI and attempts < N_MULTI * 4:
    attempts += 1
    # alternate: 50% same-page multi-hop, 50% cross-page
    if multi_title_pool and random.random() < 0.5:
        title = random.choice(multi_title_pool)
        pair = random.sample(by_title[title], 2)
    else:
        titles = random.sample(cross_title_pool, 2)
        pair = [random.choice(by_title[t]) for t in titles]
    try:
        qa = generate_multi_hop(pair[0], pair[1])
        qa_pairs.append(qa)
        count += 1
        print(f"  [{count}/{N_MULTI}] {qa['question'][:80]}")
        time.sleep(0.3)
    except Exception as e:
        print(f"  Skipped: {e}")

# --- example based ---
print(f"\nGenerating {N_EXAMPLE} example-based questions...")
example_pool = random.sample(rich, N_EXAMPLE * 2)
count = 0
for chunk in example_pool:
    if count >= N_EXAMPLE:
        break
    try:
        qa = generate_example_based(chunk)
        qa_pairs.append(qa)
        count += 1
        print(f"  [{count}/{N_EXAMPLE}] {qa['question'][:80]}")
        time.sleep(0.3)
    except Exception as e:
        print(f"  Skipped: {e}")

# ── Save ──────────────────────────────────────────────────────────────
output = {
    "total": len(qa_pairs),
    "single_hop": sum(1 for q in qa_pairs if q["type"] == "single_hop"),
    "multi_hop": sum(1 for q in qa_pairs if q["type"] == "multi_hop"),
    "example_based": sum(1 for q in qa_pairs if q["type"] == "example_based"),
    "pairs": qa_pairs,
}

with open(OUTPUT_PATH, "w") as f:
    json.dump(output, f, indent=2)

print(f"\nSaved {len(qa_pairs)} Q&A pairs to {OUTPUT_PATH}")
print(f"  single_hop:    {output['single_hop']}")
print(f"  multi_hop:     {output['multi_hop']}")
print(f"  example_based: {output['example_based']}")
