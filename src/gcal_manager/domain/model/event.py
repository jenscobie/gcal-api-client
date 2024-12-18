"""Store and retrieve Google Calendar events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from gcal_manager.domain.model.calendar_id import CalendarId


@dataclass(frozen=True)
class Event:
    calendar_id: CalendarId
    event_id: str
    name: str
    description: str
    location: str
    url: str
    start: datetime
    end: datetime
