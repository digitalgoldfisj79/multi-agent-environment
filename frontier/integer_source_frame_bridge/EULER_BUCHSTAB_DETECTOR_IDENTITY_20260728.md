# Euler--Buchstab detector identity

Date: 28 July 2026  
Status: exact prime-output identity and natural logarithmic normalization proved; first-order and higher-order covariance estimates open.

## 1. Candidate range

Let

\[
P=\prod_{r\le z}r
\]

be a primorial centre, let `z^+` be the next prime after `z`, and choose

\[
z<H<(z^+)^2.
\tag{1.1}
\]

Put

\[
Y=\sqrt{P+H}
\]

and let

\[
\mathcal P_z(H)=\{m:z<m\le H,\ m\text{ prime}\}.
\]

For every `m in mathcal P_z(H)`,

\[
\gcd(P+m,P)=1.
\tag{1.2}
\]

Hence every prime divisor of `P+m` exceeds `z`.

## 2. Locally centred prime-avoidance coordinate

For each prime `r` with `z<r<=Y`, define

\[
\boxed{
\xi_r(n)
=
\frac1{r-2}
-
\frac{r-1}{r-2}\mathbf1_{r\mid n}.
}
\tag{2.1}
\]

Then

\[
\boxed{
1+\xi_r(n)
=
\frac{r-1}{r-2}\mathbf1_{r\nmid n}.
}
\tag{2.2}
\]

The coordinate is exactly centred over nonzero offset residues.  If `P` is
nonzero modulo `r`, then as `m` ranges over `mathbb F_r^*`, the values
`P+m` contain zero once and a nonzero residue `r-2` times.  Therefore

\[
\frac1{r-1}\sum_{m\in\mathbb F_r^*}\xi_r(P+m)=0.
\tag{2.3}
\]

This is the correct local centring after the candidate-prime projector has removed
the zero residue for the offset.

## 3. Exact Euler detector

Define

\[
\boxed{
V(z,Y)
=
\prod_{z<r\le Y\atop r\text{ prime}}
\frac{r-2}{r-1}.
}
\tag{3.1}
\]

### Theorem 3.1

For every `m in mathcal P_z(H)`,

\[
\boxed{
\mathbf1_{P+m\text{ prime}}
=
V(z,Y)
\prod_{z<r\le Y\atop r\text{ prime}}
\bigl(1+\xi_r(P+m)\bigr).
}
\tag{3.2}
\]

### Proof

By (2.2), the right side is one if no prime `r` in `(z,Y]` divides `P+m`,
and zero otherwise.  Every prime divisor of `P+m` exceeds `z` by (1.2).  If
`P+m` is composite, its least prime factor is at most

\[
\sqrt{P+m}\le Y,
\]

so one factor in the product vanishes.  If `P+m` is prime, no factor vanishes,
and the product of `(r-1)/(r-2)` cancels `V(z,Y)` exactly.  \(\square\)

No proper-prime-power correction is required: every composite prime power has a
prime divisor at most its square root and is killed by the product.

## 4. Exact weighted prime-output detector

For deterministic weights `u_m`, define

\[
\mathcal D_P(u)
=
\sum_{m\in\mathcal P_z(H)}
 u_m\mathbf1_{P+m\text{ prime}}.
\]

### Corollary 4.1

One has exactly

\[
\boxed{
\mathcal D_P(u)
=
\sum_{m\in\mathcal P_z(H)}
 b_{P,m}
\prod_{z<r\le Y}(1+\xi_r(P+m)),
}
\tag{4.1}
\]

where

\[
\boxed{
b_{P,m}=u_mV(z,Y).}
\tag{4.2}
\]

For the shifted von Mangoldt prime-output detector take

\[
u_m=\log(P+m).
\tag{4.3}
\]

Then

\[
\mathcal D_P(\log(P+\cdot))
=
\sum_{z<m\le H\atop m\text{ prime}}
\log(P+m)\mathbf1_{P+m\text{ prime}}.
\tag{4.4}
\]

This differs from the original one-sided von Mangoldt source only by proper prime
powers and noncandidate offsets, both already bounded by `o(H)` in the corrected
detector programme.

## 5. Natural logarithmic normalization

The local product factors as

\[
\frac{r-2}{r-1}
=
\left(1-\frac1r\right)
\left(1-\frac1{(r-1)^2}\right).
\tag{5.1}
\]

Therefore

\[
V(z,Y)
=
\prod_{z<r\le Y}\left(1-\frac1r\right)
\prod_{z<r\le Y}\left(1-\frac1{(r-1)^2}\right).
\tag{5.2}
\]

