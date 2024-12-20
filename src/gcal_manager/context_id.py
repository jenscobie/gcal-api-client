"""Unique identifier for a context.

Typical usage example:

  context_id = ContextId("foo")
"""

from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass(frozen=True)
class ContextId(JSONWizard):
    """Unique identifier for a context.

    Attributes:
        value: Unique identifier.
    """

    value: str
