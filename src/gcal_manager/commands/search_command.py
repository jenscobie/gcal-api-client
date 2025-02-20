"""Filter criteria when performing a search on a Google Calendar.

Typical usage example:

  command = SearchCommand("today")
  events = service.search(command)
"""

from __future__ import annotations

from datetime import date, timedelta, timezone
from typing import TYPE_CHECKING

import dateparser

if TYPE_CHECKING:
    from gcal_manager.task_id import TaskId


class SearchCommand:
    """Filter criteria when performing a search on a Google Calendar."""

    def __init__(
        self,
        date: str,
        task_id: TaskId | None = None,
        search_term: str | None = None,
    ) -> None:
        """Constructor for SearchCommand.

        Args:
          date: String representation of filter date
          task_id: Unique identifier of tasks to filter by
          search_term: Free-text to filter by
        """
        self.date = date
        self.task_id = task_id
        self.search_term = search_term

    def from_date(self, tz: timezone) -> date:
        """From datetime to query by.

        Args:
          tz: The timezone to query by.

        Returns:
         The timezone aware search from date
        """
        if not self.date:
            return SearchCommand.min_date()

        return dateparser.parse(
            self.date,
            settings={"TIMEZONE": str(tz), "RETURN_AS_TIMEZONE_AWARE": True},
        )

    def to_date(self, tz: timezone) -> date:
        """To datetime to query by.

        Args:
          tz: The timezone to query by.

        Returns:
          The timezone aware search to date
        """
        if not self.date:
            return SearchCommand.max_date()

        return self.from_date(tz) + timedelta(days=1)

    def query(self) -> str:
        """Properly formatted query for free text.

        Returns:
          A search string that matches the format used in events.
        """
        query = ""

        if self.task_id:
            query += "[" + self.task_id.value + "] "

        if self.search_term:
            query += self.search_term

        return query

    def min_date() -> date:
        """Returns the minimum date to filter by."""
        return date(2020, 1, 1)

    def max_date() -> date:
        """Returns the maximum date to filter by."""
        return date(2900, 1, 1)
