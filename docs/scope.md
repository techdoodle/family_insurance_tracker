# What This Is

A living document describing *what* this project is and *why* it exists — not *how* it is built. If someone reads only this page, they should understand the problem, who it is for, and where the boundaries are.

> Status: early. This is the north star, not a contract. It will change as understanding improves.

---

## The one-sentence version

A private, self-hosted place for a family to keep every insurance policy together, so that in an emergency any family member can instantly find what is covered, who to call, and what to do.

---

## The problem

Insurance in an Indian family is scattered. Different people (self, spouse, parents, siblings) hold different policies (health, term/life, accident, motor, home) across different insurers, apps, emails, and physical folders. Nobody has the full picture.

The pain shows up at the worst possible time:

- A parent is hospitalised at night and nobody knows the policy number, the TPA helpline, or whether cashless is possible.
- Someone passes away and the nominee does not know which term policies exist or where the documents are.
- A premium quietly lapses, so a policy that everyone assumed was active cannot be claimed.
- An accident happens and it is unclear whether a personal-accident cover applies on top of health.

The recurring failure is not lack of insurance — it is lack of a single, trustworthy, up-to-date view when it matters.

---

## Who it is for

- **Primary:** my own family — me, my partner, my brother, my parents. One household, a handful of people, many policies.
- **Later (open source):** anyone who wants to run the same thing locally for their own family. Same shape of problem, different data.

It is explicitly **not** built for insurers, agents, or large-scale multi-tenant use.

---

## What success looks like

The project succeeds if, for every family member, it can calmly answer these at 2 AM:

1. Does this person have active cover for this situation, right now?
2. What is the policy number and the 24×7 claim / TPA helpline?
3. Is it cashless-friendly (network + TPA), or reimbursement only?
4. What else stacks on top (top-up, personal accident, employer group, riders)?
5. Who is the nominee, and where are the documents?
6. Were premiums paid — is the policy actually in force?

If those are answered without scrambling, the tool did its job.

---

## The two modes it must serve

### 1. Emergency mode (read, under stress)

Open one screen, filter by person and situation, and get: applicable policies, contacts to call first, IDs/cards to show, cashless likelihood, and a plain checklist of what to do next.

### 2. Stewardship mode (calm, ongoing upkeep)

Keep the data true over time: premium due dates, renewals/maturity, lapse/grace awareness, document custody, and coverage notes. This upkeep is what keeps emergency mode trustworthy.

---

## What it covers (scope)

**Insurance types, in rough priority:**

1. Health — individual, family floater, employer group, top-up / super top-up, critical illness
2. Life — term, endowment/ULIP/traditional
3. Personal accident
4. Motor — car / bike
5. Home / property
6. Travel and other niche covers — later

**Core things it keeps track of:**

- **People** in the household and how they relate.
- **Policies** — insurer, product, policy number, who is covered, sums, dates, status, nominee.
- **Claim operations** — TPA, helplines, health cards, intimation deadlines, cashless notes.
- **Documents** — policy schedules, endorsements, premium receipts, health cards.
- **Process playbooks** — reusable checklists for health cashless, health reimbursement, death claim, motor, home.
- **Lifecycle alerts** — premium due, renewal, maturity, lapse risk.

---

## What it is NOT (non-goals)

- Not a marketplace or a policy-comparison / buying tool.
- Not automatic sync with every insurer's systems (data is entered and maintained manually; official apps and the e-Insurance Account remain sources people should also keep).
- Not a replacement for insurer apps or the government e-Insurance repository — it is a **family-scoped, emergency-first** companion.
- Not legal or financial advice, and it does not file claims on anyone's behalf.
- Not a cloud SaaS. It runs locally / self-hosted, and privacy of family data is a first-class concern.

---

## Guiding principles

- **Emergency-first.** Every feature is judged by whether it helps in the moment that matters.
- **Truth over features.** A small amount of accurate, current data beats a large amount of stale data.
- **Local and private.** Family data stays under the family's control.
- **Honest simplicity.** Manual entry + documents + reminders + playbooks is a legitimate v1.
- **Learning in the open.** This is also a project to relearn solid engineering, and it will be shared publicly so others can run it themselves.

---

## Out of scope for now (explicitly parked)

- Consumer-friendly one-click distribution (e.g. a simple Docker setup for non-technical users) — planned eventually, not now.
- Multi-household / multi-tenant support.
- Integrations, imports, or AI extraction from policy PDFs.

---

## Open questions to revisit

- How much claim history to track (affects sum-insured left, NCB)?
- How to store sensitive identifiers (KYC) safely — pointers vs actual numbers.
- Whether to model coverage-gap analysis in v1 or later.
- Which single emergency scenario becomes the very first end-to-end slice.