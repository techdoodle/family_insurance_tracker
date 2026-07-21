# 0001 — Use PostgreSQL for storage

- **Status:** Accepted
- **Date:** 2026-07-21

## Context

The project needs durable storage for a household's insurance data. The data is
inherently **relational**: people, policies, who-covers-whom, nominees, documents,
and (later) claims, with relationships between them. The important queries are
relational too — e.g. "which active policies cover person X, and what stacks on top?"

Key facts about the context:

- **Low volume.** A household has dozens of policies, not millions. Load is not a concern.
- **Local, self-hosted, single household.** No cloud, no multi-tenant.
- **This is also a learning project** — building operational skill is an explicit goal.

Options considered:

- **JSON / flat-file storage** — rejected. No integrity guarantees, unsafe concurrent
  writes, and relational queries degrade into hand-written spaghetti.
- **SQLite** — strong contextual fit: relational, single file, zero-config, trivially
  backed up. Would arguably be the "simplest correct" choice for this scope.
- **PostgreSQL** — heavier to run (a server process) and arguably overkill for the
  scope, but teaches real database operations, containerisation, and migrations.

## Decision

Use **PostgreSQL**, chosen primarily for its **learning value** (running a real
database server, Docker, and proper migrations), not because it is popular. The
relational shape of the data rules out JSON; the remaining SQLite-vs-Postgres choice
was decided on learning value over minimal operational simplicity.

## Consequences

- A Postgres server must be running for the app to work — locally today, and for
  anyone who self-hosts later.
- **Reproducibility debt:** contributors should not have to hand-configure Postgres.
  Containerising the database is recorded as a later requirement (not done now).
- We gain a real reason to use schema migrations (see ADR 0003).
- Storage will sit behind a small repository interface so the database is swappable
  and the rest of the app does not depend on Postgres directly.
