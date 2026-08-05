# O5 — arithmetic connected-correlation execution

**Status:** EXACT DECOMPOSITION PASSED; GENERIC CLUSTER CRITERIA OBSTRUCTED

## Exact coefficient identity

Fix a deterministic stratum `B_b` and a common candidate-offset universe. For a prime candidate column `m`, write

\[
I_m(J)=1_{\mathbb P}(P_J+m),
\]

where `J` is uniform on the rows in the stratum. Then

\[
Z_J=\sum_m I_m(J).
\]

For every `k>=1`, the factorial cumulant satisfies the exact ordered-tuple identity

\[
\kappa_{k,b}
=
\sum_{m_1,\ldots,m_k\ \mathrm{distinct}}
\operatorname{Cum}_b(I_{m_1},\ldots,I_{m_k}),
\]

where

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
\prod_{r=1}^k1_{\mathbb P}(P_j+m_r).
\]

`verify_joint_cumulant_decomposition.py` verifies the identity exactly over rational arithmetic on finite incidence matrices.

## Local arithmetic anatomy

- For every prime `p<=ell_j`, `P_j` is zero modulo `p` and every candidate prime `m>ell_j` is nonzero modulo `p`. All shifted outputs therefore automatically avoid these small primes.
- For `p>ell_j`, the forbidden residues are controlled by the collision pattern of the offsets `m_r mod p` and by the residue of the multiplicative primorial walk `P_j mod p`.
- The connected coefficient therefore depends on cancellation across set partitions and across the selected `j`-orbit. Taking absolute values before this recombination reproduces the raw high-moment barrier.

## Complete-dependency obstruction

Viewed as random variables of the single row index `J`, all columns `I_m(J)` share the same underlying variable. No nontrivial independence graph is available; the safe dependency graph is complete.

The total column activity is

\[
\sum_m\mathbb E_b I_m=\kappa_{1,b}\asymp X
\]

conditionally. At the useful adaptive detector scale `q_b asymp log X/X`, the weighted neighbour activity of the complete graph is

\[
q_b\kappa_{1,b}\asymp\log X.
\]

This exceeds every constant Kotecky--Preiss or Dobrushin small-activity threshold. Generic absolute dependency-graph and polymer criteria are therefore closed at the explicit scale `Theta(log X)`.

## Smallest quantitative successor

A sufficient arithmetic growth condition is:

> **INT-SCG — stratified cumulant growth.** For a deterministic `polylog(X)` partition there are preregistered lower scales `L_b>=cX` and dependence scales
> \[
> D_b\ll X/(\log X)^{1+\delta}
> \]
> such that, for every `k>=2`,
> \[
> |\kappa_{k,b}|\le \kappa_{1,b}\,k!\,D_b^{k-1},
> \qquad \kappa_{1,b}\ge L_b.
> \]

Choose

\[
q_b=(1+3\varepsilon)\log(n_bB)/L_b.
\]

Then `q_bD_b=O((log X)^{-delta})` and

\[
\sum_{k\ge2}\frac{q_b^k}{k!}|\kappa_{k,b}|
\le
q_b\kappa_{1,b}\frac{q_bD_b}{1-q_bD_b}
=o(\log n_b).
\]

Thus `INT-SCG => INT-SCCB => INT-AOD` for sufficiently large `X`.

`INT-SCG` is not proved. It isolates the required signed arithmetic cancellation and the exact dependence scale; no generic cluster theorem supplies it.
