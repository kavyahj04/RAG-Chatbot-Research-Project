import json
from collections import Counter
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DIR = BASE_DIR / "json"

load_dotenv(BASE_DIR / ".env", override=True)
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

additional_instructions = """
Follow these patterns, based on this specific handbook:

1. Numbers derived from a formula (e.g. "Bug Bounty Budget is 10% of Cost of
   Compromise") become a relationship between two metric-style nodes. The
   dollar value itself is a "value" property on the node, never its own node.

2. If a named person appears only as a contact or titleholder, extract the
   ROLE as the node, not the person. Roles are stable, people change.

3. Step-by-step instructional text rarely has rich relationships. Extract only
   the system or process and what it requires. Don't force a relationship out
   of every sentence.

4. If the text is a placeholder page with no real content, return empty nodes
   and relationships. Don't invent structure from navigation text.
"""

transformer = LLMGraphTransformer(
    llm=llm,
    node_properties=["value"],
    additional_instructions=additional_instructions,
    # no allowed_nodes / allowed_relationships yet — this pass is discovery only
)
with open(JSON_DIR / "sample_200.json", "r", encoding="utf-8") as f:
    sample = json.load(f)


docs = [
    Document(page_content=c["text"], metadata={"chunk_id": c["metadata"]["chunk_id"]})
    for c in sample  # the 200 chunks from the sampling step
]
graph_documents = transformer.convert_to_graph_documents(docs)

node_type_counts = Counter()
rel_type_counts = Counter()
for gd in graph_documents:
    for node in gd.nodes:
        node_type_counts[node.type] += 1
    for rel in gd.relationships:
        rel_type_counts[rel.type] += 1

print("NODE TYPES")
for t, count in node_type_counts.most_common():
    print(f"{count:>4}  {t}")

print("\nRELATIONSHIP TYPES")
for t, count in rel_type_counts.most_common():
    print(f"{count:>4}  {t}")

# save full detail, not just counts — whoever consolidates this needs to see
# actual node/relationship instances, not just aggregate labels
with open(JSON_DIR / "raw_extraction_200.json", "w", encoding="utf-8") as f:
    json.dump({
        "node_types": dict(node_type_counts),
        "relationship_types": dict(rel_type_counts),
        "nodes": [
            {"id": n.id, "type": n.type, "properties": n.properties,
             "chunk_id": gd.source.metadata["chunk_id"]}
            for gd in graph_documents for n in gd.nodes
        ],
        "relationships": [
            {"source": r.source.id, "type": r.type, "target": r.target.id,
             "chunk_id": gd.source.metadata["chunk_id"]}
            for gd in graph_documents for r in gd.relationships
        ],
    }, f, indent=2)
print("Saved raw_extraction_200.json")