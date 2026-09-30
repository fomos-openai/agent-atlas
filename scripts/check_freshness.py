#!/usr/bin/env python3
from __future__ import annotations

from datetime import date

from common import ROOT, load_json_yaml

LIMIT = {"fast": 30, "evolving": 90, "stable": 365}
AS_OF = date.fromisoformat("2026-10-01")


def main() -> None:
    errors = []
    for source in load_json_yaml(ROOT / "catalog/sources.yaml"):
        age = (AS_OF - date.fromisoformat(source["accessed"])).days
        if age > LIMIT[source["volatility"]]: errors.append(f"{source['id']}: {age}d > {LIMIT[source['volatility']]}d")
    if errors: raise SystemExit("freshness validation failed:\n- " + "\n- ".join(errors))
    print("freshness ok: snapshot 2026-10-01")


if __name__ == "__main__": main()