The second product is `1+O(1/z)`.  Mertens' product theorem gives

\[
\prod_{z<r\le Y}\left(1-\frac1r\right)
=
\frac{\log z}{\log Y}(1+o(1)).
\tag{5.3}
\]

Since

\[
\log P=(1+o(1))z,
\qquad
\log Y=\frac12\log P+o(1),
\]

we obtain

\[
\boxed{
V(z,Y)
=
\left(2+o(1)\right)\frac{\log z}{z}.
}
\tag{5.4}
\]

For the weight (4.3), uniformly over the physical interval,

\[
\boxed{
 b_{P,m}
=
\log(P+m)V(z,Y)
=
(2+o(1))\log z.
}
\tag{5.5}
\]

In particular,

\[
|b_{P,m}|\ll\log X
\tag{5.6}
\]

uniformly in a dyadic Fortune block.  This is the key normalization gain: the
exact prime-output detector has logarithmic per-candidate weights, not weights of
size `log P asymp X`.

## 6. Exact chaos expansion

Expanding the finite Euler product in (4.1) gives

\[
\boxed{
\mathcal D_P(u)
=
\mathcal Z_P(u)
+
\mathcal F_P^{(1)}(u)
+
\mathcal F_P^{(\ge2)}(u),
}
\tag{6.1}
\]

where

\[
\mathcal Z_P(u)
=
\sum_{m\in\mathcal P_z(H)}b_{P,m},
\tag{6.2}
\]

\[
\mathcal F_P^{(1)}(u)
=
\sum_{z<r\le Y}
\sum_{m\in\mathcal P_z(H)}
 b_{P,m}\xi_r(P+m),
\tag{6.3}
\]

and

\[
\mathcal F_P^{(\ge2)}(u)
=
\sum_{k\ge2}
\sum_{z<r_1<\cdots<r_k\le Y}
\sum_{m\in\mathcal P_z(H)}
 b_{P,m}
\prod_{i=1}^k\xi_{r_i}(P+m).
\tag{6.4}
\]

The zeroth term has scale `H`:

\[
\mathcal Z_P(\log(P+\cdot))
=(1+o(1))H.
\tag{6.5}
\]

The complete detector has Hardy--Littlewood local scale
`(e^gamma/2+o(1))H`; the difference is carried by coherent nonzero chaos terms.
Thus neither the first-order nor higher-order term may be treated as a separately
positive error.

## 7. Physical and sparse ranges

Split every local prime at `r=H`:

\[
\mathcal F_P^{(1)}
=
\mathcal F_{P,\le H}^{(1)}
+
\mathcal F_{P,>H}^{(1)}.
\tag{7.1}
\]

For `r<=H`, a residue class can contain a physical progression of candidate
offsets.  This is the prime-modulus dispersion range.

For `r>H`, a fixed pair `(P,r)` selects at most one physical offset.  Every chaos
monomial containing at least two new primes has modulus greater than

\[
(z^+)^2>H,
\]

and is therefore a one-point column in the offset variable.  Across centres, the
primorial shrinking-target theorem applies to the resulting exponential-scale
columns.

The exact architecture is consequently:

1. a first-order prime-modulus frame in `z<r<=H`;
2. a sparse first-order tail in `H<r<=Y`;
3. sparse higher-order Euler chaos;
4. signed covariance among all three.

## 8. Correct next theorem

The next load-bearing estimate is not a positive bound for any one chaos level.
It is a centred block second moment for

\[
\mathcal Z_{P_j}
+
\mathcal F_{P_j}^{(1)}
+
\mathcal F_{P_j}^{(\ge2)}
-
\mu_{P_j}^{\mathrm{prim}},
\tag{8.1}
\]

where `mu_P^prim` is the exact smooth-primitive principal term already derived.

The first subproblem is to prove or refute a Fortune-scale Gram estimate for the
locally centred physical first-order term.  The sparse terms must then be
reinserted through their cross covariance.

## 9. Boundary

Proved exactly:

1. local coordinate (2.1)--(2.3);
2. Euler detector (3.2);
3. weighted detector (4.1);
4. finite chaos expansion (6.1)--(6.4);
5. physical/sparse classification.

Proved from classical published input:

1. logarithmic normalization (5.4)--(5.6);
2. zeroth-term scale (6.5).

Open:

1. the first-order prime-modulus Gram estimate;
2. the joint first-order/sparse covariance theorem;
3. the Fortune variance theorem and Fortune's conjecture.
