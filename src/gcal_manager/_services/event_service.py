"""Gateway for the Google Calendar API.

Typical usage example:

  service = EventService()
  calendars = service.search()
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Self

from gcal_manager._services.base_service import BaseService
from gcal_manager.commands.search_command import SearchCommand
from gcal_manager.event import Event
from gcal_manager.event_id import EventId

if TYPE_CHECKING:
    from pathlib import Path

from gcal_manager.calendar_id import CalendarId


class EventService(BaseService):
    def __init__(self, directory: Path) -> Self:
        """Constructor.

        Args:
            directory: Directory to search for credentials file.
        """
        super().__init__(directory)

    def search_events(
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

    def get_event(self, event_id: EventId) -> Event:
        return None

    def save_event(self, event: Event) -> Event:
        return None

    def delete_event(self, event_id: EventId) -> None:
        pass

    def event(self, calendar_id: CalendarId, result: dict) -> Event:
        return Event(
            event_id=EventId(""),
            calendar_id=calendar_id,
            name=result["summary"],
            description="",
            location="",
            url=result["htmlLink"],
            start=self.parse_datetime("start", result),
            end=self.parse_datetime("end", result),
        )

    def parse_datetime(self, field_key: str, result: dict) -> datetime:
        date = result[field_key].get("dateTime", result[field_key].get("date"))
        return datetime.fromisoformat(date)
