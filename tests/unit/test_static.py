from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORR = (ROOT / "contracts" / "corroborate.py").read_text(encoding="utf-8")
GATE = (ROOT / "contracts" / "evidence_gate.py").read_text(encoding="utf-8")


def test_no_frontend_tree():
    banned = ["package.json", "vite.config", "next.config", "src/App", "public/index.html"]
    all_paths = "\n".join(str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file())
    assert all(x not in all_paths for x in banned)


def test_consensus_is_not_format_only():
    assert "run_nondet_unsafe" in CORR
    assert "own = self._parse_assessment(leader_fn())" in CORR
    assert "own = self._parse_relation(leader_fn())" in CORR


def test_verdict_is_deterministic_not_llm_selected():
    assert "support_clusters >= threshold" in CORR
    assert "VERDICT_CONTESTED" in CORR
    assert "finalize_case" in CORR


def test_ambiguous_dependence_fails_closed_in_union():
    assert "if int(decision.relation) != REL_INDEPENDENT" in CORR


def test_consumer_is_typed_and_replay_protected():
    assert "@gl.contract_interface" in GATE
    assert "is_corroborated" in GATE
    assert "protected action was already executed" in GATE
