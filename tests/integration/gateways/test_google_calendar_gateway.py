from pathlib import Path

from gcal_manager.domain.commands.search_command import SearchCommand
from gcal_manager.domain.model.account_id import AccountId
from gcal_manager.domain.model.calendar_id import CalendarId
from gcal_manager.infrastructure.gateways.google_calendar_gateway import (
    GoogleCalendarGateway,
)


def test_list_calendars() -> None:
    directory = Path("tests/data/account/valid-token")
    account_id = AccountId("valid-token")

    gateway = GoogleCalendarGateway(directory, account_id)
    calendars = gateway.calendars()

    assert len(calendars) > 1


def test_search_events() -> None:
    directory = Path("tests/data/account/valid-token")
    account_id = AccountId("valid-token")
    calendar_id = CalendarId.primary()
    search_command = SearchCommand("today")

    gateway = GoogleCalendarGateway(directory, account_id)
    events = gateway.search(calendar_id, search_command)

    assert len(events) > 1
