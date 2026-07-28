# Primorial-index shrinking-target collapse

Date: 28 July 2026  
Status: exact orbit theorem proved; analytic use in the signed source decomposition remains open.

## 1. Purpose

The previous Heath--Brown depth note identified a real obstruction to a proof that
keeps every convolution variable below a fixed power of the physical interval

\[
H=\eta X^2,
\qquad 0<\eta<1.
\]

A fixed-depth exact identity necessarily contains divisor variables of exponential
size.  The earlier conclusion was that such a variable selects at most one physical
offset and therefore destroys the long `m`-average.

That conclusion is incomplete because it ignores the average over the primorial
index.  The large-divisor contribution has an exact multiplicative-orbit
representation, and exponential divisor scales force strong separation of its
visits.

## 2. Primorial block and physical residues

Let

\[
X\le \ell_0<\ell_1<\cdots<\ell_{N-1}<2X
\]

be the primes in the dyadic block, and let

\[
P_{j+1}=\ell_jP_j.
\]

For an integer modulus `d>H`, define the least positive residue

\[
r_j(d)\in\{1,\ldots,d\},
\qquad
r_j(d)\equiv-P_j\pmod d.
\]

Because `d>H`, there is at most one `m in [1,H]` satisfying

\[
d\mid P_j+m.
\]

It exists precisely when `r_j(d)<=H`, and then `m=r_j(d)`.

The prime-offset part of the double source is supported on

\[
X<m\le H.
\]

Accordingly define the visit set

\[
\mathcal V_d
=
\{j: X<r_j(d)\le H\}.
\]

The lower cutoff `X` is the candidate-collapse cutoff.  Prime or prime-power
offsets at most `X` either divide the primorial centre or belong to the already
separated proper-prime-power contamination.

## 3. Exact orbit recurrence

### Proposition 3.1

For every `j`,

\[
\boxed{
r_{j+1}(d)\equiv \ell_jr_j(d)\pmod d.
}
\]

More generally, for `j<k`, put

\[
Q_{j,k}=\prod_{j\le u<k}\ell_u=\frac{P_k}{P_j}.
\]

Then

\[
\boxed{
r_k(d)\equiv Q_{j,k}r_j(d)\pmod d.
}
\tag{3.1}
\]

### Proof

The congruence `P_j=-r_j(d) mod d` and the identity
`P_k=Q_{j,k}P_j` give

\[
-P_k\equiv Q_{j,k}r_j(d)\pmod d.
\]

The left side is `r_k(d)` modulo `d`.  \(\square\)

Thus the large-divisor one-point terms form a non-autonomous multiplicative orbit
whose multipliers are the consecutive block primes.

## 4. Visit-separation theorem

### Theorem 4.1 (shrinking-target separation)

If `j<k` both belong to `mathcal V_d`, then

\[
\boxed{
d\le H Q_{j,k}.
}
\tag{4.1}
\]

Consequently,

\[
\boxed{
k-j
\ge
\left\lceil
\frac{\log(d/H)}{\log(2X)}
\right\rceil.
}
\tag{4.2}
\]

### Proof

Write

\[
m_j=r_j(d),
\qquad
m_k=r_k(d),
\]

so that

\[
X<m_j,m_k\le H.
\]

Equation (3.1) gives

\[
Q_{j,k}m_j\equiv m_k\pmod d.
\tag{4.3}
\]

Assume for contradiction that `d>H Q_{j,k}`.  Then

\[
0<Q_{j,k}m_j\le Q_{j,k}H<d,
\qquad
0<m_k<d.
\]

The congruence (4.3) therefore forces equality

\[
m_k=Q_{j,k}m_j.
\]

But `Q_{j,k}>=X` and `m_j>X`, so

\[
m_k>X^2>H
\]

because `eta<1`.  This contradicts `m_k<=H`.  Hence (4.1).

Since every multiplier is below `2X`,

\[
Q_{j,k}\le(2X)^{k-j}.
\]

Combining this with (4.1) yields (4.2).  \(\square\)

## 5. Multiplicity bound

Put

\[
\Delta_X(d)
=
\max\left\{
1,
\left\lceil
\frac{\log(d/H)}{\log(2X)}
\right\rceil
\right\}.
\]

### Corollary 5.1

The visit set is `Delta_X(d)`-separated.  Therefore

\[
\boxed{
|\mathcal V_d|
\le
1+\left\lfloor\frac{N-1}{\Delta_X(d)}\right\rfloor.
}
\tag{5.1}
\]

