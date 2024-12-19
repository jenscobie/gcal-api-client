from pathlib import Path

from gcal_manager._services.google_auth import auth, credentials

from ._services.calendar_service import CalendarService
from ._services.event_service import EventService


class GoogleCalendar(EventService, CalendarService):
    def __init__(self, directory: Path):
        self.directory = directory

        creds = credentials(self.directory)
        self.client = auth(creds)
