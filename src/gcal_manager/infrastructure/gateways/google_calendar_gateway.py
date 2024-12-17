"""Gateway for the Google Calendar API.

Typical usage example:

  gateway = GoogleCalendarGateway()
  events = gateway.search()
"""

from pathlib import Path
from typing import Self

from gcal_manager.domain.model.account_id import AccountId
from gcal_manager.infrastructure.gateways.google_auth import auth, credentials

scopes = ["https://www.googleapis.com/auth/calendar"]


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

        creds = credentials(self.account_id)
        self.client = auth(creds)
