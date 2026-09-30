#!/usr/bin/env python3
from __future__ import annotations

import json

from common import ROOT, frontmatter


def main() -> None:
    errors = []
    used = set()
    for path in (ROOT / "content").rglob("*.qmd"):
        if not path.read_text(encoding="utf-8").startswith("---\n"): continue
        meta, _ = frontmatter(path)
        used.update(meta.get("figures", []))
    for figure in used:
        path = ROOT / "figures/rendered" / f"{figure}.svg"
        if not path.exists(): errors.append(f"missing {path}")
        elif "<title" not in path.read_text(encoding="utf-8") or "<desc" not in path.read_text(encoding="utf-8"): errors.append(f"{path}: missing accessible title/desc")
    map_source = ROOT / "maps/agent-atlas.architecture.json"
    data = json.loads(map_source.read_text(encoding="utf-8"))
    if len(data.get("components", [])) < 8: errors.append("knowledge map has fewer than 8 domains")
    for path in (ROOT / "artifacts/agent-knowledge-map.html",):
        if not path.exists() or path.stat().st_size < 50_000: errors.append(f"missing or incomplete {path}")
    if errors: raise SystemExit("figure validation failed:\n- " + "\n- ".join(errors))
    print(f"figures ok: {len(used)} chapter SVGs + Archify map")


if __name__ == "__main__": main()
