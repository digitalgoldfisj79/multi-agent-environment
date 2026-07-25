# Arithmetic Picard--Lefschetz correction and the exact Airy correlation wall

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic main branch for the `p=5 mod 6` function-field `d=1` half-theorem.  
**Status:** the external Picard--Lefschetz inputs are quoted from Chuang (2026); their specialization to `k=p` and `k=p-2` and the resulting obstruction are **PROVED CONSEQUENCES**. The absolute trace estimate remains **OPEN**.

## 0. Purpose

The analytic target is

\[
\left|
\operatorname{Tr}(F|U_p)
-p\operatorname{Tr}(F|U_{p-2})
\right|
\le C p^{(p+1)/2},
\]

where

\[
U_k=H_c^1(\mathbf A^1_{\overline{\mathbf F}_p},
\operatorname{Sym}^k\mathcal A)^{\mu_3}.
\]

The remaining question was whether the characteristic-boundary difference between `k=p` and `k=p-2` is merely an unaccounted local degeneration term. Chuang's arithmetic Picard--Lefschetz theorem now makes that local term explicit.

It is exactly one Tate line. Removing it does not correlate the two geometric modules.

## 1. Relevant external theorems

Chuang, *On the Generalized Arithmetic Picard--Lefschetz Formula* (arXiv:2607.05757, 2026), constructs the affine model `A'_k` for the `mu_3`-invariant Airy moment.

### Geometric model

Proposition 4.14 gives the specialization-compatible short exact sequence

