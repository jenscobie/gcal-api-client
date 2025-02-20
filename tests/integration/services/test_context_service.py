from pathlib import Path
from typing import Callable

import pytest

from gcal_manager._services.context_service import ContextService
from gcal_manager.account_id import AccountId
from gcal_manager.context import Context
from gcal_manager.context_id import ContextId

directory = "tests/data/context"
context_id = ContextId("integration-test")
account_id = AccountId.personal()
service = ContextService(directory)


def build() -> Context:
    return Context(
        context_id=context_id,
        account_id=account_id,
        path=Path(f"{directory}/{context_id.value}"),
    )


context = build()


@pytest.fixture
def _setup() -> None:
    """Remove all test data.

    State that is not cleaned between tests can result in flakey tests.
    """
    service.save_context(context)
    yield
    service.delete_context(context.context_id)


def test_search_contexts(_setup: Callable) -> None:
    contexts = service.search_contexts()

    assert context in contexts


def test_get_context(_setup: Callable) -> None:
    result = service.get_context(context_id)

    assert result == context
