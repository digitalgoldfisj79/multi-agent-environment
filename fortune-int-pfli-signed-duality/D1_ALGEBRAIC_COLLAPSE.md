# D1 — algebraic collapse of INT-PFLI

The factor-band closeout defines

\[
C_j=\sum_R I_j(R)
\]

as complete least-factor coverage and proves the exact partition

\[
|\mathcal A_j|=Z_j+C_j.
\]

Therefore

\[
C_j-|\mathcal A_j|+\gamma_j
=C_j-(Z_j+C_j)+\gamma_j
=\gamma_j-Z_j.
\]

Taking positive parts gives the pointwise identity

\[
\boxed{
(C_j-|\mathcal A_j|+\gamma_j)_+
=(\gamma_j-Z_j)_+.
}
\]

Consequently

\[
\sum_{j<N}(C_j-|\mathcal A_j|+\gamma_j)_+^2
=
\sum_{j<N}(\gamma_j-Z_j)_+^2.
\]

## Ruling

`INT-PFLI` is not an independent factor-incidence theorem. Once complete coverage is summed across every factor band, it is exactly the prime-pair count lower-tail theorem at threshold `gamma_j`.

The factor decomposition remains useful for diagnosing why classical lower sieves fail, but it supplies no additional cancellation after the exact partition is recombined. Any proof that estimates `C_j` to the required precision has, in substance, estimated `Z_j` to the same precision.

This identity is kernel-checked in `FortuneFormal/Integer/SoftDefectCriterion.lean`.
