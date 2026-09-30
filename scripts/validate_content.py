#!/usr/bin/env python3
from __future__ import annotations

import re

from common import ROOT, frontmatter, load_json_yaml

REQUIRED = {"title", "summary", "part", "chapter", "status", "as_of", "prerequisites", "learning_objectives", "source_ids", "labs", "figures", "tags"}
STATUSES = {"stable", "evolving", "experimental", "speculative"}


def main() -> None:
    sources = {item["id"] for item in load_json_yaml(ROOT / "catalog/sources.yaml")}
    chapters = sorted((ROOT / "content").glob("[0-9][0-9]-*/*.qmd"))
    errors = []
    for path in chapters:
        meta, body = frontmatter(path)
        if missing := REQUIRED - meta.keys(): errors.append(f"{path}: missing {sorted(missing)}")
        if meta.get("status") not in STATUSES: errors.append(f"{path}: bad status")
        if meta.get("as_of") != "2026-10-01": errors.append(f"{path}: as_of must be 2026-10-01")
        for source_id in meta.get("source_ids", []):
            if source_id not in sources: errors.append(f"{path}: unknown source {source_id}")
        if meta.get("chapter") == 0:
            continue
        if len(re.sub(r"\s+", "", body)) < 6000: errors.append(f"{path}: sample chapter below 6000 non-space characters")
        for marker in ("## 本章要解决的问题", "## 本章小结", "## 思考与实践", "## 生产"):
            if marker not in body: errors.append(f"{path}: missing section marker {marker}")
        if not re.search(r"\|.+\|", body): errors.append(f"{path}: missing trade-off table")
        if "![" not in body: errors.append(f"{path}: missing referenced figure")
        if "- [ ]" not in body: errors.append(f"{path}: missing checklist")
        if re.search(r"\b(TODO|TBD|PLACEHOLDER)\b|待补充|占位", body, re.I): errors.append(f"{path}: placeholder text")
    if len(chapters) != 3:  # reading guide plus two full sample chapters
        errors.append(f"foundation expects 3 content chapters, found {len(chapters)}")
    if errors: raise SystemExit("content validation failed:\n- " + "\n- ".join(errors))
    chars = sum(len(frontmatter(path)[1]) for path in chapters)
    print(f"content ok: {len(chapters)} chapters, {chars} body characters; foundation gate active")


if __name__ == "__main__": main()
