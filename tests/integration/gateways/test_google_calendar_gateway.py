from pathlib import Path

from gcal_manager.domain.model.account_id import AccountId
from gcal_manager.infrastructure.gateways.google_calendar_gateway import (
    GoogleCalendarGateway,
)


def test_list_calendars() -> None:
    directory = Path("tests/data/account/valid-token")
    account_id = AccountId("valid-token")

    gateway = GoogleCalendarGateway(directory, account_id)
    calendars = gateway.calendars()

    assert len(calendars) > 1
