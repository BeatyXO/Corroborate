# Immutable live fixture URLs

Push `fixtures/` first, obtain that exact 40-character commit SHA, then run:

```bash
python scripts/pin_fixture_commit.py <FULL_COMMIT_SHA>
```

Pinned base:

`https://raw.githubusercontent.com/BeatyXO/Corroborate/FIXTURE_COMMIT_PLACEHOLDER/fixtures/`

Files:

- `support_primary_a.md`
- `support_derivative_a.md`
- `support_independent_b.md`
- `contradict_independent_c.md`
- `irrelevant.md`

The final repository must not contain `FIXTURE_COMMIT_PLACEHOLDER`.
