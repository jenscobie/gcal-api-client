from pathlib import Path
import pytest

from typing import Callable

from gcal_manager._services.account_service import AccountService
from gcal_manager.account import Account
from gcal_manager.account_id import AccountId

path = "tests/data/account"
account_id = AccountId("test")

start_count = 4


@pytest.fixture
def _setup() -> None:
    """Remove all test data.

    State that is not cleaned between tests can result in flakey tests.
    """
    service = AccountService(path)
    service.delete_account(account_id)

def test_save_account(_setup: Callable) -> None:
    account = build()

    service = AccountService(path)
    before = service.search_accounts()

    assert len(before) == start_count

    service.save_account(account)

    after = service.search_accounts()
    assert len(after) > len(before)


def test_search_accounts(_setup: Callable) -> None:
    account = build()

    service = AccountService(path)
    service.save_account(account)

    result = service.search_accounts()

    assert len(result) == start_count + 1


def test_get_account(_setup: Callable) -> None:
    account = build()

    service = AccountService(path)
    service.save_account(account)

    result = service.get_account(account_id)

    assert result == account


def test_delete_account(_setup: Callable) -> None:
    account = build()

    service = AccountService(path)
    service.save_account(account)

    service.delete_account(account_id)

    result = service.search_accounts()
    assert len(result) == start_count


def build() -> Account:
    return Account(account_id=account_id, path=Path("tests/data/account/test"))
