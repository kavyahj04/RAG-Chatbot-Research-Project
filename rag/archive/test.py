import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DIR = BASE_DIR / "json"

with open(JSON_DIR / "consolidated_schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)

for rel in schema["relationship_types"]:
    if rel["name"] == "HAS_ATTRIBUTE":
        pull_out = ["ESTIMATED_AT", "DETERMINED_AS", "BASED_ON"]
        rel["merged_from"] = [x for x in rel["merged_from"] if x not in pull_out]
        schema["relationship_types"].append({
            "name": "DERIVED_FROM",
            "merged_from": pull_out
        })
        break

with open(JSON_DIR / "consolidated_schema.json", "w", encoding="utf-8") as f:
    json.dump(schema, f, indent=2)