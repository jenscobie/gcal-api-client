"""Gateway for the Google Calendar API.

Typical usage example:

  service = CalendarService()
  calendars = service.search()
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from pathlib import Path

    from gcal_manager.account_id import AccountId

from gcal_manager._services.base_service import BaseService
from gcal_manager.calendar_id import CalendarId
from gcal_manager.calendars import Calendar


class CalendarService(BaseService):
    def __init__(self, directory: Path) -> Self:
        """Constructor.

        Args:
            directory: Directory to search for credentials file.
        """
        super().__init__(directory)

    def search_calendars(self, account_id: AccountId) -> list[Calendar]:
        """Returns a list of calendars associated with the account."""
        results = self.client.calendarList().list().execute()

        return [
            self.calendar(account_id, result) for result in results["items"]
        ]

    def get_calendar(self, calendar_id: CalendarId) -> Calendar:
        return None

    def save_calendar(self, calendar: Calendar) -> Calendar:
        return None

    def delete_calendar(self, calendar_id: CalendarId) -> None:
        pass

    def calendar(self, account_id: AccountId, result: dict) -> Calendar:
        return Calendar(
            calendar_id=CalendarId(result["id"]),
            account_id=account_id,
            name=result["summary"],
        )
