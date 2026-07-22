# Exact p=223 counterexample to the dominant one-level Cartier minor bound

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** exact counterexample to `CT1-w1`. Independently verified through both complementary 10x10 minors and the original 213x213 Cauchy-Binet determinant product. This does **not** by itself prove that the fully grouped Cartier coefficient at this weight is nonzero.

## 1. Statement refuted

The dominant `w=1` reduction had isolated the following proposed lemma.

> If the two complementary minors
>
> `det(P^(-1))_(R,E union {0})`
>
> and
>
> `det(U)_(R,E union {p-3})`
>
> are both nonzero modulo `p`, and the torus grading holds, then
>
> `beta <= gamma+2`.

Equivalently, every nonzero dominant Cauchy-Binet product was conjectured to lie at or below the corrected one-extra-level boundary

`B_1=(p-1)(p+3)/2`.

This statement is false.

## 2. Exact witness

Take

`p=223`,

`E={5,7,8,12,13,14,16,17,18}`

and

`R={49,71,94,119,122,126,130,141,148,220}`.

Thus

`sum E=110`, `sum R=1220`.

The complementary column sets are

`C_0=E union {0}`

and

`C_1=E union {220}`.

Exact modular Gaussian elimination gives

`boxed(det(P^(-1))_(R,C_0)=86 mod 223)`

and

`boxed(det(U)_(R,C_1)=169 mod 223)`.

Both are nonzero.

The factorial complement and Jacobi sign are

`product_(r in R) r! =123 mod 223`,

`epsilon=+1`.

Therefore the complementary product is

`123*86*169=114 mod 223`,

which is nonzero.

## 3. Independent large-minor verification

Let

`Omega={0,...,222}`,

`N={1,...,222}\E`,

`Q=(N\{220}) union {0}`,

`M=Omega\R`.

The original matrices have size `213x213`:

`P_(n,m)=(n)_m`,

`B_(q,m)=1/m! [X^q](X+X^3)^m`.

A separate direct calculation, without using the small-minor determinants, gives

`det P_(N,M)=86 mod 223`,

`det B_(Q,M)=48 mod 223`,

and hence

`boxed(det P_(N,M) det B_(Q,M)=114 mod 223)`.

This agrees exactly with the complementary product.

## 4. Torus grading and filtration weight

The identity grading coordinate is

`gamma=2(sum E+1)/(p-1)=1`.

The constant-term coordinate is

`beta=(sum R-sum E)/(p-1)=5`.

The linear coordinate is

`alpha=(p+1-3beta-gamma)/2=104`.

Thus

`2alpha+3beta+gamma=208+15+1=224=p+1`,

so this is an exact torus survivor.

Its coefficient degrees are

`deg_a=445`,

`deg_c=alpha(p-1)=23088`,

`deg_d=beta(p-1)=1110`.

The `(1,2)` filtration weight is

`W=(alpha+2beta)(p-1)=114*222=25308`.

The old and corrected boundaries are

`B_0=(p^2-1)/2=24864`,

`B_1=(p-1)(p+3)/2=25086`.

Therefore

`boxed(W=B_1+(p-1)=25308)`.

Equivalently,

`beta-gamma=4`,

which is exactly the first level forbidden by `CT1-w1`.

## 5. Discovery and verification chain

The witness was found by the exact randomized adversarial search

`cartier_complementary_minor_counterexample_search.cpp`

on Hugging Face CPU-XL job

`6a6141a4d09dc1f57c6c346d`.

The job sampled only exact torus-graded configurations with `beta>=gamma+4`. At `p=223` it found the displayed witness after `9,470` sampled configurations.

Independent verification was then performed by

`p223_ct1_w1_counterexample_verify.py`

on job

`6a6145f413e6ef894d54c609`.

The verifier reconstructs both the complementary minors and the original large determinant product from their definitions.

## 6. Consequence

The following are now refuted:

1. `CT1-w1`;
2. the claim that every individual dominant grouped Cauchy-Binet product occupies only the old boundary or the first extra level;
3. a proof of the corrected complete support conjecture based solely on bounding every dominant complementary-minor product.

The following are **not** refuted by this witness:

1. cancellation after summing all degree sets `M` for a fixed identity set;
2. cancellation after summing all identity sets `E` contributing to the same monomial;
3. cancellation between `w=1,2,3,4` blocks;
4. the complete torus-projected Cartier coefficient at weight `25308`;
5. Cartier nonvanishing at `p=223`;
6. the function-field `d=1` crown.

The correct next Route-1 object is therefore the **fully assembled coefficient**, not an individual Cauchy-Binet product and not an entrywise or minorwise support bound.

## 7. Epistemic classification

- Witness sets and grading: exact integer arithmetic.
- Two complementary determinants: exact modulo 223.
- Original 213x213 determinant product: exact modulo 223.
- Equality of direct and complementary calculations: exact.
- Refutation of `CT1-w1`: definitive.
- Nonzero fully grouped coefficient: not established.
- Full corrected support conjecture: open.
- Function-field `d=1` crown: open.
