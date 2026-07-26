# Hostile audit of the `p=11/p=13` Cayley--Jacobian hook calculation

**Date:** 2026-07-26  
**Scope:** independent failure-mode review of `CAYLEY_JACOBIAN_GRADING_LIFT_AND_HOOK_AUDIT_20260726.md`.  
**Ruling:** the exact finite calculations pass. The result is a correct stopping point under condition 2: it determines the next theorem but does not prove the `d=1` crown.

## 1. Questions designed to falsify the result

### Q1. Was the Adolphson--Sperber first grading shifted by the projective dimension rather than the number of homogeneous variables?

No. Their notation uses `n` homogeneous `x` variables and projective ambient space `P^(n-1)`. Here `n=p-2`, not `p-3`. Therefore

\[
\kappa=\sum_{m=2}^{p-4}m-(p-2)
=\frac{(p-7)(p-2)}2.
\]

Using `p-3` would introduce a one-unit error and is rejected by the primary theorem.

### Q2. Were the top Dwork weights confused with the Jacobian second degrees?

No. The Jacobian second degrees are `j=0,1,2`. Adolphson--Sperber's top-form realization shifts by the codimension `r=p-5`, giving `j+r=p-5,p-4,p-3`.

### Q3. Was `W` silently replaced by the ordinary standard representation?

No. For every `p`-regular class, the trace series removes two trivial eigenlines from the permutation representation. At the `p`-cycle, no lift is assumed; that class is left as the unique unknown. The separate verifier proves that the modular `p`-cycle action on `W` is a single Jordan block of length `p-2`.

### Q4. Could a different unknown `p`-cycle trace repair the negative middle-component multiplicities?

No. Changing the `p`-cycle trace by `p` adds one copy of

\[
\Lambda_p=\sum_i(-1)^i\wedge^i\mathrm{Std}.
\]

Hence it adds `+1` to every even hook and `-1` to every odd hook. At `p=11`, nonnegativity requires simultaneously `c>=0` and `c<=-1`; at `p=13`, `c>=1` and `c<=-1`. No integer exists.

### Q5. Could non-hook irreducibles alter the hook conclusion?

No. The unknown class function is supported only on the single `p`-cycle conjugacy class. That one-dimensional kernel is exactly spanned by `Lambda_p`, which contains only hooks. Non-hook multiplicities are fixed by the `p`-regular data.

### Q6. Is the total primitive character merely a signed Euler characteristic?

No. The projective smoothness theorem puts every nontrivial `S_p`-type in actual primitive `H^2`. The recombined total character has a full nonnegative integral decomposition into ordinary irreducibles, its dimension reproduces the independently computed primitive Betti number, and all hook multiplicities occur in cohomological degree `2`.

### Q7. Was the residue determinant twist omitted?

No. The polynomial Jacobian character is twisted by `det(W)=sgn` under the residue identification. The script records the polynomial/Jacobian profile and then reverses hook indices to obtain the primitive-cohomology profile. Since `p-1` is even, this reversal preserves even/odd parity totals.

### Q8. Do the large compactified hook masses already refute the full Cayley route?

No. They refute only the compactified primitive Jacobian page as the final Sawin Betti page. The open/discriminant localization triangle can carry large-rank Gysin maps. The result proves that those maps are load-bearing and quantifies the minimum required ranks; it does not prove they cannot exist.

## 2. Independent computational checks

The main verifier uses all of the following:

1. dynamic-programming Hilbert coefficients;
2. independent subset inclusion--exclusion Hilbert coefficients;
3. independent Chern-class/Noether primitive Betti arithmetic;
4. the independent Jacobian degree-one dimension formula;
5. exact rational conjugacy-class sums;
6. hook characters from `det(1+zg|Std)`;
7. full Murnaghan--Nakayama character values;
8. full character-table row orthogonality;
9. hook-length dimensions of all irreducibles;
10. reconstruction of the total vector-space dimension from the full irreducible decomposition.

The separate root-space verifier independently checks:

1. ranks of every power of `sigma-1` on `W`, proving one Jordan block;
2. all ordinary irreducible degrees at `p=11` and `p=13` by hook lengths;
3. the integral identity `sum o diagonal=p`.

## 3. Exact numerical regressions

### `p=11`

- `kappa=18`;
- Hodge dimensions `(231419,681239,231419)`;
- total primitive dimension `1144077`;
- primitive hook profile `(0,0,0,0,0,6,14,12,6,3,1)`;
- parity totals `(21,21)`;
- sign removal leaves `41`, so a rank-`31` non-sign boundary cancellation is necessary to reach `10`.

### `p=13`

- `kappa=33`;
- Hodge dimensions `(53524799,140071679,53524799)`;
- total primitive dimension `247121277`;
- primitive hook profile `(0,0,0,0,0,11,35,51,49,34,16,4,0)`;
- parity totals `(100,100)`;
- a rank-`188` hook boundary cancellation is necessary to reach `12`.

## 4. Remaining epistemic boundary

The exact calculation determines the compactified primitive character. It does not calculate:

- the discriminant divisor cohomology;
- the residue/Gysin map rank;
- the frequency-infinity cone;
- the exceptional `q`-chart cones;
- Frobenius on the surviving open-boundary quotient.

No claim of `B_Lambda<=p-1` follows yet.

## 5. Final audit ruling

**PROVED / CERTIFIED:** grading, modular lifting obstruction, componentwise no-lift, recombined primitive hook profiles, parity totals, and minimum boundary ranks.

**REFUTED:** ordinary lift of `W`; separate ordinary lift of the middle Jacobian component; compactified primitive cohomology as the final bounded page.

**OPEN:** the equivariant discriminant-Gysin cancellation theorem.

The programme is closer because the unknown object is now a concrete boundary map with exact required ranks, not an unspecified mixed differential. It is not close enough to claim `d=1`.
