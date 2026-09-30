# Contributing

## Writing contract

Every numbered chapter must include learning objectives, prerequisites, the engineering problem, historical or architectural context, a mechanism-level explanation, at least one figure, one trade-off table, one worked example, failure modes, production constraints, a checklist, exercises, and source-backed references.

Chapter front matter must provide:

`title`, `summary`, `part`, `chapter`, `status`, `as_of`, `prerequisites`, `learning_objectives`, `source_ids`, `labs`, `figures`, and `tags`.

Allowed status values are `stable`, `evolving`, `experimental`, and `speculative`.

## Evidence contract

- Register a source before citing it.
- Prefer papers, specifications, official documentation, official repositories and release notes.
- Record facts, inferences and scenarios separately.
- Quantitative claims must include measurement conditions.
- Do not reproduce hidden chain-of-thought. Store only inputs, outputs, decisions, tool calls, state transitions and auditable events.

## Verification

Run `make all`. When a PDF changes, also inspect the complete rendered page set produced by `make visual-check`. When an Archify diagram changes, rerun its showcase `finalize` workflow and inspect the requested captures.
