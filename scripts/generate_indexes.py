#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    glossary = json.loads((ROOT / "catalog/glossary.yaml").read_text(encoding="utf-8"))
    timeline = json.loads((ROOT / "catalog/timeline.yaml").read_text(encoding="utf-8"))
    print(f"index inputs ok: {len(glossary)} terms, {len(timeline)} milestones")


if __name__ == "__main__":
    main()
