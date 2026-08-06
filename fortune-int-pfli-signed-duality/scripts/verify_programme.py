#!/usr/bin/env python3
"""Static and exact-regression verifier for the signed-duality programme."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROGRAMME = ROOT / "fortune-int-pfli-signed-duality"

required = [
    "README.md",
    "PROGRAMME.md",
    "PREREGISTERED_GATES.json",
    "CLAIM_MATRIX.json",
    "D1_ALGEBRAIC_COLLAPSE.md",
    "D2_ADAPTIVE_OCCUPANCY.md",
    "D3_FACTORIAL_EXPANSION.md",
    "D4_MOMENT_BARRIER.md",
    "D5_CORRELATION_ARITY.md",
    "D6_ASYMPTOTIC_SIEVE_AUDIT.md",
]
for rel in required:
    path = PROGRAMME / rel
    if not path.is_file():
        raise SystemExit(f"missing required file: {path}")

contract = json.loads((PROGRAMME / "PREREGISTERED_GATES.json").read_text())
assert contract["programme"] == "FORTUNE_INT_PFLI_SIGNED_DUALITY_V0_1"
assert [g["id"] for g in contract["gates"]] == [f"D{i}" for i in range(8)]
assert contract["status"] in {"EXECUTING", "RESEARCH_COMPLETE_VALIDATION_PENDING", "CLOSED"}

claims = json.loads((PROGRAMME / "CLAIM_MATRIX.json").read_text())
assert claims["new_axioms"] == 0
assert claims["fortune_claimed"] is False
claim_ids = {c["id"] for c in claims["claims"]}
for required_claim in {
    "D1-COLLAPSE",
    "D2-SOFT-DETECTOR",
    "D2-EXP-DETECTOR",
    "D2-INT-AOD",
    "D4-MOMENT-BARRIER",
    "D5-ARITY",
    "D6-ASYMPTOTIC-SIEVE",
}:
    assert required_claim in claim_ids

lean = ROOT / "fortune-formal" / "FortuneFormal" / "Integer" / "SoftDefectCriterion.lean"
text = lean.read_text()
for forbidden in ("sorry", "admit", "unsafe", "axiom "):
    if forbidden in text:
        raise SystemExit(f"forbidden token in {lean}: {forbidden}")
for theorem_name in (
    "coverageExcessSq_eq_lowerTailSq",
    "no_failure_of_soft_detector_sum_lt_one",
    "no_failure_of_expDefect_sum_lt_one",
):
    assert theorem_name in text

scripts = [
    "verify_pfli_collapse.py",
    "verify_adaptive_occupancy.py",
    "verify_factorial_expansion.py",
    "verify_moment_barrier.py",
    "verify_arity_scale.py",
]
for script in scripts:
    subprocess.run(
        [sys.executable, str(PROGRAMME / "scripts" / script)],
        check=True,
    )

print("FORTUNE_INT_PFLI_SIGNED_DUALITY_PROGRAMME_PASS")
print(f"programme={contract['programme']}")
print(f"status={contract['status']}")
print(f"gates={','.join(g['id'] for g in contract['gates'])}")
