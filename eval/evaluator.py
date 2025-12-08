"""
Evaluator Module
LLM-as-a-judge evaluation system
"""

import json
from typing import Dict, Any, List

from llama_index.llms.openai import OpenAI

from eval.test_queries import TEST_CASES
from agents.manager_agent import ManagerAgent


def get_judge_llm():
    """
    Separate OpenAI model used as judge.
    """
    return OpenAI(model="gpt-4o-mini")


JUDGE_PROMPT = """You are an evaluation agent for an insurance claim RAG system.

You will receive:
- user_query
- system_answer
- gold_answer (reference)

Evaluate on a 1-5 scale:
A. Answer Correctness
B. Context Relevancy
C. Context Recall (did the system likely use the right part of the document?)

Return ONLY a valid JSON object in this format:

{
  "correctness": <int>,
  "relevancy": <int>,
  "recall": <int>,
  "comments": "<short explanation>"
}
"""


def judge_answer(
    test_case: Dict[str, Any],
    system_answer: str,
    judge_llm: OpenAI,
) -> Dict[str, Any]:
    user_query = test_case["query"]
    gold_answer = test_case["gold_answer"]

    prompt = (
        JUDGE_PROMPT
        + "\n\nuser_query: "
        + user_query
        + "\nsystem_answer: "
        + system_answer
        + "\ngold_answer: "
        + gold_answer
        + "\n"
    )

    resp = judge_llm.complete(prompt)
    text = resp.text if hasattr(resp, "text") else str(resp)

    try:
        result = json.loads(text)
    except Exception:
        result = {
            "correctness": 0,
            "relevancy": 0,
            "recall": 0,
            "comments": f"Failed to parse judge response: {text}",
        }
    return result


def run_evaluation(manager: ManagerAgent) -> List[Dict[str, Any]]:
    judge_llm = get_judge_llm()
    results: List[Dict[str, Any]] = []

    for case in TEST_CASES:
        routed = manager.route(case["query"], use_tools=True)
        judge = judge_answer(case, routed["answer"], judge_llm)

        result = {
            "id": case["id"],
            "query": case["query"],
            "route_type": routed["route_type"],
            "agent": routed["agent"],
            "judge": judge,
        }
        results.append(result)

    # Print summary
    if results:
        avg_correct = sum(r["judge"]["correctness"] for r in results) / len(results)
        avg_relev = sum(r["judge"]["relevancy"] for r in results) / len(results)
        avg_recall = sum(r["judge"]["recall"] for r in results) / len(results)
    else:
        avg_correct = avg_relev = avg_recall = 0.0

    print("\n=== EVALUATION SUMMARY ===")
    print("Avg Correctness:", avg_correct)
    print("Avg Relevancy:", avg_relev)
    print("Avg Recall:", avg_recall)

    for r in results:
        print(f"\n### Test {r['id']}: {r['query']}")
        print(f"Route: {r['route_type']} ({r['agent']})")
        print("Judge:", r["judge"])

    return results
