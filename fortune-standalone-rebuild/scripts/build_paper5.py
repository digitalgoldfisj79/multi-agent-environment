#!/usr/bin/env python3
"""Build standalone Paper V from the authoritative replacement manuscript."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "publications/fortune-papers-ii-vi-20260724/paper5_function_fields_replacement"
SRC = SRC_DIR / "manuscript.md"
SRC_BIB = SRC_DIR / "references.bib"
OUT = ROOT / "publications/fortune-standalone-20260811/paper5_fortunate_polynomials"

FRONT = r'''---
title: "Fortunate Polynomials over Finite Fields"
subtitle: "Exact normal forms, sparse geometry, and the function-field d=1 crown"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "11 August 2026"
lang: en-GB
bibliography: references.bib
link-citations: true
reference-section-title: References
---

**Abstract.** We formulate a finite-field analogue of the Fortunate-number problem in which primes are replaced by monic irreducible polynomials. For the polynomial primorial \(P_d\), a reducible offset coprime to \(P_d\) has degree at least \(2d+2\). At \(d=1\) over \(\mathbf F_p\), where \(P_1=T^p-T\), the degree-at-most-three problem therefore reduces to an exact irreducibility count in a four-parameter affine interval. We prove the orbit decomposition
\[
I_4=(p-1)+p(p-1)N_2+\frac{p(p-1)}2(N_{\mathrm{sq}}+N_{\mathrm{ns}}),
\]
so the nonconstant crown is exactly the positivity of
\[
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2}.
\]

The associated ordered-root compactification is a smooth complete-intersection surface. Its affine short-interval variety is a translation torsor over the corresponding affine cone, giving an exact transfer of nontrivial isotypic compactly supported cohomology. A computer-assisted primitive-hook reconstruction at \(p=11\) shows that a natural aggregate absolute-Betti sufficient criterion already fails there. We prove an exact sign-hook trace, show that the alternating-hook projector is precisely the \(p\)-cycle trace, and compute the corresponding fixed-point count \(pI_4+p\), so the resulting one-sided primitive trace inequality is algebraically equivalent to the crown. Finally, the two depressed cubic square classes are assembled into one q-line system whose invariant saturation defect is exactly \(p(N_{\mathrm{sq}}+N_{\mathrm{ns}})\). Thus the geometry gives several exact reformulations and obstruction theorems, but it does not prove the universal function-field crown. No transfer to the integer Fortune conjecture is claimed.

**Keywords:** function fields; irreducible polynomials; finite fields; complete intersections; Frobenius traces; Fortunate numbers.

# 1. Problem, scope, and principal results

Let \(\mathbf F_q[T]\) play the role of the integers and monic irreducible polynomials the role of primes. For a degree cutoff \(d\), multiply all monic irreducibles of degree at most \(d\) to form a polynomial primorial. The analogue of a Fortunate offset is then the first nonconstant polynomial offset, under a fixed deterministic ordering, that makes the primorial plus the offset irreducible.

This model is not asserted to transfer to the integer Fortune conjecture. Its purpose is intrinsic: the finite coefficient spaces admit exact affine normal forms, ordered-root varieties and Frobenius actions, so one can determine which geometric or representation-theoretic transformations genuinely weaken the nonvanishing problem and which merely restate it.

The paper develops the \(d=1\) case over prime fields \(\mathbf F_p\), \(p>3\). The principal results are:

1. Proposition 2.1 gives the general reducible-offset degree barrier.
2. Theorem 4.1 and Corollary 4.2 reduce the \(d=1\) crown exactly to positivity of three nonnegative normal-form counts.
3. Theorem 5.1 proves global smoothness of the ordered-root complete-intersection surface.
4. Theorem 6.1 identifies the nontrivial isotypic compactly supported cohomology of the affine short-interval variety; the independently reproduced \(p=11\) hook census then refutes one aggregate absolute-Betti proof mechanism.
5. Theorems 7.1--9.1 and Corollary 9.2 identify the sign endpoint, the alternating-hook \(p\)-cycle projector and its exact fixed-point circularity.
6. Theorems 10.1 and 11.1 assemble the depressed cubic square classes into q-line projectors and prove that invariant saturation defect is exactly the cubic irreducible count.

Every labelled theorem below is proved symbolically in the manuscript. Finite computations are separately identified and serve as exact checks or finite-prime certificates. In particular, the \(p=11\) absolute-Betti counterexample uses an exact computer-assisted primitive-hook reconstruction; it is not a uniform theorem inferred from data. The universal positivity statement \(W_p>0\) remains open.

'''

FRONTIER = r'''# 13. Exact frontier

The results reduce the function-field \(d=1\) problem to exact nonnegative coordinates, but do not prove their universal nonvanishing.

Several natural mechanisms are closed as independent reductions.

1. **Aggregate absolute Betti control.** For the actual affine short-interval variety, the exact transfer of Theorem 6.1 and the computer-assisted \(p=11\) hook reconstruction give \(B_{\mathrm{mid}}=82>10=p-1\). Thus the proposed sufficient inequality \(B_{\mathrm{mid}}\le p-1\) is false at an admitted prime.
2. **Alternating-hook fixed-point control.** Theorem 9.1 and Corollary 9.2 show that the corresponding one-sided primitive trace inequality is exactly equivalent to \(W_p>0\); the fixed-point rewrite does not weaken the crown.
3. **Congruence-only q-line nonsaturation.** Theorem 11.1 gives
   \[
   S_0^{\mathrm{sat}}-S_0=p(N_{\mathrm{sq}}+N_{\mathrm{ns}}),
   \]
   so integrality, parity and divisibility already present in the ledger cannot distinguish zero from the first positive admissible value.

The exact crown is
\[
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2}>0.
\tag{13.1}
\]
Equivalently, when \(N_2=0\), the remaining cubic problem is strict invariant q-line nonsaturation. A successful continuation must therefore provide genuinely new one-sided Frobenius or arithmetic information that excludes the simultaneous zero state; another exact change of coordinates is not progress unless it weakens that requirement.

The universal function-field crown remains open. No theorem in this article implies the integer Fortune conjecture.

# AI-assistance disclosure

Large language models were used for literature triage, symbolic and computational cross-checking, adversarial review, software drafting and editorial assembly. Proved, computer-assisted, conjectural and open statements are separated explicitly. The named author takes responsibility for the mathematics, citations, code and final presentation.

# Data and code availability

The reproducibility package contains the independent finite-field reconstruction, irreducibility and hook-character verifier, singular-locus verifier, machine-readable outputs, source manifest and checksums. None of these files is required to read the symbolic proofs in the manuscript. Exact finite outputs are not extrapolated into a uniform theorem.
'''


def once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {n}")
    return text.replace(old, new, 1)


def build() -> tuple[str, str, list[str]]:
    src = SRC.read_text(encoding="utf-8")
    body_marker = "# 2. Polynomial primorials and the degree barrier\n"
    a = src.find(body_marker)
    frontier_marker = "# 13. The exact frontier and the input to Paper VI\n"
    b = src.find(frontier_marker)
    if a < 0 or b < 0:
        raise RuntimeError("Paper V source architecture changed")
    body = src[a:b]
    text = FRONT + body + FRONTIER

    text = once(
        text,
        "All uniform statements above have already been proved symbolically.  The\ncomputations in this section are independent regression checks of those proofs;\nthey are not used to extrapolate a theorem from finitely many primes.",
        "Every uniform statement presented above as proved is established symbolically in the manuscript. The computations in this section are independent regression checks or explicitly finite computer-assisted certificates; they are not used to extrapolate a theorem from finitely many primes.",
        "computation scope",
    )
    text = once(
        text,
        "The broader repository census extends the crown certification substantially\nfurther.  Those finite results are exact computer-assisted theorems at the\nlisted primes, not evidence that replaces the missing uniform theorem.",
        "Additional finite-prime censuses may be included in the reproducibility package. Such results are exact only at their listed primes and do not replace the missing uniform theorem.",
        "finite census scope",
    )

    forbidden = [
        "Papers III", "Paper III", "Paper IV", "Paper VI", "preceding two papers",
        "next paper", "this series", "Papers I--VI", "derandomisation barrier",
        "D1-QLINE-NONSAT", "programme boundary",
    ]
    bad = [x for x in forbidden if x in text]
    if bad:
        raise RuntimeError(f"standalone dependency token remains: {bad}")

    stmt_re = re.compile(r"^## (Proposition|Theorem|Corollary) ([0-9]+\.[0-9]+)", re.M)
    source_statements = [f"{a} {b}" for a, b in stmt_re.findall(src)]
    output_statements = [f"{a} {b}" for a, b in stmt_re.findall(text)]
    if source_statements != output_statements:
        raise RuntimeError(f"statement sequence changed: source={source_statements}, output={output_statements}")
    if len(output_statements) != 11:
        raise RuntimeError(f"expected 11 statements, found {len(output_statements)}")

    bib = SRC_BIB.read_text(encoding="utf-8")
    # Companion programme manuscripts are no longer cited by the standalone article.
    bib = re.sub(r"\n@unpublished\{BozzardPaperIII,.*?\n\}\n", "\n", bib, flags=re.S)
    bib = re.sub(r"\n@unpublished\{BozzardPaperIV,.*?\n\}\n", "\n", bib, flags=re.S)
    cite_keys = set(re.findall(r"@([A-Za-z0-9_.:-]+)", text))
    bib_keys = set(re.findall(r"@[A-Za-z]+\{([^,]+),", bib))
    missing = sorted(cite_keys - bib_keys)
    if missing:
        raise RuntimeError(f"missing bibliography keys: {missing}")
    return text.rstrip() + "\n", bib.rstrip() + "\n", output_statements


def main() -> None:
    text, bib, statements = build()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "manuscript.md").write_text(text, encoding="utf-8")
    (OUT / "references.bib").write_text(bib, encoding="utf-8")

    status = """# Standalone Paper V — claim status

