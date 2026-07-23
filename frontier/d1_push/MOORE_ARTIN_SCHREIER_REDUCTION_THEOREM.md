# One-variable Moore–Artin–Schreier reduction for `N_a(p)`

**Date:** 2026-07-23  
**Status:** exact theorem for every prime `p>=5` and every `a in F_p^*`. It replaces the two-parameter irreducibility count by the fixed points of one explicit Frobenius-rational recurrence on `F_(p^p)^*`. It does not supply a uniform point-count bound.

## 1. Root-incidence form

Let `K=F_(p^p)` and

`F_(c,d)(X)=X^p+aX^3+cX+d`.

A non-rational element `x in K` has degree exactly `p`. For such `x`, there is at most one pair `(c,d) in F_p^2` with `F_(c,d)(x)=0`, because `1,x` are linearly independent over `F_p`.

Consequently

`p N_a(p)`

is the number of `x in K\F_p` for which

`x^p+a x^3 in span_(F_p){1,x}`.

Equivalently it is the number of degree-`p` root incidences in the depressed slice.

## 2. Frobenius differences

Put

`u=x^p-x`, `v=u^p`, `w=u^(p^2)`.

Then

`x^p=x+u`,

`x^(p^2)=x+u+v`,

`x^(p^3)=x+u+v+w`.

If `F_(c,d)(x)=0`, subtraction of the equation from its p-th power gives

`c=-v/u-a(3x^2+3xu+u^2).`  (2.1)

Imposing `c^p=c` and cancelling the quadratic terms in `x` gives a linear equation for `x`:

`3a x(u+v)=(v^2-uw)/(uv)-a(2u^2+3uv+v^2).`

For `u!=0`, one also has `u+v!=0`. Indeed `u^p=-u` would put `u` in both `F_(p^2)` and `F_(p^p)`, hence in `F_p`; then `2u=0`, so `u=0`.

Define

`Xi_a(u)`

` =[v^2-uw-a u v(2u^2+3uv+v^2)]`

`   /[3a u v(u+v)],`

where `v=u^p` and `w=u^(p^2)`.

## 3. Exact reduction

### Theorem MASR.1

For every prime `p>=5` and `a in F_p^*`,

`boxed( pN_a(p)`

` =#{u in F_(p^p)^*: Xi_a(u)^p-Xi_a(u)=u}. )`

### Proof

Every root incidence gives `u=x^p-x!=0`, and the preceding calculation forces `x=Xi_a(u)`. Thus it gives a solution of the displayed equation.

Conversely, let `u!=0` satisfy

`Xi_a(u)^p-Xi_a(u)=u`,

and put `x=Xi_a(u)`. Define `c` by (2.1). The equation used to define `Xi_a` is exactly `c^p=c`, so `c in F_p`. Put

`d=-(x^p+a x^3+cx)`.

Because `c=-(s^p-s)/(x^p-x)` for `s=x^p+a x^3`, one has `d^p=d`, hence `d in F_p`. Moreover `u!=0` implies `x notin F_p`, so `x` has degree `p` and the resulting monic degree-`p` polynomial is irreducible. The constructions `x -> u` and `u -> x` are inverse, proving the identity.

## 4. Moore determinant interpretation

The root-incidence condition may also be written as one Moore determinant:

`det [[1,x,s],[1,x^p,s^p],[1,x^(p^2),s^(p^2)]]=0`,

where `s=x^p+a x^3`.

The formula for `Xi_a` is the explicit solution obtained after passing from `x` to the Artin–Schreier difference `u=x^p-x` and enforcing Frobenius invariance of the coefficient `c`.

## 5. Audit

`moore_artin_schreier_reduction_audit.py` enumerates `F_(p^p)^*` and checks the recurrence directly.

Exact results:

- `p=5`, square class: 20 recurrence points, giving `N=4`;
- `p=5`, nonsquare class: 30 recurrence points, giving `N=6`;
- `p=7`, square class: 70 recurrence points, giving `N=10`;
- `p=7`, nonsquare class: 56 recurrence points, giving `N=8`.

The denominator had no exceptional nonzero `u`, exactly as proved above.

## 6. Strategic consequence

The reduction exposes a single semilinear dynamical object rather than a family of `p^2` Rabin tests. Its induced three-state recurrence in `(u,u^p,u^(p^2))` has rapidly growing rational degree, so no low-degree integrability claim is made. Its value is structural: it gives a second exact coordinate system for the missing global trace and a direct target for Artin–Schreier, Lefschetz or cyclic-Adams methods.

## 7. Epistemic classification

- Root-incidence count: exact.
- Moore/Frobenius elimination: exact algebra.
- Recurrence identity: exact theorem.
- Audits at `p=5,7`: exact finite computation.
- Uniform cohomological rank or trace bound: open.
- Function-field d=1 crown: open.
