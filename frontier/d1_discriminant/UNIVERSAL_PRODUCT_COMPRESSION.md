# Universal product compression for the cubic slice

**Date:** 2026-07-21  
**Status:** exact algebraic identity proved; degree-p factor nonvanishing remains open.

## 1. Family products

Fix a prime `p>=5`. Put

`F_(a,c,d)(X)=X^p+aX^3+cX+d`.

Let

`V=X^p-X`,

`W=V^(p-1)`,

`Q=(X^(3p)-X^3)/V=X^(2p)+X^(p+1)+X^2`.

The quotient Q is a polynomial because `X^(3p)-X^3=(X^p-X)(X^(2p)+X^(p+1)+X^2)`.

For fixed a and c, eliminate d by the finite-field product identity

`product_(d in F_p)(Y+d)=Y^p-Y`.

This gives

`product_d F_(a,c,d)`
` =X^(p^2)-X^p+a(X^(3p)-X^3)+c(X^p-X)`
` =V(W+aQ+c)`.

Eliminating c next gives

`product_(c,d) F_(a,c,d)`
` =V^p [(W^p-W)+a(Q^p-Q)]`.

Write

`A=W^p-W`, `B=Q^p-Q`.

Thus the complete fixed-a product is simply

`P_a(X)=V^p(A+aB)`.

This is an exact compression of all `p^2` coefficient pairs into two Artin--Schreier differences.

## 2. Square-class products

Let

`n=(p-1)/2`, `epsilon=chi(-1)`.

For an indeterminate Z,

`product_(a square)(Z+a)=Z^n-epsilon`,

`product_(a nonsquare)(Z+a)=Z^n+epsilon`.

Consequently

`P_square(X)=product_(a square,c,d) F_(a,c,d)(X)`
` =V^(pn) [A^n-epsilon B^n]`,

and

`P_nonsquare(X)=product_(a nonsquare,c,d) F_(a,c,d)(X)`
` =V^(pn) [A^n+epsilon B^n]`.

Multiplying the two classes gives

`P_nonzero_a(X)`
` =V^(p(p-1)) [A^(p-1)-B^(p-1)]`.

## 3. Descent to T=X^(p-1)

For `lambda in F_p^*`,

`V(lambda X)=lambda V(X)`,

`W(lambda X)=W(X)`,

`Q(lambda X)=lambda^2 Q(X)`.

Therefore both class brackets are invariant under `X -> lambda X`. Every exponent occurring in them is divisible by `p-1`, so each is a polynomial in

`T=X^(p-1)`.

Define

`w(T)=T(T-1)^(p-1)`,

`q(T)=T^2+T+1`,

`s(T)=T^2 q(T)^p-q(T)`.

Then

`W=w(T)`,

`A=w(T)^p-w(T)`,

`B=X^2 s(T)`.

Since `2n=p-1`,

`B^n=T s(T)^n`.

Hence the two explicit class polynomials are

`R_(p,+)(T)=[w(T)^p-w(T)]^n-epsilon T s(T)^n`,

`R_(p,-)(T)=[w(T)^p-w(T)]^n+epsilon T s(T)^n`.

Here + denotes the square class and - the nonsquare class. Their degrees are

`deg R_(p,+)=deg R_(p,-)=p^2(p-1)/2`.

The universal identities are

`P_square(X)=V^(pn) R_(p,+)(X^(p-1))`,

`P_nonsquare(X)=V^(pn) R_(p,-)(X^(p-1))`.

For all nonzero a,

`R_p(T)=R_(p,+)(T)R_(p,-)(T)`
` =[w^p-w]^(p-1)-T^2 s^(p-1)`

and

`product_(a!=0,c,d)F_(a,c,d)(X)`
` =V^(p(p-1))R_p(X^(p-1))`.

## 4. Factor-degree bound

### Theorem UPC.1

Every irreducible factor of either `R_(p,+)` or `R_(p,-)` has degree at most p.

### Proof

Let t be any root of one of the class polynomials and choose x in the algebraic closure with `x^(p-1)=t`. The corresponding universal product vanishes at x. Hence at least one family polynomial `F_(a,c,d)` in that square class vanishes at x.

Therefore

`[F_p(x):F_p] <= p`.

Since `t=x^(p-1)`,

`[F_p(t):F_p] <= [F_p(x):F_p] <= p`.

Thus the minimal polynomial of t has degree at most p. QED.

This converts the entire factor sieve into the factorization of one explicit polynomial whose factor degrees are automatically p-smooth.

## 5. Exact relation to irreducible slices

Let `N_+(p)` and `N_-(p)` denote the number of irreducible members in one square and one nonsquare fixed-a slice. Scaling X shows these counts are constant inside each square class.

Every irreducible degree-p family polynomial occurs once in the corresponding universal product. Its p roots form free orbits under multiplication by `F_p^*` when all a in the same square class are included. Passing from x to

`t=x^(p-1)`

quotients exactly by this action.

A degree-p x cannot give `t in F_p`: otherwise x would satisfy `X^(p-1)-t` and have degree at most `p-1`. Thus every resulting t has degree p.

Conversely, every degree-p factor of `R_(p,+)` or `R_(p,-)` lifts to roots of an irreducible degree-p family member in that class.

### Theorem UPC.2

Let `I_p(R)` denote the number of distinct monic irreducible degree-p factors of R over F_p. Then

`N_+(p)=2 I_p(R_(p,+))`,

`N_-(p)=2 I_p(R_(p,-))`.

In particular, the d=1 cubic-slice crown is equivalent to proving that at least one of the two explicit polynomials `R_(p,+),R_(p,-)` has a degree-p factor for every prime p.

The theorem also explains the exact evenness of every fixed-a irreducible count.

## 6. Exact gcd formulation

Because p is prime, the only irreducible degrees dividing p are 1 and p. Therefore

`p I_p(R)`
` =deg gcd(R,T^(p^p)-T)-deg gcd(R,T^p-T)`.

Applied to either class polynomial, this gives an exact univariate crown criterion. Unlike the fixed-period factorial sieve, it already includes every factor degree simultaneously.

## 7. Computational audit

A clean Sage factorization of `R_p` gave:

- p=5: 5 degree-5 factors;
- p=7: 9 degree-7 factors;
- p=11: 14 degree-11 factors;
- p=13: 8 degree-13 factors.

These values equal `(N_+(p)+N_-(p))/2` from the independently computed slice counts. Every displayed degree-p factor passed the exact norm-one check

`T^((p^p-1)/(p-1))=1 mod h(T)`.

Hugging Face audit job: `6a5fc170d09dc1f57c6bfe62`.

A direct standard-library symbolic multiplication at p=5 also verifies the universal product identity coefficient by coefficient.

## 8. New frontier

The determinant, dynatomic sieve and universal product are now three exact presentations of the same crown obstruction:

1. the selected Frobenius cofactor asks for a full p-cycle;
2. the aligned cycle polynomial records all factor degrees;
3. `R_(p,+/-)` packages all coefficient pairs and all low-period incidences into one p-smooth univariate factorization.

The next useful target is not another fixed factor degree. It is a structural factorization or nonvanishing theorem for the degree-p part of `R_(p,+/-)`, preferably through its nested Artin--Schreier form `A=W^p-W`, `B=Q^p-Q`.