**Publication role:** exact function-field normal forms, ordered-root geometry and obstruction theorems for the `d=1` crown.

## Proved symbolically in the manuscript

- reducible-offset degree barrier;
- exact affine-orbit decomposition and crown coordinate;
- global smoothness of the sparse ordered-root surface;
- nontrivial Sawin-cone cohomology transfer;
- sign-hook trace;
- alternating-hook p-cycle projector;
- exact p-cycle fixed-point count and fixed-point circularity;
- q-line class projectors and saturation-defect identity.

## Exact computer-assisted finite statements

- full interval irreducibility censuses at p=5,7,11;
- p=7 singular-locus census;
- p=11 primitive-hook reconstruction used to show the aggregate absolute-Betti sufficient criterion fails there.

## Open

- universal positivity of W_p;
- strict q-line nonsaturation when the quadratic coordinate vanishes;
- the universal function-field d=1 crown;
- any transfer to the integer Fortune conjecture.
"""
    (OUT / "CLAIM_STATUS.md").write_text(status, encoding="utf-8")

    repro = """# Reproducibility boundary — Paper V

The symbolic theorem sequence is readable independently of the finite computations. The finite evidence consists of the independently rerun p=5,7,11 irreducibility/crown census, the p=7 singular-locus census, hook-character checks and the p=11 primitive-hook reconstruction. The corpus-wide assurance run reproduced the first two classes of evidence and repaired an incomplete stored p=11 hook-character JSON table; no theorem statement changed. Finite-prime results are never extrapolated to the universal crown.
"""
    (OUT / "REPRODUCIBILITY.md").write_text(repro, encoding="utf-8")

    manifest = {
        "paper": "V",
        "source": str(SRC.relative_to(ROOT)),
        "source_bibliography": str(SRC_BIB.relative_to(ROOT)),
        "standalone": str((OUT / "manuscript.md").relative_to(ROOT)),
        "statement_count": len(statements),
        "statement_sequence": statements,
        "logical_cross_paper_dependencies": 0,
        "universal_crown_proved": False,
        "integer_transfer_proved": False,
        "finite_evidence_scope": ["p=5,7,11 full crown census", "p=7 singular locus", "p=11 primitive-hook reconstruction"],
    }
    (OUT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"PAPER5_STANDALONE_BUILD_OK statements={len(statements)} words={len(text.split())}")


if __name__ == "__main__":
    main()
