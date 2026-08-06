# P0 execution — source and range freeze

**Status:** `P0_PASSED_WITH_W2_UNAVAILABLE`

## Frozen inherited inputs

- RUHL-FM parent head: `2c7c9e11d0af091d69886fd888a90876ba2e1161`.
- Prime-modulus primorial-walk theorem: `fortune-int-socg-stratified-cumulants/C5_EXECUTION.md`.
- One stratum consists of `n` consecutive terminal primes `ell_j in [X,2X)` and primorial centres `P_j`.
- Every supported modulus is squarefree and all of its prime factors exceed `2X`.

## Conductor geometry

If `omega(q)=r`, then every prime factor of `q` is strictly larger than `2X`, hence

\[
q>(2X)^r.
\]

Consequently the squarefree-composite lane is empty at the natural prime-modulus range `Q_X=X^2`: an order-two modulus would satisfy `q>4X^2`.

The first non-vacuous order-`r` range therefore requires `Q_X>(2X)^r`. This programme treats `Q_X` as an explicit parameter and never silently identifies the prime-modulus range with the larger source conductor range.

## Frozen coefficient contracts

### W0 — unrestricted diagnostic baseline

Arbitrary nonnegative weights supported on the registered modulus family. This is a falsification class only.

### W1(r,U_r) — bounded fixed-order contract

For fixed `r>=1`,

\[
\mu^2(q)=1,\quad \omega(q)=r,\quad p\mid q\Rightarrow p>2X,
\quad 0\le \beta(q)q\le U_r.
\]

This is frozen before collision inspection and supports a coefficient-uniform theorem.

### W2 — actual source coefficients

Unavailable. The inherited C7 source programme names Heath--Brown, Vaughan, divisor-switching and related identities, but commits no exact source-to-row coefficient formula `beta_X(q)`, no conductor partition and no normalization that can be inserted into the PWOC energy.

### W3 — proved majorant of W2

Unavailable because W2 is not instantiated.

## P0 decision

P0 passes for W0 and W1. It records `SOURCE_WEIGHT_CONTRACT_NOT_AVAILABLE` for W2/W3. No surrogate weight may be promoted as a source theorem.