# Phase Z4 direct dynamics calibration

**Date:** 2026-07-23  
**Job:** `6a61a21c13e6ef894d54cae9`  
**Status:** exact exhaustive height-3 calibration below 500; no universal map or small fixed menu found.

## Search

For every odd prime `p<500`, the computation tested all `2,058` integral cubic tails

`g(T)=-(aT^3+bT^2+cT+d)`

with `0<|a|<=3` and `|b|,|c|,|d|<=3`. Each positive result is an exact Rabin certificate that

`T^p+aT^3+bT^2+cT+d`

is irreducible; by the established equivalence it therefore supplies an exact `g`-composition-period-`p` point.

## Exact negative findings

No height-3 cubic map works at the following primes:

`227,419,439,461,463,487,491,499`.

The separate `p=5` failure is affected by the known small-characteristic leading/cubic collision and is not used as evidence about the general regime.

The most successful fixed map,

`(a,b,c,d)=(-2,-1,0,-2)`,

works at only eight primes below 500:

`7,11,13,23,61,197,223,373`.

Its involution mate has identical coverage. The next fixed pair covers seven primes.

The first-witness union already contains `143` different maps, and the greedy menu remains large, with many maps adding only one prime. This is not a minimum set-cover proof over all maps, but it is a strong exact negative result against a universal or very small fixed low-height menu.

## Consequence

The direct dynamical route remains logically open, but a successful construction is unlikely to be one fixed low-height cubic or a short empirical menu. It needs a map depending algebraically on `p` or on a controlled arithmetic class of `p`, together with a proof of exact period.

A height-4 search below 1500 is running separately. Finite witness coverage does not constitute a general-prime theorem.
