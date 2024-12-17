"""Gateway for the Google Calendar API.

Typical usage example:

  gateway = GoogleCalendarGateway()
  events = gateway.search()
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from pathlib import Path

    from gcal_manager.domain.model.account_id import AccountId

from gcal_manager.domain.model.calendar import Calendar
from gcal_manager.domain.model.calendar_id import CalendarId
from gcal_manager.infrastructure.gateways.google_auth import auth, credentials


class GoogleCalendarGateway:
    """Gateway for the Google Calendar API."""

    def __init__(self, directory: Path, account_id: AccountId) -> Self:
        """Constructor.

        Args:
            directory: Directory to search for credentials file.
            account_id: Unique identifier of account to auth.
        """
        self.directory = directory
        self.account_id = account_id

        creds = credentials(self.directory)
        self.client = auth(creds)

    def calendars(self) -> list[Calendar]:
        """Returns a list of calendars associated with the account."""
        results = self.client.calendarList().list().execute()

        return [
            Calendar(
                calendar_id=CalendarId(result["id"]),
                account_id=self.account_id,
                name=result["summary"],
            )
            for result in results["items"]
        ]
