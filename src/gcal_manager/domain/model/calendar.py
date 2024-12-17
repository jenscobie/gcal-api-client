"""Store and retrieve Google Calendar information."""

from __future__ import annotations

from gcal_manager.domain.model.account import Account


class Calendar:
    """A class to represent a Google Calendar."""


def get(account: Account) -> list[Calendar]:
    """Return all calendars associated with an account."""


def remove(calendar: Calendar) -> None:
    """Remove calendar from the set of known calendars."""
