import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
client = OpenAI()
EMBED_MODEL = "text-embedding-3-large"
BATCH_SIZE = 100
MAX_EMBED_TOKENS = 8000


with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

    print(f"Loaded {len(chunks)} chunks")

    MAX_EMBED_TOKENS = 8000
    skipped = [c for c in chunks if c["metadata"]["token_count"] > MAX_EMBED_TOKENS]
    chunks = [c for c in chunks if c["metadata"]["token_count"] <= MAX_EMBED_TOKENS]

    print(f"Skipping {len(skipped)} chunks over {MAX_EMBED_TOKENS} tokens:")
    for c in skipped:
        print(f"  - {c['metadata']['chunk_id']} ({c['metadata']['token_count']} tokens)")



def embed_batch(texts):
    response = client.embeddings.create(model=EMBED_MODEL, input=texts)
    return [item.embedding for item in response.data]


embeddings_data = []
for i in range(0, len(chunks), BATCH_SIZE):
    batch = chunks[i:i + BATCH_SIZE]
    texts = [c["text"] for c in batch]
    vectors = embed_batch(texts)
    for chunk, vector in zip(batch, vectors):
        embeddings_data.append({
            "chunk_id": chunk["metadata"]["chunk_id"],
            "embedding": vector
        })
    print(f"Embedded {min(i+BATCH_SIZE, len(chunks))}/{len(chunks)}")

with open("embeddings.json", "w", encoding="utf-8") as f:
    json.dump(embeddings_data, f)

print("Saved embeddings.json")
