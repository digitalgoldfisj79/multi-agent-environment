#!/usr/bin/env python3
"""Assemble and de-lineage the four frozen Paper VII manuscript parts."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "publications/fortune-paper-vii-endpoint-incidence-20260731"
PARTS = [
    SRC / "manuscript_parts/00-frontmatter-introduction-algebraisation.md",
    SRC / "manuscript_parts/01-defect-rigidity-and-cubic.md",
    SRC / "manuscript_parts/02-relaxation-and-quadratic-theorem.md",
    SRC / "manuscript_parts/03-lineage-frontier-and-appendix.md",
]
OUT = ROOT / "publications/fortune-standalone-20260811/paper7_bilateral_endpoint_incidence"

FRONT = r'''---
title: "Bilateral Endpoint Incidences over Finite Fields"
subtitle: "Defect rigidity, Frobenius orientation, and quadratic emptiness"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "11 August 2026"
lang: en-GB
bibliography: references.bib
link-citations: true
reference-section-title: References
---

**Abstract.** We study a simultaneous bilateral endpoint incidence among four distinct irreducible polynomials of common degree over finite fields. The local formulation initially contains modular inverses; we remove them exactly and express simultaneous contact as four polynomial divisibilities. For odd prime field size \(q\) with \(q>k\), the quotient polynomials possess a unique common defect \(h\) of degree at most \(q-2k\). The zero-defect locus is exactly the union of translation and reflection families, implying that the intermediate strip \(k<q<2k\) is empty. An explicit incidence over \(\mathbf F_{11}\) at \(k=3\) shows that nonzero-defect components genuinely occur.

We distinguish the bounded-degree algebraic relaxation from the arithmetic incidence: the relaxation retains value identities associated with a cyclic ordering but does not impose that this ordering is the Frobenius cycle. Its dimension therefore cannot determine the true incidence count. For modulus degree \(k=2\), a faithful q-free four-equation reduction and a two-chart exact ideal-membership certificate force all arithmetic-open solutions onto a component where both quadratic discriminants are squares, contradicting irreducibility. This gives a computer-assisted exact quadratic-emptiness theorem over every odd prime power. The accompanying Lean development kernel-checks the q-free power-lift identities and the chart-selection/discriminant logic; the full datum-to-normal-form reduction remains represented by one explicit custom normalization axiom, so the Lean theorem is not axiom-free.

The remaining arithmetic region is \(3\le k<q\) with \(q\ge2k\). The next relevant problem is a twisted-Frobenius point theorem on the true oriented components, not another dimension calculation on the relaxation. No function-field crown, endpoint dispersion theorem, or integer Fortune theorem is proved.

**Keywords:** finite fields; irreducible polynomials; Frobenius orientation; computer-assisted proof; incidence geometry.

# 1. Scope and theorem roadmap

Let \(\mathbf F_q[t]\) be a polynomial ring of odd characteristic. This paper studies an algebraic incidence that arises naturally when two endpoint contacts are imposed simultaneously on two ordered pairs of irreducible moduli. The incidence theory is treated here as an independent finite-field problem: no prior function-field Fortune manuscript is needed for its definitions or proofs, and no theorem below is asserted to transfer to the integer Fortune conjecture.

There are four layers.

1. The modular inverses are removed exactly, producing a bounded-degree coefficient scheme.
2. In odd prime fields with \(q>k\), a common bilateral defect gives a sharp zero-defect classification and an empty intermediate strip.
3. The q-uniform root-cycle relaxation is separated from the true Frobenius-oriented arithmetic locus; an explicit cubic example proves that nonzero-defect components exist.
4. At \(k=2\), exact algebraic certificates plus a discriminant contradiction prove emptiness over every odd prime power.

The quadratic theorem is computer-assisted in the algebraic-certificate sense, not a finite census. Its mathematical proof package contains the faithful reduction, chart cover, ideal-membership certificates and exceptional-characteristic checks. The formal Lean package currently has a narrower trust boundary: it verifies the q-free chart identities and downstream contradiction but still assumes the genuine-incidence-to-certified-normal-form reduction through the single ledgered axiom `p7_k2_certified_normalization`.

'''

SCOPE10 = r'''# 10. Scope relative to Fortune-type nonvanishing problems

The bilateral incidence can occur inside a broader function-field investigation of Fortune-type prime-output questions, but the present theorem sequence is logically independent of the normal-form and quotient constructions used in other approaches. In particular, quadratic endpoint emptiness does not imply positivity of any separate function-field crown, and the explicit cubic incidence does not by itself provide an endpoint dispersion estimate.

Accordingly, this article makes only the following scope claims:

- the incidence definitions and all hand proofs are local to this manuscript;
- the quadratic theorem is an exact computer-assisted incidence theorem with the formal trust boundary described in Section 12;
- no theorem here proves a universal function-field Fortune statement;
- no theorem here transfers to the integer Fortune conjecture without a separate transference theorem.

'''

FRONTIER11 = r'''# 11. Remaining existence frontier

The results proved here give the following self-contained regime summary.

| Regime | Status in this paper |
|---|---|
| \(k=2\), odd prime powers \(q\) | empty by Theorem 9.1 |
| \(k<q<2k\), odd primes \(q\) | empty by Corollary 5.3 |
| \(3\le k<q,\ q\ge2k\) | open; explicit nonzero-defect cubic examples exist |

The range \(q\le k\) is not classified in this manuscript and is not needed for Theorem 9.1 or the intermediate-strip result.

The open region begins with cubic nonzero-defect components. The appropriate next theorem is not a dimension statement for the q-uniform relaxation. It is a componentwise count or classification of points whose cyclic root orderings are the actual Frobenius cycles. A useful cubic theorem would, after affine normalisation, prove a bounded or explicitly periodic count of true oriented points; restoring the affine orbit would then convert this to an incidence bound.

Even such an existence theorem would be only one gate in a larger endpoint-dispersion programme. The literal endpoint amplitudes, affine-orbit cancellation, frequency restoration and any transfer to an integer problem remain separate questions. None is asserted here.

'''

REPRO12 = r'''# 12. Reproducibility and formal trust boundary

The computer-assisted quadratic theorem is accompanied by the q-free four-equation reduction, two localisation charts, exact ideal-membership data, faithfulness checks, exceptional-characteristic certificates, and symbolic discriminant-square verification. These are algebraic certificates rather than sampled-solution evidence. The finite cubic censuses in Section 7 are regression and motivation only.

A subsequent formal-assurance pass separated the certificate calculation from the normalization theorem more sharply. Six q-free power-lift identities—three target identities on each chart—were regenerated with exact denominator clearing and checked by the Lean kernel over integer multivariate polynomials. The chart-selection theorem taking those six identities to the certified component is also kernel checked. A compact rational lift has denominator-prime support contained in \(\{2,3,5\}\); the original direct characteristic certificates cover the exceptional odd characteristics needed by the mathematical proof package.

The Lean formalization should nevertheless be described precisely. It does **not** yet prove Theorem 9.1 from Mathlib alone. The file `FortuneFormal/Frontier/Assumptions.lean` contains the single custom axiom

`p7_k2_certified_normalization`,

whose content is the remaining genuine-incidence-to-certified-q-free-normal-form reduction. From that axiom the kernel derives the discriminant contradiction and the quadratic emptiness statement. Thus:

- the q-free polynomial certificate layer is kernel checked;
- the chart-selection and discriminant contradiction are kernel checked;
- the full formal theorem remains `DERIVED_WITH_LEDGERED_AXIOM`, not axiom-free;
- the manuscript's computer-assisted theorem continues to rely on the independently reproducible normalization/faithfulness proof package until that reduction is formalised.

No finite computation is promoted to a uniform theorem merely by testing primes.

'''

BOUNDARY13 = r'''# 13. Boundary

The stable contribution of this paper is:

- an exact inverse-free coefficient scheme;
- the common-defect theorem;
- a complete zero-defect classification for odd prime \(q>k\);
- emptiness of the intermediate strip \(k<q<2k\);
- an explicit nonzero-defect cubic incidence;
- a precise relaxation-versus-Frobenius-orientation distinction;
- an exact computer-assisted quadratic-emptiness theorem for every odd prime power.

The following stronger statements are explicitly not claimed: universal \(q>k\) emptiness; universal \(c+d=0\); control of true incidence counts from relaxation dimension; a function-field crown; an endpoint dispersion theorem; or the integer Fortune conjecture.

The next mathematically meaningful target is the cubic twisted-Frobenius point theorem. Further Gröbner calculations or relaxation point counts are useful only insofar as they enter such an arithmetic proof.

# AI-assistance disclosure

Large language models were used for structured derivation, software drafting, adversarial review, exact-computation design, formal-assurance work and editorial assembly. Human-proof, computer-assisted, formally kernel-checked, finite empirical and open claims are distinguished explicitly. The named author takes responsibility for the mathematics, code, citations and final presentation.

# Data and code availability

The reproducibility package contains the source-fidelity audit, certificate scripts, q-free power-lift identities, Lean formalisation, machine-readable outputs, review records and release checks. Frozen commit identifiers and file hashes are recorded in the publication support manifest.

'''


def section_replace(text: str, start: str, end: str, replacement: str) -> str:
    a = text.find(start)
    b = text.find(end, a + len(start))
    if a < 0 or b < 0:
        raise RuntimeError(f"missing section markers: {start!r}, {end!r}")
    return text[:a] + replacement + text[b:]


def build() -> tuple[str, str, list[str]]:
    source = "".join(p.read_text(encoding="utf-8") for p in PARTS)
    # The source fragments intentionally overlap at continuation boundaries only by syntax,
    # not by repeated prose; direct concatenation reconstructs the frozen article.
    body = source[source.find("# 2. Bilateral endpoint incidence\n"):]
    if not body:
        raise RuntimeError("Paper VII section 2 marker missing")
    text = FRONT + body

    text = section_replace(text, "# 10. Relation to Papers V and VI\n", "# 11. The remaining existence frontier\n", SCOPE10)
    text = section_replace(text, "# 11. The remaining existence frontier\n", "# 12. Reproducibility\n", FRONTIER11)
    text = section_replace(text, "# 12. Reproducibility\n", "# 13. Boundary\n", REPRO12)
    # Replace boundary through Appendix A, preserving the explicit q-free equations.
    text = section_replace(text, "# 13. Boundary\n", "# Appendix A. The quadratic four-equation system\n", BOUNDARY13)

    # Add the current formal trust status immediately after the exact chart certificate proof.
    needle = "The computation is an exact ideal-membership proof.  It does not infer a\nuniform statement from sampled solutions. \\(\\square\\)"
    replacement = needle + "\n\nThe q-free chart identities entering this argument have subsequently been regenerated as exact power-lift certificates and checked in Lean; Section 12 states precisely which normalization step remains outside the kernel."
    if needle not in text:
        raise RuntimeError("quadratic certificate close marker changed")
    text = text.replace(needle, replacement, 1)

    forbidden = [
        "Papers V", "Paper V", "Paper VI", "Fortune programme", "publication lineage",
        "corrective sequel", "six-paper sequence", "BozzardPaperV", "BozzardPaperVI",
        "input to Paper", "P7-CUBIC-TF",
    ]
    bad = [x for x in forbidden if x in text]
    if bad:
        raise RuntimeError(f"standalone dependency token remains: {bad}")

    stmt_re = re.compile(r"^## (Theorem|Corollary|Lemma) ([0-9]+\.[0-9]+)", re.M)
    source_statements = [f"{a} {b}" for a, b in stmt_re.findall(source)]
    output_statements = [f"{a} {b}" for a, b in stmt_re.findall(text)]
    if source_statements != output_statements:
        raise RuntimeError(f"statement sequence changed: {source_statements} -> {output_statements}")
    if len(output_statements) != 7:
        raise RuntimeError(f"expected 7 labelled statements, found {len(output_statements)}")

    bib = (SRC / "references.bib").read_text(encoding="utf-8")
    bib = re.sub(r"\n@unpublished\{BozzardPaperV,.*?\n\}\n", "\n", bib, flags=re.S)
    bib = re.sub(r"\n@unpublished\{BozzardPaperVI,.*?\n\}\n", "\n", bib, flags=re.S)
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

    status = """# Standalone Paper VII — claim status

