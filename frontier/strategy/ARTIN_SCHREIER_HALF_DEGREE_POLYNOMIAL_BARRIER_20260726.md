# Artin--Schreier half-degree polynomial barrier

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** polynomial/Tschirnhaus constructive route for function-field Fortune `d=1`.  
**Status:** the half-degree obstruction below is **PROVED**. The crown remains **OPEN**.

## 1. Statement

Let

\[
M_p(Z)=Z^p-Z-1
\]

and

\[
g(Y)=-aY^3-cY-d,
\qquad a\ne0.
\]

A polynomial fibre semiconjugacy is a nonconstant polynomial

\[
R(Z)\in\mathbf F_p[Z]
\]

such that

\[
R(Z+1)=g(R(Z))\pmod {M_p(Z)}.
\]

### Theorem 1.1

For every prime

\[
p\equiv5\pmod6,
\qquad p\ge17,
\]

any polynomial fibre semiconjugacy to a genuine cubic map satisfies

\[
\boxed{
\deg R\ge\frac{p-1}{2}.
}
\]

At `p=11`, every degree at most five is also impossible, so

\[
\boxed{\deg R\ge6.}
\]

This improves the earlier rational-function barrier `deg R>=p/4` by almost a factor of two inside the polynomial/Tschirnhaus class.

## 2. Degree parameters

Write

\[
p=6k+5
\]

and put

\[
m=\frac{p+1}{3}=2k+2.
\]

Degrees below `m` are already impossible: if `n=deg R<m`, then

\[
3n<p,
\]

so the cleared semiconjugacy numerator has degree below `p`; divisibility by `M_p` forces a forbidden global identity.

It remains to exclude

\[
n=m+s-1,
\qquad1\le s\le k.
\]

These are exactly the degrees

\[
m\le n<\frac{p-1}{2}=3k+2.
\]

Put

\[
q=3n-p=3s-2.
\]

The inequalities needed below are

\[
q<n,
\qquad
q+1<n-1,
\qquad
2n<p.
\]

They follow immediately from `1<=s<=k` and `m=2k+2`.

## 3. The high-coefficient gap

Define

\[
N(Z)=R(Z+1)+aR(Z)^3+cR(Z)+d.
\]

The semiconjugacy says

\[
N(Z)=Q(Z)M_p(Z)
\]

for a polynomial `Q` of degree exactly `q`.

Write

\[
R(Z)=rZ^nS(Z^{-1}),
\qquad
S(T)=1+s_1T+\cdots+s_nT^n,
\qquad r\ne0.
\]

The high-degree terms of `QM_p` are `Z^pQ(Z)`. The terms `R(Z+1)`, `cR(Z)` and `d` have degree at most `n`. Therefore the cubic term forces a polynomial `P(T)` of degree exactly `q`, with `P(0)=1`, such that

\[
\boxed{
S(T)^3\equiv P(T)\pmod {T^{2n}}.
}
\]

This is the complete high-coefficient gap condition.

## 4. Differential classification of the gap

Differentiate the congruence:

\[
3S^2S'\equiv P'\pmod {T^{2n-1}}.
\]

Using `S^3 congruent P`, one obtains

\[
3PS'-P'S\equiv0\pmod {T^{2n-1}}.
\]

But

\[
\deg(3PS'-P'S)\le q+n-1<2n-1,
\]

because `q<n`. Hence this is an exact polynomial identity:

\[
3PS'-P'S=0.
\]

Equivalently,

\[
\left(\frac{S^3}{P}\right)'=0.
\]

The kernel of the derivation on `F_p(T)` is `F_p(T^p)`, so

\[
\frac{S^3}{P}=H(T)^p
\]

for a rational function `H`.

At infinity,

\[
\operatorname{ord}_\infty(S^3/P)=-(3n-q)=-p,
\]

so the numerator degree of `H` exceeds its denominator degree by one.

Write `H=A/B` in lowest terms. If an irreducible factor divided `B`, then in

\[
S^3B^p=PA^p
\]

its valuation on the left would be at least `p`, forcing its valuation in `P` to be at least `p`. This is impossible because

\[
\deg P=q<p.
\]

Thus `B` is constant and `H` is a linear polynomial. Since `S(0)=P(0)=1`, normalize

