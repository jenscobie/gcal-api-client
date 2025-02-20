"""Validation of SearchCommand.

Typical usage example:

  service = AccountService(path)
  accounts = service.search_accounts()
"""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from gcal_manager.commands.search_command import SearchCommand
from gcal_manager.task_id import TaskId


def test_no_date() -> None:
    search = SearchCommand(date=None, task_id=TaskId("one"), search_term="two")

    assert search.from_date(timezone.utc) == SearchCommand.min_date()
    assert search.to_date(timezone.utc) == SearchCommand.max_date()


def test_date_parsing() -> None:
    search = SearchCommand(
        date="today", task_id=TaskId("one"), search_term="two"
    )

    assert (
        search.from_date(timezone.utc).date()
        == datetime.now(tz=timezone.utc).date()
    )


def test_query() -> None:
    search = SearchCommand(
        date="today", task_id=TaskId("one"), search_term="two"
    )

    query = search.query()

    assert query == "[one] two"


def test_from_date() -> None:
    search = SearchCommand(
        date="2025-01-01", task_id=TaskId("one"), search_term="two"
    )

    assert search.from_date(timezone.utc) == datetime(2025, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)


def test_to_date() -> None:
    search = SearchCommand(
        date="2025-01-01", task_id=TaskId("one"), search_term="two"
    )

    assert search.to_date(timezone.utc) == datetime(2025, 1, 2, 0, 0, 0, 0, tzinfo=timezone.utc)
