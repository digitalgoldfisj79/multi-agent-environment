# Local Fourier rank-four bridge

**Date:** 2026-07-23  
**Status:** exact reduction of the terminal conductor problem to one functorial cyclic Thom–Sebastiani compatibility. The local singularity calculation gives the sharp candidate bound `4`. The final compatibility and removal of the Artin–Schreier excess are not yet claimed as proved.

## 1. Terminal object

Let

`E_a=R^1 pi_! (Psi^p(P_a)-P_a)`

be the generic-pencil Adams pushforward on the original linear-coefficient line `A^1_c`, as in `GENERIC_PENCIL_ADAMS_PUSHFORWARD_THEOREM.md`. After removing the exact Tate, Kummer, pair, split/nonsplit `D`, CM and Artin–Schreier boundary summands, write the residual virtual middle extension as

`E_a^prim`.

The remaining crown theorem follows from an absolute bound for

`Swan_infinity(E_a^prim)-rank(E_a^prim)`

and for the invariant dimension.

For a middle extension on `A^1` with no finite singularities, Laumon's stationary-phase/rank formula identifies the conductor defect with the generic rank of the Fourier–Deligne transform away from frequency zero. Thus the sharp local target is

`rank_eff(FT_c(E_a^prim)|_(G_m)) <= 4.`

## 2. Cyclic realization of the Adams operation

For a complex `K`, the p-th Adams operation is represented by the cyclic trace on `K^(tensor p)`:

`Psi^p(K)=Tr_(C_p)(sigma|K^(tensor p))`

in the Grothendieck group, where `sigma` is a p-cycle.

Fourier–Deligne transform exchanges tensor product in the `d`-coordinate with additive convolution in the dual coordinate. Therefore the Fourier transform of the cyclic power is the cyclic trace of the p-fold additive convolution. This compatibility is formal from the projection formula, proper base change and the symmetric monoidal structure, once shifts and Tate twists are normalized.

The difficult point is localizing the resulting cyclic convolution in characteristic `p`: the factor permutation has order equal to the residue characteristic, so a naive tame fixed-point formula is invalid.

## 3. Exact fixed-diagonal singularity calculation

The cyclic fixed locus in the p-fold root fibre product is the root diagonal. The exact normal displacement is

`f_(a,c,d)(x+h)-f_(a,c,d)(x)`

`=h^p+(3a x^2+c)h+3a xh^2+ah^3.`

Consequently the only nontransverse locus is

`Gamma_a: c=-3a x^2.`

On `Gamma_a` the normal germ is

`phi_(a,x)(h)=h^p+3a xh^2+ah^3.`

The theorem `CYCLIC_DIAGONAL_SINGULARITY_THEOREM.md` proves:

- `x!=0`: formal type `A_1`, Milnor number `1`;
- `x=0`: formal type `A_2`, Milnor number `2`;
- the `h^p` term is formally removable in both cases;
- there are no further finite fixed-diagonal singularities.

## 4. The A1 contribution is already explicit

The punctured critical parabola is a quadratic cover of the `c`-line:

`c=-3a x^2.`

Its local vanishing-cycle rank is one. After pushforward to `c`, this gives the quadratic/Kummer stationary-phase class already present in the exact extremal ledger. It is therefore absent from `E_a^prim`.

Equivalently, the only possible primitive finite-diagonal contribution is supported at the single point `x=c=0`.

## 5. The A2 effective dimension

Let `V_A2` denote the two-dimensional vanishing-cycle representation of the tame `A_2` germ. Functorial Thom–Sebastiani identifies the cyclic local contribution with its p-th cyclic Adams operation.

Regardless of the arithmetic Frobenius structure, the virtual difference

`Psi^p(V_A2)-V_A2`

has an honest effective presentation using two representations of dimension `2`. Hence

`effective dimension <= 4.`

This bound is independent of `p`.

