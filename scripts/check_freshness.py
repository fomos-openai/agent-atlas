#!/usr/bin/env python3
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CUTOFF = date(2026, 9, 30)


def main() -> None:
    stale = []
    for page in (ROOT / "knowledge").rglob("*.md"):
        text = page.read_text(encoding="utf-8")
        match = re.search(r"^last_verified:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
        assert match, f"missing last_verified: {page}"
        age = (CUTOFF - date.fromisoformat(match.group(1))).days
        if age > 90:
            stale.append(str(page.relative_to(ROOT)))
    assert not stale, "stale pages: " + ", ".join(stale)
    print("freshness ok")


if __name__ == "__main__":
    main()
