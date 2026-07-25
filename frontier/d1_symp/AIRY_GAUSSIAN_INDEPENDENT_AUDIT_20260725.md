# Independent audit of the Airy Gaussian claim and transport priority

**Date:** 2026-07-25  
**Branch:** `gpt56/airy-gaussian-independent-audit-20260725`  
**Base:** `06b5fc04ea8bbd7d18742a999141a6f863518522`  
**Scope:** numerical Airy law, virtual-Adams inference, singular-locus lemma, and the proposed `(M_p,S_p)` next step.  
**Ruling:** the numerical dataset is reproducible and decisively refutes the working constant `C=4`. It does **not** prove that no absolute constant exists. The proposed four-prime computation of `(M_p,S_p)` is not well-defined until an object-level transport decomposition has been constructed.

## 1. Independent numerical reproduction

An implementation independent of `airy_gaussian_law_verify.py` reproduced the scan over all `4806` primes `p congruent 5 mod 6`, `p<100000`:

- mean `0.0032688684`;
- sample variance `2.0969370238`;
- skewness `-0.0459520387`;
- kurtosis `2.9070848206`;
- Kolmogorov--Smirnov statistic against `N(0,2)`: `0.0136181983`;
- nominal 5% critical value: `0.0195888025`;
- maximum `|rho_p| = 4.8468292139` at `p=57653`.

The five reported tail frequencies were also reproduced. The numerical table in `AIRY_GAUSSIAN_LAW_AND_TARGET_FALSIFICATION_20260725.md` is therefore genuine.

The exact calibration at `p=5,11,17,23,29` was independently reproduced. In the conventions implemented by the verifier, the calibrated formula is

\[
 rho_p=+\frac{2}{\sqrt p}\sum_t\cos(p\theta_t),
\]

not the displayed negative-sign formula in the write-up. This is probably an additive-character/Fourier convention mismatch, but it must be repaired because the current text and code assert opposite exact identities. The distributional statistics are invariant under the global sign.

## 2. What the data establishes

The computation proves the following finite statements:

1. the conjectural choice `C=4` is false;
2. every proposed universal constant `C<4.8468292139` is false;
3. up to `10^5`, the empirical distribution is close to `N(0,2)` under the reported diagnostics;
4. the observed data strongly disfavour a small bounded coefficient and support a Gaussian extreme-value heuristic.

These conclusions are sufficient to stop treating `C=4` as a viable working conjecture and to lower the priority of attempts aimed specifically at a small absolute constant.

## 3. What the data does not establish

A finite KS non-rejection cannot imply

\[
\sup_p |rho_p|=\infty,
\]

nor can it prove the limsup law

\[
|rho_p|=(2+o(1))\sqrt{\log p}.
\]

A bounded distribution with a bound larger than the observed maximum can pass every finite test reported here. The running maximum is necessarily non-decreasing by definition; observing growth to `4.85` does not distinguish unboundedness from boundedness at a larger constant.

Accordingly, the branch must use the status

> **high-confidence numerical evidence against absolute boundedness; rigorous falsification only of constants below the observed maximum**

rather than “the terminal target is false”.

The same distinction applies to the Gaussian model. Geometric `SL_2` monodromy and fixed-representation Sato--Tate equidistribution do not by themselves prove a central limit theorem when the representation degree/frequency is `k=p` and the field size is simultaneously `p`. The required uniform-in-`k` independence statement is precisely nontrivial.

## 4. Verifier defects

The committed verifier has four audit defects.

1. `SCAN_LIMIT=20000`, so it does not rerun the advertised `p<100000` scan, the `4806`-prime KS statistic, or the extremum at `p=57653`.
2. It prints and asserts “no absolute constant exists” from a finite sample. That assertion is not logically tested by the code.
3. Its exact formula has the opposite sign from the displayed formula in the accompanying paper.
4. The running-maximum monotonicity assertion is tautological and carries no evidential weight.

These do not invalidate the numerical table, which was independently reproduced; they invalidate the claimed logical certification.

## 5. Virtual-Adams ruling

The reported scalar measurements are also reproducible in principle and are strong negative evidence for the simplest covariance mechanism:

