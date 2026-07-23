# Phase Z4 geometric direct-image status

**Date:** 2026-07-23  
**Job:** `6a619e9dd09dc1f57c6c3cdf`  
**Status:** exact finite extension-field census completed; no small recurrence or bounded-rank theorem obtained.

## Computation

For the first unresolved upper hook

`V_(p-3)=V_2 tensor sign`,

all Frobenius cycle types were counted for every admissible `q` and every `t` over:

- `p=7`, extensions `j=1,...,7`;
- `p=11`, extensions `j=1,...,5`;
- `p=13`, extensions `j=1,...,4`.

The hook character was evaluated exactly from each cycle type and summed over the complete q-line.

The q-averaged sequences are:

- `p=7`: `[-1,39,77,255,-581,-315,21363]`;
- `p=11`: `[8,124,-124,3676,243]`;
- `p=13`: `[5,109,-139,4613]`.

## Recurrence test

Berlekamp–Massey over two independent large primes returned degrees:

- `4` for the length-7 sequence at `p=7`;
- `3` for the length-5 sequence at `p=11`;
- `2` for the length-4 sequence at `p=13`.

These are the generic maximal degrees allowed by the available sequence lengths. Therefore the result is **not** evidence for recurrences of orders 4, 3 or 2. It says that no shorter recurrence is visible in the exact data.

The normalized values reach approximately `23.54`, `30.38` and `27.30` respectively. Before boundary and known-factor subtraction these do not constitute primitive-rank lower bounds, but they rule out treating the total q-averaged upper-hook signal as numerically tiny.

## Consequence

The simple bounded-rank model is not supported by this census. Route 3 remains live only through a genuine geometric decomposition of the total sign-cover space, with explicit removal of boundary, `B_q`, `D_q` and Tate factors. Additional extension brute force alone has rapidly diminishing value.

No general-prime positivity statement or d=1 crown follows from this finite computation.
