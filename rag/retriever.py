import json
import numpy as np 
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv(override = True)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()
EMBED_MODEL = "text-embedding-3-large"

with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

with open("embeddings.json","r", encoding = "utf-8") as f:
    embeddings = json.load(f)

chunk_index = {c["metadata"]["chunk_id"]:c for c in chunks}
chunk_ids = [e["chunk_id"] for e in embeddings]

matrix = np.array([e["embedding"] for e in embeddings], dtype = np.float32)

norms = np.linalg.norm(matrix, axis=1, keepdims= True)
matrix = matrix / np.where(norms == 0, 1, norms)


def embed_query(text):
    response = client.embeddings.create(model=EMBED_MODEL, input = text)
    vector = np.array(response.data[0].embedding, dtype = np.float32)
    return vector/np.linalg.norm(vector)

def search(query, top_k= 5):
    query_vec = embed_query(query)
    scores = matrix @ query_vec

    top_indices = np.argpartition(scores, -top_k)[-top_k:]

    top_indices = top_indices[np.argsort(scores[top_indices])[::-1]]

    result = []

    for i in top_indices:
        chunk_id = chunk_ids[i]
        chunk = chunk_index[chunk_id]
        result.append({
            "text":chunk["text"],
            "metadata" : chunk["metadata"],
            "score": float(scores[i])
        })
    return result

if __name__ == "__main__":
    results = search("what is the vulnerability disclosure process?", top_k=3)
    for r in results:
        print(f"\nscore={r['score']:.3f} | {r['metadata']['breadcrumb']}")
        print(r["text"][:200])