\[
H(T)=1+\gamma T.
\]

Therefore

\[
S^3=P(1+\gamma T)^p.
\]

Unique factorization and `p congruent 2 mod 3` now force

\[
\boxed{
P(T)=A_0(T)^3(1+\gamma T),
}
\]

\[
\boxed{
S(T)=A_0(T)(1+\gamma T)^m,
}
\]

where

\[
\deg A_0=s-1
\]

and `3m=p+1`.

### Theorem 4.1 — long-gap classification

Every polynomial semiconjugacy of degree below `(p-1)/2` would have to be of the form

\[
\boxed{
R(Z)=r(Z+\gamma)^mC(Z),
\qquad
\deg C=s-1.
}
\]

The first-resonance translated pure power is the special case `s=1`.

## 5. Translation contradiction

Translation by an element of `F_p` preserves `M_p`. Shift `Z` to remove `gamma`. We may assume

\[
R(Z)=rZ^mC(Z),
\qquad
\deg C=s-1.
\]

Because `3m=p+1`, reduction modulo `M_p` gives

\[
R(Z)^3
=r^3Z^{p+1}C(Z)^3
\equiv
r^3(Z^2+Z)C(Z)^3.
\]

The reduced cubic term has degree at most

\[
2+3(s-1)=3s-1=q+1.
\]

By construction,

\[
q+1<n-1.
\]

Hence the coefficients of `Z^n` and `Z^(n-1)` in the reduced semiconjugacy equation come only from

\[
R(Z+1)+cR(Z).
\]

The leading coefficient gives

\[
c=-1.
\]

After this substitution, the coefficient of `Z^(n-1)` in

\[
R(Z+1)-R(Z)
\]

is

\[
r n.
\]

It is nonzero because `r!=0` and `0<n<p`. This contradiction proves Theorem 1.1 for every `p>=17`.

## 6. The remaining endpoint at p=11

For `p=11`, degrees at most four were already excluded by the first-resonance theorem. The only additional degree below half scale is `n=5`.

The same differential classification gives, after translation,

\[
R(Z)=rZ^4(Z+\delta).
\]

Put

\[
u=ar^2\ne0.
\]

After reducing `Z^12` to `Z^2+Z`, the coefficients of degrees five through one give, successively,

\[
c=-1-u,
\]

\[
u(2\delta+1)+5=0,
\]

\[
3u\delta^2+2\delta+5=0,
\]

\[
3u\delta+2\delta+5=0.
\]

Subtracting the second linear relation from the first yields

\[
\delta(u+2)=u.
\]

The case `u=-2` is immediately impossible. Otherwise substitution gives

\[
3u^2+7u+10=0.
\]

Its discriminant is

\[
7^2-4\cdot3\cdot10
\equiv6\pmod {11},
\]

and `6` is a quadratic nonsquare modulo `11`. Thus no degree-five solution exists.

## 7. Strategic consequence

The polynomial constructive route is now genuinely dense:

- no fixed-degree polynomial template survives;
- no polynomial of degree below half the extension degree survives;
- the first open polynomial degree is `(p-1)/2` for `p>=17`;
- the general rational route still starts at degree `p/4`, but must use a genuine denominator.

A successful constructive proof must therefore use at least one of:

1. a polynomial transform of half-degree or more;
2. a dense rational transform with denominator;
3. a multivariate or non-Artin--Schreier construction;
4. a new dynatomic factor theorem that constructs the orbit without an explicit low-degree semiconjugacy.

This does not disprove the constructive route. It proves that its remaining form has complexity of the same linear scale as the ambient degree and cannot be a hidden bounded-template shortcut.

## 8. Verification

`artin_schreier_half_degree_polynomial_barrier_verify.py` is a symbolic structural regression. It performs no irreducibility census. For every admitted prime below `200`, it checks:

- all load-bearing inequalities `q<n`, `q+1<n-1`, `2n<p`;
- the classified identity
  
  `S=A_0(1+gamma*T)^m`, `S^3=A_0^3(1+gamma*T) mod T^(2n)`;
- nonvanishing of the final translation coefficient `n`;
- the separate `p=11` nonsquare discriminant.

Frozen output:

`artin_schreier_half_degree_polynomial_barrier_results_20260726.json`.
