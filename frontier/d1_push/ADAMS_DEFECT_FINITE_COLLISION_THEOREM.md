# Adams-defect annihilation at every finite branch collision

**Date:** 2026-07-23  
**Status:** exact theorem for every prime `p>=5` and every `a in F_p^*`. It removes the growing-degree finite collision scheme from the cyclic-Adams localization problem. After this theorem, every finite inertia group of the root-negation descended cover is annihilated by the p-th Adams defect. Only infinity and compactification corners remain.

## 1. Setup

Put

`m=(p-1)/2`,

`H_c(Y)=Y^m+aY+c`,

`R_a(c,Y)=Y H_c(Y)^2`,

and

`y_0=-c/(3a)`,  `B_a(c)=R_a(c,y_0)`.

The finite discriminant of `R_a(c,Y)-e` is supported on

`e=0` and `e=B_a(c)`.

Let

`W=psi^p(P)-P`

for the natural degree-`p` permutation representation. Its character is

`chi_W(sigma)=p` if `sigma` is a `p`-cycle and `0` otherwise.

Generic inertia on each finite discriminant component was already shown to be annihilated by `W`. The only unresolved finite locus was their collision scheme

`e=0`,  `B_a(c)=0`.

## 2. Collision equation

Since `y_0=-c/(3a)`, one has

`a y_0+c=2c/3=-2a y_0`,

and therefore

`H_c(y_0)=y_0^m-2a y_0`

`            =y_0(y_0^(m-1)-2a).`

Because `B_a(c)=y_0 H_c(y_0)^2`, the collision scheme consists of:

1. `c=0`, equivalently `y_0=0`;
2. the nonzero points satisfying

   `y_0^(m-1)=2a`.

Its geometric degree grows with `p`, but its local sheet support does not.

## 3. The collision at c=0

At `c=0`,

`H_0(Y)=Y(Y^(m-1)+a)`,

so the special fibre is exactly

`R_a(0,Y)=Y^3(Y^(m-1)+a)^2.`

The root `Y=0` has multiplicity `3`; the other `m-1` roots occur with multiplicity `2`. Since `a!=0`, the polynomial `Y^(m-1)+a` is separable and nonzero at `Y=0`.

Thus the local sheets split into one cluster of size `3` and `m-1` disjoint clusters of size `2`. After restricting to a sufficiently small geometric neighbourhood, the local monodromy group preserves this partition and embeds in

`S_3 x (C_2)^(m-1).`

Every local inertia element has all cycle lengths in `{1,2,3}`. Since `p>=5`, none is a `p`-cycle. Hence

### Theorem ADCF.1

`boxed( W|_(I_(c=0,e=0))=0. )`

## 4. The nonzero collision points

Assume `c!=0` and `B_a(c)=0`. Then `y_0!=0` and

`y_0^(m-1)=2a.`

Now

`H'_c(Y)=mY^(m-1)+a`.

In characteristic `p`, `m=(p-1)/2=-1/2`, so

`H'_c(y_0)=m(2a)+a=0.`

Moreover

`H''_c(y_0)=m(m-1)y_0^(m-2)!=0`,

because `p>=5`, `y_0!=0`, and neither `m` nor `m-1` vanishes modulo `p`. Therefore `y_0` is an exact double root of `H_c`. Write

`H_c(Y)=(Y-y_0)^2 K_c(Y)`,  `K_c(y_0)!=0`.

The special fibre is then

`R_a(c,Y)=Y(Y-y_0)^4 K_c(Y)^2.`

Since `c!=0`, the root `Y=0` is simple. Hence the sheets split into:

- one fixed sheet at `Y=0`;
- one local cluster of size `4` at `Y=y_0`;
- `m-2` disjoint clusters of size `2`.

The local monodromy group therefore embeds in

`S_4 x (C_2)^(m-2)`

with the `Y=0` sheet fixed. Every local inertia element has cycle lengths in `{1,2,3,4}`. Again no element is a `p`-cycle.

### Theorem ADCF.2

At every nonzero geometric collision point,

`boxed( W|_(I_collision)=0. )`

## 5. Complete finite-inertia annihilation

Combining ADCF.1 and ADCF.2 with the generic finite-inertia theorem gives:

### Theorem ADCF.3 — no finite Adams boundary

For the descended degree-`p` cover

`R_a(c,Y)=e`,

the p-th Adams defect restricts to zero on every geometric finite inertia group, including all generic points and all collision points of the two finite discriminant components:

`boxed( W|_(I_x)=0 for every finite discriminant point x. )`

The statement remains true after tensoring by the square-value Kummer projector `1 direct_sum L_chi`.

Consequently the finite collision scheme contributes no localized Adams-defect class despite its growing geometric degree.

## 6. Strategic consequence

The cyclic-Adams localization problem is now reduced to:

1. wild infinity, where `W=-V+2Q` is already explicit;
2. corners and exceptional divisors introduced by the chosen compactification at infinity.

There is no remaining finite branch or finite collision contribution to estimate. In particular, the former concern that `B_a(c)=0` has degree growing with `p` is eliminated exactly rather than bounded.

## 7. Audit

`adams_defect_finite_collision_audit.py` checks for both square classes and every prime in its range that:

- the collision equation has the stated form;
- at `c=0`, the special fibre has multiplicity partition `3,2^(m-1)`;
- at every nonzero rational collision, `H_c` has one exact double root at `y_0` and the fibre has partition `1,4,2^(m-2)`;
- neither partition contains a cycle of length `p`.

The audit is supplementary; the theorem is symbolic over the algebraic closure.

## 8. Epistemic classification

- collision equation: exact algebra;
- multiplicity-three and multiplicity-four local models: exact algebra;
- preservation of separated local sheet clusters: standard local finite-cover theory;
- absence of p-cycles and Adams annihilation: exact representation theory;
- complete finite-inertia annihilation: exact;
- infinity/corner localization: open;
- Cyclic-Adams Weight-Three Lemma: open;
- function-field `d=1` crown: open.
