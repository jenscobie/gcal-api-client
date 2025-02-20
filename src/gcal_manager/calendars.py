"""A calendar linked to a Google account.

Typical usage example:

  calendar = Calendar("primary", "jenscobie@gmail.com", "Events")
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gcal_manager.account_id import AccountId
    from gcal_manager.calendar_id import CalendarId


@dataclass(frozen=True)
class Calendar:
    """Unique identifier for a task.

    Args:
      calendar_id: Unique identifier.
      account_id: Unique identifier.
      name: Unique identifier.
    """

    calendar_id: CalendarId
    account_id: AccountId
    name: str
