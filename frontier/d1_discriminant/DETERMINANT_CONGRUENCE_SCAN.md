# Determinant congruence viability scan

**Date:** 2026-07-21  
**Status:** exhaustive falsification scan completed through `p=379`; route survives.

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

The function-field crown needs one nonzero cubic slice, not both square classes. Therefore:

- a zero residue in one square class kills a uniform proof using that class alone;
- it does not kill the determinant architecture if the other class is nonzero;
- the immediate two-class congruence architecture becomes inconclusive at a prime only if both square classes have residue zero.

Even simultaneous zero residues would not disprove the crown: the integer counts could be positive multiples of p. A different weighted aggregate could also remain possible.

## 3. Exact scan through p=379

Hugging Face jobs:

- `6a5fb42f13e6ef894d549fc7` for every prime through 199;
- `6a5fb515d09dc1f57c6bfc6a` for the completed range 211 through 271;
- `6a5fb7dbd09dc1f57c6bfc9d` for every prime 272 through 379.

The scans used `python-flint` factorisation and reproduced the previously established counts at `p=5,7,11,13`.

The later scans used two exact reductions:

1. the local cubic rootless prefilter;
2. the involution `d -> -d`, with `d=0` excluded because it gives the factor X.

They exhaustively counted both square classes for every prime

`5 <= p <= 379`.

There were 73 primes and 146 class-slices.

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
- `(211; 184,190)`
- `(263; 260,196)`
- `(331; 1,286)`
- `(347; 15,330)`
- `(353; 310,11)`
- `(373; 7,15)`
- `(379; 352,356)`

The residues show no obvious constant formula. Small residues such as 1, 3, 7, 11 and 15 recur, but many residues are close to p. The free involution forces every integer count to be even, but does not itself explain the residues modulo p.

## 4. Interpretation

This is evidence only. It proves no nonvanishing theorem.

It does establish that the determinant shortcut is not immediately defeated by a hidden divisibility symmetry across a substantial exact range. The absence of a translation action inside the centered slice is consistent with the data.

The committed scanner is

`determinant_congruence_scan.py`.

## 5. Strategic consequence

The determinant route remains the highest-information crown front because one structural formula for the residue would bypass the growing-period sieve entirely.

`DETERMINANT_TWO_CLASS_REDUCTION.md` shows that the top coefficient has only two square-class modes. The next algebraic questions are therefore:

1. whether the class sum and class difference admit separate coefficient or p-adic formulas;
2. whether the two modes can vanish simultaneously;
3. whether determinant multilinearity produces a recurrence in p for these aggregates;
4. whether the top coefficient is a Hasse-type invariant of the incidence variety;
5. whether the same two modes can be extracted from the Frobenius-aligned cycle polynomial.
