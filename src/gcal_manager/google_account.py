from pathlib import Path

from gcal_manager._services.account_service import AccountService


class GoogleAccount(AccountService):
    def __init__(self, directory: Path):
        self.directory = directory
