# All coprime extensions: the three-cubic-twist bridge

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling, primes `p=5 mod 6`.  
**Status:** the geometric and Airy coefficient-twist identities below are **PROVED** for every extension degree `r` with `p` not dividing `r`. The remaining comparison with the original `mu_3`-projected Airy module in even degree is **OPEN**.

## 0. Purpose

`ODD_EXTENSION_AIRY_PRIMITIVE_BRIDGE_20260724.md` proved

\[
\operatorname{Tr}(F^r|\mathcal R_p)
=
\operatorname{Tr}(F^r|\mathcal D_p(-3))
\]

when `gcd(r,2p)=1`.

This note treats every degree with `p` not dividing `r`. In even degree the correct primitive trace is not one ordinary Airy trace. It is the average of the three cubic-coefficient twists over the three cube classes of the extension field.

## 1. Cube-class coefficient sums

Fix `r>=1` with `p` not dividing `r`, and put

\[
Q=p^r,
\qquad
k_r=\mathbf F_Q,
\qquad
L_r=\mathbf F_{Q^p}.
\]

Let

\[
d_r=\gcd(3,Q-1).
\]

Thus

\[
d_r=
\begin{cases}
1,&r\text{ odd},\\
3,&r\text{ even}.
\end{cases}
\]

Choose representatives

\[
C_r\subset k_r^*
\]

for the quotient

\[
k_r^*/(k_r^*)^3.
\]

For `c in C_r`, define

\[
T_{p,r}^{(c)}
=
\sum_{x\in L_r,\ \operatorname{Tr}_{L_r/k_r}(x)=0}
\psi_r\left(
\operatorname{Tr}_{L_r/k_r}(c x^3)
\right).
\]

The value depends only on the cube class of `c`: replacing `c` by `c s^3` and substituting `x -> s^{-1}x` preserves the trace-zero hyperplane.

## 2. Projective zero-fibre formula

Let

\[
W_r=(\ker\operatorname{Tr}_{L_r/k_r})/k_r
\]

and write

\[
Q_2(w)=\operatorname{Tr}(w^2),
\qquad
Q_3(w)=\operatorname{Tr}(w^3).
\]

Translation by `k_r` gives

\[
T_{p,r}^{(c)}
=
Q
\sum_{w\in W_r,\ Q_2(w)=0}
\psi_r(cQ_3(w)).
\]

Let

\[
M_0=\#\{w\in W_r:Q_2(w)=Q_3(w)=0\}.
\]

Additive orthogonality detects the cubic zero fibre:

\[
M_0
=
\frac1Q
\sum_{v\in k_r}
\sum_{w:Q_2(w)=0}
\psi_r(vQ_3(w)).
\]

The `v=0` term is the null-cone cardinality

\[
Q^{p-3}.
\]

For `v!=0`, the inner sum depends only on the cube class of `v`. Every cube class has `(Q-1)/d_r` members. Therefore

\[
M_0
=
Q^{p-4}
+
\frac{Q-1}{d_rQ^2}
\sum_{c\in C_r}T_{p,r}^{(c)}.
\]

Projectivizing gives

\[
M_0=1+(Q-1)\#X_p^{AS}(k_r),
\]

while

\[
Q^{p-4}=1+(Q-1)\#\mathbf P^{p-5}(k_r).
\]

Hence

\[
\boxed{
\#X_p^{AS}(k_r)
-
\#\mathbf P^{p-5}(k_r)
=
\frac1{d_rQ^2}
\sum_{c\in C_r}T_{p,r}^{(c)}.
}
\]

Because `p` does not divide `r`, the Artin--Schreier algebra remains the degree-`p` field and twisted descent gives

\[
\boxed{
\operatorname{Tr}(F^r|\mathcal D_p)
=
\frac1{d_rQ^2}
\sum_{c\in C_r}T_{p,r}^{(c)}.
}
\]

For odd `r`, `d_r=1` and this is the previous one-sum formula. For even `r`, it is the exact three-sum replacement.

## 3. Cubic-coefficient Airy modules

For each `c in k_r^*`, let `A_c` be the rank-two cubic Airy sheaf on the `u`-line over `k_r` with trace function

