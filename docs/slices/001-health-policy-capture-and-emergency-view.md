# Slice 001 — Health policy: capture and emergency view

- **Status:** Planned
- **Type in scope:** Health insurance only

## User story

As a family member, I can record a health insurance policy (with its document), and
later select a family member and instantly see their active health policies with the
details I'd need in an emergency — without opening the PDF.

## Why this slice

It exercises the full stack (form → API → database → file storage → read-back) *and*
touches the project's core value: emergency-mode retrieval. Storing data alone would
not prove anything the project exists for.

## Entities (minimum needed)

- **Person** — a household member. Needed because policies are filtered by *who is
  covered*, so a minimal Person concept must exist even if people are inserted manually.
- **HealthPolicy** — the policy record and its important fields.
- **PolicyDocument** — metadata for one stored file (see ADR 0002).
- **Coverage** — the link between people and policies. This is **many-to-many**: one
  family-floater policy can cover several people, and one person can be on several
  policies.

## Fields (initial, to be refined by research)

For a health policy:

- Insurer
- Product / policy name
- Policy number
- Coverage start date and end date
- Covered family members (one or more `Person`s)
- Sum insured
- TPA name
- Claims / TPA emergency phone number
- Cashless / network-hospital info or link

> **Open question:** confirm the exact field set by researching what dependents
> actually need at a hospital at 2 AM. This research refines fields but must not block
> building the basic data path.

## API surface (all under `/api/v1`)

- `POST /api/v1/health-policies` — create a policy (with covered people)
- `GET  /api/v1/health-policies?covered_person_id={id}` — list a person's policies
- `GET  /api/v1/health-policies/{id}` — one policy's details
- `GET  /api/v1/health-policies/{id}/document` — download the stored document

Filtering is on the **collection** endpoint (by *covered person*, not owner). A
dedicated `/search` endpoint is unnecessary at this stage.

## Emergency flow (read path)

1. User selects a family member.
2. Type defaults to Health for this slice.
3. UI fetches that person's matching active policies.
4. Results show the important details immediately (insurer, policy number, coverage
   dates/status, TPA + emergency phone, sum insured, covered members).
5. Each result offers **View details** and **Download document**.

The PDF download is supporting evidence, **not** the primary outcome — the actionable
information must be visible without opening the file.

## Acceptance criteria

A family member can:

1. Open a health-policy form and enter the fields above.
2. Attach one PDF policy document.
3. Save the policy and receive a clear success result.
4. Select a family member and see their active health policies listed with the
   important fields.
5. Open a policy's emergency view and read the important fields without opening the PDF.
6. Download the same PDF that was uploaded.
7. Retrieve everything after restarting the application (data is durable).

## Explicitly out of scope for this slice

- Other insurance types (life, motor, home, etc.).
- Inferring whether a claim *is covered*. This slice reports **what was recorded**, not
  coverage judgements.
- Editing/deleting policies, authentication, lifecycle alerts, and multi-document upload.