- each normalized symmetric-power sum has RMS close to `1`;
- their sample correlation is near zero;
- the difference has RMS close to `sqrt(2)`.

What follows is narrower than the committed ruling. The data refutes the hypothesis that the desired gain comes from a persistent positive correlation between the two **total scalar traces** over the sampled primes. It does not prove that every conductor, Spin, Clausen, or cohomological use of the Adams decomposition is impossible. Zero sample correlation is not independence, and scalar covariance does not determine all constituent-level cancellations or bounds.

The exact Hayes circularity theorem remains a rigorous closure of that specific Hayes reconstruction. The Gaussian measurement is an explanatory heuristic, not a theorem that every future exact identity must be tautological.

## 6. Singular-locus lemma correction

The proof that the projective cubic

\[
\{\operatorname{Tr}(x^3)=0\}\subset \mathbf P(\ker\operatorname{Tr})
\]

has singular locus `[1]` is correct for primes `p>3`.

It is false as stated for “every odd prime”. In characteristic `3`,

\[
\operatorname{Tr}(x^3)=\operatorname{Tr}(x)^3,
\]

so the restricted cubic vanishes identically on `ker Tr`, and its derivative is identically zero. The lemma must be stated for `p>3` (which is sufficient for the `p congruent 5 mod 6` branch).

## 7. Non-identifiability of `(M_p,S_p)`

The proposed next step says to compute

\[
\mathcal R_p=S_p+M_pT_p
\]

at four primes from already committed scalar values. This is not a defined computation.

### Proposition

Given only the scalars `(R_p,T_p)`, with `T_p != 0`, the pair `(M_p,S_p)` is non-identifiable: for every chosen scalar `m_p`,

\[
M_p=m_p,\qquad S_p=R_p-m_pT_p
\]

is a valid decomposition.

Four primes provide four equations but eight prime-dependent unknowns. An empirical fit cannot distinguish `M_p=O(1)`, `M_p asymp sqrt(p)`, or `M_p asymp p` unless an independently defined residual `S_p`, a shared symbolic formula, or an object-level direct-sum/filtration decomposition fixes the meaning of the two terms.

This is exactly what `GATE0_PRIME_DEPENDENCY_AUDIT_20260724.md` already says: the repository lacks the transport identity. The missing object is not a table entry; it is the bridge theorem.

## 8. Corrected programme order

The application side should now receive priority, but the first task is not scalar fitting.

1. **Construct the object-level bridge.** In the nonzero-frequency Fourier--Cayley complex, define a canonical Airy summand or subquotient and a canonical complementary residual, including Tate normalization and every boundary stratum.
2. **Derive exact symbolic coefficients.** Only after the decomposition exists, read off the transport multiplicity `M_p` and residual trace `S_p` as explicit functions of `p`.
3. **Validate at `p=11,17,23,29`.** Use the committed exact ledger and `T_p` values to check the symbolic formula; do not infer the formula from those four scalars.
4. **Evaluate the threshold.** Compare the resulting growth of `M_p,S_p` with the proved `C(p)<=2 sqrt(p)` bound.
5. **Reopen analysis only if required.** If the exact bridge yields a threshold below `sqrt(p)`, formulate the weakest uniform-in-large-symmetric-power estimate actually needed. Do not restore the unsupported absolute-constant target by default.

The load-bearing theorem remains the nonzero-frequency stationary-phase/hook transport theorem isolated in `FOURIER_CAYLEY_ZERO_FREQUENCY_OBSTRUCTION_20260725.md`. The new numerical evidence changes resource allocation, but it does not bypass that theorem.

## 9. Final status

- **Machine-reproduced:** the full `p<100000` Gaussian-looking dataset and the failure of `C=4`.
- **Strong heuristic:** unbounded Gaussian coefficients and `2 sqrt(log p)` extreme-value growth.
- **Not proved:** failure of every absolute constant; the limsup law; independence of the Adams terms; impossibility of all future exact/cohomological mechanisms.
- **Proved after correction:** the singular-locus lemma for `p>3`.
- **Theorem-level obstruction:** object-level Airy transport through the positive-dimensional nonzero-frequency Fourier--Cayley sector.
