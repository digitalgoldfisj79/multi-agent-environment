# Full rough-quotient Euler collapse

Date: 28 July 2026  
Status: exact full-chaos quotient identity proved; deterministic centred sampling theorem open.

## 1. Setup

Let

\[
P=\prod_{p\le z}p,
\qquad
z<H<(z^+)^2,
\qquad
Y=\sqrt{P+H}.
\tag{1.1}
\]

Define the candidate source

\[
\mathcal C_P(H)=\{m:z<m\le H,\ (m,P)=1\}.
\tag{1.2}
\]

In this range `mathcal C_P(H)` is exactly the set of primes in `(z,H]`.
Let `mathcal Q(z,Y)` be the squarefree integers, including `1`, all of whose
prime factors lie in `(z,Y]`.

## 2. Exact Euler divisor detector

### Theorem 2.1

For every `m in mathcal C_P(H)`, putting `n=P+m`,

\[
\boxed{
\mathbf1_{n\text{ prime}}
=
\sum_{Q\in\mathcal Q(z,Y)\atop Q\mid n}\mu(Q).
}
\tag{2.1}
\]

### Proof

Every prime factor of `n` exceeds `z`, because `(n,P)=(m,P)=1`.  If `n` is
prime, then `n>Y`, so the only divisor in `mathcal Q(z,Y)` is `Q=1`, and the
sum is one.

If `n` is composite, its least prime factor is at most `sqrt(n)<=Y` and exceeds
`z`.  Let `r_1,...,r_t` be the distinct prime divisors of `n` in `(z,Y]`; then
`t>=1`.  The admissible divisors `Q|n` are exactly the squarefree subset products
of these primes.  Hence the right side is

\[
\prod_{i=1}^{t}(1-1)=0.
\]

This proves (2.1).  \(\square\)

Equation (2.1) is the complete signed Euler cancellation, not a truncation or a
positive sieve majorant.

## 3. Coprimality transport for every Euler divisor

### Lemma 3.1

Let `(Q,P)=1` and `m=Qk-P`.  Then

\[
\boxed{(m,P)=1\iff(k,P)=1.}
\tag{3.1}
\]

### Proof

For each prime `p|P`,

\[
m\equiv Qk\pmod p.
\]

Since `Q` is invertible modulo `p`, divisibility of `m` and `k` by `p` is
equivalent.  \(\square\)

## 4. Exact full quotient identity

Let `w_m` be arbitrary complex weights on `mathcal C_P(H)`.  For
`Q in mathcal Q(z,Y)` define

\[
\mathcal K_P(Q)
=
\{k\in\mathbb Z:P+z<Qk\le P+H,\ (k,P)=1\}.
\tag{4.1}
\]

### Theorem 4.1 (full rough-quotient Euler identity)

\[
\boxed{
\sum_{m\in\mathcal C_P(H)}
 w_m\mathbf1_{P+m\text{ prime}}
=
\sum_{Q\in\mathcal Q(z,Y)}
\mu(Q)
\sum_{k\in\mathcal K_P(Q)}w_{Qk-P}.
}
\tag{4.2}
\]

### Proof

Insert (2.1), interchange the finite `m` and `Q` sums, and for each divisor
relation `Q|P+m` set `k=(P+m)/Q`.  Lemma 3.1 gives a weight-preserving
bijection between the candidate offsets hit by `Q` and `mathcal K_P(Q)`.
\(\square\)

No prime indicator remains on the right side.  Both the Euler divisor `Q` and
the complementary quotient `k` are primorial-rough.

## 5. Exact four-level decomposition

The condition `H<(z^+)^2` has a decisive consequence.

### Theorem 5.1

Every `Q in mathcal Q(z,Y)` lies in exactly one of the following classes:

1. `Q=1`;
2. `z<Q<=H`, in which case `Q` is a single physical prime;
3. `H<Q<=Y`, in which case `Q` is a single tail prime;
4. `Q` has at least two new prime factors, in which case
   `Q>=(z^+)^2>H`.

Moreover, for every `Q>H`, whether prime or composite,

\[
\boxed{|\mathcal K_P(Q)|\le1.}
\tag{5.1}
\]

