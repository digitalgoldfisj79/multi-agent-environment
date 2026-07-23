# Weighted endpoint: two escaping A1 stationary branches

**Date:** 2026-07-23  
**Status:** the endpoint normalization, critical sections, weighted local equations and critical values are exact for every prime `p>=5`. Standard local stationary phase gives one rank-one cyclic-convolution term per branch after the explicit Artin–Schreier central class is removed. The Adams defect subtracts one rank-one original term on the same branch, so each branch has effective presentation dimension at most two. There are exactly two branches; hence the candidate generic effective-rank bound is `4`. The exact weighted-specialization identification and the zero-frequency/invariant bound remain separate.

## 1. Normalized endpoint family

The reciprocal weighted-corner equation is

`x^p+a u^(p-3)x^3+R^(-1)x-S^(-1)=0.`

Choose a tame Kummer coordinate `lambda` satisfying

`lambda^(p-1)=-R^(-1)`

and put

`w=x/lambda`,

`tau=u/lambda`,

`B=S^(-1)/lambda^p`.

Dividing by `lambda^p` gives the exact normalized family

### Theorem WEA1.1

`boxed(F_tau(w):=w^p-w+a tau^(p-3)w^3=B.)`

Moreover

`tau^(p-1)=-1/c`

on the original coefficient pencil. Thus `tau=0` is precisely `c=infinity` after the tame Kummer base change.

The central fibre is the universal affine Artin–Schreier map

`F_0(w)=w^p-w`,

whose complete Adams boundary class has already been isolated and removed in `E_a^prim`.

## 2. Critical sections

Put

`e=(p-3)/2`,

so `p-3=2e`. Since the derivative of `w^p` is zero,

`F_tau'(w)=-1+3a tau^(2e)w^2.`

Choose `xi` with

`xi^2=(3a)^(-1)`.

For `tau!=0`, the complete critical locus consists of exactly two sections

### Theorem WEA1.2

`boxed(w_+(tau)= xi tau^(-e),`

`      w_-(tau)=-xi tau^(-e).)`

They escape to root infinity as `tau->0`; there are no further critical points.

## 3. Weighted local germ

Fix one sign and write

`w=w_sign+tau^(-e)h.`

Because `w_sign` is critical, the linear term vanishes. In characteristic `p`,

`F_tau(w_sign+tau^(-e)h)-F_tau(w_sign)`

`=tau^(-ep)h^p`

` +3a tau^(2e)w_sign tau^(-2e)h^2`

` +a tau^(2e)tau^(-3e)h^3.`

Multiplying the target displacement by `tau^(ep)` gives

### Theorem WEA1.3 — exact rescaled germ

`boxed(Phi_sign(h,T)`

`      =h^p+T(3a xi_sign h^2+a h^3),)`

where

`xi_sign=+xi` or `-xi`,

`T=tau^(e(p-1))`

` =tau^((p-3)(p-1)/2).`

The exponent of `tau` is prime to `p`, so the passage to `T` is tame.

For `T!=0`, scalar rescaling of the target and the formal Morse lemma identify the local vanishing cycle with that of

`3a xi_sign h^2+a h^3`.

Since `xi_sign!=0`, this is an `A_1` germ with Milnor number one.

The second critical point of the displayed cubic, at `h=-2xi_sign`, is the opposite section and lies outside a sufficiently small local neighborhood of `h=0`.

## 4. Critical values remain separated

At a critical section, the derivative equation gives

`a tau^(p-3)w_sign^3=w_sign/3.`

Hence

`F_tau(w_sign)=w_sign^p-(2/3)w_sign.`

After multiplying by `tau^(ep)`, the two rescaled critical values are

### Theorem WEA1.4

`boxed(C_+(T)= xi^p-(2/3)xi T,`

`      C_-(T)=-xi^p+(2/3)xi T.)`

At `T=0` they are `+xi^p` and `-xi^p`, which are distinct because `p>=5` and `xi!=0`.

