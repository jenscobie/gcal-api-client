"""Repository for Google Accounts.

Typical usage example:

  service = ContextService(path)
  accounts = service.search_contexts()
"""

from __future__ import annotations

from pathlib import Path
from typing import Self

from gcal_manager.account_id import AccountId
from gcal_manager.context import Context
from gcal_manager.context_id import ContextId


class ContextService:
    def __init__(self, directory: Path) -> Self:
        self.directory = directory

    def search_contexts(self) -> list[Context]:
        """Returns a list of known accounts."""

        return [self.context(d) for d in self.list_directories()]

    def context(self, directory: Path) -> Context:
        context_id = ContextId(directory.name)
        return Context(
            context_id=context_id,
            account_id=AccountId.personal(),
            path=directory,
        )

    def get_context(self, context_id: ContextId) -> Context | None:
        return next(
            (
                context
                for context in self.search_contexts()
                if context.context_id == context_id
            ),
            None,
        )

    def save_context(self, context: Context) -> Context | None:
        directory = f"{self.directory}/{context.context_id.value}"
        print(directory)
        if not Path(directory).exists():
            Path(directory).mkdir()

    def delete_context(self, context_id: ContextId) -> None:
        directory = f"{self.directory}/{context_id.value}"
        if Path(directory).exists():
            Path(directory).rmdir()

    def list_directories(self) -> list[str]:
        for file in Path(self.directory).iterdir():
            if file.is_dir():
                yield file