Thus, once the cyclic Thom–Sebastiani localization is shown to have no additional primitive wild excess,

### Rank-four consequence

`boxed(rank_eff(FT_c(E_a^prim)|_(G_m)) <= 4.)`

## 6. Wild excess and the weighted corner

All possible non-finite excess is concentrated at the unique corner `c=d=infinity`:

- the infinity family is formally constant at every finite `c`;
- the weighted exceptional divisor is the universal Artin–Schreier family;
- its open contribution is explicit Tate/Artin–Schreier;
- the tame endpoint is Adams-annihilated;
- the wild endpoint is exactly Artin–Schreier infinity;
- the only p-cycle fibres on the descended exceptional divisor are the known orbit `X^p-X+D`, `D!=0`.

Therefore the remaining bridge is not to classify another local type. It is to prove the derived equality:

`wild cyclic excess = explicit Artin-Schreier/Tate boundary class`

in the localization triangle. After that subtraction, only the `A_2` term remains.

## 7. Precise bridge lemma

### Cyclic Thom–Sebastiani–corner lemma

For the p-fold cyclic convolution defining `Psi^p(P_a)`:

1. the iterated Thom–Sebastiani isomorphism is `C_p`-equivariant;
2. its stationary-phase decomposition localizes the finite part to the fixed diagonal;
3. the punctured `A_1` family maps to the already identified Kummer summand;
4. the isolated `A_2` point contributes `Psi^p(V_A2)-V_A2`;
5. the entire wild correction is the explicit Artin–Schreier/Tate class of the weighted corner.

Then

`rank_eff(FT_c(E_a^prim)|_(G_m)) <= 4`,

and Laumon's rank formula gives

`Swan_infinity(E_a^prim)-rank(E_a^prim) <= 4.`

Together with the already explicit endpoint invariant calculation, this supplies the Primitive effective-degree lemma and hence

`N_a(p)=p+O(sqrt p)`.

## 8. Evidence for sharpness

The true `c`-pencil Fourier audit through `p=199` found

`max_(k!=0) |FT(m_(p,A))(k)|/p^(3/2)=3.85138337984372`

at `(p,A,k)=(127,1,35)`.

For a pure effective trace object, a rank-three Weil envelope would be at most `3`. The observed coefficient is therefore consistent with effective rank at least four and strongly supports `4` as the sharp generic rank rather than merely a convenient upper bound.

This is evidence, not part of the proof, because the current object is virtual until the effective presentation in the bridge lemma is constructed.

## 9. Literature mechanism

The required formal ingredients exist individually:

- Illusie, *Around the Thom–Sebastiani theorem*: nearby cycles commute with external products under the stated `Psi`-good hypotheses, and vanishing cycles of a sum are local additive convolutions;
- Fu, *A Thom–Sebastiani Theorem in Characteristic p*: the isolated-singularity form via Fourier transform and stationary phase;
- Fu and Abbes–Saito: explicit local Fourier transforms and stationary-phase decompositions;
- T. Saito: the Milnor formula identifies vanishing-cycle total dimension with characteristic-cycle intersection multiplicity.

The project-specific work is to write the cyclic equivariance and the weighted-corner subtraction in one commutative localization diagram.

## 10. Epistemic classification

### Exact

- cyclic realization of Adams at the representation/trace level;
- Fourier tensor/convolution compatibility at the six-functor level;
- fixed diagonal and critical parabola;
- formal `A_1/A_2` classification and Milnor numbers;
- explicit weighted Artin–Schreier corner and endpoints;
- effective dimension `<=4` for the isolated `A_2` Adams difference.

### Remaining

- `C_p`-equivariant iterated Thom–Sebastiani comparison in the exact global-local diagram used here;
- equality of the wild cyclic excess with the explicit Artin–Schreier/Tate corner class;
- resulting rank-four theorem;
- conductor-defect lemma;
- `N_a=p+O(sqrt p)` and the function-field `d=1` crown.
