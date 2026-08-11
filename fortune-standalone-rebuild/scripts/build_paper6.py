#!/usr/bin/env python3
"""Build standalone Paper VI from the authoritative replacement manuscript."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "publications/fortune-papers-ii-vi-20260724/paper6_secondary_quotients_replacement"
SRC = SRC_DIR / "manuscript.md"
SRC_BIB = SRC_DIR / "references.bib"
OUT = ROOT / "publications/fortune-standalone-20260811/paper6_secondary_traces_quotients"

FRONT = r'''---
title: "Secondary Traces and Kummer Quotients for a Function-Field Fortune Crown"
subtitle: "Cyclotomic tangents, Artin--Schreier descent, and an exact nonvanishing frontier"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "11 August 2026"
lang: en-GB
bibliography: references.bib
link-citations: true
reference-section-title: References
---

**Abstract.** Over \(\mathbf F_p[T]\), consider the degree-one polynomial primorial \(T^p-T\) and its degree-at-most-three coefficient interval. Affine normalisation reduces the nonconstant irreducibility crown to positivity of
\[
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2},
\]
where \(N_2\) is a quadratic normal-form count and \(N_{\mathrm{sq}},N_{\mathrm{ns}}\) are the two depressed-cubic square-class counts. This paper studies integral and quotient-geometric information that is invisible to ordinary semisimple class projectors.

For a fixed nonzero cubic coefficient \(a\), we introduce the Cartier first moment \(M_a=\sum_{\mathrm{irr}}c\) and identify it as the first cyclotomic tangent of the coefficient Fourier transform. The coefficient tangent is a nonsplit self-extension of the trivial \(\mathbf F_p[C_p]\)-module, with explicit Tate groups and identity Bockstein; nevertheless a family of Frobenius lifts proves that those modular data do not determine the tangent trace. The root-cycle hook satisfies \(\Theta_p=p\mathbf1-\operatorname{Reg}_{C_p}\), so division by \(p\) is not an ordinary virtual character. Hattori--Stallings trace instead gives an integral coefficient extraction \(\operatorname{Tr}_{\mathbf Z}(\Phi\sigma^{-r})=ph_r\).

On the fixed cubic ordered-root slice we construct a global Artin--Schreier coordinate \(y\) with \(\sigma(y)=y+1\). The invariant \(g=y^p-y\) records Frobenius shift and its level \(g=1\) is exactly the irreducibility section. A logarithmic-derivative argument proves that the split level is empty for \(p>5\). The two cubic arithmetic classes are Kummer forms under \(\mu_{p-3}\), and their common quotient has \((N_{\mathrm{sq}}+N_{\mathrm{ns}})/2\) rational points on the irreducibility level. Finally, the natural projective root-cycle quotient has one isolated wild fixed point and exact count
\[
\operatorname{card}\mathscr Q_p(\mathbf F_p)=1+(p-1)W_p.
\]
These constructions do not prove \(W_p>0\): the remaining task is still a one-sided compactly supported Frobenius or rational-point theorem. No integer Fortune theorem is claimed.

**Keywords:** Hattori--Stallings trace; Artin--Schreier theory; Kummer theory; cyclotomic tangents; finite fields; Frobenius traces.

# 1. Exact crown coordinates and scope

We first derive the arithmetic coordinates needed later, so that no companion manuscript is required. For \(p>3\), the degree-one polynomial primorial is
\[
P_1=\prod_{u\in\mathbf F_p}(T-u)=T^p-T.
\tag{1.1}
\]
Consider the four-parameter interval
\[
\mathcal I_4=\{T^p-T+aT^3+bT^2+cT+d:(a,b,c,d)\in\mathbf F_p^4\},
\]
and let \(I_4(p)\) be its irreducible count. The constant-offset Artin--Schreier sector contains exactly \(p-1\) irreducibles \(T^p-T+d\), \(d\ne0\); these are excluded from the nonconstant crown.

For \(a=0,b\ne0\), translation uniquely kills the total linear coefficient and monic scaling uniquely normalises the quadratic coefficient to one. Define
\[
N_2=\#\{d\in\mathbf F_p:T^p+T^2+d\text{ irreducible}\}.
\]
Each quadratic normal form has an affine orbit of size \(p(p-1)\).

For \(a\ne0\), translation uniquely removes the quadratic coefficient. The depressed slice is
\[
f_{a,c,d}(X)=X^p+aX^3+cX+d.
\tag{1.2}
\]
Monic scaling sends \(a\mapsto a\lambda^2\), so its irreducible count depends only on \(A=\chi(a)\in\{+1,-1\}\). Write these two counts as \(N_{\mathrm{sq}}\) and \(N_{\mathrm{ns}}\). Each depressed polynomial has \(p\) translates and each square class contains \((p-1)/2\) values of \(a\). Therefore
\[
\boxed{
I_4=(p-1)+p(p-1)N_2+
\frac{p(p-1)}2(N_{\mathrm{sq}}+N_{\mathrm{ns}}).
}
\tag{1.3}
\]
Thus the nonconstant \(d=1\) crown is exactly
\[
\boxed{
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2}>0.
}
\tag{1.4}
\]
Since all three counts are nonnegative integers, failure means their simultaneous vanishing. The involution \(d\mapsto-d\) is fixed-point-free on irreducible depressed cubic slices, so both cubic counts are even.

The purpose of this paper is to test whether integral first-order data or quotient geometry yields a strictly weaker nonvanishing theorem than (1.4). All labelled results below are unconditional unless a finite computation is explicitly identified. No theorem proves the universal crown, and no transfer to the integer Fortune conjecture is asserted. Throughout, \(F\) denotes Frobenius normalised so that its fixed points are the \(\mathbf F_p\)-points in the trace formula. The coefficient cyclic group and root-cycle group are distinct copies of \(C_p\). We use the standard periodic Tate complex [@BrownCohomology], Artin--Schreier theory and Kummer cohomology.

'''

FRONTIER = r'''# 15. Exact nonvanishing frontier

The paper has constructed the integral and geometric objects that ordinary semisimple class projectors do not retain:

- the fixed-class Cartier tangent;
- the nonsplit coefficient extension and its Bockstein;
- the Hattori--Stallings divided root-cycle trace;
- the Artin--Schreier quotient whose \(g=1\) level is irreducibility;
- the Kummer quotient packaging the cubic class sum;
- the projective quotient with exact point count \(1+(p-1)W_p\).

None of these constructions supplies an independently computable positive term. The remaining statement is genuinely one-sided:

> **Kummer-quotient nonvanishing problem.** For every admitted prime, prove that the compactly supported Frobenius trace on the specific cubic quotient open cannot attain its zero-point value.

Arithmetically, when \(N_2=0\), this is exactly
\[
\boxed{N_{\mathrm{sq}}+N_{\mathrm{ns}}>0.}
\tag{15.1}
\]
or equivalently strict invariant q-line nonsaturation. It is not weakened by another projector, congruence or quotient coordinate change.

The following continuations are closed without an additional idea: a universal quadratic sign-twist compactification; an ordinary divided-hook perfect complex; coefficient Tate/Bockstein data without a secondary Frobenius trace; generic Artin--Schreier trace-surjectivity as a point theorem; standard proper-point congruences; automatic Fano/rational-connected/Witt-rational claims at the wild quotient point; and larger finite scans without a structural prediction.

The function-field \(d=1\) crown remains open. No theorem in this paper proves Fortune's conjecture over the integers.

# AI-assistance disclosure

Large language models were used for literature triage, symbolic and computational cross-checking, adversarial review, software drafting and editorial assembly. Proved, computer-assisted, empirical, open and refuted claims are separated explicitly. The named author takes responsibility for the mathematics, citations, code and final presentation.

# Data and code availability

The reproducibility package contains the source manifest, claim-status ledger, independent algebraic reconstruction, verification scripts, machine-readable outputs and checksums. These finite regressions do not replace the missing uniform rational-point theorem.
'''


def once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {n}")
    return text.replace(old, new, 1)


def build() -> tuple[str, str, list[str]]:
    src = SRC.read_text(encoding="utf-8")
    a = src.find("# 2. A fixed-class Cartier first moment\n")
    b = src.find("# 15. The terminal theorem\n")
    if a < 0 or b < 0:
        raise RuntimeError("Paper VI source architecture changed")
    body = src[a:b]
    text = FRONT + body + FRONTIER

    # Close the q-line selection dependency locally.
    old = """For $c\\ne0$, use the q-line coordinate
