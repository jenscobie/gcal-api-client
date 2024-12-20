from pathlib import Path
from typing import Self

from gcal_manager._services.google_auth import auth, credentials


class BaseService:
    def __init__(self, directory: Path) -> Self:
        """Constructor.

        Args:
            directory: Directory to search for credentials file.
        """
        self.directory = directory

        creds = credentials(self.directory)
        self.client = auth(creds)
