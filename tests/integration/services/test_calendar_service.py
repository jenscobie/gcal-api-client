from pathlib import Path

from gcal_manager._services.calendar_service import CalendarService
from gcal_manager.account_id import AccountId
from gcal_manager.calendar import Calendar


def test_list_calendars() -> None:
    directory = Path("tests/data/account/valid-token")
    account_id = AccountId("valid-token")

    service = CalendarService(directory)
    calendars = service.search_calendars(account_id)

    assert len(calendars) > 1
