#!/usr/bin/env python3
"""Static, trust-boundary and exact-regression audit for INT-PWOC-SF."""
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
    PROGRAMME / "scripts" / "verify_squarefree_walk.py",
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
    assert {"PWOC-SF0-LEAN-A", "PWOC-SF0-LEAN-B", "PWOC-SF1", "PWOC-SF2"} <= claim_ids


def verify_lean_boundary() -> None:
    text = LEAN.read_text()
    forbidden = (r"\bsorry\b", r"\badmit\b", r"\baxiom\b", r"\bunsafe\b")
    for pattern in forbidden:
        assert re.search(pattern, text) is None, f"forbidden Lean token: {pattern}"
    for theorem in (
        "totalCollision_le_of_rowBudget",
        "weightedEnergy_le_of_collisionBudget",
        "weightedEnergy_le_of_rowCollisionBudget",
    ):
        assert f"theorem {theorem}" in text, theorem
    import_text = ROOT_IMPORT.read_text()
    assert "import FortuneFormal.Integer.SquarefreeCompositeEnergyCriterion" in import_text


def verify_claim_hygiene() -> None:
    status_text = "\n".join(path.read_text() for path in REQUIRED if path.suffix in {".md", ".json"})
    assert "built; execution not yet started" in status_text
    assert "No squarefree-composite energy estimate has yet been proved." in status_text
    assert "No proof of INT-AOD or Fortune is claimed." in status_text


def run_exact_regression() -> None:
    subprocess.run(
        [sys.executable, str(PROGRAMME / "scripts" / "verify_squarefree_walk.py")],
        check=True,
        cwd=ROOT,
    )


def main() -> None:
    require_files()
    verify_json()
    verify_lean_boundary()
    verify_claim_hygiene()
    run_exact_regression()
    print("FORTUNE_INT_PWOC_SF_PROGRAMME_BUILD_PASS")


if __name__ == "__main__":
    main()