\\[
q=-3/c.
\\]
If $A=\\chi(a)$, Paper V shows that the required normal-form reading at $q$ is
$\\varepsilon=A\\chi(q)$.  Let $I_\\varepsilon(q)$ be the irreducible constant-fibre
count in that cell.  Since $c=-3q^{-1}$ and the $c=0$ boundary has zero weight,
we obtain the reciprocal form.
"""
    new = """For $c\\ne0$, use the q-line coordinate
\\[
q=-3/c.
\\]
Put $A=\\chi(a)$ and $r=-c/(3a)=1/(aq)$.  Scaling to the split depressed normal form requires a square root of $r$; hence the split/nonsplit reading is
\\[
\\varepsilon=\\chi(r)=A\\chi(q),
\\]
because quadratic characters are unchanged by inversion.  Let $I_\\varepsilon(q)$ be the irreducible constant-fibre count in that reading.  Since $c=-3q^{-1}$ and the $c=0$ boundary has zero weight, we obtain the reciprocal form.
"""
    text = once(text, old, new, "q-line local derivation")

    # Close the projective-surface dependency locally.
    old2 = """Let
\\[
\\mathscr Y_p=
\\{s_2=s_3=\\cdots=s_{p-4}=0\\}\\subset\\mathbf P(W)
\\]
be the smooth sparse surface of Paper V, and put
\\[
\\mathscr Q_p=\\mathscr Y_p/C_p.
\\]
The open where $s_{p-3}\\ne0$ is the common fixed-cubic Kummer quotient.
"""
    new2 = """Let
