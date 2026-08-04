#!/usr/bin/env python3
"""Closeout contract for FORTUNE_INT_ISC_FOCUSED_V0_1."""

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
    "EXPONENT_LEDGER.json",
    "METHOD_LEDGER.md",
    "CLAIM_LEDGER.md",
    "STATUS.md",
    "FINAL_STATUS.md",
    "RUN_PROTOCOL.md",
    "I1_WEAKEST_TARGET_AUDIT.md",
    "I2_SPARSE_FIRST_MOMENT_AUDIT.md",
    "I3_FOUR_PRIME_LANE.md",
    "I4_SHIFTED_SOURCE_LANE.md",
    "I5_SOURCE_ORBIT_PSD_LANE.md",
    "I6_FALSIFICATION_MODELS.md",
    "scripts/verify_programme.py",
    "scripts/scale_audit.py",
    "scripts/i1_strictness_check.py",
    "scripts/i3_scale_audit.py",
    "scripts/i4_source_scale_audit.py",
    "scripts/i5_coherence_audit.py",
    "scripts/i6_adversarial_models.py",
]

CHECKS = [
    ("scripts/scale_audit.py", "FORTUNE_INT_ISC_SCALE_AUDIT_PASS"),
    ("scripts/i1_strictness_check.py", "FORTUNE_INT_ISC_I1_STRICTNESS_PASS"),
    ("scripts/i3_scale_audit.py", "FORTUNE_INT_ISC_I3_SCALE_OBSTRUCTION_PASS"),
    ("scripts/i4_source_scale_audit.py", "FORTUNE_INT_ISC_I4_SOURCE_SCALE_PASS"),
    ("scripts/i5_coherence_audit.py", "FORTUNE_INT_ISC_I5_COHERENCE_PASS"),
    ("scripts/i6_adversarial_models.py", "FORTUNE_INT_ISC_I6_ADVERSARIAL_PASS"),
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load(name: str) -> dict:
    try:
        return json.loads((ROOT / name).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot parse {name}: {exc}")


def run_check(relpath: str, sentinel: str) -> str:
    proc = subprocess.run(
        [sys.executable, str(ROOT / relpath)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode or sentinel not in proc.stdout:
        fail(f"{relpath} failed: {proc.stdout}{proc.stderr}")
    return proc.stdout.strip()


def main() -> int:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    if missing:
        fail(f"missing programme files: {missing}")

    gates = load("PREREGISTERED_GATES.json")
    exponents = load("EXPONENT_LEDGER.json")

    if gates.get("programme") != "FORTUNE_INT_ISC_FOCUSED_V0_1":
        fail("wrong programme identifier")
    if gates.get("base_commit") != "deb6bb5468a951bc5485514c5848abcfcf386594":
        fail("base commit drift")
    if gates.get("terminal_outcome") != "REDUCED_TO_SMALLER_NEW_THEOREM":
        fail("terminal outcome drift")
    if gates.get("primary_target") != "INT-PSLT":
        fail("terminal target drift")
    if gates.get("status") not in {
        "I0_I6_COMPLETE_I7_VALIDATION",
        "COMPLETED_REDUCED_TO_INT_PSLT",
    }:
        fail("unexpected closeout state")

    ids = [gate.get("id") for gate in gates.get("gates", [])]
    if ids != [f"I{i}" for i in range(8)]:
        fail(f"unexpected gate sequence: {ids}")
    statuses = {gate.get("id"): gate.get("status") for gate in gates.get("gates", [])}
    expected = {
        "I0": "PASSED",
        "I1": "PASSED",
        "I2": "CLOSED_DIAGNOSTIC_NOT_REQUIRED",
        "I3": "CLOSED_METHOD_OBSTRUCTED",
        "I4": "PASSED_REDUCED_TO_SMALLER_NEW_THEOREM",
        "I5": "CLOSED_COHERENCE_OBSTRUCTION",
        "I6": "PASSED",
    }
    for gate, status in expected.items():
        if statuses.get(gate) != status:
            fail(f"unexpected {gate} state: {statuses.get(gate)}")

    policy = gates.get("compute_policy", {})
    expected_policy = {
        "sentinel_timeout_minutes": 10,
        "ordinary_job_timeout_minutes": 45,
        "absolute_timeout_minutes": 120,
        "terminal_programme_jobs_required": 0,
        "inspect_unrelated_jobs_before_any_cancellation": True,
    }
    for key, value in expected_policy.items():
        if policy.get(key) != value:
            fail(f"compute policy drift: {key}")

    if exponents.get("programme") != gates.get("programme"):
        fail("exponent ledger programme mismatch")
    if exponents.get("status") != "EXECUTED_REDUCED_TO_INT_PSLT":
        fail("exponent ledger closeout drift")
    if "X/L(X)" not in exponents.get("lane_obstructions", {}).get("I3_raw_four_prime", ""):
        fail("I3 loss obstruction missing")

    docs = "\n".join(
        (ROOT / name).read_text(encoding="utf-8")
        for name in REQUIRED
        if name.endswith(".md")
    )
    for phrase in (
        "INT-PSLT",
        "REDUCED_TO_SMALLER_NEW_THEOREM",
        "one-defect",
        "X/L(X)",
        "F_X(a/q)=N",
        "provider sweep",
        "remain unproved",
    ):
        if phrase.lower() not in docs.lower():
            fail(f"missing closeout phrase: {phrase}")

    for prohibited in (
        "P7-CUBIC-TF",
        "D1-QLINE-NONSAT",
        "finite-panel extrapolation",
    ):
        if prohibited not in str(gates.get("prohibited_lanes", [])):
            fail(f"missing prohibited lane: {prohibited}")

    # The focused directory may not hide an open arithmetic theorem as an axiom.
    for path in ROOT.rglob("*.lean"):
        text = path.read_text(encoding="utf-8")
        if re.search(r"^\s*axiom\b", text, re.MULTILINE):
            fail(f"focused programme contains an axiom: {path.relative_to(ROOT)}")
        if re.search(r"\b(sorry|admit|unsafe)\b", text):
            fail(f"focused programme contains a prohibited Lean token: {path.relative_to(ROOT)}")

    inherited = [
        REPO / "fortune-mainline" / "FINAL_STATUS.md",
        REPO / "fortune-formal" / "FortuneFormal" / "Integer" / "BlockCriterion.lean",
        REPO / "fortune-formal" / "FortuneFormal" / "Integer" / "LowerTailCriterion.lean",
    ]
    missing_inherited = [str(path.relative_to(REPO)) for path in inherited if not path.is_file()]
    if missing_inherited:
        fail(f"missing inherited/formal spine: {missing_inherited}")

    outputs = [run_check(path, sentinel) for path, sentinel in CHECKS]
    for output in outputs:
        print(output)

    print("FORTUNE_INT_ISC_PROGRAMME_CLOSEOUT_PASS")
    print("programme=FORTUNE_INT_ISC_FOCUSED_V0_1")
    print("gates=I0,I1,I2,I3,I4,I5,I6,I7")
    print("terminal_outcome=REDUCED_TO_SMALLER_NEW_THEOREM")
    print("primary_target=INT-PSLT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
