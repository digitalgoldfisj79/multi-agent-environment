# Exact Artin–Schreier/tame splitting of the infinity Adams class

**Date:** 2026-07-23  
**Status:** exact rational representation identity for every prime `p>=5`. The explicit Artin–Schreier boundary class contains the complete wild restriction of the Adams defect. The residual infinity class is purely tame and inflated from the quotient `C_((p-1)/2)`. The remaining problem is the degeneration/pushforward of this tame augmentation at the weighted corner.

## 1. Infinity inertia

Let

`I=C_p semidirect C_m`,  `m=(p-1)/2`,

be the geometric inertia group at root infinity. It acts affinely on the p-element set `F_p`.

Let

- `P_aff` be this p-dimensional permutation representation;
- `V=P_aff-1` be its standard quotient;
- `Q=Reg_(C_m)` inflated from `I/C_p`.

The exact Adams restriction is

`W|I=-V+2Q.`

## 2. Affine Artin–Schreier class

The permutation representation of the universal affine Artin–Schreier torsor, including the tame multiplier action, is precisely `P_aff`.

Define its Adams boundary defect by

`W_AS^aff=p*1-P_aff.`

Since `P_aff=1+V`,

`W_AS^aff=(p-1)*1-V.`

Restricted to `C_p`, this is

`p*1-Reg_(C_p)`,

the exact Artin–Schreier representation found on the weighted exceptional divisor.

## 3. Splitting identity

Subtract:

`W-W_AS^aff`

`=(-V+2Q)-((p-1)1-V)`

`=2Q-(p-1)1`

`=2(Q-m1).`

### Theorem IATS.1

`boxed(W|I=W_AS^aff+2(Q-m1).)`

The second term is the doubled augmentation representation of the tame quotient.

## 4. Complete wild removal

The subgroup `C_p` acts trivially on `Q` and on `1`. Therefore

`2(Q-m1)|_(C_p)=0`

in the representation ring.

Consequently:

1. `W_AS^aff` and `W` have exactly the same restriction to every positive ramification subgroup;
2. their refined wild character multiplicities agree;
3. the residual `2(Q-m1)` has Swan conductor zero;
4. the Artin–Schreier subtraction removes the complete wild inertia class, not merely the rational-point p-cycle orbit.

The common Swan conductor is the previously computed virtual value

`-(p-3)`

under the lower filtration with jump `(p-3)/2`.

## 5. Nature of the residual class

The residual class is

`2(Q-m1)`

`=2[Reg_(C_m)-m*1].`

It has:

- virtual rank zero;
- no wild inertia;
- character zero at the identity after virtual subtraction;
- support entirely in the nontrivial tame quotient characters.

Thus the remaining corner problem is not an unidentified wild representation. It is the global degeneration of a tame augmentation family whose number of characters grows with `m`.

## 6. Relation to the critical factorization

The critical scheme of the weighted descended family consists of:

- the transposition branch `H=0`;
- the linear branch `C+3avZ=0`;
- their triple and quadruple intersections.

Every finite member is Adams-annihilated. The tame quotient characters in `Q-m1` encode how these finite branch clusters are permuted before they coalesce at `v=0`.

The exact quadratic critical map and cubic Fourier collapse show that this growing tame character list is governed by fixed-degree stationary-phase geometry. The rank-four bridge is precisely the assertion that its augmentation pushforward collapses to the punctual `A_2` Adams difference.

## 7. Consequence for proof strategy

A further wild-ramification classification is unnecessary. The remaining proof should:

1. construct the tame augmentation sheaf `2(Q-m1)` along the weighted exceptional/Kummer cover;
2. push it through the critical map to the `c`-line;
3. use the exact main/Kummer decomposition on the punctured `A_1` locus;
4. calculate the specialization cone at the single `A_2` point.

Since the input after AS subtraction is tame, the standard tame part of Illusie's Thom–Sebastiani theorem applies; the genuinely wild convolution has already been isolated in `W_AS^aff`.

This materially reduces the remaining categorical difficulty.

## 8. Epistemic classification

### Exact

- affine permutation representation `P_aff=1+V`;
- Artin–Schreier class `p1-P_aff`;
- splitting `W=W_AS^aff+2(Q-m1)`;
- equality of all positive-ramification restrictions;
- zero Swan conductor of the residual tame class.

### Open

- global realization of `2(Q-m1)` as the tame augmentation family on the resolved corner;
- its pushforward/specialization to the `A_2` punctual complex;
- rank-four theorem and crown.
