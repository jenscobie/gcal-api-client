"""Unique identifier for an event.

Typical usage example:

  event_id = EventId("foo")
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Self

from dataclass_wizard import JSONWizard


@dataclass(frozen=True)
class EventId(JSONWizard):
    """Unique identifier for an event.

    Args:
        value: Unique identifier.
    """

    value: str

    def none() -> Self:
        return EventId("")