\[
0\longrightarrow
\left(\operatorname{Sym}^k H_c^1
(\mathbf A^1,\mathcal L_\psi(x^3/3))\right)^{\mu_3}
\longrightarrow
H_c^{k-1}(A'_k)^{S_k\times\mu_2,\chi}(-1)
\longrightarrow
U_k
\longrightarrow0.
\]

### Arithmetic Picard--Lefschetz correction

For odd `k=2m+1`, Theorem 4.18 gives a split exact sequence of local Galois representations

\[
0\longrightarrow
H_c^{k-1}(A'_{k,\mathbf F_p})^{S_k\times\mu_2,\chi}
\longrightarrow
H_c^{k-1}(A'_{k,\mathbf Q_p})^{S_k\times\mu_2,\chi}
\longrightarrow
\bigoplus_{\substack{a\text{ odd}\\1\le a\le k/p}}
\mathbf Q_\ell(-m)
\longrightarrow0.
\]

The singularities are ordinary double points. The number of Tate lines is exactly the number of odd integers in `[1,k/p]`.

After the `(-1)` in the Airy geometric model, each such correction line is

\[
\mathbf Q_\ell(-m-1).
\]

## 2. Specialization to the characteristic boundary

Write

\[
p=6r+5.
\]

### `k=p`

Here

\[
k=2m+1,
\qquad
m=\frac{p-1}{2},
\]

and the indexing set contains exactly `a=1`. Therefore the invariant Airy model has one local correction line

\[
\boxed{
\mathbf Q_\ell\left(-\frac{p+1}{2}\right).
}
\]

The generic characteristic-zero invariant Airy rank is

\[
\left\lfloor\frac{p-1}{2}\right\rfloor
-
\left\lfloor\frac p3\right\rfloor
=r+1,
\]

whereas the characteristic-`p` space has rank

\[
\dim U_p=r=\frac{p-5}{6}.
\]

Thus the Picard--Lefschetz line accounts for the entire one-dimensional rank drop.

Denoting the generic realization by `U_p^gen` and the special realization by `U_p^sp=U_p`, the compatible split sequences give

\[
\boxed{
U_p^{\mathrm{gen}}
\cong
U_p^{\mathrm{sp}}
\oplus
\mathbf Q_\ell\left(-\frac{p+1}{2}\right).
}
\]

### `k=p-2`

Now `k<p`, so there is no integer `a` with

\[
1\le a\le k/p.
\]

The correction sum is empty. Hence

\[
\boxed{
U_{p-2}^{\mathrm{gen}}
\cong
U_{p-2}^{\mathrm{sp}}.
}
\]

Both special spaces have rank `r`; the generic spaces have ranks `r+1` and `r`.

## 3. Exact reformulation of the target

Geometric Frobenius acts on

\[
\mathbf Q_\ell\left(-\frac{p+1}{2}\right)
\]

by

\[
p^{(p+1)/2}.
\]

Therefore

\[
\boxed{
\operatorname{Tr}(F|U_p^{\mathrm{sp}})
-p\operatorname{Tr}(F|U_{p-2}^{\mathrm{sp}})
=
\operatorname{Tr}(F|U_p^{\mathrm{gen}})
-p\operatorname{Tr}(F|U_{p-2}^{\mathrm{gen}})
-p^{(p+1)/2}.
}
\]

The local correction is already exactly on the permitted absolute-constant scale. It costs one unit in the normalized inequality and no growing factor.

Consequently, the analytic theorem is equivalent, up to this explicit Tate term, to an absolute Frobenius correlation between the two **generic geometric** Airy moment motives.

There is no further unknown local Picard--Lefschetz correction in the invariant sector.

## 4. What Chuang's nontrivial-mu3 theorem does and does not say

Chuang's Theorems 4.21--4.24 concern the `A''` model for the nontrivial `mu_3` eigenspaces. They decompose that local Galois module into a geometric part and diagonal `A_2` vanishing cycles; for `p=2 mod 3`, the trace on the inertia-invariant vanishing-cycle part is zero.

That result is exact but is not the load-bearing theorem here: `U_p` and `U_{p-2}` are the **trivial** `mu_3` eigenspaces. Their relevant local correction is the single ordinary-double-point Tate line from `A'` described above.

Thus the zero-trace result for `A''` must not be used to claim that the invariant Airy correlation has been proved.

## 5. Precise theorem-level obstruction

The repository already proves that the common-weight characteristic-zero Hodge spectra of

\[
U_p^{\mathrm{gen}}
\quad\text{and}\quad
U_{p-2}^{\mathrm{gen}}(-1)
\]

are disjoint. Hence

\[
\operatorname{Hom}_{\mathrm{HS}}
\left(
U_p^{\mathrm{gen}},
U_{p-2}^{\mathrm{gen}}(-1)
\right)=0.
\]

Therefore no algebraic correspondence spread out from characteristic zero can pair the two motives and produce the required cancellation.

Other natural bounded-cone mechanisms are also already closed:

1. the add-two-variables correspondence leaves a residual invariant summand of rank `(p+1)/6`;
2. the canonical mod-`p` Adams near-intertwiner has full-rank defect `(p-5)/6` after the exact `mu_3` projection;
3. exact low-rank spectra show no uniform common Frobenius factor or matched-slope theorem;
4. the Gaussian-period remainder has maximal orbit degree in every calibrated sector.

Chuang's theorem removes the possibility that an omitted local correction explains this failure. The local correction is one explicit Tate line and is already harmless.

The remaining analytic statement is therefore a genuinely global theorem:

> Prove absolute cancellation between Frobenius traces of two equal-weight, linearly growing, Hodge-disjoint Airy motives at the exceptional coincidence `k=char=p`, after removing one explicit Tate eigenvalue.

This is a numerical Frobenius-correlation theorem. It cannot arise from a characteristic-zero motivic morphism, a missing local vanishing cycle, or a bounded-rank canonical connection defect.

## 6. Ruling

### PROVED / EXTERNAL THEOREM APPLIED

1. The invariant Airy moment at `k=p` has exactly one Picard--Lefschetz correction line
   \[
   \mathbf Q_\ell(-(p+1)/2).
   \]
2. The invariant Airy moment at `k=p-2` has no such correction.
3. The local term contributes exactly `p^((p+1)/2)` to the first trace.
4. After removing it, the original target is precisely a generic cross-motive Frobenius correlation.
5. The corresponding characteristic-zero motives admit no nonzero Hodge-compatible morphism.

### PRECISE THEOREM-LEVEL OBSTRUCTION

Any proof of the absolute Airy bound must establish a new characteristic-`p`, Frobenius-dependent correlation between Hodge-disjoint motives. Existing local Picard--Lefschetz theory completely determines the local correction but supplies no such correlation.

### OPEN

\[
\left|
\operatorname{Tr}(F|U_p)
-p\operatorname{Tr}(F|U_{p-2})
\right|
\le C p^{(p+1)/2}
\]

with absolute `C`, and therefore the crown.