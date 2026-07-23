# Local Fourier rank-four bridge — conditional form

**Date:** 2026-07-23  
**Status:** the local algebra gives a candidate effective bound `4`, but the passage from the finite cyclic fixed diagonal to the primitive weighted-corner Fourier transform is not proved. The two rank-one wild infinity orbits belong to the Artin–Schreier class already subtracted and provide no direct bound for `E_a^prim`. This file records the exact conditional bridge and the remaining theorem without treating it as established.

## 1. Terminal object

Let

`E_a=R^1 pi_! (Psi^p(P_a)-P_a)`

be the generic-pencil Adams pushforward on the original linear-coefficient line `A^1_c`. After removing the exact Tate, Kummer, pair, split/nonsplit `D`, CM and Artin–Schreier boundary summands, write the residual virtual middle extension as

`E_a^prim`.

The crown would follow from absolute effective bounds for

`Swan_infinity(E_a^prim)-rank(E_a^prim)`

and for the invariant dimension.

If `E_a^prim[1]` admits an effective perverse presentation with no constant or punctual summands, and if its Fourier transform is a middle extension lisse on `G_m`, then Laumon stationary phase identifies the relevant conductor defect with the generic effective rank of the Fourier transform. Under those additional hypotheses, the sharp candidate target is

`rank_eff(FT_c(E_a^prim)|_(G_m)) <= 4.`

None of the hypotheses in the preceding paragraph is automatic from the finite trace data.

## 2. Cyclic realization of Adams

For a complex `K`, the p-th Adams operation is represented in the Grothendieck group by the cyclic trace on `K^(tensor p)`:

`Psi^p(K)=Tr_(C_p)(sigma|K^(tensor p))`,

where `sigma` is a p-cycle.

Fourier–Deligne transform exchanges tensor product in the `d`-coordinate with additive convolution in the dual coordinate. At the level of Grothendieck classes and normalized six-functor operations, the Fourier transform of the cyclic power is therefore represented by the cyclic trace of the p-fold additive convolution.

The unresolved issue is localizing that cyclic trace in characteristic `p`, where the factor permutation itself has order `p`. A tame fixed-point argument does not apply.

## 3. Exact finite fixed-diagonal algebra

The cyclic fixed locus in the p-fold root fibre product is the root diagonal. The one-factor normal displacement is

`f_(a,c,d)(x+h)-f_(a,c,d)(x)`

`=h^p+(3a x^2+c)h+3a xh^2+ah^3.`

Consequently the one-factor nontransverse locus is

`Gamma_a: c=-3a x^2.`

On `Gamma_a` the one-factor normal germ is

`phi_(a,x)(h)=h^p+3a xh^2+ah^3.`

The exact local calculation gives:

- `x!=0`: formal type `A_1`, Milnor number `1`;
- `x=0`: formal type `A_2`, Milnor number `2`;
- the `h^p` term is formally removable in both one-variable germs.

This does **not** by itself identify the complete normal complex of the p-fold cyclic convolution. The normal space has `p-1` directions and the reduction to the one-factor vanishing cycles requires the missing equivariant Thom–Sebastiani comparison.

## 4. Exact A1 main/Kummer decomposition

The punctured critical parabola maps to the `c`-line by

`x -> c=-3a x^2.`

Its pushforward is exactly

`Q_l direct_sum L_(chi(-c/(3a))).`

Thus, if the finite fixed-diagonal contribution is identified by the cyclic localization theorem, its punctured `A_1` part is exhausted by the already removed main/Tate and Kummer classes.

The word “if” is essential: the quadratic-cover calculation is exact, while its identification with the complete cyclic Fourier contribution is conditional.

## 5. Candidate A2 effective dimension

Let `V_A2` be the two-dimensional tame vanishing-cycle representation of the one-variable `A_2` germ. In the tame representation ring, the virtual class

`Psi^p(V_A2)-V_A2`

has an effective presentation as the difference of two representations of dimension `2`; hence its total effective presentation dimension is at most `4`.

Therefore, **conditional on** the cyclic Thom–Sebastiani–corner lemma identifying the entire primitive finite contribution with this class and proving that no additional specialization cone survives, one obtains

