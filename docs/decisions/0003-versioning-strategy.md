# 0003 — Versioning strategy

- **Status:** Accepted
- **Date:** 2026-07-21

## Context

"Versioning" can mean three unrelated things, each solved differently. Rather than
adopting all of them as blanket ceremony, each is turned on when it starts paying off.

## Decision

- **Schema / migration versioning — adopt now.** Use a migration tool (Alembic) from
  the very first table. Payoff is immediate: schema will change constantly and we must
  never drop tables and lose data by hand.
- **API versioning — adopt now.** Prefix routes with `/api/v1`. Cost is nearly zero (a
  route prefix) and it is annoying to retrofit, so it is worth having from the start,
  even though the only consumer today is our own UI.
- **Release versioning — adopt the discipline, use later.** Follow SemVer with git tags.
  The first meaningful working slice can be tagged `v0.1.0`; a `0.x` version signals the
  software is still evolving. No tag is cut before there is something usable to release.

## Consequences

- Every schema change ships as a migration; no manual DDL against the dev database.
- All endpoints live under `/api/v1`; a future `/api/v2` can coexist for breaking changes.
- Releases are tagged starting at `v0.1.0`, not `v1.0.0`.
