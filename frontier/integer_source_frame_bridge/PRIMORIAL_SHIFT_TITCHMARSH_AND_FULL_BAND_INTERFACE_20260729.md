# Primorial-shift Titchmarsh compression and the all-order first-band interface

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the corrected first-band same-band coordinate has been compressed exactly to a weighted truncated Titchmarsh divisor sum over the shifted primes `P_j+m`. Recombining all Euler orders in the first physical band has also been carried out exactly. Every Euler order at least two enters the one-point regime because the product of two first-band primes exceeds the source length `H`. This exposes a semiprime shrinking-target interface, but does not prove the required signed covariance. Existing uniform large-modulus and Titchmarsh theorems do not cover the simultaneous prime-modulus, exponentially large-shift and microscopic-window geometry. Fortune's conjecture remains **OPEN**.

## 1. Setup

Let `B` be a frozen mesoscopic block with common cutoff `Z`, prime source

\[
\mathcal M_Z=\{m:Z<m\le H,\ m\ \mathrm{prime}\},
\qquad M_Z=|\mathcal M_Z|,
\]

and first physical dyadic band

\[
\mathcal P_R=\{p: R<p\le 2R,\ p\ \mathrm{prime}\},
\qquad R\asymp X.
\]

Put

\[
w_p=\frac{p-1}{p-2},
\qquad
\lambda_R=\sum_{p\in\mathcal P_R}\frac1{p-2}.
\]

The frozen same-band coordinate is

\[
T_{B,R}(j)
=
\beta_j
\sum_{p\in\mathcal P_R}
w_p
\left(
N_{P_j,Z}(p)-\frac{M_Z-1}{p-1}
\right),
\tag{1.1}
\]

where

\[
N_{P_j,Z}(p)
=
\#\{m\in\mathcal M_Z:m\ne p,\ p\mid P_j+m\}.
\tag{1.2}
\]

Since every band prime exceeds the primes entering `P_j`, one has `p\nmid P_j`. Therefore the omitted self source `m=p` never satisfies `p\mid P_j+p`.

## 2. Exact primorial-shift Titchmarsh compression

Define the weighted truncated prime-divisor function

\[
\omega_R^\ast(n)
=
\sum_{\substack{p\in\mathcal P_R\\p\mid n}}w_p.
\tag{2.1}
\]

### Theorem 2.1 — exact Titchmarsh form

For every frozen centre,

\[
\boxed{
\frac{T_{B,R}(j)}{\beta_j}
=
\sum_{m\in\mathcal M_Z}\omega_R^\ast(P_j+m)
-
(M_Z-1)\lambda_R.
}
\tag{2.2}
\]

### Proof

Interchange the source and modulus sums in (1.1). The self source can be restored inside the hit count because `p\nmid P_j+p`. Also

\[
w_p\frac1{p-1}=\frac1{p-2}.
\]

Hence

\[
\begin{aligned}
\frac{T_{B,R}(j)}{\beta_j}
&=
\sum_{p\in\mathcal P_R}
w_p
\sum_{m\in\mathcal M_Z}
\mathbf 1_{p\mid P_j+m}
-
(M_Z-1)\sum_{p\in\mathcal P_R}\frac1{p-2}\\
&=
\sum_{m\in\mathcal M_Z}
\omega_R^\ast(P_j+m)
-
(M_Z-1)\lambda_R.
\end{aligned}
\]

\(\square\)

Thus `MRPMD(X)` / `SBD(X)` is exactly a mean-square theorem for a centred truncated divisor sum over primes shifted by the primorial `P_j`. It is a Titchmarsh-type problem, but in the extreme regime

\[
m\le H\asymp X^2,
\qquad
P_j=\exp((1+o(1))X).
\tag{2.3}
\]

The shift is exponentially larger than the prime variable.

## 3. Relation to the exact first-order Euler coordinate

For a physical integer `n`, put

\[
\xi_p(n)
=
\frac1{p-2}
-
w_p\mathbf 1_{p\mid n}.
\tag{3.1}
\]

This is `-1` on a hit and `1/(p-2)` otherwise. Define the complete first-order source sum

\[
\mathcal F_{j,R}
=
\beta_j
\sum_{m\in\mathcal M_Z}
\sum_{p\in\mathcal P_R}\xi_p(P_j+m).
\tag{3.2}
\]

Theorem 2.1 gives the exact self/zeroth relation

\[
\boxed{
\mathcal F_{j,R}
=
\beta_j\lambda_R-T_{B,R}(j).
}
\tag{3.3}
\]

The extra `\beta_j\lambda_R` is precisely the self/zeroth drift that was kept separate in the locally centred formulation. This is consistent with the previously proved identity `E_{j,p}=-a_{j,p}`.

## 4. Exact all-order first-band recombination

Put

\[
V_R
=
\prod_{p\in\mathcal P_R}\frac{p-2}{p-1}.
\tag{4.1}
\]

For each source prime,

