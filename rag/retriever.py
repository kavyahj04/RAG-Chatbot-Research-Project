import json
import os
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

client = OpenAI()
EMBED_MODEL = "text-embedding-3-small"

# ── Load data lazily ───────────────────────────────────────────────────
# chunks.json / embeddings.json are only needed by retrieve() (unused by the
# API, which searches via chromadb instead) — load on first use, not on import.

_chunks = None
_embeddings_data = None
_chunk_index = None
_chunk_ids = None
_matrix = None


def _ensure_loaded():
    global _chunks, _embeddings_data, _chunk_index, _chunk_ids, _matrix
    if _matrix is not None:
        return

    with open("chunks.json", "r", encoding="utf-8") as f:
        _chunks = json.load(f)

    with open("embeddings.json", "r", encoding="utf-8") as f:
        _embeddings_data = json.load(f)

    # index chunks by chunk_id for fast lookup
    _chunk_index = {c["metadata"]["chunk_id"]: c for c in _chunks}

    # build numpy matrix: shape (N, dims)
    _chunk_ids = [e["chunk_id"] for e in _embeddings_data]
    _matrix = np.array([e["embedding"] for e in _embeddings_data], dtype=np.float32)

    # pre-normalize rows so dot product == cosine similarity
    _norms = np.linalg.norm(_matrix, axis=1, keepdims=True)
    _matrix = _matrix / np.where(_norms == 0, 1, _norms)

    print(f"Retriever ready: {len(_chunks)} chunks, matrix {_matrix.shape}")


# ── Core functions ────────────────────────────────────────────────────

def rewrite_query(question: str) -> list[str]:
    """Use LLM to rephrase the question into 3 search-friendly variants."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": (
                "You are helping improve search over a security policy handbook.\n"
                "Rewrite the question below into 3 different phrasings that capture the same intent "
                "but use different words. Each phrasing should be a short, clear search query.\n"
                "Return one phrasing per line, nothing else.\n\n"
                f"Question: {question}"
            )
        }],
        temperature=0.3,
        max_tokens=150,
    )
    lines = response.choices[0].message.content.strip().splitlines()
    variants = [l.strip() for l in lines if l.strip()]
    # always include the original
    if question not in variants:
        variants.insert(0, question)
    return variants


def _embed(text: str) -> np.ndarray:
    response = client.embeddings.create(model=EMBED_MODEL, input=text)
    vec = np.array(response.data[0].embedding, dtype=np.float32)
    return vec / np.linalg.norm(vec)


def _cosine_search(query_vec: np.ndarray, top_k: int) -> list[tuple[str, float]]:
    scores = _matrix @ query_vec  # cosine similarity for all chunks
    top_indices = np.argpartition(scores, -top_k)[-top_k:]
    top_indices = top_indices[np.argsort(scores[top_indices])[::-1]]
    return [(_chunk_ids[i], float(scores[i])) for i in top_indices]


def retrieve(question: str, top_k: int = 5) -> list[dict]:
    """
    Rewrite question → embed each variant → cosine search → deduplicated top chunks.
    Returns list of chunks with text, metadata, and similarity score.
    """
    _ensure_loaded()
    variants = rewrite_query(question)

    seen: dict[str, float] = {}  # chunk_id → best score

    for variant in variants:
        query_vec = _embed(variant)
        results = _cosine_search(query_vec, top_k)
        for chunk_id, score in results:
            if chunk_id not in seen or score > seen[chunk_id]:
                seen[chunk_id] = score

    # sort by best score, take top_k unique chunks
    ranked = sorted(seen.items(), key=lambda x: x[1], reverse=True)[:top_k]

    output = []
    for chunk_id, score in ranked:
        chunk = _chunk_index.get(chunk_id)
        if chunk:
            output.append({
                "text": chunk["text"],
                "metadata": chunk["metadata"],
                "score": score,
            })

    return output


# ── CLI test ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (or 'quit'): ").strip()
        if question.lower() == "quit":
            break

        print("\nRewriting question...")
        variants = rewrite_query(question)
        print("Variants:")
        for v in variants:
            print(f"  - {v}")

        print("\nTop results:")
        results = retrieve(question, top_k=5)
        for i, r in enumerate(results):
            print(f"\n[{i+1}] score={r['score']:.3f} | {r['metadata']['breadcrumb']}")
            print(f"     summary: {r['metadata']['section_summary']}")
            print(f"     text preview: {r['text'][:150]}...")
