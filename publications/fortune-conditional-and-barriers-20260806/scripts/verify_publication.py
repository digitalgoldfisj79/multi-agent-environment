#!/usr/bin/env python3
"""Static and exact audit for the consolidated Fortune publication package."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = ROOT / "publications" / "fortune-conditional-and-barriers-20260806"


def run(*command: str) -> None:
    completed = subprocess.run(command, cwd=ROOT, text=True, check=False)
    if completed.returncode:
        raise SystemExit(f"command failed ({completed.returncode}): {' '.join(command)}")


def require_text(path: Path, phrases: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            raise AssertionError(f"missing required phrase {phrase!r} in {path}")


def reject_text(path: Path, phrases: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase in text:
            raise AssertionError(f"forbidden overclaim {phrase!r} in {path}")


def main() -> None:
    manuscript = PACKAGE / "MANUSCRIPT.md"
    compliance = PACKAGE / "LEAN_COMPLIANCE.md"
    matrix_path = PACKAGE / "CLAIM_MATRIX.json"
    for path in (manuscript, compliance, matrix_path):
        if not path.is_file():
            raise AssertionError(f"missing publication file: {path}")

    require_text(
        manuscript,
        [
            "Theorem 3.1",
            "E_{b,k}=A_{b,k}+S_{b,k}",
            "beta=5",
            "coefficient count proves this weighted-accuracy requirement, not impossibility",
            "does not prove Fortune's conjecture",
        ],
    )
    require_text(
        compliance,
        [
            "Lean compliance does not imply full formalization",
            "p7_k2_certified_normalization",
            "COMPLIANT_WITH_ONE_LEDGERED_EXTERNAL_BOUNDARY",
        ],
    )
    reject_text(
        manuscript,
        [
            "all seven prior papers are fully formalized.",
            "Heath--Brown methods are impossible",
            "Fortune's conjecture is proved",
        ],
    )

    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    assert len(matrix["documents"]) == 8
    assert matrix["allowed_axioms"] == ["FortuneFormal.p7_k2_certified_normalization"]
    assert all("status" in item for item in matrix["documents"])

    arithmetic = ROOT / "fortune-int-ruhl-fm-consolidation" / "ARITHMETIC_INTERFACE.md"
    require_text(arithmetic, ["E_{b,k}=A_{b,k}+S_{b,k}", "must not be appended"])
    reject_text(arithmetic, ["E_{b,k}=A_{b,k}+S_{b,k}+Q_{b,k}"])

    source = ROOT / "fortune-ruhl-selected-tuple-residual" / "R4_HEATH_BROWN_SOURCE.md"
    require_text(source, ["coefficient mass alone does **not** prove", "sum_{r=1}^{J}{J\\choose r}|R_r|"])

    run(sys.executable, "fortune-int-ruhl-fm-consolidation/scripts/verify_ruhl_budget.py")
    run(
        sys.executable,
        "fortune-int-ruhl-fm-consolidation/scripts/verify_ruhl_budget.py",
        "--epsilon", "0.000001",
        "--ratio", "1",
        "--beta", "3.6",
        "--diagnostic-limit", "1000",
    )
    run(sys.executable, "fortune-int-lcsk-tree-graph/scripts/verify_tree_graph.py")
    run(sys.executable, "fortune-formal/scripts/verify_cross_paper_audit.py")
    run(sys.executable, "fortune-formal/scripts/verify_programme.py")

    print("FORTUNE_PUBLICATION_CONSOLIDATION_LEAN_AUDIT_PASS")


if __name__ == "__main__":
    main()
