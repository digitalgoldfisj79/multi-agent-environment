# Tail-inclusive Cartier ledger and the one-extra-level phenomenon

**Date:** 2026-07-22  
**Status:** exact finite audit through `p=47`; corrected support statement remains conjectural. This advances Phase Z, Route 1.

## 1. Exact projection computed

For the complete Cartier cofactor

`D_a(c,d)=det(I-H)_(row p,column 3 deleted)`,

set

`c=c_0 t,  d=d_0 t^2`.

The committed program `cartier_weight_resolved_ledger.cpp` performs:

1. exact summation over `c_0,d_0 in F_p`, which projects to positive exponents of `c,d` divisible by `p-1`;
2. exact multiplicative Fourier inversion over `F_(p^2)^*`, which separates every `(1,2)`-weight;
3. an exact Hungarian assignment bound proving that every polynomial degree is below `p^2-1`, so there is no Fourier aliasing.

Both square classes of `a` are computed, first with `w=1` only and then with the complete `w=1,2,3,4` Cartier matrix.

The full ledgers are in

`cartier_weight_resolved_full_results.csv`.

Hugging Face CPU-XL jobs:

- `6a612671d09dc1f57c6c30f8`: independent p=29 full counterexample audit;
- `6a612671d09dc1f57c6c31b6`: p=23,29,31 weight ledgers;
- `6a61283ed09dc1f57c6c31e0`: p=37,41,43 weight ledgers;
- `6a612c1713e6ef894d54c440`: p=47 out-of-sample ledger.

## 2. Exact finite support result

Put

`B_0(p)=(p^2-1)/2=(p-1)(p+1)/2`

and

`B_1(p)=(p-1)(p+3)/2.`

The former proposed theorem asserted support at most `B_0`; it is false from `p=29` onward.

The complete finite audit gives:

- for every prime `5<=p<=23`, all nonzero torus-surviving coefficients have weight at most `B_0(p)`;
- for every audited prime `29<=p<=47`, above-bound coefficients are nonzero;
- in every audited case, every nonzero coefficient has weight at most `B_1(p)`;
- whenever the tail is nonzero, it is supported only at the single weight `B_1(p)`.

Thus the first failed cutoff has, so far, expanded by exactly one orthogonality level:

`boxed( B_0(p) -> B_1(p). )`

Equivalently, in exponent coordinates

`deg_c=alpha(p-1),  deg_d=beta(p-1)`,

the finite data satisfy

`boxed( alpha+2beta <= (p+3)/2. )`

This is an exact finite theorem for the audited primes, not a claimed uniform theorem.

## 3. Tail transition

The tail sums for the complete matrix are:

| p | square tail | nonsquare tail | tail weight |
|---:|---:|---:|---:|
| 23 | 0 | 0 | none |
| 29 | 22 | 14 | 448 |
| 31 | 10 | 12 | 510 |
| 37 | 6 | 18 | 720 |
| 41 | 1 | 26 | 880 |
| 43 | 39 | 33 | 966 |
| 47 | 21 | 6 | 1150 |

All values are modulo `p`.

There is no sign of decay or systematic cancellation at the extra level. A successful tail-inclusive theorem must evaluate or pair this coefficient; merely bounding its rank is insufficient for nonvanishing.

## 4. Lower filtration blocks matter

At `p=29,31,37`, the top-tail coefficient happens to agree between the dominant `w=1` block and the complete matrix.

That agreement is not structural. Starting at `p=41`:

| p | class | w=1 top | full top |
|---:|---|---:|---:|
| 41 | square | 16 | 1 |
| 41 | nonsquare | 30 | 26 |
| 43 | square | 19 | 39 |
| 43 | nonsquare | 30 | 33 |
| 47 | square | 16 | 21 |
| 47 | nonsquare | 28 | 6 |

Therefore the dominant substitution-minor object does not determine the tail by itself. The correct object is the complete `w=1,2,3,4` torus projection.

This answers Phase Z question 1.2 negatively for any approach that discards the lower filtration blocks as harmless corrections.

## 5. Certificate assembly check

For every audited prime and square class, summing all weight coefficients gives exactly

`3aN_a(p) mod p.`

Examples:

- `p=29`, square: `28+22=21 mod 29=3*36 mod 29`;
- `p=41`, square: `26+1=27 mod 41=3*50 mod 41`;
- `p=43`, nonsquare representative `a=2`: `11+33=1 mod 43=6*36 mod 43`;
- `p=47`, nonsquare representative `a=5`: `30+6=36 mod 47=15*40 mod 47`.

This independently validates the exact projection and confirms that the tail is part of the original irreducibility certificate.

## 6. Corrected algebraic target

The highest-value Route-1 theorem is now:

### Conjecture CT1 — one-extra-level Cartier support

For every prime `p>=5`, every torus-surviving coefficient of the complete Cartier cofactor satisfies

`alpha+2beta <= (p+3)/2.`

Unlike the refuted cutoff, CT1 explicitly allows the p=29 counterexample and every subsequently observed tail.

A proof must use the complete filtration assembly. The exact substitution-minor formula remains useful for the `w=1` part, but the p=41,43,47 ledgers prove that a theorem solely about those minors cannot determine the top coefficient.

After CT1, the certificate would consist of only `O(p)` weight levels and one new top-tail layer. The remaining task would be an exact formula or nonvanishing law for the assembled coefficients, especially the `B_1(p)` term.

## 7. Limits

The audit does not prove CT1. A second support failure may occur at a larger prime. No inference from seven primes is sufficient for a uniform determinant theorem.

Even if CT1 is true, support alone does not prove `S_a!=0`: the low and top coefficients can cancel in the total sum.

## 8. Epistemic classification

- Projection algorithm and no-aliasing bounds: exact.
- Complete ledgers through `p=47`: exact finite arithmetic.
- Equality with the Cartier certificate: exact finite cross-check.
- Need to retain `w=2,3,4`: exact counterexample to dominant-only assembly.
- CT1: open conjecture, supported through `p=47`.
- Top-tail evaluation: open.
- Function-field d=1 crown: open.
