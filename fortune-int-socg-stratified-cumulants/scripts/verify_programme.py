#!/usr/bin/env python3
"""Static and exact sentinel for the executed INT-SOCG programme."""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
PROGRAMME=ROOT/"fortune-int-socg-stratified-cumulants"
required=[
 "README.md","PROGRAMME.md","PREREGISTERED_GATES.json","CLAIM_MATRIX.json",
 "EXPONENT_LEDGER.json","METHOD_LEDGER.md","LITERATURE_AUDIT.md","LITERATURE_EXECUTION.md",
 "RUNBOOK.md","FORMALISATION_PLAN.md","STATUS.md","FINAL_STATUS.md","SUCCESSOR.md",
 "C0_SOURCE_FREEZE.md","C1_STRATUM_GEOMETRY.md","C2_FIRST_CUMULANT.md",
 "C3_EQUALITY_PATTERNS.md","C4_LOCAL_CONNECTED_KERNEL.md","C5_PRIMORIAL_WALK.md",
 "C6_SIGNED_ASSEMBLY.md","C7_SOURCE_DECOMPOSITION.md","C8_CONDITIONAL_DIAGNOSTICS.md",
 "C9_CLOSEOUT.md","C0_EXECUTION.md","C1_EXECUTION.md","C2_EXECUTION.md",
 "C3_EXECUTION.md","C4_EXECUTION.md","C5_EXECUTION.md","C6_EXECUTION.md",
 "C7_EXECUTION.md","C8_EXECUTION.md","C9_EXECUTION.md"
]
for rel in required:
    path=PROGRAMME/rel
    if not path.is_file(): raise SystemExit(f"missing required file: {path}")
contract=json.loads((PROGRAMME/"PREREGISTERED_GATES.json").read_text())
assert contract["programme"]=="FORTUNE_INT_SOCG_STRATIFIED_CUMULANTS_V0_1"
assert contract["base_commit"]=="1d6ace4553bb88492dfceb894abd9e5d6713d426"
assert contract["primary_issue"]==56
assert contract["status"] in {"BUILT_NOT_EXECUTED","EXECUTING","RESEARCH_COMPLETE_VALIDATION_PENDING","CLOSED"}
assert contract["terminal_target"]=="INT-SCME"
assert contract["terminal_outcome"]=="MEAN_LOWER_BOUND_IS_PRIMARY_OBSTRUCTION"
assert [g["id"] for g in contract["gates"]]==[f"C{i}" for i in range(10)]
assert contract["cumulant_contract"]["kind"]=="ordinary"
assert contract["cumulant_contract"]["ordered_column_tuples_include_repetitions"] is True
assert contract["cumulant_contract"]["factorial_distinct_column_identity_forbidden"] is True
assert contract["cumulant_contract"]["correct_factorial_stirling_transform_proved"] is True
assert contract["cumulant_contract"]["factorial_radius_to_ordinary_radius_additive_cost"]==1
claims=json.loads((PROGRAMME/"CLAIM_MATRIX.json").read_text())
assert claims["new_axioms"]==0
assert claims["fortune_claimed"] is False
assert claims["int_socg_claimed"] is False
assert claims["int_scme_claimed"] is False
all_text="\n".join((PROGRAMME/rel).read_text() for rel in required)
for forbidden in (
    "factorial cumulant satisfies the exact ordered-tuple identity",
    "finite panels prove",
    "Fortune is proved"
):
    if forbidden in all_text: raise SystemExit(f"forbidden promotion or identity: {forbidden}")
parent_formal=ROOT/"fortune-formal"/"FortuneFormal"/"Integer"/"AdaptiveOccupancyCriterion.lean"
assert parent_formal.is_file()
formal_text=parent_formal.read_text()
for theorem in (
    "no_failure_of_rowDependentExp_sum_lt_one",
    "uniformExp_sum_lt_one_of_rowDependent"
): assert theorem in formal_text
for script in (
    "verify_stratum_geometry.py","verify_partition_mobius.py",
    "verify_equality_pattern_decomposition.py","verify_socg_budget.py",
    "verify_scale_ledger.py","verify_factorial_stirling.py",
    "verify_weighted_mean_reduction.py","verify_prime_modulus_walk_large_sieve.py"
):
    subprocess.run([sys.executable,str(PROGRAMME/"scripts"/script)],check=True)
for diagnostic in (
    "run_primorial_walk_diagnostics.py","run_selected_centre_cumulants.py",
    "run_local_edge_diagnostics.py"
):
    path=PROGRAMME/"scripts"/diagnostic
    assert path.is_file()
selected=(PROGRAMME/"scripts"/"run_selected_centre_cumulants.py").read_text()
assert "primorial(ell,nth=False)" in selected
assert "method=\"primes\"" not in selected
print("FORTUNE_INT_SOCG_STRATIFIED_CUMULANTS_PROGRAMME_PASS")
print(f"programme={contract['programme']}")
print(f"status={contract['status']}")
print(f"outcome={contract['terminal_outcome']}")
print(f"gates={','.join(g['id'] for g in contract['gates'])}")
