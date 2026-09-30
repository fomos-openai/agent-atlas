# Auditable evidence catalog

The catalog is machine-readable JSON stored in `.yaml` files; JSON is a strict subset of YAML and keeps the default validation path dependency-free.

- `sources.yaml`: one record per primary or authoritative source.
- `claims.yaml`: atomic fact, inference or scenario records.
- `technologies.yaml`: versioned technology radar entries.
- `benchmarks.yaml`: benchmark intent and caveats, not leaderboard snapshots.
- `patterns.yaml`: architecture patterns and their forces.
- `cases.yaml`: case-study contracts and acceptance criteria.
- `glossary.yaml`: Chinese terminology with canonical English names.

Every manuscript citation uses a source id that is also present in `references.bib`. Source freshness is checked according to its volatility class.
