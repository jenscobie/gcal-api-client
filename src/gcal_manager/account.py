"""Store and retrieve Google Account information."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gcal_manager.account_id import AccountId


@dataclass(frozen=True)
class Account:
    """A class to represent a Google Account."""

    account_id: AccountId
    path: str
