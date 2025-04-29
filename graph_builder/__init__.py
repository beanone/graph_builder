"""Graph Builder - A library for building and managing graph data structures."""

__version__ = "0.1.0"

from .compactor import GraphCompactor
from .config import GraphBuilderConfig
from .storage_manager import GraphBuilder

__all__ = ["GraphBuilder", "GraphBuilderConfig", "GraphCompactor"]
