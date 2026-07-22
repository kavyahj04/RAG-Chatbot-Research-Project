import json
from openai import OpenAI

from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DIR = BASE_DIR / "json"

load_dotenv(BASE_DIR / ".env", override=True)
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

with open(JSON_DIR / "raw_extraction_200.json", "r", encoding="utf-8") as f:
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

Aim for a final list of roughly 20-30 node types and 25-40 relationship types
total. If your output is much larger than that, you have not merged enough.

Here are worked examples of the kind of merging expected:

Example 1, fold narrow instances into one general category:
Input: ["HAS_KICK_OFF_MEETING", "HAS_WEEKLY_MEETING", "HAS_PAIR_WORK_SESSION",
"HAS_WEEKLY_1_1", "WALKS_THROUGH_PROCESSES", "IDENTIFIES_PAIR_WORK_TOPICS"]
Output: one category, "HAS_RECURRING_ACTIVITY", merged_from all six.
Why: each is a specific instance of "some recurring scheduled interaction",
not a genuinely different kind of relationship.

Example 2, values mistakenly extracted as relationship types:
Input: ["HIGH_PRIORITY_ACCESS_REQUEST", "LOW_PRIORITY_ACCESS_REQUEST",
"HIGH_PRIORITY_DAY_TO_DAY_REQUEST", "LOW_PRIORITY_DAY_TO_DAY_REQUEST",
"PROJECT_FIRE_DRILL"]
Output: one category, "REQUESTS", merged_from all five.
Why: "high priority" / "low priority" / "fire drill" are values describing a
request, not distinct relationships. The distinction belongs in a property,
not the type name.

Example 3, a pair that should NOT merge, despite looking similar:
Input: ["REQUIRES", "DEPENDS_ON"]
Output: two separate categories, unchanged.
Why: REQUIRES is a policy mandate ("remote work requires VPN"), DEPENDS_ON is
a structural/technical dependency ("service A depends on service B"). Similar
surface wording, genuinely different relationship semantics, don't merge just
because two rules exist for narrow cases, keep merging real duplicates and
narrow instances, but preserve real semantic distinctions.

Drop types that are clearly UI-interaction noise, not real graph concepts (e.g.
CLICK, NAVIGATE_TO, ADD_VARIABLE, CHECK-as-a-button-action).

Merge job-title relationship types (ENGINEER, MANAGER, ANALYST, PROGRAM_MANAGER,
ENG_MANAGER, STAFF_ENGINEER) into a single HAS_ROLE relationship, note this
merge explicitly.

Node types found: {json.dumps(raw["node_types"])}
Relationship types found: {json.dumps(raw["relationship_types"])}

For each final category, list which raw labels above got merged into it.
"""

response = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": prompt}],
    response_format=consolidation_schema,
    
)

consolidated = json.loads(response.choices[0].message.content)

with open(JSON_DIR / "consolidated_schema.json", "w", encoding="utf-8") as f:
    json.dump(consolidated, f, indent=2)

print(f"Node types: {len(consolidated['node_types'])} (from {len(raw['node_types'])} raw)")
print(f"Relationship types: {len(consolidated['relationship_types'])} (from {len(raw['relationship_types'])} raw)")