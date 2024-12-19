from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass(frozen=True)
class TaskId(JSONWizard):
    value: str
