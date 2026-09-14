# Architecture

## 1. Case definition

Each case freezes a proposition, context, and independent-cluster threshold in `definition_hash`. The definition is the semantic namespace under which all later evidence is judged.

## 2. Evidence admission

During `OPEN`, anyone may submit a unique public HTTPS URL with a short label. URLs are normalized and checked against obvious local/private-host forms. Submission does not make an item countable.

## 3. Seal

The creator seals the case. The exact ordered evidence membership becomes `evidence_set_hash`. From this point onward no new evidence may enter.

## 4. Evidence assessment

Each evidence URL is independently fetched by leader and validators. An LLM classifies its stance relative to the frozen proposition/context. The security-critical field is the stance enum; explanatory text is stored for auditability but never directly drives quorum arithmetic.

Countable stances are `SUPPORTS` and `CONTRADICTS`. `IRRELEVANT`, `UNAVAILABLE`, and `AMBIGUOUS` do not count.

## 5. Pair relation matrix

Every unordered pair of countable evidence items must receive a consensus-backed relation:

- `INDEPENDENT`
- `LEFT_DERIVED_FROM_RIGHT`
- `RIGHT_DERIVED_FROM_LEFT`
- `SHARED_ORIGIN`
- `DEPENDENCE_AMBIGUOUS`

The pair classifier independently fetches both sources. A relation other than `INDEPENDENT` becomes a lineage edge.

## 6. Deterministic clustering

At finalization the contract verifies matrix completeness, then runs deterministic union-find over countable evidence IDs. All lineage edges join components. Because ambiguous dependence is also an edge, uncertainty cannot manufacture a new independent cluster.

The root/cluster identifier is deterministic: the minimum evidence ID in the connected component.

## 7. Cluster stance

For each component:

- support only -> `SUPPORT`
- contradiction only -> `CONTRADICTION`
- both -> `MIXED`

A mixed component counts toward neither side.

## 8. Final verdict

Let `k` be the frozen threshold.

- support >= k and contradiction >= k -> `CONTESTED`
- support >= k -> `SUPPORT_CORROBORATED`
- contradiction >= k -> `CONTRADICTION_CORROBORATED`
- otherwise -> `INSUFFICIENT`

The LLM never performs this calculation.

## 9. Consumer contract

`EvidenceGate` performs a typed IC-to-IC read against `is_corroborated`. The caller must pin:

- case ID
- exact definition hash
- exact finalization hash
- required side (support or contradiction)
- one-time action hash

This makes stale-result substitution and replay observable and rejectable.
