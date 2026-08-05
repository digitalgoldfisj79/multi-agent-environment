# Literature audit for the occupancy lane

## János Pintz, *On the singular series in the prime k-tuple conjecture* (2010)

Source: https://arxiv.org/abs/1004.1084

Pintz proves forms of Gallagher's average singular-series result with explicit uniformity as the tuple size grows. In particular, the paper gives lower estimates when the shift interval is sufficiently large relative to `k`, including ranges controlled by `exp(c k/log k)`.

**Permitted use:** control or benchmark averages of local singular-series constants over offset sets.

**Not supplied:** prime-tuple counts at a fixed or selected increasing-primorial centre; an error term uniform in the present exponentially large output size and polynomial offset window; one-row lower-tail resolution.

## Vivian Kuperberg, *Sums of singular series with large sets and the tail of the distribution of primes* (2022)

Source: https://arxiv.org/abs/2210.09775

Kuperberg studies singular-series sums for growing set size and obtains asymptotics in ranges such as `k=O((log h)^(1-delta))`, together with more general upper bounds. Applications to prime-count tails are conditional on a uniform Hardy-Littlewood conjecture for growing tuples.

**Permitted use:** quantify the local-factor and tuple-size range in the conditional benchmark.

**Not supplied:** the required row-uniform Hardy-Littlewood estimate itself; transfer from averaging over ordinary interval starts to the sparse primorial-centre path.

## Abhishek Jha, *The Poisson Tail Conjecture for Primes in Short Intervals* (2026)

Source: https://arxiv.org/abs/2605.23014

Jha proves conditional Poisson-tail asymptotics for slowly growing interval parameters under a strong Hardy-Littlewood hypothesis, combining extremal interval sieve estimates with concentration inequalities.

**Permitted use:** design the conditional occupancy benchmark and identify which concentration mechanisms can replace raw moment-by-moment estimates.

**Not supplied:** an unconditional theorem at logarithmic-square windows centred on primorials; a selected-centre parity-breaking estimate.

## Governing literature rule

No external result is considered a bridge until the programme verifies all of:

1. the averaging variable matches the increasing primorial centres;
2. the offset range includes `H=eta X^2`;
3. tuple-size or cluster-size uniformity reaches the required range;
4. the error remains below the absolute one-defect margin;
5. actual primes, rather than almost primes, are detected.
