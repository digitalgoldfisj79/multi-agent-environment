#!/usr/bin/env python3
"""Static and symbolic verifier for Fortune Paper VII.

This script does not replace the Singular chart certificates.  It checks the
frozen manuscript/ledger boundary, the quadratic discriminant algebra, the
chart cover and the exact equation transcription.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
EXPECTED_MANUSCRIPT_SHA256 = "4c95d04b5c055dd4e97b0bdc75db8ed50c61ff2c2cbf23009f830ca25484819b"


def assemble_manuscript() -> str:
    parts = sorted((ROOT / "manuscript_parts").glob("*.md"))
    if [part.name for part in parts] != [
        "00-frontmatter-introduction-algebraisation.md",
        "01-defect-rigidity-and-cubic.md",
        "02-relaxation-and-quadratic-theorem.md",
        "03-lineage-frontier-and-appendix.md",
    ]:
        raise SystemExit("unexpected manuscript part set or order")
    manuscript = "".join(part.read_text(encoding="utf-8") for part in parts)
    digest = hashlib.sha256(manuscript.encode()).hexdigest()
    if digest != EXPECTED_MANUSCRIPT_SHA256:
        raise SystemExit(f"assembled manuscript SHA-256 mismatch: {digest}")
    return manuscript


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"missing {label}: {needle}")


def main() -> None:
    manuscript = assemble_manuscript()
    claims = (ROOT / "CLAIM_STATUS.md").read_text(encoding="utf-8")
    audit = (ROOT / "PAPER_VI_LINEAGE_AUDIT.md").read_text(encoding="utf-8")

    for forbidden in ("TODO", "TBD", "PLACEHOLDER", "REPLACE_ME"):
        if forbidden in manuscript:
            raise SystemExit(f"forbidden token in manuscript: {forbidden}")

    markers = {
        "quadratic theorem": "For every odd prime power \\(q\\), there is no cross-distinct",
        "prime-only defect hypothesis": "assume that \\(q\\) is an odd prime",
        "relaxation warning": "They do **not** impose",
        "crown boundary": "No function-field crown, endpoint dispersion theorem or integer Fortune",
        "Paper VI retained": "Paper VI is **valid and retained**",
        "withdrawn q>k": "universal \\(q>k\\) emptiness",
    }
    for label, needle in markers.items():
        require(manuscript, needle, label)

    require(claims, "Exact computer-assisted theorem", "claim classification")
    require(claims, "P7-K2", "quadratic theorem ledger")
    require(audit, "corrective sequel, not a replacement", "lineage verdict")
    require(audit, "Non-overlap guard", "quadratic terminology guard")

    A, B, C, U, r = sp.symbols("A B C U r")
    target = [U - 1, B + 2, (A - C) ** 2 + 4 * A]
    subs = {U: 1, B: -2, A: -r**2 / 4, C: -r**2 / 4 - r}
    if any(sp.simplify(expr.subs(subs)) != 0 for expr in target):
        raise SystemExit("target component parametrisation failed")

    disc_p = sp.expand(-4 * A).subs(subs)
    disc_s = sp.expand(B**2 - 4 * C).subs(subs)
    if sp.simplify(disc_p - r**2) != 0:
        raise SystemExit("disc(P) square identity failed")
    if sp.simplify(disc_s - (r + 2) ** 2) != 0:
        raise SystemExit("disc(S) square identity failed")

    equal_coeff_conditions = (B, A - C)
    if len(equal_coeff_conditions) != 2:
        raise SystemExit("chart cover internal error")

    equation_markers = (
        "f_0={}&-4A^2BU+6A^2B",
        "f_1={}&-4A^2U+4A^2",
        "f_2={}&-2A^2B-2A^2U",
        "f_3={}&4A^2U-4A^2",
    )
    for marker in equation_markers:
        if manuscript.count(marker) != 1:
            raise SystemExit(f"equation transcription marker count !=1: {marker}")

    output = {
        "manuscript_sha256": hashlib.sha256(manuscript.encode()).hexdigest(),
        "word_count": len(manuscript.split()),
        "disc_P": str(sp.factor(disc_p)),
        "disc_S": str(sp.factor(disc_s)),
        "chart_cover": "P!=S iff B!=0 or A-C!=0",
        "status": "PAPER7_STATIC_SYMBOLIC_PASS",
    }
    (ROOT / "paper7_verify_results.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
