#!/usr/bin/env python3
"""Static and exact-regression verifier for the INT-AOD occupancy-dual programme."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROGRAMME = ROOT / "fortune-int-aod-occupancy-dual"

required = [
    "README.md",
    "PROGRAMME.md",
    "PREREGISTERED_GATES.json",
    "CLAIM_MATRIX.json",
    "EXPONENT_LEDGER.json",
    "METHOD_LEDGER.md",
    "LITERATURE_AUDIT.md",
    "RUNBOOK.md",
    "FORMALISATION_PLAN.md",
    "O1_DETECTOR_ADMISSIBILITY.md",
    "O2_RANDOM_COVER_DUAL.md",
    "O3_DEGREE_COEFFICIENT_COST.md",
    "O4_CONNECTED_CUMULANT_COMPRESSION.md",
    "O5_ARITHMETIC_CONNECTED_CORRELATIONS.md",
    "O6_CONDITIONAL_POISSON_BENCHMARK.md",
    "O7_ROWWISE_PARITY_BREAKING.md",
    "O8_FALSIFICATION_AND_SMALL_PANELS.md",
    "STATUS.md",
]
for rel in required:
    path = PROGRAMME / rel
    if not path.is_file():
        raise SystemExit(f"missing required file: {path}")

contract = json.loads((PROGRAMME / "PREREGISTERED_GATES.json").read_text())
assert contract["programme"] == "FORTUNE_INT_AOD_OCCUPANCY_DUAL_V0_1"
assert contract["base_commit"] == "831184e1ceb519803591eda441de2672dc8a9939"
assert contract["primary_issue"] == 54
assert [gate["id"] for gate in contract["gates"]] == [f"O{i}" for i in range(10)]
assert contract["status"] in {
    "BUILT_NOT_EXECUTED",
    "EXECUTING",
    "RESEARCH_COMPLETE_VALIDATION_PENDING",
    "CLOSED",
}
assert contract["detector_admissibility"][
    "weights_must_be_frozen_before_output_prime_incidence"
] is True
assert contract["detector_admissibility"]["comparison_budget_required"] is True

claims = json.loads((PROGRAMME / "CLAIM_MATRIX.json").read_text())
assert claims["new_axioms"] == 0
assert claims["fortune_claimed"] is False
assert claims["int_aod_claimed"] is False
claim_ids = {claim["id"] for claim in claims["claims"]}
for required_claim in {
    "O1-GENERIC-DETECTOR",
    "O1-WEIGHTED-DETECTOR",
    "O2-BERNOULLI-COVER",
    "O2-HYPERGEOMETRIC-COVER",
    "O3-DEGREE-COST",
    "O4-INT-CCB",
    "O5-CONNECTED-ARITHMETIC",
    "O6-RUHL-IMPLICATION",
    "O7-ROWWISE-BILINEAR",
    "O8-NO_FINITE_PROMOTION",
}:
    assert required_claim in claim_ids

for rel in required:
    text = (PROGRAMME / rel).read_text()
    if "Fortune is proved" in text or "PROVED_FORTUNE" in text:
        raise SystemExit(f"forbidden theorem promotion in {rel}")

scripts = [
    "verify_detector_implication.py",
    "verify_random_cover.py",
    "verify_scale_ledger.py",
    "verify_factorial_cumulants.py",
    "verify_adversarial_private_columns.py",
]
for script in scripts:
    subprocess.run(
        [sys.executable, str(PROGRAMME / "scripts" / script)],
        check=True,
    )

print("FORTUNE_INT_AOD_OCCUPANCY_DUAL_PROGRAMME_PASS")
print(f"programme={contract['programme']}")
print(f"status={contract['status']}")
print(f"gates={','.join(gate['id'] for gate in contract['gates'])}")
