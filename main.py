"""
Insurance Claim Timeline Retrieval System
Main entry point for the application
Author: NITZAN NOSSERY
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from indexing.index_builder import (
    build_hierarchical_and_summary_indices,
    load_indices,
)
from agents.summarization_agent import SummarizationAgent
from agents.needle_agent import NeedleAgent
from agents.manager_agent import ManagerAgent
from eval.evaluator import run_evaluation


def build_system() -> ManagerAgent:
    hierarchical_index, summary_index, hier_storage = load_indices()
    sum_agent = SummarizationAgent(summary_index)
    needle_agent = NeedleAgent(hierarchical_index, hier_storage)
    manager = ManagerAgent(sum_agent, needle_agent)
    return manager


def demo_queries(manager: ManagerAgent) -> None:
    queries = [
        "Give me a high-level overview of the claim timeline.",
        "What was the special deductible applied in this claim?",
        "How many days passed between the accident and the final claim closure?",
    ]

    for q in queries:
        result = manager.route(q, use_tools=True)
        print(f"\n=== Query: {q}")
        print(f"Routed to: {result['route_type']} ({result['agent']})")
        print("Answer:", result["answer"])
        print("Tool used:", result.get("tool_used"))


if __name__ == "__main__":
    print("🔧 Building indices (first run)...")
    # Build indices once; if already built, this will just overwrite.
    build_hierarchical_and_summary_indices()

    print("\n💬 Demo queries:")
    manager = build_system()
    demo_queries(manager)

    print("\n🧪 Running evaluation:")
    run_evaluation(manager)
