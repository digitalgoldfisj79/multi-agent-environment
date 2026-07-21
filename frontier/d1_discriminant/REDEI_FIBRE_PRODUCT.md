# The Redei fibre product and its rational components

**Date:** 2026-07-21  
**Status:** exact decomposition and parameterization proved.

## 1. The one-branch polynomial

Let

`n=(p-1)/2`

and define

`D_p(U)=U(U^2-1)^n`.

Its derivative is

`D_p'(U)=-(U^2-1)^(n-1)`.

Thus zero is its only finite critical value. The fibres above zero have one simple point U=0 and two points U=+/-1 of multiplicity n.

This polynomial arose from the universal coefficient product because

`A^n=D_p(W^n)`

and

`B^n=D_p(Q^n)`.

## 2. A rational square transformation

Put

`Z=1/(U^2-1)`.

Then

`D_p(U)^2`
` =U^2(U^2-1)^(p-1)`
` =(Z+1)/Z^p`.

Therefore equality of squared D-values is the rational equation

`(Z+1)R^p=(R+1)Z^p`,

where `R=1/(V^2-1)`.

Away from the diagonal R=Z, put

`q=R/Z`.

The equation becomes

`q^p(Z+1)=qZ+1`,

so

`Z=(1-q^p)/(q^p-q)`.

Using `1-q^p=(1-q)^p`, one obtains

`U^2=(1-q)^(-(p-1))`,

`V^2=q^(p-1)(1-q)^(-(p-1))`.

## 3. Exact component parameterization

Fix `r in {+1,-1}` and consider

`D_p(V)=r D_p(U)`.

For each `sigma in {+1,-1}`, define

`U=sigma (1-q)^(-n)`,

`V=r sigma q^n (1-q)^(-n)`.

A direct substitution gives

`D_p(V)=rD_p(U)`.

Conversely, every off-diagonal point of the fibre product has this form. Indeed q is recovered rationally as

`q=(U^2-1)/(V^2-1)`.

Thus each sigma gives a rational, absolutely irreducible component, birational to the q-line.

### Theorem RFP.1

For each r=+/-1, the plane curve

`D_p(V)-rD_p(U)=0`

has exactly three absolutely irreducible components:

1. the diagonal line `V-rU=0`;
2. a rational component `C_(r,+)` of degree n;
3. a rational component `C_(r,-)` of degree n.

The two rational components are parameterized by the displayed formulas with sigma=+1 and sigma=-1.

The degree statement follows because projection to U has generic degree n on each off-diagonal component, while the total degree is p=1+n+n.

## 4. Exact factorization

There are absolutely irreducible polynomials `H_(r,+),H_(r,-)` of total degree n such that

`D_p(V)-rD_p(U)`
` =(V-rU) H_(r,+)(U,V) H_(r,-)(U,V)`.

The parameterization supplies a constructive definition of the two H factors. Equivalently they can be obtained by eliminating q from

`U(1-q)^n-sigma=0`,

`V(1-q)^n-r sigma q^n=0`.

A clean Sage factorization for p=5,7,11,13,17 gives exactly the degrees `1,n,n` for both r signs. Audit job:

`6a5fc65c13e6ef894d54a215`.

## 5. Interpretation as coefficient-character cells

Let eta and kappa be signs. In the universal coefficient product, eta records the square class of a and kappa the square class of nonzero c.

For formal W,Q define

`U=W^n`, `V=Q^n`, `epsilon=chi(-1)`.

The product over all a with `chi(a)=eta` and all c with `chi(c)=kappa` is, after eliminating d,

`H_(eta,kappa)(U,V)`
` =product_(chi(a)=eta) [(W+aQ)^n-kappa epsilon]`.

It is invariant under independent multiplication of W and Q by nth roots of unity, hence is a polynomial in U,V of total degree n.

The complete eta-class polynomial factors as

`R_(p,eta)`
` =(U-eta epsilon V) H_(eta,+)(U,V) H_(eta,-)(U,V)`.

The linear factor is the c=0 cell. The two degree-n factors are the nonzero-square and nonsquare c cells. Under the identification

`r=eta epsilon`,

they are exactly the two rational off-diagonal components of Theorem RFP.1.

## 6. Strategic conclusion

The Redei factorization is a genuine exact compression, but it does not create an additional constructive subfamily. Its three components unwind precisely to

- c=0;
- chi(c)=+1;
- chi(c)=-1.

Substituting the rational parameterization back into `U=W^n`, `V=Q^n` yields constants a and c satisfying

`W+aQ+c=0`.

Thus this route reorganizes the coefficient plane and proves its hidden affine-square monodromy, but it does not by itself force a degree-p factor. Any crown proof through the universal product must still establish degree-p nonvanishing in at least one of these coefficient-character cells.