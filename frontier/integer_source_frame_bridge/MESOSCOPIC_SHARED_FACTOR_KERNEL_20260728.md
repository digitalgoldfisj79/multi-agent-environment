# Mesoscopic shared-factor kernel

Date: 28 July 2026  
Status: exact shared-factor transport and bounded fixed-offset Gram proved; coherent source-pair summation remains open.

## 1. Setup

Let `B` be a consecutive block of primorial centres

\[
P_j=\prod_{p\le z_j}p,
\qquad
X\le z_j<2X,
\qquad
|B|\le K,
\qquad
K\ll\sqrt X.
\]

For `j<k`, write

\[
P_k=Q_{j,k}P_j,
\qquad
Q_{j,k}=\prod_{j<u\le k}z_u.
\tag{1.1}
\]

Let

\[
H=\eta X^2,
\qquad 0<\eta<1,
\]

and let `m,n` be physical offsets with

\[
z_B<m,n\le H,
\qquad z_B=\max_{u\in B}z_u.
\]

## 2. Shared-factor transport

### Theorem 2.1

If a prime `r>z_B` divides both

\[
P_j+m
\qquad\text{and}\qquad
P_k+n,
\]

then

\[
\boxed{r\mid n-Q_{j,k}m.}
\tag{2.1}
\]

Moreover

\[
n-Q_{j,k}m\ne0.
\tag{2.2}
\]

### Proof

Subtract `Q_{j,k}(P_j+m)` from `P_k+n` and use (1.1):

\[
(P_k+n)-Q_{j,k}(P_j+m)=n-Q_{j,k}m.
\]

This proves (2.1).  Since `Q_{j,k}>=X`, `m>z_B>=X` and `n<=H=eta X^2`,

\[
Q_{j,k}m>X^2>H\ge n,
\]

so the integer in (2.2) is strictly negative.  \(\square\)

## 3. Number and reciprocal mass of shared new primes

Put `h=k-j`.  Since every factor in (1.1) is below `2X`,

\[
Q_{j,k}<(2X)^h.
\tag{3.1}
\]

Also

\[
0<Q_{j,k}m-n<Q_{j,k}H.
\]

### Theorem 3.1

Uniformly in the centre pair and physical offsets,

\[
\boxed{
\#\{r>z_B:r\text{ prime},\ r\mid P_j+m,\ r\mid P_k+n\}
\ll h+1,
}
\tag{3.2}
\]

and

\[
\boxed{
\sum_{r>z_B\atop r\mid P_j+m,\ r\mid P_k+n}\frac1r
\ll\frac{h+1}{X}.
}
\tag{3.3}
\]

### Proof

Every prime in (3.2) divides the nonzero integer `Q_{j,k}m-n`.  If there are `s`
such primes, their product exceeds `X^s`; hence

\[
s\log X
\le
\log(Q_{j,k}H)
\le
h\log(2X)+2\log X+O(1).
\]

This proves (3.2).  Since every such prime exceeds `X`, (3.3) follows.  \(\square\)

## 4. Fixed-offset mesoscopic Gram

For fixed physical offsets `m,n`, define

\[
\mathcal C_{jk}(m,n)
=
\sum_{r>z_B\atop r\mid P_j+m,\ r\mid P_k+n}\frac1r
\quad(j\ne k),
\tag{4.1}
\]

and set the diagonal to any uniformly bounded nonnegative value.

### Corollary 4.1

For every fixed offset pair and every mesoscopic block,

\[
\boxed{
\|\mathcal C(m,n)\|_{\rm op}\ll1.
}
\tag{4.2}
\]

### Proof

By (3.3), one row has off-diagonal absolute sum

\[
\ll
\sum_{1\le h<K}\frac{h+1}{X}
\ll\frac{K^2}{X}\ll1.
\]

Apply the Schur row-sum bound.  \(\square\)

This is the common-divisor analogue of the mesoscopic additive-orbit frame.

## 5. Strategic limitation

The full source square contains a coherent sum over all offset pairs

\[
(m,n)\in\mathcal C_{P_j}(H)\times\mathcal C_{P_k}(H),
\]

of cardinality

\[
M^2\asymp\frac{H^2}{(\log H)^2}.
\]

Applying (4.2) separately to each pair and then taking absolute values loses this
entire factor.  Therefore the fixed-offset kernel does not by itself prove the
Fortune variance theorem.

A successful use must preserve at least one of:

1. cancellation in the offset-pair sum;
2. the complete smooth candidate projector;
3. the alternating Euler/Buchstab factor-cluster cancellation;
4. the signed pair singular-series centring.

The theorem removes shared-factor multiplicity as an obstruction on mesoscopic
blocks, but not the coherent source covariance.

## 6. Boundary

Proved exactly:

1. shared-factor transport (2.1);
2. nonvanishing of the transported integer;
3. `O(h)` shared-new-prime count;
4. reciprocal mass bound (3.3);
5. bounded fixed-offset mesoscopic Gram (4.2).

Not proved:

1. summation over the complete offset-pair source without an `M^2` loss;
2. deterministic centred sampling of the full quotient system;
3. Fortune's conjecture.
