#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [root / "artifacts/agent-atlas-book.zh-CN.pdf", root / "artifacts/agent-knowledge-map.html", root / "artifacts/agent-knowledge-map.png"]
missing = [str(path) for path in required if not path.exists()]
if missing: raise SystemExit("foundation release check missing:\n- " + "\n- ".join(missing))
print("foundation release check ok: review package complete (full-book metrics intentionally deferred)")