\[
\prod_{p\in\mathcal P_R}(1+\xi_p(P_j+m))
=
V_R^{-1}
\mathbf 1_{(P_j+m,\prod_{p\in\mathcal P_R}p)=1}.
\tag{4.2}
\]

Let

\[
H_{j,R}
=
\#\{m\in\mathcal M_Z:
\exists p\in\mathcal P_R,\ p\mid P_j+m\}.
\tag{4.3}
\]

The full normalized-survivor band is therefore

\[
\boxed{
\mathcal U_{j,R}
=
\beta_j
\left[
V_R^{-1}(M_Z-H_{j,R})-M_Z
\right].
}
\tag{4.4}
\]

This is the exact drift/union-hit representation. It contains every Euler order in the band.

Write

\[
\mathcal C_{j,R}
=
\mathcal U_{j,R}-\mathcal F_{j,R}.
\tag{4.5}
\]

If

\[
h_{j,R}(m)
=
\#\{p\in\mathcal P_R:p\mid P_j+m\},
\tag{4.6}
\]

then

\[
\boxed{
\begin{aligned}
\frac{\mathcal C_{j,R}}{\beta_j}
={}&
\left(V_R^{-1}-1-\lambda_R\right)M_Z\\
&+
\sum_{\substack{m\in\mathcal M_Z\\h_{j,R}(m)>0}}
\left[
\sum_{\substack{p\in\mathcal P_R\\p\mid P_j+m}}w_p
-
V_R^{-1}
\right].
\end{aligned}
}
\tag{4.7}
\]

Thus the full-band alternative does not delete the first-order arithmetic. It couples it to an explicit normalization and multiple-hit correction.

## 5. Euler order two is already a one-point problem

At Fortune scale,

\[
H=\eta X^2,\qquad 0<\eta<1,
\tag{5.1}
\]

and every first-band prime satisfies `p>X`. Hence, for distinct `p,s\in\mathcal P_R`,

\[
\boxed{ps>X^2>H.}
\tag{5.2}
\]

For a squarefree product `Q` of at least two band primes, define the unique representative

\[
\rho_{j,Z}(Q)
=
Z+1+\bigl(-P_j-(Z+1)\bmod Q\bigr),
\tag{5.3}
\]

so that

\[
Z<\rho_{j,Z}(Q)\le Z+Q,
\qquad
\rho_{j,Z}(Q)\equiv-P_j\pmod Q.
\]

### Theorem 5.1 — one-point intersection formula

For every `Q` containing at least two first-band primes,

\[
\#\{m\in\mathcal M_Z:Q\mid P_j+m\}
=
\boxed{
\mathbf 1_{\rho_{j,Z}(Q)\le H}
\mathbf 1_{\rho_{j,Z}(Q)\ \mathrm{prime}}.
}
\tag{5.4}
\]

In particular, every pair intersection is either zero or one.

### Proof

The interval `(Z,H]` has length less than `Q`, so it contains at most one integer in the residue class `-P_j\bmod Q`. Formula (5.3) is that candidate. Membership in `\mathcal M_Z` is exactly the two conditions in (5.4). \(\square\)

Equivalently, using the common-base collapse, the prime test in (5.4) can be replaced by the roughness of the unique quotient

\[
k_{j,Q}=\frac{P_j+\rho_{j,Z}(Q)}Q.
\tag{5.5}
\]

Therefore every Euler order at least two is a shrinking-target one-point roughness test. The transition from physical interval statistics to one-point statistics occurs immediately at order two.

## 6. Exact inclusion-exclusion interface

For a nonempty subset `S\subseteq\mathcal P_R`, put

\[
Q_S=\prod_{p\in S}p
\]

and let

\[
I_j(S)
=
\#\{m\in\mathcal M_Z:Q_S\mid P_j+m\}.
\tag{6.1}
\]

Then

\[
H_{j,R}
=
\sum_{\varnothing\ne S\subseteq\mathcal P_R}
(-1)^{|S|+1}I_j(S).
\tag{6.2}
\]

For `|S|=1`, `I_j(S)=N_{P_j,Z}(p)`. For every `|S|\ge2`, Theorem 5.1 gives

\[
I_j(S)
=
\mathbf 1_{\rho_{j,Z}(Q_S)\in\mathcal M_Z}.
\tag{6.3}
\]

Thus the exact normalized-survivor alternative replaces the unresolved first-order covariance by an alternating interface consisting of:

1. the physical prime-modulus counts `N_{P_j,Z}(p)`;
2. semiprime and higher one-point prime/roughness tests at the residues `\rho_{j,Z}(Q_S)`;
3. the dense normalization in (4.4).

No order may be bounded positively and reinserted by triangle inequality without proving that its interface covariance is negligible.

## 7. Pair injectivity is not enough

The exact pair-incidence count is

\[
\sum_{m\in\mathcal M_Z}\binom{h_{j,R}(m)}2
=
\sum_{p<s}I_j(\{p,s\}).
\tag{7.1}
\]

The one-point property gives only

\[
\boxed{
\sum_m\binom{h_{j,R}(m)}2
\le
\binom{|\mathcal P_R|}{2}.
}
\tag{7.2}
\]

