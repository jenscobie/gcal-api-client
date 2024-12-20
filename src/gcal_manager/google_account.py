from pathlib import Path

from gcal_manager._services.account_service import AccountService
from gcal_manager.account import Account


class GoogleCalendar(AccountService):
    def __init__(self, directory: Path):
        self.directory = directory
