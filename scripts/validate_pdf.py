#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader


def main() -> None:
    path = Path(sys.argv[1]).resolve()
    if not path.exists(): raise SystemExit(f"missing PDF: {path}")
    reader = PdfReader(path)
    pages = len(reader.pages)
    if not 12 <= pages <= 100: raise SystemExit(f"foundation sample expected 12-100 pages, got {pages}")
    sparse = []
    extracted = []
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        extracted.append(text)
        if len(text.strip()) < 20: sparse.append(i)
    if len(sparse) > pages // 4: raise SystemExit(f"too many sparse pages: {sparse}")
    width = float(reader.pages[0].mediabox.width)
    height = float(reader.pages[0].mediabox.height)
    if not (495 <= width <= 502 and 705 <= height <= 712): raise SystemExit(f"expected ISO B5, got {width:.1f}x{height:.1f}pt")
    if not reader.outline: raise SystemExit("PDF outline/bookmarks missing")
    mark_info = reader.trailer["/Root"].get("/MarkInfo")
    if not mark_info or not mark_info.get("/Marked"): raise SystemExit("tagged PDF metadata missing")
    if "工具契约" not in "\n".join(extracted) or "符号主义" not in "\n".join(extracted): raise SystemExit("sample chapters not extractable")
    out = path.parents[1] / "tmp/pdfs/rendered"
    out.mkdir(parents=True, exist_ok=True)
    subprocess.run(["pdftoppm", "-png", "-r", "110", str(path), str(out / "page")], check=True, stdout=subprocess.DEVNULL)
    images = list(out.glob("page-*.png"))
    if len(images) != pages: raise SystemExit(f"rendered {len(images)} of {pages} pages")
    print(f"pdf ok: {pages} ISO B5 pages, tagged/text extractable, bookmarks present, {len(images)} pages rendered; sparse={sparse}")


if __name__ == "__main__": main()
