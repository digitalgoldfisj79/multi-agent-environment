# The first dense Artin--Schreier endpoint and the wild Pade wall

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** first surviving polynomial/Tschirnhaus degree for function-field Fortune `d=1`.  
**Status:** the general reduction and Wronskian theorem are **PROVED**. Nonexistence at `p=11,17` is an **EXACT COMPUTER-ASSISTED FINITE THEOREM**. Uniform endpoint nonexistence remains **OPEN**.

## 1. First surviving degree

The trace-resonance theorem and the previous half-degree barrier leave

\[
n=\frac{p+1}{2}
\]

as the first possible degree of a polynomial Artin--Schreier construction for every admitted prime `p>=11`.

Let

\[
R(Z+1)=-aR(Z)^3-cR(Z)-d\pmod{Z^p-Z-1},
\qquad a\ne0,
\]

with `deg R=n`.

Scale the output so that `R` is monic. Translation `Z -> Z+t` preserves `Z^p-Z-1` and uniquely removes the coefficient of `Z^(n-1)`.

The sparse target minimal polynomial has

\[
\operatorname{Tr}(R(\alpha)^2)=0.
\]

Since `2n=p+1`, the Artin--Schreier trace filtration shows that this trace is minus the coefficient of `Z^(p-1)` in `R^2`. With the `Z^(n-1)` coefficient already zero, that coefficient is twice the `Z^(n-2)` coefficient of `R`. Hence the latter also vanishes.

Write

\[
R(Z)=Z^nS(Z^{-1}),
\]

where

\[
S(T)=1+s_3T^3+s_4T^4+\cdots+s_nT^n.
\]

## 2. Exact cubic-gap ledger

Put

\[
C(T)=S(T)^3.
\]

The semiconjugacy numerator has degree `3n`. On division by

\[
M_p(Z)=Z^p-Z-1,
\]

the quotient has degree

\[
3n-p=n+1.
\]

The lower term `(Z+1)Q(Z)` therefore has degree at most `n+2`. Between degrees `n+3` and `p-1=2n-2`, only the cubic term can contribute. Comparing the two boundary degrees as well gives:

### Theorem 2.1 — endpoint cubic gap

Every degree-`(p+1)/2` polynomial construction satisfies

\[
\boxed{
[T^j]S^3=0
\qquad(n+2\le j\le2n-3),
}
\]

and

\[
\boxed{
[T^{2n-2}]S^3=[T^{2n-1}]S^3=-1.
}
\]

Let `P` be the truncation of `S^3` through degree `n+1`. Then

\[
S^3-P
\]

is divisible by `T^(p-1)`, with first two quotient coefficients `-1,-1`.

The number of unknown coefficients `s_3,...,s_n` equals the number of displayed equations. Thus the first dense endpoint is a zero-dimensional cubic-gap problem, not a positive-dimensional ansatz.

## 3. Sparse Wronskian theorem

Define

\[
W(T)=3P(T)S'(T)-P'(T)S(T).
\]

Because `P` agrees with `S^3` through degree `p-2`, the Wronskian is divisible by `T^(p-2)`. Its naive maximum degree is `p+1`, but the leading coefficient is

\[
(3n-(n+1))[T^{n+1}]P[T^n]S
=p[T^{n+1}]P[T^n]S=0.
\]

The coefficient of `T^(p-1)` vanishes because `s_1=s_2=0`, and the coefficient of `T^(p-2)` is one. Therefore:

### Theorem 3.1 — wild Pade Wronskian

There is a scalar `mu in F_p` such that

\[
\boxed{
3PS'-P'S=T^{p-2}(1+\mu T^2).
}
\]

Equivalently, the rational function

\[
\Phi(T)=\frac{S(T)^3}{P(T)}
\]

has

\[
\Phi(T)=1-T^{p-1}-T^p+O(T^{p+1})
\]

at zero and

\[
\Phi'(T)=
\frac{S(T)^2T^{p-2}(1+\mu T^2)}{P(T)^2}.
\]

