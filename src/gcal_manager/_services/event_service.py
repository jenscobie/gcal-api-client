"""Gateway for the Google Calendar API.

Typical usage example:

  service = EventService()
  calendars = service.search()
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Self

from gcal_manager._services.base_service import BaseService
from gcal_manager.event import Event
from gcal_manager.event_id import EventId

if TYPE_CHECKING:
    from pathlib import Path

    from gcal_manager.calendar_id import CalendarId
    from gcal_manager.commands.search_command import SearchCommand


class EventService(BaseService):
    """Gateway for the Google Calendar API."""

    def __init__(self, directory: Path) -> Self:
        """Constructor.

        Args:
            directory: Directory to search for credentials file.
        """
        super().__init__(directory)

    def search_events(
        self, calendar_id: CalendarId, command: SearchCommand
    ) -> list[Event]:
        """Filter events in the Google Calendar.

        Args:
            calendar_id: The unique identifier for the calendar being
              searched.
            command: Criteria to filter search results by.

        Returns:
          A list of events matching the search criteria.
        """
        # TODO: Should come from calendar settings
        calendar_timezone = "US/Pacific"
        query = command.query()
        date_from = command.from_date(calendar_timezone)
        date_to = command.to_date(calendar_timezone)

        # https://developers.google.com/calendar/api/v3/reference/events/list
        results = (
            self.client.events()
            .list(
                calendarId=calendar_id.value,
                q=query,
                timeMin=date_from.isoformat(),
                timeMax=date_to.isoformat(),
                maxResults=100,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        return [self.event(calendar_id, result) for result in results["items"]]

    def get_event(self, calendar_id: CalendarId, event_id: EventId) -> Event:
        # https://developers.google.com/calendar/api/v3/reference/events/get
        return self.event(
            calendar_id,
            self.client.events()
            .get(calendarId=calendar_id.value, eventId=event_id.value)
            .execute(),
        )

    def save_event(self, event: Event) -> Event:
        resource = event.to_json()

        # https://developers.google.com/calendar/api/v3/reference/events/insert
        result = (
            self.client.events()
            .insert(calendarId=event.calendar_id.value, body=resource)
            .execute()
        )
        return self.event(event.calendar_id, result)

    def delete_event(self, calendar_id: CalendarId, event_id: EventId) -> None:
        # https://developers.google.com/calendar/api/v3/reference/events/delete
        self.client.events().delete(
            calendarId=calendar_id.value, eventId=event_id.value
        ).execute()

    def event(self, calendar_id: CalendarId, result: dict) -> Event:
        return Event(
            event_id=EventId(result["id"]),
            calendar_id=calendar_id,
            name=result["summary"],
            # description=result["description"],
            description="something",
            # location=result["location"],
            location="something",
            url=result["htmlLink"],
            start=self.parse_datetime("start", result),
            end=self.parse_datetime("end", result),
        )

    def parse_datetime(self, field_key: str, result: dict) -> datetime:
        date = result[field_key].get("dateTime", result[field_key].get("date"))
        return datetime.fromisoformat(date)
