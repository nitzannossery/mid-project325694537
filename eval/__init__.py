"""
Evaluation Module
LLM-as-a-judge evaluation for the retrieval system
"""

from .evaluator import run_evaluation, judge_answer
from .test_queries import TEST_CASES

__all__ = [
    "run_evaluation",
    "judge_answer",
    "TEST_CASES",
]
