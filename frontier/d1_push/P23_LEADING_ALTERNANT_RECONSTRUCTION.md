# Exact reconstruction of the p=23 leading filtered assignment

**Date:** 2026-07-22  
**Status:** exact finite reconstruction.  
**Purpose:** replace the unsupported sentence “the corresponding leading alternant vanishes modulo 23” by a reproducible statement of what actually cancels.

## 1. Explicit excess assignment

Use the dominant `w=1` identity-selected expansion of the Cartier minor at `p=23`.
Choose identity entries in rows

`S={16,17,18,21,22}`.

Equivalently, in the falling-factorial coordinate `n=p-u`, omit

`T={1,2,5,6,7}`.

The active rows and columns are

`R={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,19,20}`,  
`C={1,2,4,5,6,7,8,9,10,11,12,13,14,15,19,20,23}`.

One admissible choice of cubic-factor counts, in increasing column order, is

`i=(4,3,6,6,0,0,5,2,0,0,0,3,3,0,1,1,0)`.

The corresponding linear-factor and falling-factorial degree vectors are

`j=(10,12,1,0,17,16,0,8,13,12,11,1,0,8,1,0,0)`,

`m=i+j=(14,15,7,6,17,16,5,10,13,12,11,4,3,8,2,1,0)`.

Their totals are

`I=sum i=34`,  
`J=sum j=110=5(p-1)`,  
`K=p-3+2I=88=4(p-1)`.

Thus the `(1,2)`-weight is

`J+2K=286`,

strictly above the proposed boundary

`(p^2-1)/2=264`.

So this is a genuine raw filtered-assignment excess.

## 2. The individual alternant does not vanish

The active row parameters are

`n=(22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,4,3)`.

For the displayed assignment, the falling-factorial alternant is

`det( (n_r)_(m_c) )`.

Direct exact elimination gives

`det( (n_r)_(m_c) ) = 3 mod 23`.

The product of the factorial scalars `1/(i_c!j_c!)` is

`10 mod 23`.

After the identity-expansion, `-H`, and row signs are included, this single assignment contributes

`7 mod 23`.

Therefore the earlier formulation

> the corresponding leading alternant vanishes modulo 23

is false if “alternant” means this individual determinant. The determinant is nonzero and its individual contribution is nonzero.

## 3. What actually vanishes

For the same identity-selected minor, enumerate every dominant `w=1` column choice with

`sum i=34`

and with distinct falling-factorial degrees `m` (choices with repeated `m` have zero determinant automatically).

There are exactly

`332,192`

such assignments. After sorting the degree vectors, they fall into only

`18`

distinct degree sets. For a fixed sorted degree set `M`, all assignments share the same alternant

`det((n_r)_(m))_(m in M)`

up to the column-permutation sign. Their combined scalar coefficient is

`sum_(assignments with degree set M) sign * product_c 1/(i_c!j_c!).`

The exact enumeration proves:

`boxed( every one of the 18 scalar coefficients is 0 mod 23. )`

Many of the associated alternants are nonzero modulo `23`; their coefficients vanish before multiplication by the alternant. Hence the complete leading coefficient of this identity-selected minor is zero.

This is a sharper and structurally different mechanism than the provisional status sentence suggested:

- not one modularly singular alternant;
- rather a factorial-weighted cancellation among many column choices sharing each alternant degree set.

## 4. The “first at p=23” wording

Under the natural dominant-`w=1`, distinct-degree assignment model used above, `p=23` is not the first prime admitting a raw survivor above the boundary.

Exact examples also occur at:

- `p=17`: weight `160 > 144`; one displayed alternant determinant is `8 mod 17`. The corresponding identity minor has `476` admissible assignments in `2` degree sets, and both grouped scalar coefficients vanish modulo `17`.
- `p=19`: weight `198 > 180`; one displayed alternant determinant is `7 mod 19`. The corresponding identity minor has `7,054` admissible assignments in `5` degree sets, and all five grouped scalar coefficients vanish modulo `19`.

Therefore the statement “the cheap assignment bound stays below the boundary for every p<23” is not correct for this explicit formulation. If a different reduced assignment bound was intended, it must be defined separately and audited.

## 5. Consequence for the general proof strategy

The reconstruction changes the highest-value algebraic target.

A proof based only on showing that above-bound factorial-Schur alternants are divisible by `p` cannot be sufficient: explicit above-bound alternants are nonzero modulo `p`.

The required theorem must also capture the factorial-weighted column-choice cancellation. A suitable general formulation is:

> For every identity-selected minor and every above-bound survivor degree, the coefficient of each distinct falling-factorial degree alternant in the column expansion vanishes modulo `p`.

Only after this coefficient cancellation is understood should hook-content or Schur divisibility be applied to the remaining degree sets.

## 6. Reproducibility

Files:

- `p23_leading_alternant_witness.py`
- `p23_leading_alternant_witness_results.json`

The script uses only the Python standard library. It reconstructs the explicit nonzero assignment, enumerates all `332,192` compatible choices, groups them into the `18` alternant degree sets, and verifies all scalar sums are zero modulo `23`.

## 7. Epistemic classification

- Explicit p=23 assignment and exponent ledger: exact.
- Individual alternant determinant and signed contribution: exact.
- Enumeration count and 18 grouped cancellations: exact.
- p=17 and p=19 comparison statements: exact finite computations under the same model.
- General factorial-weighted cancellation theorem: open.
- Full Cartier support law and function-field crown: open.
