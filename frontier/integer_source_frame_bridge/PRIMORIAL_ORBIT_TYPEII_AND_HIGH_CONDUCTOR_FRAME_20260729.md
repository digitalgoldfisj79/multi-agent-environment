# Primorial inverse-orbit Type-II frame and high-conductor collision frame

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the next programme has been run through its exact algebraic, frame and scale gates. A new bounded inverse-orbit frame is proved after shortening mesoscopic centre blocks to `K << log X`. A second new theorem gives a small complete-model frame for every conductor containing at least two first-band primes. Neither theorem by itself closes Fortune: the inverse-orbit frame still loses a full critical Type-II factor when the second bilinear variable is separated by Cauchy, while the high-conductor frame controls model energy rather than deterministic point sampling. The remaining theorem is a joint primorial-orbit bilinear dispersion estimate, coupled to the signed one-point conductor interface. Fortune's conjecture remains **OPEN**.

## 1. Purpose

The preceding programme reduced the first physical band to the exact primorial-shift Titchmarsh discrepancy

\[
\frac{T_{B,R}(j)}{\beta_j}
=
\sum_{m\in\mathcal M_Z}\omega_R^\ast(P_j+m)
-(M_Z-1)\lambda_R.
\]

It also proved that every Euler conductor containing at least two first-band primes exceeds the physical source length `H`, so every higher intersection is a one-point shrinking-target test.

The direct Titchmarsh route and the full-survivor route therefore require a theorem that preserves simultaneously:

1. the prime-source bilinear structure;
2. the consecutive-primorial centre orbit;
3. cancellation between distinct physical prime moduli;
4. the signed physical/one-point conductor interface.

The present programme tests whether a Harman/Vaughan Type-II decomposition and a separate high-conductor orbit theorem can provide those ingredients.

## 2. Exact critical Type-II identity

Let `p` be a first-band prime. Let `\mathcal U,\mathcal V` be finite integer sets whose elements are nonzero modulo `p`, and let `\alpha_u,\gamma_v` be coefficients. Put

\[
A=\sum_u\alpha_u,
\qquad
C=\sum_v\gamma_v.
\]

Define the unit-residue Type-II discrepancy

\[
\Delta_{j,p}^{\times}(\alpha,\gamma)
=
\sum_{u,v}\alpha_u\gamma_v
\left(
\mathbf 1_{uv\equiv-P_j\pmod p}-\frac1{p-1}
\right).
\tag{2.1}
\]

It is useful first to centre additively:

\[
\Delta_{j,p}^{+}(\alpha,\gamma)
=
\sum_{u,v}\alpha_u\gamma_v
\left(
\mathbf 1_{uv\equiv-P_j\pmod p}-\frac1p
\right).
\tag{2.2}
\]

The two centres differ by the exact deterministic drift

\[
\boxed{
\Delta_{j,p}^{\times}
=
\Delta_{j,p}^{+}-\frac{AC}{p(p-1)}.
}
\tag{2.3}
\]

For

\[
\widehat\gamma_p(\ell)
=
\sum_{v\in\mathcal V}\gamma_v e(\ell v/p),
\]

additive orthogonality and the change of variable `\ell=hu` give

\[
\boxed{
\Delta_{j,p}^{+}
=
\sum_{u\in\mathcal U}\alpha_u
\frac1p\sum_{\ell=1}^{p-1}
 e(\ell P_j\overline u/p)\widehat\gamma_p(\ell).
}
\tag{2.4}
\]

This is the exact critical factorization. One Type-II variable has joined the primorial centre inside the inverse orbit

\[
(j,u)\longmapsto P_j\overline u\pmod p,
\]

while the other variable appears through one ordinary additive Fourier transform.

## 3. Combined primorial--inverse orbit frame

Assume that `\mathcal U` occupies distinct residues modulo every `p` in a dyadic prime band `\mathcal P_R`. This holds, for example, when `\mathcal U` is an interval of length less than the smallest band prime.

For `j\in B`, `u\in\mathcal U`, `p\in\mathcal P_R` and `1\le\ell<p`, define

\[
\Phi_{j,u}(p,\ell)
=
\frac1p e(\ell P_j\overline u/p).
\tag{3.1}
\]

