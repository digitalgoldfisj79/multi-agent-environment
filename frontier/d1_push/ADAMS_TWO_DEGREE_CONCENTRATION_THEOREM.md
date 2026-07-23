# Two-degree concentration of the normalized Adams error

**Date:** 2026-07-23  
**Status:** exact cohomological reduction for every prime `p>=5` and every `a in F_p^*`. After removal of the unique top Tate class, the compactly supported Adams error is concentrated in degrees `2` and `3`, of weights at most `2` and `3` respectively. Uniform effective degree bounds remain open.

## 1. Setup

Let `U_a` be the étale locus in `A^2_(c,d)` of

`X^p+aX^3+cX+d=0`,

let `P_a` be its root permutation sheaf, and put

`W_a=Psi^p(P_a)-P_a`.

By `ADAMS_TOP_WEIGHT_EXTRACTION_THEOREM.md`,

`pN_a(p^r)=Tr(Frob_p^r|RGamma_c(U_a,W_a))`

and

`H_c^4(U_(a,bar F_p),W_a)=Q_l(-2)`

in the Grothendieck group, with no other top-weight constituent.

## 2. Affine Artin vanishing

The variety `U_a` is a smooth affine surface. Every irreducible constituent of the finite-monodromy virtual local system `W_a` is lisse and semisimple. For such a lisse sheaf `L`, the shift

`L[2]`

is perverse on `U_a`.

Artin vanishing for perverse sheaves on an affine variety gives

`H_c^j(U_(a,bar F_p),L[2])=0` for `j<0`.

Equivalently,

`H_c^i(U_(a,bar F_p),L)=0` for `i<2`.

The same holds additively in the Grothendieck group for `W_a`.

Since a surface has compactly supported cohomological dimension `4`, only degrees `2,3,4` can occur.

## 3. Exact concentration theorem

Define

`C_a=RGamma_c(U_a,W_a)-Q_l(-2)[-4]`.

### Theorem ATD.1

`boxed(C_a=[H_c^2(U_a,W_a)][-2]+[H_c^3(U_a,W_a)][-3])`

in the Grothendieck group of arithmetic Frobenius complexes.

Thus for every `r>=1`,

`boxed(pN_a(p^r)-p^(2r)`

`=Tr(Frob_p^r|H_c^2(U_a,W_a))`

` -Tr(Frob_p^r|H_c^3(U_a,W_a)). )`

By Deligne's weight bounds:

- `H_c^2` has weights at most `2`;
- `H_c^3` has weights at most `3`.

## 4. Exact quantitative target

Let `b_2^eff(p,a)` and `b_3^eff(p,a)` denote the effective virtual degrees needed to express the two Grothendieck classes as differences of honest semisimple Frobenius modules. Then

`|pN_a(p)-p^2|`

`<=b_2^eff(p,a) p+b_3^eff(p,a) p^(3/2).`

After subtracting the already explicit main, Kummer, pair, D and Artin–Schreier boundary summands, the function-field crown follows from absolute bounds

`b_2^eff<=C_2`, `b_3^eff<=C_3`

for at least one square class.

This identifies the final complexity problem exactly: bound two effective degrees. No weight-four term, lower cohomological degree, or additional extension-field weight can occur.

## 5. Appropriate geometric tool

The boundary analysis has already classified every local inertia type in the weighted compactification. To control the two effective degrees, the next step is a characteristic-cycle or generic-pencil calculation:

1. form the primitive virtual Adams class after subtracting all explicit summands;
2. compute its singular support and characteristic-cycle multiplicities on the weighted surface;
3. use generic hyperplane/pencil vanishing cycles to control the effective degree of `H_c^3`;
4. control `H_c^2` through the same localization triangle and endpoint attachments.

An Euler-characteristic calculation alone is insufficient for a virtual difference: it controls `b_2-b_3`, not the two effective degrees separately. The generic-pencilled vanishing-cycle calculation is therefore the relevant terminal test.

## 6. Epistemic classification

- perversity of a shifted lisse sheaf on a smooth surface: standard exact theorem;
- affine Artin vanishing: standard exact theorem;
- concentration in degrees `2,3,4`: exact;
- unique degree-4 Tate class: proved in ATW.2;
- weights of degrees `2,3`: exact Deligne bounds;
- uniform effective bounds for the primitive degrees: open;
- function-field `d=1` crown: open.
