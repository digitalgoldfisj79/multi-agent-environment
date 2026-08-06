#!/usr/bin/env python3
"""Static and exact audit for the INT-LCSK tree-graph execution."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROGRAMME = ROOT / "fortune-int-lcsk-tree-graph"
LEAN = (
    ROOT
    / "fortune-formal"
    / "FortuneFormal"
    / "Integer"
    / "LocalConnectedTreeObstruction.lean"
)
ROOT_IMPORT = ROOT / "fortune-formal" / "FortuneFormal.lean"

REQUIRED = [
    PROGRAMME / "README.md",
    PROGRAMME / "PROGRAMME.md",
    PROGRAMME / "TARGET.md",
    PROGRAMME / "SOURCE_AUDIT.md",
    PROGRAMME / "EXECUTION.md",
    PROGRAMME / "FINAL_STATUS.md",
    PROGRAMME / "FORMALISATION_PLAN.md",
    PROGRAMME / "PREREGISTERED_GATES.json",
    PROGRAMME / "CLAIM_MATRIX.json",
    PROGRAMME / "scripts" / "verify_tree_graph.py",
    LEAN,
    ROOT_IMPORT,
]


def require_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file()]
    assert not missing, f"missing required files: {missing}"


def verify_json() -> None:
    gates = json.loads((PROGRAMME / "PREREGISTERED_GATES.json").read_text())
    claims = json.loads((PROGRAMME / "CLAIM_MATRIX.json").read_text())
    assert gates["programme"] == "FORTUNE_INT_LCSK_TREE_GRAPH_V0_1"
    assert {gate["id"] for gate in gates["gates"]} == {f"L{i}" for i in range(9)}
    assert claims["execution_state"] == "EXECUTED_AND_VALIDATED"
    assert claims["validation"]["workflow_run_id"] == 31081057533
    claim_ids = {claim["id"] for claim in claims["claims"]}
    assert {
        "LCSK-TG-PAIR",
        "LCSK-TG-TRIPLE",
        "LCSK-TG-OBSTRUCTION",
        "LCSK-HYPEREDGE-EXPONENT",
        "INT-LCSK",
    } <= claim_ids


def verify_lean_boundary() -> None:
    text = LEAN.read_text()
    for pattern in (r"\bsorry\b", r"\badmit\b", r"\baxiom\b", r"\bunsafe\b"):
        assert re.search(pattern, text) is None, f"forbidden Lean token: {pattern}"
    for theorem in (
        "normalizedPairCollision",
        "normalizedTripleCollisionCumulant",
        "tripleCollisionExceedsPairTree",
        "absoluteHyperedgeExponentGap",
    ):
        assert f"theorem {theorem}" in text, theorem
    assert "import FortuneFormal.Integer.LocalConnectedTreeObstruction" in ROOT_IMPORT.read_text()


def verify_claim_hygiene() -> None:
    text = "\n".join(path.read_text() for path in REQUIRED if path.suffix in {".md", ".json"})
    for phrase in (
        "PAIR_TREE_MAJORANT_REFUTED",
        "ABSOLUTE_HYPEREDGE_RADIUS_INSUFFICIENT",
        "REDUCED_TO_SIGNED_HIGHER_BODY_CLUSTER_THEOREM",
        "No proof or disproof of `INT-LCSK` is claimed.",
        "No proof of `INT-SOCG`, `INT-AOD` or Fortune is claimed.",
    ):
        assert phrase in text, phrase


def run_exact_regression() -> None:
    subprocess.run(
        [sys.executable, str(PROGRAMME / "scripts" / "verify_tree_graph.py")],
        check=True,
        cwd=ROOT,
    )


def main() -> None:
    require_files()
    verify_json()
    verify_lean_boundary()
    verify_claim_hygiene()
    run_exact_regression()
    print("FORTUNE_INT_LCSK_TREE_GRAPH_PROGRAMME_PASS")


if __name__ == "__main__":
    main()
