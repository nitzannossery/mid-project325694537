"""
Manager Agent
Orchestrates multiple agents for complex tasks
"""

from dataclasses import dataclass
from typing import Literal, Dict, Any


@dataclass
class ManagerAgent:
    """
    Manager/Router agent.

    - Receives user query.
    - Classifies it as "summary" vs "needle".
    - Routes to SummarizationAgent or NeedleAgent.
    """

    summarization_agent: Any
    needle_agent: Any

    def classify_query(self, query: str) -> Literal["summary", "needle"]:
        q = query.lower()

        summary_keywords = ["overview", "timeline", "summary", "high-level"]
        needle_keywords = [
            "exact",
            "specific",
            "deductible",
            "how much",
            "amount",
            "date",
            "days",
        ]

        if any(k in q for k in needle_keywords):
            return "needle"
        if any(k in q for k in summary_keywords):
            return "summary"

        # default: needle, because the dataset is small and factual
        return "needle"

    def route(self, query: str, use_tools: bool = True) -> Dict[str, Any]:
        route_type = self.classify_query(query)

        if route_type == "summary":
            result = self.summarization_agent.answer(query)
        else:
            # needle agent can choose to use tools or not
            if use_tools:
                result = self.needle_agent.answer_with_tools(query)
            else:
                result = self.needle_agent.answer(query)

        result["route_type"] = route_type
        return result
