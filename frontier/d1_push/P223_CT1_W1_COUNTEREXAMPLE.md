# Exact p=223 counterexample to the dominant one-level Cartier bound

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** exact counterexample to `CT1-w1`, strengthened by exact summation over every Cauchy-Binet degree set for the displayed identity set. The fixed-identity grouped coefficient remains nonzero. Cancellation across other identity sets or filtration blocks is not resolved.

## 1. Statement refuted

The dominant `w=1` programme proposed:

> If
>
> `det(P^(-1))_(R,E union {0})`
>
> and
>
> `det(U)_(R,E union {p-3})`
>
> are nonzero modulo `p`, and the torus grading holds, then
>
> `beta<=gamma+2`.

Equivalently, every nonzero dominant Cauchy-Binet product was expected to lie at or below

`B_1=(p-1)(p+3)/2`.

This is false.

## 2. Exact witness

Take

`p=223`,

`E={5,7,8,12,13,14,16,17,18}`

and

`R={49,71,94,119,122,126,130,141,148,220}`.

Then

`sum E=110`, `sum R=1220`.

With

`C_0=E union {0}`, `C_1=E union {220}`,

exact modular elimination gives

`boxed(det(P^(-1))_(R,C_0)=86 mod 223)`

and

`boxed(det(U)_(R,C_1)=169 mod 223)`.

The factorial complement is `123 mod 223` and the Jacobi sign is `+1`, so

`boxed(123*86*169=114 mod 223)`.

## 3. Independent original-minor verification

Let

`Omega={0,...,222}`,

`N={1,...,222}\E`,

`Q=(N\{220}) union {0}`,

`M=Omega\R`.

The original matrices have size `213x213`:

`P_(n,m)=(n)_m`,

`B_(q,m)=1/m! [X^q](X+X^3)^m`.

A separate calculation gives

`det P_(N,M)=86 mod 223`,

`det B_(Q,M)=48 mod 223`,

and

`boxed(det P_(N,M)det B_(Q,M)=114 mod 223)`.

Thus the large-minor and complementary-minor calculations agree exactly.

## 4. Torus grading and weight

The grading coordinates are

`gamma=2(sum E+1)/(p-1)=1`,

`beta=(sum R-sum E)/(p-1)=5`,

`alpha=(p+1-3beta-gamma)/2=104`.

Therefore

`2alpha+3beta+gamma=p+1`.

The monomial degrees are

`deg_a=445`,

`deg_c=23088=104(p-1)`,

`deg_d=1110=5(p-1)`.

Its filtration weight is

`W=(alpha+2beta)(p-1)=25308`.

The previous boundaries are

`B_0=(p^2-1)/2=24864`,

`B_1=(p-1)(p+3)/2=25086`.

Hence

`boxed(W=B_1+(p-1))`.

Equivalently `beta-gamma=4`, the first level excluded by `CT1-w1`.

## 5. Fixed-identity Cauchy-Binet assembly

The individual witness could in principle have cancelled against other degree sets `M` with the same identity set `E`. That possibility has now been tested exactly.

For fixed `E`, Cauchy-Binet and Jacobi give the generating determinant

`D_E(z)=det(A^T diag(r!z^r)U)`,

where

`A=P^(-1)_(Omega,E union {0})`

and

`U=U_(Omega,E union {220})`.

The coefficient

`[z^1220]D_E(z)`

is precisely the sum of all Cauchy-Binet products having this identity set and the required grading.

Exact Fourier inversion over `F_(223^2)^*` used all `49,728` nonzero field elements. The determinant polynomial has degree at most `2,175`, below the multiplicative order `49,728`, so there is no aliasing.

The result is

`boxed([z^1220]D_E(z)=114 mod 223)`.

The imaginary component in the quadratic field model is zero.

Therefore the nonzero second-extra-level contribution survives complete grouping over all degree sets for this fixed identity set.

## 6. Discovery and verification chain

- Adversarial discovery: `cartier_complementary_minor_counterexample_search.cpp`, CPU-XL job `6a6141a4d09dc1f57c6c346d`.
- Independent small and `213x213` verification: `p223_ct1_w1_counterexample_verify.py`, job `6a6145f413e6ef894d54c609`.
- Fixed-identity grouped Fourier assembly: `p223_fixed_identity_grouped_fourier.cpp`, job `6a61474513e6ef894d54c612`.

## 7. Consequence

The following are definitively refuted:

1. `CT1-w1`;
2. the claim that each dominant Cauchy-Binet product is confined to the old boundary plus one extra level;
3. the claim that summing degree sets for each identity set restores that one-level bound;
4. any proof of complete support based on termwise or fixed-identity support exclusion.

The following remain open:

1. cancellation among different identity sets `E` contributing to the same monomial;
2. cancellation between `w=1,2,3,4` blocks;
3. the complete dominant or full Cartier coefficient at weight `25308`;
4. Cartier nonvanishing at `p=223`;
5. the function-field `d=1` crown.

The correct Route-1 object is now the complete identity-set and four-block assembly.

## 8. Epistemic classification

- Witness grading: exact.
- Small complementary determinants: exact modulo 223.
- Original `213x213` determinant product: exact modulo 223.
- Fixed-identity grouped coefficient: exact modulo 223.
- Refutation of `CT1-w1` and fixed-identity one-level support: definitive.
- Complete coefficient after all identity sets and `w` blocks: open.
- Function-field `d=1` crown: open.
