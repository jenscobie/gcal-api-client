"""Gateway for the Google Calendar API.

Typical usage example:

  gateway = GoogleCalendarGateway()
  events = gateway.search()
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from pathlib import Path

    from gcal_manager.domain.commands.search_command import SearchCommand
    from gcal_manager.domain.model.account_id import AccountId

from gcal_manager.domain.model.calendar import Calendar
from gcal_manager.domain.model.calendar_id import CalendarId
from gcal_manager.domain.model.event import Event
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

        return [self.calendar(result) for result in results["items"]]

    def calendar(self, result) -> Calendar:
        return Calendar(
            calendar_id=CalendarId(result["id"]),
            account_id=self.account_id,
            name=result["summary"],
        )

    def search(
        self, calendar_id: CalendarId, command: SearchCommand
    ) -> list[Event]:
        query = command.query()

        results = (
            self.client.events()
            .list(
                calendarId=calendar_id.value,
                q=query,
                maxResults=100,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        return [self.event(calendar_id, result) for result in results["items"]]

    def event(self, calendar_id: CalendarId, result) -> Event:
        return Event(
            event_id="",
            calendar_id=calendar_id,
            name=result["summary"],
            description="",
            location="",
            url=result["htmlLink"],
            start=self.parse_datetime(
                result["start"].get("dateTime", result["start"].get("date"))
            ),
            end=self.parse_datetime(
                result["end"].get("dateTime", result["end"].get("date"))
            ),
        )

    def parse_datetime(self, date: str) -> datetime:
        return datetime.fromisoformat(date)
