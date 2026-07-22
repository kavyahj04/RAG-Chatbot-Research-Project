import json
import random

random.seed(42)

RELATIONSHIP_KEYWORDS = [
    "%", "determined as", "determined by", "owned by", "estimated at",
    "responsible for", "approved by", "based on", "leads", "maintained by",
    "requires", "agreed on", "divided by", "map back to"
]

DOMAIN_KEYWORDS = [
    "security department", "product security", "security operations",
    "security assurance", "sirt", "red team", "bug bounty", "gearing ratio",
    "policy exception", "controlled document", "audit logging",
    "threat management", "corpsec", "zendesk", "gitleaks", "pgp", "iscp",
    "disaster recovery", "ransomware", "security shadow", "security culture committee",
    "iam", "rbac", "seoc", "least privilege"
]

ALL_KEYWORDS = RELATIONSHIP_KEYWORDS + DOMAIN_KEYWORDS


def keyword_score(chunk):
    text = chunk["text"].lower()
    return sum(text.count(kw) for kw in ALL_KEYWORDS)


def keywords_in(chunk):
    text = chunk["text"].lower()
    return {kw for kw in ALL_KEYWORDS if kw in text}


with open("chunks.json", "r", encoding="utf-8") as f:
    all_chunks = json.load(f)

eligible = [c for c in all_chunks if c["metadata"].get("token_count", 0) >= 40]

TOTAL = 200
DENSITY_BUDGET = int(TOTAL * 0.5)

sample, picked_ids, covered = [], set(), set()

# 1. set-cover — rarest keywords first, cheapest chunk that covers each one
kw_freq = {kw: sum(1 for c in eligible if kw in c["text"].lower()) for kw in ALL_KEYWORDS}
rarity_order = sorted(ALL_KEYWORDS, key=lambda kw: kw_freq[kw])

for kw in rarity_order:
    if kw in covered:
        continue
    candidates = [
        c for c in eligible
        if c["metadata"]["chunk_id"] not in picked_ids and kw in c["text"].lower()
    ]
    if not candidates:
        continue  # keyword doesn't appear anywhere in the corpus
    best = max(candidates, key=keyword_score)
    sample.append(best)
    picked_ids.add(best["metadata"]["chunk_id"])
    covered |= keywords_in(best)

print(f"Set-cover: {len(sample)} chunks cover {len(covered)}/{len(ALL_KEYWORDS)} keywords")

# 2. density fill — more examples per pattern, not just one
remaining = [c for c in eligible if c["metadata"]["chunk_id"] not in picked_ids]
remaining.sort(key=keyword_score, reverse=True)
density_picks = remaining[:max(0, DENSITY_BUDGET - len(sample))]
sample.extend(density_picks)
picked_ids.update(c["metadata"]["chunk_id"] for c in density_picks)

# 3. random fill — catch schema patterns the keyword list didn't anticipate
remaining_pool = [c for c in all_chunks if c["metadata"]["chunk_id"] not in picked_ids]
sample.extend(random.sample(remaining_pool, TOTAL - len(sample)))

print(f"Final sample size: {len(sample)}")

with open("sample_200.json", "w", encoding="utf-8") as f:
    json.dump(sample, f, indent=2, ensure_ascii=False)
print("Saved sample_200.json")
