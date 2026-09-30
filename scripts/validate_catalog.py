#!/usr/bin/env python3
from __future__ import annotations

import re

from common import ROOT, load_json_yaml

FILES = {
    "sources": {"id", "title", "url", "publisher", "published", "accessed", "kind", "authority", "volatility", "tags"},
    "claims": {"id", "claim", "claim_type", "source_ids", "confidence", "status", "as_of", "falsifiers"},
    "glossary": {"term", "zh", "definition"},
    "technologies": {"id", "name", "layer", "maturity", "version", "languages", "license", "deployment_model", "source_ids", "last_verified"},
    "benchmarks": {"id", "name", "domain", "measures", "source_ids", "caveat"},
    "patterns": {"id", "name", "problem", "forces", "solution", "consequences", "source_ids"},
    "cases": {"id", "name", "scenario", "risk_tier", "inputs", "outputs", "acceptance", "source_ids"},
}


def main() -> None:
    datasets = {name: load_json_yaml(ROOT / "catalog" / f"{name}.yaml") for name in FILES}
    source_ids = {item["id"] for item in datasets["sources"]}
    errors = []
    for name, required in FILES.items():
        seen = set()
        for index, item in enumerate(datasets[name]):
            missing = required - item.keys()
            if missing: errors.append(f"{name}[{index}] missing {sorted(missing)}")
            item_id = item.get("id", item.get("term"))
            if not item_id or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", item_id): errors.append(f"{name}[{index}] invalid id")
            if item_id in seen: errors.append(f"{name}: duplicate id {item_id}")
            seen.add(item_id)
            for source_id in item.get("source_ids", []):
                if source_id not in source_ids: errors.append(f"{name}:{item_id} unknown source {source_id}")
    bib = (ROOT / "catalog/references.bib").read_text(encoding="utf-8")
    for source_id in source_ids:
        if not re.search(r"@[A-Za-z]+\{" + re.escape(source_id) + r",", bib): errors.append(f"missing BibTeX entry: {source_id}")
    schemas = list((ROOT / "catalog/schemas").glob("*.json")) + list((ROOT / "labs/contracts").glob("*.json"))
    for schema in schemas: load_json_yaml(schema)
    if errors: raise SystemExit("catalog validation failed:\n- " + "\n- ".join(errors))
    print(f"catalog ok: {len(source_ids)} sources, {sum(map(len, datasets.values()))} records, {len(schemas)} schemas")


if __name__ == "__main__": main()
