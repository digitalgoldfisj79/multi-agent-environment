#!/usr/bin/env python3
"""Static contract for FORTUNE_INT_ISC_FOCUSED_V0_1."""

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
    "RUN_PROTOCOL.md",
    "scripts/verify_programme.py",
    "scripts/scale_audit.py",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load(name: str) -> dict:
    try:
        return json.loads((ROOT / name).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot parse {name}: {exc}")


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
    if gates.get("status") != "I0_PASSED_I1_READY":
        fail("programme must be frozen at the validated I0 state")

    ids = [gate.get("id") for gate in gates.get("gates", [])]
    if ids != [f"I{i}" for i in range(8)]:
        fail(f"unexpected gate sequence: {ids}")
    statuses = {gate.get("id"): gate.get("status") for gate in gates.get("gates", [])}
    if statuses.get("I0") != "PASSED" or statuses.get("I1") != "READY":
        fail(f"unexpected promoted gate state: {statuses}")

    validation = gates.get("validation", {})
    if validation.get("job_id") != "6a7205146b79c09949c2236a":
        fail("I0 validation job drift")
    if validation.get("result") != "COMPLETED" or validation.get("failure_count") != 0:
        fail("I0 validation did not complete cleanly")

    allowed = gates.get("allowed_final_statuses", [])
    expected_allowed = [
        "PROVED_INT_ISC",
        "REDUCED_TO_ESTABLISHED_THEOREM",
        "REDUCED_TO_SMALLER_NEW_THEOREM",
        "METHOD_OBSTRUCTED_AT_EXPLICIT_SCALE",
    ]
    if allowed != expected_allowed:
        fail("final-status contract drift")

    policy = gates.get("compute_policy", {})
    if policy.get("sentinel_timeout_minutes") != 10:
        fail("sentinel timeout drift")
    if policy.get("ordinary_job_timeout_minutes") != 45:
        fail("ordinary timeout drift")
    if policy.get("absolute_timeout_minutes") != 120:
        fail("absolute timeout drift")
    if policy.get("terminal_programme_jobs_required") != 0:
        fail("terminal job requirement must be zero")

    if exponents.get("programme") != gates.get("programme"):
        fail("exponent ledger programme mismatch")
    if exponents.get("scales", {}).get("loss_condition") != "1 <= L(X) = o(log X)":
        fail("loss condition drift")

    docs = "\n".join(
        (ROOT / name).read_text(encoding="utf-8")
        for name in REQUIRED
        if name.endswith(".md")
    )
    for phrase in (
        "INT-ISC",
        "weakest-sufficient-target",
        "necessary sparse first moment",
        "increasing primorial centres",
        "o(log X)",
        "provider sweep",
        "not a proof",
    ):
        if phrase.lower() not in docs.lower():
            fail(f"missing programme boundary phrase: {phrase}")

    for prohibited in (
        "P7-CUBIC-TF",
        "D1-QLINE-NONSAT",
        "finite-panel extrapolation",
    ):
        if prohibited not in str(gates.get("prohibited_lanes", [])):
            fail(f"missing prohibited lane: {prohibited}")

    # This focused programme may not hide open arithmetic claims as axioms.
    for path in ROOT.rglob("*.lean"):
        text = path.read_text(encoding="utf-8")
        if re.search(r"^\s*axiom\b", text, re.MULTILINE):
            fail(f"focused programme contains an axiom: {path.relative_to(ROOT)}")
        if re.search(r"\b(sorry|admit|unsafe)\b", text):
            fail(f"focused programme contains a prohibited Lean token: {path.relative_to(ROOT)}")

    inherited = [
        REPO / "fortune-mainline" / "FINAL_STATUS.md",
        REPO / "fortune-formal" / "FortuneFormal" / "Integer" / "BlockCriterion.lean",
    ]
    missing_inherited = [str(path.relative_to(REPO)) for path in inherited if not path.is_file()]
    if missing_inherited:
        fail(f"missing inherited closeout spine: {missing_inherited}")

    scale = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "scale_audit.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if scale.returncode or "FORTUNE_INT_ISC_SCALE_AUDIT_PASS" not in scale.stdout:
        fail("scale audit failed: " + scale.stdout + scale.stderr)

    print(scale.stdout.strip())
    print("FORTUNE_INT_ISC_PROGRAMME_STATIC_PASS")
    print("programme=FORTUNE_INT_ISC_FOCUSED_V0_1")
    print("gates=I0,I1,I2,I3,I4,I5,I6,I7")
    print("primary_target=INT-ISC")
    print("status=I0_PASSED_I1_READY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
