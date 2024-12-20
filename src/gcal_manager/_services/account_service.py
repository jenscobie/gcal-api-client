"""Repository for Google Accounts.

Typical usage example:

  service = AccountService()
  accounts = service.search()
"""

from __future__ import annotations

from pathlib import Path
from typing import Self

from gcal_manager.account import Account
from gcal_manager.account_id import AccountId


class AccountService:
    def __init__(self, path: Path) -> Self:
        self.path = path

    def search_accounts(self) -> list[Account]:
        """Returns a list of known accounts."""

        return [
            self.account_id(directory)
            for directory in self.list_directories()
        ]
    
    def account_id(self, path: Path) -> Account:
        account_id = AccountId(path.name)
        return Account(account_id=account_id, path=path)

    def get_account(self, account_id: AccountId) -> Account | None:
        account = next(
            (
                account
                for account in self.search_accounts()
                if account.account_id == account_id
            ),
            None,
        )
        return account

    def save_account(self, account: Account) -> Account | None:
        directory = f"{self.path}/{account.account_id.value}"
        if not Path(directory).exists():
            Path(directory).mkdir()

    def delete_account(self, account_id: AccountId) -> None:
        directory = f"{self.path}/{account_id.value}"
        if Path(directory).exists():
            Path(directory).rmdir()

    def list_directories(self) -> list[str]:
        for file in Path(self.path).iterdir():
            if file.is_dir():
                yield file
