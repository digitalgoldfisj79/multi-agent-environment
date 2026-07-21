# Parity-breaking factor sieve for the d=1 function-field problem

**Date:** 2026-07-21  
**Status:** exact reduction proved.

## 1. Setup

Let `p >= 5` be prime and `a` a nonzero element of `F_p`. Put

`F_(c,d)(X) = X^p + a X^3 + c X + d`

and

`H_(c,d)(X) = a X^3 + (c + 1) X + d`.

Let `A_a` be the coefficient pairs `(c,d)` for which `H_(c,d)` has no root in `F_p`.

The local-squarefreeness theorem in `DISCRIMINANT_MASS.md` gives, for every `(c,d)` in `A_a`:

1. `F_(c,d)` has no linear factor;
2. `F_(c,d)` is squarefree;
3. `chi(Disc F_(c,d))` is either `+1` or `-1`.

## 2. Exact parity-breaking lemma

### Theorem PS.1

For `(c,d)` in `A_a`, the following are equivalent:

1. `F_(c,d)` is irreducible;
2. `chi(Disc F_(c,d)) = +1` and `F_(c,d)` has no irreducible factor of degree from `2` through `floor(p/3)`.

### Proof

Factor

`F_(c,d) = P_1 ... P_r`

into distinct monic irreducibles. Local admissibility gives `deg P_i >= 2`, and the factor degrees sum to `p`.

Pellet's formula gives

`mu(F_(c,d)) = (-1)^p chi(Disc F_(c,d))`.

Since `p` is odd and the polynomial is squarefree,

`chi(Disc F_(c,d)) = (-1)^(r+1)`.

Thus positive discriminant character is equivalent to odd `r`.

If the polynomial is irreducible, then `r = 1`, so the stated conditions hold.

Conversely, suppose the discriminant character is positive and the polynomial is reducible. Then `r` is odd and `r >= 3`. The smallest factor degree is at most the average factor degree, hence at most `p/r <= p/3`. This contradicts the absence of factors in the stated range. Therefore `r = 1`. QED.

## 3. Exact inclusion-exclusion identity

Set `z = floor(p/3)`. Let `P_z` be the set of monic irreducibles over `F_p` with degrees from `2` through `z`. Let `D_z` be the squarefree monic products of elements of `P_z`, including `D = 1`.

For squarefree `F`,

`sum_(D in D_z, D divides F) mu(D)`

is `1` when `F` has no factor in `P_z`, and `0` otherwise.

Therefore the irreducible count in the slice is exactly

`I_a(p) = (1/2) sum_((c,d) in A_a) (1 + chi(Disc F_(c,d))) sum_(D in D_z, D divides F_(c,d)) mu(D)`.

Define

`A_a(D) = number of (c,d) in A_a for which D divides F_(c,d)`

and

`B_a(D) = sum of chi(Disc F_(c,d)) over those same coefficient pairs`.

Interchanging the finite sums gives

`I_a(p) = (1/2) sum_(D in D_z) mu(D) (A_a(D) + B_a(D))`.

The `D = 1` terms are already known:

`A_a(1) = (p^2 - 1)/3`

and

`B_a(1) = M_a^loc(p)`.

## 4. Incidence uniqueness

### Lemma PS.2

For every monic `D` with `deg D >= 2`, one has `A_a(D) <= 1`.

### Proof

If the same `D` divided both `F_(c,d)` and `F_(c',d')`, then `D` would divide their difference

`(c - c') X + (d - d')`.

A nonzero polynomial of degree at most one cannot be divisible by `D`. Hence `c = c'` and `d = d'`. QED.

Consequently `B_a(D)` belongs to `{-1,0,+1}` for every `D != 1`.

Thus the remaining theorem is an incidence-distribution problem: determine the signed Mobius sum over those squarefree small-factor products compatible with the two-parameter sparse family.

## 5. Frobenius hook-character form

For squarefree degree-p `F`, let `sigma_F` be Frobenius acting on its roots, and let `Std` be the standard representation of `S_p`.

### Theorem PS.3

`p * 1_(F irreducible) = det(1 - sigma_F | Std)`

and

`det(1 - sigma_F | Std) = sum_(j=0)^(p-1) (-1)^j chi_(exterior^j Std)(sigma_F)`.

### Proof

If `sigma_F` has more than one cycle, its permutation representation has eigenvalue `1` with multiplicity greater than one. Therefore `Std` still has eigenvalue `1`, and the determinant vanishes.

If `F` is irreducible, `sigma_F` is a p-cycle. Its eigenvalues on `Std` are the nontrivial p-th roots of unity, and their product under `1 - eigenvalue` is `p`.

The second equality is the characteristic-polynomial expansion of the determinant into exterior-power traces. QED.

The discriminant character is only the top exterior-power character. The theorem explains the remaining gap precisely: sign information breaks the ordinary sieve parity barrier but does not replace the lower hook traces needed to isolate a single Frobenius cycle.

## 6. Correct next target

A sufficient theorem is any estimate proving

`sum_(D in D_z) mu(D) (A_a(D) + B_a(D)) > 0`

for at least one nonzero cubic slice `a`, uniformly for all sufficiently large primes `p`. Finite certification can then handle the remaining primes.

The two plausible implementations are:

1. a parity-weighted combinatorial sieve with a level of distribution reaching degree `p/3`;
2. a geometric trace formula that evaluates the full alternating hook sum as one object rather than bounding its p terms separately.
