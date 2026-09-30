from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Protocol

from .model import ModelClient
from .types import (
    AgentState,
    Message,
    ModelRequest,
    PolicyDecision,
    PolicyDecisionKind,
    RunStatus,
    ToolCall,
    ToolResult,
    ToolSpec,
    Trace,
)

ToolHandler = Callable[[dict[str, Any]], dict[str, Any]]


class Policy(Protocol):
    def evaluate(self, call: ToolCall, state: AgentState) -> PolicyDecision: ...


@dataclass(frozen=True)
class RegisteredTool:
    spec: ToolSpec
    handler: ToolHandler


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, RegisteredTool] = {}

    def register(self, spec: ToolSpec, handler: ToolHandler) -> None:
        if spec.name in self._tools:
            raise ValueError(f"duplicate tool: {spec.name}")
        self._tools[spec.name] = RegisteredTool(spec, handler)

    @property
    def specs(self) -> tuple[ToolSpec, ...]:
        return tuple(item.spec for item in self._tools.values())

    def require(self, name: str) -> RegisteredTool:
        if name not in self._tools:
            raise KeyError(name)
        return self._tools[name]


class AllowReadsApproveWrites:
    def evaluate(self, call: ToolCall, state: AgentState) -> PolicyDecision:
        del state
        if call.tool_name.startswith("modify_production"):
            return PolicyDecision(PolicyDecisionKind.DENY, "PRODUCTION_TOOL_FORBIDDEN")
        return PolicyDecision(PolicyDecisionKind.ALLOW, "LOW_RISK")


class AgentRuntime:
    def __init__(
        self,
        model: ModelClient,
        registry: ToolRegistry,
        policy: Policy | None = None,
        max_steps: int = 8,
    ) -> None:
        self.model = model
        self.registry = registry
        self.policy = policy or AllowReadsApproveWrites()
        self.max_steps = max_steps
        self.trace: Trace | None = None
        self._results_by_key: dict[str, ToolResult] = {}

    def run(self, state: AgentState, *, approved_call_id: str | None = None) -> AgentState:
        if self.trace is None or self.trace.run_id != state.run_id:
            self.trace = Trace(state.run_id)
            self.trace.append("run_started", goal=state.goal)

        if state.status == RunStatus.WAITING_APPROVAL:
            if not state.pending_call or approved_call_id != state.pending_call.id:
                return state
            self.trace.append("approval_received", call_id=approved_call_id)
            executed = self._execute(state, state.pending_call, bypass_policy=True)
            state.pending_call = None
            if not executed:
                return state
            state.status = RunStatus.RUNNING

        while state.status == RunStatus.RUNNING:
            if state.steps >= self.max_steps:
                state.status = RunStatus.BUDGET_EXHAUSTED
                state.error_code = "MAX_STEPS"
                self.trace.append("budget_exhausted", limit=self.max_steps)
                break

            request = ModelRequest(
                messages=(Message("user", state.goal),),
                tools=self.registry.specs,
                state_version=state.version,
            )
            response = self.model.complete(request)
            state.steps += 1
            self.trace.append(
                "model_result",
                has_tool_call=response.tool_call is not None,
                has_final_output=response.final_output is not None,
                usage=response.usage,
            )
            if response.final_output is not None:
                state.final_output = response.final_output
                state.status = RunStatus.COMPLETED
                state.version += 1
                self.trace.append("run_completed", output=response.final_output)
                break
            if response.tool_call is None:
                state.status = RunStatus.FAILED
                state.error_code = "EMPTY_MODEL_RESPONSE"
                self.trace.append("run_failed", code=state.error_code)
                break
            if not self._execute(state, response.tool_call):
                break
        return state

    def _execute(self, state: AgentState, call: ToolCall, bypass_policy: bool = False) -> bool:
        assert self.trace is not None
        try:
            tool = self.registry.require(call.tool_name)
        except KeyError:
            state.status = RunStatus.FAILED
            state.error_code = "UNKNOWN_TOOL"
            self.trace.append("tool_rejected", call_id=call.id, code=state.error_code)
            return False

        missing = [key for key in tool.spec.required if key not in call.arguments]
        if missing:
            state.status = RunStatus.FAILED
            state.error_code = "INVALID_ARGUMENTS"
            self.trace.append("tool_rejected", call_id=call.id, missing=missing)
            return False

        if not bypass_policy:
            decision = self.policy.evaluate(call, state)
            self.trace.append(
                "policy_decision",
                call_id=call.id,
                decision=decision.kind.value,
                reason_code=decision.reason_code,
            )
            if decision.kind == PolicyDecisionKind.DENY:
                state.status = RunStatus.FAILED
                state.error_code = decision.reason_code
                return False
            if decision.kind == PolicyDecisionKind.REQUIRE_APPROVAL:
                state.pending_call = call
                state.status = RunStatus.WAITING_APPROVAL
                state.version += 1
                self.trace.append("approval_requested", call_id=call.id)
                return False

        if call.idempotency_key in self._results_by_key:
            result = self._results_by_key[call.idempotency_key]
            self.trace.append("tool_result_reused", call_id=call.id, key=call.idempotency_key)
        else:
            try:
                payload = tool.handler(call.arguments)
                result = ToolResult(call.id, "ok", payload)
            except Exception as exc:  # adapters must classify production errors more narrowly
                result = ToolResult(call.id, "error", code=type(exc).__name__, retryable=False)
            self._results_by_key[call.idempotency_key] = result
            self.trace.append("tool_executed", call_id=call.id, status=result.status)

        state.observations.append(result)
        state.version += 1
        if result.status != "ok":
            state.status = RunStatus.FAILED
            state.error_code = result.code
            return False
        return True
