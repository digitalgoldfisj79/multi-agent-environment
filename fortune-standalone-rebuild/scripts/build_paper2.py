#!/usr/bin/env python3
"""Build standalone Paper II from the authoritative corrected manuscript.

The theorem/proof body is inherited verbatim except for narrowly scoped
publication-language replacements.  Front matter, introduction, open-boundary
section, conclusion and evidence ledger are rebuilt so the article can be read
without any other Fortune manuscript or internal programme note.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "publications/fortune-papers-ii-vi-20260724/paper2_revised/manuscript.md"
SRC_BIB = ROOT / "publications/fortune-papers-ii-vi-20260724/paper2_revised/references.bib"
OUT = ROOT / "publications/fortune-standalone-20260811/paper2_prime_pair_detection"

FRONT_AND_INTRO = r'''---
title: "Prime-Pair Detection at Primorial Centres"
subtitle: "Exact existence criteria, reciprocal frames, and structural obstructions"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "11 August 2026"
bibliography: references.bib
---

**Abstract.** Let \(P_n=\prod_{p\le p_n}p\) and let \(F_n\) be the least integer \(m>1\) for which \(P_n+m\) is prime. We begin with the elementary but decisive observation that, below the square threshold \(p_{n+1}^2\), every offset producing a prime at a primorial centre must itself be prime. Prime detection at that scale is therefore a two-prime problem. We prove an exact prime-pair detector decomposition, three block criteria showing that sufficiently sharp mean-square control excludes every failed primorial centre, and an exact double-von-Mangoldt Fourier representation whose geometric kernel is the single cumulative-product walk. The Hardy--Littlewood singular-series expressions used to calibrate the expected means are stated explicitly as conjectural rather than proved asymptotics.

Independently of that direct detector, we analyse a reciprocal pair-sum model attached to the same cumulative-product path. We prove an exact harmonic-energy decomposition with one-sided centring, an exact fourth moment and centred \(L^2\) law for the pair-sum polynomial, a growing-degree cumulative Möbius truncation, a semiprime-resonance obstruction to positive density surrogates, exact multiplicative-character diagonal and ratio identities, a local failure certificate, critical-scale coherence and conductor-migration results, and a Fourier-scale conservation obstruction. These results explain why several natural large-sieve, density, character-factorisation and large-value mechanisms do not by themselves yield the required prime-pair variance. No source-to-reciprocal transference theorem and no proof of Fortune's conjecture is claimed.

**Keywords:** Fortunate numbers; primorials; prime pairs; primes in short intervals; reciprocal exponential sums; Barban--Davenport--Halberstam variance; multiplicative characters; sieve parity.

**MSC 2020:** 11N05, 11N13, 11N35, 11L07, 11B83.

# Introduction

Let \(p_n\) denote the \(n\)-th prime and define the primorial
\[
P_n=\prod_{p\le p_n}p.
\]
The \(n\)-th Fortunate number is the least integer \(F_n>1\) for which \(P_n+F_n\) is prime [@guy2004]. Every prime divisor of \(F_n\) exceeds \(p_n\); hence
\[
F_n\text{ composite}\quad\Longrightarrow\quad F_n\ge p_{n+1}^2.
\tag{1.1}
\]
Consequently, a prime in
\[
(P_n,P_n+p_{n+1}^2)
\tag{1.2}
\]
forces \(F_n\) to be prime. Since \(p_{n+1}^2=(1+o(1))(\log P_n)^2\), this is a pointwise prime-detection problem at a Cramér--Granville-scale interval around a prescribed and extremely sparse sequence of centres [@granville1995]. Classical and modern results on primes in short intervals or mean-square prime distribution average over substantially denser families of centres and do not directly supply such pointwise information [@goldston-montgomery1987; @chan2003; @montgomery-soundararajan2004; @harper2025].

The first purpose of this paper is to identify the exact arithmetic object that must be controlled at this scale. Fix a dyadic block of consecutive primes \(X\le \ell_1<\cdots<\ell_N<2X\), set
\[
A_X=\prod_{p<X}p,\qquad Q_j=\prod_{u=1}^j\ell_u,\qquad P_j=A_XQ_j,
\]
and take \(H=\eta X^2\) with fixed \(0<\eta<1\). If \(P_j+m\) is prime for \(1<m<H<\ell_{j+1}^2\), then \((m,P_j)=1\), and every prime factor of \(m\) exceeds \(\ell_j\). Thus \(m\) itself is prime. The exact existence variable is therefore
\[
Z_j(H)=\#\{m\le H:m\text{ prime and }P_j+m\text{ prime}\},
\]
not an ordinary shifted-prime count. We also use the weighted variants
\[
Y_j(H)=\sum_{m\le H}\mathbf1_{\mathbb P}(m)\Lambda(P_j+m),
\qquad
T_j(H)=\sum_{m\le H}\Lambda(m)\Lambda(P_j+m).
\]
A single failed centre creates a discrepancy of the same order as the full expected mean. This converts sufficiently sharp block variance bounds into exact no-failure criteria. The proofs of those implications are elementary; the missing mathematics is the variance theorem itself.

The second purpose is structural. Reciprocal harmonic sampling of the cumulative-product path naturally produces the pair-sum polynomial
\[
H_2(\theta)=\sum_{0\le j\le k<N}e\bigl(\theta(P_j+P_k)\bigr)
\]
and kernels of the form
\[
\left|H_2\!\left(a\left(\frac1q-\frac1r\right)\right)\right|^2-M,
\qquad M=\frac{N(N+1)}2.
\tag{1.3}
\]
We study this reciprocal frame as an independent deterministic model. It has exact collision, moment, Möbius and character structure, but no theorem in this paper transfers the direct two-prime detector to that frame. This separation is deliberate: it prevents a structural identity about the reciprocal model from being mistaken for a prime-detection theorem.

The principal results are grouped as follows.

1. **Exact detector and no-failure criteria.** Proposition 2.3 proves candidate collapse and isolates the proper-prime-power remainder. Theorems 2.4, 2.5 and 2.7 give unweighted, weighted and double-von-Mangoldt block criteria. Theorem 2.8 gives the exact double-von-Mangoldt source-to-walk Fourier identity.
2. **Reciprocal-frame structure.** Propositions 3.1 and 3.2 give exact harmonic aggregation and the one-sided residual decomposition. Theorem 4.2 gives the exact fourth moment of the pair-sum polynomial and its centred \(L^2\) mass.
3. **Signed detector and obstruction results.** Theorem 5.2 gives a growing-degree Möbius truncation with negligible high-degree tail while preserving the need for global signed coupling. Theorem 6.1 shows that a positive Hardy--Littlewood density surrogate is polynomially too large because of resonant semiprimes. Theorems 7.1 and 7.2 and Corollary 7.3 show that multiplicative-character factorisation does not de-tensorise the load-bearing additive kernel.
4. **Sparse-centre and harmonic obstructions.** Theorem 8.1 converts Fortune failure into a cubic local Selberg-energy lower bound. Theorems 8.2 and 8.3 establish critical-scale phase coherence and moving conductors along primorial centres. Proposition 9.1 and Lemma 9.2 show why enlarging the harmonic family or using power-scale large values does not create the required fine arithmetic alignment.

## Status of results

The article uses four distinct epistemic classes.

- Statements labelled theorem, proposition, lemma or corollary are proved in the text.
- Hardy--Littlewood formulae used for \(\lambda_j\), \(\mu_j\) and \(\nu_j\) are conjectural calibrations; the no-failure implications require only baselines of the displayed orders.
- Finite computations in the reproducibility section validate exact identities or illustrate diagnostics and are not used to infer asymptotic theorems.
- The required sparse-centre prime-pair variance estimates and any source-to-reciprocal transference theorem remain open.

The paper is therefore a collection of exact reductions, structural theorems and obstruction results around a sharply stated open analytic boundary. It does not prove Fortune's conjecture.

'''

OPEN_BOUNDARY = r'''# Open analytic boundary

The direct arithmetic results isolate three sufficient variance estimates. None is proved in this paper.

For the unweighted prime-pair detector, the target is
\[
\boxed{
\sum_{j<N}|Z_j(H)-\lambda_j(H)|^2
\ll NX L(X),
\qquad L(X)=o(\log X),
}
\tag{12.1}
\]
where the Hardy--Littlewood expression (2.19) supplies the conjectural calibration \(\lambda_j(H)\asymp X\). Theorem 2.4 shows that (12.1) would exclude every failed centre in a sufficiently large dyadic block.

For the singly weighted detector, the corresponding target is
\[
\boxed{
\sum_{j<N}|Y_j(H)-\mu_j(H)|^2
\ll NHX L(X),
\qquad L(X)=o(\log X),
}
\tag{12.2}
\]
with conjectural calibration \(\mu_j(H)\asymp H\); Theorem 2.5 gives the deterministic implication.

For the double-von-Mangoldt source, an analytically natural sufficient target is
\[
\boxed{
\sum_{j<N}|T_j(H)-\nu_j(H)|^2
\ll NHX(\log X)^2L(X),
\qquad L(X)=o(\log X),
}
\tag{12.3}
\]
where \(\nu_j(H)=\mathfrak S(P_j)H\) is the conjectural Hardy--Littlewood calibration. Theorem 2.7 again turns this variance estimate into a no-failure statement.

Theorem 2.8 rewrites the double-von-Mangoldt variance exactly in Fourier variables. This does not solve (12.3): its source \(G_X=A_HB_X\) retains both prime weights and their common offset. A second possible representation starts from the shifted detector \(\Psi_j\), uses Proposition 2.3 to recenter it at the prime-pair scale \(\mu_j\), and keeps the prime-power remainder explicit. Either representation would require a new transference theorem before the reciprocal pair-sum frame of Sections 3--9 could become load-bearing for Fortune.

Thus the reciprocal residual bound analysed in this paper remains a well-defined deterministic model problem, not a proved equivalent of (12.1)--(12.3). The obstruction theorems explain why several natural attempts to build such a bridge fail, but they do not rule out every possible signed transference mechanism.

'''

CONCLUSION = r'''# Conclusion

At the square threshold relevant to Fortunate numbers, primorial-centre prime detection collapses to a prime-pair problem: a successful offset must itself be prime. This observation fixes the correct arithmetic source before any harmonic or sieve decomposition is attempted. The paper proves exact no-failure criteria for three versions of that source and an exact Fourier representation for the double-von-Mangoldt correlation. What remains open is the sparse-centre variance estimate at the required scale.

The reciprocal pair-sum analysis supplies a separate body of exact mathematics. Its one-sided harmonic decomposition, exact fourth moment, globally coupled Möbius truncation, semiprime resonance theorem, character-ratio collapse, sparse-centre coherence results and harmonic-scale conservation law sharply constrain possible transference arguments. In particular, positive density replacement, naive CRT de-tensorisation, ordinary large-value information and artificial enlargement of the harmonic family do not supply the missing prime-pair variance theorem.

The logical boundary is therefore explicit. Theorems 2.4, 2.5 and 2.7 are exact implications; the Hardy--Littlewood baselines are conjectural calibrations; the reciprocal-frame results are unconditional statements about that model; and no source-to-reciprocal transference theorem is known. No prime-pair asymptotic and no proof of Fortune's conjecture is claimed.

# AI-assistance disclosure

Large language models were used for literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. Every mathematical statement presented as a theorem is accompanied by a proof in the manuscript. Conjectural, conditional, computational, diagnostic and negative results are distinguished explicitly. The named author takes responsibility for the mathematical content, citations, code and final presentation.

# References

::: {#refs}
:::
'''


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {n}")
    return text.replace(old, new, 1)


def build() -> tuple[str, str]:
    src = SRC.read_text(encoding="utf-8")

    # Replace everything from the YAML opening through the first body heading.
    marker = "# Primorial blocks and the direct detector\n"
    pos = src.find(marker)
    if pos < 0:
        raise RuntimeError("Paper II body marker not found")
    body = src[pos:]
    text = FRONT_AND_INTRO + body

    # Remove provenance/programme phrasing without altering theorem content.
    replacements = {
        "## Correct block-variance implications": "## Block-variance implications",
        "The following criteria separate the exact implication from the conjectural\nchoice of main term.":
            "The following criteria separate the exact deterministic implication from the conjectural\nchoice of main term.",
        "For the explicit double-von-Mangoldt route, the first exact harmonic object is":
            "For the double-von-Mangoldt representation, the first exact harmonic object is",
        "There is also a distinct one-sided route: Proposition 2.3 shows that the":
            "There is also a distinct one-sided representation: Proposition 2.3 shows that the",
        "but it must recompute the principal term at the square-root sieve boundary.\nThe pair-sum frame below is therefore retained as a model whose connection to\neither corrected source remains unproved, not as a route that has been\nrefuted.":
            "but it must compute the principal term at the square-root sieve boundary.\nThe pair-sum frame below is therefore analysed as a model whose connection to\neither prime-pair source is proved; none of the structural results below is used\nas a substitute for that missing transference theorem.",
        "The corrected criteria in Theorems 2.4--2.7 are the direct Fortune implications. The following reciprocal pair-sum frame is an independent structural model inherited from the earlier programme; no transference from the corrected two-prime source is presently proved.":
            "Theorems 2.4--2.7 give the direct Fortune implications. We now introduce an independent reciprocal pair-sum model on the same cumulative-product path. It is motivated by harmonic sampling of pair differences; no transference from the two-prime source to this model is proved.",
        "The earlier uncorrected architecture proposed the following local target:":
            "A natural local target for this reciprocal model is:",
        "Equation (3.6) is not presently derived from Theorems 2.4--2.7. For the\ndouble-von-Mangoldt source, (2.24) contains the additional factor \\(A_H\\).\nFor the recentered one-sided source \\(\\Psi_j-\\mu_j\\), that factor is implicit\nrather than explicit, but the old principal cancellation was calibrated at\n\\(H\\) and has not been rebuilt at \\(\\mu_j\\). Consequently (3.6) is treated as\na deterministic model estimate whose internal structure is analysed below.\nProving it for the increasing order could contribute to Fortune only together\nwith a new corrected source-to-frame theorem; the present manuscript neither\nproves nor rules out such a theorem.":
            "Equation (3.6) is not derived from Theorems 2.4--2.7. For the\ndouble-von-Mangoldt source, (2.24) contains the additional factor \\(A_H\\).\nFor the recentered one-sided source \\(\\Psi_j-\\mu_j\\), that factor is implicit\nrather than explicit, and no principal-cancellation theorem at the prime-pair\nmean \\(\\mu_j\\) is proved. Consequently (3.6) is treated as a deterministic\nmodel estimate whose internal structure is analysed below. Proving it for the\nincreasing order could contribute to Fortune only together with a new\nsource-to-frame theorem; the present manuscript neither proves nor rules out\nsuch a theorem.",
    }
    for old, new in replacements.items():
        text = replace_exact(text, old, new, old[:50])

    # Replace the historical terminal boundary and conclusion wholesale.
    boundary_start = text.find("# The corrected theorem boundary\n")
    conclusion_start = text.find("# Conclusion\n", boundary_start)
    if boundary_start < 0 or conclusion_start < 0:
        raise RuntimeError("historical boundary/conclusion markers not found")
    text = text[:boundary_start] + OPEN_BOUNDARY + CONCLUSION

    # Publication-facing language should not require knowledge of a series.
    forbidden = [
        "Paper I", "Paper III", "preceding programme", "earlier programme",
        "earlier uncorrected", "Correction notice", "first circulation edition",
        "corrected edition", "former weighted", "programme boundary",
        "INT-ISC", "RUHL-FM", "D1-QLINE-NONSAT", "P7-CUBIC-TF",
    ]
    for token in forbidden:
        if token in text:
            raise RuntimeError(f"standalone dependency/provenance token remains: {token!r}")

    # Preserve the complete theorem/proposition/lemma/corollary sequence.
    stmt_re = re.compile(r"^\*\*(Theorem|Proposition|Lemma|Corollary)\s+([0-9]+\.[0-9]+)", re.M)
    source_statements = stmt_re.findall(src)
    out_statements = stmt_re.findall(text)
    if source_statements != out_statements:
        raise RuntimeError(
            "statement sequence changed during standalone rebuild:\n"
            f"source={source_statements}\nout={out_statements}"
        )

    # Keep citation closure local. Companion Paper I is not needed by the standalone article.
    bib = SRC_BIB.read_text(encoding="utf-8")
    bib, n = re.subn(r"@misc\{bozzard2026paper1,.*?\n\}\n\n", "", bib, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError("could not remove companion-paper bibliography entry")
    cite_keys = set(re.findall(r"@([A-Za-z0-9_.:-]+)", text))
    bib_keys = set(re.findall(r"@[A-Za-z]+\{([^,]+),", bib))
    missing = sorted(cite_keys - bib_keys)
    if missing:
        raise RuntimeError(f"missing local bibliography keys: {missing}")

    return text.rstrip() + "\n", bib.rstrip() + "\n"


def main() -> None:
    text, bib = build()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "manuscript.md").write_text(text, encoding="utf-8")
    (OUT / "references.bib").write_text(bib, encoding="utf-8")

    stmt_re = re.compile(r"^\*\*(Theorem|Proposition|Lemma|Corollary)\s+([0-9]+\.[0-9]+)", re.M)
    statements = [f"{kind} {num}" for kind, num in stmt_re.findall(text)]
    status = "# Standalone Paper II — claim status\n\n"
    status += "**Publication role:** exact prime-pair detection criteria plus independent reciprocal-frame structural mathematics.\n\n"
    status += "## Proved in the manuscript\n\n"
    status += "- Fortunate-number square-threshold lower bound and candidate collapse.\n"
    status += "- Exact unweighted, weighted and double-von-Mangoldt detector implications.\n"
    status += "- Exact double-von-Mangoldt Fourier source identity.\n"
    status += "- Reciprocal-frame harmonic decomposition, fourth moment, Möbius truncation, semiprime-resonance obstruction, character identities, failure certificate, coherence/conductor results and Fourier-scale obstruction.\n\n"
    status += "## Conjectural calibration only\n\n"
    status += "- Hardy--Littlewood singular-series formulae for the expected means of the prime-pair detectors.\n\n"
    status += "## Open\n\n"
    status += "- The sparse-centre variance estimates (12.1)--(12.3).\n"
    status += "- Any theorem transferring either exact prime-pair source to the reciprocal pair-sum frame at the required scale.\n"
    status += "- Fortune's conjecture.\n\n"
    status += "## Computational evidence\n\n"
    status += "Finite validators check selected exact identities and diagnostics only; no asymptotic theorem depends on a finite panel.\n\n"
    status += f"## Preserved formal statement sequence\n\nCount: **{len(statements)}**.\n\n" + "\n".join(f"- {s}" for s in statements) + "\n"
    (OUT / "CLAIM_STATUS.md").write_text(status, encoding="utf-8")

    manifest = {
        "paper": "II",
        "source": str(SRC.relative_to(ROOT)),
        "source_bibliography": str(SRC_BIB.relative_to(ROOT)),
        "standalone_manuscript": str((OUT / "manuscript.md").relative_to(ROOT)),
        "statement_count": len(statements),
        "statement_sequence": statements,
        "logical_cross_paper_dependencies": 0,
        "fortune_proved": False,
        "open_primary_targets": ["12.1", "12.2", "12.3", "source-to-reciprocal transference"],
    }
    (OUT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"PAPER2_STANDALONE_BUILD_OK statements={len(statements)} words={len(text.split())}")


if __name__ == "__main__":
    main()
