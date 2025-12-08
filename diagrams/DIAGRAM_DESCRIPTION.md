# System Architecture Diagram Description

This document describes the system architecture diagram for the Insurance Claim Timeline Retrieval System.

## Diagram Components

### Boxes (Components)

1. **User** - The end user submitting queries
2. **ManagerAgent (Router)** - Routes queries to appropriate agents
3. **SummarizationAgent** - Handles high-level timeline questions
4. **NeedleAgent** - Handles precise factual questions
5. **SummaryIndex** - Document-level summary index
6. **Hierarchical Index + AutoMergingRetriever** - Multi-level vector index with auto-merging
7. **MCP Tools (DateDiff, RentalCost)** - External computation tools
8. **Judge Model (LLM-as-a-judge)** - Evaluation system

### Arrows (Data Flow)

**Main Query Flow:**
- User → ManagerAgent (User query)
- ManagerAgent → SummarizationAgent (for summary queries) - *"route based on intent"*
- SummarizationAgent → SummaryIndex (retrieve & summarize) - *"high-level summary"*
- ManagerAgent → NeedleAgent (for precise / needle queries) - *"route based on intent"*
- NeedleAgent → Hierarchical Index + AutoMergingRetriever (retrieve nodes) - *"needle search + auto-merging"*
- NeedleAgent ↔ MCP Tools (call tools for dates / costs when needed) - *"tool-augmented reasoning"*
- ManagerAgent → User (final answer back)

**Evaluation Flow (Side Chain):**
- User query + System answer + Gold answer → Judge Model - *"evaluation pipeline"*
- Judge Model → Scores (correctness, relevancy, recall)

## Visual Layout Suggestions

- Place User at the top center
- ManagerAgent in the middle as the central router
- SummarizationAgent and NeedleAgent on left and right sides
- Indices at the bottom
- MCP Tools connected to NeedleAgent
- Evaluation chain on the right side as a separate flow

## Tools for Creating the Diagram

- **draw.io** (https://app.diagrams.net/)
- **Figma** (https://www.figma.com/)
- **Lucidchart**
- **Miro**

Save the final diagram as `agent_diagram.png` in the `diagrams/` directory.
