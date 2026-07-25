# Affine-normalizer character no-go for a second trace collapse

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic `d=1` Airy wall.  
**Status:** **PROVED**.

## 1. Existing two-block decomposition

Let

\[
N_p=C_p\rtimes\mathbf F_p^*
=\operatorname{AGL}_1(\mathbf F_p)
\]

be the affine normalizer of the coordinate `p`-cycle. The primitive cohomology of the split `(2,3)` complete intersection has the Frobenius-stable decomposition

\[
H_p
\cong
M_{0,p}\oplus(\rho_p\otimes M_{1,p}),
\]

where

\[
\dim M_{0,p}=\dim M_{1,p}
=rac{2^{p-1}-1}{3p},
\]

and `rho_p` is the unique irreducible representation of `N_p` of dimension `p-1`, induced from a nontrivial character of `C_p`.

The hard virtual module is

\[
\mathcal D_p=M_{0,p}-M_{1,p}.
\]

## 2. Character of the affine representation

### Theorem 2.1

For `g in N_p`,

\[
\boxed{
\chi_{\rho_p}(g)
=
\begin{cases}
p-1,&g=1,\\
-1,&g\in C_p\setminus\{1\},\\
0,&g\notin C_p.
\end{cases}}
\]

### Proof

Realize `rho_p` on the nontrivial additive characters of `F_p`. A translation by `b` acts diagonally with eigenvalues

\[
\psi(cb),
\qquad c\in\mathbf F_p^*.
\]

For `b!=0`, their sum is `-1`; at `b=0`, it is `p-1`.

An affine element with nontrivial multiplier permutes the nontrivial additive characters without a fixed character, so its trace is zero.

Equivalently, this is the standard induced-character formula for

\[
\rho_p=\operatorname{Ind}_{C_p}^{N_p}\xi.
\]

## 3. Frobenius traces of normalizer correspondences

Geometric Frobenius commutes with `N_p`. Therefore

\[
\operatorname{Tr}(gF^r|H_p)
=
\operatorname{Tr}(gF^r|M_{0,p})
+
\chi_{\rho_p}(g)
\operatorname{Tr}(F^r|M_{1,p}).
\]

Consequently:

### Identity

\[
\operatorname{Tr}(F^r|H_p)
=
\operatorname{Tr}(F^r|M_{0,p})
+(p-1)\operatorname{Tr}(F^r|M_{1,p}).
\]

### Nontrivial translation

For every `sigma^a!=1`,

\[
\boxed{
\operatorname{Tr}(\sigma^aF^r|H_p)
=
\operatorname{Tr}(F^r|M_{0,p})
-
\operatorname{Tr}(F^r|M_{1,p})
=
\operatorname{Tr}(F^r|\mathcal D_p).
}
\]

This is exactly the original twisted Airy trace.

### Affine element outside `C_p`

If the multiplier is nontrivial, then

\[
\boxed{
\operatorname{Tr}(gF^r|H_p)
=
\operatorname{Tr}(gF^r|M_{0,p}).
}
\]

Such a correspondence is completely blind to `M_(1,p)`.

## 4. No-go theorem

### Theorem 4.1

No linear combination of Frobenius traces of affine-normalizer elements outside `C_p` can determine or bound

\[
\operatorname{Tr}(F^r|\mathcal D_p)
\]

without an additional independent estimate for either:

1. the identity trace on the full exponentially large primitive cohomology; or
2. a nontrivial translation trace, which is the original hard quantity.

### Proof

Every outside-`C_p` character value of `rho_p` is zero. Hence every such trace factors through the `M_0` summand and is unchanged if the Frobenius action on `M_1` is varied arbitrarily while preserving purity.

The character functions capable of detecting the `rho_p` multiplicity are supported on `C_p`. Within `C_p`, the identity gives the total trace and every nonidentity element gives exactly the hard difference `M_0-M_1`. There is no third character value and hence no second exact collapse.

## 5. Interpretation

The affine normalizer remains useful for proving the exact two-block decomposition, but it does not supply an easier family of fixed-locus traces from which the Airy correlation can be reconstructed.

In particular, computing fixed schemes of dilations or general affine coordinate permutations cannot by itself solve the terminal estimate. Those correspondences only probe `M_0`.

## 6. Programme ruling

### Closed

A second exact trace collapse obtained solely by averaging or interpolating fixed-locus traces of affine-normalizer elements outside the translation subgroup.

### Still open

A genuinely Frobenius-dependent correlation between `M_0` and `M_1`, or an unrelated q-line certificate sufficient for the crown.

## 7. Verification

`affine_normalizer_character_no_go_verify.py` constructs the permutation model on nontrivial additive characters and verifies the complete character table for the calibrated primes.
