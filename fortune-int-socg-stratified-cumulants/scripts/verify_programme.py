#!/usr/bin/env python3
"""Static and exact build sentinel for the INT-SOCG programme."""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
PROGRAMME=ROOT/"fortune-int-socg-stratified-cumulants"
required=[
 "README.md","PROGRAMME.md","PREREGISTERED_GATES.json","CLAIM_MATRIX.json",
 "EXPONENT_LEDGER.json","METHOD_LEDGER.md","LITERATURE_AUDIT.md","RUNBOOK.md",
 "FORMALISATION_PLAN.md","STATUS.md","C0_SOURCE_FREEZE.md","C1_STRATUM_GEOMETRY.md",
 "C2_FIRST_CUMULANT.md","C3_EQUALITY_PATTERNS.md","C4_LOCAL_CONNECTED_KERNEL.md",
 "C5_PRIMORIAL_WALK.md","C6_SIGNED_ASSEMBLY.md","C7_SOURCE_DECOMPOSITION.md",
 "C8_CONDITIONAL_DIAGNOSTICS.md","C9_CLOSEOUT.md"
]
for rel in required:
    path=PROGRAMME/rel
    if not path.is_file(): raise SystemExit(f"missing required file: {path}")
contract=json.loads((PROGRAMME/"PREREGISTERED_GATES.json").read_text())
assert contract["programme"]=="FORTUNE_INT_SOCG_STRATIFIED_CUMULANTS_V0_1"
assert contract["base_commit"]=="1d6ace4553bb88492dfceb894abd9e5d6713d426"
assert contract["primary_issue"]==56
assert contract["status"] in {"BUILT_NOT_EXECUTED","EXECUTING","CLOSED"}
assert [g["id"] for g in contract["gates"]]==[f"C{i}" for i in range(10)]
assert contract["cumulant_contract"]["kind"]=="ordinary"
assert contract["cumulant_contract"]["ordered_column_tuples_include_repetitions"] is True
assert contract["cumulant_contract"]["factorial_distinct_column_identity_forbidden"] is True
claims=json.loads((PROGRAMME/"CLAIM_MATRIX.json").read_text())
assert claims["new_axioms"]==0
assert claims["fortune_claimed"] is False
assert claims["int_socg_claimed"] is False
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
    "verify_scale_ledger.py"
):
    subprocess.run([sys.executable,str(PROGRAMME/"scripts"/script)],check=True)
for diagnostic in ("run_primorial_walk_diagnostics.py","run_selected_centre_cumulants.py"):
    assert (PROGRAMME/"scripts"/diagnostic).is_file()
print("FORTUNE_INT_SOCG_STRATIFIED_CUMULANTS_PROGRAMME_PASS")
print(f"programme={contract['programme']}")
print(f"status={contract['status']}")
print(f"gates={','.join(g['id'] for g in contract['gates'])}")
