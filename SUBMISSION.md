# Submission framing

## Title

Corroborate — Independence-Aware Evidence Quorum for GenLayer

## One-line description

A reusable Intelligent Contract that prevents source-count inflation by clustering semantically dependent evidence before applying deterministic corroboration thresholds.

## Why this needs GenLayer

The hard part is not adding integers. It is deciding whether unstructured sources actually support a frozen proposition and whether apparently different sources are informationally independent. Those are semantic judgments over live external content. GenLayer provides consensus over those nondeterministic judgments; Corroborate then turns the accepted decisions into deterministic, reviewable state.

## Why this is not a thin LLM wrapper

The model never decides the final verdict. The contract owns an immutable case definition, sealed evidence set, pair-completeness requirement, conservative dependence graph, deterministic connected components, cluster-level stance aggregation, quorum rules, immutable finalization hash, and a typed consumer gate with replay protection.

## Reuse surface

Other contracts can consume:

- `is_corroborated(...)`
- `get_case(...)`
- `get_evidence(...)`
- `get_pair_decision(...)`
- `get_cluster_for_evidence(...)`

Potential consumers include dispute systems, oracle settlement, research verification, claims review, governance, insurance, prediction settlement, reputation, moderation, procurement, and compliance workflows.

## Non-goals

Corroborate does not claim philosophical truth, score publisher reputation, create a news product, summarize the web, or replace domain-specific adjudication. It measures independent corroboration under an explicit frozen case definition.
