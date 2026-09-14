# Corroborate

**Corroborate is an independence-aware evidence quorum primitive for GenLayer.**

Traditional quorum systems count submissions, attestations, or sources. That is unsafe when many apparent sources are merely copies, citations, syndications, or reinterpretations of the same original information. Corroborate asks a narrower question before anything is counted:

> Are these evidence items informationally independent, or are they part of the same evidence lineage?

Corroborate does **not** decide that a proposition is objectively true. It classifies each evidence item relative to a frozen proposition, classifies the dependence relation between every pair of countable evidence items, and then deterministically computes connected information-lineage clusters. Quorum is measured in clusters, never raw submissions.

## Protocol in one example

A case is created with proposition `P` and corroboration threshold `2`.

Five URLs are submitted:

- A: first-hand field report supporting P
- B: article that republishes A
- C: independent public record supporting P
- D: social post quoting B
- E: independent record contradicting P

After semantic assessment and the completed pair matrix, A/B/D form one information-lineage cluster, C forms another, and E forms a third. Corroborate therefore sees **2 independent support clusters and 1 independent contradiction cluster**, not 4 supporting sources versus 1 contradicting source.

## What GenLayer decides

Consensus is deliberately narrow:

1. **Evidence stance** — does an independently fetched source SUPPORT, CONTRADICT, fail to address, or fail to provide usable evidence for the frozen proposition?
2. **Pair relation** — are two countable evidence items independent, derived from one another, sharing a common origin, or too ambiguous to establish independence?

Validators independently fetch and re-evaluate the relevant source material. The leader's JSON shape alone is never trusted.

## What is deterministic

Everything after those semantic decisions:

- URL admission and duplicate prevention
- case lifecycle and immutable definition hash
- frozen evidence set hash
- pair-matrix completeness
- conservative treatment of ambiguous dependence
- connected-component lineage clustering
- per-cluster stance aggregation
- support / contradiction / mixed cluster counts
- final verdict
- finalization hash
- consumer pinning and action replay protection

## Lifecycle

`OPEN -> SEALED -> FINALIZED`

- **OPEN**: evidence URLs may be submitted.
- **SEALED**: evidence membership is frozen. Evidence assessments and pair classifications may be completed permissionlessly.
- **FINALIZED**: only after every countable pair has a consensus-backed relation. Clusters and verdict are computed deterministically and become immutable.

## Verdicts

- `INSUFFICIENT`: neither side reaches the configured independent-cluster threshold.
- `SUPPORT_CORROBORATED`: support reaches threshold and contradiction does not.
- `CONTRADICTION_CORROBORATED`: contradiction reaches threshold and support does not.
- `CONTESTED`: both support and contradiction independently reach threshold.

A cluster containing both supporting and contradicting evidence is `MIXED` and counts toward neither side. This prevents one shared information origin from being double-counted merely because downstream interpretations disagree.

## Conservative independence

Corroborate requires independence to be positively established. Pair outcomes other than `INDEPENDENT` create a lineage edge. `DEPENDENCE_AMBIGUOUS` therefore fails closed and joins the two items into the same connected component for quorum purposes.

## Contracts

- `contracts/corroborate.py` — reusable evidence-quorum primitive.
- `contracts/evidence_gate.py` — minimal consumer proving another IC can pin a finalized Corroborate result and reject replay.

## Reviewer-critical invariants

See `docs/INVARIANTS.md`. The most important are:

1. Raw evidence count is never used as quorum.
2. A case cannot finalize with an incomplete countable-pair matrix.
3. The LLM never computes the final case verdict.
4. Ambiguous dependence cannot increase independent cluster count.
5. Evidence membership cannot change after sealing.
6. A consumer can pin both the case definition and the exact finalization hash.

## Network

The submission targets stable GenLayer Studionet:

- alias: `studionet`
- chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- explorer: `https://explorer-studio.genlayer.com`

Do not silently switch this repository to the Studio development preview.

## Local validation

```bash
python scripts/preflight.py
python -m compileall contracts tests scripts
python -m pytest -q
```

The Direct Mode suite and live Studionet proof have been completed. Real deployment, lifecycle, hash, and transaction evidence is recorded in `DEPLOYMENT.md`.

## Immutable live fixtures

`fixtures/` contains small public-source fixtures for a reproducible live demonstration. `scripts/pin_fixture_commit.py` pins their raw GitHub URLs to the first real 40-character Git commit containing those fixtures.

## Repository boundary

Corroborate is a **standalone Intelligent Contract primitive**. It intentionally has no frontend, backend, database, wallet UI, dashboard, or off-chain adjudication service.
