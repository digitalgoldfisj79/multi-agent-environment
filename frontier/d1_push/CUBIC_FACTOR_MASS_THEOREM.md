# Exact irreducible-cubic-factor mass by additive-orbit quantization

**Date:** 2026-07-22  
**Status:** exact theorem for every prime `p>=5` and every `a in F_p^*`. This advances Phase Z, Route 4 from degree two to degree three. It does not prove irreducibility of a slice member or the d=1 crown.

## 1. Setup

Fix

`F_(c,d)(X)=X^p+aX^3+cX+d`,

with `a!=0` and `(c,d) in F_p^2`.

Let

`Q_3(c,d)=#{monic irreducible cubics h over F_p : h|F_(c,d)}.`

We compute the complete first incidence mass

`sum_(c,d)Q_3(c,d)`.

## 2. Frobenius coefficient criterion

Let `theta in F_(p^3)\F_p` have degree three and minimal polynomial

`h(X)=X^3-tX^2+sX-n`.

There are unique `A,B,C in F_p` such that

`theta^p=A+B theta+C theta^2`.

The minimal-polynomial relation is

`theta^3=t theta^2-s theta+n`.

Therefore

`theta^p+a theta^3+c theta+d`

`=(C+at)theta^2+(B-as+c)theta+(A+an+d).`

Hence:

### Lemma CFM.1 — cubic divisibility criterion

The irreducible cubic `h` divides a member of the slice if and only if

`boxed(C+at=0).`

When this condition holds, the member is unique:

`boxed(c=as-B,  d=-A-an).`

Thus the first cubic-factor mass is the number of degree-three Frobenius orbits satisfying one scalar coefficient equation.

## 3. Additive translation action

For `u in F_p`, put

`eta=theta+u`.

Writing Frobenius in the basis `1,eta,eta^2` gives

`eta^p`

`=[A-Bu+Cu^2+u]+[B-2Cu]eta+C eta^2.`

Therefore the quadratic Frobenius coefficient is invariant:

`C(eta)=C(theta).`

The trace changes by

`t(eta)=t(theta)+3u.`

Since `p>=5` and `a!=0`, the equation

`C+a(t+3u)=0`

has exactly one solution `u in F_p`.

Translation preserves degree three and acts freely on

`F_(p^3)\F_p`.

There are

`(p^3-p)/p=p^2-1`

translation orbits. Each orbit contains exactly one element satisfying the slice divisibility condition.

## 4. Exact mass theorem

Every irreducible cubic has three Frobenius-conjugate roots. If one root satisfies CFM.1, the quotient-ring identity shows that the cubic divides the corresponding slice member, so all three roots are counted and give the same factor incidence.

Therefore:

### Theorem CFM.2 — irreducible cubic-factor mass

For every prime `p>=5` and every `a!=0`,

`boxed( sum_(c,d in F_p) Q_3(c,d)=(p^2-1)/3. )`

The value is independent of `a`, not merely of its square class.

This is the degree-three analogue of the exact quadratic incidence

`sum Q_2=p(p-1)/2`,

but its mechanism is different: quadratic factors occur because Frobenius is automatically linear in a quadratic quotient, while cubic factors are quantized one per additive translation orbit.

## 5. Oriented-discriminant form

The scalar criterion can also be expressed directly in cubic invariants.

Order the roots so that Frobenius acts

`r_1 -> r_2 -> r_3 -> r_1`,

and define the Frobenius-oriented discriminant square root

`delta_F=(r_1-r_2)(r_1-r_3)(r_2-r_3) in F_p^*.`

It is invariant under the cyclic Frobenius permutation and satisfies

`delta_F^2=Disc(h).`

Exact interpolation gives

`C=(t^2-3s)/delta_F,`

`A=t/2+(t^2s+3tn-4s^2)/(2delta_F),`

`B=-1/2+(-2t^3+7ts-9n)/(2delta_F).`

Thus CFM.1 is equivalently the oriented-discriminant equation

`boxed(t^2-3s+at delta_F=0).`

The corresponding slice coefficients are obtained by substituting the displayed `A,B` into

`c=as-B,  d=-A-an.`

This gives an explicit oriented-discriminant surface for future higher moments of `Q_3`.

## 6. Relation to the singular-series programme

The exact first factor-degree masses now begin:

- degree one: controlled by the cubic tail, with exact rootless count `(p^2-1)/3`;
- degree two: `sum Q_2=p(p-1)/2`;
- degree three: `sum Q_3=(p^2-1)/3`.

The degree-three value equals the number of rootless members, but no equality of the underlying sets is asserted.

To use these masses for irreducibility, one must still control overlaps and factors of every degree up to `(p-1)/2`. The next degree-three tasks are

`sum binom(Q_3,2)`

and mixed moments such as

`sum L Q_3`, `sum Q_2 Q_3`.

The oriented-discriminant equation supplies the exact geometric object for those counts.

## 7. Audit

`cubic_factor_mass_audit.py` independently:

1. enumerates all monic irreducible cubics;
2. computes `X^p mod h` by quotient-ring exponentiation;
3. checks the coefficient condition `C+at=0`;
4. constructs the unique `(c,d)`;
5. verifies direct polynomial divisibility;
6. checks translation invariance of `C` and unique solvability in every additive orbit.

The exact audit passes for both square classes for every prime

`5<=p<=29`.

## 8. Epistemic classification

- Frobenius coefficient criterion: exact quotient-ring algebra.
- Translation invariance and orbit count: exact.
- CFM.2: exact theorem.
- Oriented-discriminant formulas: exact interpolation.
- Finite audit through `p=29`: exact independent computation.
- Higher cubic-factor moments: open.
- Full singular-series positivity: open.
- Function-field d=1 crown: open.
