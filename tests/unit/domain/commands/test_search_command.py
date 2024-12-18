from datetime import datetime

from gcal_manager.domain.commands.search_command import SearchCommand
from gcal_manager.domain.model.task_id import TaskId


def test_no_date() -> None:
    search = SearchCommand(date=None, task_id=TaskId("one"), search_term="two")

    assert search.from_date() == SearchCommand.min_date()
    assert search.to_date() == SearchCommand.max_date()


def test_date_parsing() -> None:
    search = SearchCommand(
        date="today", task_id=TaskId("one"), search_term="two"
    )

    assert search.from_date().date() == datetime.today().date()


def test_query() -> None:
    search = SearchCommand(
        date="today", task_id=TaskId("one"), search_term="two"
    )

    query = search.query()

    assert query == "[one] two"