`rank_eff(FT_c(E_a^prim)|_(G_m)) <= 4.`

The dimension calculation is exact. The identification with `FT_c(E_a^prim)` is open.

## 6. Artin–Schreier subtraction and what remains

At the root-infinity inertia group,

`W|I=W_AS^aff+2(Q-m1).`

The class `W_AS^aff` contains the complete positive-ramification representation, including the two square/nonsquare wild orbits whose local Fourier transforms have rank one. That entire class is explicitly removed in `E_a^prim`.

The residual term `2(Q-m1)` is tame. Its global weight-zero contribution collapses to the single quadratic Kummer line, also removed.

Consequently the remaining primitive problem is **not** controlled by the two wild rank-one orbits. It is the derived specialization cone of the residual tame augmentation at the weighted corner.

The exact weighted-corner results establish:

- formal rigidity away from the corner;
- the universal Artin–Schreier central fibre;
- the tame and wild endpoint types;
- complete finite critical factorization;
- Adams annihilation of every finite collision stratum.

They do not yet prove that the residual specialization cone is the isolated `A_2` Adams difference.

## 7. Precise remaining theorem

### Tame augmentation specialization theorem

Construct the localization triangle for the resolved weighted corner after removing the explicit Artin–Schreier/Tate and Kummer summands, and prove that:

1. the p-fold cyclic Thom–Sebastiani comparison is `C_p`-equivariant in the required normalized derived category;
2. all finite `A_1`, triple and quadruple strata map to the already removed main/Kummer or zero Adams classes;
3. the specialization cone of `2(Q-m1)` at the central fibre is supported only at the persistent `A_2` point;
4. that punctual cone is represented by `Psi^p(V_A2)-V_A2` with no additional wild, constant or extension summands.

Only then does the effective rank-four bound follow. A further check that the primitive Fourier transform has no constant/punctual summand is required to convert the generic rank bound into a bound for the zero-frequency stalk and hence the conductor defect.

## 8. Finite evidence

The exact primitive `c`-pencil audits found

`max_(k!=0) |FT(m_(p,A))(k)|/p^(3/2)=3.85138337984372`

through `p=199`, and the out-of-sample `p=251` values remained below `3.29`.

These computations reject visible growth on the tested range. They do **not** determine geometric rank: a high-rank or virtual sheaf may have bounded normalized traces through cancellation. The data are compatible with rank four but are not evidence that distinguishes rank four from a larger cancelling object.

A sparse fit against ordinary cubic Airy and normalized tame Jacobi dictionaries explained less than about one quarter of the variance. Thus no simple small list of standard Airy/Kummer factors has been identified.

## 9. Literature mechanism

The required general ingredients exist separately:

- Illusie’s étale Thom–Sebastiani theorem replaces tensor product by local additive convolution in characteristic `p` and gives tame convolution formulas;
- Fu’s characteristic-`p` isolated-singularity theorem uses Fourier transform and stationary phase;
- Laumon, Fu and Abbes–Saito compute local Fourier transforms and rank/Swan changes;
- T. Saito’s Milnor formula relates total vanishing-cycle dimension to characteristic-cycle intersection multiplicity.

The project-specific missing work is the equivariant specialization diagram for the residual tame augmentation. None of the cited general results automatically supplies that diagram.

## 10. Epistemic classification

### Exact

- cyclic Adams trace identity in the Grothendieck group;
- normalized Fourier tensor/convolution compatibility;
- one-factor fixed-diagonal normal expansion;
- formal `A_1/A_2` classification and Milnor numbers;
- critical-parabola main/Kummer decomposition;
- complete Artin–Schreier/tame infinity splitting;
- effective presentation dimension `<=4` for the isolated tame `A_2` Adams difference;
- finite stationary equations and absence of generic affine stationary points at nonzero `c`-frequency.

### Conditional or open

- reduction of the full p-fold normal complex to the one-factor `A_1/A_2` germs;
- `C_p`-equivariant cyclic Thom–Sebastiani at the weighted corner;
- identification of the residual tame specialization cone;
- rank-four theorem for the primitive Fourier transform;
- absence of primitive constant/punctual summands;
- conductor-defect lemma;
- `N_a=p+O(sqrt p)` and the function-field `d=1` crown.
