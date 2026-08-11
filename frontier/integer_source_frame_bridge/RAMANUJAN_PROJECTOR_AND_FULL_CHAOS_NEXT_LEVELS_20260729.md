# Ramanujan projector and full-chaos next levels

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the projector, coefficient identities, interval representation, band telescope and complete-residue orthogonality below are **PROVED EXACTLY**. The finite panels are **COMPUTATIONALLY VERIFIED** or **EMPIRICAL** as labelled. The deterministic sampling theorems `JIRP(X)` and `BMST(X)`, the Fortune variance theorem and Fortune's conjecture are **OPEN**.

## 1. Purpose

The preceding same-band audit isolated the signed common-source covariance theorem `SBD(X)` and identified a barrier for a *termwise Möbius--sawtooth truncation*: after the signs are discarded, the divisor count is

\[
\tau(P)=2^{\pi(z)}.
\]

That barrier is valid for the termwise truncation route, but it is not the end of every signed-divisor formulation. The exact Ramanujan projector packages the complete smooth-divisor cancellation before any interval estimate. It replaces the raw divisor count by coefficient identities of total mass one.

This document executes the next two levels:

1. replace the termwise sawtooth expansion by an exact incomplete Ramanujan-projector system and identify its remaining theorem;
2. reinsert the complete Euler--Buchstab detector as exact dyadic martingale increments and identify the final deterministic sampling theorem.

Neither level proves Fortune. Both sharpen the remaining mathematical obligation.

## 2. Exact Ramanujan roughness projector

Let

\[
P=\prod_{p\le z}p,
\qquad
\delta_P=\frac{\varphi(P)}P,
\]

and let

\[
c_d(k)=\sum_{a\bmod d\atop(a,d)=1}e(ak/d)
\]

be the Ramanujan sum. For every divisor `d|P`, put

\[
\lambda_P(d)=\delta_P\frac{\mu(d)}{\varphi(d)}.
\tag{2.1}
\]

### Theorem 2.1 — exact quotient roughness projector

For every integer `k`,

\[
\boxed{
\mathbf 1_{(k,P)=1}
=
\sum_{d\mid P}\lambda_P(d)c_d(k).
}
\tag{2.2}
\]

### Proof

Both sides are multiplicative in the squarefree modulus `P`. At a prime `p|P`,

\[
\left(1-\frac1p\right)
\left(1-\frac{c_p(k)}{p-1}\right)
=
\begin{cases}
0,&p\mid k,\\
1,&p\nmid k,
\end{cases}
\]

because `c_p(k)=p-1` when `p|k` and `c_p(k)=-1` otherwise. Multiplication over `p|P` gives (2.2). \(\square\)

This is the quotient-side version of the established candidate projector. It must be applied before taking absolute values in the divisor variable.

## 3. Exact coefficient and complete-period energy identities

### Theorem 3.1 — no exponential coefficient loss

The coefficients (2.1) satisfy

\[
\boxed{
\sum_{d\mid P}|\lambda_P(d)|=1.
}
\tag{3.1}
\]

Moreover,

\[
\boxed{
\sum_{d\mid P}|\lambda_P(d)|^2\varphi(d)=\delta_P,
}
\tag{3.2}
\]

and

\[
\boxed{
\sum_{d\mid P\atop d>1}|\lambda_P(d)|^2\varphi(d)
=
\delta_P(1-\delta_P).
}
\tag{3.3}
\]

### Proof

Since `P` is squarefree,

\[
\sum_{d\mid P}\frac1{\varphi(d)}
=
\prod_{p\mid P}\left(1+\frac1{p-1}\right)
=
\frac P{\varphi(P)}.
\]

Multiplying by `delta_P` proves (3.1), and multiplying by `delta_P^2` proves (3.2). The `d=1` term in (3.2) is `delta_P^2`, giving (3.3). \(\square\)

The complete-period Ramanujan orthogonality relation is