\\[
H=\\{s_1=0\\}\\subset\\mathbf A^p,
\\qquad L=\\mathbf A^1(1,\\ldots,1),
\\qquad W=H/L,
\\]
and define
\\[
\\mathscr Y_p=
\\{s_2=s_3=\\cdots=s_{p-4}=0\\}\\subset\\mathbf P(W).
\\]
For $p\\ge11$ this is a smooth complete-intersection surface.  Indeed, on the affine cone a Jacobian rank drop forces at most $p-5$ distinct coordinate values; adjoining the $m=0$ power-sum relation gives a square Vandermonde system for their multiplicities, forcing a single coordinate value.  Thus the affine singular locus is exactly the diagonal line, which disappears after quotienting by $L$ and projectivising.  Put
\\[
\\mathscr Q_p=\\mathscr Y_p/C_p.
\\]
The open where $s_{p-3}\\ne0$ is the common fixed-cubic Kummer quotient.
"""
    text = once(text, old2, new2, "projective surface local definition")

    text = once(
        text,
        "The complement is the\nfixed-cubic open, whose count is Theorem 11.2 multiplied by the \\(p-1\\)\nnonzero shifts.",
        "The complement is the fixed-cubic open, whose count is exactly the second formula of Theorem 11.2.",
        "compactified-count proof wording",
    )
    text = once(
        text,
        "Every uniform theorem in the preceding sections is proved symbolically.  The\nclean-room script described here supplies independent finite regressions of the\nalgebraic carriers and point-count ledgers; no theorem is inferred from a\nfinite scan.",
        "Every uniform theorem presented in the preceding sections as proved is established symbolically. The clean-room script described here supplies independent finite regressions of the algebraic carriers and point-count ledgers; no uniform theorem is inferred from a finite scan.",
        "reproducibility scope",
    )

    forbidden = [
        "Paper V", "preceding paper", "six-paper sequence", "this series",
        "BozzardPaperV", "D1-QLINE-NONSAT", "programme boundary",
    ]
    bad = [x for x in forbidden if x in text]
    if bad:
        raise RuntimeError(f"standalone dependency token remains: {bad}")

    stmt_re = re.compile(r"^## (Proposition|Theorem|Corollary) ([0-9]+\.[0-9]+)", re.M)
    source_statements = [f"{x} {y}" for x, y in stmt_re.findall(src)]
    output_statements = [f"{x} {y}" for x, y in stmt_re.findall(text)]
    if source_statements != output_statements:
        raise RuntimeError(f"statement sequence changed: source={source_statements}, output={output_statements}")
    if len(output_statements) != 16:
        raise RuntimeError(f"expected 16 statements, found {len(output_statements)}")

    bib = SRC_BIB.read_text(encoding="utf-8")
    bib = re.sub(r"\n@unpublished\{BozzardPaperV,.*?\n\}\n", "\n", bib, flags=re.S)
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

    status = """# Standalone Paper VI — claim status

