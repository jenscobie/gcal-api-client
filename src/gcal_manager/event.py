"""A serializable Google event.

Typical usage example:

  event = Event(CalendarId("primary"), EventId("123"), "", ...)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

    from gcal_manager.calendar_id import CalendarId
    from gcal_manager.event_id import EventId


@dataclass(frozen=True)
class Event:
    """A serializable Google event.

    Args:
        calendar_id: The unique identifier for the parent calendar
        event_id: The unique identifier for the event
        name: The event name
        description: A description of the event, or a meeting agenda
        location: The location of the event
        url: The meeting URL for the event, if applicable
        start: Event start datetime
        end: Event end datetime
    """

    calendar_id: CalendarId
    event_id: EventId
    name: str
    description: str
    location: str
    url: str
    start: datetime
    end: datetime

    def to_json(self) -> str:
        """Returns a valid json representation of the event."""
        return {
            "kind": "calendar#event",
            "summary": self.name,
            "description": self.description,
            "location": self.location,
            "start": self.start_json(),
            "end": self.end_json(),
        }

    def start_json(self) -> str:
        """Returns a valid json representation of the event start time."""
        return {
            "dateTime": self.start.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": "America/Los_Angeles",
        }

    def end_json(self) -> str:
        """Returns a valid json representation of the event end time."""
        return {
            "dateTime": self.end.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": "America/Los_Angeles",
        }
