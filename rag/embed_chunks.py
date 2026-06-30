import json
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

client = OpenAI()

CHUNKS_PATH = "chunks.json"
BATCH_SIZE = 500  # OpenAI allows up to 2048, 500 is safe
EMBED_MODEL = "text-embedding-3-small"


def get_text_to_embed(chunk: dict) -> str:
    summary = chunk["metadata"].get("section_summary", "").strip()
    if summary:
        return summary
    # fall back to breadcrumb for chunks with no summary
    return chunk["metadata"].get("breadcrumb", "")


def embed_batch(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=texts,
    )
    return [item.embedding for item in response.data]


def main():
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    print(f"Total chunks: {len(chunks)}")

    # find chunks that still need embeddings
    to_embed = [(i, chunk) for i, chunk in enumerate(chunks) if "embedding" not in chunk]
    print(f"Chunks needing embeddings: {len(to_embed)}")

    if not to_embed:
        print("All chunks already have embeddings.")
        return

    total_batches = (len(to_embed) + BATCH_SIZE - 1) // BATCH_SIZE

    for batch_num in range(total_batches):
        batch = to_embed[batch_num * BATCH_SIZE : (batch_num + 1) * BATCH_SIZE]
        indices = [i for i, _ in batch]
        texts = [get_text_to_embed(chunk) for _, chunk in batch]

        print(f"Batch {batch_num + 1}/{total_batches} — {len(texts)} chunks...", end=" ", flush=True)

        embeddings = embed_batch(texts)

        for idx, embedding in zip(indices, embeddings):
            chunks[idx]["embedding"] = embedding

        print("done")

        # save after every batch so we can resume if interrupted
        with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
            json.dump(chunks, f)

        if batch_num < total_batches - 1:
            time.sleep(0.5)

    print(f"\nFinished. All {len(chunks)} chunks now have embeddings saved to {CHUNKS_PATH}")


if __name__ == "__main__":
    main()
