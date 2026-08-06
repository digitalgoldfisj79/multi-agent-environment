# INT-AOD occupancy-dual closeout

**Programme:** `FORTUNE_INT_AOD_OCCUPANCY_DUAL_V0_1`  
**Date:** 5 August 2026  
**Branch:** `gpt56/fortune-int-aod-occupancy-dual-v01-20260805`  
**Outcome:** `REDUCED_TO_CONNECTED_CUMULANT_BOUND`  
**Terminal target:** `INT-SOCG`

## Final ruling

The programme establishes no proof of `INT-AOD` or Fortune's conjecture. It replaces the full occupancy theorem by one quantitatively smaller signed theorem and closes the other admitted routes at explicit barriers.

## Exact detector reduction

For any preregistered row-dependent temperatures `0<tau_j<=tau_A`,

\[
\sum_j e^{-\tau_jZ_j}<1
\]

excludes every zero row and implies the frozen issue-#54 detector term by term. This implication is kernel checked.

Choosing `tau_b=Theta(log X/X)` after fixing a deterministic lower mean scale reduces the associated exact-cover degree from

\[
\Theta(X^2/\log X)
\quad\text{to}\quad
\Theta(X).
\]

## Whole-block obstruction

An equal mixture of two Poisson row classes has Laplace transform

\[
\frac12e^{-\tau\lambda_-}+\frac12e^{-\tau\lambda_+}
\]

with nearest zero at `i*pi/(lambda_+-lambda_-)`. Whole-block mean variation of order `X` therefore gives a cumulant-series radius `Theta(1/X)`, while the useful detector temperature is `Theta(log X/X)`. Rowwise Poisson behaviour alone cannot justify a whole-block cumulant expansion.

## Correct connected identity

For a uniform row `J` in one deterministic stratum and

\[
Z_J=\sum_m I_m(J),
\]

the ordinary cumulants satisfy

\[
c_{k,b}=\sum_{m_1,\ldots,m_k}
\operatorname{Cum}_b(I_{m_1},\ldots,I_{m_k}),
\]

with all ordered column tuples, including repetitions.

The initially built factorial-cumulant/distinct-column identity was false. O9 static validation detected it; the identity, diagnostics, claim ledger and successor theorem were corrected before closeout. No claim depends on the rejected formula.

## Primary successor — INT-SOCG

Partition the rows deterministically into `B=polylog(X)` terminal-prime strata. For stratum `b`, let `c_{k,b}` be the ordinary cumulants of `Z_J`. Prove that there are preregistered scales

\[
L_b\ge cX,
\qquad
\tau_b=(1+3\varepsilon)\frac{\log(n_bB)}{L_b}\le\tau_A,
\qquad
D_b\ll\frac{X}{(\log X)^{1+\delta}},
\]

such that

\[
c_{1,b}\ge L_b
\]

and, for every `k>=2`,

\[
|c_{k,b}|\le c_{1,b}k!D_b^{k-1}.
\]

Then `tau_bD_b=o(1)`, the ordinary cumulant series converges absolutely, and

\[
\sum_{k\ge2}\frac{\tau_b^k}{k!}|c_{k,b}|
\le
\tau_bc_{1,b}\frac{\tau_bD_b}{1-\tau_bD_b}
=o(\log(n_bB)).
\]

Consequently each stratum contributes less than `1/B` to the occupancy detector, giving

\[
\boxed{
\mathrm{INT\!-\!SOCG}
\Longrightarrow
\mathrm{INT\!-\!AOD}
\Longrightarrow
\text{eventual Fortune}.
}
\]

`INT-SOCG` remains open.

## Independent conditional and rowwise routes

- `RUHL-FM`: row-uniform Hardy--Littlewood factorial-moment estimates through order `Theta(log X)`, with the registered weighted one-row error, imply `INT-AOD` by even Bonferroni truncation. This is a complete conditional implication, not an available theorem.
- `INT-RPBH`: a signed rowwise bilinear-hyperbola estimate beyond `d=sqrt(H)` would imply actual prime pairs. Direct asymptotic-sieve and weighted-switching applications do not supply it; beyond `d>H` there is at most one offset per modulus.

## Exact diagnostics

Exact primorial panels with `H=floor(X^2/2)` contained no zero row through `X=300`. After deterministic terminal-prime stratification, the corrected ordinary-cumulant diagnostics gave total exponential detector values from `0.07618` at `X=100` to `0.02586` at `X=300`; every tested stratum stayed inside its numerical Laplace zero-free radius and had positive order-twelve absolute margin.

The temperatures used observed means and are therefore diagnostic only.

## Formal validation

`FortuneFormal/Integer/AdaptiveOccupancyCriterion.lean` kernel-checks:

- zero-row exclusion for row-dependent exponential temperatures;
- termwise monotonicity from row-dependent to frozen uniform temperature;
- the aggregate implication to the frozen detector.

No new axiom, `sorry`, `admit`, or unsafe declaration was introduced.

## Validation record

- build sentinel `6a72b306a00abefd4b29302e`: completed, zero failures;
- corrected exact panel job `6a72bdeca00abefd4b29310c`: completed, zero failures;
- targeted Lean job `6a72bab0a00abefd4b2930d2`: 8,659 jobs, zero failures;
- final static job `6a72c04c6b79c09949c22c85`: completed, zero failures;
- full clean-room job `6a72c07e6b79c09949c22c89`: Lean 4.32.0, 8,684 jobs, all inherited and new audits passed.

A stale clean-room job `6a72bd81a00abefd4b2930fc` was cancelled after the branch changed; its result is not used.

## Explicitly not claimed

- `INT-SOCG`;
- `INT-AOD`;
- `INT-PFLI` or `INT-PSLT`;
- Fortune's conjecture;
- a function-field-to-integer transfer.
