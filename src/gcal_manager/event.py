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
