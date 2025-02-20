"""Modify properties of a Google Account.

Typical usage example:

  account = GoogleAccount("~/creds")
"""

from pathlib import Path
from typing import Self

from gcal_manager._services.account_service import AccountService


class GoogleAccount(AccountService):
    """Modify properties of a Google Account."""

    def __init__(self, directory: Path) -> Self:
        """Constructor for GoogleAccount.

        Args:
          directory: Path to directory where credentials.json file is located
        """
        self.directory = directory
