"""Store and retrieve contexts."""

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Context:
    """A class to represent a context."""
