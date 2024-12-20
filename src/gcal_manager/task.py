"""Store and retrieve task templates."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    """A class to represent a task template."""
