#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

from common import ROOT


def main() -> None:
    errors = []
    files = list(ROOT.glob("*.md")) + list((ROOT / "content").rglob("*.qmd")) + list((ROOT / "content").rglob("*.md"))
    pattern = re.compile(r"!?\[[^]]*\]\(([^)]+)\)")
    for path in files:
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            target = target.split(" ", 1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")): continue
            clean = unquote(target.split("#", 1)[0])
            if clean and not (path.parent / clean).resolve().exists(): errors.append(f"{path}: missing {target}")
    if errors: raise SystemExit("internal link validation failed:\n- " + "\n- ".join(errors))
    print(f"internal links ok: {len(files)} files")


if __name__ == "__main__": main()
