# Root-negation quadratic descent for the depressed d=1 slice

**Date:** 2026-07-23  
**Status:** exact theorem for every prime `p>=5` and every `a in F_p^*`. It gives a degree-preserving descent of the paired polynomials `F_(c,d),F_(c,-d)` to one degree-`p` polynomial in `Y`, proves the evenness of `N_a` structurally, and gives the complete discriminant of the descended family. It does not by itself prove positivity.

## 1. Setup

Put

`m=(p-1)/2`,

`F_(c,d)(X)=X^p+aX^3+cX+d`,

`H_c(Y)=Y^m+aY+c`,

and

`G_(c,e)(Y)=Y H_c(Y)^2-e`.

The polynomial `G_(c,e)` is monic of degree `2m+1=p`.

## 2. Product identity

Because `X^(p-1)=(X^2)^m`,

`X H_c(X^2)=X^p+aX^3+cX`.

Therefore, for every `c,d`,

### Theorem RNQD.1 — exact root-negation product

`boxed( G_(c,d^2)(X^2)=F_(c,d)(X)F_(c,-d)(X). )`

This is an identity in `F_p[X]`.

## 3. Irreducibility descent

Assume `d!=0`.

### Theorem RNQD.2 — degree-preserving quadratic descent

The following are equivalent:

1. `F_(c,d)` is irreducible over `F_p`;
2. `F_(c,-d)` is irreducible over `F_p`;
3. `G_(c,d^2)` is irreducible over `F_p`.

### Proof

Suppose `F_(c,d)` is irreducible and let `alpha` be a root. Then

`alpha H_c(alpha^2)=-d`.

Put `y=alpha^2`. By RNQD.1, `G_(c,d^2)(y)=0`. Since `[F_p(alpha):F_p]=p` and `[F_p(alpha):F_p(y)]` divides `2`, the latter degree cannot be `2`; hence `F_p(y)=F_p(alpha)` and `y` has degree `p`. Since `G_(c,d^2)` also has degree `p`, it is irreducible.

Conversely, suppose `G_(c,d^2)` is irreducible and let `y` be a root in `F_(p^p)`. Its norm is

`Norm_(F_(p^p)/F_p)(y)=d^2`,

because `p` is odd and the constant term of `G` is `-d^2`. An element of `F_(p^p)^*` is a square exactly when its norm to `F_p` is a square: both quadratic characters are given by exponent `(p^p-1)/2`, and the quotient by `(p-1)/2` is odd. Thus `y=alpha^2` for some `alpha in F_(p^p)`. RNQD.1 gives

`F_(c,d)(alpha)F_(c,-d)(alpha)=0`.

The chosen factor has a root of degree `p` and is monic of degree `p`, so it is irreducible. Replacing `alpha` by `-alpha` exchanges the two factors, proving both are irreducible.

## 4. Exact count consequence

Let

`J_a(p)=#{(c,e): c in F_p, e in (F_p^*)^2, G_(c,e) irreducible}.`

Every nonzero square `e` has exactly two square roots `+/-d`, and RNQD.2 gives:

### Corollary RNQD.3

`boxed( N_a(p)=2 J_a(p). )`

In particular, `N_a(p)` is even. This is a geometric explanation of the previously proved free root-negation involution.

## 5. Critical points and discriminant

In characteristic `p`, `2m=p-1=-1`. Differentiating gives

`G'_(c,e)(Y)=H_c(Y)[H_c(Y)+2YH'_c(Y)]`

`              =H_c(Y)(3aY+c).`

Thus the finite critical locus consists of:

- the roots of `H_c`, all mapping to the branch value `e=0`;
- the single point `y_0=-c/(3a)`.

Put

`B_a(c)=y_0 H_c(y_0)^2`.

Using resultants,

`Res(G,H_c)=e^m`,

and

`Res(G,3aY+c)=3a(e-B_a(c)).`

Since `p(p-1)/2` has parity `m`, the monic discriminant is:

### Theorem RNQD.4 — complete discriminant

`boxed( Disc_Y G_(c,e)=(-1)^m 3a e^m(e-B_a(c)). )`

For square `e!=0`, `e^m=1`, so the discriminant square class is governed only by the two-branch expression

`(-1)^m 3a(e-B_a(c)).`

The universal cover

`(c,Y) -> (c,e=Y H_c(Y)^2)`

therefore has only the explicit finite branch divisors `e=0` and `e=B_a(c)`, plus the wild fibre at infinity.

## 6. Audit

`root_negation_quadratic_descent_audit.py` verifies RNQD.2 and RNQD.3 by exact factorisation for both square classes at every prime `5<=p<=43`.

`root_negation_descent_discriminant_audit.py` verifies RNQD.4 for every `c`, every nonzero `e`, both square classes, and every prime `5<=p<=101`. No mismatch occurred.

## 7. Strategic consequence

The depressed slice is no longer merely a two-parameter list of sparse polynomials. After pairing `d` with `-d`, it is the square-value sector of one explicit degree-`p` cover with derivative

`H_c(Y)(3aY+c)`

and only two finite branch divisors. This is the natural geometric object on which to apply the p-th Adams-operation irreducibility detector and a global localization argument.

## 8. Epistemic classification

- Product identity: exact algebra.
- Irreducibility equivalence: exact finite-field degree and norm argument.
- Count identity and evenness: exact.
- Derivative and discriminant: exact algebra/resultants.
- Finite audits: exact machine verification.
- Adams localization and a uniform trace bound: open.
- Function-field d=1 crown: open.
