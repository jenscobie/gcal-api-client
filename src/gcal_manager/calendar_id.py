"""Unique identifier for a calendar.

Typical usage example:

  primary = CalendarId.primary()
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Self

from dataclass_wizard import JSONWizard


@dataclass(frozen=True)
class CalendarId(JSONWizard):
    """Unique identifier for a calendar.

    Args:
        value: Unique identifier.
    """

    value: str

    def primary() -> Self:
        """Returns primary calendar id."""
        return CalendarId(value="primary")
