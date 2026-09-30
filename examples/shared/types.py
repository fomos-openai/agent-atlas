from dataclasses import dataclass, field
from typing import Any, Literal


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: dict[str, Any]


@dataclass(frozen=True)
class ModelDecision:
    kind: Literal["tool", "final"]
    content: str = ""
    tool_call: ToolCall | None = None


@dataclass
class RunState:
    goal: str
    step: int = 0
    observations: list[str] = field(default_factory=list)
    events: list[dict[str, Any]] = field(default_factory=list)
