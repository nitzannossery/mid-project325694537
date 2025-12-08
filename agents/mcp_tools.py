"""
MCP Tools Module
MCP-style tool integration for the insurance claim system
"""

from datetime import datetime


class MCPDateTool:
    """
    Simple MCP-style tool that computes date differences in days.
    In a real MCP setup, this would be registered as an external tool.
    """

    @staticmethod
    def date_diff_days(start: str, end: str) -> int:
        """
        start/end format: YYYY-MM-DD
        """
        d1 = datetime.strptime(start, "%Y-%m-%d")
        d2 = datetime.strptime(end, "%Y-%m-%d")
        return (d2 - d1).days


class MCPCostTool:
    """
    Simple MCP-style tool that computes total rental cost.
    """

    @staticmethod
    def compute_rental_cost(days: int, daily_rate: float) -> float:
        return days * daily_rate
