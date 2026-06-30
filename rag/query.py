import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
import pickle
import networkx as nx
from retriever import rewrite_query

with open("graph.pkl", "rb") as f:
    G = pickle.load(f)


load_dotenv(override=True)

openai = OpenAI()

# connect to existing chromadb — don't recreate, just load
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("security_handbook")

print(f"Connected to collection with {collection.count()} chunks")

def search(query, n_results=5):
    # embed the user's question using same model as indexing
    response = openai.embeddings.create(
        input=query,
        model="text-embedding-3-large"
    )
    
    query_vector = response.data[0].embedding
    
    # search chromadb for similar chunks
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )
    
    # format results cleanly
    chunks = []
    for i in range(len(results["ids"][0])):
        chunks.append({
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })
    
    return chunks

def expand_with_graph(vector_results, max_chunks=15):
    # priority order for edge types
    edge_priority = {
        "references": 1,      # explicitly linked — most meaningful
        "parent_of": 2,       # broader context
        "child_of": 2,        # more specific context
        "next_section": 3,    # sequential — least priority
        "prev_section": 3
    }

    # track all collected chunks with their priority score
    # lower score = higher priority
    collected = {}

    # step 1 — add vector search results first (highest priority)
    for i, chunk in enumerate(vector_results):
        chunk_id = chunk["metadata"]["chunk_id"]
        collected[chunk_id] = {
            "text": chunk["text"],
            "metadata": chunk["metadata"],
            "score": chunk["distance"],  # distance from vector search
            "hop": 0                     # 0 = direct vector result
        }

    # step 2 — expand each entry point via graph
    for chunk in vector_results:
        chunk_id = chunk["metadata"]["chunk_id"]

        # check if this node exists in graph
        if chunk_id not in G:
            continue

        # 1 hop — direct neighbors
        for neighbor_id, edge_data in G[chunk_id].items():
            relationship = edge_data.get("relationship", "")
            priority = edge_priority.get(relationship, 3)

            if neighbor_id not in collected:
                collected[neighbor_id] = {
                    "text": None,       # fetch later from chromadb
                    "metadata": None,
                    "score": chunk["distance"] + (priority * 0.1),
                    "hop": 1
                }

        # 2 hops — neighbors of neighbors
        for neighbor_id in list(G[chunk_id].keys()):
            if neighbor_id not in G:
                continue

            for second_neighbor_id, edge_data in G[neighbor_id].items():
                relationship = edge_data.get("relationship", "")
                priority = edge_priority.get(relationship, 3)

                if second_neighbor_id not in collected:
                    collected[second_neighbor_id] = {
                        "text": None,
                        "metadata": None,
                        "score": chunk["distance"] + (priority * 0.2),
                        "hop": 2
                    }

    # step 3 — sort by score and cap at max_chunks
    sorted_chunks = sorted(collected.items(), key=lambda x: x[1]["score"])
    top_chunks = sorted_chunks[:max_chunks]

    # step 4 — fetch text for graph-expanded chunks from chromadb
    final_chunks = []
    ids_to_fetch = [
        chunk_id for chunk_id, data in top_chunks
        if data["text"] is None
    ]

    if ids_to_fetch:
        results = collection.get(
            ids=ids_to_fetch,
            include=["documents", "metadatas"]
        )
        
        # build lookup for fetched results
        fetched = {}
        for i, chunk_id in enumerate(results["ids"]):
            fetched[chunk_id] = {
                "text": results["documents"][i],
                "metadata": results["metadatas"][i]
            }
    else:
        fetched = {}

    # step 5 — build final list
    for chunk_id, data in top_chunks:
        if data["text"] is not None:
            # already have text from vector search
            final_chunks.append({
                "text": data["text"],
                "metadata": data["metadata"],
                "score": data["score"],
                "hop": data["hop"]
            })
        elif chunk_id in fetched:
            # text fetched from chromadb
            final_chunks.append({
                "text": fetched[chunk_id]["text"],
                "metadata": fetched[chunk_id]["metadata"],
                "score": data["score"],
                "hop": data["hop"]
            })

    return final_chunks

def decompose_query(query):
    """Use LLM to split a compound question into individual sub-questions."""
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": (
                "Split this question into individual sub-questions if it contains multiple distinct topics. "
                "Return one sub-question per line, nothing else. "
                "If it's already a single question, return it as-is.\n\n"
                f"Question: {query}"
            )
        }],
        temperature=0
    )
    lines = response.choices[0].message.content.strip().splitlines()
    return [l.strip() for l in lines if l.strip()]


def answer(query, n_results=5):
    # step 1 — rewrite question into clear search-friendly variants (also handles compound questions)
    sub_queries = rewrite_query(query)

    seen_ids = set()
    all_retrieved = []
    for sub_query in sub_queries:
        for chunk in search(sub_query, n_results):
            cid = chunk["metadata"]["chunk_id"]
            if cid not in seen_ids:
                seen_ids.add(cid)
                all_retrieved.append(chunk)

    # step 2 — expand with knowledge graph
    expanded = expand_with_graph(all_retrieved, max_chunks=25)

    # step 3 — build context from expanded chunks
    context = ""
    for i, chunk in enumerate(expanded):
        context += f"""
Source {i+1}: {chunk['metadata']['breadcrumb']}
URL: {chunk['metadata']['url']}
{chunk['text']}
---
"""

    # step 4 — generate answer
    prompt = f"""You are a helpful security policy assistant.
Answer the employee's question using the provided policy excerpts below.
- Answer each part of the question separately if there are multiple parts.
- For each part you can answer, cite which policy section it comes from.
- If the excerpts contain closely related information (e.g. "Helpdesk Support Analyst" when asked about "Support Analyst"), use that information to answer — do not reject it just because the exact term differs.
- Only say "I could not find [that specific topic]" if the excerpts contain truly nothing relevant to that part of the question.
- Never refuse to answer a part you do have information about.

Policy excerpts:
{context}

Employee question: {query}

Answer:"""

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return {
        "answer": response.choices[0].message.content.strip(),
        "sources": [
            {
                "breadcrumb": chunk["metadata"]["breadcrumb"],
                "url": chunk["metadata"]["url"],
                "hop": chunk["hop"]
            }
            for chunk in expanded
        ]
    }

if __name__ == "__main__":
    debug = "--debug" in __import__("sys").argv

    while True:
        query = input("\nAsk a security question (or 'quit'): ")
        if query.lower() == "quit":
            break

        result = answer(query)

        if debug:
            print("\n--- DEBUG: chunk texts sent to LLM ---")
            sub_queries = rewrite_query(query)
            print(f"Rewritten queries: {sub_queries}")
            seen = set()
            retrieved = []
            for sq in sub_queries:
                for c in search(sq, 5):
                    if c["metadata"]["chunk_id"] not in seen:
                        seen.add(c["metadata"]["chunk_id"])
                        retrieved.append(c)
            expanded = expand_with_graph(retrieved, 25)
            for i, chunk in enumerate(expanded):
                hop_label = "direct" if chunk["hop"] == 0 else f"hop {chunk['hop']}"
                print(f"\n[{hop_label}] {chunk['metadata']['breadcrumb']}")
                print(chunk["text"][:300])
            print("--- END DEBUG ---\n")

        print("\nANSWER:")
        print(result["answer"])

        print("\nSOURCES:")
        for source in result["sources"]:
            hop_label = "direct" if source["hop"] == 0 else f"hop {source['hop']}"
            print(f"- [{hop_label}] {source['breadcrumb']}")
            print(f"  {source['url']}")