import json
from openai import OpenAI

client = OpenAI()

with open("raw_extraction_200.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

consolidation_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "schema_consolidation",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "node_types": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "merged_from": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": ["name", "merged_from"],
                        "additionalProperties": False,
                    },
                },
                "relationship_types": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "merged_from": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": ["name", "merged_from"],
                        "additionalProperties": False,
                    },
                },
            },
            "required": ["node_types", "relationship_types"],
            "additionalProperties": False,
        },
    },
}

prompt = f"""These node and relationship type labels were extracted from a security policy handbook.

Merge near-duplicates that refer to the same real category (e.g. "Environment_variable"
and "Environment variable", "Requirement" and "System requirement").

Drop types that are clearly UI-interaction noise, not real graph concepts (e.g.
CLICK, NAVIGATE_TO, ADD_VARIABLE, CHECK).

Merge job-title relationship types (ENGINEER, MANAGER, ANALYST, PROGRAM_MANAGER,
ENG_MANAGER, STAFF_ENGINEER) into a single HAS_ROLE relationship, and note this
merge explicitly.

Keep genuinely distinct categories separate even if related.

Node types found: {json.dumps(raw["node_types"])}
Relationship types found: {json.dumps(raw["relationship_types"])}

For each final category, list which raw labels above got merged into it.
"""

response = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": prompt}],
    response_format=consolidation_schema,
    temperature=0,
)

consolidated = json.loads(response.choices[0].message.content)

with open("consolidated_schema.json", "w", encoding="utf-8") as f:
    json.dump(consolidated, f, indent=2)

print(f"Node types: {len(consolidated['node_types'])} (from {len(raw['node_types'])} raw)")
print(f"Relationship types: {len(consolidated['relationship_types'])} (from {len(raw['relationship_types'])} raw)")