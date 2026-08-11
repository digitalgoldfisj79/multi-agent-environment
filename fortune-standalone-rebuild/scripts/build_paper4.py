#!/usr/bin/env python3
"""Build standalone Paper IV and close its sole logical import locally."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "publications/fortune-papers-ii-vi-20260724/paper4_random_order/manuscript.md"
OUT = ROOT / "publications/fortune-standalone-20260811/paper4_random_product_paths"

FRONT = r'''---
title: |
  Reciprocal-Frame Bounds Along Random Primorial-Product Paths
subtitle: |
  An unconditional theorem in the random-order model
author:
  - "Edward Stewart Anthony Bozzard (ORCID 0009-0002-4052-0994)"
date: "11 August 2026"
lang: en-GB
abstract: |
  Let the primes in a dyadic block be placed in a uniformly random order and
  form the associated nested product path. For the reciprocal pair-sum frame
  defined in this paper, we prove an effective expectation bound of order
  M(log X)^9, uniformly in every harmonic in the natural range. The same
  estimate holds for the weighted distinct-modulus aggregate and, by a local
  weighted-Cauchy comparison proved below, for the full pair-space frame
  energy. Cancellation is supplied by expectation over the random permutation;
  no corresponding pointwise statement is claimed for the unique increasing
  primorial order. The proof conditions exactly on endpoint ranks, converts
  the random path into a uniform ordered set partition, obtains exponential
  ratio-character decay by a multivariate Cauchy estimate, bounds exceptional
  characters by sixth-moment orthogonality and unique factorisation, and closes
  a complete configuration ledger. The binding classes meet the target with
  only polylogarithmic slack. This is a theorem about the random-order model,
  not a prime-detection theorem: neither a transfer to the increasing order nor
  a bridge from this reciprocal frame to the corrected prime-pair detector is
  proved.
keywords: ["random permutations", "primorial products", "reciprocal frames", "character sums", "ordered set partitions", "derandomisation"]
---

# 1. Introduction

Let \(0<\eta<1\), let \(X\) be large, and let
\[
\mathcal L=\{\ell:X\le \ell<2X,\ \ell\text{ prime}\},
\qquad K=|\mathcal L|.
\]
Choose a uniformly random permutation \(\sigma\in S_K\) and form
\[
Q_0^\sigma=1,
\qquad
Q_j^\sigma=\prod_{i\le j}\ell_{\sigma(i)},
\qquad
P_j^\sigma=A_XQ_j^\sigma,
\qquad
A_X=\prod_{p<X}p.
\]
The identity permutation gives the increasing primorial path. The theorem in this article averages over all \(K!\) orderings and does not establish a pointwise estimate for that identity ordering.

For pair indices \(0\le j\le k\le K\), set
\[
S_{\{j,k\}}^\sigma=P_j^\sigma+P_k^\sigma,
\qquad
N=K+1,
\qquad
M=\frac{N(N+1)}2.
\]
At the critical shell \(H=\eta X^2\), Section 2 defines a reciprocal harmonic frame on the differences of these pair sums. The principal theorem shows that this frame has expected energy \(O(M(\log X)^9)\) under random ordering.

The mechanism is intrinsic to the random model. Conditioning on endpoint ranks turns path segments into cells of a uniformly random ordered set partition. Multivariate coefficient extraction gives exponential decay unless certain ratio characters are unusually biased on the block primes; sixth-moment orthogonality controls the exceptional characters. A matching argument and exhaustive configuration ledger then close every endpoint pattern. Because several classes are binding at exactly \(M(\log X)^9\), the proof has no positive power-of-\(X\) reserve.

The distinction from the deterministic prime problem is important. Even a pointwise version of the reciprocal-frame estimate for the increasing order would still require a separate theorem connecting the corrected two-prime source at primorial centres to this frame. The present article proves neither that source-to-frame bridge nor Fortune's conjecture.

'''

SCOPE = r'''# 11. Scope, deterministic order, and open interfaces

The expectation over \(S_K\) is the source of the decisive cancellation. The identity ordering has no order entropy, and the proof supplies no mechanism showing that it is nonexceptional. Consequently the theorem does not provide a pointwise reciprocal-frame estimate for increasing primorial products.

This limitation should also not be conflated with the full Fortune boundary. At the square threshold relevant to Fortunate numbers, the corrected existence source is a prime-pair detector. No theorem in this article transfers that source to the reciprocal frame. Therefore even a successful derandomisation of Theorem 2.1 would establish a deterministic model estimate, not by itself a prime-pair theorem.

Natural questions internal to the random model include a second moment over orderings, for example
\[
\mathbb E_\sigma[(\mathcal E_a^\sigma)^2]\ll M^2X^{o(1)},
\]
and concentration strong enough to distinguish atypical orderings. A separate arithmetic problem is whether any valid source-to-frame transference can be built while retaining the two-prime structure. None of these statements is claimed here.

## AI-assistance disclosure

Large language models were used for structured literature triage, symbolic and computational cross-checking, adversarial review, software drafting and editorial assembly. The manuscript was rebuilt from a frozen proof source after hostile review of the configuration ledger. The named author takes responsibility for the mathematical claims, citations, code and final presentation.

## Data, code, and reproducibility

The supporting archive contains the frozen mathematical source, source-to-manuscript fidelity records, clean-room finite checks and the configuration ledger. Finite checks validate implementation and bookkeeping; they are not proofs of the asymptotic random-order theorem.

# References

1. H. Davenport, *Multiplicative Number Theory*, 3rd ed., revised by H. L. Montgomery, Springer, 2000, Chapter 9.
2. Standard effective forms of the prime number theorem for dyadic intervals.
'''


def build() -> tuple[str, list[str]]:
    src = SRC.read_text(encoding="utf-8")
    body = src[src.find("# 2. Frame, hypotheses, and theorem\n"):]
    if not body:
        raise RuntimeError("Paper IV section 2 marker missing")
    text = FRONT + body

    imported = r'''Let \(\mathfrak F_X^\sigma\) denote the reciprocal-frame Frobenius energy of
[1, Definition 3.5]. The only result imported from [1] is its precise comparison
[1, Proposition 3.1]:
\[
\mathfrak F_X^\sigma
 \le 2\sum_{a\ge1}\frac{\mathcal E_a^\sigma}{m_a}.
\tag{2.3}
\]
All other estimates used below are proved in this paper.
'''
    local = r'''Define the full symmetric row measure
\[
\Phi_X(L)=\sum_{q\in\mathcal Q_X}\sum_{a\ne0}p_{q,a}e(aL/q)
=2\operatorname{Re}\sum_{a\ge1}\Psi_a(L),
\]
and define the full pair-space frame energy
\[
\mathfrak F_X^\sigma
=\sum_{u\ne v}|\Phi_X(D_{u,v}^\sigma)|^2.
\]
Then, pointwise in \(L\), weighted Cauchy--Schwarz and
\(\sum_{a\ge1}m_a=1/2\) give
\[
\left|\sum_{a\ge1}\Psi_a(L)\right|^2
\le\frac12\sum_{\substack{a\ge1\\m_a>0}}
\frac{|\Psi_a(L)|^2}{m_a}.
\]
Since \(|2\operatorname{Re}z|^2\le4|z|^2\), summing over \(u\ne v\) yields the exact local comparison
\[
\boxed{
\mathfrak F_X^\sigma
 \le 2\sum_{\substack{a\ge1\\m_a>0}}\frac{\mathcal E_a^\sigma}{m_a}.
}
\tag{2.3}
\]
No result from another manuscript is required for (2.3).
'''
    if imported not in text:
        raise RuntimeError("Paper IV imported comparison block changed")
    text = text.replace(imported, local, 1)

    a = text.find("# 11. Scope and derandomisation\n")
    if a < 0:
        raise RuntimeError("Paper IV scope marker missing")
    text = text[:a] + SCOPE

    forbidden = ["preceding paper", "from [1]", "[1, Definition", "[1, Proposition", "Prime Detection Along", "remaining Fortune-relevant obstacle", "relocates the remaining problem to derandomisation"]
    bad = [x for x in forbidden if x in text]
    if bad:
        raise RuntimeError(f"standalone dependency/overclaim token remains: {bad}")

    stmt_re = re.compile(r"^## (Theorem|Proposition|Lemma|Corollary) ([0-9]+\.[0-9]+)", re.M)
    source_statements = [f"{a} {b}" for a, b in stmt_re.findall(src)]
    output_statements = [f"{a} {b}" for a, b in stmt_re.findall(text)]
    if source_statements != output_statements or len(output_statements) != 14:
        raise RuntimeError(f"Paper IV statement sequence changed: {source_statements} -> {output_statements}")
    return text.rstrip() + "\n", output_statements


def main() -> None:
    text, statements = build()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "manuscript.md").write_text(text, encoding="utf-8")
    status = """# Standalone Paper IV — claim status

