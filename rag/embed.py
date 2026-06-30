import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
from pathlib import Path
import tiktoken

load_dotenv(override=True)

openai = OpenAI()
tokenizer = tiktoken.get_encoding("cl100k_base")

MAX_TOKENS = 8192

def truncate_to_token_limit(text: str, max_tokens: int = MAX_TOKENS) -> str:
    tokens = tokenizer.encode(text)
    if len(tokens) <= max_tokens:
        return text
    return tokenizer.decode(tokens[:max_tokens])

with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Loaded {len(chunks)} chunks")

# setup chromadb — stores data locally in a folder called chroma_db
client = chromadb.PersistentClient(path = "chroma_db")

collection = client.get_or_create_collection(
    name = "security_handbook",
    metadata = {"hnsw:space": "cosine"}  # use cosine similarity for search
)

print(f"Collection ready: {collection.name}")

# temporary test
print(f"Chunks in collection: {collection.count()}")

def embed_and_store(chunks, collection, batch_size=100):
    already_stored = collection.count()

    if already_stored:
        print(f"Resuming from {already_stored}")
    
    chunks_to_process = chunks[already_stored:]

    print(f"Embedding {len(chunks_to_process)} chunks...")

    for i in range(0, len(chunks_to_process), batch_size):
        batch = chunks_to_process[i : i + batch_size]

        texts_to_embed = []

        for chunk in batch:
            combined = f"{chunk['metadata']['breadcrumb']}\n{chunk['metadata']['section_summary']}\n{chunk['text']}"
            texts_to_embed.append(truncate_to_token_limit(combined))

        response = openai.embeddings.create(
            input=texts_to_embed,
            model="text-embedding-3-large"
        )

        embeddings = [item.embedding for item in response.data]

        # prepare data for chromadb
        ids = [chunk["metadata"]["chunk_id"] for chunk in batch]
        documents = [chunk["text"] for chunk in batch]
        metadatas = [chunk["metadata"] for chunk in batch]
        
        # store in chromadb
        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )
        
        print(f"  Stored {already_stored + i + len(batch)}/{len(chunks)} chunks")
    
    print(f"\nDone. Total chunks in collection: {collection.count()}")

if __name__ == "__main__":
    embed_and_store(chunks, collection)