# Smooth quadric-cubic reduction for the d=1 trace sum

**Date:** 2026-07-23  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** the geometric reduction and smoothness theorem below are **PROVED**. The Frobenius-trace estimate remains **OPEN**.

## 1. Setup

Let

\[
K=\mathbf F_{p^p},\qquad H=\{x\in K:\operatorname{Tr}(x)=0\},
\]

and write

\[
Q(x)=\operatorname{Tr}(x^2),\qquad C(x)=\operatorname{Tr}(x^3).
\]

For `t in F_p` and `x in H`, characteristic `p` gives

\[
Q(x+t)=Q(x),
\]

and

\[
C(x+t)=C(x)+3tQ(x).
\]

Hence on the null cone `Q=0`, both `Q` and `C` descend through the translation quotient

\[
W:=H/\mathbf F_p.
\]

The trace pairing on `H` has radical exactly `F_p`, so the descended quadratic form on `W` is nondegenerate. Since `dim H=p-1`, one has `dim W=p-2`.

The collapse sum may be written

\[
T_p=p\sum_{w\in W,\,Q(w)=0}\psi(C(w)).
\]

Equivalently,

\[
D_{b\ne0}=-\sum_{w\in W,\,Q(w)=0}\psi(C(w)).
\]

Thus the analytic target is square-root cancellation for a cubic phase on a nondegenerate quadric of affine dimension `p-3`.

## 2. PROVED: no nonzero critical points

### Theorem 2.1

For every prime `p>=5`, the restriction of `C` to the quadric `Q=0` in `W` has no nonzero critical point.

Equivalently, the projective complete intersection

\[
X_p:=\{Q=C=0\}\subset \mathbf P(W)
\]

is smooth.

### Proof

Let `w in W` be represented by `x in H` with `Q(x)=0`. Suppose `w` is a critical point of `C|_{Q=0}`. Since the trace pairing on `K/F_p` is nondegenerate, the differentials are

\[
dQ_x(y)=2\operatorname{Tr}(xy),\qquad dC_x(y)=3\operatorname{Tr}(x^2y).
\]

Criticality on the hyperplane `H`, modulo the translation radical, means that for some `lambda in F_p`,

\[
3\operatorname{Tr}(x^2y)=2\lambda\operatorname{Tr}(xy)
\]

for every `y in H`.

The orthogonal complement of `H` under the trace pairing is exactly `F_p`. Therefore there is `mu in F_p` such that

\[
3x^2-2\lambda x=\mu.
\]

Hence `x` satisfies a polynomial of degree at most two over `F_p`, so

\[
[\mathbf F_p(x):\mathbf F_p]\mid 2.
\]

But `x in K=F_{p^p}`, and every subfield degree divides `p`. Since `p` is odd,

\[
\gcd(2,p)=1,
\]

therefore `x in F_p`. Its class in `W=H/F_p` is zero. Thus there is no nonzero critical point. The projective smoothness statement is the standard Jacobian criterion: a singular projective point of `Q=C=0` would be a nonzero point where `dC` is proportional to `dQ`. QED.

## 3. Consequences

### PROVED

- `Q=0` is a smooth projective quadric in `P(W)`.
- `X_p={Q=C=0}` is a smooth complete intersection of type `(2,3)` in `P^{p-3}`.
- The missing factor of order `p` in the current bound is not caused by singularities or a positive-dimensional critical locus.
- The cubic phase is cohomologically nondegenerate in the usual stationary-phase sense away from the cone vertex.

### OPEN

Generic Deligne bounds for a smooth `(2,3)` complete intersection are not enough by themselves because the primitive middle Betti number grows rapidly with `p`. The remaining task is to exploit the arithmetic Frobenius composed with the cyclic coordinate shift on this very special smooth complete intersection.

## 4. Exact next target

Over `Fbar_p`, restriction of scalars identifies `W` with the trace-zero coordinate representation modulo the constant line. The cyclic shift acts unipotently because its order is `p` in characteristic `p`.

The next theorem to prove is therefore a wild Lefschetz/local-term statement for the cyclic-Frobenius action on the smooth pair

\[
Q=\sum x_i^2=0,\qquad C=\sum x_i^3=0,
\]

modulo the constant translation line.

A successful result would show that the twisted trace on the primitive cohomology is controlled by a bounded collection of local terms, despite the growing ordinary Betti number.

The immediate subproblems are:

1. determine the scheme-theoretic fixed locus of the cyclic shift on the projective quadric and on `X_p`;
2. compute its tangent and normal action, noting that the shift is unipotent and ordinary semisimple fixed-point formulas do not apply directly;
3. identify the correct wild Lefschetz formula or arithmetic Picard-Lefschetz theorem;
4. compare the resulting local term with `T_p/p^{(p-1)/2}`.

## 5. Boundary

This theorem is a genuine simplification of Route 2, but it does not prove the absolute-constant bound. It shows that the remaining difficulty is entirely the trace of a wild cyclic action on smooth cohomology, not singular geometry.