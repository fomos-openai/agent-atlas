from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class RunStatus(StrEnum):
    RUNNING = "running"
    WAITING_APPROVAL = "waiting_approval"
    COMPLETED = "completed"
    FAILED = "failed"
    BUDGET_EXHAUSTED = "budget_exhausted"


class PolicyDecisionKind(StrEnum):
    ALLOW = "allow"
    DENY = "deny"
    REQUIRE_APPROVAL = "require_approval"


@dataclass(frozen=True)
class Message:
    role: str
    content: str


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    required: tuple[str, ...] = ()
    side_effect: str = "read"


@dataclass(frozen=True)
class ToolCall:
    id: str
    tool_name: str
    arguments: dict[str, Any]
    idempotency_key: str


@dataclass(frozen=True)
class ToolResult:
    call_id: str
    status: str
    payload: dict[str, Any] = field(default_factory=dict)
    code: str | None = None
    retryable: bool = False


@dataclass(frozen=True)
class ModelRequest:
    messages: tuple[Message, ...]
    tools: tuple[ToolSpec, ...]
    state_version: int


@dataclass(frozen=True)
class ModelResponse:
    final_output: str | None = None
    tool_call: ToolCall | None = None
    usage: dict[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class PolicyDecision:
    kind: PolicyDecisionKind
    reason_code: str


@dataclass(frozen=True)
class AgentEvent:
    sequence: int
    kind: str
    data: dict[str, Any]


@dataclass
class AgentState:
    run_id: str
    goal: str
    status: RunStatus = RunStatus.RUNNING
    version: int = 0
    steps: int = 0
    observations: list[ToolResult] = field(default_factory=list)
    pending_call: ToolCall | None = None
    final_output: str | None = None
    error_code: str | None = None


@dataclass
class Trace:
    run_id: str
    events: list[AgentEvent] = field(default_factory=list)

    def append(self, kind: str, **data: Any) -> None:
        # Deliberately records auditable decisions, never hidden reasoning text.
        self.events.append(AgentEvent(len(self.events) + 1, kind, data))
