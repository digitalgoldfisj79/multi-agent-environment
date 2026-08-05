#!/usr/bin/env python3
"""Review-corrected sentinel for the INT-SCME programme."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROGRAMME = ROOT / "fortune-int-scme-selected-centre-mean"

required = [
    "README.md", "PROGRAMME.md", "PREREGISTERED_GATES.json",
    "CLAIM_MATRIX.json", "STATUS.md", "FINAL_STATUS.md",
    "SUCCESSOR.md", "EXTERNAL_REVIEW_RESPONSE.md",
    "M1_NORMALIZATION.md", "M6_PARITY_TAIL.md", "M9_CLOSEOUT.md",
]
for rel in required:
    assert (PROGRAMME / rel).is_file(), rel

contract = json.loads((PROGRAMME / "PREREGISTERED_GATES.json").read_text())
assert contract["status"] == "CLOSED_REVIEW_CORRECTED"
assert contract["terminal_outcome"] == "SELECTED_RESIDUE_VARIANCE_ROUTE_OBSTRUCTED"
assert contract["frontier_components"] == ["INT-SCME", "INT-LCSK", "INT-PWOC"]
assert contract["auxiliary_conditional_target"] == "INT-SCVAR"
assert contract["scpt_status"] == "EQUIVALENT_TO_INT_SCME_GIVEN_INT_SCVAR"
assert contract["external_review"]["commit"] == "029cc8c"

claims = json.loads((PROGRAMME / "CLAIM_MATRIX.json").read_text())
assert claims["fortune_claimed"] is False
assert claims["int_socg_claimed"] is False
assert claims["int_scme_claimed"] is False

text = "\n".join((PROGRAMME / rel).read_text() for rel in required)
for forbidden in (
    "two independent subordinate targets",
    "completed `INT-SOCG -> INT-SCME` reduction",
    "INT-SCME implies INT-SOCG",
    "sole primary integer frontier",
):
    assert forbidden not in text, forbidden

formal = ROOT / "fortune-formal" / "FortuneFormal" / "Integer" / "SelectedCentreMeanCriterion.lean"
assert formal.is_file()
for forbidden in ("sorry", "admit", "unsafe"):
    assert forbidden not in formal.read_text()

for script in (
    "verify_bdh_exponents.py",
    "verify_collision_multiplicity.py",
    "verify_microblock_aggregation.py",
    "verify_parity_tail_reduction.py",
    "verify_fi_scale_gap.py",
    "verify_divisor_band_main.py",
    "verify_large_sieve_obstruction.py",
):
    subprocess.run([sys.executable, str(PROGRAMME / "scripts" / script)], check=True)

print("FORTUNE_INT_SCME_REVIEW_CORRECTED_PASS")
print("frontier=INT-SCME+INT-LCSK+INT-PWOC")
print("auxiliary=INT-SCVAR")
print("scpt=equivalent_to_int_scme_given_int_scvar")