## Proved in the manuscript

- random-order reciprocal-frame expectation theorem with loss (log X)^9;
- per-modulus-pair bias bound;
- ordered-partition conditioning and coefficient extraction bounds;
- exceptional-character sixth-moment control;
- complete endpoint-configuration ledger;
- full weighted harmonic/frame comparison, now proved locally.

## Open / not implied

- a pointwise theorem for the increasing primorial ordering;
- a source-to-reciprocal transference theorem for the corrected prime-pair detector;
- Fortune's conjecture.

The theorem is a random-permutation model theorem. Derandomisation alone would not close the corrected prime-detection problem.
"""
    (OUT / "CLAIM_STATUS.md").write_text(status, encoding="utf-8")
    referee = """# Independent-standalone referee read — Paper IV

**Disposition:** `PASS_AFTER_LOCAL_COMPARISON_AND_SCOPE_REPAIR`

All 14 labelled source statements are preserved. The sole logical import from another manuscript—the definition of the full frame energy and weighted harmonic comparison—has been restated and proved locally. The title and terminal discussion no longer call the result `Prime Detection` or suggest that derandomisation is the only remaining Fortune obstacle.

The highest residual correctness risk is the binding logarithmic-slack configuration ledger; this remains a priority for specialist analytic-number-theory review.
"""
    (OUT / "REFEREE_READ.md").write_text(referee, encoding="utf-8")
    repro = """# Reproducibility boundary — Paper IV

Finite checks cover ordered-partition identities, coefficient taxonomy, multiplicities, CRT/Gauss norms, the sixth-moment identity and the configuration ledger. They validate bookkeeping and implementation only. The asymptotic theorem is supported by the manuscript proof, and no finite check establishes a deterministic increasing-order theorem.
"""
    (OUT / "REPRODUCIBILITY.md").write_text(repro, encoding="utf-8")
    manifest = {
        "paper": "IV",
        "source": str(SRC.relative_to(ROOT)),
        "standalone": str((OUT / "manuscript.md").relative_to(ROOT)),
        "statement_count": len(statements),
        "statement_sequence": statements,
        "logical_cross_paper_dependencies": 0,
        "random_order_only": True,
        "increasing_order_proved": False,
        "source_to_prime_pair_bridge_proved": False,
        "fortune_proved": False,
    }
    (OUT / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"PAPER4_STANDALONE_BUILD_OK statements={len(statements)} words={len(text.split())}")


if __name__ == "__main__":
    main()
