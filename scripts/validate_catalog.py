#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_SCHEMAS = {
    "sources.yaml": "source.schema.json",
    "claims.yaml": "claim.schema.json",
    "timeline.yaml": "timeline.schema.json",
    "glossary.yaml": "glossary.schema.json",
    "technologies.yaml": "technology.schema.json",
    "benchmarks.yaml": "benchmark.schema.json",
}


def load(name: str):
    return json.loads((ROOT / "catalog" / name).read_text(encoding="utf-8"))


def validate_required_fields(filename: str, data: object) -> None:
    """Validate the repository's deliberately small JSON Schema subset offline."""
    schema_name = CATALOG_SCHEMAS[filename]
    schema = json.loads(
        (ROOT / "catalog" / "schemas" / schema_name).read_text(encoding="utf-8")
    )
    assert schema.get("type") == "array", f"{schema_name}: root must be an array"
    assert isinstance(data, list), f"{filename}: root must be an array"
    required = schema.get("items", {}).get("required", [])
    for index, item in enumerate(data):
        assert isinstance(item, dict), f"{filename}[{index}]: item must be an object"
        missing = [field for field in required if field not in item]
        assert not missing, f"{filename}[{index}]: missing {missing}"


def main() -> None:
    catalogs = {filename: load(filename) for filename in CATALOG_SCHEMAS}
    for filename, data in catalogs.items():
        validate_required_fields(filename, data)

    sources = catalogs["sources.yaml"]
    source_ids = [item["id"] for item in sources]
    assert len(source_ids) == len(set(source_ids)), "duplicate source id"
    known = set(source_ids)
    for filename in ("claims.yaml", "timeline.yaml"):
        for item in catalogs[filename]:
            missing = set(item["source_ids"]) - known
            assert not missing, f"{filename}: unknown sources {sorted(missing)}"
    for item in catalogs["technologies.yaml"] + catalogs["benchmarks.yaml"]:
        assert item["source_id"] in known, f"unknown source in {item['id']}"
    print(f"catalog ok: {len(sources)} sources")


if __name__ == "__main__":
    main()
