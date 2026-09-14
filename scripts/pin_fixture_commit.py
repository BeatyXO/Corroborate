#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = re.compile(r"FIXTURE_[A-Z]+_PLACEHOLDER")

if len(sys.argv) != 2:
    raise SystemExit("usage: python scripts/pin_fixture_commit.py <40-char-commit-sha>")
sha = sys.argv[1].strip().lower()
if not re.fullmatch(r"[0-9a-f]{40}", sha):
    raise SystemExit("commit SHA must be exactly 40 lowercase hex characters")

# Files containing raw fixture URL templates are intentionally small and explicit.
targets = [ROOT / "docs" / "LIVE_FIXTURES.md"]
changed = 0
for path in targets:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER.search(text):
        path.write_text(PLACEHOLDER.sub(sha, text), encoding="utf-8")
        changed += 1
print(f"Pinned fixture commit {sha} in {changed} file(s).")
