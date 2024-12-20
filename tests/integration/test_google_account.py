from pathlib import Path

from gcal_manager.google_account import GoogleAccount


def test_search_accounts() -> None:
    directory = Path("tests/data/account/")

    service = GoogleAccount(directory)
    accounts = service.search_accounts()

    assert len(accounts) > 1