## Proved by hand in the manuscript

- inverse-free equivalence and uniqueness of endpoint witnesses;
- common bilateral defect and degree bound for odd prime q>k;
- zero-defect translation/reflection classification in that range;
- forced zero defect and empty intermediate strip k<q<2k for odd primes;
- affine covariance and q-uniform root-cycle relaxation/orientation distinction.

## Exact computer-assisted theorem

- no cross-distinct bilateral endpoint incidence at k=2 over any odd prime power.

## Formal status of the quadratic theorem

- six q-free chart power-lift identities: Lean-kernel checked;
- chart-selection and discriminant contradiction: Lean-kernel checked;
- datum-to-certified-normal-form reduction: one custom axiom `p7_k2_certified_normalization`;
- therefore the Lean theorem is `DERIVED_WITH_LEDGERED_AXIOM`, not axiom-free.

## Exact finite evidence, not uniform theorem

- explicit nonzero-defect cubic incidence at (q,k)=(11,3);
- cubic oriented/relaxation censuses on frozen prime panels.

## Open

- cubic twisted-Frobenius point theorem and componentwise true-orientation classification;
- endpoint amplitude/cancellation and dispersion layers;
- universal function-field crown;
- every integer Fortune transfer.
"""
    (OUT / "CLAIM_STATUS.md").write_text(status, encoding="utf-8")

    referee = """# Independent-standalone referee read — Paper VII

