# Phase Z4 direct dynamics status

**Date:** 2026-07-23  
**Job:** `6a619f4b13e6ef894d54cabd`  
**Status:** exhaustive bounded-height cubic search complete below 1500; height 4 is not a uniform dynamical mechanism.

## 1. Exact search

For every odd prime `p<1500`, the computation tested all `5,832` cubic tails

`aT^3+bT^2+cT+d`

with `a!=0` and

`|a|,|b|,|c|,|d|<=4`.

Each successful tail was certified by the exact Rabin criterion for

`T^p+aT^3+bT^2+cT+d`.

By the established dynamical equivalence, each success is also an exact composition-period-`p` certificate for the associated cubic map.

## 2. Exact failure set

The complete height-4 family has no witness at

`p=571,701,751,761,773,839,859,887,971,977,1009,1033,1091,1093,1151,1171,1187,1201,1223,1229,1249,1291,1301,1367,1381,1409,1423,1433,1459,1481,1489,1493,1499`.

These are `33` nondegenerate failures. For each of them, all `5,832` candidates were tested exactly.

The separate `p=5` failure is affected by the known small-characteristic collision and is not counted as evidence about the general regime.

The first genuine failure occurs at `p=571`. Failure frequency then increases materially with `p` in the audited range.

## 3. Fixed-map and menu behaviour

The first-three-witness union contains `493` distinct maps. The best fixed map,

`(a,b,c,d)=(-2,-1,0,-2)`,

works at only eight audited primes:

`7,11,13,23,61,197,223,373`.

No finite menu formed from the height-4 family can cover the exact failure primes, because no member of the family works there.

## 4. Consequence

The following direct-dynamics mechanisms are now closed:

1. one universal cubic map with coefficient height at most 4;
2. a finite menu drawn from all height-4 cubic maps;
3. the assertion that every prime admits some height-4 cubic exact-period witness.

The general dynamical route remains logically open. It must use at least one of:

- coefficients whose height grows with `p`;
- a map selected by a substantive arithmetic invariant of `p`;
- a higher-degree tail;
- a structural exact-period argument not based on bounded coefficient enumeration.

The computation does not prove or refute the unrestricted direct dynamical conjecture, the function-field d=1 crown, or the integer Fortune conjecture.
