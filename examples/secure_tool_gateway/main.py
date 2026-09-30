import hashlib
import json
from pathlib import Path
from typing import Any


def decide(action: str, arguments: dict[str, Any], policy_path: Path | None = None) -> dict[str, str]:
    target = policy_path or Path(__file__).with_name("policy.yaml")
    policy = json.loads(target.read_text(encoding="utf-8"))
    effect = policy.get(action, "deny")
    canonical = json.dumps({"action": action, "arguments": arguments}, sort_keys=True)
    return {"effect": effect, "approval_key": hashlib.sha256(canonical.encode()).hexdigest()[:16]}


if __name__ == "__main__":
    print(decide("send_email", {"to": "reviewer@example.com", "subject": "Atlas"}))
