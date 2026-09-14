# Reviewer demo

Use the immutable raw GitHub fixture URLs after `scripts/pin_fixture_commit.py` has replaced the placeholder.

Suggested case:

- Proposition: `The Harbor Delta sensor station reported a pressure excursion above its operating threshold during the 2026-09-10 test window.`
- Context: evidence must concern the same station and test window; repetition of an earlier report is not independent corroboration.
- Threshold: `2`

Submit:

1. `support_primary_a.md` — first-hand engineering log, SUPPORTS.
2. `support_derivative_a.md` — explicitly republishes #1, SUPPORTS but dependent.
3. `support_independent_b.md` — separate instrument custodian log, SUPPORTS and independent from #1.
4. `contradict_independent_c.md` — separate calibration record, CONTRADICTS.
5. `irrelevant.md` — does not address the test window.

Expected semantic shape:

- #1 + #2 -> one lineage cluster.
- #3 -> independent support cluster.
- #4 -> independent contradiction cluster.
- #5 -> non-countable.

Expected deterministic result with threshold 2:

- raw evidence: 5
- countable evidence: 4
- support clusters: 2
- contradiction clusters: 1
- mixed clusters: 0
- verdict: `SUPPORT_CORROBORATED`

Then deploy `EvidenceGate`, pin the exact case definition/finalization hashes, execute one action successfully, prove wrong-hash rejection, then prove action replay rejection.
