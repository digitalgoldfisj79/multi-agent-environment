#!/usr/bin/env python3
"""Static, trust-boundary and exact-regression audit for executed INT-PWOC-SF."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROGRAMME = ROOT / "fortune-int-pwoc-squarefree"
LEAN = (
    ROOT
    / "fortune-formal"
    / "FortuneFormal"
    / "Integer"
    / "SquarefreeCompositeEnergyCriterion.lean"
)
ROOT_IMPORT = ROOT / "fortune-formal" / "FortuneFormal.lean"

REQUIRED = [
    PROGRAMME / "README.md",
    PROGRAMME / "PROGRAMME.md",
    PROGRAMME / "TARGET.md",
    PROGRAMME / "FORMALISATION_PLAN.md",
    PROGRAMME / "PREREGISTERED_GATES.json",
    PROGRAMME / "CLAIM_MATRIX.json",
    PROGRAMME / "P0_SOURCE_FREEZE.md",
    PROGRAMME / "P1_P5_EXECUTION.md",
    PROGRAMME / "P6_P8_EXECUTION.md",
    PROGRAMME / "P7_EXECUTION.md",
    PROGRAMME / "FINAL_STATUS.md",
    PROGRAMME / "scripts" / "verify_squarefree_walk.py",
    PROGRAMME / "scripts" / "run_execution_panels.py",
    LEAN,
    ROOT_IMPORT,
]


def require_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file()]
    assert not missing, f"missing required files: {missing}"


def verify_json() -> None:
    gates = json.loads((PROGRAMME / "PREREGISTERED_GATES.json").read_text())
    claims = json.loads((PROGRAMME / "CLAIM_MATRIX.json").read_text())
    assert gates["programme"] == "FORTUNE_INT_PWOC_SQUAREFREE_V0_1"
    assert {gate["id"] for gate in gates["gates"]} == {f"P{i}" for i in range(10)}
    assert gates["lean"]["new_axioms_forbidden"] is True
    claim_ids = {claim["id"] for claim in claims["claims"]}
    assert {
        "PWOC-SF0-LEAN-A",
        "PWOC-SF0-LEAN-B",
        "PWOC-SF1",
        "PWOC-SF2",
    } <= claim_ids
    sf1 = next(claim for claim in claims["claims"] if claim["id"] == "PWOC-SF1")
    assert sf1["status"] == "PROVED_FIXED_ORDER_BOUNDED_WEIGHT"


def verify_lean_boundary() -> None:
    text = LEAN.read_text()
    forbidden = (r"\bsorry\b", r"\badmit\b", r"\baxiom\b", r"\bunsafe\b")
    for pattern in forbidden:
        assert re.search(pattern, text) is None, f"forbidden Lean token: {pattern}"
    for theorem in (
        "totalCollision_le_of_rowBudget",
        "weightedEnergy_le_of_collisionBudget",
        "weightedEnergy_le_of_rowCollisionBudget",
        "fixedOrderChooseSum",
    ):
        assert f"theorem {theorem}" in text, theorem
    import_text = ROOT_IMPORT.read_text()
    assert "import FortuneFormal.Integer.SquarefreeCompositeEnergyCriterion" in import_text


def verify_claim_hygiene() -> None:
    text = "\n".join(path.read_text() for path in REQUIRED if path.suffix in {".md", ".json"})
    assert "FIXED_ORDER_COMPOSITE_EXTENSION_PROVED" in text
    assert "SOURCE_WEIGHT_CONTRACT_NOT_AVAILABLE" in text
    assert "NO_TRANSFER_TO_RUHL_OR_SOCG" in text
    assert "No proof of INT-AOD or Fortune is claimed." in text
    assert "PWOC-SF2 remains open" in text


def run_regressions() -> None:
    for script in ("verify_squarefree_walk.py", "run_execution_panels.py"):
        subprocess.run(
            [sys.executable, str(PROGRAMME / "scripts" / script)],
            check=True,
            cwd=ROOT,
        )


def main() -> None:
    require_files()
    verify_json()
    verify_lean_boundary()
    verify_claim_hygiene()
    run_regressions()
    print("FORTUNE_INT_PWOC_SF_EXECUTED_PROGRAMME_PASS")


if __name__ == "__main__":
    main()
