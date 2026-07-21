# First-Witt adjugate formula for the Hasse--Witt indicator

**Date:** 2026-07-21  
**Status:** exact matrix expansion proved; aggregate nonvanishing remains open.

## 1. Notation

Let `n=p-1`, and let

`B=Beta_p(F) mod p^2`,

`Beta_(p^2)=B^2+p Gamma mod p^2`.

Write uniquely

`B=B0+pB1 mod p^2`,

where `B0` is the entrywise canonical lift of `B mod p` and `B1` is a matrix over `F_p`.

## 2. Correct noncommutative expansion

One has

`B-Beta_(p^2)=B-B^2-p Gamma`

and therefore

`B-Beta_(p^2)=A0+pC mod p^2`,

where

`A0=B0-B0^2`,

`C=B1-B0B1-B1B0-Gamma mod p`.

The two mixed products are distinct. The tempting abbreviation `B1(I-2B0)` is invalid unless `B0` and `B1` commute.

For any integral matrix `A0` whose determinant is divisible by p,

`det(A0+pC)=det(A0)+p Tr(adj(A0)C) mod p^2`.

Hence, defining

`qdet_p(A0)=det(A0)/p mod p`,

we obtain the exact first-order formula

`K_a(c,d)=qdet_p(A0)+Tr(adj(A0 mod p) C) mod p`.

If `A0 mod p` has corank at least two, both terms vanish: its adjugate is zero and its determinant is divisible by `p^2`.

## 3. Factorization through the ordinary Hasse--Witt determinant

Because

`A0=B0(I-B0)`,

one has over the integers

`det(A0)=det(B0)det(I-B0)`.

For a squarefree polynomial, `B0 mod p` represents reduced Frobenius. Its determinant is the sign of Frobenius on the roots. By Pellet's formula this is the discriminant character. Both sides are polynomial functions of the coefficients of the universal monic polynomial, and the squarefree locus is dense. Degree comparison is exact:

- `det(B0)` has total coefficient degree `(p-1)^2`;
- `Disc(F)^((p-1)/2)` has degree `(2p-2)(p-1)/2=(p-1)^2`.

Thus the universal polynomial identity is

`det(B0)=Disc(F)^((p-1)/2) mod p`.

Also `det(I-B0)=0 mod p` identically: every reduced Frobenius partition of total degree p gives a characteristic polynomial vanishing at one, and in the irreducible p-cycle case its value is p, which is zero modulo p.

Define the determinantal Fermat quotient

`Q_p(F)=det(I-B0)/p mod p`.

On the squarefree locus, where `B0` is invertible, the indicator can be written

`K_a(c,d)=Disc(F)^((p-1)/2) * (Q_p(F)-L_p(F)) mod p`,

where

`L_p(F)=Tr(adj(I-B0 mod p) B0^(-1) Gamma)`

with the remaining lift correction incorporated by the exact matrix C above. Equivalently, without choosing an inverse or separating lift terms, use the universal `qdet+adjugate` formula of Section 2.

## 4. Interpretation

The two terms have different origins:

1. `Q_p(F)` is the first p-adic failure of the ordinary Hasse--Witt matrix to have exact eigenvalue one;
2. the adjugate pairing with `Gamma` is the first Witt correction that replaces the ordinary Hasse--Witt approximation by actual unit-root Frobenius.

Neither term is individually an irreducibility indicator. For a squarefree product of two irreducible factors, `I-B0` has corank one, so both first-order terms may be nonzero; the Dwork correction cancels the determinantal Fermat quotient exactly. For an irreducible p-cycle, their corrected sum is one.

## 5. Exhaustive decomposition data

A `python-flint` computation evaluated the two contributions for both square classes at `p=5,7,11,13`, over every `c` and every `d!=0`. In every case:

- the final value K was 0 or 1 and reproduced the certified irreducible counts;
- reducible members frequently had nonzero `K0=det(B-B^2)/p` and nonzero correction `KG=K-K0`, but `K0+KG=0`;
- irreducible members had `K0+KG=1`;
- no divisibility failure occurred.

The aggregate residues `(sum K, sum K0, sum KG)` were:

- `p=5`: square `(4,4,0)`, nonsquare `(1,2,4)`;
- `p=7`: square `(3,4,6)`, nonsquare `(1,5,3)`;
- `p=11`: square `(3,7,7)`, nonsquare `(3,2,1)`;
- `p=13`: square `(10,12,11)`, nonsquare `(6,11,8)`.

These data reject a naive claim that either first-order term alone has a fixed or one-character formula.

## 6. Remaining exact target

The crown is now to evaluate, after summing over `c in F_p` and `d in F_p^*`,

`sum qdet_p(B0-B0^2) + sum Tr(adj(B0-B0^2)C)`.

The required compression must preserve the cancellation on two-factor members. Promising exact forms are:

1. a constant-term identity for the complete corrected determinant, rather than for either term separately;
2. a matrix-tree formula for `adj(I-B0)` combined with the sparse vector `X F'(X)=3aX^3+cX`;
3. Cauchy--Binet followed by finite-field orthogonality before the coefficient sums are expanded.
