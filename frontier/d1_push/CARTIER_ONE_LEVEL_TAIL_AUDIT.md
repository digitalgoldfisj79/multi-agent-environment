# Tail-inclusive Cartier ledger and the one-extra-level phenomenon

**Date:** 2026-07-22  
**Status:** exact finite audit through `p=47`; the corrected support statement remains conjectural. This advances Phase Z, Route 1.

## 1. Exact projection

`cartier_weight_resolved_ledger.cpp` evaluates the complete Cartier cofactor after

`c=c_0t,  d=d_0t^2`.

Exact summation over `c_0,d_0 in F_p` projects to positive exponents divisible by `p-1`; multiplicative Fourier inversion over `F_(p^2)^*` separates every `(1,2)`-weight. An exact Hungarian assignment bound proves that all polynomial degrees are below `p^2-1`, excluding Fourier aliasing.

The complete ledgers are recorded in

`cartier_weight_resolved_full_results.csv`.

Relevant Hugging Face CPU-XL jobs are:

- `6a61214013e6ef894d54c372`: independent p=29 complete-determinant counterexample audit;
- `6a612671d09dc1f57c6c31b6`: p=23,29,31 weight ledgers;
- `6a61283ed09dc1f57c6c31e0`: p=37,41,43 weight ledgers;
- `6a612c1713e6ef894d54c440`: p=47 out-of-sample ledger.

## 2. Exact finite result

Put

`B_0(p)=(p^2-1)/2=(p-1)(p+1)/2`

and

`B_1(p)=(p-1)(p+3)/2.`

The old support theorem at `B_0` is false from `p=29` onward. The complete finite audit proves:

- for every prime `5<=p<=23`, all nonzero torus survivors have weight at most `B_0(p)`;
- for every audited prime `29<=p<=47`, the tail above `B_0` is nonzero;
- every audited nonzero survivor has weight at most `B_1(p)`;
- whenever the tail is nonzero, it is supported only at the single weight `B_1(p)`.

Equivalently, all audited exponents satisfy

`boxed(alpha+2beta <= (p+3)/2).`

This is a finite theorem only.

## 3. Complete top-tail ledger

All entries are modulo `p`.

| p | square tail | nonsquare tail | tail weight |
|---:|---:|---:|---:|
| 23 | 0 | 0 | none |
| 29 | 22 | 14 | 448 |
| 31 | 10 | 12 | 510 |
| 37 | 6 | 18 | 720 |
| 41 | 1 | 26 | 880 |
| 43 | 39 | 33 | 966 |
| 47 | 21 | 6 | 1150 |

There is no systematic vanishing at the extra level.

## 4. Lower filtration blocks are essential

The top coefficient agrees between `w=1` and the complete matrix at `p=29,31,37`, but this ceases at `p=41`:

| p | class | w=1 top | full top |
|---:|---|---:|---:|
| 41 | square | 16 | 1 |
| 41 | nonsquare | 30 | 26 |
| 43 | square | 19 | 39 |
| 43 | nonsquare | 30 | 33 |
| 47 | square | 16 | 21 |
| 47 | nonsquare | 28 | 6 |

Therefore a dominant-substitution-minor theorem cannot determine the actual tail. The correct object is the complete `w=1,2,3,4` torus projection.

## 5. Certificate cross-check

For every audited prime and class, the sum of all resolved weights equals exactly

`3aN_a(p) mod p.`

Examples:

- `p=29`, square: `28+22=21=3*36 mod 29`;
- `p=41`, square: `26+1=27=3*50 mod 41`;
- `p=43`, nonsquare representative `a=2`: `11+33=1=6*36 mod 43`;
- `p=47`, nonsquare representative `a=5`: `30+6=36=15*40 mod 47`.

Thus the tail is a genuine component of the irreducibility certificate.

## 6. Corrected Route-1 target

### Conjecture CT1 — one-extra-level support

For every prime `p>=5`, every torus-surviving coefficient of the complete Cartier cofactor satisfies

`alpha+2beta <= (p+3)/2.`

A proof must assemble all four filtration blocks. If CT1 holds, the certificate has only `O(p)` weight levels and one new top-tail layer. The remaining problem is then exact evaluation or nonvanishing of the assembled weight sum.

CT1 is verified only through `p=47`. A second support failure at a larger prime remains possible, and CT1 alone would not prevent cancellation of the total certificate.

## 7. Epistemic classification

- Projection and no-aliasing method: exact.
- Full ledgers through `p=47`: exact finite arithmetic.
- Necessity of lower filtration blocks: exact.
- CT1: open conjecture.
- Top-tail formula and total nonvanishing: open.
- Function-field d=1 crown: open.
