# Programme status after the global Cartier-mass obstruction

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** function-field Fortune `d=1`  
**Crown:** **OPEN**  
**Current stopping condition:** **THEOREM-LEVEL OBSTRUCTION TO THE PROPOSED NEXT ROUTE**.

## 1. Result of the autonomous mass-invariant push

The proposed next route was:

1. sum the depressed-cubic Cartier cofactor over all `a,c,d`;
2. obtain a global mod-`p` mass invariant for `N_++N_-`;
3. if that first digit vanished, lift the same invariant to `p^2`;
4. combine it with the quadratic invariant to exclude simultaneous vanishing.

The audit found that Step 1 had already been executed in the earlier Cartier programme. The exact two-mode result is `DETERMINANT_TWO_CLASS_REDUCTION.md`: all multiplicative averaging in `a` recovers only

\[
N_++N_-
\qquad\text{and}\qquad
N_+-N_-.
\]

The present push independently rederived that reduction and tested the proposed `p^2` continuation.

## 2. Exact obstruction

For

\[
C_3(F_{a,c,d})=3a1_{irr},
\]

the complete weighted masses have only the trivial and quadratic modes:

\[
\sum_{a,c,d}a^{-1}C_3
=-\frac32(N_++N_-),
\]

\[
\sum_{a,c,d}\chi(a)a^{-1}C_3
=-\frac32(N_+-N_-).
\]

No third invariant is created by averaging over `a`.

The trivial mode is not uniformly nonzero. At `p=5` and `p=19`,

\[
N_++N_-=2p,
\]

so the aggregate mass vanishes modulo `p` despite positive cubic counts.

The obvious coefficientwise lift of the same cofactor formula to `Z/p^2` also fails:

- reducible fibres acquire nonzero lifted cofactors;
- the value depends on the arbitrary integer lift `a` versus `a+p`;
- the complete lifted mass is not the lifted irreducible count.

This is verified exhaustively at `p=5,7`.

## 3. Canonical higher Hasse--Witt distinction

The naive-lift obstruction must not be confused with the already-proved canonical higher Hasse--Witt indicator.

The earlier programme constructed

\[
K_a(c,d)
=
\frac1p\det\bigl(\Beta_p(F)-\Beta_{p^2}(F)\bigr)
\pmod p
\]

and proved

\[
K_a(c,d)=1_{F_{a,c,d}\text{ irreducible}}
\]

for every `d!=0`, including singular completion.

That construction contains the first Witt correction and is canonical. However, after summation it gives exactly

\[
N_a\pmod p,
\]

which is the same fixed-class residue supplied by the ordinary Cartier cofactor. It does not evaluate the next digit of `N_a`.

A genuine second-digit invariant would require one further level of Frobenius precision—schematically `Beta_(p^3)` and a determinant calculation modulo `p^3`—together with a complete aggregate evaluation. No existing Dwork-crystal theorem supplies the required nonvanishing after summing over the coefficient plane.

## 4. Routes now closed or exhausted

Do not continue with:

1. another multiplicative average in the cubic coefficient `a`;
2. asserting universal nonvanishing of the class-sum mass;
3. reading the ordinary Cartier cofactor coefficientwise modulo `p^2`;
4. treating the canonical `Beta_p-Beta_(p^2)` indicator as a new independent count invariant;
5. extending the existing finite residue scan without a structural formula;
6. a fixed low-height q-line cell;
7. another low-degree Artin--Schreier/Tschirnhaus construction;
8. the aggregate unsigned-Betti or direct `p`-cycle fixed-point routes.

Each item has either an exact counterexample, a circularity theorem, or a previously committed no-go result.

## 5. Remaining active theorem fronts

### A. Fixed-class Cartier transfer theorem

The shortest direct algebraic target remains

\[
\boxed{(\alpha_p,\beta_p)\ne(0,0),}
\]

where

\[
3aN_a=\alpha_pa+\beta_pa^{(p+1)/2}.
\]

Equivalently, prove that the square and nonsquare counts are not both divisible by `p`.

The existing exact architecture reduces this to a corrected cofactor-row/boundary-Witt pairing. A genuine advance requires a new constant-term, Cauchy--Binet, transfer-matrix or matrix-tree theorem that evaluates the **complete corrected sum** without expanding exponentially many minors. Parameter averaging alone cannot provide it.

### B. Invariant q-line nonsaturation

Exclude the exact failure value

\[
S_0=p\bigl(2(p-2)+B_++B_-\bigr)
\]

when the quadratic count vanishes. This requires a Frobenius-compatible parity reversal or a strict phase-nonsaturation theorem for the middle-hook q-line complex. Existing local and endpoint calculations do not control that middle block.

### C. Constructive cubic dynamics

Produce a cubic map with the required Frobenius rotation-one `p`-cycle. Affine, bounded-degree rational, low-degree Tschirnhaus and natural fixed-cell constructions are closed. A viable construction must be genuinely fibre-specific and have complexity growing with `p`, or arise from a new dynatomic factor theorem.

### D. Higher-digit canonical Cartier theorem

Construct and evaluate a canonical pointwise indicator modulo `p^2`, not merely a matrix formula. This requires higher Dwork precision and an aggregate theorem strong enough to distinguish zero from positive multiples of `p`. At present this is at least as difficult as Front A.

## 6. Priority ruling

The fixed-class Cartier residue remains the highest-information algebraic object, but there is no remaining routine calculation on it. The exact next theorem would be:

> **Corrected Cartier transfer theorem.** Express the complete square-class pair `(alpha_p,beta_p)` as a finite constant term or transfer determinant whose non-simultaneous vanishing is manifest.

If no such transfer representation is found, the next distinct route is the invariant q-line nonsaturation theorem. The constructive route is third because every bounded-complexity ansatz has already been eliminated.

## 7. Decisive stopping point

The autonomous run has reached a genuine stopping point:

- the recommended global-mass simplification was already known to collapse to two modes;
- its universal first-digit nonvanishing claim is false;
- its naive higher-digit continuation is noncanonical and false;
- the correct canonical Witt construction reproduces the existing fixed-class residue rather than evaluating it;
- no currently available literature theorem evaluates the corrected aggregate or forces its nonvanishing.

Further progress requires one of the four new theorems in Section 5. Another census, symbolic determinant expansion, parameter average or projector rewrite would not advance the crown.

## 8. New files

- `frontier/strategy/global_cartier_mass_p2_verify.py`
- `frontier/strategy/global_cartier_mass_p2_results_20260726.json`
- `frontier/strategy/GLOBAL_CARTIER_MASS_AND_P2_LIFT_OBSTRUCTION_20260726.md`
- `frontier/strategy/GLOBAL_CARTIER_MASS_P2_HOSTILE_AUDIT_20260726.md`
