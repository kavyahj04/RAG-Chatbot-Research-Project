"""
Evaluate the RAG system against qa_dataset.json using LLM-as-judge.

Scoring per question (1-3):
  3 = Correct and complete
  2 = Partially correct / missing some details
  1 = Incorrect or not found

Run:   python3 evaluation.py
Debug: python3 evaluation.py --debug
"""

import json
import sys
import time
from dotenv import load_dotenv
from openai import OpenAI
from query import answer as rag_answer

load_dotenv(override=True)
client = OpenAI()

QA_PATH     = "qa_dataset.json"
RESULTS_PATH = "eval_results.json"
DEBUG = "--debug" in sys.argv


# ── LLM judge ────────────────────────────────────────────────────────

def judge(question: str, expected: str, actual: str) -> dict:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": (
                "You are evaluating a RAG chatbot's answer against an expected answer.\n\n"
                f"Question: {question}\n\n"
                f"Expected answer:\n{expected}\n\n"
                f"RAG system answer:\n{actual}\n\n"
                "Score the RAG answer on a scale of 1-3:\n"
                "  3 = Correct and complete — covers all key points in the expected answer\n"
                "  2 = Partially correct — gets the main idea but misses details or has minor errors\n"
                "  1 = Incorrect or not found — wrong, irrelevant, or says it could not find the information\n\n"
                "Respond in JSON:\n"
                '{"score": <1|2|3>, "reason": "<one sentence>"}'
            )
        }],
        temperature=0,
        max_tokens=150,
        response_format={"type": "json_object"},
    )
    return json.loads(resp.choices[0].message.content)


# ── Run evaluation ────────────────────────────────────────────────────

with open(QA_PATH) as f:
    dataset = json.load(f)

pairs = dataset["pairs"]
print(f"Evaluating {len(pairs)} questions ({dataset['single_hop']} single-hop, "
      f"{dataset['multi_hop']} multi-hop, {dataset['example_based']} example-based)\n")

results = []
scores_by_type = {"single_hop": [], "multi_hop": [], "example_based": []}

for i, pair in enumerate(pairs):
    q   = pair["question"]
    exp = pair["expected_answer"]
    qtype = pair["type"]

    print(f"[{i+1}/{len(pairs)}] [{qtype}] {q[:70]}...")

    # run RAG
    try:
        rag_result = rag_answer(q)
        actual = rag_result["answer"]
        sources = rag_result.get("sources", [])
    except Exception as e:
        actual = f"ERROR: {e}"
        sources = []

    # judge
    try:
        verdict = judge(q, exp, actual)
        score  = verdict["score"]
        reason = verdict["reason"]
    except Exception as e:
        score  = 0
        reason = f"Judge error: {e}"

    label = {3: "✅ CORRECT", 2: "⚠️  PARTIAL", 1: "❌ WRONG"}.get(score, "?")
    print(f"  {label} (score={score}) — {reason}")

    if DEBUG:
        print(f"  Expected: {exp[:120]}")
        print(f"  Got:      {actual[:120]}")
        print(f"  Sources:  {[s['breadcrumb'] for s in sources[:3]]}")
    print()

    result = {
        "id": i + 1,
        "type": qtype,
        "question": q,
        "expected_answer": exp,
        "rag_answer": actual,
        "score": score,
        "reason": reason,
        "breadcrumbs": pair.get("breadcrumbs", []),
        "sources_returned": [s["breadcrumb"] for s in sources[:5]],
    }
    results.append(result)
    scores_by_type[qtype].append(score)

    time.sleep(0.3)


# ── Summary ───────────────────────────────────────────────────────────

def avg(lst):
    return round(sum(lst) / len(lst), 2) if lst else 0

def pct_correct(lst):
    return round(sum(1 for s in lst if s == 3) / len(lst) * 100, 1) if lst else 0

def pct_partial_plus(lst):
    return round(sum(1 for s in lst if s >= 2) / len(lst) * 100, 1) if lst else 0

all_scores = [r["score"] for r in results]

print("=" * 60)
print("EVALUATION SUMMARY")
print("=" * 60)
print(f"Total questions : {len(results)}")
print(f"Overall avg score : {avg(all_scores)} / 3")
print(f"Fully correct (3) : {pct_correct(all_scores)}%")
print(f"Correct or partial (≥2): {pct_partial_plus(all_scores)}%")
print()

for qtype, scores in scores_by_type.items():
    if not scores:
        continue
    label = qtype.replace("_", " ").title()
    print(f"{label} ({len(scores)} questions)")
    print(f"  Avg score      : {avg(scores)} / 3")
    print(f"  Fully correct  : {pct_correct(scores)}%")
    print(f"  Correct/partial: {pct_partial_plus(scores)}%")
    print()

# worst performers
failures = [r for r in results if r["score"] == 1]
if failures:
    print(f"Failed questions ({len(failures)}):")
    for r in failures:
        print(f"  [{r['type']}] {r['question'][:70]}")
        print(f"    Reason: {r['reason']}")
    print()

# ── Save results ──────────────────────────────────────────────────────

output = {
    "summary": {
        "total": len(results),
        "avg_score": avg(all_scores),
        "pct_correct": pct_correct(all_scores),
        "pct_partial_plus": pct_partial_plus(all_scores),
        "by_type": {
            qtype: {
                "count": len(scores),
                "avg_score": avg(scores),
                "pct_correct": pct_correct(scores),
                "pct_partial_plus": pct_partial_plus(scores),
            }
            for qtype, scores in scores_by_type.items()
            if scores
        },
    },
    "results": results,
}

with open(RESULTS_PATH, "w") as f:
    json.dump(output, f, indent=2)

print(f"Full results saved to {RESULTS_PATH}")