\[
\boxed{
\frac1P\sum_{k\bmod P}c_d(k)c_e(k)
=
\mathbf1_{d=e}\varphi(d),
\qquad d,e\mid P.
}
\tag{3.4}
\]

Consequently, (3.3) is exactly the variance of the roughness indicator over a complete period:

\[
\frac1P\sum_{k\bmod P}
\left(\mathbf1_{(k,P)=1}-\delta_P\right)^2
=
\delta_P(1-\delta_P).
\tag{3.5}
\]

Thus the complete projector has finite natural energy. The exponential loss in the earlier audit belongs specifically to a termwise Möbius--sawtooth truncation after absolute values; it is not intrinsic to the exact Ramanujan projector.

## 4. Exact incomplete interval representation

For a physical prime modulus `q`, define the quotient interval

\[
I_{P,Z,H}(q)
=
\left\{k:\frac{P+Z}{q}<k\le\frac{P+H}{q}\right\},
\tag{4.1}
\]

and put

\[
C_d(I)=\sum_{k\in I}c_d(k).
\tag{4.2}
\]

### Theorem 4.1 — incomplete Ramanujan representation

The corrected rough-quotient count satisfies exactly

\[
\boxed{
N_{P,Z}(q)
=
\sum_{d\mid P}\lambda_P(d)C_d(I_{P,Z,H}(q)).
}
\tag{4.3}
\]

### Proof

Sum (2.2) over the integers in (4.1). By the quotient bijection, that sum is precisely `N_{P,Z}(q)`. \(\square\)

Writing `|I_q|` for the interval cardinality and `M_Z` for the number of candidate primes in `(Z,H]`, the locally centred discrepancy becomes

\[
\boxed{
D_P(q)
=
A_P(q)
+
\sum_{d\mid P\atop d>1}\lambda_P(d)C_d(I_q),
}
\tag{4.4}
\]

where

\[
A_P(q)
=
\delta_P|I_q|-\frac{M_Z-1}{q-1}.
\tag{4.5}
\]

## 5. The density-cancellation boundary

Formula (4.4) cannot be estimated by bounding `A_P(q)` and the nontrivial Ramanujan spectrum separately.

Indeed, on non-endpoint physical ranges,

\[
\delta_P|I_q|
\sim
\frac{e^{-\gamma}H}{q\log X},
\qquad
\frac{M_Z-1}{q-1}
\sim
\frac{H}{2q\log X}.
\tag{5.1}
\]

The difference has main scale

\[
\left(e^{-\gamma}-\frac12\right)\frac{H}{q\log X},
\tag{5.2}
\]

not an admissible negligible error. The nontrivial Ramanujan part in (4.4) must cancel this deterministic drift in aggregate. Therefore the projector removes the coefficient explosion but does not permit a triangle-inequality proof.

This is the same structural warning already seen in the full Euler system: cancellation must be retained across components carrying main-size terms.

## 6. Level-one theorem after the projector

For one mesoscopic centre block `B` and one physical dyadic band `\mathcal Q_R`, define

\[
\mathcal R_{j,q}
=
A_{P_j}(q)
+
\sum_{d\mid P_j\atop d>1}
\lambda_{P_j}(d)C_d(I_{P_j,Z,H}(q)).
\tag{6.1}
\]

By (4.4), `\mathcal R_{j,q}=D_j(q)` exactly. Thus the following theorem is equivalent in target strength to `SBD(X)`, but exposes the signed smooth-divisor cancellation in a finite-energy basis.

### Open theorem `JIRP(X)` — joint incomplete Ramanujan projector

Uniformly for every mesoscopic block `B` with `|B|=K\ll\sqrt X` and every physical dyadic prime band `R<q\le2R`, prove

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{q\in\mathcal Q_R}
\frac{q-1}{q-2}\,\mathcal R_{j,q}
\right|^2
\ll
\sum_{j\in B}\sum_{q\in\mathcal Q_R}
\left|
\frac{q-1}{q-2}\,\mathcal R_{j,q}
\right|^2
+E_{B,R},
}
\tag{6.2}
\]

