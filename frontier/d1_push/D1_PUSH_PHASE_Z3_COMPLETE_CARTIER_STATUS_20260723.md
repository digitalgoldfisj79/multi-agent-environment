# d=1 crown push — Phase Z3 complete Cartier status

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** the corrected complete Cartier support conjecture is exactly refuted at `p=223`. The support-cutoff form of Route 1 is closed. The function-field `d=1` crown remains open.

## 1. Decisive result

For the complete Cartier minor `M_3(F)` associated with

`F(X)=X^223+X^3+cX+d`,

set

`c=t`, `d=t^2`.

Exact multiplicative Fourier inversion gives

`[t^25308] det M_3(X^223+X^3+tX+t^2)=12 mod 223`.

The corrected support boundary was

`B_1=(223-1)(223+3)/2=25086`.

Therefore the complete determinant has nonzero support at

`25308=B_1+222`.

This coefficient includes every identity subset, every Cauchy-Binet degree set and all four Cartier blocks.

## 2. Independent verification

The calculation was reproduced in the two independent quadratic models

- `F_223[s]/(s^2-3)`;
- `F_223[s]/(s^2-5)`.

Both give the complete coefficient `12` and zero imaginary component.

A separate unpaired run evaluated every one of the `49,728` nonzero elements of `F_(223^2)` and again gave `12`.

The exact determinant degree bound is `33,077`, below the Fourier order `49,728`, so no aliasing occurs.

## 3. Dominant versus complete assembly

The dominant block alone gives

`[t^25308] det M_3^(w=1)=14 mod 223`.

The `w=2,3,4` blocks alter this by `-2`, yielding

`14-2=12 mod 223`.

Thus:

- degree-set cancellation does not repair the witness;
- identity-set cancellation does not repair it;
- cross-block cancellation does not repair it.

## 4. Route-1 conclusion

The following Route-1 programme is closed:

1. prove a hard filtration cutoff;
2. evaluate only the boundary coefficient;
3. deduce Cartier nonvanishing from that boundary term.

Both the original cutoff and the corrected one-extra-level cutoff are false. The complete determinant possesses support beyond them.

A future Cartier argument would have to tolerate the full high-weight tail and prove nonvanishing by a genuinely global identity, factorization, residue pairing, or geometric mechanism.

## 5. Live routes after Z3

The scientifically live routes are now:

1. **Quantized residue conversion:** turn the exact residue classes into a nonzero integer or low-height algebraic invariant without relying on support truncation.
2. **Geometric direct-image pairing:** identify a duality or determinant-line argument forcing a nonzero global Cartier value despite the long tail.
3. **Fixed-dimensional motives and all-degree sieve:** prove effective trace bounds for the cubic and higher cycle masses and insert them into an all-degree signed sieve.
4. **Direct dynamical route:** prove existence of an exact-period point for `x^p=g(x)` without passing through the failed support cutoff.

## 6. Evidence

Primary evidence:

- `P223_COMPLETE_CARTIER_WEIGHT_COUNTEREXAMPLE.md`;
- `p223_full_cartier_weight_fourier.cpp`;
- `p223_full_cartier_weight_unpaired_verify.sh`;
- `p223_full_cartier_weight_fourier_results.json`.

Associated jobs:

- `6a619aa513e6ef894d54ca7d` — dominant, `s^2=3`;
- `6a619aaf13e6ef894d54ca7f` — complete, `s^2=3`;
- `6a619ab9d09dc1f57c6c3c83` — dominant, `s^2=5`;
- `6a619ac4d09dc1f57c6c3c85` — complete, `s^2=5`;
- `6a619b1513e6ef894d54ca83` — complete unpaired verification.

## 7. Honest bottom line

The requested full calculation has been completed exactly.

It gives a definitive negative answer to the corrected support conjecture, but not to the `d=1` crown itself. The function-field crown and the integer Fortune conjecture remain open.