Thus, apart from the cubic zero divisor, the wild point at infinity and the order-`p-1` point over `1`, there are at most two additional finite critical points. This is a wild almost-Belyi/Pade object with only a quadratic residual critical polynomial.

## 4. The next semiconjugacy coefficient

Write

\[
\lambda=ar^2
\]

before the leading coefficient `r` is scaled to one. The exact reciprocal division identity gives

\[
\frac{S^3}{P}
=1-T^{p-1}(1+T)
-\lambda^{-1}T^{p+1}
\frac{(1+T)^nS(T/(1+T))+cS+\delta T^n}{P}.
\]

Expanding this identity and using the degree bound on the Wronskian gives

\[
\lambda^{-1}=4s_3.
\]

In particular `s_3` is nonzero. One more coefficient comparison yields the following necessary condition:

### Theorem 4.1 — endpoint compatibility equation

Every degree-`(p+1)/2` polynomial semiconjugacy satisfies

\[
\boxed{8s_4+3s_3=0.}
\]

A convenient derivation is as follows. If

\[
B=[T^{p+2}]S^3,
\qquad
C=[T^{p+3}]S^3,
\]

then the vanishing of the Wronskian coefficients above degree `p` gives

\[
B=-5s_3,
\]

\[
3C+9s_3+13s_4=0.
\]

The reciprocal semiconjugacy coefficient at the next degree says

\[
C+3s_3+3s_4
=-\lambda^{-1}\binom n2.
\]

Since `lambda^(-1)=4s_3`, `n=1/2` in `F_p`, and

\[
\binom n2=-\frac18,
\]

the displayed compatibility equation follows.

## 5. Exact first-prime elimination

The endpoint verifier exhausts the cubic-gap system, not the original irreducible-polynomial family.

At `p=11`, the cubic gap has exactly two solutions:

\[
(s_3,s_4,s_5,s_6)=(4,10,4,2),
\]

\[
(s_3,s_4,s_5,s_6)=(7,2,6,4).
\]

For both,

\[
8s_4+3s_3=4\ne0.
\]

At `p=17`, the cubic gap again has exactly two solutions:

\[
(1,10,5,8,13,7,9),
\]

\[
(16,9,0,7,14,9,1).
\]

Their compatibility residuals are respectively

\[
15\ne0,
\qquad
1\ne0.
\]

Therefore:

### Theorem 5.1 — finite endpoint no-go

There is no polynomial Artin--Schreier semiconjugacy of degree

\[
\frac{p+1}{2}
\]

at `p=11` or `p=17`.

This is an exact finite theorem and is not used as evidence for a uniform statement.

## 6. Exact remaining theorem

The first dense polynomial route has now been reduced to the following uniform assertion:

> **Wild Pade incompatibility theorem.** For every admitted prime `p>=23`, no polynomial
> \[
> S=1+s_3T^3+\cdots+s_nT^n,
> \qquad n=(p+1)/2,
> \]
> simultaneously satisfies the endpoint cubic-gap equations and
> \[
> 8s_4+3s_3=0.
> \]

Equivalently, classify the wild almost-Belyi pairs `(S,P)` with

\[
3PS'-P'S=T^{p-2}(1+\mu T^2)
\]

and exclude the semiconjugacy local coefficient.

No theorem located in the Belyi, lacunary-power, modular-invariant or prescribed-coefficient literature performs this characteristic-`p`, degree-growing classification. General Belyi existence results do not classify this wild ramification type, and generic lacunary-power algorithms do not prove the required uniform incompatibility.

This is a genuinely new capstone theorem, not a remaining computation. Extending finite Groebner or exhaustive calculations would certify more primes but would not settle the uniform endpoint.

## 7. Verification

Run

```bash
python frontier/strategy/artin_schreier_first_dense_endpoint_verify.py
```

The frozen output is

`frontier/strategy/artin_schreier_first_dense_endpoint_results_20260726.json`.
