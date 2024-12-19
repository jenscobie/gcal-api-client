from pathlib import Path

import pytest

from gcal_manager._services.google_auth import credentials


def test_token_doesnt_exist() -> None:
    directory = Path("tests/data/account/none")

    creds = credentials(directory)

    assert not creds


def test_credentials_dont_exist() -> None:
    directory = Path("tests/data/account/none")

    creds = credentials(directory)

    assert not creds


def test_valid_token_exists() -> None:
    directory = Path("tests/data/account/valid-token")

    creds = credentials(directory)

    assert creds.valid


def test_expired_token_exists() -> None:
    directory = Path("tests/data/account/expired-token")

    creds = credentials(directory)

    assert creds.valid


@pytest.mark.skip(reason="test launches a browser window")
def test_credentials_exist() -> None:
    path = "tests/data/account/credentials-only"
    directory = Path(path)

    creds = credentials(directory)

    assert Path(f"{path}/token.json").exists()
    assert creds.valid

    Path(f"{path}/token.json").unlink()
