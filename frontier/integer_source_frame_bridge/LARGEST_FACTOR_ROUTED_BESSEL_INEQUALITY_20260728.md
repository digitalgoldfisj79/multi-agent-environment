# Largest-factor-routed Bessel inequality

Date: 28 July 2026  
Status: exact Hilbert-space consequence of the shrinking-target theorem.

## 1. Setup

Use the visit sets

\[
\mathcal V_d=\{j:X<r_j(d)\le H\}
\]

from `PRIMORIAL_INDEX_SHRINKING_TARGET_COLLAPSE_20260728.md`.
For a modulus family `mathcal D`, put

\[
M(\mathcal D)=\sup_{d\in\mathcal D}|\mathcal V_d|.
\]

Let `x_{j,d}` be arbitrary complex coefficients supported on
`j in mathcal V_d`.

## 2. Exact inequality

### Theorem 2.1

One has

\[
\boxed{
\sum_{d\in\mathcal D}
\left|\sum_{j\in\mathcal V_d}x_{j,d}\right|^2
\le
M(\mathcal D)
\sum_{d\in\mathcal D}
\sum_{j\in\mathcal V_d}|x_{j,d}|^2.
}
\tag{2.1}
\]

### Proof

For each fixed `d`, Cauchy--Schwarz gives

\[
\left|\sum_{j\in\mathcal V_d}x_{j,d}\right|^2
\le
|\mathcal V_d|
\sum_{j\in\mathcal V_d}|x_{j,d}|^2.
\]

Sum over `d` and use `|mathcal V_d|<=M(mathcal D)`.  \(\square\)

The point is not the Cauchy inequality itself.  The new input is the deterministic
orbit theorem, which replaces the trivial multiplicity `N` by a scale-sensitive
quantity.

## 3. Dyadic large-factor scales

If every `d in mathcal D` satisfies

\[
d\ge H(2X)^s,
\]

then the shrinking-target theorem gives

\[
M(\mathcal D)
\le
1+\left\lfloor\frac{N-1}{s}\right\rfloor.
\]

Therefore

\[
\boxed{
\sum_{d\in\mathcal D}
\left|\sum_{j\in\mathcal V_d}x_{j,d}\right|^2
\le
\left(1+\left\lfloor\frac{N-1}{s}\right\rfloor\right)
\sum_{d,j}|x_{j,d}|^2.
}
\tag{3.1}
\]

At exponential scale `d=exp(cX+o(X))`, one has

\[
s\asymp_c\frac{X}{\log X}\asymp_c N,
\]

so the factor on the right is `O_c(1)`.

## 4. Fixed-depth factorisations

Route every factorisation

\[
P_j+m=x_1\cdots x_R,
\qquad X<m\le H,
\]

to a canonical largest factor `d`.  Then

\[
d\ge P_0^{1/R}.
\]

For fixed `R`, the visit theorem gives

\[
M_R
:=
\sup_{d\ge P_0^{1/R}}|\mathcal V_d|
=O(R).
\]

Consequently,

\[
\boxed{
\sum_d
\left|\sum_{j\in\mathcal V_d}x_{j,d}\right|^2
\ll_R
\sum_{d,j}|x_{j,d}|^2.
}
\tag{4.1}
\]

A centre-by-centre argument would insert the factor

\[
N\asymp X/\log X
\]

at this point.  Largest-factor routing replaces it by `O(R)`.

## 5. Application boundary

Equation (4.1) is load-bearing only if the signed Heath--Brown or Vaughan
expansion is arranged so that the primorial-index sum occurs inside the square at
fixed routed factor `d`.  Taking absolute values before routing destroys the gain.

The remaining work is therefore precise:

1. write one fixed-depth centred source component in largest-factor-routed form;
2. keep its Möbius and combinatorial signs;
3. apply (4.1) to the `j`-sum at fixed `d`;
4. prove that the remaining quotient-coefficient square sum lies at the Fortune
   variance scale.

The theorem does not yet bound that quotient square sum.  It proves that the
formerly missing factor `X/log X` is recoverable from primorial-index sparsity and
need not be supplied by a short-interval prime-pair theorem.
