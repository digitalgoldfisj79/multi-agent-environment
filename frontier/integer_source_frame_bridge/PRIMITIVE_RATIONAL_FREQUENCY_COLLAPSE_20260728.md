# Primitive rational-frequency collapse

Date: 28 July 2026  
Status: exact reduced-frequency identity proved; Ramanujan-coefficient asymptotic proved from the classical zeta zero-free region in ranges with a long complementary sum; final signed frame estimate open.

## 1. Exact centred Möbius--log source

Let `w_m` be deterministic complex weights supported on `2<=m<=H`.  Put

\[
W_H=\sum_m w_m,
\qquad
\widehat w_d(r)=\sum_m w_m e(rm/d).
\]

For one centre `P` put `Z=P+H`.  The exact Möbius--log principal term is

\[
\mu_P^{\mathrm{mob}}
=-W_H\sum_{d\le Z}\frac{\mu(d)\log d}{d}.
\]

The centred residual is

\[
R_P
=
\sum_mw_m\Lambda(P+m)-\mu_P^{\mathrm{mob}}.
\]

Additive orthogonality gives

\[
\boxed{
R_P
=-
\sum_{d\le Z}
\frac{\mu(d)\log d}{d}
\sum_{r=1}^{d-1}
\widehat w_d(r)e(rP/d).
}
\tag{1.1}
\]

## 2. Reduction of a rational frequency

Write a nonzero fraction `r/d` uniquely as

\[
\frac rd=\frac aq,
\qquad
(a,q)=1,
\qquad
1\le a<q.
\]

Then there is a unique integer `u>=1` such that

\[
d=qu,
\qquad
r=au.
\]

Moreover

\[
\widehat w_{qu}(au)=\widehat w_q(a),
\qquad
e(auP/(qu))=e(aP/q).
\tag{2.1}
\]

Thus every multiple of the same reduced rational frequency has the same Fourier
row.

## 3. Exact primitive-frequency identity

For `2<=q<=Z`, define

\[
\boxed{
\Gamma_Z(q)
=-\frac1q
\sum_{u\le Z/q}
\frac{\mu(qu)\log(qu)}u.
}
\tag{3.1}
\]

### Theorem 3.1

One has exactly

\[
\boxed{
R_P
=
\sum_{q=2}^{Z}
\Gamma_Z(q)
\sum_{a\bmod q\atop (a,q)=1}
\widehat w_q(a)e(aP/q).
}
\tag{3.2}
\]

### Proof

In (1.1), replace every pair `(d,r)` by its unique triple `(q,a,u)` from
Section 2.  Equations (2.1) remove `u` from the Fourier row, and the remaining
coefficient sum is exactly (3.1).  The transformation is a bijection between

\[
\{(d,r):d\le Z,\ 1\le r<d\}
\]

and

\[
\{(q,a,u):2\le q\le Z,\ (a,q)=1,\ 1\le a<q,\ qu\le Z\}.
\]

Hence no term is added or removed.  \(\square\)

This identity preserves every sign, the exact principal subtraction and all
cross-modulus interactions.  It shows that the apparent large-divisor sector
contains many repetitions of lower primitive frequencies.

## 4. Arithmetic form of the coefficient

If `q` is not squarefree, then

\[
\Gamma_Z(q)=0.
\]

If `q` is squarefree and `T=Z/q`, then

\[
\boxed{
\Gamma_Z(q)
=-\frac{\mu(q)}q
\left[
\log q\,M_q(T)+L_q(T)
\right],
}
\tag{4.1}
\]

where

\[
M_q(T)=
\sum_{u\le T\atop(u,q)=1}\frac{\mu(u)}u,
\qquad
L_q(T)=
\sum_{u\le T\atop(u,q)=1}\frac{\mu(u)\log u}{u}.
\tag{4.2}
\]

This follows from

\[
\mu(qu)=\mu(q)\mu(u)\mathbf1_{(u,q)=1}.
\]

## 5. Ramanujan limit

The Dirichlet series of the coprime Möbius sum is

\[
F_q(s)
=
\sum_{(u,q)=1}\frac{\mu(u)}{u^s}
=
\frac1{\zeta(s)}
\prod_{p\mid q}(1-p^{-s})^{-1}.
\tag{5.1}
\]

At `s=1`, `1/zeta(s)` has a simple zero.  Therefore

\[
F_q(1)=0,
\qquad
-F_q'(1)
=
\sum_{(u,q)=1}\frac{\mu(u)\log u}{u}
=-\frac q{\varphi(q)}.
\tag{5.2}
\]

