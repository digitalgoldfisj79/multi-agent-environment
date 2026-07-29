# Programme status after the complete-CRT survivor Gram

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: a new exact all-order Gram theorem now proves the complete-CRT model component of the normalized-survivor transfer. The remaining obstruction is deterministic sampling by the actual candidate primes. Fortune's conjecture remains **OPEN**.

## 1. New exact theorem

For one dyadic band `\mathcal P_R`, put

\[
V_R=\prod_{p\in\mathcal P_R}\frac{p-2}{p-1}
\]

and, on the product of nonzero residue classes,

\[
g_{j,R}(\omega)
=
V_R^{-1}
\mathbf1_{\omega_p\ne-P_j\pmod p\ {\rm for\ all}\ p\in\mathcal P_R}
-1.
\]

The complete covariance matrix is now evaluated exactly:

\[
\mathcal K_{jj}=V_R^{-1}-1,
\]

and, for `j\ne k`,

\[
\mathcal K_{jk}
=
\prod_{p\mid P_j-P_k}\frac{p-1}{p-2}
\prod_{p\nmid P_j-P_k}\frac{(p-1)(p-3)}{(p-2)^2}
-1.
\]

All products are over the band.

Primorial-prefix rigidity then gives

\[
\|\mathcal K(R)\|_{\rm op}
\ll
\frac1{\log R}
+
\frac{K^2}{R}
+
\frac{K}{R\log R}.
\]

This keeps the density coordinate, every nontrivial Euler conductor, normalization drift, sparse hits and higher factor clusters inside one centred object.

## 2. Conditional model transfer and self coordinates

Because a current band is independent of all previous bands in the complete CRT model, the Gram theorem yields a conditional Bessel estimate with arbitrary coefficients measurable in the earlier bands. Thus the complete-CRT analogue of the bandwise normalized-survivor martingale transfer is proved.

For a candidate offset `m=p_0` equal to a band prime, the source residue at `p_0` is zero. It is handled exactly by

\[
g^{[p_0]}_{j,R}
=
\frac{p_0-1}{p_0-2}g_{j,R\setminus\{p_0\}}
+
\frac1{p_0-2}.
\]

The first term is a reduced-band centred survivor coordinate and the second is explicit normalization drift. No self source point is discarded.

The complete-CRT model geometry, including the centred part of the self coordinates, is no longer open.

## 3. Complement-divisor preconditioner

A Hilbert-valued complement-divisor identity is also proved:

\[
\sum_{d\mid\Pi}\varphi(d)
\left\|
\sum_{d\mid m\mid\Pi}\frac{\lambda_m}{m}
\right\|^2
=
\frac{\varphi(\Pi)}{\Pi}
\sum_{\delta\mid\Pi}\frac1{\varphi(\delta)}
\left\|
\sum_{m\mid\delta}\lambda_m
\right\|^2.
\]

For the coherent Möbius family, the right side collapses to its single `\delta=1` coordinate. This is the correct coefficient-space mechanism for retaining full Euler cancellation.

## 4. Remaining theorem

The actual band increment is a weighted sum of:

1. ordinary nonzero-residue survivor coordinates;
2. reduced-band centred self coordinates;
3. the explicit self-normalization drift, retained jointly with the existing zeroth coordinate.

The weights contain the frozen logarithmic factor and all preceding survivor bands.

The remaining theorem is `PCRST(X)`: prove that these deterministic prime residue vectors obey the complete-CRT covariance scale, with dyadically summable error. This is a sparse, weighted empirical-process theorem for a rigid family of normalized survivor tests. It is strictly narrower than the previous formulation of `NSMT(X)`.

Neither Friedlander's 2026 sieve inequality nor Gorodetsky's translation-averaged rough-number variance theorem supplies this sparse primorial sampling step.

## 5. Current boundary

**PROVED EXACTLY**

- common-base quotient collapse;
- common hybrid Fourier representation;
- fixed-conductor frame;
- normalized-survivor martingale identities;
- Hilbert complement-divisor identity;
- complete-CRT all-order survivor Gram;
- conditional model Bessel transfer;
- band-prime self-coordinate decomposition.

**CLOSED AS POSITIVE ROUTES**

- conductorwise Cauchy before density cancellation;
- independent sparse-hit estimates;
- factorized source/orbit norms;
- treating the model covariance itself as an open problem.

**OPEN**

- `PCRST(X)`, deterministic prime-candidate residue transfer;
- dyadic recombination into arithmetic `NSMT(X)`;
- the Fortune variance theorem;
- Fortune's conjecture.

Authoritative theorem note:

`frontier/integer_source_frame_bridge/COMPLETE_CRT_SURVIVOR_GRAM_AND_SAMPLING_BOUNDARY_20260729.md`
