# Full `C_wedge` terminal-bar probe at the first order-`p` resonance

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** first computations on the rank-two braided object underlying the aggregate hook detector.  
**Status:** the `p=3,5,7` profiles are exact. The `p=11` first-homology profile has now been promoted to an exact characteristic-zero theorem in `P11_CWEDGE_CYCLOTOMIC_LIFT_AND_SIGN_OVERAGE_20260726.md`. The raw-bar budget mechanism is subsequently refuted uniformly by the exact `p=13` obstruction in `P13_CWEDGE_EXACT_BUDGET_OBSTRUCTION_20260726.md`.

## 0. Correct role of this probe

The aggregate Sawin target is

\[
B_\Lambda=B(\pi_+)+B(\pi_-)\le p-1.
\]

The Pascal oscillator and scalar bar theorem control signed virtual objects. This probe asks whether the complete rank-two hook package is small before virtual cancellation.

Ma's braided vector space satisfies

\[
C_\wedge^{\otimes n}
\cong
\bigoplus_{k=0}^{n-1}
\left(\bigwedge^k\operatorname{Std}_n\right)^{\oplus2}.
\]

Thus it contains two copies of every hook.

## 1. Exact small-prime profiles

The quantum-shuffle bar differential preserves Hamming weight.

### `p=3`

| weight | `(dim H_1, dim H_2)` |
|---:|---:|
| 2 | `(1,1)` |
| 3 | `(1,1)` |

Total terminal homology: `4`.

### `p=5`

| weight | `(dim H_1, dim H_2)` |
|---:|---:|
| 4 | `(1,1)` |
| 5 | `(1,1)` |

Total terminal homology: `4`.

### `p=7`

| weight | `(dim H_1, dim H_2)` |
|---:|---:|
| 2 | `(1,1)` |
| 3 | `(2,2)` |
| 4 | `(1,1)` |
| 6 | `(1,1)` |
| 7 | `(1,1)` |

Total terminal homology:

\[
12=2(p-1).
\]

## 2. Exact `p=11` first homology

The Hamming-weight profile is

| weight | `dim H_1` |
|---:|---:|
| 2 | 1 |
| 3 | 2 |
| 4 | 2 |
| 5 | 4 |
| 6 | 6 |
| 7 | 4 |
| 8 | 1 |
| 10 | 1 |
| 11 | 1 |

Hence

\[
\boxed{\dim H_1=22.}
\]

The corresponding multiplicity-one hook-nullity profile is

\[
(0,0,1,1,1,3,3,1,0,0,1).
\]

The unique final hook is the sign representation. Removing it leaves multiplicity-one total `10=p-1`; in the doubled model the two sign copies account exactly for `22-20=2`.

This is an exact theorem over `Q(zeta_11)`, certified independently of the earlier stable modular calculations.

## 3. Why `p=11` does not settle the programme

The exact `p=13` calculation proves

\[
\dim\ker(\wedge^3)=2,
\quad
\dim\ker(\wedge^4)=5,
\quad
\dim\ker(\wedge^5)=5,
\quad
\dim\ker(\wedge^6)=5.
\]

These four non-sign hooks alone contribute `17>12=p-1` in multiplicity one.

Therefore the apparent `p=11` mechanism

> remove the sign hook and the raw terminal bar page meets the Sawin budget

is not uniform.

## 4. Final interpretation

The raw `C_wedge` bar complex remains a useful associated model, but it cannot itself be the required Betti-bounded `E_1` page.

A valid sparse Fourier--Cayley/Rees comparison must introduce further structure absent from the full configuration space:

1. differentials;
2. quotients;
3. weight exclusions;
4. arithmetic projectors.

The exact `p=13` profile is now a mandatory regression: at least five known non-sign multiplicity-one classes must disappear before the sparse associated graded can meet the budget.

## 5. Verification files

- `cwedge_terminal_bar_probe.py`: original small-prime and modular probe;
- `p11_cwedge_cyclotomic_lift_verify.py`: exact `p=11` lift;
- `p13_cwedge_budget_obstruction_verify.py`: exact `p=13` obstruction.