with dyadically summable errors at the Fortune scale.

The theorem must use jointly:

1. the coefficient identities (3.1)--(3.3);
2. incomplete Ramanujan sums on the moving intervals (4.1);
3. the consecutive-primorial centre average;
4. cancellation between (4.5) and the `d>1` spectrum.

Complete-period orthogonality alone does not prove (6.2), because `|I_q|\asymp H/q` ranges from order `X` down to order one while the period `P_j` is exponential.

## 7. Current Kloosterman technology does not close `JIRP(X)`

Recent 2026 results strengthen bilinear forms with Kloosterman sums and fractions, including Blomer--Pascadi (`arXiv:2607.24311`), Dong--Robles--Zeindler (`arXiv:2601.00292`) and Wright (`arXiv:2604.25177`). Their coefficient geometries involve fixed moduli or long dyadic bilinear/trilinear convolutions. The present system instead has:

1. divisors constrained by `d|P_j`;
2. a modulus-dependent primorial numerator;
3. microscopic moving intervals `I_{P_j,Z,H}(q)`;
4. mandatory cancellation between the density coordinate and the nontrivial projector;
5. a one-point top range and exact Euler-tail recombination.

Accordingly, no direct black-box implication to (6.2) has been identified. This is an applicability statement, not a no-go theorem for future Kloosterman methods.

## 8. Exact full-detector band martingale

Order the new primes `z<r\le Y` and define

\[
M_t(n)=\prod_{i\le t}(1+\xi_{r_i}(n)),
\qquad M_0(n)=1.
\tag{8.1}
\]

Then

\[
M_t(n)-M_{t-1}(n)
=
M_{t-1}(n)\xi_{r_t}(n).
\tag{8.2}
\]

### Theorem 8.1 — exact ordered telescope

\[
\boxed{
\prod_{z<r\le Y}(1+\xi_r(n))-1
=
\sum_{z<r\le Y}
\xi_r(n)
\prod_{z<s<r}(1+\xi_s(n)).
}
\tag{8.3}
\]

This is a finite algebraic telescope. Each increment carries the complete previous Euler history, so factor-cluster cancellation is retained.

Now partition the new primes into ordered dyadic bands `\mathcal R_1,...,\mathcal R_L`. Put

\[
M_\ell(n)=\prod_{r\in\mathcal R_1\cup\cdots\cup\mathcal R_\ell}(1+\xi_r(n))
\]

and

\[
B_\ell(n)
=
M_{\ell-1}(n)
\left(
\prod_{r\in\mathcal R_\ell}(1+\xi_r(n))-1
\right).
\tag{8.4}
\]

### Corollary 8.2 — exact band telescope

\[
\boxed{
\prod_{z<r\le Y}(1+\xi_r(n))-1
=
\sum_{\ell=1}^{L}B_\ell(n).
}
\tag{8.5}
\]

The physical single-prime, tail-prime and higher-order terms are now parts of the same band increments rather than independently bounded layers.

## 9. Exact complete-residue martingale orthogonality

Use the product measure in which the candidate offset is uniform over the nonzero residue classes modulo every new prime. The local centring identity gives

\[
\mathbb E\xi_r=0,
\qquad
\mathbb E(1+\xi_r)=1,
\tag{9.1}
\]

and direct calculation gives

\[
\mathbb E\xi_r^2=\frac1{r-2},
\qquad
\mathbb E(1+\xi_r)^2=\frac{r-1}{r-2}.
\tag{9.2}
\]

### Theorem 9.1 — model band orthogonality

For `\ell<m`,

\[
\boxed{
\mathbb E B_\ell=0,
\qquad
\mathbb E(B_\ell B_m)=0.
}
\tag{9.3}
\]

Consequently,

