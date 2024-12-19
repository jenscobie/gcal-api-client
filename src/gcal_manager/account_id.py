"""Unique identifier for an account.

Typical usage example:

  personal = AccountId.personal()
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Self

from dataclass_wizard import JSONWizard


@dataclass(frozen=True)
class AccountId(JSONWizard):
    """Unique identifier for an account.

    Attributes:
        value: Unique identifier.
    """

    value: str

    def personal() -> Self:
        """Returns personal account id."""
        return AccountId(value="personal")
