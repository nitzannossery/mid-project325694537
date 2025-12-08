"""
Index Builder Module
Handles data segmentation and indexing (summary index + hierarchical chunk index)
"""

import os
from pathlib import Path

from llama_index.core import (
    Document,
    VectorStoreIndex,
    SummaryIndex,
    StorageContext,
)
from llama_index.core.node_parser import HierarchicalNodeParser, SentenceSplitter
from llama_index.core.indices import load_index_from_storage
from llama_index.llms.openai import OpenAI

DATA_PATH = Path("data/claim_timeline.txt")

HIER_STORAGE_DIR = Path("storage/hierarchical")
SUM_STORAGE_DIR = Path("storage/summary")


def get_llm():
    """
    Return an OpenAI LLM for use with LlamaIndex.
    Assumes OPENAI_API_KEY is set in the environment.
    """
    return OpenAI(model="gpt-4o-mini")


def load_raw_document() -> Document:
    text = DATA_PATH.read_text(encoding="utf-8")
    return Document(
        text=text,
        metadata={
            "claim_id": "CLM-2024-0193",
            "source": "synthetic_midterm_dataset",
        },
    )


def build_hierarchical_and_summary_indices() -> None:
    """
    Build:
    - Hierarchical vector index over the claim timeline.
    - Summary index using MapReduce-style summarization.

    Chunking strategy:
    - HierarchicalNodeParser with chunk_sizes [200, 500, 1200]
      (small / medium / large).
    """
    llm = get_llm()
    doc = load_raw_document()

    # Base splitter (mainly for potential map/reduce usage)
    _base_splitter = SentenceSplitter(
        chunk_size=200,
        chunk_overlap=40,
    )

    # Hierarchical parser: small / medium / large chunks
    node_parser = HierarchicalNodeParser.from_defaults(
        chunk_sizes=[200, 500, 1200]
    )
    nodes = node_parser.get_nodes_from_documents([doc])

    # --- Build hierarchical vector index ---
    hier_storage = StorageContext.from_defaults()
    hier_index = VectorStoreIndex(
        nodes,
        storage_context=hier_storage,
        llm=llm,
    )
    hier_index.set_index_id("hierarchical_index")

    HIER_STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    hier_storage.persist(persist_dir=str(HIER_STORAGE_DIR))

    # --- Build summary index (document-level summaries) ---
    sum_storage = StorageContext.from_defaults()
    summary_index = SummaryIndex.from_documents(
        [doc],
        storage_context=sum_storage,
        llm=llm,
    )
    summary_index.set_index_id("summary_index")

    SUM_STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    sum_storage.persist(persist_dir=str(SUM_STORAGE_DIR))

    print("✅ Indices built and persisted.")


def load_indices():
    """
    Load previously built hierarchical and summary indices.
    Returns: (hierarchical_index, summary_index, hier_storage)
    """
    llm = get_llm()

    hier_storage = StorageContext.from_defaults(
        persist_dir=str(HIER_STORAGE_DIR)
    )
    sum_storage = StorageContext.from_defaults(
        persist_dir=str(SUM_STORAGE_DIR)
    )

    hierarchical_index = load_index_from_storage(
        storage_context=hier_storage,
        index_id="hierarchical_index",
    )
    hierarchical_index._llm = llm  # ensure LLM is set

    summary_index = load_index_from_storage(
        storage_context=sum_storage,
        index_id="summary_index",
    )
    summary_index._llm = llm

    return hierarchical_index, summary_index, hier_storage


if __name__ == "__main__":
    build_hierarchical_and_summary_indices()