In particular, if

\[
d\ge H(2X)^s,
\]

then

\[
\boxed{
|\mathcal V_d|
\le1+\left\lfloor\frac{N-1}{s}\right\rfloor.
}
\tag{5.2}
\]

This is deterministic.  It uses no distribution theorem for the orbit.

## 6. Fixed-depth largest-factor routing

Suppose a convolution term represents an output as

\[
P_j+m=x_1x_2\cdots x_R,
\qquad X<m\le H,
\]

with fixed `R`.  Route the term to a largest factor `d`.  Then

\[
d\ge(P_j+m)^{1/R}\ge P_0^{1/R}.
\tag{6.1}
\]

For fixed `R`, the prime number theorem gives

\[
\log P_0\asymp X,
\qquad
N\asymp\frac{X}{\log X}.
\]

Hence

\[
\Delta_X(P_0^{1/R})
\asymp_R\frac{X}{\log X}
\asymp_R N.
\]

### Corollary 6.1 (fixed-depth centre multiplicity)

For every fixed `R`, a fixed numerical largest factor

\[
d\ge P_0^{1/R}
\]

can be routed from prime-offset outputs in only

\[
\boxed{O(R)}
\]

centres of the dyadic primorial block.

More explicitly,

\[
|\mathcal V_d|
\le
1+
\frac{N\log(2X)}{R^{-1}\log P_0-\log H}
\]

whenever the denominator is positive.

## 7. Why this changes the Heath--Brown assessment

The previous depth obstruction remains correct in its narrow statement:

- bounded divisor cutoffs force depth `K asymp X/log X`;
- fixed depth forces at least one exponentially large factor.

What changes is the interpretation of the second point.

A factor

\[
d\asymp\exp(cX)
\]

does not merely select one offset for each centre.  The orbit theorem shows that,
for fixed `d`, those selected offsets can lie in the candidate interval at only
`O_c(1)` centres.  For a depth-`K` largest factor of natural size
`exp(X/O(K))`, the multiplicity is `O(K)`, not

\[
N\asymp X/\log X.
\]

Thus routing the largest factor before taking absolute values recovers the exact
factor `N` that a centre-by-centre positive treatment loses.

This does not by itself prove the required Type I/II estimate.  It proves that the
large-variable branch is not killed merely by the absence of a long `m`-progression.
The primorial-index average supplies a replacement form of sparsity.

## 8. Exact one-point transform

For `d>H`, put

\[
e_j(d)=\left\lceil\frac{P_j}{d}\right\rceil,
\qquad
m_j(d)=d e_j(d)-P_j.
\]

Then for arbitrary coefficient sequences `alpha_m` and `beta_e`,

\[
\boxed{
\sum_{1\le m\le H}
\alpha_m\beta_{(P_j+m)/d}
\mathbf 1_{d\mid P_j+m}
=
\mathbf 1_{1\le m_j(d)\le H}
\alpha_{m_j(d)}\beta_{e_j(d)}.
}
\tag{8.1}
\]

The large divisor sum is therefore exactly a shrinking-target orbit sum.  No
approximation or divisor switching error is present in (8.1).

## 9. Revised analytic target

A fixed-depth signed decomposition should now be organised as follows.

1. Expand the centred source without taking absolute values.
2. In every factorisation term, route to a canonical largest factor `d`.
3. Use (8.1) to remove the physical offset sum for that factor.
4. Average over the primorial index while the signs remain present.
5. Apply Corollary 6.1 to replace the former centre multiplicity `N` by `O(R)`.
6. Estimate the remaining fixed-complexity quotient coefficients and cross-factor
   correlations.

The next theorem is no longer a generic growing-depth Heath--Brown estimate.  It is
a fixed-depth, largest-factor-routed signed inequality in which each large factor
has bounded primorial-index multiplicity.

## 10. Boundary

Proved:

1. exact multiplicative orbit recurrence;
2. exact visit-separation inequality `d<=H Q_{j,k}`;
3. the deterministic visit multiplicity bound;
4. `O(R)` centre multiplicity after routing a fixed-depth term to its largest
   factor;
5. the exact one-point transform (8.1).

Not proved:

1. the required signed bound after summing all largest factors;
2. uniform control of the quotient convolution coefficients;
3. the final four-prime covariance or centred source-energy estimate;
4. Fortune's conjecture.

The former statement that exponentially large variables remove all useful
averaging is retracted.  The useful average is over the primorial index, and the
shrinking-target theorem quantifies it exactly.
