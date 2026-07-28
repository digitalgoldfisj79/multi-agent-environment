# Mesoscopic primorial-orbit reduction

Date: 28 July 2026  
Status: unconditional mesoscopic freezing and orbit-frame theorems proved; source--orbit bilinear estimate remains open.

## 1. Setup

Let

\[
H=\eta X^2,
\qquad 0<\eta<1,
\]

and let

\[
P_0,P_1,\ldots,P_{N-1}
\]

be the consecutive primorial centres whose largest prime factors

\[
z_0<z_1<\cdots<z_{N-1}
\]

lie in `[X,2X)`.  Thus

\[
P_{j+1}=z_{j+1}P_j.
\tag{1.1}
\]

Use the exact Euler--Buchstab candidate weights

\[
b_{j,m}=\log(P_j+m)V(z_j,Y_j),
\qquad Y_j=\sqrt{P_j+H},
\]

on the candidate primes `z_j<m<=H`.

The locally centred physical first-order term is

\[
G_j^{(1)}
=-\sum_{z_j<r\le H\atop r\ {m prime}}
\frac{r-1}{r-2}\Delta_{j,r},
\tag{1.2}
\]

with `Delta_{j,r}` as in `FIRST_ORDER_PRIME_MODULUS_GRAM_20260728.md`.

## 2. Mesoscopic partition

Choose an integer

\[
1\le K\le c\sqrt X
\tag{2.1}
\]

for a fixed sufficiently small constant `c`, and partition the centre indices into
consecutive blocks `B` of cardinality at most `K`.

For one block put

\[
z_B=\max_{j\in B}z_j,
\]

and define the common candidate and modulus sets

\[
\mathcal M_B=\{m:z_B<m\le H,\ m\text{ prime}\},
\tag{2.2}
\]

\[
\mathcal R_B=\{r:z_B<r\le H,\ r\text{ prime}\}.
\tag{2.3}
\]

Also put

\[
\beta_j=\log P_j\,V(z_j,Y_j).
\tag{2.4}
\]

## 3. Freezing the candidate source

### Lemma 3.1 (weight freezing)

Uniformly for `2<=m<=H`,

\[
 b_{j,m}=\beta_j+O\!\left(V(z_j,Y_j)\frac H{P_j}\right).
\tag{3.1}
\]

The total contribution of the error in (3.1) to every first-order detector is
exponentially smaller than any negative power of `X`.

### Proof

The factor `V(z_j,Y_j)` is independent of `m`, and

\[
\log(P_j+m)-\log P_j
=\log(1+m/P_j)
=O(H/P_j).
\]

Since `P_j=\exp((1+o(1))X)` while `H` is polynomial in `X`, the claimed aggregate
error follows even after summing over all physical offsets and moduli.  \(\square\)

The candidate sets for two indices in one block differ by at most `K` prime
offsets.  The modulus sets differ by at most `K` primes.

### Lemma 3.2 (one-offset cost)

For a fixed candidate prime offset `m`,

\[
\left|
 b_{j,m}
 \sum_{z_j<r\le H}\xi_r(P_j+m)
\right|
\ll X.
\tag{3.2}
\]

### Proof

The baseline satisfies

\[
\sum_{X<r\le H}\frac1{r-2}\ll1.
\]

Every active hit prime divides `P_j+m` and exceeds `X`, so their number is at most

\[
\frac{\log(P_j+H)}{\log X}\ll\frac X{\log X}.
\]

Since `|b_{j,m}|\ll\log X`, (3.2) follows.  \(\square\)

### Lemma 3.3 (one-modulus cost)

Uniformly for `z_j<r<=H`, the full locally centred contribution of one modulus is

\[
\ll X.
\tag{3.3}
\]

### Proof

For `r<=H/2`, Brun--Titchmarsh gives at most

\[
\ll \frac{H}{r\log(H/r)}
\]

candidate prime hits.  After multiplication by `|b_{j,m}|\ll\log X`, this is
`O(X)` uniformly for `r>X`.  The centred baseline is also `O(H/r)=O(X)`.
For `r>H/2`, there are at most two physical integers in the residue class and the
same conclusion follows trivially.  \(\square\)

Define `\widetilde G_j^{(1)}` by replacing the candidate set by `\mathcal M_B`,
the modulus set by `\mathcal R_B`, and `b_{j,m}` by `\beta_j`.

### Theorem 3.4 (mesoscopic freezing)

For every block `B`,

\[
\boxed{
|G_j^{(1)}-\widetilde G_j^{(1)}|
\ll KX
}
\tag{3.4}
\]

uniformly for `j in B`, apart from an exponentially negligible error.  Consequently,

\[
\boxed{
\sum_{j<N}|G_j^{(1)}-\widetilde G_j^{(1)}|^2
\ll NK^2X^2
\ll NHX.
}
\tag{3.5}
\]

### Proof

There are at most `K` deleted offsets and at most `K` deleted moduli.  Apply
Lemmas 3.2 and 3.3.  The last inequality uses `K^2 ll H/X`.  \(\square\)

Thus moving cutoffs and candidate weights may be frozen on `sqrt(X)`-centre blocks
without consuming more than the existing Fortune variance budget.

## 4. Mesoscopic orbit kernel

For a block `B` and any prime set `\mathcal R subseteq \mathcal R_B`, define

\[
\Phi_j(r,a)=\frac1r e(aP_j/r),
\qquad
r\in\mathcal R,
\quad 1\le a<r.
\tag{4.1}
\]

Its centre Gram kernel is

\[
\mathcal K_{jk}
=
\sum_{r\in\mathcal R}\frac1{r^2}
\sum_{a=1}^{r-1}e(a(P_j-P_k)/r).
\tag{4.2}
\]

