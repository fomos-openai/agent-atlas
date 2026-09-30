#!/usr/bin/env python3
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> None:
    checked = 0
    for page in ROOT.rglob("*.md"):
        for raw in LINK.findall(page.read_text(encoding="utf-8")):
            target = raw.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (page.parent / target).resolve()
            assert resolved.exists(), f"broken link: {page.relative_to(ROOT)} -> {raw}"
            checked += 1
    print(f"links ok: {checked} internal links")


if __name__ == "__main__":
    main()
