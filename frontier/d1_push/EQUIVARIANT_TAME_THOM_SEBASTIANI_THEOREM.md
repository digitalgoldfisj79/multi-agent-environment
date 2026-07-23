# Equivariant tame Thom–Sebastiani for the cyclic A1 branches

**Date:** 2026-07-23  
**Status:** standard theorem application, valid for every prime `p>=5` and every auxiliary prime `ell!=p`. Naturality of the nearby-cycle Künneth/Thom–Sebastiani isomorphism makes it equivariant under permutation of identical factors. Because `p` is invertible in the `ell`-adic coefficient field, cyclic character projection is exact. This closes the local equivariance question for a rank-one tame `A1` vanishing cycle. It does not by itself prove that the complete weighted primitive boundary is exhausted by the two escaping branches.

## 1. Coefficients and cyclic action

Fix a finite extension `Lambda/Q_ell`, with `ell!=p`, containing the p-th roots of unity if individual `C_p` eigenspaces are desired.

Let `V` be the rank-one tame vanishing-cycle object of one nondegenerate `A1` germ, placed in perverse degree zero. Form the p-fold local additive convolution

`V^(star p)=V star ... star V.`

The p-cycle `sigma` acts by cyclically permuting the p identical input factors.

Although this automorphism has order equal to the residue characteristic `p`, the coefficient field has characteristic zero and `p` is a unit in `Lambda`. Therefore `Lambda[C_p]` is semisimple and every character projector

`e_chi=(1/p) sum_(j=0)^(p-1) chi(sigma)^(-j) sigma^j`

is an exact idempotent.

No modular-representation obstruction occurs in the sheaf category.

## 2. Naturality of Thom–Sebastiani

Illusie's nearby-cycle Kunneth theorem constructs the external-product isomorphism as a natural morphism in the input pairs `(f_i,K_i)`. Its application to the addition map gives the etale Thom–Sebastiani isomorphism between the vanishing cycles of the sum and local additive convolution of the factor vanishing cycles.

For p identical factors, every permutation of the factors is an automorphism of the input diagram. Naturality implies that the Thom–Sebastiani isomorphism commutes with that automorphism. Iterating the binary theorem, with the associativity constraints of local convolution, gives a canonical `S_p`-equivariant isomorphism, and in particular a `C_p`-equivariant one.

The same conclusion follows from Fu's Fourier/stationary-phase construction: the Fourier transform and external tensor product are functorial, and permutation of identical factors commutes with the sum map.

### Theorem ETS.1 — cyclic equivariance

For p identical isolated tame germs,

`boxed(Phi_(f_1+...+f_p)`

`      ~=Phi_(f_1) star ... star Phi_(f_p))`

is `C_p`-equivariant for the cyclic permutation of factors, including the standard cohomological shifts, Tate twists and Koszul symmetry signs.

For the rank-one `A1` object in perverse degree zero, the cyclic permutation has no additional Koszul sign because `p` is odd and the normalized object is even in the symmetric monoidal perverse convention.

## 3. Rank-one tame convolution

The local additive convolution of rank-one tame vanishing cycles is rank one, up to its Jacobi-sum/epsilon-factor arithmetic twist. Thus

`rank(V^(star p))=1.`

The `C_p` action on this one-dimensional object is a scalar. Equivariant Thom–Sebastiani identifies its cyclic trace with the cyclic trace on the p-fold local vanishing-cycle construction.

Consequently the local Adams term has one-dimensional effective support:

`Psi^p(V)=[V^(star p), cyclic trace]`,

with

`rank_eff Psi^p(V)=1.`

Subtracting the original rank-one cycle gives:

### Corollary ETS.2 — one-branch Adams presentation

`boxed(Psi^p(V)-V`

`      =[one rank-one cyclic-convolution object]`

`       -[one rank-one original object].)`

Hence the effective presentation dimension of one tame `A1` branch is at most `2`, at every stalk where the two objects are defined as middle-extension or punctual perverse objects.

## 4. Application to the weighted endpoint

`WEIGHTED_ENDPOINT_ESCAPING_A1_THEOREM.md` proves that, after the tame Kummer base change, the endpoint family has exactly two separated nondegenerate critical sections. On each section the post-Artin–Schreier local germ is tame `A1`.

Applying Corollary ETS.2 separately to those two sections yields an effective presentation of total dimension at most

`2+2=4`.

This statement is exact for the sum of the two branchwise local stationary-phase classes.

## 5. What remains project-specific

To identify this four-object class with the complete primitive Fourier complex, one must still prove the localization inventory statement:

1. the Fourier/convolution compactification has no primitive face omitted from `CYCLIC_CONVOLUTION_STATIONARY_EQUATIONS.md`;
2. the `lambda_i=0` faces are exactly the already removed Tate and lower-length Kummer/pair/D terms;
3. the affine Artin–Schreier central class is removed before the tame nearby-cycle comparison;
4. both escaping branches are counted once, and the factor `2(Q-m1)` is not applied as an additional multiplicity;
5. no residual extension object is supported at the intersection of the two weighted charts.

These are localization and subtraction statements, not a failure of equivariant Thom–Sebastiani.

## 6. Consequence if the inventory is proved

If the five statements above hold in the resolved localization triangle, the complete primitive Fourier complex has an effective presentation by four rank-one perverse objects. Therefore every geometric stalk, including Fourier frequency zero, has effective dimension at most four.

The frequency-zero stalk is the compactly supported primitive error complex. Weight at most three then gives

`|pN_a(p)-p^2-explicit_lower_weight_terms|<=4p^(3/2)`

up to the already explicit `O(p)` sectors.

## 7. References

- L. Illusie, *Around the Thom–Sebastiani theorem*, arXiv:1604.07004: nearby-cycle Kunneth theorem, Thom–Sebastiani via local additive convolution, and the tame convolution analysis.
- L. Fu, *A Thom–Sebastiani theorem in characteristic p*, arXiv:1105.5210: isolated-singularity theorem via Fourier transform and stationary phase.
- G. Laumon, *Transformation de Fourier, constantes d'equations fonctionnelles et conjecture de Weil*: local additive convolution and local Fourier transform.

## 8. Epistemic classification

### Published theorem application

- nearby-cycle Kunneth/Thom–Sebastiani isomorphism;
- naturality under factor automorphisms;
- tame rank-one local convolution;
- compatibility with shifts, twists and monodromy.

### Exact formal consequence

- `C_p`-equivariance for identical factors;
- exact cyclic character projection over `Q_ell`;
- one rank-one convolution term per `A1` branch;
- effective dimension at most two per branch and four for two branches.

### Open

- complete identification of the global primitive weighted-boundary localization triangle with those two branchwise classes;
- final lower-length face bookkeeping;
- function-field `d=1` crown.
