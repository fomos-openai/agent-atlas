import unittest

from agent_atlas import (
    AgentRuntime, AgentState, FakeModel, ModelResponse, PolicyDecision,
    PolicyDecisionKind, RunStatus, ToolCall, ToolSpec, ToolRegistry,
)


def call(call_id="c1", name="read", args=None, key="k1"):
    return ToolCall(call_id, name, args or {"resource": "orders"}, key)


class FixedPolicy:
    def __init__(self, kind): self.kind = kind
    def evaluate(self, tool_call, state):
        del tool_call, state
        return PolicyDecision(self.kind, "TEST_POLICY")


class RuntimeTests(unittest.TestCase):
    def registry(self, effects=None):
        effects = effects if effects is not None else []
        registry = ToolRegistry()
        registry.register(ToolSpec("read", "read", ("resource",)), lambda args: {"value": args["resource"]})
        registry.register(ToolSpec("write", "write", ("resource",), "reversible_write"), lambda args: effects.append(args["resource"]) or {"saved": True})
        return registry

    def test_tool_then_stop(self):
        model = FakeModel([ModelResponse(tool_call=call()), ModelResponse(final_output="done")])
        runtime = AgentRuntime(model, self.registry())
        state = runtime.run(AgentState("r1", "goal"))
        self.assertEqual(state.status, RunStatus.COMPLETED)
        self.assertEqual(len(state.observations), 1)

    def test_budget_is_owned_by_runtime(self):
        model = FakeModel([ModelResponse(tool_call=call("c1", key="k1")), ModelResponse(tool_call=call("c2", key="k2"))])
        state = AgentRuntime(model, self.registry(), max_steps=1).run(AgentState("r2", "goal"))
        self.assertEqual(state.status, RunStatus.BUDGET_EXHAUSTED)

    def test_unknown_tool_fails_closed(self):
        model = FakeModel([ModelResponse(tool_call=call(name="missing"))])
        state = AgentRuntime(model, self.registry()).run(AgentState("r3", "goal"))
        self.assertEqual(state.error_code, "UNKNOWN_TOOL")

    def test_missing_argument_is_rejected(self):
        model = FakeModel([ModelResponse(tool_call=call(args={"wrong": 1}))])
        state = AgentRuntime(model, self.registry()).run(AgentState("r4", "goal"))
        self.assertEqual(state.error_code, "INVALID_ARGUMENTS")

    def test_deny_never_executes(self):
        effects = []
        model = FakeModel([ModelResponse(tool_call=call(name="write"))])
        state = AgentRuntime(model, self.registry(effects), FixedPolicy(PolicyDecisionKind.DENY)).run(AgentState("r5", "goal"))
        self.assertEqual(state.status, RunStatus.FAILED)
        self.assertEqual(effects, [])

    def test_approval_pauses_then_resumes_exact_call(self):
        effects = []
        model = FakeModel([ModelResponse(tool_call=call(name="write")), ModelResponse(final_output="done")])
        runtime = AgentRuntime(model, self.registry(effects), FixedPolicy(PolicyDecisionKind.REQUIRE_APPROVAL))
        state = runtime.run(AgentState("r6", "goal"))
        self.assertEqual(state.status, RunStatus.WAITING_APPROVAL)
        self.assertEqual(effects, [])
        runtime.run(state, approved_call_id="c1")
        self.assertEqual(effects, ["orders"])
        self.assertEqual(state.status, RunStatus.COMPLETED)

    def test_idempotency_reuses_result(self):
        effects = []
        model = FakeModel([
            ModelResponse(tool_call=call("c1", "write", key="same")),
            ModelResponse(tool_call=call("c2", "write", key="same")),
            ModelResponse(final_output="done"),
        ])
        runtime = AgentRuntime(model, self.registry(effects))
        runtime.run(AgentState("r7", "goal"))
        self.assertEqual(effects, ["orders"])
        self.assertIn("tool_result_reused", [event.kind for event in runtime.trace.events])

    def test_trace_contains_no_reasoning_field(self):
        runtime = AgentRuntime(FakeModel([ModelResponse(final_output="done")]), self.registry())
        runtime.run(AgentState("r8", "goal"))
        serialized_keys = {key for event in runtime.trace.events for key in event.data}
        self.assertTrue({"reasoning", "chain_of_thought", "thought"}.isdisjoint(serialized_keys))


if __name__ == "__main__":
    unittest.main()
