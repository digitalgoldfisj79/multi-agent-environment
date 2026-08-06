# Programme gates

## D0 — source freeze

Freeze PR #51, issue #52, the exact partition `|A_j|=Z_j+C_j`, the compressed threshold `gamma_j`, and the one-defect implication. Reject any change of source, centre set, window, or failure definition.

## D1 — algebraic collapse audit

Prove and kernel-check

\[
(C_j-|\mathcal A_j|+\gamma_j)_+=(\gamma_j-Z_j)_+.
\]

Classify whether `INT-PFLI` is a genuinely new factor-incidence theorem or an exact rewriting of a prime-pair lower-tail theorem.

## D2 — adaptive occupancy reduction

Define

\[
\tau_X=2\log N/\gamma_{\min},
\qquad
\mathcal O_X=\sum_{j<N}e^{-\tau_XZ_j}.
\]

Prove:

1. `O_X<1` excludes every failed row;
2. `INT-PFLI` implies `O_X=o(1)`;
3. the occupancy criterion permits positive counts below `gamma_j`, so it is a strictly softer sufficient target.

## D3 — exact factorial expansion

Put `q_X=1-e^{-tau_X}`. Derive

\[
e^{-\tau_XZ_j}=(1-q_X)^{Z_j}
=\sum_{k=0}^{Z_j}(-q_X)^k\binom{Z_j}{k}.
\]

Record the Bonferroni upper and lower truncations and the exact aggregate factorial moments.

## D4 — finite-moment indistinguishability

For every integer `K>=0`, construct two panels of `2^K` nonnegative integer counts:

- one panel contains a zero count;
- the other contains no zero count;
- their ordinary and factorial moments agree through order `K`.

Use the even/odd binomial finite-difference construction and prove that, for any block with `N>=2^K`, padding preserves the obstruction. Conclude that a moment-only proof resolving one failed row requires

\[
K>\log_2N=\Theta(\log X).
\]

## D5 — prime-correlation arity audit

Expand

\[
\sum_j\binom{Z_j}{k}
\]

as a sum over `k` distinct candidate offsets. Each factor contains primality of `m_i` and `P_j+m_i`, so the `k`th factorial moment is a coupled `2k`-prime correlation. Quantify the resulting arity requirement `2K=Omega(log X)`.

## D6 — asymptotic-sieve and switching audit

Map the row sequence to the Friedlander–Iwaniec asymptotic-sieve axioms and to weighted switching. Verify the exact missing hypotheses rather than invoking either framework by analogy. In particular audit:

- row-uniform divisor sums for moduli beyond `sqrt(H)`;
- the required bilinear parity-breaking input;
- whether averaging over centres retains one-row resolution;
- whether switching produces a variable range with a positive distribution level.

A lane closes if it assumes the selected-centre theorem it is meant to prove, loses one-row resolution, or requires an unverified post-level distribution estimate.

## D7 — closeout

Allowed terminal outcomes:

1. `PROVED_INT_PFLI`;
2. `PROVED_ADAPTIVE_OCCUPANCY`;
3. `REDUCED_TO_ESTABLISHED_THEOREM`;
4. `REDUCED_TO_GROWING_ARITY_GENERATING_FUNCTION`;
5. `METHOD_OBSTRUCTED_AT_LOGARITHMIC_MOMENT_ORDER`.

No claim of Fortune is permitted unless the full implication and finite prefix are closed.