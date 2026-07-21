# Documentation

All project documentation lives under this folder. Keep it here — do not scatter
docs across the repo root.

## Map

- **[scope.md](./scope.md)** — the north star: *what* this project is and *why* it
exists. Read this first.
- **[decisions/](./decisions/)** — Architecture Decision Records (ADRs). One short
file per significant decision, capturing the context, the decision, and its
consequences. Add a new numbered file when a real decision is made; never rewrite
history — supersede instead.
- **[slices/](./slices/)** — one file per vertical slice we build, containing its
user story, scope, entities, API surface, and acceptance criteria.

## Conventions

- ADRs are numbered sequentially: `NNNN-short-title.md`.
- Slices are numbered sequentially: `NNN-short-title.md`.
- Docs describe intent and decisions, not implementation detail that the code already
expresses.