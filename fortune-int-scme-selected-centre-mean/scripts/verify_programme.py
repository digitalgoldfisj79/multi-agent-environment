#!/usr/bin/env python3
"""Static and exact sentinel for the INT-SCME selected-centre programme."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROGRAMME = ROOT / "fortune-int-scme-selected-centre-mean"

REQUIRED = [
    "README.md",
    "PROGRAMME.md",
    "PREREGISTERED_GATES.json",
    "CLAIM_MATRIX.json",
    "STATUS.md",
    "FINAL_STATUS.md",
    "CORRECTION_RECORD.md",
    "SUCCESSOR.md",
    "M0_SOURCE_FREEZE.md",
    "M1_NORMALIZATION.md",
    "M2_LOCAL_DENSITY_AND_SIEVE.md",
    "M3_MICROBLOCKS.md",
    "M4_SELECTED_BDH.md",
    "M5_POST_TERMINAL_BAND.md",
    "M6_PARITY_TAIL.md",
    "M7_SOURCE_AUDIT.md",
    "M8_DIAGNOSTICS.md",
    "M9_CLOSEOUT.md",
    "LITERATURE_AUDIT.md",
    "FORMALISATION_PLAN.md",
]

for rel in REQUIRED:
    path = PROGRAMME / rel
    if not path.is_file():
        raise SystemExit(f"missing required file: {path}")

contract = json.loads((PROGRAMME / "PREREGISTERED_GATES.json").read_text())
assert contract["programme"] == "FORTUNE_INT_SCME_SELECTED_CENTRE_MEAN_V0_1"
assert contract["base_commit"] == "e1a9822e8f43c37329c03a863595af522626d73b"
assert contract["primary_issue"] == 58
assert contract["status"] in {"EXECUTING", "RESEARCH_COMPLETE_VALIDATION_PENDING", "CLOSED"}
assert [gate["id"] for gate in contract["gates"]] == [f"M{i}" for i in range(10)]
assert contract["terminal_outcome"] == "METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE"
assert contract["conditional_reduction"] == ["INT-SCVAR", "INT-SCPT"]
assert contract["correction"]["initial_m5_promotion_retracted"] is True

claims = json.loads((PROGRAMME / "CLAIM_MATRIX.json").read_text())
assert claims["new_axioms"] == 0
assert claims["fortune_claimed"] is False
assert claims["int_scme_claimed"] is False
assert claims["int_scvar_claimed"] is False
assert claims["int_scpt_claimed"] is False

all_text = "\n".join((PROGRAMME / rel).read_text() for rel in REQUIRED)
for forbidden in (
    "divisor-band mass proves primality",
    "PROVED_USING_CLASSICAL_BDH",
    "genuine unconditional post-terminal distribution result",
    "finite panels prove",
    "Fortune is proved",
):
    if forbidden in all_text:
        raise SystemExit(f"forbidden promotion: {forbidden}")

assert "issue #60" in (PROGRAMME / "SUCCESSOR.md").read_text()
assert "issue #61" in (PROGRAMME / "SUCCESSOR.md").read_text()
assert "incorrectly" in (PROGRAMME / "CORRECTION_RECORD.md").read_text()

formal = ROOT / "fortune-formal" / "FortuneFormal" / "Integer" / "SelectedCentreMeanCriterion.lean"
assert formal.is_file()
formal_text = formal.read_text()
for theorem in (
    "selectedCentreMean_lowerBound_of_band_and_tail",
    "selectedCentreMean_of_normalized_parityTail",
):
    assert theorem in formal_text
for forbidden in ("sorry", "admit", "unsafe"):
    assert forbidden not in formal_text

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

assert (PROGRAMME / "scripts" / "run_factor_profile_diagnostics.py").is_file()

print("FORTUNE_INT_SCME_SELECTED_CENTRE_MEAN_PROGRAMME_PASS")
print(f"status={contract['status']}")
print(f"outcome={contract['terminal_outcome']}")
print(f"gates={','.join(g['id'] for g in contract['gates'])}")
