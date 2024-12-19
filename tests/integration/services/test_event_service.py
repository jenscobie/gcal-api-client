from pathlib import Path

from gcal_manager._services.event_service import EventService
from gcal_manager.account_id import AccountId
from gcal_manager.calendar_id import CalendarId
from gcal_manager.commands.search_command import SearchCommand


def test_search_events() -> None:
    directory = Path("tests/data/account/valid-token")
    account_id = AccountId("valid-token")
    calendar_id = CalendarId.primary()
    search_command = SearchCommand("today")

    gateway = EventService(directory)
    events = gateway.search_events(calendar_id, search_command)

    assert len(events) > 1
