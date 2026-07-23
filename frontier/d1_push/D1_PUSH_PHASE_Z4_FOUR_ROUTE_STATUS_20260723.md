# d=1 crown push — Phase Z4 four-route big-compute status

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** all four scientifically live routes were executed with exact large compute. The programme has gained one strong positive structural target, one useful geometric reduction, and two substantial negative route calibrations. No general-prime d=1 theorem has been proved.

## 1. Executive assessment

The four routes do not emerge equally strong.

1. **Quantized residue conversion is now the leading route.** Exact counts through `p=701` remain positive, below `3p/2`, and empirically satisfy a much sharper square-root-scale envelope around `p`.
2. **Fixed-dimensional motives remain live and have become more concrete.** Cubic mixed residuals continue to be `O(p)` in a large exact range, and the linear–cubic surface has been reduced birationally to a quartic cover with one explicit irreducible primitive branch factor.
3. **The simple geometric bounded-rank fingerprint failed.** Raw upper-hook q-averages do not exhibit a short recurrence; Route G requires an actual decomposition and subtraction of known and boundary factors.
4. **Bounded-height direct dynamics is decisively negative.** Height 4 fails at 33 nondegenerate primes below 1500, beginning at `p=571`. Any surviving direct route must be genuinely p-dependent or leave bounded cubic tails.

The function-field d=1 crown and integer Fortune conjecture remain open.

## 2. Route Q — quantized residue conversion

### Exact large-prime counts

For the depressed slice count `N_a(p)`, the new exact square/nonsquare pairs are:

- `p=401`: `(362,370)`;
- `p=503`: `(480,466)`;
- `p=601`: `(516,488)`;
- `p=701`: `(628,642)`.

All are even, positive and below `3p/2`, hence below the critical `2p` quantization threshold. The new FLINT composition counter was independently cross-checked against the original C++ implementation at `p=101`, where both returned `(76,116)`.

### Stronger empirical law

Across the complete exact ledger through `p=293` together with `401,503,601,701`,

`max |N_a-p|/sqrt(p)=4.875086...`.

Thus the natural theorem target has sharpened from

`0<N_a<2p`

to

`N_a=p+O(sqrt(p))`.

A fixed-complexity Weil bound of this form would imply positivity and the `2p` gate for all sufficiently large primes, with a finite check for the remainder.

A comparison against `1,676` small elliptic curves found no exact or stable short elliptic decomposition. The prospective trace object is therefore not an obvious small direct sum of elliptic curves.

### Gate

Construct a fixed-complexity curve, surface or sheaf whose Frobenius trace is `N_a-p`, or otherwise prove a uniform square-root-scale estimate.

## 3. Route G — geometric direct-image pairing

For the first unresolved upper hook `V_(p-3)=V_2 tensor sign`, exact extension-field cycle censuses gave q-averaged sequences:

- `p=7`: `[-1,39,77,255,-581,-315,21363]`;
- `p=11`: `[8,124,-124,3676,243]`;
- `p=13`: `[5,109,-139,4613]`.

Berlekamp–Massey degrees `4,3,2` are the generic maximal values for sequence lengths `7,5,4`; they do not constitute short recurrences. The unprocessed upper-hook signal is not numerically tiny.

### Gate

Construct the total sign-cover cohomology, remove the `B_q`, `D_q`, boundary and Tate components exactly, and only then bound or identify the primitive complement. Additional raw extension-field enumeration without that subtraction has low marginal value.

## 4. Route M — fixed-dimensional motives and all-degree sieve

### Large cubic sweep

Both square classes were evaluated exactly for every prime `503<=p<=1999`, giving `416` cases. The largest cubic multiplicity remained `8`. The observed centered envelopes were:

- `|M_13-(p^2-1)/3|/p <= 1.89293`;
- `|M_23-(p^2-1)/6|/p <= 1.67280`;
- `|M_33-(p^2-1)/18|/p <= 1.03094`.

These data continue to support fixed-dimensional `O(p)` primitive traces. A library of `240` small elliptic traces and twists gave weak correlations and poor holdout prediction, so the simplest elliptic motive model is rejected.

### Exact X13 reduction

On `2aD-9y != 0`, the linear–cubic incidence surface is birational to a quartic cover in `D`. Its quartic discriminant factors as

`27 S^2 a^2 (8aS^2+30aSy^2+18ay^4+27y^2)^2 R_a(S,y)`.

For `a=1,2`, the primitive branch polynomial `R_a` has degrees

`deg_S=10`, `deg_y=18`, total degree `19`,

and is irreducible over `Q`.

This gives a concrete geometric object for compactification and Betti-number analysis, while explaining why a few elliptic factors did not fit the trace data.

### Gate

Resolve the affine boundary and excluded divisor, compactify and desingularize the quartic cover, compute algebraic components and Betti numbers, derive effective `O(p)` trace constants, and insert them into the signed all-degree sieve.

## 5. Route D — direct dynamics

### Height 3

All `2,058` nonzero-cubic tails of coefficient height at most 3 were tested at every odd prime below 500. Eight nondegenerate primes had no witness.

### Height 4

All `5,832` tails of coefficient height at most 4 were then tested at every odd prime below 1500. There are `33` nondegenerate failure primes:

`571,701,751,761,773,839,859,887,971,977,1009,1033,1091,1093,1151,1171,1187,1201,1223,1229,1249,1291,1301,1367,1381,1409,1423,1433,1459,1481,1489,1493,1499`.

The first failure is `p=571`. The first-three-witness union contains `493` maps, while the best fixed map works at only eight primes.

### Consequence and gate

The universal bounded-height cubic route and every finite menu drawn from the height-4 family are closed. The unrestricted dynamical route remains open only through coefficients growing with `p`, a substantive arithmetic selection rule, a higher-degree tail, or a structural exact-period theorem.

## 6. Updated priority

The recommended programme order is now:

1. **Route Q / geometric bridge:** explain `N_a-p` as a fixed-complexity Frobenius trace and prove `O(sqrt p)`.
2. **Route M:** compactify the X13 quartic cover and obtain effective Betti/trace bounds; continue the same treatment for X23 and the cubic-pair surface.
3. **Route G:** use the sign-cover decomposition to identify the same primitive objects from the representation-theoretic side.
4. **Route D:** retain only as an independent p-dependent construction route; discontinue bounded-height enumeration.

Routes Q, M and G now appear more likely to be different descriptions of the same missing fixed-complexity geometric invariant. Establishing that identification is the highest-value next theorem task.

## 7. Epistemic classification

### Exact finite computation

- depressed-slice counts through `p=701` at the stated primes and through `p=293` in the prior ledger;
- p101 cross-implementation equality;
- hook cycle censuses at `p=7,11,13`;
- cubic mixed moments for `503<=p<=1999`;
- height-3 and height-4 exhaustive dynamics sweeps in their stated ranges.

### Exact algebra

- X13 elimination to a quartic cover;
- factorisation of its quartic discriminant;
- irreducibility over `Q` of the primitive branch factor for `a=1,2`.

### Finite-data conjectures

- `N_a=p+O(sqrt p)`;
- uniform `O(p)` cubic mixed residuals with manageable constants.

### Open

- a uniform square-root bound for `N_a-p`;
- primitive cohomology and trace bounds for the cubic surfaces;
- the signed all-degree sieve;
- an unrestricted direct dynamical construction;
- the function-field d=1 crown;
- the integer Fortune conjecture.

The complete source/job/result inventory is `D1_PHASE_Z4_FOUR_ROUTE_MANIFEST_20260723.json`.
