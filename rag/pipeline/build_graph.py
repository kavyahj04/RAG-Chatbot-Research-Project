import json
import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document

load_dotenv(override=True)

JSON_DIR = Path(__file__).parent.parent / "json"

with open(JSON_DIR / "consolidated_schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)

allowed_nodes = [n["name"] for n in schema["node_types"]]
allowed_relationships = [r["name"] for r in schema["relationship_types"]]
print(f"Frozen schema: {len(allowed_nodes)} node types, {len(allowed_relationships)} relationship types")

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

additional_instructions = """
Follow these patterns, based on this specific handbook:

1. Numbers derived from a formula (e.g. "Bug Bounty Budget is 10% of Cost of
   Compromise") become a DERIVED_FROM relationship between two metric-style
   nodes. The dollar value itself is a "value" property on the node, never
   its own node.

2. If a named person appears only as a contact or titleholder, extract the
   ROLE as the node, not the person's name. Roles are stable, people change.

3. Job titles (Engineer, Manager, Analyst, DRI) must be Role entities
   connected via HAS_ROLE. Never make the job title itself a relationship
   type. (The frozen schema already blocks this structurally since job
   titles aren't in allowed_relationships, this instruction is a second
   layer, not the only one.)

4. Step-by-step instructional text rarely has rich relationships. Extract
   only the system or process and what it REQUIRES.

5. Never extract UI actions (click, navigate to, add a field, check a box)
   as relationships or entities. These come from step-by-step screenshots
   and don't belong in a policy knowledge graph.

6. If the text is a placeholder page with no real content, return empty
   nodes and relationships. Don't invent structure from navigation text.
"""

transformer = LLMGraphTransformer(
    llm=llm,
    allowed_nodes=allowed_nodes,
    allowed_relationships=allowed_relationships,
    node_properties=["value"],
    additional_instructions=additional_instructions,
    strict_mode=False,
)

with open(JSON_DIR / "chunks.json", "r", encoding="utf-8") as f:
    all_chunks = json.load(f)
print(f"Total chunks: {len(all_chunks)}")

OUTPUT_PATH = JSON_DIR / "graph_documents_full.jsonl"
done_ids = set()
if Path(OUTPUT_PATH).exists():
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            done_ids.add(json.loads(line)["chunk_id"])
    print(f"Resuming: {len(done_ids)} already done, skipping those")

remaining = [c for c in all_chunks if c["metadata"]["chunk_id"] not in done_ids]
print(f"Remaining: {len(remaining)}")

BATCH_SIZE = 50

with open(JSON_DIR / OUTPUT_PATH, "a", encoding="utf-8") as out_f:
    for i in range(0, len(remaining), BATCH_SIZE):
        batch = remaining[i:i + BATCH_SIZE]
        docs = [
            Document(page_content=c["text"], metadata={"chunk_id": c["metadata"]["chunk_id"]})
            for c in batch
        ]
        try:
            graph_documents = transformer.convert_to_graph_documents(docs)
        except Exception as e:
            print(f"Batch at {i} failed: {e}")
            print("Everything before this batch is already saved. Rerun this script to resume.")
            raise

        for gd in graph_documents:
            record = {
                "chunk_id": gd.source.metadata["chunk_id"],
                "nodes": [{"id": n.id, "type": n.type, "properties": n.properties} for n in gd.nodes],
                "relationships": [
                    {"source": r.source.id, "type": r.type, "target": r.target.id}
                    for r in gd.relationships
                ],
            }
            out_f.write(json.dumps(record) + "\n")
        out_f.flush()
        print(f"Progress: {min(i + BATCH_SIZE, len(remaining)) + len(done_ids)}/{len(all_chunks)}")

print("Done:", OUTPUT_PATH)