### Proof

A product of two primes exceeding `z` is at least `(z^+)^2>H`.  Hence an
admissible `Q<=H` is either one or one prime.  A one-prime divisor larger than
`H` lies in class 3 because every prime factor of an admissible `Q` is at most
`Y`.  Every product of at least two new primes lies in class 4 and exceeds `H`.
Finally, the interval in (4.1) has length `(H-z)/Q<1` for every `Q>H`, so it
contains at most one integer.  \(\square\)

Thus (4.2) decomposes exactly into

\[
\boxed{
\text{principal }Q=1
+
\text{physical single-prime layer}
+
\text{sparse single-prime tail}
+
\text{sparse higher-order tail}.
}
\tag{5.2}
\]

The last two layers are both one-point quotient systems.  All four are algebraic
parts of one signed identity and may not be bounded by independent positive
majorants.

## 6. Relation to the previous first-order quotient theorem

The `Q=1` term is

\[
\sum_{m\in\mathcal C_P(H)}w_m.
\tag{6.1}
\]

The physical single-prime part is

\[
-\sum_{z<q\le H\atop q\text{ prime}}
\sum_{k\in\mathcal K_P(q)}w_{qk-P},
\tag{6.2}
\]

which is exactly the hit component of
`ROUGH_QUOTIENT_HYPERBOLA_COLLAPSE_20260728.md`.  The locally centred first-order
formula adds and subtracts its complete-residue conditional mean.

The single-prime tail `H<q<=Y` is the sparse first-order tail already present in
the ordered Buchstab decomposition.  The composite `Q` terms are the higher
Euler/Buchstab chaos.  Together they cancel factor clusters in the physical and
tail first-order layers.

## 7. Factor-cluster cancellation

Suppose `n=P+m` has exactly `t>=1` distinct prime factors in `(z,Y]`.  Its
contribution to all Euler layers of (4.2) is

\[
\sum_{r=0}^{t}(-1)^r\binom tr=0.
\tag{7.1}
\]

The complete single-prime layer contributes `-t`; all orders `r>=2` are required
to restore the exact zero.  Therefore a same-band physical first-order Bessel
theorem cannot be promoted to a generic arbitrary-source operator statement
without controlling factor clusters.  The actual-source physical estimate remains
a useful diagnostic, but the full quotient identity (4.2) is the preferred final
architecture.

## 8. Correct centred target

For the natural weight `w_m=log(P+m)`, proper prime powers contribute `o(H)` by
the already-proved prime-power estimate.  Let `mu_P^prim` be the exact
smooth-primitive principal term.  Define

\[
\mathcal E_P^{\mathrm{quot}}
=
\sum_{Q\in\mathcal Q(z,Y)}
\mu(Q)
\sum_{k\in\mathcal K_P(Q)}\log(Qk)
-
\mu_P^{\mathrm{prim}}.
\tag{8.1}
\]

Then the load-bearing theorem is

\[
\boxed{
\sum_j|\mathcal E_{P_j}^{\mathrm{quot}}|^2
\ll NHX\,L(X),
\qquad L(X)=o(\log X).
}
\tag{8.2}
\]

The normalized Buchstab-martingale representation supplies an equivalent
coefficient system with total square mass `O(NHX)`.  Equation (4.2) supplies the
exact rough-quotient geometry of the same system.

## 9. Boundary

Proved exactly:

1. complete Euler divisor detector (2.1);
2. coprimality transport for arbitrary new divisor products (3.1);
3. weighted full quotient identity (4.2);
4. principal/physical-prime/tail-prime/higher-order classification (5.2);
5. one-point support of every quotient column `Q>H`;
6. exact factor-cluster cancellation (7.1).

Strategic qualification:

1. the same-band physical first-order theorem is sufficient for that layer but is
   not a substitute for the joint full-chaos covariance;
2. arbitrary-source Bessel estimates can fail in the presence of large factor
   clusters.

Open:

1. deterministic centred sampling for the full quotient system (8.2);
2. a proof that combines same-band physical dispersion with both sparse tail
   layers without losing (7.1);
3. Fortune's conjecture.
