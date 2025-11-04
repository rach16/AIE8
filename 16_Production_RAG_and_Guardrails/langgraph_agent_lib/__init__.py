"""LangGraph Agent Library

A library for LangGraph agents with caching, monitoring, and agent integration.
"""

from .agents import create_langgraph_agent
from .caching import CacheBackedEmbeddings, setup_llm_cache
from .rag import ProductionRAGChain
from .models import get_openai_model

# Guardrails imports (optional - may not be available if guardrails not installed)
try:
    from .guardrails import (
        create_guardrails_guard,
        create_factuality_guard,
        create_guardrails_node,
        validate_input,
        validate_output,
        GuardrailsState
    )
    _guardrails_available = True
except ImportError:
    _guardrails_available = False

__version__ = "0.1.0"
__all__ = [
    "create_langgraph_agent",
    "CacheBackedEmbeddings",
    "setup_llm_cache",
    "ProductionRAGChain",
    "get_openai_model",
]

if _guardrails_available:
    __all__.extend([
        "create_guardrails_guard",
        "create_factuality_guard",
        "create_guardrails_node",
        "validate_input",
        "validate_output",
        "GuardrailsState",
    ])

