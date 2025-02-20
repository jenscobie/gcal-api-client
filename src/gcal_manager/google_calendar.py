"""Modify properties of a Google Calendar and events.

Typical usage example:

  calendar = GoogleCalendar("~/creds")
"""

from pathlib import Path
from typing import Self

from gcal_manager._services.google_auth import auth, credentials

from ._services.calendar_service import CalendarService
from ._services.event_service import EventService


class GoogleCalendar(EventService, CalendarService):
    """Modify properties of a Google Calendar and events."""

    def __init__(self, directory: Path) -> Self:
        """Constructor for GoogleCalendar.

        Args:
          directory: Path to directory where credentials.json file is located
        """
        self.directory = directory

        creds = credentials(self.directory)
        self.client = auth(creds)
