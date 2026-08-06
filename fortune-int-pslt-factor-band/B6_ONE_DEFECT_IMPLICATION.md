# B6 — one-defect implication

Let

\[
A_j=|\mathcal A_j|,
\qquad
C_j=\sum_R I_j(R),
\qquad
Z_j=A_j-C_j.
\]

Choose

\[
\gamma_j=\left\lceil\frac{B_j}{\log P_j}\right\rceil
\]

with the harmless adjustment needed to account for `log(P_j+m)>=log P_j`.

If

\[
C_j\le A_j-\gamma_j,
\]

then `Z_j>=gamma_j`, and the prime outputs alone contribute at least `B_j` to the shifted von Mangoldt source. Proper prime powers contribute nonnegatively.

Define

\[
\mathcal E_{\mathrm{fac}}(X)=
\sum_{j<N}(C_j-A_j+\gamma_j)_+^2.
\]

At a failed row, `C_j=A_j`, so its summand is exactly `gamma_j^2`. Therefore

\[
\boxed{
\mathcal E_{\mathrm{fac}}(X)
=o\!\left((\min_j\gamma_j)^2\right)
}
\]

excludes all failed rows for sufficiently large `X`.

The abstract complete-coverage implication is kernel checked in

`FortuneFormal/Integer/FactorBandCriterion.lean`.

## Consequence chain

\[
\text{INT-PFLI}
\Longrightarrow
\text{compressed variable-threshold INT-PSLT}
\Longrightarrow
\text{no sufficiently large failed centre}
\Longrightarrow
\text{eventual Fortune}.
\]

The finite prefix remains separately decidable.

## Honesty boundary

`INT-PFLI` is not proved. It is the exact signed aggregate theorem left after the Buchstab/factor-band audit. It cannot be replaced by independent absolute estimates for each dyadic band because the accumulated `O(1)` band error exceeds the total `Theta(log X)` one-row margin.