### Theorem 3.1 -- exact inverse-orbit Gram

For a fixed `p`, the Gram kernel on row indices `(j,u)` is

\[
\boxed{
G_p((j,u),(k,u'))
=
\frac1p\mathbf 1_{P_j\overline u\equiv P_k\overline{u'}\pmod p}
-\frac1{p^2}.
}
\tag{3.2}
\]

Equivalently,

\[
P_j\overline u\equiv P_k\overline{u'}\pmod p
\iff
p\mid P_j u'-P_k u.
\tag{3.3}
\]

For each fixed centre `j`, the map `u\mapsto P_j\overline u` is injective. Hence every residue class has multiplicity at most `K=|B|` among all `(j,u)`, and

\[
\boxed{
\|G_p\|_{\rm op}\le\frac Kp.
}
\tag{3.4}
\]

#### Proof

Summing the nonzero additive frequencies gives

\[
\frac1{p^2}\sum_{\ell=1}^{p-1}e(\ell(a-b)/p)
=
\frac1p\mathbf1_{a=b}-\frac1{p^2},
\]

which proves (3.2). Multiplying by `uu'` proves (3.3). Let `B_p` be the incidence matrix from the row set `(j,u)` to the residue `P_j\overline u`. Then

\[
0\le G_p\le p^{-1}B_pB_p^\ast
\]

as quadratic forms. The nonzero eigenvalues of `B_pB_p^\ast` are the residue multiplicities, all at most `K`. This proves (3.4). `\square`

### Corollary 3.2 -- logarithmic-block frame

For arbitrary coefficients `c_{p,\ell}`,

\[
\boxed{
\sum_{j\in B}\sum_{u\in\mathcal U}
\left|
\sum_{p\in\mathcal P_R}\sum_{\ell=1}^{p-1}
 c_{p,\ell}\Phi_{j,u}(p,\ell)
\right|^2
\le
K\left(\sum_{p\in\mathcal P_R}\frac1p\right)
\sum_{p,\ell}|c_{p,\ell}|^2.
}
\tag{3.5}
\]

For `p\asymp R`, the reciprocal-prime sum is `O(1/\log R)`. Consequently

\[
K\ll\log R
\quad\Longrightarrow\quad
\|\Phi\|_{\rm synth}=O(1).
\tag{3.6}
\]

This is stronger than the earlier centre-only orbit frame in one structural respect: it absorbs one complete Type-II variable before any inequality is applied. Choosing shorter blocks is compatible with the freezing theorem, whose error only requires `K^2\ll X`.

## 4. The remaining Type-II loss

Insert

\[
c_{p,\ell}=\widehat\gamma_p(\ell)
\]

in (3.5) and then sum the row variable `u` against `\alpha_u`. Generic Cauchy gives

\[
\sum_j
\left|
\sum_u\alpha_u
\sum_{p,\ell}\widehat\gamma_p(\ell)\Phi_{j,u}(p,\ell)
\right|^2
\le
\|\alpha\|_2^2
K\left(\sum_p\frac1p\right)
\sum_{p,\ell}|\widehat\gamma_p(\ell)|^2.
\tag{4.1}
\]

If `\mathcal V` is also shorter than `p`, Parseval gives

\[
\sum_{\ell\bmod p}|\widehat\gamma_p(\ell)|^2
=p\|\gamma\|_2^2.
\tag{4.2}
\]

Therefore, for `p\asymp X`,

\[
\boxed{
\text{right side of (4.1)}
\ll
\frac{KX^2}{(\log X)^2}
\|\alpha\|_2^2\|\gamma\|_2^2.
}
\tag{4.3}
\]

At the critical Type-II scale

\[
UV\asymp H\asymp X^2,
\qquad
\|\alpha\|_2^2\|\gamma\|_2^2
=UV\,X^{o(1)},
\]

this becomes

\[
KX^{4+o(1)}/(\log X)^2.
\tag{4.4}
\]

The Fortune first-band block allowance is of order

\[
KHX/\log X
\asymp
KX^3/\log X.
\tag{4.5}
\]

Thus the exact inverse-orbit frame removes the modulus-count and centre-orbit losses, but a subsequent Cauchy inequality in the remaining Type-II variable is still larger than the required scale by

\[
\boxed{X^{1-o(1)}/\log X.}
\tag{4.6}
\]

This is the new location of the physical-band wall. It is a bilinear contraction problem, not a centre-frame problem.

## 5. High-conductor candidate frame

Let `\mathcal Q_R^{\ge2}` be the squarefree products of at least two first-band primes. Since every band prime exceeds `X>\sqrt H`, every `Q\in\mathcal Q_R^{\ge2}` satisfies `Q>H`.

Define the unique representative

\[
\rho_{j,Z}(Q)
=
Z+1+\bigl(-P_j-(Z+1)\bmod Q\bigr).
\tag{5.1}
\]

Put

\[
w(Q)=\frac1{\varphi^\dagger(Q)},
\qquad
\varphi^\dagger(Q)=\prod_{p\mid Q}(p-2),
\]

and define the weighted candidate Gram

\[
\mathcal H_{jk}
=
\sum_{Q\in\mathcal Q_R^{\ge2}}
 w(Q)\mathbf1_{\rho_{j,Z}(Q)=\rho_{k,Z}(Q)}.
\tag{5.2}
\]

The weight `w(Q)` is the aggregate complete-model energy at exact primitive conductor `Q`: there are `\varphi^\dagger(Q)` primitive local character choices, each with squared coefficient `1/\varphi^\dagger(Q)^2`.

### Theorem 5.1 -- high-conductor orbit collision formula

For `j<k`, write

\[
P_k=L_{jk}P_j.
\]

Then

\[
\boxed{
\rho_{j,Z}(Q)=\rho_{k,Z}(Q)
\iff
Q\mid L_{jk}-1.
}
\tag{5.3}
\]

Let

\[
\mathcal S_{jk}
=
\{p\in\mathcal P_R:p\mid L_{jk}-1\},
\qquad
S_{jk}=\sum_{p\in\mathcal S_{jk}}\frac1{p-2}.
\]

The off-diagonal Gram is exactly

\[
\boxed{
\mathcal H_{jk}
=
\prod_{p\in\mathcal S_{jk}}
\left(1+\frac1{p-2}\right)
-1-S_{jk}.
}
\tag{5.4}
\]

If `h=k-j`, primorial-prefix rigidity gives

\[
S_{jk}\ll\frac{h+1}{X},
\]

and hence

\[
\boxed{
\mathcal H_{jk}\ll\frac{(h+1)^2}{X^2}.
}
\tag{5.5}
\]

The diagonal is

\[
\mathcal H_{jj}
=
\prod_{p\in\mathcal P_R}
\left(1+\frac1{p-2}\right)
-1-\sum_{p\in\mathcal P_R}\frac1{p-2}
\ll\frac1{(\log X)^2}.
\tag{5.6}
\]

Consequently

\[
\boxed{
\|\mathcal H\|_{\rm op}
\ll
\frac1{(\log X)^2}+\frac{K^3}{X^2}.
}
\tag{5.7}
\]

In particular, the complete-model high-conductor candidate frame is small for every previously admissible block `K\ll\sqrt X`.

#### Proof

Two representatives in the same interval of length `Q` are equal exactly when their residue classes agree. Thus

\[
\rho_j(Q)=\rho_k(Q)
\iff
Q\mid P_k-P_j
\iff
Q\mid L_{jk}-1,
\]

because `(Q,P_j)=1`. Summing `w(Q)` over subsets of `\mathcal S_{jk}` of cardinality at least two gives (5.4). Since

\[
e^t-1-t\ll t^2
\]

for the present `t=S_{jk}=o(1)`, (5.5) follows. Equation (5.6) is the same product identity on the full band. Schur summation over `h` gives (5.7). `\square`

## 6. Why the high-conductor theorem does not finish the proof

The frame (5.7) controls complete-model energy, where each conductor carries the reciprocal weight `1/\varphi^\dagger(Q)`. Deterministic character summation reconstructs the point indicator

\[
\mathbf1_{Q\mid P_j+m},
\]

and removes that reciprocal decay through character multiplicity. Equivalently, the exact all-order survivor formula compresses the entire conductor system to the unweighted union-hit statistic.

Therefore (5.7) proves that repeated high-conductor candidate locations across primorial centres are not the obstruction. It does not prove that the unique candidate `\rho_{j,Z}(Q)` is prime with the required centred frequency, nor does it control cancellation between physical and one-point conductors.

## 7. Current literature gate

The closest large-modulus prime-progression results are formulated for a fixed nonzero residue or shift and achieve logarithmic or distributional savings after averaging moduli. The present family has exponentially growing shifts `P_j`, prime moduli at the critical square-root scale, and requires an `L^2` estimate over a consecutive primorial orbit.

Even a hypothetical rowwise estimate of the usual form

\[
|\mathcal E(P_j)|\ll H(\log H)^{-A}
\]

would yield after squaring and summing the block

\[
KH^2(\log H)^{-2A},
\]

whereas the Fortune allowance is `KHX/\log X`. Since `H\asymp X^2`, their ratio is

\[
\frac{X}{(\log X)^{2A-1}},
\]

which diverges for every fixed `A`. Fixed-shift logarithmic savings are therefore not a substitute for the required family-shift bilinear contraction, even before addressing uniformity in `P_j`.

## 8. Precise next theorem

### `POTD(X)` -- primorial-orbit Type-II dispersion

For every logarithmic centre block `B`, every first physical dyadic band `\mathcal P_R`, and every actual critical Type-II coefficient pair arising from a frozen prime-source decomposition, prove

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{p\in\mathcal P_R}
\lambda_p\Delta_{j,p}^{\times}(\alpha,\gamma)
\right|^2
\ll
\sum_{j\in B}\sum_{p\in\mathcal P_R}
|\lambda_p\Delta_{j,p}^{\times}(\alpha,\gamma)|^2
+E_{B,R}^{\rm II},
}
\tag{8.1}
\]

with Fortune-scale dyadically summable errors, while preserving the signed recombination of the Type-I/II decomposition.

In the inverse-orbit coordinates (2.4), `POTD(X)` must save the factor `X^{1-o(1)}/\log X` lost by generic Cauchy in (4.6). It must use the actual arithmetic of `\alpha`, rather than hold for arbitrary coefficients.

A complete route also requires the deterministic counterpart of the small model frame (5.7): signed sampling of the unique prime candidates `\rho_{j,Z}(Q)` and their covariance with the physical Type-II block.

## 9. Programme verdict

### Proved exactly

1. the additive and unit-centred Type-II identities (2.3)--(2.4);
2. the combined primorial--inverse orbit Gram (3.2)--(3.3);
3. the fixed-modulus norm `K/p`;
4. the logarithmic-block synthesis frame (3.5);
5. the high-conductor candidate collision criterion (5.3);
6. the exact Euler-product Gram formula (5.4);
7. the small high-conductor complete-model frame (5.7).

### Proved from classical input

1. `\sum_{p\asymp R}1/p\ll1/\log R`;
2. the inverse-orbit frame is bounded for `K\ll\log X`;
3. generic frame plus Cauchy misses the Fortune scale by `X^{1-o(1)}/\log X`;
4. fixed rowwise logarithmic savings do not reach the required family `L^2` scale.

### Computationally verified

1. the direct, Fourier and inverse-orbit Type-II identities;
2. the exact unit-centre drift;
3. every inverse-orbit collision identity on finite panels;
4. the high-conductor representative collision and Euler-product formulas;
5. finite coherent/diagonal Type-II ratios, labelled empirical only.

### Closed as direct routes

1. centre-only or centre-plus-one-variable frame followed by generic Cauchy;
2. fixed-shift rowwise logarithmic estimates as a substitute for family dispersion;
3. complete-model high-conductor energy as a substitute for deterministic candidate sampling;
4. separate physical and one-point positive estimates.

### Open

1. `POTD(X)`;
2. signed deterministic high-conductor candidate sampling;
3. `MRPMD(X)` / `SBD(X)`;
4. `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

The programme has therefore moved the wall again. Centre geometry, one Type-II variable and high-conductor model collisions are now controlled. The irreducible remaining object is a bilinear arithmetic contraction in the second Type-II variable, coherently coupled to one-point conductor sampling.