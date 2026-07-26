# Sparse quotient compactification and rational-point theorem audit

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Status:** the adjunction calculation and applicability ruling below are **PROVED**. They close the direct Fano/rationally-connected compactification shortcut. A specially constructed quotient compactification is not ruled out. The crown remains open.

## 1. Natural projective sparse surface

The previously proved smooth sparse surface is

\[
\mathcal Y_p=
\{s_2=s_3=\cdots=s_{p-4}=0\}
\subset\mathbf P^{p-3}.
\]

It is a smooth complete-intersection surface of multidegree

\[
(2,3,\ldots,p-4).
\]

The fixed nonzero cubic slices arise from affine/weighted slices of the cone over this surface before taking the cyclic root quotient. Thus `mathcal Y_p` is the first natural proper compactification candidate for the sparse quotient programme.

## 2. Canonical class

Adjunction for a complete intersection of degrees `d_1,...,d_r` in `P^N` gives

\[
K_{\mathcal Y_p}
=
\mathcal O_{\mathcal Y_p}
\left(\sum_i d_i-(N+1)\right).
\]

Here

\[
N=p-3
\]

and

\[
\sum_{m=2}^{p-4}m
=
\frac{(p-4)(p-3)}2-1.
\]

Therefore

\[
\boxed{
K_{\mathcal Y_p}
=
\mathcal O_{\mathcal Y_p}
\left(\frac{(p-7)(p-2)}2\right).}
\]

### Theorem 2.1 — canonical trichotomy

- `p=5`: `K=O(-3)` and the surface is the projective plane/Fano boundary case;
- `p=7`: `K=O` and the surface is in the trivial-canonical range;
- every `p>7`: `K` is ample and `mathcal Y_p` is of general type.

In particular every admitted prime `p>=11` lies in the ample-canonical range.

## 3. Failure of the direct Esnault/Fano shortcut

The standard finite-field rational-point theorems for smooth projective Fano or separably rationally connected varieties do not apply to `mathcal Y_p` at an admitted prime. The canonical bundle has the opposite sign.

Likewise, the standard Hodge-type/Witt congruence shortcut is not available directly upstairs: the ample canonical class supplies a nontrivial top Hodge piece rather than the required vanishing of positive-degree `O`-cohomology.

This does not state that no proper model has a rational point. It states that the most immediate compactification is outside the hypotheses of the available automatic point-existence theorems.

## 4. Quotient caveat

A wild cyclic quotient can alter singularities and canonical data. The theorem above therefore does **not** prove that every resolution or stack compactification of

\[
Y_a=X_a/C_p
\]

is of general type. Such a claim would require an explicit ramification and discrepancy calculation.

However, it prevents the following invalid inference:

\[
\text{smooth sparse complete intersection}
\Longrightarrow
\text{Fano/rationally connected}
\Longrightarrow
\text{rational point}.
\]

The first implication is false for every admitted `p>=11`.

## 5. Boundary obstruction

Even if a specially constructed proper quotient model satisfied a rational-point congruence, one would still need to prove that the guaranteed point does not lie entirely on the compactification boundary. The no-split-torsor theorem removes the affine `g=0` fibre, but it does not remove projective points at infinity or exceptional divisors of a resolution.

A valid compactification route must therefore provide both:

1. a point theorem for the proper quotient model;
2. an exact boundary analysis showing that at least one point lies in the affine `g!=0` locus.

Neither follows from adjunction alone.

## 6. Ruling

### Closed

The direct use of Fano, rational connectedness or the standard smooth-complete-intersection point theorem on the natural projective sparse surface is closed.

### Still logically possible

A quotient-specific compactification could remain useful if it proves:

- regularity or a controlled resolution;
- the required coniveau/Witt vanishing on the quotient rather than upstairs;
- a boundary point count strictly below the proper point count.

That would be a new theorem package, not a routine application of the existing sparse-surface smoothness result.

## 7. Verification

Run

```bash
python frontier/strategy/sparse_surface_canonical_class_verify.py
```

Frozen output:

`frontier/strategy/sparse_surface_canonical_class_results_20260726.json`.
