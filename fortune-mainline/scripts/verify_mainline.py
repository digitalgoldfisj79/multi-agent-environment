#!/usr/bin/env python3
"""Static and executable verification for FORTUNE_MAINLINE_CLOSEOUT_V1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent

REQUIRED = [
    "SOURCE_MANIFEST.json",
    "CLAIM_MATRIX.json",
    "PAPERS_II_III_RECONSTRUCTION.md",
    "INTEGER_FRONTIER.md",
    "PAPERS_V_VI_RECONSTRUCTION.md",
    "PAPERS_I_IV_SELECTIVE_AUDIT.md",
    "FINAL_STATUS.md",
    "scripts/finite_obstruction_checks.py",
    "scripts/verify_mainline.py",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load(path: str) -> dict:
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot load {path}: {exc}")


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    if missing:
        fail(f"missing files: {missing}")

    manifest = load("SOURCE_MANIFEST.json")
    matrix = load("CLAIM_MATRIX.json")

    if manifest.get("programme") != "FORTUNE_MAINLINE_CLOSEOUT_V1":
        fail("wrong source-manifest programme")
    if matrix.get("programme") != "FORTUNE_MAINLINE_CLOSEOUT_V1":
        fail("wrong claim-matrix programme")
    if matrix.get("status") != "COMPLETED_REDUCTION_RECONSTRUCTION_AND_OBSTRUCTION_ANALYSIS":
        fail("programme is not frozen at the registered completion state")

    ids = [p.get("id") for p in manifest.get("papers", [])]
    if ids != ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]:
        fail(f"unexpected paper sequence: {ids}")

    open_ids = [p.get("id") for p in matrix.get("open_research_theorems", [])]
    if open_ids != ["INT-ISC", "D1-QLINE-NONSAT", "P7-CUBIC-TF"]:
        fail(f"unexpected open theorem sequence: {open_ids}")

    prohibited_claims = {
        "Fortune's conjecture",
        "INT-ISC",
        "universal function-field d=1",
        "D1-QLINE-NONSAT",
        "axiom-free P7-K2",
        "P7-CUBIC-TF",
        "function-field-to-integer transfer",
    }
    if not prohibited_claims.issubset(set(matrix.get("explicitly_not_claimed", []))):
        fail("honesty boundary incomplete")

    docs = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in REQUIRED if p.endswith(".md"))
    for phrase in (
        "INT-ISC",
        "D1-QLINE-NONSAT",
        "one external",
        "Fortune: open",
        "function-field-to-integer transfer",
    ):
        if phrase not in docs:
            fail(f"documentation missing boundary phrase: {phrase}")

    finite = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "finite_obstruction_checks.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if finite.returncode or "FORTUNE_MAINLINE_FINITE_OBSTRUCTION_PASS" not in finite.stdout:
        fail("finite obstruction regression failed: " + finite.stdout + finite.stderr)

    formal = subprocess.run(
        [sys.executable, str(REPO / "fortune-formal" / "scripts" / "verify_programme.py")],
        cwd=REPO / "fortune-formal",
        text=True,
        capture_output=True,
        check=False,
    )
    if formal.returncode or "FORTUNE_FORMAL_PROGRAMME_STATIC_PASS" not in formal.stdout:
        fail("formal static contract failed: " + formal.stdout + formal.stderr)

    print(finite.stdout.strip())
    print(formal.stdout.strip())
    print("FORTUNE_MAINLINE_CLOSEOUT_PASS")
    print("papers=7")
    print("open_frontiers=3")
    print("primary_integer_frontier=INT-ISC")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
