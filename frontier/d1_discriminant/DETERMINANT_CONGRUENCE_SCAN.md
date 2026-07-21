# Determinant congruence viability scan

**Date:** 2026-07-21  
**Status:** first falsification range completed; route survives.

## 1. Target

For fixed nonzero `a`, let

`N_a(p) = # {(c,d) in F_p^2 : X^p + aX^3 + cX + d is irreducible}`.

The exact Frobenius cofactor satisfies

`J_a(c,d)=3a 1_irreducible`.

Hence

`sum_(c,d) J_a(c,d)=3a N_a(p)` in `F_p`.

Equivalently, the canonical determinant top coefficient is nonzero exactly when

`N_a(p) != 0 mod p`.

The count depends only on the square class of `a`.

## 2. Correct failure criterion

The function-field crown needs one nonzero cubic slice, not both square classes.
Therefore:

- a zero residue in one square class kills a uniform proof using that class alone;
- it does not kill the determinant architecture if the other class is nonzero;
- the immediate two-class architecture fails at a prime only if both square classes have residue zero.

A weighted sum over the two classes could remain possible even after a one-class failure.

## 3. Exact scan through p=199

Hugging Face job:

`6a5fb42f13e6ef894d549fc7`

The scan used `python-flint` factorisation and reproduced the previously established counts at `p=5,7,11,13`.

It then exhaustively counted both square classes for every prime

`5 <= p <= 199`.

There were 44 primes and 88 class-slices.

Result:

`N_a(p) mod p != 0`

for every tested class-slice.

In particular:

- no prime had both classes zero;
- no prime had even one class zero.

Selected values `(p; N_square mod p, N_nonsquare mod p)`:

- `(5; 4,1)`
- `(17; 1,14)`
- `(31; 30,7)`
- `(71; 1,5)`
- `(101; 76,15)`
- `(137; 13,126)`
- `(181; 3,3)`
- `(191; 1,176)`
- `(193; 170,1)`
- `(199; 166,180)`

The residues show no obvious constant formula. Small residues such as `1` and `3` recur, but many residues are close to `p`; this may reflect the free involution `d -> -d` rather than a simple recurrence.

## 4. Interpretation

This is evidence only. It proves no nonvanishing theorem.

It does establish that the determinant shortcut is not immediately defeated by a hidden divisibility symmetry. The absence of a translation action inside the centered slice is consistent with the data.

The next scan uses the exact local-rootless prefilter, reducing the number of polynomial factorisations by approximately two thirds. The committed scanner is

`determinant_congruence_scan.py`.

## 5. Strategic consequence

The determinant route remains the highest-information crown front because one structural formula for the residue would bypass the growing-period sieve entirely.

The next algebraic questions are:

1. whether the two class residues satisfy a relation under quadratic twisting;
2. whether their sum, difference, or character-weighted sum has a simpler formula;
3. whether determinant multilinearity produces a recurrence in `p` for these aggregated residues;
4. whether the top coefficient can be expressed as a resultant or dynamical zeta coefficient.