**Disposition:** `PASS_WITH_EXPLICIT_FORMAL_TRUST_BOUNDARY`

The four source manuscript fragments have been assembled into one continuous article. The publication-lineage section and imported k>=q context were removed because neither is needed for the theorem sequence. All seven labelled source statements are preserved.

The principal assurance correction is terminological rather than mathematical: Theorem 9.1 remains an exact computer-assisted theorem supported by the external algebraic certificate package, but the current Lean implementation is not axiom-free. It derives the theorem from the single custom normalization axiom after kernel-checking the q-free chart identities and discriminant contradiction. The standalone manuscript states this distinction explicitly.
"""
    (OUT / "REFEREE_READ.md").write_text(referee, encoding="utf-8")

    manifest = {
        "paper": "VII",
        "sources": [str(p.relative_to(ROOT)) for p in PARTS],
        "standalone": str((OUT / "manuscript.md").relative_to(ROOT)),
        "statement_count": len(statements),
        "statement_sequence": statements,
        "logical_cross_paper_dependencies": 0,
        "quadratic_mathematical_status": "EXACT_COMPUTER_ASSISTED",
        "quadratic_lean_status": "DERIVED_WITH_LEDGERED_AXIOM",
        "custom_axiom": "FortuneFormal.p7_k2_certified_normalization",
        "fortune_proved": False,
    }
    (OUT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"PAPER7_STANDALONE_BUILD_OK statements={len(statements)} words={len(text.split())}")


if __name__ == "__main__":
    main()
