# Literature audit for the occupancy lane

## János Pintz, *On the singular series in the prime k-tuple conjecture* (2010)

Source: https://arxiv.org/abs/1004.1084

Pintz proves forms of Gallagher's average singular-series result with explicit uniformity as the tuple size grows, when the shift interval is sufficiently large relative to `k`.

**Permitted use:** local-factor averaging and the tuple-size audit in `RUHL-FM`.

**Not supplied:** prime-tuple counts at a fixed or selected increasing-primorial centre; the weighted one-row error required in O6.

## Vivian Kuperberg, *Sums of singular series with large sets and the tail of the distribution of primes* (2022)

Source: https://arxiv.org/abs/2210.09775

Kuperberg studies singular-series sums for growing set size and obtains asymptotics in ranges including logarithmically growing tuple sets, with prime-tail applications conditional on a uniform Hardy--Littlewood conjecture.

**Permitted use:** confirm that local singular-series averaging is not the tuple-order bottleneck for `K=Theta(log X)`.

**Not supplied:** the selected-centre Hardy--Littlewood count or its exponentially small weighted aggregate error.

## Abhishek Jha, *The Poisson Tail Conjecture for Primes in Short Intervals* (2026)

Source: https://arxiv.org/abs/2605.23014

Jha proves conditional Poisson-tail asymptotics for slowly growing interval parameters under a strong Hardy--Littlewood hypothesis.

**Permitted use:** benchmark the Bonferroni order and the type of concentration expected after sufficiently uniform tuple estimates.

**Not supplied:** an unconditional theorem at logarithmic-square windows centred on primorials or a transfer to the multiplicative primorial path.

## John Friedlander and Henryk Iwaniec, *Asymptotic sieve for primes* (1998)

Source: Annals of Mathematics 148, 1041--1065; DOI 10.2307/121035.

The asymptotic sieve can detect primes when classical divisor information is supplemented by a separate parity-breaking bilinear hypothesis.

**Permitted use:** define the logical role of the O7 bilinear input.

**Not supplied:** the required row-uniform bilinear estimate for the sequence `Lambda(m)` at the sparse shifts `P_j+m`, particularly beyond the `sqrt(H)` post-level boundary.

## Execution conclusion

The literature supports two conditional interfaces but no unconditional bridge:

1. `RUHL-FM` through order `Theta(log X)` implies the stratified occupancy detector;
2. a rowwise asymptotic-sieve implementation would require the new `INT-RPBH` sparse-hyperbola bilinear theorem.

Neither required input is presently an established theorem in the audited literature.

## Governing literature rule

No external result is considered a bridge until the programme verifies all of:

1. the averaging variable matches the increasing primorial centres;
2. the offset range includes `H=eta X^2`;
3. tuple-size or cluster-size uniformity reaches the required range;
4. the error remains below the absolute one-defect margin;
5. actual primes, rather than almost primes, are detected.
