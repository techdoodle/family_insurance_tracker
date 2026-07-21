# 0002 — Store documents on disk, metadata in the database

- **Status:** Accepted
- **Date:** 2026-07-21

## Context

Policies come with documents (policy schedules, health cards, receipts). We need to
store the original file and be able to retrieve it later.

Postgres *can* store binary data:

- `bytea` — practical limit ~1 GB per value, but large blobs inflate memory use and
  make database dumps/restores heavy.
- Large Objects — up to ~4 TB, but add API and lifecycle complexity.

Capacity is not the deciding factor here; operational simplicity and backup hygiene are.

## Decision

Store document **files on disk** under `family_docs/` (already gitignored), and store
only **metadata** in Postgres:

- internal id
- internally generated storage path / filename (do **not** trust the uploaded filename)
- original filename
- MIME type
- size in bytes
- checksum (for integrity)

## Consequences

- The database stays lean, so backups and restores stay fast.
- Backup now has **two** concerns — the database *and* the `family_docs/` files — which
  must be kept consistent.
- We must maintain integrity between a metadata row and its file (e.g. handle orphaned
  files or missing files).
- Privacy is preserved: `family_docs/` is gitignored, so real documents never enter git.
- The file-storage mechanism can later be swapped (e.g. encrypted-at-rest) without
  changing policy behaviour.
