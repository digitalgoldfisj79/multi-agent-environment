# O7 — rowwise parity-breaking dual

This lane is independent of the connected-cumulant route.

## Source

Use the weighted prime-pair source

\[
S_j(H)=\sum_{2\le m\le H}\Lambda(m)\Lambda(P_j+m).
\]

A lower bound of the correct order for every row implies many prime-pair offsets after the explicit prime-power contribution is removed.

## Required decomposition

Apply a registered Vaughan, Heath–Brown, or asymptotic-sieve identity to the second von Mangoldt factor and retain the first prime variable exactly. The resulting pieces must be grouped into:

- Type I divisor sums with divisor `d<=D_1`;
- balanced Type II bilinear sums;
- large-divisor terms requiring cofactor switching;
- proper-prime-power and endpoint remainders.

Because `P_j` is exponentially large while `m<=H=Theta(X^2)`, a divisor of `P_j+m` may be far larger than the summation variable. The programme must write the large-divisor dual exactly rather than importing a long-interval Type I/II template.

## One-row requirement

Every estimate must hold uniformly for each registered `j`, or in an aggregate norm whose threshold is strictly below one failed row. Statements allowing `o(N)` exceptional centres do not pass.

## Candidate terminal theorem

Define `INT-RPBB` only after the decomposition is explicit:

> **INT-RPBB — rowwise parity-breaking bilinear bound.** The registered Type I, Type II, switched, and remainder pieces combine to give
> \[
> S_j(H)>B_j
> \]
> for every sufficiently large registered row.

A softer aggregate version is admissible only if it implies `INT-AOD` with the full detector calculation shown.

## Audit checklist

For every bilinear piece record:

- both variable ranges;
- coefficient `l2` and divisor norms;
- modulus range;
- use of `P_j=A_XQ_j`;
- smooth-modulus coherence already identified in PR #49;
- target saving in absolute units;
- whether actual primes or almost primes are detected.

## Stop conditions

Close the lane if:

1. the required bilinear input is simply a restatement of the original rowwise prime-pair lower bound;
2. Cauchy–Schwarz or absolute values lose more than the one-row margin;
3. the available distribution level ends before the post-level factor range;
4. switching produces only a prime/almost-prime result;
5. any unregistered exceptional set remains.