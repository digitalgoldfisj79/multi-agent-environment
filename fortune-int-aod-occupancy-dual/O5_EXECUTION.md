# O5 — arithmetic connected-correlation execution

**Status:** EXACT ORDINARY-CUMULANT DECOMPOSITION PASSED; REDUCED TO `INT-SOCG`

## Exact coefficient identity

Fix a deterministic stratum `B_b` and a common candidate-offset universe. For a candidate column `m`, write

\[
I_m(J)=1_{\mathbb P}(m)1_{\mathbb P}(P_J+m),
\]

where `J` is uniform on the rows in the stratum. Then

\[
Z_J=\sum_m I_m(J).
\]

Let `c_{k,b}=Cum_b(Z_J,\ldots,Z_J)` be the ordinary cumulant of order `k`. Multilinearity gives the exact common-centre identity

\[
c_{k,b}
=
\sum_{m_1,\ldots,m_k}
\operatorname{Cum}_b(I_{m_1},\ldots,I_{m_k}),
\]

where the sum is over all ordered offset tuples, including repetitions, and

\[
\operatorname{Cum}_b(I_{m_1},\ldots,I_{m_k})
=
\sum_{\pi\in\Pi_k}
(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{C\in\pi}
\mathbb E_b\prod_{r\in C}I_{m_r}.
\]

The joint moments are selected-centre prime-tuple incidences

\[
\frac1{n_b}\sum_{j\in B_b}
\prod_{r\in C}1_{\mathbb P}(m_r)1_{\mathbb P}(P_j+m_r).
\]

Repeated offsets collapse inside each product because the indicators are idempotent. The verifier checks the complete identity exactly over rational arithmetic by comparing ordinary cumulants of `Z` with the sum over all ordered column tuples.

## Correction to the built conjectural identity

The initially built programme stated the analogous formula for factorial cumulants over distinct columns. That formula is false: factorial cumulants involve a more complicated partition/injection combinatorics and do not equal common-row joint cumulants over distinct columns. The O9 static audit detected this before closeout. The corrected ordinary-cumulant identity is the natural one for the exponential detector

\[
\log\mathbb E_b e^{-\tau Z_J}
=\sum_{k\ge1}c_{k,b}\frac{(-\tau)^k}{k!}.
\]

No theorem claim relies on the rejected factorial identity.

## Local arithmetic anatomy

- For every prime `p<=ell_j`, `P_j` is zero modulo `p` and every candidate prime `m>ell_j` is nonzero modulo `p`; all shifted outputs automatically avoid these small primes.
- For `p>ell_j`, forbidden residues are controlled by the collision pattern of the distinct offsets represented in the tuple and by the residue of the multiplicative primorial walk `P_j mod p`.
- The ordinary connected coefficient depends on cancellation across set partitions and across the selected `j`-orbit. Taking absolute values before the cumulant recombination recovers the raw high-correlation barrier.

## Complete-dependency obstruction

Viewed as random variables of the single row index `J`, all columns share the same underlying variable. The safe dependency graph is complete.

The total activity is

\[
\sum_m\mathbb E_b I_m=c_{1,b}\asymp X
\]

conditionally. At useful temperature

\[
\tau_b\asymp\log X/X,
\]

the complete-graph weighted activity is

\[
\tau_b c_{1,b}\asymp\log X.
\]

This exceeds every constant small-activity threshold. Generic absolute dependency-graph, Dobrushin, and Kotecky--Preiss criteria are therefore closed at the explicit scale `Theta(log X)`.

## Primary successor theorem — INT-SOCG

> **INT-SOCG — stratified ordinary-cumulant growth.** For a deterministic `B=polylog(X)` partition there are preregistered lower scales `L_b>=cX`, temperatures
> \[
> \tau_b=(1+3\varepsilon)\frac{\log(n_bB)}{L_b}\le\tau_A,
> \]
> and dependence scales
> \[
> D_b\ll X/(\log X)^{1+\delta}
> \]
> such that
> \[
> c_{1,b}\ge L_b
> \]
> and, for every `k>=2`,
> \[
> |c_{k,b}|\le c_{1,b}\,k!\,D_b^{k-1}.
> \]

The coefficient bound gives absolute convergence whenever `tau_bD_b<1`. Moreover,

\[
\sum_{k\ge2}\frac{\tau_b^k}{k!}|c_{k,b}|
\le
\tau_bc_{1,b}\frac{\tau_bD_b}{1-\tau_bD_b}.
\]

Since `tau_bD_b=O((log X)^(-delta))`, the higher connected contribution is `o(log(n_bB))`, while

\[
\tau_bc_{1,b}\ge(1+3\varepsilon)\log(n_bB).
\]

Thus, for sufficiently large `X`,

\[
-\log\mathbb E_b e^{-\tau_bZ_J}>\log(n_bB).
\]

Consequently

\[
\boxed{\mathrm{INT\!-\!SOCG}\Longrightarrow
\mathrm{INT\!-\!SOCB}\Longrightarrow
\mathrm{INT\!-\!AOD}\Longrightarrow
\text{eventual Fortune}.}
\]

`INT-SOCG` is not proved. It isolates the required signed arithmetic cancellation and an explicit subcritical dependence scale. No generic cluster theorem supplies it.