\[
u\longmapsto-
\sum_{x\in k_r}
\psi_r(c x^3+ux).
\]

Let

\[
H_{k,c}=H_c^1
(\mathbf A^1_{\overline{k}_r},\operatorname{Sym}^k A_c)
\]

and define the full common-weight virtual module

\[
\mathcal R_{p,c}
=H_{p,c}-H_{p-2,c}(-1).
\]

The local rank-two Adams identity and additive orthogonality give

\[
\boxed{
\operatorname{Tr}(F_Q|\mathcal R_{p,c})
=Q T_{p,r}^{(c)}.
}
\]

Combining with the projective formula yields

\[
\boxed{
Q^3\operatorname{Tr}(F^r|\mathcal D_p)
=
\frac1{d_r}
\sum_{c\in C_r}
\operatorname{Tr}(F_Q|\mathcal R_{p,c}).
}
\]

Equivalently, the Tate-shifted primitive multiplicity trace is the cube-class average of the full cubic-coefficient Airy traces.

## 4. Odd and even specializations

### Odd `r`

There is one cube class. The coefficient can be taken to be `c=1`, and the odd-power `mu_3` extraction theorem identifies the full Airy trace with the original invariant trace. Thus

\[
\operatorname{Tr}(F^r|\mathcal R_p)
=Q^3\operatorname{Tr}(F^r|\mathcal D_p).
\]

### Even `r`

The field `k_r` contains `mu_3`. Choose a primitive cube root `omega`. Then

\[
C_r=\{1,\omega,\omega^2\}
\]

after replacing `omega` by any representatives of the three cube classes. The exact primitive trace is

\[
\boxed{
Q^3\operatorname{Tr}(F^r|\mathcal D_p)
=
\frac13
\sum_{j=0}^2
\operatorname{Tr}(F_Q|\mathcal R_{p,\omega^j}).
}
\]

The remaining even-power discrepancy is therefore the explicit number

\[
\boxed{
\Delta_{p,r}
=
\operatorname{Tr}(F^r|\mathcal R_p)
-
\frac13
\sum_{j=0}^2
\operatorname{Tr}(F_Q|\mathcal R_{p,\omega^j}).
}
\]

Computing `Delta_{p,r}` is exactly the twisted `mu_3` Lefschetz/projector problem. No other part of the primitive comparison remains in degrees not divisible by `p`.

## 5. Why this is the arithmetic quadratic sector

For odd `r`, arithmetic Frobenius exchanges the two nontrivial `mu_3` characters and their traces vanish. For even `r`, it fixes those characters, so they contribute separately. The three coefficient twists are defined over the quadratic extension in which `mu_3` splits and are permuted by the base-field arithmetic Frobenius.

Thus `Delta_{p,r}` is not a generic failure of the Airy--primitive bridge. It is the exact quadratic/projector sector already present in the application ledger.

## 6. Exact `p=5`, `r=2` check

`three_twist_bridge_verify.py` works in

\[
\mathbf F_{25}=\mathbf F_5[t]/(t^2-2)
\]

and enumerates the split coordinate model directly.

It finds:

- the affine null cone has `625=25^2` points;
- the cubic zero fibre has `25` points;
- `#X_5(F_25)=1=#P^0(F_25)`, so the primitive second trace is zero;
- for three cube-class representatives, the null-cone additive sums are

\[
-50,\quad25,\quad25;
\]

and their average is zero;
- multiplying by `Q=25` gives the extension-field sums

\[
-1250,\quad625,\quad625,
\]

whose average again gives `Q^2 Tr(F^2|D_5)=0`.

At `p=5`, the `mu_3`-invariant Airy spaces have rank zero, so `Delta_{5,2}=0`. This is a complete direct check of the even bridge in the first case.

## 7. Remaining exact tasks

### Even sector

Compute the twisted projector term `Delta_{p,r}`, beginning with `r=2`, and identify it with the arithmetic quadratic/boundary factors already present in the hook ledger.

### `p`-divisible sector

When `p|r`, the Artin--Schreier algebra splits into `p` factors and the descent twist disappears. The three-twist formula above intentionally does not apply. That sector remains the split-algebra/hook comparison.
