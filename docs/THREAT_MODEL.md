# Threat model

## Sybil source inflation

Attack: submit many mirrors/reposts of one original report.

Control: pairwise dependence classification plus connected-component quorum. Mirrors can enlarge a cluster but not the independent-cluster count.

## Citation laundering

Attack: a secondary article cites an intermediary rather than the original and appears independent.

Control: relation prompt asks about shared informational origin and derivation, not merely direct hyperlinks.

## Ambiguous provenance

Attack: provenance is unclear, so the system guesses independence.

Control: `DEPENDENCE_AMBIGUOUS` is conservative and creates a lineage edge.

## Leader fabrication

Attack: leader returns a plausible classification without actually grounding it in the source.

Control: validators independently fetch and re-run the substantive classification; format-only validation is not sufficient.

## Prompt injection inside evidence

Attack: fetched source text tells the validator to ignore protocol instructions or return a chosen label.

Control: prompts explicitly treat source content as untrusted evidence and demand fixed-schema classification only. Deterministic parser rejects malformed/unknown enums.

## Mutable web pages

Attack: a page changes between validators or after assessment.

Control: the live reviewer fixture path uses immutable commit-pinned raw URLs. General production callers should prefer immutable/archived sources. Accepted assessments are historical observations; Corroborate does not pretend mutable web content is permanent truth.

## Incomplete pair matrix

Attack: finalize before comparing an inconvenient pair.

Control: deterministic finalization rejects unless all unordered pairs among countable evidence are present.

## Pair poisoning

Attack: an irrelevant/unavailable item creates artificial lineage edges.

Control: only SUPPORTS/CONTRADICTS evidence enters the required pair matrix or cluster computation.

## Result substitution

Attack: downstream consumer is shown a different case definition or later finalization than expected.

Control: `EvidenceGate` pins both hashes and required side.

## Replay

Attack: reuse one corroborated decision for the same protected side effect multiple times.

Control: one-time `action_hash` registry in EvidenceGate.
