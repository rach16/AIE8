"""Toolbelt assembly for agents.

Collects third-party tools and local tools (like RAG) into a single list that
graphs can bind to their language models.
"""
from __future__ import annotations

from typing import List
import os

from langchain_tavily import TavilySearch
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from app.rag import retrieve_information


def get_tool_belt() -> List:
    """Return the list of tools available to agents (Tavily, Arxiv, RAG).

    Set env TOOLBELT_ONLY_RAG=true to expose only the PDF RAG tool.
    """
    only_rag = os.getenv("TOOLBELT_ONLY_RAG", "false").lower() in {"1", "true", "yes"}
    if only_rag:
        return [retrieve_information]

    tavily_tool = TavilySearch(max_results=5)
    return [tavily_tool, ArxivQueryRun(), retrieve_information]
