#!/usr/bin/env python3
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("title:", "summary:", "status:", "last_verified:", "source_ids:", "tags:")
ALLOWED = {"stable", "evolving", "experimental", "speculative"}


def main() -> None:
    pages = sorted((ROOT / "knowledge").rglob("*.md"))
    assert pages, "no knowledge pages"
    for page in pages:
        text = page.read_text(encoding="utf-8")
        assert text.startswith("---\n"), f"missing front matter: {page}"
        front = text.split("---", 2)[1]
        for key in REQUIRED:
            assert key in front, f"{page}: missing {key}"
        match = re.search(r"^status:\s*(\S+)", front, re.M)
        assert match and match.group(1) in ALLOWED, f"{page}: invalid status"
        assert len(text.splitlines()) >= 9, f"{page}: content too short"
    print(f"content ok: {len(pages)} pages")


if __name__ == "__main__":
    main()
