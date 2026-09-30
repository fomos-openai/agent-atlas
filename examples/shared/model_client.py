from typing import Protocol

from .types import ModelDecision, RunState


class ModelClient(Protocol):
    """Small provider-neutral boundary used by every example."""

    def decide(self, state: RunState, tools: list[str]) -> ModelDecision:
        ...
