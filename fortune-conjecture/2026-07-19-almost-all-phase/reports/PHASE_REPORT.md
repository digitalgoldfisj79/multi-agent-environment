# Fortune almost-all phase — final report

**Date:** 2026-07-19  
**Register:** cold  
**Final status:** no proof of Fortune; no almost-all theorem.

## Objective

Test the proposed route

\[
\text{Fortune failure certificate}
\to
\text{positive Selberg variance}
\to
\text{average over primorial indices}
\to
\text{zeta-zero pair cancellation}
\to
\text{Fortune for almost all }n.
\]

## Results

### A. Failure certificate: PASS

For

\[
y_n=p_{n+1}^2-2,
\quad
h_n=y_n/2,
\]

define

\[
J_n=
\int_{P_n+1}^{P_n+1+y_n/4}
|\psi(x+h_n)-\psi(x)-h_n|^2\,dx.
\]

For all sufficiently large \(n\),

\[
F_n\text{ composite}\Longrightarrow J_n\ge y_n^3/64.
\]

Hence

\[
\#\{n\le N:F_n\text{ composite}\}
\le64\sum_{n\le N}J_n/y_n^3+O(1).
\]

This is a genuine exact reduction to a positive variance quantity.

### B. Generic short-interval theory: FAILS TO TRANSFER

Current unconditional ordinary-centre results remain at polynomial interval length. RH reaches \((\log x)^{2+\varepsilon}\) for almost all ordinary centres; RH plus strong pair correlation reaches the probabilistic almost-all scale. None controls a prescribed sequence as sparse as \(P_n\).

### C. Primorial-index zero average: FAIL

The proposed new average was expected to provide cancellation in

\[
\mathcal Z_N(t)=\sum_{n\le N}e^{it\log P_n}.
\]

Instead, for fixed \(c\),

\[
\frac1N\mathcal Z_N(c/\log P_N)
\to
\int_0^1e^{icu}\,du.
\]

At natural zeta-zero spacing this is generically nonzero, so the sum is order \(N\), not \(\sqrt N\).

### D. Shared spectral average: FAIL

The effective explicit-formula cutoff

\[
T_n=P_n/(p_{n+1}^2-2)
\]

satisfies

\[
T_{n+1}/T_n\sim p_{n+1}\to\infty.
\]

The dominant zero bands for successive indices are asymptotically disjoint. The high-frequency sector that controls each interval does not receive a common index average.

## Scientific conclusion

The almost-all scope move was strategically legitimate because it sought a genuinely new variable. The variable does not yield the anticipated analytic surplus:

\[
\boxed{
\text{primorial-index averaging is coherent at critical zero spacing and migrates in conductor.}
}
\]

The route is stopped in its proposed explicit-formula form.

This is stronger than an inconclusive computation. The coherence and conductor-migration statements are exact asymptotic theorems.

## Surviving outputs

1. deterministic cubic Fortune-failure certificate;
2. exact critical-scale Fourier-kernel limit;
3. exact conductor-migration identity;
4. reproducible zeta-gap finite audit;
5. exact statement of the bespoke sparse-centre zero-correlation theorem that would still suffice.

## Revised frontier

Two mathematically honest routes remain:

- return to the single-shell positive sampling target STL2;
- seek a direct arithmetic/sieve argument averaged over \(n\) that works before the explicit formula and survives the lacunarity of \(P_n\).

A generic almost-all short-interval theorem or standard pair-correlation conjecture cannot simply be imported.

## Decision

\[
\boxed{
\text{AAF explicit-formula route: STOP as an independent escape from PGD2.}
}
\]

Fortune's conjecture and the density-one version both remain open.