\[
\boxed{
\mathbb E\left|
\prod_{z<r\le Y}(1+\xi_r)-1
\right|^2
=
\sum_{\ell=1}^{L}\mathbb E|B_\ell|^2.
}
\tag{9.4}
\]

### Proof

The residue coordinates at distinct primes are independent under the complete CRT product measure. Each later band factor in (8.4) has conditional mean zero by (9.1), while `M_{\ell-1}` is measurable with respect to earlier bands. This proves (9.3); expanding the square of (8.5) gives (9.4). \(\square\)

This is exact orthogonality in the local model. The actual source consists of prime offsets sampled along prescribed primorial centres, so transferring (9.3) to that deterministic sample is the new theorem, not a consequence of CRT alone.

## 10. Level-two theorem after full reinsertion

For each centre `P_j`, let

\[
\mathcal E_j^{\rm full}
=
\sum_{z_j<m\le H\atop m\ {\rm prime}}
\log(P_j+m)\mathbf1_{P_j+m\ {\rm prime}}
-
\mu_{P_j}^{\rm prim}.
\tag{10.1}
\]

By the exact Euler detector and (8.5), this residual has an exact representation through the zeroth coordinate and the weighted band increments `B_{j,\ell}(P_j+m)`.

### Open theorem `BMST(X)` — Buchstab-martingale sampling transfer

For every mesoscopic block `B` of consecutive primorial centres, prove

\[
\boxed{
\sum_{j\in B}|\mathcal E_j^{\rm full}|^2
\ll
KHX\,L(X),
\qquad L(X)=o(\log X),
}
\tag{10.2}
\]

by transferring the band-martingale cancellation (9.3)--(9.4) to the deterministic candidate-prime/primorial sample, while preserving:

1. exact local centring;
2. the logarithmic Euler normalization;
3. physical same-band rough-quotient dispersion;
4. tail and higher-order factor-cluster cancellation;
5. mesoscopic primorial-orbit rigidity.

Summing (10.2) over blocks is the full Fortune variance target already established in the merged programme. Thus `BMST(X)` is the second and final analytic level after the exact reductions; it is not yet proved.

## 11. Finite diagnostics

The companion verifier proves in exact rational arithmetic on complete finite panels:

1. projector identity (2.2);
2. coefficient identities (3.1)--(3.3);
3. complete-period orthogonality (3.4);
4. interval representation (4.3);
5. band telescope (8.5);
6. complete-residue band orthogonality and quadratic variation (9.3)--(9.4).

It also computes small full-chaos Fortune panels at `X=7,11,13,17`. The complete-to-physical block energy ratios range from approximately `0.024` to `37.117`, and the three pairwise covariance terms occur with both signs. These values are **EMPIRICAL ONLY**. They establish no asymptotic trend, but they decisively reject any claim that reinserting the tail and higher chaos is a monotone `L^2` contraction.

## 12. Revised boundary

**PROVED EXACTLY**

1. the quotient Ramanujan projector;
2. unit coefficient `l1` mass and finite weighted quadratic mass;
3. exact incomplete interval representation;
4. exact ordered and dyadic Euler-band telescopes;
5. exact complete-CRT martingale orthogonality.

**CORRECTED**

The exponential `2^{pi(z)}` loss is a barrier to termwise Möbius--sawtooth truncation after signs are discarded. It is not a barrier to the exact Ramanujan projector, whose coefficients have total absolute mass one. The earlier broader reading is superseded by Sections 2--5 above.

**OPEN**

1. `JIRP(X)`, equivalently the signed physical same-band sampling theorem in the Ramanujan basis;
2. `BMST(X)`, the deterministic full-detector martingale transfer;
3. the Fortune variance theorem and Fortune's conjecture.

The first level now has a finite-energy basis but lacks incomplete-interval sampling. The second level has exact full-chaos reinsertion but lacks deterministic martingale orthogonality. No further algebraic or bookkeeping step is being mistaken for the missing analytic theorem.
