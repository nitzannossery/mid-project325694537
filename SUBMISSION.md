# Insurance Claim Timeline Retrieval System (GenAI + Agents + MCP)

**Author:** Nitzan Nossery

---

## System Overview

This project implements a production-style GenAI retrieval system for an auto insurance claim. The system ingests a multi-page, second-by-second claim timeline and exposes a multi-agent interface:

- A **ManagerAgent** routes each user query.
- A **SummarizationAgent** answers high-level, timeline-oriented questions using a SummaryIndex.
- A **NeedleAgent** answers precise factual questions using a hierarchical RAG index with an AutoMergingRetriever.

## Data & Indexing

The claim is represented as a chronological event log (seconds/minutes resolution) across multiple phases: policy renewal, FNOL, garage inspection, deductible override, rental coverage, invoice and payout, and post-closure analytics. The indexing layer uses hierarchical chunking (small / medium / large) to support both needle retrieval and broader contextual reasoning. A separate SummaryIndex enables fast high-level answers without scanning the full context every time.

## Agent Architecture & MCP Integration

The ManagerAgent classifies queries as summary vs. needle and routes them to the appropriate agent. The NeedleAgent can optionally call MCP-style tools:

- A **DateDiff** tool to compute durations between key events (e.g., accident to closure).
- A **RentalCost** tool to compute rental car cost (days × daily rate).

This demonstrates tool-augmented reasoning: instead of relying only on natural language generation, the model delegates clear numeric tasks to deterministic tools.

## Evaluation (LLM-as-a-Judge)

A separate judge model (LLM-as-a-judge) evaluates the system on 8 test queries. For each query, it receives the user query, the system answer, and a gold reference answer, and returns 1–5 scores for:

- **Answer Correctness**
- **Context Relevancy**
- **Context Recall**

The system achieves near-perfect scores across all metrics, indicating that:

- Routing between agents is appropriate (summary vs. needle).
- The hierarchical RAG setup successfully retrieves the correct details, including subtle "needle" information such as the special deductible override and rental coverage terms.
- The SummaryIndex supports robust high-level explanations of the timeline and financial outcome.

## MCP Usage in One Sentence

In this system, MCP-style tools are used to extend the LLM beyond text-only reasoning by handling precise date and cost computations in a transparent, auditable way.
