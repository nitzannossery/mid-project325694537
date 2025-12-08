"""
Test Queries Module
Contains test queries for evaluation
"""

TEST_CASES = [
    {
        "id": 1,
        "query": "Give me a high-level overview of the entire claim timeline.",
        "expected_type": "summary",
        "gold_answer": (
            "A summary mentioning policy renewal, the accident on 2024-03-11, "
            "the FNOL process, the garage inspection and hidden sensor damage, "
            "the special deductible reduction, rental car coverage, final invoice, "
            "payout, and claim closure."
        ),
    },
    {
        "id": 2,
        "query": "What was the special deductible applied in this claim?",
        "expected_type": "needle",
        "gold_answer": (
            "A temporarily reduced deductible of 850 ILS for this claim only, "
            "instead of the standard 1,500 ILS."
        ),
    },
    {
        "id": 3,
        "query": "How many days passed between the accident and the final claim closure?",
        "expected_type": "needle",
        "gold_answer": (
            "The accident occurred on 2024-03-11 and the claim was closed on 2024-04-04, "
            "so 24 days passed between them."
        ),
    },
    {
        "id": 4,
        "query": "On which date and approximately what time was the preliminary claim created in the core system?",
        "expected_type": "needle",
        "gold_answer": (
            "The preliminary claim was created on 2024-03-11 at around 14:14, "
            "when the claim status was set to SUBMITTED."
        ),
    },
    {
        "id": 5,
        "query": "Was any bodily injury or medical claim opened for the driver in this incident?",
        "expected_type": "needle",
        "gold_answer": (
            "No separate bodily injury or medical claim was opened. "
            "The driver mentioned mild neck discomfort but declined medical assistance, "
            "and the adjuster explicitly logged that no bodily injury claim should be opened."
        ),
    },
    {
        "id": 6,
        "query": "Was rental car coverage approved, and if so, for how many days and what was the daily limit?",
        "expected_type": "needle",
        "gold_answer": (
            "Yes. Rental car coverage was approved for 5 days with a daily limit "
            "of 200 ILS per day for a compact class vehicle."
        ),
    },
    {
        "id": 7,
        "query": "What was the final payout amount and how was it calculated from the invoice and deductible?",
        "expected_type": "needle",
        "gold_answer": (
            "The final payout was 6,800 ILS, calculated as the final repair invoice "
            "of 7,650 ILS minus the reduced deductible of 850 ILS."
        ),
    },
    {
        "id": 8,
        "query": "Explain the special deductible override: why was it applied and what was its scope.",
        "expected_type": "summary",
        "gold_answer": (
            "The deductible was reduced from the standard 1,500 ILS to 850 ILS as a loyalty "
            "retention benefit because the policy holder had long-term continuous coverage "
            "with no at-fault accidents. The override was explicitly limited to this single "
            "claim only and was not applied to future claims or the policy as a whole."
        ),
    },
]
