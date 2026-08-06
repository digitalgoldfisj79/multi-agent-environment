#!/usr/bin/env python3
"""Static and regression verifier for the INT-PSLT factor-band programme."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent

REQUIRED = [
    "README.md",
    "PROGRAMME.md",
    "PREREGISTERED_GATES.json",
    "SCALE_LEDGER.json",
    "CLAIM_LEDGER.md",
    "LITERATURE_AUDIT.md",
    "B1_PRIME_POWER_THRESHOLD.md",
    "B2_PROPAGATION_AUDIT.md",
    "B3_LEAST_FACTOR_IDENTITY.md",
    "B4_SIEVE_LEVEL_OBSTRUCTION.md",
    "B5_CRITICAL_FACTOR_INCIDENCE.md",
    "B6_ONE_DEFECT_IMPLICATION.md",
    "FINAL_STATUS.md",
    "STATUS.md",
]

SCRIPTS = [
    "b1_prime_power_audit.py",
    "b2_propagation_audit.py",
    "b3_factor_partition_audit.py",
    "b4_sieve_level_audit.py",
    "b5_incidence_audit.py",
    "b6_one_defect_audit.py",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_json(name: str) -> dict:
    try:
        return json.loads((ROOT / name).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot parse {name}: {exc}")


def run_script(name: str) -> str:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / name)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode:
        fail(f"{name} failed:\n{proc.stdout}{proc.stderr}")
    return proc.stdout.strip()


def main() -> int:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    missing += [f"scripts/{name}" for name in SCRIPTS if not (ROOT / "scripts" / name).is_file()]
    if missing:
        fail(f"missing files: {missing}")

    gates = load_json("PREREGISTERED_GATES.json")
    scales = load_json("SCALE_LEDGER.json")

    if gates.get("programme") != "FORTUNE_INT_PSLT_BUCHSTAB_FACTOR_BAND_V0_1":
        fail("programme identifier drift")
    if gates.get("base_commit") != "cc8c00c30a436b8ced65bbd4703326145d129de3":
        fail("base commit drift")
    if gates.get("terminal_target") != "INT-PFLI":
        fail("terminal target drift")
    if gates.get("terminal_outcome") != "REDUCED_TO_CRITICAL_FACTOR_INCIDENCE":
        fail("terminal outcome drift")
    if gates.get("status") not in {"RESEARCH_COMPLETE_VALIDATION_PENDING", "CLOSED"}:
        fail("unexpected programme status")

    ids = [gate.get("id") for gate in gates.get("gates", [])]
    if ids != [f"B{i}" for i in range(8)]:
        fail(f"gate sequence drift: {ids}")

    statuses = {gate["id"]: gate["status"] for gate in gates["gates"]}
    expected_prefix = {
        "B0": "PASSED",
        "B1": "PASSED",
        "B2": "CLOSED_NO_NATURAL_PROPAGATION",
        "B3": "PASSED",
        "B4": "CLOSED_AT_S_LT_2",
        "B5": "REDUCED_TO_INT_PFLI",
        "B6": "PASSED_FORMAL_IMPLICATION",
    }
    for gate, expected in expected_prefix.items():
        if statuses.get(gate) != expected:
            fail(f"{gate} status drift: {statuses.get(gate)}")
    if statuses.get("B7") not in {"VALIDATING", "PASSED"}:
        fail("B7 must be validating or passed")

    if scales.get("programme") != gates.get("programme"):
        fail("scale ledger programme mismatch")
    scale_text = json.dumps(scales, sort_keys=True)
    for phrase in ("X log X", "r > ell_j", "s=log D/log r < 2"):
        if phrase not in scale_text:
            fail(f"missing scale invariant: {phrase}")

    docs = "\n".join((ROOT / name).read_text(encoding="utf-8") for name in REQUIRED if name.endswith(".md"))
    for phrase in (
        "INT-PFLI",
        "X log X",
        "sqrt(H)",
        "s<2",
        "signed aggregate",
        "not proved",
    ):
        if phrase.lower() not in docs.lower():
            fail(f"missing boundary phrase: {phrase}")

    lean = REPO / "fortune-formal" / "FortuneFormal" / "Integer" / "FactorBandCriterion.lean"
    if not lean.is_file():
        fail("missing FactorBandCriterion.lean")
    lean_text = lean.read_text(encoding="utf-8")
    if re.search(r"^\s*axiom\b", lean_text, re.MULTILINE):
        fail("factor-band formalization contains an axiom")
    if re.search(r"\b(sorry|admit|unsafe)\b", lean_text):
        fail("factor-band formalization contains a prohibited token")
    for theorem in (
        "lowerTail_quarter_gap_of_source_le_half",
        "no_failure_of_variable_source_cap",
        "no_failure_of_coverage_excess",
    ):
        if theorem not in lean_text:
            fail(f"missing formal theorem: {theorem}")

    importer = (REPO / "fortune-formal" / "FortuneFormal.lean").read_text(encoding="utf-8")
    if "import FortuneFormal.Integer.FactorBandCriterion" not in importer:
        fail("FactorBandCriterion is not in the package import spine")

    for name in SCRIPTS:
        output = run_script(name)
        print(output)

    print("FORTUNE_INT_PSLT_FACTOR_BAND_PROGRAMME_PASS")
    print("programme=FORTUNE_INT_PSLT_BUCHSTAB_FACTOR_BAND_V0_1")
    print("terminal_outcome=REDUCED_TO_CRITICAL_FACTOR_INCIDENCE")
    print("terminal_target=INT-PFLI")
    print(f"status={gates['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
