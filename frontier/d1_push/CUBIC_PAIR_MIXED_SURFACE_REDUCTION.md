# Cubic pair and mixed factor moments as fixed-dimensional surfaces

**Date:** 2026-07-22  
**Status:** exact algebraic reduction for every prime `p>=5` and every `a in F_p^*`. It identifies the three next Route-4 moments as point counts on explicit two-dimensional fiber products. It does not yet evaluate their primitive Frobenius traces or prove the `d=1` crown.

## 1. Setup

Fix

`F_(c,d)(X)=X^p+aX^3+cX+d`,

and let `L,Q_2,Q_3` count irreducible factors of degrees `1,2,3`.

The moments still required after the quadratic Kummer theorem are

`M_33=sum_(c,d) binom(Q_3(c,d),2)`,

`M_13=sum_(c,d) L(c,d)Q_3(c,d)`,

`M_23=sum_(c,d) Q_2(c,d)Q_3(c,d)`.

## 2. Trace-zero cubic parameter space

Every additive translation orbit of monic irreducible cubics has a unique trace-zero representative

`h_(S,N)(X)=X^3+SX-N`.

Write in its quotient ring

`X^p=A_0+B_0X+C_0X^2`.

Let `Delta_F` be the Frobenius-oriented discriminant square root. The interpolation formulas from `CUBIC_FACTOR_MASS_THEOREM.md` become

`Delta_F^2=-4S^3-27N^2`,

`C_0=-3S/Delta_F`,

`A_0=-2S^2/Delta_F`,

`B_0=-1/2-9N/(2Delta_F)`.

The orientation is arithmetic: for an irreducible cubic, Frobenius is a three-cycle and selects one of the two square roots.

Put

`u=-C_0/(3a)=S/(a Delta_F).`

Translation by `u` gives the unique cubic in the orbit satisfying the slice condition `C+at=0`. Its invariants are

`t=3u`,

`s=S+3u^2`,

`n=N+Su+u^3`,

and its Frobenius coefficients in the translated basis are

`A=A_0-B_0u+C_0u^2+u`,

`B=B_0-2C_0u`,

`C=C_0`.

Therefore define the exact rational map

`Phi_a:(S,N,Delta_F) -> (c,d)`

by

`boxed(c=as-B, d=-A-an.)`

The denominators are harmless on the irreducible-cubic locus because `Delta_F!=0` and `a!=0`.

### Theorem CMMR.1 — cubic factors as fibers

For every `(c,d)`,

`boxed(Q_3(c,d)=# Phi_a^(-1)(c,d))`

where the fiber is taken over Frobenius-oriented trace-zero irreducible cubics.

This is the additive-orbit proof of the first cubic mass, upgraded to a pointwise parametrisation.

## 3. Cubic pair surface

Let `O_3,a` denote the oriented trace-zero cubic parameter surface with the above arithmetic orientation and map `Phi_a`.

Then ordered pairs of distinct cubic factors of one slice member are exactly the off-diagonal rational points of

`O_3,a x_(A^2_(c,d)) O_3,a.`

Consequently:

### Theorem CMMR.2 — pair fiber product

`boxed(2M_33`

` =# {(P_1,P_2):P_1!=P_2, Phi_a(P_1)=Phi_a(P_2)}. )`

The ambient variables are two copies of `(S,N,Delta_F)` subject to two discriminant equations and the two equations equating `c,d`. Thus the primitive object is two-dimensional, independently of `p`.

The diagonal has the already-evaluated mass `(p^2-1)/3` and is removed explicitly.

## 4. Linear-cubic incidence surface

For a cubic parameter point, set `x=y+u`. Direct substitution into the rational-root equation gives

`boxed( 2Delta_F F_(c,d)(y+u)`

` =2Delta_F a y^3+6S y^2`

`  +(2Delta_F S a+3Delta_F+9N)y`

`  +4S^2-2Delta_F N a. )`

Hence the linear-cubic moment is the point count on the explicit surface

`X_13,a:`

