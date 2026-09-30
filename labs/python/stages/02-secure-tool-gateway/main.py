from agent_atlas import AgentRuntime, AgentState, FakeModel, ModelResponse, PolicyDecision, PolicyDecisionKind, ToolCall, ToolSpec, ToolRegistry


class GatewayPolicy:
    def evaluate(self, call, state):
        del state
        if call.tool_name == "submit_for_review":
            return PolicyDecision(PolicyDecisionKind.REQUIRE_APPROVAL, "EXTERNAL_COMMITMENT")
        return PolicyDecision(PolicyDecisionKind.ALLOW, "READ_OR_DRAFT")


effects = []
registry = ToolRegistry()
registry.register(ToolSpec("lookup_service", "读取权威服务目录", ("service_name",)), lambda args: {"owner": "commerce", **args})
registry.register(ToolSpec("submit_for_review", "向固定评审队列提交方案", ("proposal_id",), "external_commitment"), lambda args: effects.append(args["proposal_id"]) or {"ticket": "REV-42"})
model = FakeModel([
    ModelResponse(tool_call=ToolCall("read-1", "lookup_service", {"service_name": "orders"}, "read-orders")),
    ModelResponse(tool_call=ToolCall("submit-1", "submit_for_review", {"proposal_id": "change-42"}, "submit-change-42")),
    ModelResponse(final_output="方案已提交固定评审队列。"),
])
runtime = AgentRuntime(model, registry, GatewayPolicy())
state = runtime.run(AgentState("run-02", "生成并提交变更方案"))
print("before approval:", state.status.value, "effects:", effects)
state = runtime.run(state, approved_call_id="submit-1")
print("after approval:", state.status.value, "effects:", effects)
for event in runtime.trace.events:
    print(event.sequence, event.kind, event.data)
