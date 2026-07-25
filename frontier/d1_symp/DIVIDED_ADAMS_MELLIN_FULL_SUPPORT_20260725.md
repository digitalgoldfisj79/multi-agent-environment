# Divided-Adams Mellin transform: full-support theorem and no-go

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling, primes `p=5 mod 6`.  
**Status:** the Mellin factorisation is **PROVED**. Exact support computations close bounded character support and simple character-pairing as routes to the absolute Airy bound.

## 1. Local trace function and sign

Let

\[
t_u=-\sum_{x\in\mathbf F_p}\zeta_p^{x^3+ux}
\]

and let `D_p(X,p)` be the Dickson polynomial satisfying

\[
D_p(\alpha+\beta,\alpha\beta)=\alpha^p+\beta^p.
\]

The local rank-two Adams trace is

\[
f_p(u)=D_p(t_u,p).
\]

With this explicit local sign and the repository's positively normalized `T_p`,

\[
\boxed{
\sum_{u\in\mathbf F_p}f_p(u)=-pT_p.
}
\]

Since `f_p(0)=0`, the same sum may be taken over `F_p^*`. This corrects the stale opposite sign formerly displayed in this note; it agrees with `DIVIDED_ADAMS_HASSE_COEFFICIENT_20260725.md` and the exact cyclotomic verifier.

## 2. Exact multiplicative Mellin factorisation

Let `E=F_(p^p)` and

\[
\Psi(z)=\psi(\operatorname{Tr}_{E/\mathbf F_p}z).
\]

The extension-field Airy identity is

\[
f_p(u)=-\sum_{x\in E}\Psi(x^3+ux).
\]

Let `chi` be a nontrivial multiplicative character of `F_p^*`, and let `r` be the inverse of `3` modulo `p-1`. Then

\[
\boxed{
\mathcal M_p(\chi)
:=\sum_{u\in\mathbf F_p^*}\chi(u)f_p(u)
=-G(\chi)G(\chi^{-r})
\sum_{\substack{y\in E\\ \operatorname{Tr}(y)=1}}
\chi^r(\operatorname{Tr}(y^3)).
}
\]

### Proof

Interchanging the `u` and `x` sums gives

\[
\mathcal M_p(\chi)
=-\sum_{x\in E}\Psi(x^3)
\sum_{u\in\mathbf F_p^*}\chi(u)\psi(u\operatorname{Tr}x).
\]

The inner sum is zero when `Tr(x)=0`; otherwise it equals

\[
G(\chi)\chi^{-1}(\operatorname{Tr}x).
\]

Write `x=t y`, where `t=Tr(x) in F_p^*` and `Tr(y)=1`. This gives

\[
-G(\chi)
\sum_{\operatorname{Tr}y=1}
\sum_{t\in\mathbf F_p^*}
\chi^{-1}(t)\psi(t^3\operatorname{Tr}(y^3)).
\]

Cubing is a bijection of `F_p^*` because `p=2 mod 3`. Substituting `s=t^3` yields the second Gauss sum and the displayed formula.

For the trivial character,

\[
\boxed{\mathcal M_p(1)=-pT_p.}
\]

## 3. Geometric interpretation

The residual character sum lives on the affine hyperplane

\[
\operatorname{Tr}(y)=1
\]

with Kummer phase `chi^r(Tr(y^3))`. After splitting `E/F_p` geometrically, this is the cubic linear section

\[
\sum_i y_i=1,
\qquad
\sum_i y_i^3.
\]

Its projective leading form at infinity is the previously isolated trace-zero cubic linear section. The Mellin transform therefore returns to the same high-dimensional cubic geometry; it does not produce a bounded-conductor one-variable object.

This is consistent with the proved local Adams collapse: the virtual local inertia class has rank two and Swan conductor zero, but the global `SL_2` Adams class is

\[
[\operatorname{Sym}^p]-[\operatorname{Sym}^{p-2}],
\]

which is not the class of an honest bounded-rank semisimple representation.

## 4. Exact support test

Script: `divided_adams_mellin_probe.py`.

Order `F_p^*` as `g^j`. The local values are represented exactly in `Z[zeta_p]`. For character exponent `k`, put

\[
d=(p-1)/\gcd(k,p-1).
\]

The transform vanishes exactly when each cyclotomic coordinate polynomial

\[
C_s(X)=\sum_{j=0}^{p-2}f_p(g^j)_sX^j
\]

is divisible by the cyclotomic polynomial `Phi_d(X)`. This gives an exact zero test without numerical Fourier transforms.

The results are:

| `p` | nonzero Mellin modes | zero modes |
|---:|---:|---|
| 11 | `9/10` | quadratic character only |
| 17 | `16/16` | none |
| 23 | `22/22` | none |
| 29 | `28/28` | none |
| 41 | `40/40` | none |

There is no nontrivial translation period or antiperiod in any tested case. For `p=11,17,23,29`, the exact rational rank of the matrix of cyclotomic value coordinates is respectively

\[
5,8,11,14=(p-1)/2,
\]

so the values span the full real cyclotomic field dimension. The latter statement is now proved uniformly by `LOCAL_AIRY_ADAMS_CYCLOTOMIC_INITIAL_TERM_20260725.md`.

## 5. Ruling

### Closed

1. The local divided-Adams trace does not have uniformly bounded multiplicative Mellin support.
2. The support is generically full, not a bounded collection of cubic, quadratic or other low-order characters.
3. There is no exact period, antiperiod or uniform character-pair cancellation visible in the value function.
4. The exact Mellin transform does not reduce to a bounded-conductor curve; it is two Gauss factors times a Kummer sum on the original cubic linear section.
5. The local values and their square-class combination do not descend to a bounded-degree cyclotomic field.

The exceptional quadratic zero at `p=11` is not stable and cannot support a theorem.

### Still open

The absolute estimate

\[
|T_p|\le C p^{(p-1)/2}
\]

requires cancellation inside the full-support Kummer sum, square-root cancellation across the full real-cyclotomic orbit, or an equivalent characteristic-`p` correlation theorem. Mellin diagonalisation alone does not reduce the complexity.
