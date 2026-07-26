# Generic Cartier transfer minimality obstruction

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** fixed-class Cartier/Krylov transfer route for function-field Fortune `d=1`.  
**Status:** the algebraic statements below are **PROVED**. The crown remains **OPEN**.

## 1. Generic sparse family

Let

\[
k_0=\mathbf F_p(a,c),
\qquad
k=k_0(d),
\]

where `a,c,d` are algebraically independent and `a!=0`. Put

\[
F(X)=X^p+aX^3+cX+d
\]

and

\[
A=k[X]/(F).
\]

Write `x` for the residue class of `X` and define the sparse tail

\[
h=a x^3+c x+d=-x^p.
\]

The existing Cartier--Krylov theorem identifies multiplication by `h` as the natural one-step recurrence behind the principal-part transfer. The question is whether that recurrence has a nontrivial coefficient-rational quotient of dimension below `p`.

## 2. Generic irreducibility

### Theorem 2.1

The polynomial

\[
F(X)=X^p+aX^3+cX+d
\]

is irreducible and separable over `k`.

### Proof

Over `k_0`, let

\[
g(X)=X^p+aX^3+cX.
\]

Its derivative is

\[
g'(X)=3aX^2+c,
\]

which is not the zero polynomial. Hence the rational map `g` is separable of degree `p`, and

\[
[k_0(X):k_0(g(X))]=p.
\]

The element `X` therefore has minimal polynomial of degree `p` over the rational function field `k_0(g(X))`. Since it is a root of

\[
T^p+aT^3+cT-g(X),
\]

that polynomial is irreducible in `k_0(g(X))[T]`. Replacing the transcendental element `g(X)` by `-d` gives the claimed irreducibility over `k_0(d)`. Separability follows again from `3aX^2+c!=0`. ∎

Consequently `A` is a field of prime degree `p` over `k`.

## 3. The tail is a primitive generator

### Theorem 3.1

The element `h` generates the complete generic algebra:

\[
\boxed{k(h)=A.}
\]

Its minimal polynomial is

\[
\boxed{Z^p+aZ^3+cZ-d.}
\]

### Proof

If `h` belonged to `k`, then

\[
x^p=-h\in k.
\]

The element `x` would then be purely inseparable over `k`, contradicting Theorem 2.1. Thus `h notin k`.

Because `[A:k]=p` is prime, the intermediate field `k(h)` has degree either `1` or `p`. The first case has just been excluded, so `k(h)=A`.

Finally,

\[
h^p=(a x^3+c x+d)^p
=a x^{3p}+c x^p+d
=-a h^3-c h+d,
\]

and hence

\[
h^p+a h^3+c h-d=0.
\]

This relation has degree `p`, which is the degree of `h` over `k`, so it is the minimal polynomial. ∎

This recovers intrinsically the characteristic polynomial

\[
-F(-Z)=Z^p+aZ^3+cZ-d
\]

previously found for the one-step Krylov operator.

## 4. No nontrivial linear transfer quotient

### Corollary 4.1

There is no nonzero proper `k`-linear subspace of `A` stable under multiplication by `h`.

### Proof

An `h`-stable `k`-subspace is a module over

\[
k[h]=A.
\]

Since `A` is a field acting on itself by multiplication, its only submodules are `0` and `A`. ∎

### Corollary 4.2: minimal state dimension

Any coefficient-rational linear realization that contains a cyclic state reproducing the complete generic sequence

\[
1,h,h^2,\ldots
\]

has dimension at least `p`.

Indeed, the annihilator of the cyclic state is the degree-`p` polynomial

\[
Z^p+aZ^3+cZ-d.
\]

A linear operator on a space of dimension below `p` cannot have this polynomial as the minimal polynomial of a cyclic vector.

### Exact ruling

The fixed-class Cartier transfer cannot be compressed by:

1. a smaller Krylov state;
2. a proper invariant subspace of the generic tail recurrence;
3. a coefficient-rational linear quotient preserving that recurrence;
4. a Hankel or companion realization with fewer than `p` states.

This strengthens the earlier `H=G^{-1}QG` ruling. That theorem proved that the natural `p`-state transfer is merely Frobenius in another basis. The present theorem proves that the generic sparse tail itself has no nontrivial linear state quotient.

## 5. What is not ruled out

The theorem does **not** rule out:

1. summing coefficient orbits before constructing a transfer;
2. a nonlinear invariant;
3. a correspondence that does not preserve multiplication by `h`;
4. a special arithmetic degeneration unavailable over the generic coefficient field;
5. a q-line or constructive-dynamical theorem.

The only plausible escape inside the transfer programme is therefore an **orbit-first** transform. The corresponding Hayes logarithmic transform is analysed separately.

## 6. Verification

`generic_cartier_transfer_minimality_verify.py` is a standard-library regression. It does not perform a prime census. For one irreducible square-class and one nonsquare-class specialization at each of `p=5,7,11`, it verifies:

- the exact relation `h^p+a h^3+c h-d=0`;
- full rank `p` of the Krylov vectors `1,h,...,h^(p-1)`.

Frozen output:

`generic_cartier_transfer_minimality_results_20260726.json`.