Consequently, for each fixed squarefree `q`,

\[
\boxed{
\Gamma_Z(q)\longrightarrow\frac{\mu(q)}{\varphi(q)}
\qquad (Z\to\infty).
}
\tag{5.3}
\]

The coefficient is the classical Ramanujan coefficient of the von Mangoldt
function.

## 6. Uniform long-complementary range

The classical zero-free region for `zeta(s)`, applied to (5.1), gives the
following standard uniform form.  For every fixed `delta>0`, uniformly for
squarefree

\[
q\le Z^{1-\delta},
\qquad T=Z/q\ge Z^\delta,
\]

one has

\[
M_q(T)
\ll_\delta
\frac q{\varphi(q)}(\log Z)^C E(T),
\tag{6.1}
\]

and

\[
L_q(T)
=-\frac q{\varphi(q)}
+
O_\delta\left(
\frac q{\varphi(q)}(\log Z)^C E(T)
\right),
\tag{6.2}
\]

where `C` is absolute and

\[
E(T)=
\exp\left(
-c(\log T)^{3/5}(\log\log T)^{-1/5}
\right).
\]

Hence

\[
\boxed{
\Gamma_Z(q)
=
\frac{\mu(q)}{\varphi(q)}
+
O_\delta\left(
\frac1{\varphi(q)}(\log Z)^{C+1}E(Z^\delta)
\right)
}
\tag{6.3}
\]

uniformly in this range.

The finite Euler factors in (5.1) cost only powers of logarithms because
`q/phi(q) ll log log q`; the zero-free-region decay dominates those factors when
`T>=Z^delta`.

In particular, every polynomial denominator `q<=H=poly(log Z)` lies deep inside
the uniform range, and its exact coefficient is exponentially close on the
`log Z` scale to `mu(q)/phi(q)`.

## 7. Source/frame consequence

Define the primitive row

\[
\mathcal W_{P,q}
=
\sum_{a\bmod q\atop(a,q)=1}
\widehat w_q(a)e(aP/q).
\]

Then (3.2) is

\[
R_P=\sum_{q\le Z}\Gamma_Z(q)\mathcal W_{P,q}.
\tag{7.1}
\]

For a block of centres, the exact variance is therefore

\[
\boxed{
\sum_j|R_{P_j}|^2
=
\sum_{q,r}
\Gamma_{Z_j}(q)\overline{\Gamma_{Z_j}(r)}
\sum_j
\mathcal W_{P_j,q}
\overline{\mathcal W_{P_j,r}},
}
\tag{7.2}
\]

with the understood centre-dependent cutoffs `q<=Z_j`, `r<=Z_j`.  More
explicitly, the right side is summed over `j,q,r`; it is not a product of a
centre-independent coefficient and Gram matrix unless the cutoff is first
uniformised.

The critical gain is conceptual and algebraic:

1. divisor multiples with the same reduced phase have already cancelled inside
   `Gamma_Z(q)`;
2. the polynomial and fixed-power denominator ranges carry the standard signed
   coefficient `mu(q)/phi(q)` up to a negligible error;
3. only primitive rational frequencies remain;
4. the top range `q>Z^{1-delta}` is the genuine short-complementary tail.

## 8. Correct next estimate

The load-bearing theorem is now a signed primitive-frequency frame estimate for
(7.2), retaining the `mu(q)/phi(q)` coefficients and the cross-frequency terms.
It must not be replaced by the sum of absolute energies of individual `q` ranges:
the low primitive frequencies contain deterministic local structure and cancel
against other frequencies in the centred source.

A viable proof architecture is:

1. use (6.3) on `q<=Z^{1-delta}`;
2. exploit the primorial structure in the signed Ramanujan kernel;
3. treat `q>Z^{1-delta}` by a complementary-factor or shrinking-target argument;
4. recombine all ranges before taking absolute values.

## 9. Boundary

Proved exactly:

1. reduced-frequency parametrisation;
2. primitive coefficient formula (3.1);
3. exact source identity (3.2);
4. vanishing for nonsquarefree `q`;
5. arithmetic decomposition (4.1).

Proved from published classical input:

1. the Ramanujan limit (5.3);
2. the uniform long-complementary estimate (6.3).

Open:

1. the signed primitive-frequency frame bound for the primorial centre set;
2. control of the top short-complementary range after recombination;
3. the Fortune variance theorem and Fortune's conjecture.
