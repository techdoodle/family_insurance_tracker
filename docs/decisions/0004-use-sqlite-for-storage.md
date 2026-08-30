# 0004 — Use SQLite for storage

- **Status:** Accepted
- **Date:** 2026-08-30
- **Supersedes:** [0001 — Use PostgreSQL for storage](./0001-use-postgresql.md)

## Context

ADR 0001 chose PostgreSQL primarily for **learning value** (running a server database,
Docker, operational practice). After initial setup, the operational cost outweighed
the benefit for the current phase:

- A Postgres server must be installed, started, and maintained locally.
- Connection URLs, sync/async drivers, and environment setup add friction before the
  first vertical slice is working.
- The project's actual requirements remain unchanged: single household, low read/write
  volume, local/self-hosted, relational data (people, policies, coverage, documents).

The relational data model and migration workflow (ADR 0003) are still required. Only
the **database engine** changes.

Options reconsidered:

- **Stay on PostgreSQL** — continues teaching server DB ops, but slows progress on
  slice 001 for limited gain at this scale.
- **SQLite** — single file, zero server, trivial backup (copy the file), same
  SQLAlchemy + Alembic stack. Strong fit for v0 and self-hosting by non-technical
  family members later.

## Decision

Use **SQLite** as the database for v0 and slice 001 onward.

- Store the database as a file in the project (e.g. `famsure.db` or under `data/`).
- Keep SQLAlchemy models, Alembic migrations, and the async app stack (`aiosqlite`).
- PostgreSQL may be revisited later if multi-user concurrency or deployment needs
  justify the complexity; the repository seam from ADR 0001 remains the escape hatch.

## Consequences

- **No database server** — clone, `poetry install`, migrate, run. Simpler for
  open-source adopters and aligns with "local and private" from scope.md.
- **Backup** — copy the `.db` file (and `family_docs/`); both must stay in sync
  with document metadata in the database.
- **Gitignore** — the SQLite file must never be committed (real family data).
- **Alembic** — enable batch mode (`render_as_batch=True`) in `env.py` for SQLite-safe
  schema changes on later migrations.
- **Portability** — avoid PostgreSQL-specific column types (e.g. `JSONB`, native
  `ARRAY`); use portable SQLAlchemy types or join tables.
- **Concurrency** — acceptable for a single-household app with few concurrent writers;
  not suitable if the app later becomes multi-tenant or heavily concurrent.

## Implementation notes (for the developer)

These are reminders, not prescriptive steps — the owner implements:

| Area | Change |
|------|--------|
| `.env` | `DATABASE_URL=sqlite:///./famsure.db`, `ASYNC_DATABASE_URL=sqlite+aiosqlite:///./famsure.db` |
| Dependencies | Remove `asyncpg`; add `aiosqlite` |
| Alembic | Sync SQLite URL; `render_as_batch=True` |
| `.gitignore` | Ignore `*.db` (or chosen data directory) |