Complete additive orthogonality gives exactly

\[
\boxed{
\mathcal K_{jk}
=-\sum_{r\in\mathcal R}\frac1{r^2}
+
\sum_{r\in\mathcal R\atop r\mid P_j-P_k}\frac1r
\quad(j\ne k),
}
\tag{4.3}
\]

and

\[
\mathcal K_{jj}
=
\sum_{r\in\mathcal R}\frac{r-1}{r^2}.
\tag{4.4}
\]

## 5. Primorial collision count

If `j<k` are in one block and `r>z_B`, then `r` is coprime to `P_j`, and (1.1)
gives

\[
\boxed{
 r\mid P_k-P_j
\iff
 r\mid\prod_{j<u\le k}z_u-1.
}
\tag{5.1}
\]

Put `h=k-j`.  The integer on the right of (5.1) is smaller than `(2X)^h`.
Therefore it has at most

\[
\frac{h\log(2X)}{\log X}\ll h
\]

prime divisors exceeding `X`.  Hence

\[
\boxed{
\sum_{r\in\mathcal R\atop r\mid P_k-P_j}\frac1r
\ll\frac hX.
}
\tag{5.2}
\]

Also

\[
\sum_{r>X}\frac1{r^2}\ll\frac1{X\log X},
\qquad
\sum_{X<r\le H}\frac1r\ll1.
\tag{5.3}
\]

## 6. Bounded mesoscopic orbit frame

### Theorem 6.1

For every block `B` of size at most `K`,

\[
\boxed{
\|\mathcal K\|_{\rm op}
\ll
1+\frac{K^2}{X}+rac{K}{X\log X}.
}
\tag{6.1}
\]

In particular, if `K ll sqrt(X)`, then

\[
\|\mathcal K\|_{\rm op}\ll1.
\tag{6.2}
\]

Equivalently, for arbitrary complex coefficients `c_{r,a}`,

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{r\in\mathcal R}\sum_{a=1}^{r-1}
\frac{c_{r,a}}r e(aP_j/r)
\right|^2
\ll
\sum_{r,a}|c_{r,a}|^2.
}
\tag{6.3}
\]

### Proof

Use (4.3)--(4.4), (5.2)--(5.3), and the Schur row-sum bound.  For one row,

\[
\sum_{k\ne j}\frac{|k-j|}{X}
\ll\frac{K^2}{X}.
\]

The dense `-sum 1/r^2` term contributes `O(K/(X log X))`, and the diagonal is
`O(1)`.  The synthesis inequality (6.3) is the corresponding Hilbert-space
operator bound.  \(\square\)

This removes the full-block collision factor from the primorial orbit.  At the
mesoscopic scale, the orbit itself is already a bounded frame.

## 7. Why the theorem does not yet close the source

The frozen first-order Fourier term contains

\[
T_{B,r}(a)
=
\sum_{m\in\mathcal M_B}e(am/r).
\tag{7.1}
\]

Inserting `c_{r,a} roughly T_{B,r}(a)` into (6.3) separates the orbit and source
norms.  This is too expensive.  Parseval gives

\[
\sum_{a\bmod r}|T_{B,r}(a)|^2
=
r\sum_{c\bmod r}\nu_{B,r}(c)^2,
\tag{7.2}
\]

where `nu_{B,r}(c)` is the number of candidate primes in the residue class `c`.
Even the unavoidable singleton contribution has size `r|mathcal M_B|`.  Summing
this separated source norm over the physical modulus range is far above `HX`.

More generally, redistributing a scalar weight between the source coefficient and
the orbit row cannot solve the problem.  If positive weights `w_r` are used, the
product of the two separated diagonal budgets contains

\[
\left(\sum_r r w_r^2\right)
\left(\sum_r\frac1{r w_r^2}\right)
\ge (\#\mathcal R)^2
\tag{7.3}
\]

by Cauchy--Schwarz.

### Proposition 7.1 (factorised-frame no-go)

No argument which first bounds a source Fourier norm independently of the
primorial orbit norm can reach the Fortune scale throughout `X<r<=H`.  The
load-bearing estimate must preserve the joint phases

\[
e\!\left(\frac{a(P_j+m)}r-\frac{b(P_j+n)}s\right)
\]

until after source and orbit averaging have been combined.

The mesoscopic theorem therefore removes the orbit-collision obstruction but
leaves the genuinely bilinear source--orbit dispersion problem.

## 8. Revised target

By Theorem 3.4, it suffices to establish on every block `B`

\[
\boxed{
\sum_{j\in B}|\widetilde G_j^{(1)}|^2
\ll K H X\,L_1(X),
\qquad L_1(X)=o(\log X),
}
\tag{8.1}
\]

and then to reinsert the normalized rough coordinate and ordered Buchstab tail
with their exact covariance.

The advantage is precise:

1. the moving source and modulus cutoffs are gone;
2. the candidate weights are row scalars;
3. the primorial orbit Gram has bounded operator norm;
4. only a common-source bilinear dispersion theorem remains inside each block.

## 9. Boundary

Proved unconditionally:

1. weight and cutoff freezing at cost `O(NHX)`;
2. exact mesoscopic orbit kernel;
3. collision bound (5.2);
4. bounded orbit frame (6.1)--(6.3);
5. factorised-frame no-go (7.3).

Computationally supported:

1. first-order dyadic modulus ranges have small mixed-sign covariance through
   `X=503`;
2. the aggregate cross-range covariance is much smaller than the diagonal in the
   largest tested block.

Open:

1. common-source mesoscopic bilinear estimate (8.1);
2. its covariance with the rough coordinate and Buchstab tail;
3. Fortune's conjecture.
