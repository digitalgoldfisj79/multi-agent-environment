# Primorial Incidence Transfer v0.1 — final status

Date: 27 August 2026

## Terminal state

`THEOREM_PROOF_COMPLETE__NOVELTY_PROVISIONAL__NO_FORTUNE_TRANSFER`

## Frozen theorem

Let `q_1<...<q_N` be the primes in `[X,2X]`,

`B_X=product_{p<X}p`,

`P_0=B_X`, `P_j=B_X product_{i<=j}q_i`,

and let `varpi>2X` be prime. Then, for all sufficiently large integers `X`,

`|{P_j mod varpi:0<=j<=N}| >> (X/(log X)^2)^(8/15)`.

Choosing a prime `2X<varpi<4X` gives

`|{P_j mod varpi}| >> varpi^(8/15)/(log varpi)^(16/15)`,

so the value set is asymptotically larger than `sqrt(varpi)`.

## Gate ledger

- **G1 exact recurrence:** PASS.
- **G2 affine composition / multiplicity <=2:** PASS.
- **G3 repeated prime-gap population `>>X/(log X)^2`:** PASS unconditionally from PNT + telescoping + pigeonhole.
- **G4 Stevens--de Zeeuw hypotheses:** PASS. Cartesian-product conditions reduce to an automatic `m^3<=m^6` plus `m^3<<varpi^2`; failure of the latter already gives the stronger `m>>varpi^(2/3)` alternative.
- **G5 exponent `8/15`:** PASS.
- **G6 finite algebra/combinatorics regression:** PASS on six frozen panels; maximum nonidentity line multiplicity 2 throughout.
- **G7 literature collision screen:** NO DIRECT COLLISION FOUND; human specialist priority review required.

## Proof audit

`PASS_AFTER_ONE_OFF_BY_ONE_REPAIR`.

The initial draft counted `N-2` rather than `N-1` internal consecutive-prime gaps. Correcting this does not change any asymptotic, constant class, or exponent. No other proof defect was found.

## Novelty

`PROVISIONAL_NEW_SPECIALIZATION_HUMAN_PRIORITY_REVIEW_REQUIRED`.

The method is an explicit adaptation of Xiyu Hu's factorial-residue incidence argument (arXiv:2608.01781) and depends on the Cartesian-product incidence theorem of Stevens--de Zeeuw (arXiv:1609.06284). Searches found adjacent factorial-value-set, fixed-polynomial-product, freely chosen prime-product, and consecutive-prime residue-pattern literature, but no matching theorem for deterministic cumulative products of consecutive primes.

The result is also not subsumed by current Paper I: Paper I's almost-injectivity theorem is an averaged-modulus result aimed mainly at `r~X^2`, whereas the new theorem is pointwise for every prime `varpi>2X` and yields a comparable-modulus `varpi~X` corollary.

## Publication disposition

Candidate for the next revision of Paper I, **held outside the frozen standalone release until specialist priority review**.

Publication-safe description:

> Adapting Hu's fractional-linear incidence method for factorial residues, we obtain a pointwise modular anti-concentration theorem for deterministic cumulative products of consecutive primes.

Do not currently market it as the first such theorem without specialist literature review.

## Fortune disposition

`INTEGER_FORTUNE_MAINLINE_REMAINS_CLOSED`.

This theorem proves modular anti-concentration of the prefix path. It does not provide:

- selected-centre prime-pair variance;
- signed high-order prime-tuple control;
- source-to-reciprocal transference;
- a prime in every primorial square window.

No progress toward a proof of Fortune's conjecture is claimed.
