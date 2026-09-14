# Build status

This repository is the completed review-ready submission for Corroborate.

Implemented in the starter:

- standalone Corroborate contract architecture
- case/evidence/pair/finalization state model
- independent leader/validator semantic paths
- deterministic connected-component cluster computation
- fail-closed ambiguous-dependence rule
- immutable case/evidence/matrix/finalization hashes
- typed EvidenceGate consumer with replay protection
- direct-mode test suite scaffold with adversarial cases
- immutable fixture set + commit pinning script
- preflight checks
- architecture, invariants, threat model, reviewer demo and submission docs

Validation and live deployment evidence are recorded in `DEPLOYMENT.md`.

The final commit includes the pinned immutable fixture URLs, stable-Studionet
addresses, deterministic case hashes, and the adversarial Direct Mode suite.
