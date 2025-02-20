"""Unique identifier for a task.

Typical usage example:

  task_id = TaskId("foo")
"""

from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard


@dataclass(frozen=True)
class TaskId(JSONWizard):
    """Unique identifier for a task.

    Args:
        value: Unique identifier.
    """

    value: str
