# Exact p=223 counterexample to the corrected complete Cartier support conjecture

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** exact refutation of the corrected complete Cartier support conjecture. The complete four-block Cartier determinant has a nonzero filtration component one full level above the corrected boundary. This does **not** prove Cartier nonvanishing or the function-field `d=1` crown.

## 1. Complete object evaluated

Let

`F(X)=X^p+aX^3+cX+d`

and let `M_3(F)` be the `(p-1)x(p-1)` minor of `I-H(F)` obtained by deleting row `p` and column `3`.

At `p=223`, specialize

`a=1`, `c=t`, `d=t^2`.

This preserves the filtration

`wt(a)=0`, `wt(c)=1`, `wt(d)=2`.

Consequently

`[t^W] det M_3(X^223+X^3+tX+t^2)`

is the sum of **every** determinant monomial of filtration weight `W`. The determinant itself automatically assembles:

1. every identity subset;
2. every Cauchy-Binet degree set;
3. all Cartier blocks `w=1,2,3,4`.

No termwise or fixed-identity truncation remains.

## 2. Target level

The old support boundary is

`B_0=(p^2-1)/2=24864`.

The corrected one-extra-level boundary was

`B_1=(p-1)(p+3)/2=25086`.

The `p=223` termwise witness identified the next level

`W=25308=B_1+(p-1)`.

Thus a nonzero complete coefficient at `W=25308` definitively refutes the corrected complete support conjecture.

## 3. Exact Fourier extraction

The source

`p223_full_cartier_weight_fourier.cpp`

constructs the complete `222x222` matrix directly from

`H_(u,v)=sum_(w=1)^min(4,u) (-1)^(p-1-u+w) [X^(pw-v)](aX^3+cX+d)^(p-1-u+w)`.

After `c=t`, `d=t^2`, an exact Hungarian assignment gives

`deg_t det M_3 <= 33077`.

Fourier extraction is performed over `F_(223^2)^*`, whose order is

`223^2-1=49728`.

Since

`33077 < 49728`,

there is no coefficient aliasing.

The paired implementation evaluates one representative from each Frobenius orbit, namely `24,975` exact `222x222` determinants. The unpaired verifier independently evaluates all `49,728` nonzero field elements.

## 4. Dominant block

Keeping only `w=1` gives

`boxed([t^25308] det M_3^(w=1)(1,t,t^2)=14 mod 223)`.

This value was obtained independently in both quadratic models

`F_223[s]/(s^2-3)`

and

`F_223[s]/(s^2-5)`.

The corresponding jobs were

- `6a619aa513e6ef894d54ca7d`;
- `6a619ab9d09dc1f57c6c3c83`.

Thus cancellation across identity subsets does not remove the high-weight dominant contribution.

## 5. Complete four-block assembly

Including every block `w=1,2,3,4` gives

`boxed([t^25308] det M_3(1,t,t^2)=12 mod 223)`.

The value `12` was reproduced in both quadratic field models:

- `6a619aaf13e6ef894d54ca7f`, using `s^2=3`;
- `6a619ac4d09dc1f57c6c3c85`, using `s^2=5`.

The imaginary component was zero in each run.

An independent unpaired Fourier calculation,

`p223_full_cartier_weight_unpaired_verify.sh`,

evaluated all `49,728` nonzero elements of `F_(223^2)` directly and again returned

`12 mod 223`.

Its job was

`6a619b1513e6ef894d54ca83`.

Therefore the lower blocks change the dominant value from `14` to `12`, but do not cancel it.

## 6. Exact consequence

Write the determinant as

`det M_3(a,c,d)=sum h_(I,J,K) a^I c^J d^K`.

The computed equality says

`sum_(J+2K=25308) sum_I h_(I,J,K) =12 mod 223`

after setting `a=1`.

Because this sum is nonzero, at least one complete determinant coefficient with

`J+2K=25308`

is nonzero modulo `223`.

Since

`25308 > 25086`,

the corrected complete Cartier support conjecture is false.

This is stronger than the earlier fixed-identity result:

- degree-set cancellation fails;
- identity-set cancellation fails;
- cross-`w` cancellation fails.

## 7. What is now refuted

The following statements are definitively false:

1. every complete Cartier coefficient lies at or below `(p-1)(p+3)/2`;
2. cancellation among all identity subsets restores the corrected one-level bound;
3. cancellation among `w=1,2,3,4` restores that bound;
4. Route 1 can prove the `d=1` crown through this corrected support cutoff.

## 8. What is not proved or refuted

This computation does not by itself determine whether

`det M_3(F)`

is nonzero for every relevant `F`, nor whether the associated polynomial has an exact-period point.

Therefore it does not prove or refute:

1. Cartier nonvanishing at every prime;
2. the function-field `d=1` crown;
3. the integer Fortune conjecture.

The support-cutoff version of Route 1 is closed. Any surviving Cartier route must use a global evaluation, factorization, residue conversion, or geometric argument that tolerates arbitrarily high filtration support.

## 9. Evidence

Source and exact results:

- `p223_full_cartier_weight_fourier.cpp`;
- `p223_full_cartier_weight_unpaired_verify.sh`;
- `p223_full_cartier_weight_fourier_results.json`;
- `P223_CT1_W1_COUNTEREXAMPLE.md`;
- `p223_fixed_identity_grouped_fourier_results.json`.

No floating-point arithmetic enters the determinant, degree-bound, Fourier, or nonvanishing claims.
