from datetime import date, datetime
from pathlib import Path
import pytest

from gcal_manager._services.event_service import EventService
from gcal_manager.calendar_id import CalendarId
from gcal_manager.commands.search_command import SearchCommand
from gcal_manager.event import Event
from gcal_manager.event_id import EventId

directory = Path("tests/data/account/valid-token")
service = EventService(directory)
calendar_id = CalendarId.primary()

@pytest.fixture
def _setup() -> None:
    """Remove all test data.

    State that is not cleaned between tests can result in flakey tests.
    """
    event = create(calendar_id)
    event = service.save_event(event)
    yield
    service.delete_event(calendar_id, event.event_id)


@pytest.mark.usefixtures("_setup")
def test_search_events() -> None:
    search_command = SearchCommand("2025-01-01")

    events = service.search_events(calendar_id, search_command)

    assert len(events) == 3

    first = events[0]

    assert first.event_id != EventId.none()
    assert first.calendar_id == calendar_id
    assert first.name == "integration test event"
    assert first.description != "This is a description"
    assert first.location != "This is a location"
    assert first.url != "This is the meeting link"
    assert first.start.date() == date(2025, 1, 1)
    assert first.end.date() == date(2025, 1, 1)

@pytest.mark.usefixtures("_setup")
def get_event() -> None:
    event = create(calendar_id)
    event = service.save_event(event)

    event = service.get_event(calendar_id, event.event_id)

    assert event.event_id != EventId.none()
    assert event.calendar_id == calendar_id
    assert event.name == "integration test event"
    assert event.description != "This is a description"
    assert event.location != "This is a location"
    assert event.url != "This is the meeting link"
    assert event.start.date() == date(2025, 1, 1)
    assert event.end.date() == date(2025, 1, 1)

    service.delete_event(calendar_id, event.event_id)

def create(calendar_id: CalendarId) -> Event:
    return Event(
        calendar_id,
        EventId(""),
        "integration test event",
        "this is a test event created by integration test suite.",
        "test location",
        "test url",
        datetime(2025, 1, 1, 3, 0, 0, 0),
        datetime(2025, 1, 1, 4, 0, 0, 0)
    )
