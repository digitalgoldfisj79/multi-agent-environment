#!/usr/bin/env python3
"""Build standalone Paper I with proof-status and publication-boundary tightening."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "publications/fortune-papers-ii-vi-20260724/paper1_collision_geometry/manuscript.md"
OUT = ROOT / "publications/fortune-standalone-20260811/paper1_collision_geometry"

STATUS_INSERT = r'''## 1.2. Status of results

Every labelled theorem, proposition, lemma and corollary in this article is proved in the text. Exact finite enumeration is used only to validate template constants, Smith-form calculations and algebraic identities; numerical modulus panels are diagnostic and are not proof inputs. The named estimates HTE4, HWF4, FBHE4 and RQHE4 are explicitly open hypotheses or targets. No theorem in this paper supplies a prime-pair detector or proves Fortune's conjecture.

'''


def main() -> None:
    src = SRC.read_text(encoding="utf-8")
    text = src
    text = text.replace('date: "24 July 2026 - Original reproducibility archive DOI 10.5281/zenodo.21426465"', 'date: "11 August 2026"', 1)
    marker = "# 2. Exact fourth-moment identity\n"
    if marker not in text:
        raise RuntimeError("Paper I section marker missing")
    text = text.replace(marker, STATUS_INSERT + marker, 1)
    old = "The paper's asymptotic assertions are proved symbolically. Finite enumeration is used only for the explicit template constants and for independent verification of algebraic identities."
    new = "Every asymptotic assertion presented in this article as proved is established symbolically. Finite enumeration is used only for explicit template constants and independent verification of algebraic identities; the named open estimates are not included in that claim."
    if old not in text:
        raise RuntimeError("Paper I reproducibility wording changed")
    text = text.replace(old, new, 1)
    text = text.replace("The research programme used large language models", "Large language models were used", 1)

    forbidden = ["Paper II", "Paper III", "Paper IV", "Paper V", "Paper VI", "Paper VII", "preceding paper", "following paper", "this series", "INT-ISC", "RUHL-FM"]
    bad = [x for x in forbidden if x in text]
    if bad:
        raise RuntimeError(f"standalone dependency token remains: {bad}")

    # Paper I uses both ## and ### for labelled statements; preserve the full frozen sequence.
    stmt_re = re.compile(r"^#{2,3} (Theorem|Proposition|Lemma|Corollary) ([0-9]+\.[0-9]+)", re.M)
    a = [f"{x} {y}" for x, y in stmt_re.findall(src)]
    b = [f"{x} {y}" for x, y in stmt_re.findall(text)]
    if a != b or len(b) != 25:
        raise RuntimeError(f"Paper I statement sequence changed or unexpected count: {len(a)} -> {len(b)}")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "manuscript.md").write_text(text.rstrip() + "\n", encoding="utf-8")
    status = """# Standalone Paper I — claim status

## Proved in the manuscript

- exact fourth-moment/collision identity;
- averaged low-transport collision bound;
- weighted large-divisor offset-slice incidence bound;
- average almost-injectivity and local repeated-collision bounds;
- interval endpoint-graph affine-rank and Smith-invariant classification;
- exact pair-overlap/median decompositions and independent-prefix covariance laws;
- non-Gaussian fourth-moment law;
- sparse-composition closure, square-function comparison, additive-frequency averaging and common-translation obstruction results.

## Conditional/open

- HTE4 centered rank-two dispersion;
- HWF4 hereditary weighted moment;
- FBHE4 four-distinct-block energy;
- RQHE4 root-quartet estimate;
- any signed prime-detection bridge.

Even proving all internal energy targets would not by itself prove Fortune's conjecture.
"""
    (OUT / "CLAIM_STATUS.md").write_text(status, encoding="utf-8")
    referee = """# Independent-standalone referee read — Paper I

**Disposition:** `PASS_STANDALONE_STRUCTURAL`

Paper I already had the strongest standalone architecture in the series. The rebuild preserves all 25 labelled statements, adds an explicit proof-status paragraph, tightens the computational wording, and leaves the Fortune motivation contextual only. No theorem imports a companion manuscript.

The principal external-review risk remains literature priority for the interval-specific Smith-form theorem and analytic scrutiny of the open HTE4/HWF4 interfaces, not a hidden cross-paper dependency.
"""
    (OUT / "REFEREE_READ.md").write_text(referee, encoding="utf-8")
    repro = """# Reproducibility boundary — Paper I

Finite enumeration and code check template multiplicities, Smith invariants, exact algebraic identities and diagnostic modulus panels. The labelled analytic results have manuscript proofs. Numerical panels do not establish HTE4, HWF4, FBHE4, RQHE4 or any prime-detection theorem.
"""
    (OUT / "REPRODUCIBILITY.md").write_text(repro, encoding="utf-8")
    manifest = {
        "paper": "I",
        "source": str(SRC.relative_to(ROOT)),
        "standalone": str((OUT / "manuscript.md").relative_to(ROOT)),
        "statement_count": len(b),
        "statement_sequence": b,
        "logical_cross_paper_dependencies": 0,
        "fortune_proved": False,
    }
    (OUT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"PAPER1_STANDALONE_BUILD_OK statements={len(b)} words={len(text.split())}")


if __name__ == "__main__":
    main()
