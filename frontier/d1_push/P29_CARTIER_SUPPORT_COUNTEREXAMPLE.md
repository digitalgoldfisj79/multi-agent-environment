# Exact p=29 counterexample to the proposed Cartier support law

**Date:** 2026-07-22  
**Status:** exact counterexample. This reaches stop condition 3 of the filtered-minor programme. It refutes the proposed Cartier survivor-support law, not the function-field crown itself.

## 1. Identity-selected dominant witness

Take `p=29`. In the falling-factorial row coordinate omit

`T={1,2,4,5,7,8}`.

Equivalently, select identity entries in rows

`S={21,22,24,25,27,28}`.

Let

`N={1,...,28}\T`

and

`Q=(N\{26}) union {0}`.

Then

`sum N=379`,

`sum Q=353`.

Choose the dominant `w=1` cubic-factor total

`I=43`.

The corresponding coefficient exponents are

`J=sum Q-3I=353-129=224=8(p-1)`,

`K=sum N-sum Q+2I=26+86=112=4(p-1)`.

Hence this is an orthogonality survivor with filtration weight

`J+2K=224+224=448=16(p-1)`.

The proposed boundary is

`(p^2-1)/2=420=15(p-1)`.

Thus the witness lies one survivor level above the boundary.

## 2. Exact substitution-minor computation

The substitution-minor audit replaces raw enumeration by the identity

`Gamma_(Q,M)=det( 1/m! [X^q](X+X^3)^m )_(q in Q,m in M).`

A dynamic programme records the number of compatible distinct-degree assignments for each degree set `M` without traversing them individually.

For this identity minor it finds exactly

- `2,166,022,375` compatible assignments;
- `2,177` distinct falling-factorial degree sets;
- `15` nonzero substitution minors modulo `29`.

Summing the Cauchy-Binet products gives

`[a^43 c^224 d^112] D_(N,Q)(a,c,d)=7 mod 29.`

The identity-expansion, `-H`, and row-sign product is `-1`, so this one identity selection contributes

`-7=22 mod 29`

to the full Cartier determinant.

An explicit nonzero grouped term is

`M={0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,23,24,25,26,27}`,

for which

`Gamma_(Q,M)=25 mod 29`,

`det((n)_m)_(N,M)=15 mod 29`.

Both factors are nonzero.

## 3. Independent full-determinant Fourier audit

The complete `28 x 28` Cartier minor was evaluated over each of the two independent field models

`F_29[s]/(s^2-2)`

and

`F_29[s]/(s^2-3)`.

Both `2` and `3` are nonsquares modulo `29`. The multiplicative group has order `840`.

Set

`c=c0*t`, `d=t^2`.

An exact two-stage multiplicative Fourier inversion extracts first weight `448` in `t`, then `c`-degree `224`. Exact tropical assignment gives

`deg_t <=550<840`,

while

`deg_c <=406<840`,

so there is no Fourier aliasing.

For the complete `w=1,2,3,4` Cartier matrix, both field models give

`[c^224 d^112] det(I-H)=22` for `a=1`,

`[c^224 d^112] det(I-H)=14` for `a=2`.

Here `2` is a nonsquare. These values equal

`boxed( 22 a chi_29(a) )`

for the two square classes of `a`.

Running the same extraction with only the dominant `w=1` block gives the identical pair `22,14`. Therefore the lower `w=2,3,4` pieces do not cancel or alter this coefficient.

The full Fourier result agrees with the independently computed signed contribution of the displayed identity minor:

`22 * 2^43 =14 mod 29`.

Thus the remaining identity selections sum to zero at this coefficient; the displayed identity selection already accounts for the complete answer.

## 4. Theorem

### Theorem P29C.1 — Cartier support counterexample

For `p=29` and every `a!=0`, the complete Cartier cofactor contains the nonzero orthogonality-surviving coefficient

`boxed( [c^224 d^112] det(I-H)=22 a chi_29(a). )`

Its filtration weight is

`448>(29^2-1)/2=420`.

Consequently:

1. the grouped factorial-coefficient cancellation theorem is false;
2. the dominant `w=1` support theorem is false;
3. the proposed full Cartier survivor-support law is false;
4. the lower filtration blocks `w=2,3,4` do not repair this counterexample.

## 5. Consequence for the Fortune programme

This counterexample closes the present support-cutoff route. It does **not** imply that the `d=1` function-field crown is false. The crown is independently machine-certified in the existing finite range, including `p=29`; the failed statement was a proposed sufficient structural theorem for a uniform proof.

A replacement route must allow above-bound Cartier survivors and control their assembled contribution, rather than proving that the tail is absent.

## 6. Reproducibility

Files:

- `CARTIER_SUBSTITUTION_MINOR_IDENTITY.md`;
- `cartier_substitution_minor_audit.py`;
- `cartier_substitution_minor_audit_results.json`;
- `p29_full_cartier_counterexample.cpp`;
- `p29_full_cartier_counterexample_results.json`.

All arithmetic is exact. No floating-point interpolation or fitting is used.

## 7. Epistemic classification

- Substitution-minor identity: exact.
- Assignment and degree-set counts: exact integer dynamic programming.
- Identity-minor coefficient `7 mod 29`: exact Cauchy-Binet computation.
- Identity-expansion sign and signed contribution `22 mod 29`: exact.
- Full determinant coefficients in two quadratic field models: exact.
- Equality of full and `w=1` coefficients: exact.
- Proposed support law: refuted.
- Function-field crown and integer Fortune conjecture: remain open.
