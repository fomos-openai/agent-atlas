import json
from pathlib import Path


def score(case: dict) -> dict[str, object]:
    result_ok = case["result"] == case["expected"]
    violations = sorted(set(case["events"]) & set(case["forbidden"]))
    return {"id": case["id"], "passed": result_ok and not violations, "violations": violations}


def evaluate(path: Path | None = None) -> list[dict[str, object]]:
    target = path or Path(__file__).with_name("cases.json")
    return [score(case) for case in json.loads(target.read_text(encoding="utf-8"))]


if __name__ == "__main__":
    print(json.dumps(evaluate(), ensure_ascii=False, indent=2))
