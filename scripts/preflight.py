#!/usr/bin/env python3
from pathlib import Path
import argparse, re, sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md", "SUBMISSION.md", "DEPLOYMENT.md", "BUILD_STATUS.md",
    "contracts/corroborate.py", "contracts/evidence_gate.py",
    "docs/ARCHITECTURE.md", "docs/INVARIANTS.md", "docs/THREAT_MODEL.md",
    "docs/REVIEWER_DEMO.md", "tests/direct/test_corroborate.py",
    "tests/unit/test_static.py", "fixtures/support_primary_a.md",
    "scripts/pin_fixture_commit.py",
]
BANNED_PARTS = ["node_modules", ".venv", "venv", "__pycache__", ".pytest_cache"]
SECRET_PATTERNS = [
    re.compile(r"(?i)private[_ -]?key\s*=\s*[0-9a-f]{64}"),
    re.compile(r"(?i)mnemonic\s*=\s*[^\n]{20,}"),
]


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", action="store_true")
    args = ap.parse_args()
    errors = 0
    for rel in REQUIRED:
        if not (ROOT / rel).exists(): errors += fail(f"missing {rel}")
    for p in ROOT.rglob("*"):
        if any(part in BANNED_PARTS for part in p.parts): errors += fail(f"banned artifact {p}")
        if p.is_file() and p.stat().st_size < 2_000_000:
            try: text = p.read_text(encoding="utf-8")
            except Exception: continue
            for pat in SECRET_PATTERNS:
                if pat.search(text): errors += fail(f"possible secret in {p}")
    all_text = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in ROOT.rglob("*") if p.is_file() and p.stat().st_size < 1_000_000
    )
    if "61999" not in all_text or "https://studio.genlayer.com/api" not in all_text:
        errors += fail("stable Studionet network references missing")
    config_text = (ROOT / "gltest.config.yaml").read_text(encoding="utf-8")
    if "61997" in config_text or "studio-dev.genlayer.com" in config_text:
        errors += fail("gltest config must not target Studio development preview")
    if args.final:
        if re.search(r"FIXTURE_[A-Z]+_PLACEHOLDER", all_text):
            errors += fail("immutable fixture commit is not pinned")
        deployment = (ROOT / "DEPLOYMENT.md").read_text(encoding="utf-8")
        if "`TBD`" in deployment:
            errors += fail("DEPLOYMENT.md still contains TBD proof")
    if errors:
        print(f"Preflight failed with {errors} issue(s).")
        return 1
    print("Preflight passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
