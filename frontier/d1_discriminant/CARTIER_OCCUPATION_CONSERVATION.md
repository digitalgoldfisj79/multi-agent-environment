# Cartier occupation conservation law

**Date:** 2026-07-21  
**Status:** exact combinatorial theorem proved.

## 1. Toeplitz minors in the selected cofactor

Let

`F=X^p+aX^3+bX^2+cX+d`

and

`G=F^(p-1)`.

In the cofactor of `I-H(F)` obtained by deleting row p and column j, expand the identity entries first. Every nonzero term is indexed by a subset

`S subset {1,...,p-1}`

containing j. The H-rows are S, and their H-columns are

`C=(S minus {j}) union {p}`.

The corresponding minor is

`det([X^(pu-v)]G)_(u in S,v in C)`.

## 2. Occupation equation

In an entry `[X^(pu-v)]F^(p-1)`, let

- `n_p` be the occupation of `X^p`;
- `n_3,n_2,n_1,n_0` be the occupations of `aX^3,bX^2,cX,d`.

Then

`n_p+n_3+n_2+n_1+n_0=p-1`,

`p n_p+3n_3+2n_2+n_1=pu-v`.

Equivalently,

`(p-3)n_3+(p-2)n_2+(p-1)n_1+p n_0`
`=p(p-1-u)+v`.

Across a complete determinant term, let A,B,C,D be the total occupations of a,b,c,d. Summing the displayed identity over rows in S, and using

`sum_(v in C)v=sum_(u in S)u-j+p`,

gives the permutation-independent law

### Theorem COC.1

`boxed((p-3)A+(p-2)B+(p-1)C+pD`
`      =(p-1) sum_(u in S)(p-u)+(p-j).)`

The right side depends only on S, not on the determinant permutation or the individual multinomial allocations.

## 3. Translation-weight target: p congruent to 1 mod 3

Put

`m=(p-1)/3`

and use the column-three cofactor with external weight `d^m`. Complete summation over b,c,d forces

`B=beta(p-1)`,

`C=gamma(p-1)`,

`D+m=delta(p-1)`

for positive integers beta,gamma,delta.

Reducing Theorem COC.1 modulo p-1 gives

`-2A-m=-2 mod p-1`.

Since primes `p congruent 1 mod 3` satisfy `p congruent 1 mod 6`, m is even, and division by two gives

`boxed(A congruent m+1 mod (p-1)/2.)`

Equivalently,

`A congruent (p+2)/3 mod (p-1)/2`.

## 4. Translation-weight target: p congruent to 2 mod 3

Put

`k=(p-2)/3`

and use the column-two cofactor with external weight `d^k`. Complete summation over b,c,d gives the same congruences for B,C and `D+k`.

Reduction modulo p-1 now yields

`-2A-k=-1 mod p-1`.

Here `p congruent 5 mod 6`, so k is odd and

`boxed(A congruent k+1 mod (p-1)/2.)`

Equivalently,

`A congruent (p+1)/3 mod (p-1)/2`.

## 5. Interpretation

The surviving powers of a occupy exactly two residue classes modulo p-1:

- the displayed base exponent;
- that exponent plus `(p-1)/2`.

These are precisely the constant and quadratic-character modes in the square class of a. Thus the two-mode reduction is not only a consequence of geometric scaling; it is forced term-by-term by the Cartier occupation law after full coefficient orthogonality.

The remaining crown calculation is a signed sum over occupation configurations satisfying Theorem COC.1. The law removes every other a-mode and makes a transfer-matrix or constant-term treatment plausible without expanding the complete determinant polynomial.
