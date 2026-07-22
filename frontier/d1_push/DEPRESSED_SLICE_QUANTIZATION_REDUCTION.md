# Depressed-slice quantization: a complete residue certificate under a 2p bound

**Date:** 2026-07-22  
**Status:** exact conditional reduction plus exact finite audit. The quantization lemma is proved. The uniform size bound and positivity remain open.

## 1. Setup

For prime `p>=5` and `a!=0`, put

`N_a(p)=#{(c,d) in F_p^2 : X^p+aX^3+cX+d is irreducible}.`

The Cartier cofactor theorem gives

`S_a(p)=3a N_a(p) mod p.`

The affine involution theorem gives

`2|N_a(p)`.

Since `p` is odd, parity contains information not visible in the residue modulo `p`.

## 2. Exact quantization lemma

Let

`r_a=(3a)^(-1) S_a(p) mod p`,

chosen in `{0,1,...,p-1}`. Then `r_a=N_a mod p`.

### Theorem DSQ.1 — complete residue recovery below 2p

Assume

`0<=N_a(p)<2p.`

Then

`boxed( N_a(p)=r_a          if r_a is even,`

`        N_a(p)=r_a+p        if r_a is odd. )`

In particular,

`boxed( S_a(p)=0 mod p  iff  N_a(p)=0. )`

### Proof

The only integers in `[0,2p)` congruent to `r_a` modulo `p` are `r_a` and `r_a+p`. Since `p` is odd, exactly one of these is even. The proved parity of `N_a` selects it. If `r_a=0`, the two candidates are `0` and the odd integer `p`, so `N_a=0`.

Thus a uniform `2p` upper bound would promote the Cartier residue from a one-sided nonvanishing certificate to a complete exact count certificate.

## 3. Stronger finite phenomenon

The existing independently audited cubic-normal-form dataset gives exact values for both square classes of `a` for every prime

`5<=p<=293`.

In that complete range:

`boxed( 0<N_a(p)<3p/2<2p )`

for both square classes separately.

The largest observed ratio is

`N_1(7)/7=10/7`,

and the nearest later high value is

`N_1(127)/127=156/127`.

The finite statement is exact but is not promoted to a uniform theorem.

## 4. Independent recomputation in Phase Z

`depressed_slice_irreducible_count.cpp` implements an independent exact Rabin test specialised to

`X^p+aX^3+cX+d`.

For prime degree, irreducibility is equivalent to

`gcd(F,X^p-X)=1`

and

`X^(p^p)=X mod F`.

The implementation constructs the Frobenius map from the sparse relation

`X^p=-(aX^3+cX+d)`

and uses exact finite-field polynomial arithmetic.

It independently reproduces the dataset through `p=199`, and Hugging Face CPU-XL jobs reproduce selected larger values, including:

- `p=211`: `(184,190)`;
- `p=251`: `(224,222)`;
- the previously highlighted `p=127`: `(156,116)`.

The complete committed finite table is in

`depressed_slice_quantization_results.csv`.

## 5. Relationship to the tail-inclusive Cartier ledger

For every prime where both computations have been performed, the complete weight-resolved Cartier sum satisfies exactly

`sum_weights coefficient_a(weight)=3aN_a(p) mod p.`

Examples:

- `p=29`, square class: the full sum is `21`, equal to `3*36 mod 29`;
- `p=41`, square class: the full sum is `27`, equal to `3*50 mod 41`;
- `p=43`, nonsquare representative `a=2`: the full sum is `1`, equal to `6*36 mod 43`.

This independently checks that the tail-inclusive Fourier projection is assembling the original Cartier certificate correctly.

## 6. Correct uniform target

A sufficient quantized route to the d=1 crown is now:

### Bound QNV

For every prime `p>=5` and at least one square class of `a`,

`0<N_a(p)<2p.`

A stronger form, matching all current data, is

`0<N_a(p)<3p/2.`

The lower inequality proves the crown directly. The upper inequality makes the Cartier residue exact through DSQ.1. Equivalently, one may prove:

1. `N_a<2p` for both classes; and
2. `S_a!=0` for at least one class.

The second formulation separates the geometric size problem from the algebraic nonvanishing problem.

## 7. Why this is not yet a proof

The finite scan cannot establish QNV. Existing Weil-II control gives only

`N_a=p+O(p)`

with a constant not yet known to be below `1`. Proving `N_a<2p` requires winning precisely that constant battle. Proving positivity requires the corresponding lower constant or a separate nonvanishing congruence.

The new result is that the target constant is now exact and operational:

`|N_a-p|<p`

is enough to make the Cartier certificate complete, while the observed data suggests the stronger

`|N_a-p|<p/2`

apart from harmless small-prime endpoint effects.

## 8. Epistemic classification

- Cartier congruence: previously proved exact theorem.
- Evenness of `N_a`: previously proved exact theorem.
- DSQ.1: exact elementary theorem.
- Exact values through `p=293`: machine-certified finite theorem from the committed dataset.
- Independent Phase-Z spot and range checks: exact.
- Uniform `N_a<2p`: open.
- Uniform positivity: open.
- Function-field d=1 crown: open.
