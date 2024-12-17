from __future__ import annotations

from dataclasses import dataclass
from typing import Self

from dataclass_wizard import JSONWizard


@dataclass(frozen=True)
class AccountId(JSONWizard):
    value: str = None

    def __eq__(self, other: AccountId) -> bool:
        if isinstance(other, AccountId):
            return self.value == other.value
        return False

    def all() -> Self:
        return AccountId(value="all")

    def none() -> Self:
        return AccountId(value="none")

    def personal() -> Self:
        return AccountId(value="personal")
