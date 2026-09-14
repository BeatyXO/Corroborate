# Protocol invariants

1. **No raw-count quorum** — final quorum depends only on connected information-lineage clusters.
2. **Immutable semantic namespace** — proposition, context and threshold cannot change after case creation.
3. **Frozen membership** — evidence cannot be added after seal.
4. **One URL, one evidence item per case** — normalized duplicate URLs are rejected.
5. **Assessment before pair classification** — unassessed evidence cannot participate in the matrix.
6. **Countable-only matrix** — only SUPPORTS/CONTRADICTS items require pair decisions.
7. **Complete matrix before finalization** — every unordered countable pair must have exactly one accepted relation.
8. **Positive independence requirement** — only explicit `INDEPENDENT` avoids a lineage edge.
9. **Ambiguity fails closed** — ambiguous dependence can never increase independent cluster count.
10. **Deterministic component identity** — cluster root is the minimum evidence ID in the component.
11. **Mixed origin neutrality** — a lineage containing both support and contradiction counts toward neither side.
12. **LLM cannot choose final verdict** — verdict is derived from deterministic counts and frozen threshold.
13. **Finalization immutability** — a FINALIZED case cannot be reopened, reassessed or re-clustered.
14. **Consumer exact pinning** — downstream approval can require both definition hash and finalization hash.
15. **Replay resistance** — EvidenceGate accepts a protected action hash at most once.
