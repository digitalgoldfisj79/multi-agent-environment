# d=1 next-phase consolidated status

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-collapse-integration-20260723`  
**Scope:** function-field `d=1` Fortune sibling only.

## 1. Completed fixed-scheme calculation

**PROVED:** for the bare cyclic shift `sigma`,

\[
\operatorname{Fix}(\sigma,\mathbf P(W))
\cong\operatorname{Spec}k[t]/(t^{p-2}),
\]

and on the smooth `(2,3)` complete intersection,

\[
\operatorname{Fix}(\sigma,X_p)
\cong\operatorname{Spec}k[t]/(t^{p-4}).
\]

Thus the unique set-theoretic fixed point has linearly growing nilpotent thickness.

## 2. Critical correction to Route 2

The target trace is `Tr(sigma Frob_p)`, not `Tr(sigma)`. The fixed equations of `sigma Frob_p` reconstruct the original `F_{p^p}` trace locus, while `dFrob_p=0`. Therefore the proposed localization at the unique thickened `sigma`-fixed point does not address `T_p`.

**VERDICT:** bare-shift fixed-point localization is closed as a direct route to the target.

## 3. Exact p-adic boundary evidence

**VERIFIED COMPUTATIONALLY:** exact arithmetic at every calibrated nonzero case

\[
p=11,17,23,29,41,47,53
\]

gives

\[
\boxed{v_p(T_p)=\frac{p+4}{3}.}
\]

The exact values at `p=41,47,53` reproduce the previously committed decimal normalizations. The earlier `p=23` factorization contained a one-power typo and has been corrected.

This suggests a Dwork boundary theorem but does not improve the decisive archimedean factor of order `p`.

## 4. Mod-p Adams/Frobenius exact sequence

**PROVED:** for every rank-two bundle `E` in characteristic `p`,

\[
0\to F^*E\to\operatorname{Sym}^pE
\to\det(E)\otimes\operatorname{Sym}^{p-2}E\to0.
\]

The sequence is compatible with connections. Therefore the virtual Adams difference becomes an actual rank-two Frobenius pullback after reduction mod `p`.

This unifies the special `k=p` Dwork boundary, the local inertia collapse and the p-adic valuation pattern.

## 5. Characteristic-zero lift audit

Let `P_p` be the natural integral lift of the modular quotient map. In Haessig's Airy frame its exact connection defect is

\[
P_p\partial_p-\partial_{p-2}P_p
=-p\pi aJ_p+\frac{p(p-1)\pi a^2}{3}E_p.
\]

**PROVED:** the principal map `J_p` has full target-module rank `p-1`.

## 6. Cohomological defect audit

For `k=p-2`, Haessig's effective decomposition applies and gives primitive cohomology basis

\[
\{[a v^{p-2-2j}w^{2j}]:0\le j\le(p-3)/2\}.
\]

The principal lift defect maps the even source monomials directly onto this entire basis.

**PROVED:** its projection to target primitive Dwork cohomology has rank

\[
\frac{p-1}{2}.
\]

Hence the naive hope that the modular rank-two sequence lifts to a characteristic-zero bounded cone is false. The defect remains maximally nontrivial after the known target cohomological reduction.

## 7. Current theorem boundary

The absolute bound

\[
|T_p|\le C p^{(p-1)/2}
\]

remains **OPEN**.

The work has removed two candidate shortcuts:

1. localization at the unique bare-shift fixed point;
2. a routine characteristic-zero lift of the mod-p rank-two Adams sequence.

The smallest remaining theorem is still a genuinely Frobenius-dependent global correlation between the `p` and `p-2` Airy symmetric powers. Any Dwork proof must cancel a family of `(p-1)/2` explicit target classes, not merely a bounded error space.

The alternative valid route remains an exact Jacobi-sum/character-orbit decomposition for the `sigma Frob_p` trace on the cubic linear section.

## 8. Files added in this phase

- `COMPLETED_FIXED_SCHEME_AND_CORRESPONDENCE_CORRECTION.md`
- `fixed_scheme_verify.py`
- `p_adic_boundary_check.py`
- `p_adic_boundary_results.txt`
- `MOD_P_ADAMS_FROBENIUS_EXACT_SEQUENCE.md`
- `mod_p_adams_sequence_verify.py`
- `AIRY_BOUNDARY_NEAR_INTERTWINER.md`
- `airy_boundary_intertwiner_verify.py`
- `AIRY_DEFECT_COHOMOLOGY_AUDIT.md`

All claims are labelled as proved, computational, heuristic or open in the individual notes.
