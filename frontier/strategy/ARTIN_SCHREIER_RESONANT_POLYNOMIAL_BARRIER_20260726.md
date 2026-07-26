# Artin--Schreier resonant polynomial barrier

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** constructive cubic semiconjugacy route, primes `p congruent 5 mod 6`.  
**Status:** the polynomial degree barrier below is **PROVED**. The crown remains **OPEN**.

## 1. Setup

Let

\[
M_p(Z)=Z^p-Z-1
\]

and let

\[
g(Y)=-aY^3-cY-d,
\qquad a\ne0.
\]

A polynomial Artin--Schreier construction is a nonconstant

\[
R(Z)\in\mathbf F_p[Z]
\]

satisfying

\[
\boxed{
R(Z+1)=g(R(Z))\pmod {M_p(Z)}.
}
\]

For a root `zeta` of `M_p`, the element `beta=R(zeta)` then obeys

\[
\beta^p=g(\beta).
\]

If `beta` has degree `p`, this gives the desired irreducible sparse polynomial.

The earlier rational-function theorem proved only

\[
\deg R\ge p/4
\]

for a general quotient `A/B`, because clearing denominators has degree at most `4m`. For a polynomial, the cleared equation has degree `3m`, so the first unresolved resonance is substantially later.

## 2. Below the first resonance

Let

\[
p=3h+2.
\]

If `m=deg R<=h`, then

\[
3m\le p-2<p.
\]

The polynomial

\[
N(Z)=R(Z+1)+aR(Z)^3+cR(Z)+d
\]

has degree below `p`. Divisibility by `M_p` would force `N=0` identically. That would give a global rational semiconjugacy from translation to a cubic map, impossible because the induced map on the stable rational subfield must be Möbius.

Thus

\[
\deg R\ge h+1=\frac{p+1}{3}.
\]

The threshold `m=h+1` is the first case in which the cleared numerator may be a nonzero multiple of `M_p`.

## 3. Classification at the first resonance

Put

\[
m=h+1=\frac{p+1}{3},
\qquad 3m=p+1.
\]

Suppose a degree-`m` solution exists. Since `deg N=p+1`, there are `q_1,q_0 in F_p` such that

\[
N(Z)=(q_1Z+q_0)(Z^p-Z-1).
\]

Write

\[
R(Z)=rZ^mS(Z^{-1}),
\qquad
S(T)=1+s_1T+\cdots+s_mT^m,
\qquad r\ne0.
\]

The right side has no terms of degrees

\[
p-1,p-2,\ldots,3.
\]

For degrees above `m`, only the cubic term `aR^3` contributes. Therefore the coefficients of `R^3` in degrees

\[
m+1,\ldots,p-1=3m-2
\]

vanish. Equivalently,

\[
\boxed{
S(T)^3\equiv1+\gamma T\pmod {T^{2m}}
}
\]

for some `gamma in F_p`.

Now `3m=p+1`, so in characteristic `p`,

\[
\bigl((1+\gamma T)^m\bigr)^3
=(1+\gamma T)^{p+1}
\equiv1+\gamma T\pmod {T^{2m}},
\]

because the Frobenius term `T^p` has degree at least `2m`.

Cubing is an automorphism of the nilpotent group

\[
1+T\mathbf F_p[T]/(T^{2m})
\]

since `p!=3`. Hence the cube root is unique:

\[
S(T)\equiv(1+\gamma T)^m\pmod {T^{2m}}.
\]

Both sides have degree at most `m`, so this is equality. Thus:

### Theorem 3.1 — threshold classification

Every degree-`(p+1)/3` polynomial solution would have to be

\[
\boxed{
R(Z)=r(Z+\gamma)^m.
}
\]

## 4. Final contradiction

Translation by `gamma in F_p` preserves the Artin--Schreier polynomial:

\[
M_p(Z+\gamma)=M_p(Z).
\]

We may therefore replace `Z` by `Z-gamma` and assume

\[
R(Z)=rZ^m.
\]

In the quotient by `M_p`,

\[
Z^{3m}=Z^{p+1}=Z^2+Z.
\]

The semiconjugacy equation becomes the ordinary polynomial identity of degree below `p`

\[
r(Z+1)^m
+a r^3(Z^2+Z)
+c rZ^m+d=0.
\]

For `p>=11`, one has `m>=4`. The coefficient of `Z^(m-1)` is therefore contributed only by the first term and equals

\[
rm.
\]

It is nonzero because `r!=0` and `0<m<p`. This is a contradiction.

### Theorem 4.1 — resonant polynomial barrier

For every prime `p>=11` with `p congruent 5 mod 6`, a polynomial semiconjugacy to a genuine cubic map must satisfy

\[
\boxed{
\deg R\ge\frac{p+4}{3}.
}
\]

Equivalently, no polynomial transform of degree at most `(p+1)/3` can produce the required cubic-tail witness from the canonical Artin--Schreier extension.

## 5. Significance

This strictly improves the earlier general rational bound

\[
\deg R\ge p/4
\]

inside the polynomial/Tschirnhaus class. It also subsumes all fixed-degree polynomial ansatzes for sufficiently large `p` and explains the first characteristic-`p` resonance exactly:

- below `(p+1)/3`, divisibility forces a forbidden global identity;
- at `(p+1)/3`, the high coefficients force a translated pure power;
- that pure power is killed by one explicit coefficient.

The remaining constructive route must use:

1. polynomial degree at least `(p+4)/3`;
2. a rational function with a genuine denominator and degree at least `p/4`;
3. a multivariate construction;
4. a different cyclic extension or a new dynatomic factor theorem.

No bounded-complexity constructive template remains.

## 6. Verification

`artin_schreier_resonant_polynomial_barrier_verify.py` is a symbolic structural regression, not an irreducibility census. For every admitted prime below `200`, it verifies:

- the resonant cube-root identity
  
  `(1+gamma*T)^(3m) = 1+gamma*T mod T^(2m)`;
- the nonzero obstruction coefficient `rm` at degree `m-1`.

Frozen output:

`artin_schreier_resonant_polynomial_barrier_results_20260726.json`.
