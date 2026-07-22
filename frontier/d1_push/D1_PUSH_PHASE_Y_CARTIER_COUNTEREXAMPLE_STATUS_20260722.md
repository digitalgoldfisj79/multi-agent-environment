# d=1 crown push — Phase Y status: Cartier cutoff refuted

**Date:** 2026-07-22  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Status:** stop condition 3 reached. The proposed Cartier survivor-support law is false at `p=29`. The function-field `d=1` crown remains open and is not contradicted.

## 1. Executive result

The dominant-`w=1` grouped factorial coefficient has an exact algebraic description.

For an identity-selected minor, let `N` be the active falling-factorial row set and

`Q=(N\{p-3}) union {0}.`

Put

`B(q,m)=1/m! [X^q](X+X^3)^m.`

For each fixed distinct falling-factorial degree set `M`, the factorial-weighted signed sum over all compatible column choices is exactly

`Gamma(Q,M)=det(B(q,m))_(q in Q,m in M).`

This is an exact Cauchy-Binet/substitution-matrix identity and completes Phase A of the programme.

It explains the committed finite cancellations:

- `p=17`: `476` assignments, `2` degree sets, both substitution minors zero;
- `p=19`: `7,054` assignments, `5` degree sets, all substitution minors zero;
- `p=23`: `332,192` assignments, `18` degree sets, all substitution minors zero.

The same vanishing is not uniform.

At `p=29`, with omitted row parameters

`T={1,2,4,5,7,8}`

and cubic-factor total

`I=43`,

the corresponding exponents are

`J=224=8(p-1),`

`K=112=4(p-1),`

with weight

`J+2K=448=16(p-1)>420=(p^2-1)/2.`

This is a genuine above-bound orthogonality survivor.

## 2. Exact p=29 identity-minor counterexample

For the displayed identity selection:

- compatible assignments: `2,166,022,375`;
- distinct degree sets: `2,177`;
- nonzero substitution minors modulo `29`: `15`;
- identity-minor coefficient:

`[a^43 c^224 d^112]D_(N,Q)=7 mod 29`;

- identity-expansion sign: `-1`;
- signed contribution to the complete Cartier cofactor: `22 mod 29`.

An explicit grouped term has both factors nonzero:

`Gamma(Q,M)=25 mod 29,`

`det((n)_m)_(N,M)=15 mod 29.`

Therefore neither individual-alternant divisibility nor grouped substitution-minor cancellation controls this survivor.

## 3. Full Cartier verification

The complete `28 x 28` Cartier cofactor was checked by exact two-stage multiplicative Fourier inversion over two independent field models:

- `F_29[s]/(s^2-2)`;
- `F_29[s]/(s^2-3)`.

For both models:

- dominant `w=1` only:
  - `a=1`: coefficient `22`;
  - `a=2`: coefficient `14`;
- complete `w=1,2,3,4` matrix:
  - `a=1`: coefficient `22`;
  - `a=2`: coefficient `14`.

The degree bounds are below the multiplicative order `840`:

- `t`-degree at most `550`;
- `c`-degree at most `380` for `w=1`;
- `c`-degree at most `406` for the full matrix.

Thus there is no Fourier aliasing. The coefficient is

`[c^224 d^112]det(I-H)=22 a chi_29(a).`

The lower `w=2,3,4` blocks neither cancel nor alter it.

## 4. Independent verification added in this phase

Two additional implementations were committed after the counterexample first appeared.

### 4.1 Direct identity-minor Fourier extraction

`p29_identity_minor_independent_fourier.py`

This implementation performs no assignment or degree-set enumeration. It evaluates the selected `22 x 22` dominant-`w=1` identity minor at all `840` nonzero elements of each of two independent `F_(29^2)` models and extracts `[a^43]` directly.

Both models return:

- identity-minor coefficient `7`;
- zero extension-field imaginary component;
- signed contribution `22`;
- nonsquare check `22*2^43=14 mod 29`.

### 4.2 Independent full determinant implementation

`p29_full_cartier_independent_audit.cpp`

This is a separately written complete Cartier/Fourier implementation. It was run on Hugging Face `cpu-xl` as job

`6a61214013e6ef894d54c372`.

Runtime was `42` seconds. It reproduced all four full checks in both quadratic field models, including equality of the `w=1` and full `w=1,2,3,4` coefficients.

## 5. Theorems refuted

The following proposed statements are false:

1. every above-bound grouped factorial coefficient vanishes modulo `p`;
2. every above-bound dominant-`w=1` identity minor vanishes;
3. every complete Cartier orthogonality survivor has weight at most `(p^2-1)/2`;
4. the lower `w=2,3,4` blocks repair the dominant support cutoff.

The first counterexample is at `p=29` among the primes now tested by the exact substitution-minor audit.

## 6. What remains exact and useful

The counterexample does not invalidate:

- the Cartier cofactor certificate;
- the exact relation between the Cartier sum and `N_a(p)` modulo `p`;
- the `a`-grading and two-square-class structure;
- the dominant no-identity determinant formula;
- the substitution-minor/Cauchy-Binet identity;
- the weight-zero collapse theorem;
- the explicit pair and `D` extremal sectors;
- the discriminant-24 and discriminant-40 CM formulas;
- the finite machine certification of the `d=1` crown below `p<1200`.

It invalidates only the proposed support-cutoff sufficient theorem.

## 7. Corrected path to d=1

The previous short chain

`support cutoff -> boundary evaluation -> nonzero certificate -> d=1`

is closed.

Any renewed Cartier route must retain the above-bound tail. The exact object is now a sum of products

`det((n)_m) * det(B(q,m))`

over identity selections and degree sets, followed by the two torus projections in `c` and `d`.

A viable replacement must do one of the following:

1. **Tail-inclusive Cartier assembly.** Derive an exact recurrence, involution, or closed determinant for the complete torus-projected sum, allowing nonzero above-bound survivors.
2. **Quantized nonvanishing.** Use parity, square-class structure, or a new congruence to rule out the exact zero class without estimating every survivor separately.
3. **Geometric direct-image route.** Control the unresolved primitive middle-configuration object by structure not contained in the circular configuration trace identity.
4. **Singular-series or mass route.** Return to the exact `d=1` ledger and prove positivity by a uniform main term or an exact discriminant/Stickelberger mass identity.

The substitution-minor identity remains the most concrete algebraic input for option 1, but no uniform nonvanishing theorem follows from it yet.

## 8. Epistemic classification

- Substitution-minor identity: exact theorem.
- `p=17,19,23` grouped cancellations: exact finite arithmetic.
- `p=29` identity-minor coefficient: exact, independently verified.
- `p=29` complete Cartier coefficient: exact, independently verified in two field models and two implementations.
- Proposed Cartier support law: refuted.
- Function-field `d=1` crown: open.
- Integer Fortune conjecture: open.

## 9. Evidence files

- `CARTIER_SUBSTITUTION_MINOR_IDENTITY.md`
- `cartier_substitution_minor_audit.py`
- `cartier_substitution_minor_audit_results.json`
- `P29_CARTIER_SUPPORT_COUNTEREXAMPLE.md`
- `p29_full_cartier_counterexample.cpp`
- `p29_full_cartier_counterexample_results.json`
- `p29_identity_minor_independent_fourier.py`
- `p29_identity_minor_independent_fourier_results.json`
- `p29_full_cartier_independent_audit.cpp`
- `p29_full_cartier_independent_audit_results.json`
