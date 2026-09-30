#!/usr/bin/env python3
"""Apply book-level layout options that orange-book otherwise resets to A4."""
from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    marker = "#show: book.with(\n"
    replacement = marker + '  paper-size: "iso-b5",\n  margin: (x: 20mm, top: 22mm, bottom: 22mm),\n'
    if "paper-size: \"iso-b5\"" in text[text.find(marker):text.find(marker) + 180]:
        print("Typst book layout already finalized")
        return
    if text.count(marker) != 1:
        raise SystemExit("unable to locate unique orange-book entry point")
    path.write_text(text.replace(marker, replacement, 1), encoding="utf-8")
    print("Typst book layout finalized: ISO B5, 20/22 mm margins")


if __name__ == "__main__": main()
