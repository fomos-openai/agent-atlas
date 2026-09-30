from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from .types import ModelRequest, ModelResponse


class ModelClient(Protocol):
    def complete(self, request: ModelRequest) -> ModelResponse: ...


class FakeModel:
    """Deterministic response tape: repeatable, offline and assertion-friendly."""

    def __init__(self, responses: Iterable[ModelResponse]):
        self._responses = iter(responses)
        self.requests: list[ModelRequest] = []

    def complete(self, request: ModelRequest) -> ModelResponse:
        self.requests.append(request)
        try:
            return next(self._responses)
        except StopIteration as exc:
            raise RuntimeError("FAKE_MODEL_TAPE_EXHAUSTED") from exc
