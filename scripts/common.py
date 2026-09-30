from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json_yaml(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_scalar(value: str):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [] if not inner else [item.strip().strip('"\'') for item in inner.split(",")]
    if re.fullmatch(r"\d+", value):
        return int(value)
    return value.strip('"\'')


def frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        raw, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError(f"{path}: unterminated YAML frontmatter") from exc
    data = {}
    for line in raw.splitlines():
        if not line.strip() or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = parse_scalar(value)
    return data, body