Thus the two stationary contributions do not collide in the weighted limit.

## 5. Adams and stationary-phase bookkeeping

The central term `h^p` is the radicial/Artin–Schreier part represented by the explicit weighted central fibre. After subtracting that class, the relative vanishing-cycle cone at each critical section is the tame rank-one `A_1` vanishing cycle above.

For one branch:

1. tame Thom–Sebastiani and local stationary phase give one rank-one term for the cyclic `p`-fold convolution, i.e. the `Psi^p` side;
2. the original root sheaf contributes one rank-one `A_1` term on the same branch, i.e. the subtracted `P` side.

Therefore the Adams difference on one branch has an effective presentation as

`[one rank-one cyclic-convolution term]`

`-[one rank-one original term]`,

of total effective dimension at most `2`.

There are exactly two escaping branches. Hence:

### Theorem WEA1.5 — conditional generic rank-four consequence

Provided the resolved weighted specialization triangle identifies the post-Artin–Schreier primitive boundary with the two branchwise Adams differences above and introduces no additional boundary summand,

`boxed(rank_eff FT_c(E_a^prim)|G_m <= 2+2=4.)`

The exact infinity identity

`W|I=W_AS^aff+2(Q-m1)`

is consistent with this bookkeeping: its factor `2` records the two escaping finite-critical branches collectively. It must not be applied as a second multiplicity after those branches have already been counted.

All local algebra, the number of branches and the effective `2+2` presentation are exact. The remaining proviso is a functorial localization identification, not an estimate.

## 6. Relation to the previous A2 bridge

The finite fixed-diagonal cusp at `(x,c)=(0,0)` is an exact `A_2` germ, but the nonzero-frequency stationary equations place its zero-critical-value configurations in the already Adams-annihilated finite collision strata.

The actual weighted-infinity contribution is more naturally described by the two escaping `A_1` sections above. The earlier phrase “the primitive corner is the isolated A2 Adams difference” should therefore be treated as a candidate model, not as the preferred proof mechanism.

The escaping-A1 formulation has three advantages:

1. it is obtained directly in the weighted endpoint coordinates;
2. it displays all critical sections explicitly;
3. standard nondegenerate stationary phase gives the rank contribution without computing an exponentially large Milnor algebra.

## 7. Remaining zero-frequency issue

A generic rank bound on `FT_c(E_a^prim)|G_m` does not alone bound the stalk at Fourier frequency zero. To deduce the conductor-defect lemma one must also prove an absolute bound for:

- geometrically constant summands of `E_a^prim`;
- punctual summands of its Fourier transform at zero;
- lower-weight endpoint extension classes.

The unique fibrewise Tate class and the complete weight-zero Kummer class have already been removed. The remaining task is to show that the weighted specialization triangle creates no new constant or punctual primitive summand, or at least only an absolutely bounded one.

## 8. Audit

`weighted_endpoint_escaping_a1_audit.py` checks exactly:

- Kummer normalization;
- `tau^(p-1)=-1/c`;
- the two critical sections;
- the weighted rescaled germ;
- the two rescaled critical values;
- nondegeneracy and separation.

The rank bookkeeping is representation-theoretic: two branches, each represented as one rank-one cyclic-convolution term minus one rank-one original term.

## 9. Epistemic classification

### Exact

- normalized endpoint family;
- two and only two critical sections;
- their escape rate;
- rescaled local germs;
- tame `A_1` type at each section;
- separated rescaled critical values;
- branchwise effective dimension at most two for the Adams difference;
- total candidate effective dimension at most four.

### Standard theorem input

- tame Thom–Sebastiani/local convolution for the rank-one `A_1` vanishing cycle;
- one rank-one local Fourier contribution per nondegenerate stationary section.

### Open

- exact identification of the resolved primitive specialization cone with the two branchwise Adams differences;
- absence/boundedness of primitive zero-frequency punctual and constant classes;
- conductor-defect lemma;
- `N_a=p+O(sqrt p)` and the function-field `d=1` crown.
