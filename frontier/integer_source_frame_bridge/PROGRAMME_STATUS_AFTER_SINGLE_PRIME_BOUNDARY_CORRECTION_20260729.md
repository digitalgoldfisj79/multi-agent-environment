# Programme status after the single-prime boundary correction

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the conductor-`p` programme has been checked against the already-established frozen first-order coordinate. The apparent first-band one-logarithm gap was caused by replacing the actual constant prime-source coefficient by a broader logarithmically weighted source model. For the actual first physical band, the one-residue low mode is exactly the negative of the established same-band coordinate, so its diagonal is already bounded by `KHX/log X`. The genuine open theorem remains the coherent signed covariance across distinct physical prime moduli. Fortune's conjecture remains **OPEN**.

## 1. Exact correction

For every first-band centre and physical prime,

\[
E_{j,p}=-a_{j,p}.
\]

Consequently,

\[
\sum_{j,p}|E_{j,p}|^2=D_{B,R},
\]

and the branch already proves

\[
\sum_R D_{B,R}\ll\frac{KHX}{\log X}.
\]

`SW1BDH(X)` is therefore retracted as a new first-band obstruction.

## 2. Actual same-band wall

The open expression is

\[
\sum_j\left|\sum_pE_{j,p}\right|^2,
\]

not `\sum_{j,p}|E_{j,p}|^2`.

Its expansion contains the signed `p\ne s` covariance already named `SBD(X)`. The equivalent moving-residue formulation is recorded as `MRPMD(X)`; it is the same theorem, not another missing input.

## 3. Exact no-go

For every scalar split

\[
\frac1{p-2}=u_pv_p,
\]

the separate centre/source diagonal masses satisfy

\[
\left(\sum_p(p-2)|u_p|^2\right)
\left(\sum_p(p-2)|v_p|^2\right)
\ge|\mathcal P_R|^2.
\]

Thus sequential source and centre Cauchy estimates necessarily lose the full number of physical moduli. Sparse-modulus large-sieve or BDH estimates control the already-bounded diagonal, not the coherent all-ones modulus vector.

## 4. Range calibration

Since

\[
H=\eta X^2,
\qquad \eta<1,
\]

and the first physical primes satisfy `p>X`, the band lies strictly beyond `\sqrt H`. Classical Bombieri--Vinogradov cannot be inserted as a black box. A genuinely joint moving-residue dispersion theorem, or a complete normalized-survivor argument preserving higher-order cancellation, is required.

## 5. Boundary

**PROVED EXACTLY**

- first-band low-mode/frozen-coordinate identification;
- equality of the low-mode diagonal and established same-band diagonal;
- sharp scalar factorisation lower bound;
- strict above-square-root geometry.

**RETRACTED**

- `SW1BDH(X)` as a new first-band logarithmic-saving theorem;
- the generic `KHX log X` large-sieve estimate as the current sharp bound for the actual first-band detector coefficients.

**CLOSED**

- sequential source/centre scalar splitting;
- sparse-modulus diagonal theorems as a substitute for cross-modulus covariance;
- classical level-`1/2` distribution as a black-box finish.

**OPEN**

- `MRPMD(X)` / `SBD(X)`;
- a full normalized-survivor alternative;
- later-band survivor-weighted conditional coordinates;
- `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

Authoritative notes:

- `frontier/integer_source_frame_bridge/SINGLE_PRIME_DIAGONAL_CONSISTENCY_CORRECTION_20260729.md`
- `frontier/integer_source_frame_bridge/SAME_BAND_PRIME_MODULUS_FACTORISATION_BOUNDARY_20260729.md`
