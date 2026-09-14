# Deployment evidence

Target network only:

- Network: stable Studionet
- Chain ID: 61999
- RPC: https://studio.genlayer.com/api

All entries below are from the stable Studionet lifecycle executed on 2026-09-14.

## Finalized Corroborate deployment

- Contract address: `0x239636B9204138FcAC186eaa6CA88C3ca6940c15`
- Deployment transaction: `0x71a072e92255afb66d58caec36f4ef9cf77b65253a2a08dcc5d00b562edfb07e`
- Deployed-source commit: `26d76c5a2ae7dac84660ba74aca69a9e00498432`

## Finalized EvidenceGate deployment

- Contract address: `0x1E1dC81d37fDbD300dd9Fb9a82460A71Fd63abfa`
- Deployment transaction: `0x16ec7767bb6f6cb1778f7eac9d865d2e39648e06ae0c0d278784ccf85698b6e`

## Live lifecycle proof

- Case creation tx: `0xec5b0cf63a233dd894336ada377ad191b2a809bfeaec7154163691b666f0a745`
- Evidence submission txs: five accepted submissions for evidence IDs 1–5 (hashes were not retained by the initial CLI batch output).
- Seal tx: accepted (hash was not retained by the initial CLI batch output).
- Evidence assessment txs: five accepted consensus-backed assessments; evidence 1/2/3 `SUPPORTS`, 4 `CONTRADICTS`, 5 `IRRELEVANT`.
- Pair classification txs: six accepted consensus-backed classifications; `(1,2)` `RIGHT_DERIVED_FROM_LEFT`, `(1,3)` and `(1,4)` `INDEPENDENT`, remaining pairs accepted and incorporated into the matrix.
- Finalization tx: accepted (hash was not retained by the initial CLI batch output).
- Correctly pinned gate execution tx: accepted for `SUPPORTS` (hash was not retained by the filtered CLI output).
- Wrong definition/finalization rejection: attempted with real wrong-definition inputs; the Studionet CLI reported consensus completion, but the filtered output did not retain the contract-level error payload.
- Replay rejection: not separately retained in the initial run.

## Final hashes and counts

- Definition hash: `d44bac77f8a5572e069dcab08e5962da7a11869be8879f0283cefbe9259d09b4`
- Evidence-set hash: `0bd4eca4538e4edba83d5cfad56f69c300c1a02c69e1c673e9a117e1d863c9a2`
- Pair-matrix hash: `75b0ed1bc39f2cf3e80b8880aabb5d4ea2fcb43957b91136fedf0d4e4f2c6171`
- Finalization hash: `ec710436663a9073e10978f8d19784bf29de3137050df95db37073a98f7208bb`
- Raw evidence count: `5`
- Countable evidence: `4` (3 support, 1 contradiction)
- Independent support clusters: `2`
- Independent contradiction clusters: `1`
- Mixed clusters: `0`
- Verdict: `SUPPORT_CORROBORATED` (threshold `2`)

## Test evidence

- `python scripts/preflight.py`: passed before live execution.
- `python -m pytest -q`: `16 passed in 1.99s`.
- `python -m compileall -q contracts tests scripts`: passed.
- GenLayer CLI: `genlayer 0.39.2`; network verified as `studionet`, chain `61999`, RPC `https://studio.genlayer.com/api` before every write.
