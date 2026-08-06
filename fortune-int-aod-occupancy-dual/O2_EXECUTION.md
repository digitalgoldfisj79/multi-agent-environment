# O2 — exact random-cover dual execution

**Status:** PASSED

Let the candidate-offset universe have size `M`, and let row `j` contain `Z_j` successful columns.

## Bernoulli cover

Choose each candidate independently with probability `q`. A row is uncovered exactly when none of its `Z_j` successful columns is chosen, with probability

\[
(1-q)^{Z_j}.
\]

Therefore

\[
\mathbb E[\#\text{ uncovered rows}]
=\sum_{j<N}(1-q)^{Z_j}.
\]

If this expectation is below one, some preregistered random-cover realization covers every row. More importantly, a zero row makes the expectation at least one, so the inequality itself excludes failure independently of selecting a realization.

## Fixed-size cover

Choose exactly `K` columns uniformly. A row with `Z` successes is missed with probability

\[
\frac{\binom{M-Z}{K}}{\binom{M}{K}}
=\prod_{r=0}^{K-1}\left(1-\frac{Z}{M-r}\right).
\]

For `K/M=q+o(1)` and `Z=o(M)`, this is bounded above by

\[
\left(1-\frac KM\right)^Z
\]

and has logarithm

\[
-Z\frac KM+O\!\left(\frac{ZK^2+Z^2K}{M^2}\right)
\]

in the sparse regime. Exact identities, not asymptotic replacements, are used by the verifier.

## Kill ruling

The existence of a hitting set is not treated as independent arithmetic evidence. The only admissible proof route is an a priori bound on the expected uncovered-row detector or an exact deterministic certificate implying that bound.
