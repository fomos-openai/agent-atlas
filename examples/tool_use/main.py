from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class Tool:
    handler: Callable[..., Any]
    required: frozenset[str]


def add(a: int, b: int) -> int:
    return a + b


TOOLS = {"add": Tool(add, frozenset({"a", "b"}))}


def execute(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    tool = TOOLS.get(name)
    if tool is None:
        return {"ok": False, "error": "unknown_tool"}
    if set(arguments) != set(tool.required):
        return {"ok": False, "error": "invalid_arguments"}
    try:
        return {"ok": True, "value": tool.handler(**arguments)}
    except (TypeError, ValueError) as exc:
        return {"ok": False, "error": "tool_failure", "detail": str(exc)}


if __name__ == "__main__":
    print(execute("add", {"a": 20, "b": 26}))