`Delta_F^2=-4S^3-27N^2`,

`2Delta_F a y^3+6S y^2`

` +(2Delta_F S a+3Delta_F+9N)y`

` +4S^2-2Delta_F N a=0`,

with the Frobenius-oriented irreducible-cubic condition.

### Theorem CMMR.3 — linear-cubic point count

`boxed(M_13=#X_13,a(F_p) on the arithmetic oriented component.)`

The centered quantity

`M_13-(p^2-1)/3=sum (L-1)Q_3`

is therefore the primitive trace after subtracting the first cubic mass.

## 5. Quadratic-cubic incidence surface

An irreducible quadratic with trace-norm pair `(r,m)` maps to the unique slice member

`c=1-a(r^2-m)`,

`d=r(am-1)`,

with irreducibility condition

`chi(r^2-4m)=-1`.

Equating these two expressions with `Phi_a(S,N,Delta_F)` defines an explicit two-dimensional fiber product `X_23,a`.

### Theorem CMMR.4 — quadratic-cubic point count

`boxed(M_23=#X_23,a(F_p))`

with the quadratic sign local system and the Frobenius-oriented cubic component understood exactly as in the two separate factor parametrisations.

Its natural centered form is

`M_23-(p^2-1)/6`,

because the exact first masses are `(p^2-1)/3` for cubic factors and asymptotic mean `1/2` for quadratic factors.

## 6. Exceptional odd locus

The audit shows that the largest cubic fibers occur at `d=0`. This is structural, not numerical.

There

`F_(c,0)(X)=X H_c(X^2)`,

`H_c(Y)=Y^((p-1)/2)+aY+c.`

Every irreducible cubic factor occurs with its root-negation partner. The exact factorisation is stated separately in `CUBIC_ODD_LOCUS_PAIRING_THEOREM.md`.

For a primitive geometric analysis, the correct decomposition is therefore:

1. evaluate the one-variable odd locus `d=0` separately;
2. compactify the generic fiber products over `d!=0`;
3. subtract diagonal, reducible-cubic and boundary components;
4. identify the remaining surface motives.

Failing to separate `d=0` mixes a forced root-negation component into the primitive pair surface.

## 7. Exact audit through p=101

`cubic_mixed_mass_audit.cpp` uses the trace-zero parametrisation, not enumeration of all `p^3` monic cubics. It independently constructs `Q_2,Q_3,L` for every member and computes all three moments.

The CPU-XL audit job

`6a613c24d09dc1f57c6c33b6`

completed all 48 prime/square-class cases for `5<=p<=101` in three seconds after compilation.

The exact data show:

- `M_33` has scale `p^2/18` with non-polynomial lower terms;
- `M_13-(p^2-1)/3` remains of scale `p` in the audited range;
- `M_23-(p^2-1)/6` remains of scale `p` in the audited range;
- none of the three residuals is determined by `p` and the square class alone through an elementary polynomial formula;
- high `Q_3` multiplicities are concentrated on the odd locus.

These are finite observations, not uniform estimates.

## 8. New proof gates

The three former unspecified moments are now replaced by explicit geometric tasks:

1. determine the irreducible components and boundary of the generic off-diagonal pair surface;
2. identify the primitive motive of `X_13,a` after subtracting the first mass and odd locus;
3. identify the primitive motive of `X_23,a` after subtracting the quadratic and cubic first masses;
4. prove bounded Betti numbers and an effective trace bound for these fixed equations;
5. insert the resulting exact or bounded moments into an all-degree cycle-index sieve.

## 9. Epistemic classification

- Trace-zero Frobenius parametrisation: exact.
- Pointwise map `Phi_a`: exact.
- Pair and mixed surface identities: exact.
- Fixed-dimensionality: exact.
- Audit through `p=101`: exact finite arithmetic.
- Polynomial/main-term interpretations of the data: empirical only.
- Primitive surface decomposition and uniform trace bounds: open.
- Singular-series positivity and general `d=1`: open.