**Publication role:** integral secondary traces and quotient geometry for the cubic function-field nonvanishing problem.

## Proved in the manuscript

- Cartier first-moment and translation/q-line projector identities;
- cyclotomic tangent formula;
- nonsplit tangent extension and Frobenius-blindness theorem;
- nonexistence of an ordinary divided-hook virtual representation;
- Hattori--Stallings coefficient extraction;
- free root-cycle action and explicit global Artin--Schreier quotient;
- irreducibility section and split-level emptiness;
- Kummer-form classification and common quotient counts;
- unique projective fixed point and compactified quotient count.

## Exact finite regressions

- dual-number tangent checks at p=5,7,11;
- divided-hook Fourier multiplicities;
- Hattori--Stallings random matrix checks at p=5,7;
- no-split finite checks at p=7,11;
- Kummer sign checks at p=5,11,17,23,29;
- compactified point-count ledger at p=7,11,17,23.

## Open

- uniform nonvanishing of a fixed-class Cartier moment;
- a rational point on the Kummer irreducibility open for every admitted prime;
- N_sq + N_ns > 0 when N_2=0;
- the universal function-field d=1 crown;
- any implication to the integer Fortune conjecture.
"""
    (OUT / "CLAIM_STATUS.md").write_text(status, encoding="utf-8")

    referee = """# Independent-standalone referee read — Paper VI

**Disposition:** `PASS_AFTER_DEPENDENCY_CLOSURE`

The rebuild supplies locally the three pieces formerly imported from the preceding function-field paper: the exact crown-coordinate decomposition, the q-line square-class selection rule, and the definition/smoothness argument for the projective sparse surface. All 16 labelled source statements are preserved.

A minor source wording error in the proof of Theorem 13.1 was also repaired: the fixed-cubic open count is already the second formula of Theorem 11.2 and must not be multiplied by an additional factor p-1.

The central negative conclusion is unchanged. The Artin--Schreier and Kummer quotients give exact positive geometric carriers, but their rational-point nonvanishing is equivalent to the same cubic positivity target rather than a weaker theorem.
"""
    (OUT / "REFEREE_READ.md").write_text(referee, encoding="utf-8")

    repro = """# Reproducibility boundary — Paper VI

The symbolic theorem sequence is independent of the finite scans. The independently rerun algebraic reconstruction checks tangent modules, divided-hook multiplicities, Hattori--Stallings extraction, no-split cases, Kummer classes and quotient point-count ledgers. These computations are regression/certificate evidence only and do not prove the uniform Kummer-open rational-point theorem.
"""
    (OUT / "REPRODUCIBILITY.md").write_text(repro, encoding="utf-8")

    manifest = {
        "paper": "VI",
        "source": str(SRC.relative_to(ROOT)),
        "source_bibliography": str(SRC_BIB.relative_to(ROOT)),
        "standalone": str((OUT / "manuscript.md").relative_to(ROOT)),
        "statement_count": len(statements),
        "statement_sequence": statements,
        "logical_cross_paper_dependencies": 0,
        "source_prose_repair": "Theorem 13.1 proof: U_p count already includes the p-1 shifts",
        "universal_crown_proved": False,
        "integer_transfer_proved": False,
    }
    (OUT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"PAPER6_STANDALONE_BUILD_OK statements={len(statements)} words={len(text.split())}")


if __name__ == "__main__":
    main()
