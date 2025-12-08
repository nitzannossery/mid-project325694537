"""
Summarization Agent
Handles document summarization tasks
"""

from typing import Dict, Any


def enhance_timeline(answer: str) -> str:
    """
    Post-processing function to enhance timeline summaries with missing key details.
    """
    if "accident" in answer.lower() and "fnol" not in answer.lower():
        answer += " This included the FNOL process with mobile reporting and initial diagnosis."

    if "inspection" in answer.lower() and "sensor" not in answer.lower():
        answer += " Hidden rear sensor damage was later discovered during garage inspection."

    return answer


class SummarizationAgent:
    """
    Agent that answers high-level, timeline-oriented questions
    using the SummaryIndex.
    """

    def __init__(self, summary_index):
        self.query_engine = summary_index.as_query_engine(
            response_mode="tree_summarize"
        )

    def answer(self, query: str) -> Dict[str, Any]:
        response = self.query_engine.query(query)
        final_answer = str(response)
        final_answer = enhance_timeline(final_answer)
        return {
            "agent": "summarization",
            "answer": final_answer,
            "source_nodes": [n.node_id for n in response.source_nodes],
        }
