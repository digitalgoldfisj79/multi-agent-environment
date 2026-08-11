# Programme status after the full rough-quotient reduction

Date: 28 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`  
Status: exact structural programme completed through its present theorem-level boundary; Fortune remains open.

## 1. Target

For consecutive primorial centres `P_j` with largest prime factors in `[X,2X)`,
put

\[
H=\eta X^2,
\qquad 0<\eta<1.
\]

The merged primitive-centred programme constructed an exact positive principal
term `mu_{P_j}^{prim}` and reduced Fortune to

\[
\boxed{
\sum_j
\left|
\sum_{m\le H}\Lambda(P_j+m)-\mu_{P_j}^{\rm prim}
\right|^2
\ll NHX L(X),
\qquad L(X)=o(\log X).
}
\tag{1.1}
\]

The present branch attacks the deterministic sampling side of (1.1).

## 2. PROVED — mesoscopic freezing and orbit geometry

Partition the primorial centres into consecutive blocks of size

\[
K\ll\sqrt X.
\]

On each block:

1. the moving candidate cutoff, physical modulus cutoff and Euler row weights may
   be frozen at total square cost `O(NHX)`;
2. the complete additive primorial-orbit Gram has bounded operator norm;
3. prime collisions satisfy an exact prefix-product criterion;
4. fixed-offset shared new factors have reciprocal Gram mass `O(1)`.

These results remove moving cutoffs, row-weight variation and bare orbit
multiplicity from the critical path.

## 3. PROVED — physical rough-quotient collapse

For

\[
P=\prod_{p\le z}p,
\qquad z<H<(z^+)^2,
\]

the candidate offsets are exactly

\[
\mathcal C_P(H)=\{m:z<m\le H,(m,P)=1\}.
\]

If a new prime `q` divides `P+m` and `P+m=qk`, then

\[
\boxed{(m,P)=1\iff(k,P)=1.}
\tag{3.1}
\]

Thus the prime-progression hit count is exactly a count of primorial-rough
quotients in

\[
P+z<qk\le P+H.
\]

The exact quotient count is

\[
\boxed{
N_P(q)=
\sum_{d\mid P}\mu(d)
\left[
\left\lfloor\frac{P+H}{qd}\right\rfloor-
\left\lfloor\frac{P+z}{qd}\right\rfloor
\right].
}
\tag{3.2}
\]

This is genuine compression: no prime indicator remains in the complementary
quotient interval.

## 4. PROVED — same-band reduction for the physical layer

The physical prime-modulus source may be partitioned into `O(log X)` dyadic
bands.  Outer Cauchy--Schwarz gives

\[
\sum_{j\in B}|G_j^{(1)}|^2
\le
O(\log X)
\sum_R\sum_{j\in B}|G_j^{(1)}(R)|^2.
\]

The previously proved physical diagonal is

\[
D_B^{(1)}\ll\frac{KHX}{\log X}.
\]

Therefore a uniform same-band actual-source Bessel estimate would prove an
`O(KHX)` bound for the complete physical layer.  Separate estimates for every
mixed dyadic covariance are unnecessary.

This is a genuine reduction of the missing theorem, but the same-band estimate
itself is open.

## 5. VERIFIED COMPUTATIONALLY — same-band diagonal behaviour

Complete frozen panels through `X=2003` give:

| `X` | maximum band square / diagonal | aggregate ratio |
|---:|---:|---:|
| 101 | 2.1541 | 1.1235 |
| 211 | 1.5819 | 0.9668 |
| 503 | 2.2870 | 1.0383 |
| 1009 | 1.7793 | 1.0034 |
| 2003 | 1.5508 | 0.9758 |

No asymptotic theorem is inferred.  The data support, but do not prove, a bounded
same-band actual-source operator.

## 6. PROVED — full rough-quotient Euler system

Let

\[
Y=\sqrt{P+H}
\]

and let `mathcal Q(z,Y)` be the squarefree products of primes in `(z,Y]`,
including `1`.  The complete prime-output detector is

\[
\boxed{
\sum_{m\in\mathcal C_P(H)}w_m\mathbf1_{P+m\text{ prime}}
=
\sum_{Q\in\mathcal Q(z,Y)}
\mu(Q)
\sum_{P+z<Qk\le P+H\atop(k,P)=1}w_{Qk-P}.
}
\tag{6.1}
\]

Its exact layers are:

1. `Q=1`, the principal layer;
2. `z<Q<=H`, physical single primes;
3. `H<Q<=Y`, sparse single tail primes;
4. products of at least two new primes, all exceeding `H`.

Every column `Q>H` has at most one quotient hit.  If an output has `t` new prime
factors at most `Y`, its complete factor-cluster contribution is

\[
\sum_{r=0}^{t}(-1)^r\binom tr=0.
\tag{6.2}
\]

Thus the tail-prime and higher-order layers are not optional error terms; they
restore the exact parity cancellation lost by the physical first-order layer.

## 7. EQUIVALENT REFORMULATION — complete Euler recombination

The rough quotient and Euler-divisor Dirichlet series satisfy

\[
\left(\sum_{(k,P)=1}k^{-s}\right)
\left(\sum_{Q\in\mathcal Q(z,Y)}\mu(Q)Q^{-s}\right)
=
\zeta(s)\prod_{p\le Y}(1-p^{-s}).
\tag{7.1}
\]

The coefficients on the right are the `Y`-rough integers, which in the Fortune
interval are exactly primes.  Therefore complete recombination returns the
original prime short-interval detector.

Equation (7.1) validates (6.1), but it is not an analytic shortcut.  The useful
structure lies before complete recombination.

## 8. CLOSED DIRECT ROUTES

The following direct routes are now closed absent a new ingredient.

### 8.1 Generic source/orbit factorisation

Bounding a source Fourier norm independently of the primorial orbit norm loses
the complete within-residue pair mass and cannot reach (1.1).

### 8.2 Support-only sparse-tail estimates

One-point support and shrinking-target multiplicity do not control arbitrary
signed column amplitudes.  Factor-cluster cancellation must be retained.

### 8.3 Positive separation of Euler layers

The physical, tail-prime and higher-order layers have main-size terms which
cancel by (6.2).  Independent positive majorants erase the parity cancellation.

### 8.4 Literal generic Kloosterman-fraction bounds

For `d|P`, additive reciprocity gives

\[
e(hP\overline d/q)=e(hP/(dq)).
\]

The literal Bettin--Chandee parameter has fixed numerator `vartheta=P`, producing
an exponential conductor factor on polynomial `d,q` ranges.  Current generic
bilinear/trilinear fraction theorems do not directly match the primorial divisor
system or the one-point top tail.

### 8.5 Fully recombined Perron analysis

By (7.1), this is the original prime short-interval problem in another exact
form.

## 9. Current technology boundary

Published results on:

1. rough integers possessing a divisor in a dyadic interval;
2. divisors and Poisson models of shifted primes;
3. bilinear/trilinear Kloosterman fractions;
4. primes in progressions to large moduli;

control global averages, fixed shifts, long convolutions or polynomial-length
intervals.  They do not currently provide the deterministic centred estimate for
this prescribed family of primorial centres at physical length
`H asymp (log P)^2`.

In particular, fixed-shift Kubilius models sample primes beyond the magnitude of
the fixed shift and treat small factors relative to the prime-sampling range.
Here the shift `P` grows exponentially, the source primes are at most `H`, and
the physical factors occupy the full range from `sqrt(H)` to `H`.

## 10. Smallest surviving theorem

The non-tautological target is not the already-proved quadratic-variation
identity.  It is the following deterministic covariance theorem.

### Full quotient sampling theorem — OPEN

For each mesoscopic block of consecutive primorial centres, prove a signed
second-moment estimate for the intermediate quotient system (6.1), centred by
the exact smooth-primitive principal, such that:

1. the physical single-prime bands satisfy an actual-source same-band Bessel
   estimate;
2. the sparse tail-prime and higher-order columns are recombined with the physical
   layer before absolute values are taken;
3. the factor-cluster cancellation (6.2) and normalized Buchstab martingale
   quadratic variation are preserved;
4. the block total is `O(KHX L(X))` with `L(X)=o(log X)`.

Summed over the mesoscopic blocks, this is precisely (1.1).

## 11. Assessment

The programme has genuinely removed:

1. incorrect centring;
2. growing convolution depth;
3. coefficient normalization;
4. moving cutoffs;
5. bare primorial collision multiplicity;
6. mixed-dyadic physical covariance as a separate obligation;
7. the prime indicator from each complementary quotient interval.

It has also shown that completely recombining the final Euler system is
tautological.  The surviving theorem is therefore sharply located: parity-breaking
cancellation must be transferred from the complete Euler/Buchstab model to the
mesoscopic primorial source without factorising the source or separating the
Euler layers.

Fortune's conjecture is not proved.
