# O2 — exact random-cover dual

## Bernoulli cover

Let every candidate offset be selected independently with probability `q`. A row with `Z_j` successful offsets is uncovered exactly when none of those successful offsets is selected. Thus

\[
\Pr(j\text{ uncovered})=(1-q)^{Z_j}.
\]

By linearity of expectation,

\[
\mathbb E[\#\text{ uncovered rows}]
=\sum_{j<N}(1-q)^{Z_j}.
\]

At `q=q_X`, this is exactly `INT-AOD`. Therefore `INT-AOD` says that a random constant-density sample has expected uncovered-row count below one, and hence some deterministic sample hits every row.

This is an interpretation, not a proof: the expected-value inequality remains the analytic target.

## Hypergeometric cover

Suppose every row uses the same candidate universe of size `M` and exactly `K` offsets are selected uniformly without replacement. A row with `Z` successful offsets is missed with probability

\[
H_{M,K}(Z)=
\frac{\binom{M-Z}{K}}{\binom{M}{K}}
=\prod_{r=0}^{K-1}\left(1-\frac{Z}{M-r}\right),
\]

with the convention that the value is zero when `K>M-Z`.

For `K/M=q+o(1)` and `Z=o(M)`,

\[
H_{M,K}(Z)=\exp\!\left(Z\log(1-q)+O\!\left(\frac{ZK}{M^2}+\frac{Z^2K}{M^2}\right)\right).
\]

The verifier must use an exact finite-product comparison rather than this asymptotic whenever it is used in a theorem.

## Weighted cover

For independent nonuniform selection probabilities `q_m`,

\[
\Pr(j\text{ uncovered})
=\prod_{m:I_{jm}=1}(1-q_m)
=\exp\!\left(-\sum_m a_mI_{jm}\right),
\]

where `a_m=-log(1-q_m)`.

This identifies the weighted occupancy detector with an explicit randomized covering process, subject to the O1 admissibility rule.

## Diagnostic outputs

Execution must record:

- candidate-universe size by row;
- the exact `q_X` and corresponding `K`;
- Bernoulli versus hypergeometric detector ratios;
- sample-budget sensitivity;
- whether any registered nonuniform profile improves the uniform detector before output incidences are observed.