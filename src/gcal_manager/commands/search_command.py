from datetime import date, timedelta

import dateparser

from gcal_manager.task_id import TaskId


class SearchCommand:
    def __init__(
        self, date: str, task_id: TaskId = None, search_term: str = None
    ) -> None:
        self.date = date
        self.task_id = task_id
        self.search_term = search_term

    def from_date(self, tz) -> date:
        if not self.date:
            return SearchCommand.min_date()

        return dateparser.parse(
            self.date,
            settings={"TIMEZONE": str(tz), "RETURN_AS_TIMEZONE_AWARE": True},
        )

    def to_date(self, tz) -> date:
        if not self.date:
            return SearchCommand.max_date()

        return self.from_date(tz) + timedelta(days=1)

    def query(self) -> str:
        query = ""

        if self.task_id:
            query += "[" + self.task_id.value + "] "

        if self.search_term:
            query += self.search_term

        return query

    def min_date() -> date:
        return date(2020, 1, 1)

    def max_date() -> date:
        return date(2900, 1, 1)
