from collections.abc import Callable

from .types import ModelDecision, RunState


class FakeModel:
    """Deterministic model substitute: a test supplies the policy explicitly."""

    def __init__(self, policy: Callable[[RunState, list[str]], ModelDecision]):
        self._policy = policy

    def decide(self, state: RunState, tools: list[str]) -> ModelDecision:
        return self._policy(state, tools)
