from examples.shared.fake_model import FakeModel
from examples.shared.types import ModelDecision, RunState, ToolCall


def run(goal: str, max_steps: int = 4) -> RunState:
    def policy(state: RunState, _: list[str]) -> ModelDecision:
        if not state.observations:
            return ModelDecision("tool", tool_call=ToolCall("inspect", {"topic": goal}))
        return ModelDecision("final", content=f"基于观察完成：{state.observations[-1]}")

    model = FakeModel(policy)
    state = RunState(goal=goal)
    for step in range(max_steps):
        state.step = step + 1
        decision = model.decide(state, ["inspect"])
        state.events.append({"step": state.step, "decision": decision.kind})
        if decision.kind == "final":
            state.events.append({"final": decision.content, "stop_reason": "success"})
            return state
        call = decision.tool_call
        if call is None or call.name != "inspect":
            raise RuntimeError("unsupported tool")
        state.observations.append(f"{call.arguments['topic']} 已检查")
    state.events.append({"stop_reason": "max_steps"})
    return state


if __name__ == "__main__":
    result = run("Agent loop")
    print(result.events)
