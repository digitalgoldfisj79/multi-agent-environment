# PGD2 autonomous attack phase report

**Date:** 2026-07-19  
**Status:** natural stopping point reached; PGD2 and Fortune's conjecture remain open

## Executive conclusion

The pre-registered three-route tournament has been completed.

1. **Traceless symmetric-square route:** exact projector identity obtained, but the leading edge block has the same \(M\)-scale dimension as PC-FROB2. Loop terms are closed; edge/mixed separation is badly conditioned. Route stopped.
2. **Prime-pair density route:** the Hardy--Littlewood density main term is itself polynomially too large because squarefree semiprimes below \(X^2\) divide every primorial centre. A conventional main-term-plus-small-error dispersion argument cannot work.
3. **Coupled detector route:** a new growing Möbius-degree truncation theorem removes the high-\(\omega\) tail at negligible Frobenius cost. The retained detector has degree \((1+\eta)\log X/\log\log X\), but must remain globally coupled; divisor-size separation remains catastrophically ill-conditioned.
4. **Primorial-residue route:** largest-endpoint decomposition maps to the previously closed weighted pair-walk/fixed-conductor architecture and supplies no new average.

No proof of PGD2 was obtained.

## Exact new results

### A. Traceless projector identity

\[
M^2\operatorname{Tr}(A_{q,a}A_{r,a})
=
|H_2(a(1/q-1/r))|^2-M.
\]

### B. Density-main-term obstruction

For the Hardy--Littlewood pair-density surrogate,

\[
\mathcal R_a^{\rm HL}
\gg \frac{M^2}{\log^4X}-MX^{o(1)}.
\]

The obstruction is caused by semiprimes \(pr\) with
\(X/\sqrt2\le p<r<X\), which divide every primorial centre.

### C. Growing Möbius-degree reduction

For

\[
k=\left\lceil(1+\eta)\frac{\log X}{\log\log X}\right\rceil,
\]

the difference between the exact prime detector and the truncated detector

\[
T_k(n)=\sum_{d\mid(n,A_X),\,\omega(d)\le k}\mu(d)
\]

contributes

\[
\|\mathcal C(R_k)\|_F^2
\le MX^{-2\eta+o(1)}.
\]

Thus high Möbius degree is not load-bearing.

## Revised theorem boundary

The smallest surviving target is:

> Prove PGD2/CFR2 for the complete signed reciprocal operator formed with the cumulative Möbius-degree detector \(T_k\), where \(k\sim(1+\eta)\log X/\log\log X\), without separating degree or divisor-size sectors absolutely.

This is narrower than the full exact pre-sieve because its high-degree tail is now rigorously removed. It is not covered by current sieve, Kloosterman, simultaneous-AP, or sparse-large-sieve theorems identified in the audit.

## Scientific assessment

This phase made real structural progress but did not improve the asymptotic bound. It establishes that:

- ordinary density dispersion is conceptually wrong for this kernel;
- high Möbius degree can be discarded;
- the parity-sensitive, growing-degree coupled detector is the actual remaining prime-detection interface;
- tensor, endpoint and conductor decompositions do not bypass it.

Further computation is justified only if a theorem candidate is written for that globally coupled growing-degree operator. Larger generic panels would be a diversion.
