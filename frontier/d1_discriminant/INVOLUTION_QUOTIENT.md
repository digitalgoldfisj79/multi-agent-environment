# Involution quotient of the cubic slice

**Date:** 2026-07-21  
**Status:** exact equivalence and discriminant formula proved.

## 1. Pairing d and -d

Fix an odd prime `p>=5`, nonzero `a in F_p`, and put

`n=(p-1)/2`.

For `d!=0`, pair

`F_(a,c,d)(X)=X^p+aX^3+cX+d`

with `F_(a,c,-d)(X)`. Set

`Y=X^2`, `e=d^2`.

Then

`F_(a,c,d)(X)F_(a,c,-d)(X)`
` =(X^p+aX^3+cX)^2-d^2`
` =Y(Y^n+aY+c)^2-e`.

Define the monic degree-p quotient polynomial

`G_(a,c,e)(Y)=Y(Y^n+aY+c)^2-e`.

## 2. Exact irreducibility equivalence

### Theorem IQ.1

For every `d!=0`,

`F_(a,c,d)` is irreducible over F_p

if and only if

`G_(a,c,d^2)` is irreducible over F_p.

### Proof

If F is irreducible and x is a root in `F_(p^p)`, then `y=x^2` has degree p. Indeed, if y lay in F_p then x would satisfy a polynomial of degree at most two, impossible for p>=5. The p conjugates of y are roots of G, so G is its monic minimal polynomial and is irreducible.

Conversely, suppose G is irreducible and y is a root in `F_(p^p)`. Its norm is

`Norm(y)=e=d^2`,

because p is odd and the constant term of G is `-e`. In an odd-degree finite-field extension, an element is a square if and only if its norm is a square. Hence `y=x^2` for some `x in F_(p^p)`.

The equation G(y)=0 gives

`[x(x^(p-1)+ax^2+c)]^2=d^2`.

Therefore either x or -x is a root of `F_(a,c,d)`. That root has degree p, so F is irreducible. QED.

Consequently

`N_a(p)=2 * # {(c,e): e is a nonzero square and G_(a,c,e) is irreducible}`.

This gives a conceptual explanation for the exact evenness of every fixed-a count.

## 3. Critical-point collapse

Put

`H(Y)=Y^n+aY+c`,

`phi(Y)=YH(Y)^2`.

Since `1+2n=p=0` in F_p,

`phi'(Y)`
` =H(Y)[H(Y)+2YH'(Y)]`
` =H(Y)(3aY+c)`.

Thus the degree-p map phi has only two finite critical values:

1. zero, containing all roots of H;
2. `beta=phi(-c/(3a))`.

The quotient family is `G=phi-e`. This is a three-branch wild degree-p cover rather than a generic degree-p polynomial.

## 4. Exact discriminant

Let

`y0=-c/(3a)`,

`beta=phi(y0)`.

The derivative factorization gives

`Res(G,H)=e^n`

and

`Res(G,3aY+c)=-3a(beta-e)`.

Since `p(p-1)/2` has parity n, the monic discriminant is

### Theorem IQ.2

`Disc_Y G_(a,c,e)`
` =(-1)^(n+1) 3a e^n (beta-e)`.

This formula has been checked symbolically in characteristics 5,7,11,13.

For the square values `e=d^2`, the factor `e^n` is a square. Hence the factorization parity of G is controlled by one quadratic character of the second critical value.

## 5. Coalesced critical-value loci

The two finite critical values coalesce exactly when `H(y0)=0`, equivalently when H has a double root at y0.

For `c!=0`, this forces

`c=3/2` or `c=-3/2`,

with the corresponding quadratic-character compatibility condition on a. Writing

`s=chi(y0)=+1 or -1`,

one has

`2ay0=s`, `c=-3s/2`.

After scaling `Y=y0 Z`, the map becomes, up to the nonzero target scalar y0,

`Phi_p(Z)=Z[Z^n+(Z-3)/2]^2`.

Moreover

`Z^n+(Z-3)/2=(Z-1)^2 L_p(Z)`

where

`L_p(Z)=sum_(j=0)^(n-2)(n-1-j)Z^j`.

Thus the coalesced map is the universal one-branch form

`Phi_p(Z)=Z(Z-1)^4 L_p(Z)^2`.

This is independent of a after source and target scaling.

## 6. Empirical status of the coalesced construction

A direct scan of the special `c=+/-3/2` fibres shows that they sometimes contain irreducible members but often do not. The coalesced locus is therefore not by itself a universal construction.

Its value is structural: it identifies a canonical wild two-branch specialization whose monodromy and fibre factorization can be studied independently of a.

## 7. Strategic consequence

The quotient gives a second exact crown formulation:

> prove that, for at least one nonzero a, the two-parameter family
> `Y(Y^((p-1)/2)+aY+c)^2-e`, with e restricted to nonzero squares,
> contains an irreducible degree-p member.

Compared with the original cubic slice, this formulation has:

- no d-to-minus-d duplication;
- an explicit two-critical-value map;
- a one-line discriminant;
- a generic S_p monodromy route through the isolated critical point;
- a distinguished coalesced specialization for testing wild-cover constructions.