Also

\[
\sum_m(h_{j,R}(m)-1)_+
\le
\sum_m\binom{h_{j,R}(m)}2.
\tag{7.3}
\]

This information is sharp as an abstract incidence constraint: because

\[
\binom{|\mathcal P_R|}{2}
\ll
M_Z
\]

at the first-band scale, an abstract hit system can assign a distinct source to every modulus pair while respecting pair injectivity.

Using only (7.2), Mertens/PNT scale gives

\[
|\mathcal P_R|\asymp\frac X{\log X},
\qquad
M_Z\asymp\frac{X^2}{\log X},
\qquad
\beta_j\asymp\log X.
\tag{7.4}
\]

A positive estimate for the multiple-hit correction is then allowed to be as large as

\[
\beta_j\binom{|\mathcal P_R|}{2}
\asymp
\frac{X^2}{\log X},
\tag{7.5}
\]

whose square is polynomially above the Fortune row scale. Consequently:

> Pair injectivity proves the one-point geometry, but cannot by itself bound the higher-order correction at Fortune scale.

A proof needs cancellation in the alternating semiprime/higher residue system or cancellation with the physical first-order and normalization coordinates.

## 8. Applicability of current large-modulus technology

Two nearby bodies of work were checked.

### 8.1 Uniform large-modulus prime progressions

Maynard's uniform-residue theorems beyond the square-root barrier require moduli with factors in prescribed ranges. In the weakest fully uniform theorem, a modulus near `x^{1/2+\delta}` must possess a factor near `x^{1/10}`. The physical modulus in (2.2) is a prime

\[
p\asymp X\asymp H^{1/2}
\]

and has no such factorization. Introducing a smooth divisor through the roughness projector changes the modulus to `pd`, but the available factor ranges do not match the first-band prime factor `p\asymp H^{1/2}` while retaining the exact full conductor system.

### 8.2 Uniform Titchmarsh divisor problems

Assing--Blomer--Li prove strong Titchmarsh formulae uniform in shifts comparable to the prime-variable range, and their Kloosterman technology permits certain large residue parameters. Here the prime variable has length `H\asymp X^2`, while the shift is

\[
P_j=\exp((1+o(1))X)\gg H^A
\]

for every fixed `A`. The divisor is also restricted to prime factors in a microscopic band rather than the full divisor function. The present parameter regime is therefore not a specialization of their theorem.

At order two the modulus `ps` already exceeds `H`; the progression contains at most one candidate, so mean-value theorems for long prime progressions do not estimate (5.4).

These are applicability statements, not impossibility theorems for future spectral or dispersion methods.

## 9. Finite exact audit

The committed verifier checks, in rational arithmetic:

1. the Titchmarsh compression (2.2);
2. the first-order/self relation (3.3);
3. the full normalized-survivor formula (4.4);
4. the correction identity (4.7);
5. pair and higher-order one-point injectivity;
6. the exact residue candidate (5.3);
7. equality between pair prime hits and `\sum_m\binom{h_m}{2}`;
8. the first-order/full-band energy decomposition.

On the panels `X=11,17,23,29,37`, all identities pass. The same-band ratios remain bounded on those panels, but this is **EMPIRICAL ONLY**. The correction cross term changes sign, confirming that higher-order reinsertion is not a monotone positive operation.

## 10. Decisive boundary

**PROVED EXACTLY**

1. the weighted truncated Titchmarsh form (2.2);
2. the exact relation to the frozen first-order coordinate (3.3);
3. the all-order union-hit formula (4.4);
4. the explicit higher-order correction (4.7);
5. the order-two one-point transition (5.4);
6. the inclusion-exclusion interface (6.2)--(6.3);
7. the pair-injectivity bound (7.2).

**PROVED FROM CLASSICAL PRIME ESTIMATES**

1. the positive pair-injectivity scale in (7.4)--(7.5), showing that this information alone is insufficient.

**COMPUTATIONALLY VERIFIED**

1. every exact identity above on five complete panels;
2. sign-indefinite covariance between first order and the all-order correction.

**CLOSED AS DIRECT BLACK-BOX ROUTES**

1. current uniform large-modulus theorems requiring factorable moduli;
2. current uniform Titchmarsh theorems with shift comparable to the prime range;
3. positive control of the semiprime/higher one-point layer using only pair injectivity;
4. gluing first order and higher orders by triangle inequality.

**OPEN**

1. `MRPMD(X)` / `SBD(X)`, the primorial-shift truncated Titchmarsh variance;
2. a signed semiprime/higher shrinking-target theorem preserving (6.2);
3. a complete normalized-survivor transfer preserving the physical/one-point interface;
4. `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

The two nominal alternatives now meet at the same arithmetic boundary:

\[
\boxed{
\text{signed deterministic sampling of primorial-shift roughness across physical and one-point conductors}.
}
\]

Separate first-order dispersion and full-band reinsertion are different coordinate systems for this same unresolved interface.
