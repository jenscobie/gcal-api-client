from pathlib import Path
import pytest

from typing import Callable

from gcal_manager._services.account_service import AccountService
from gcal_manager.account import Account
from gcal_manager.account_id import AccountId

path = "tests/data/account"
account_id = AccountId("test")
service = AccountService(path)


def build() -> Account:
    return Account(account_id=account_id, path=Path(f"{path}/{account_id.value}"))

account = build()

@pytest.fixture
def _setup() -> None:
    """Remove all test data.

    State that is not cleaned between tests can result in flakey tests.
    """
    service.save_account(account)
    yield
    service.delete_account(account_id)


def test_search_accounts(_setup: Callable) -> None:
    accounts = service.search_accounts()

    assert account in accounts


def test_get_account(_setup: Callable) -> None:
    result = service.get_account(account_id)

    assert result == account
