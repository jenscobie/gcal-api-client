"""Store and retrieve contexts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gcal_manager.account_id import AccountId
    from gcal_manager.context_id import ContextId


@dataclass(frozen=True)
class Context:
    """A class to represent a context."""

    context_id: ContextId
    account_id: AccountId
    path: str
