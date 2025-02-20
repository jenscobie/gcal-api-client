"""Store and retrieve Google Calendar events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from gcal_manager.calendar_id import CalendarId
from gcal_manager.event_id import EventId


@dataclass(frozen=True)
class Event:
    calendar_id: CalendarId
    event_id: EventId
    name: str
    description: str
    location: str
    url: str
    start: datetime
    end: datetime

    def to_json(self) -> str:
        return {
            "kind": "calendar#event",
            "summary": self.name,
            "description": self.description,
            "location": self.location,
            "start": self.start_json(),
            "end": self.end_json(),
        }

    def start_json(self) -> str:
        return {
            #'date': date,
            "dateTime": self.start.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": "America/Los_Angeles",
        }

    def end_json(self) -> str:
        return {
            #'date': date,
            "dateTime": self.end.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": "America/Los_Angeles",
        }
