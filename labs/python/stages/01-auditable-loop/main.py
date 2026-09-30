from agent_atlas import AgentRuntime, AgentState, FakeModel, ModelResponse, ToolCall, ToolSpec, ToolRegistry


registry = ToolRegistry()
registry.register(ToolSpec("lookup_service", "读取服务目录", ("service_name",)), lambda args: {"service": args["service_name"], "tier": 1})
model = FakeModel([
    ModelResponse(tool_call=ToolCall("call-1", "lookup_service", {"service_name": "orders"}, "lookup-orders")),
    ModelResponse(final_output="订单服务为 Tier 1；建议先完成兼容性验证。"),
])
runtime = AgentRuntime(model, registry, max_steps=4)
state = runtime.run(AgentState("run-01", "评估订单服务数据库驱动升级"))

print(state.status.value, state.final_output)
for event in runtime.trace.events:
    print(event.sequence, event.kind, event.data)
