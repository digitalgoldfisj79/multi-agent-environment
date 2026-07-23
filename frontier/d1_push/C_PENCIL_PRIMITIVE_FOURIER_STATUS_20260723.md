# Primitive Fourier transform on the true coefficient pencil

**Date:** 2026-07-23  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`  
**Compute:** Hugging Face job `6a61dfc9d09dc1f57c6c4d9d`  
**Status:** exact finite census and exact primitive subtraction completed for both square classes at `p=31,43,59,83,101,127,167,199`. The additive DFT is numerical. The results support a bounded local-Fourier conductor defect but do not prove it.

## 1. Object tested

For each cubic square class `A=chi(a)`, the split and nonsplit normal-form cells were reassembled on the original linear-coefficient pencil `c` using

`q=-3/c` on the split cells,

`q=3/c` on the nonsplit cells.

At every generic cell, the exact Kummer, pair and split/nonsplit `D` traces were removed pointwise. The resulting function

`m_(p,A)(c)`

is the finite trace diagnostic for the primitive pushforward class `E_a^prim` from `GENERIC_PENCIL_ADAMS_PUSHFORWARD_THEOREM.md`.

The explicit `c=0` and `q=2` boundary values were omitted because they belong to the already identified boundary ledger rather than the primitive class.

## 2. Main numerical result

For every tested prime and both classes, both

`sum_c |m_(p,A)(c)|^2 / p^3`

and

`max_(k!=0) |sum_c m_(p,A)(c) exp(-2 pi i kc/p)| / p^(3/2)`

remain bounded on the tested range.

The exact observed envelopes are

`max second moment / p^3 = 2.6865160618978887`,

attained at `(p,A)=(31,-1)`, and

`max nonzero Fourier coefficient / p^(3/2) = 3.85138337984372`,

attained at `(p,A,k)=(127,1,35)` and its conjugate frequency.

The largest coefficient when frequency zero is included is

`4.492808420749096 p^(3/2)`,

at `(p,A,k)=(167,1,0)`. This is exactly the previously identified global primitive residual `E_middle=9696`; it is not a new Fourier spike.

No monotone growth is visible. At the largest tested prime `p=199`, the maxima are only

- `2.7861603294456034 p^(3/2)` for `A=1`;
- `2.684026371275401 p^(3/2)` for `A=-1`.

## 3. Complete compact table

| p | A | primitive sum / p^(3/2) | second moment / p^3 | max nonzero Fourier / p^(3/2) |
|---:|---:|---:|---:|---:|
| 31 | 1 | 1.135569 | 1.277701 | 2.018438 |
| 31 | -1 | -2.085739 | 2.686516 | 2.843832 |
| 43 | 1 | 0.922084 | 1.413108 | 2.554149 |
| 43 | -1 | 0.624180 | 1.144956 | 2.209193 |
| 59 | 1 | 1.376913 | 1.358756 | 1.833052 |
| 59 | -1 | 1.884429 | 1.451375 | 2.786494 |
| 83 | 1 | -0.460216 | 2.371380 | 2.800963 |
| 83 | -1 | 0.195724 | 1.619316 | 2.982928 |
| 101 | 1 | 2.291541 | 1.294484 | 2.715158 |
| 101 | -1 | -1.887615 | 2.081124 | 2.807699 |
| 127 | 1 | -1.942402 | 2.246540 | 3.851383 |
| 127 | -1 | 0.543593 | 2.167271 | 3.169933 |
| 167 | 1 | 4.492808 | 1.221325 | 2.521661 |
| 167 | -1 | 3.872823 | 1.641436 | 2.773627 |
| 199 | 1 | 2.658126 | 1.668740 | 2.786160 |
| 199 | -1 | 1.099300 | 1.703561 | 2.684026 |

## 4. Interpretation

This is the strongest finite evidence so far for the proposed conductor mechanism.

The primitive pointwise trace is broad in additive frequency, so it is not a sum of a handful of linear Artin-Schreier characters. However, broad support is compatible with a Fourier-Deligne transform of bounded rank. The relevant facts are that the normalized Fourier amplitudes and the normalized second moments remain bounded, not that the spectrum is sparse.

The data therefore support the following sharper terminal statement:

### Local Fourier conductor lemma

After the explicit Kummer, pair, `D`, Tate and Artin-Schreier pieces are removed, the local Fourier transform of `E_a^prim` at `c=infinity` has bounded effective rank and bounded Swan conductor, uniformly in `p`, for at least one square class.

Such a theorem would imply absolute effective bounds for the compactly supported cohomology of `E_a^prim`, and hence

`N_a(p)=p+O(sqrt(p)).`

## 5. What the computation does not prove

A bounded trace envelope at finitely many primes does not by itself bound geometric rank or Swan conductor. Large virtual objects can have trace cancellation. The computation therefore cannot replace the local Fourier-transform calculation.

It does rule against the simplest negative scenario: there is no observed growth in the nonzero-frequency envelope or the pointwise second moment through `p=199` after the correct primitive subtraction and coordinate reassembly.

## 6. Next proof step

The next task is no longer another prime sweep. It is to compute the stationary-phase/local Fourier transform of the weighted corner model

`x^p+a u^(p-3)x^3+R^(-1)x-S^(-1)=0`

with the exact Adams projector, then remove the explicit Artin-Schreier central fibre. The expected output is a bounded list of residual critical points and their vanishing-cycle multiplicities. That calculation would give the conductor defect directly.

## 7. Epistemic status

- coefficient-penc il reassembly: exact;
- pointwise irreducibility counts: exact FLINT certification;
- Kummer, pair and `D` subtraction: exact finite-field formulas;
- compact moments: exact integers before normalization;
- additive Fourier coefficients: numerical evaluation of exact integer traces;
- bounded conductor interpretation: supported, not proved;
- local Fourier conductor lemma: open;
- function-field `d=1` crown: open.
