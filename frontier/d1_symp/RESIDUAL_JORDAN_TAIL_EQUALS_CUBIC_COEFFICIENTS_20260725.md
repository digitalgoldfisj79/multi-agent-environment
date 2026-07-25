# Residual Jordan tail equals the cubic coefficient space

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** residual local object after the wild-infinity Pascal pairing.  
**Status:** the Newton identification below is **PROVED**. The cohomological elimination that reaches this residual object is still **OPEN**.

## 1. Sparse root equations

Let `x_1,...,x_p` be ordered roots and write

\[
\prod_{i=1}^p(T-x_i)
=T^p-e_1T^{p-1}+e_2T^{p-2}-\cdots-e_p.
\]

Assume

\[
s_1=s_2=\cdots=s_{p-4}=0,
\qquad
s_k=\sum_i x_i^k.
\]

Since every integer `1,...,p-4` is invertible in characteristic `p`, Newton identities give

\[
e_1=e_2=\cdots=e_{p-4}=0.
\]

Thus the polynomial has the sparse form

\[
T^p+AT^3+BT^2+CT+D,
\]

with

\[
A=e_{p-3},
\qquad
B=-e_{p-2},
\qquad
C=e_{p-1},
\qquad
D=-e_p.
\]

## 2. Exact tail identities

For `k<p`, Newton's identity is

\[
s_k-e_1s_{k-1}+\cdots+(-1)^{k-1}e_{k-1}s_1
+(-1)^k k e_k=0.
\]

At `k=p-3,p-2,p-1`, all earlier terms vanish. Hence

\[
s_k=(-1)^{k+1}k e_k.
\]

Using `p=0` gives

\[
\boxed{s_{p-3}=3A,}
\]

\[
\boxed{s_{p-2}=2B,}
\]

and

\[
\boxed{s_{p-1}=C.}
\]

The factors `3,2,1` are units for the admitted primes `p=5 mod 6`.

## 3. Consequence for the wild-infinity reduction

The Pascal-pairing theorem leaves, on the associated graded, exactly the normal levels

\[
s_{p-3},s_{p-2},s_{p-1}.
\]

The theorem above identifies these levels integrally and diagonally with

\[
A,B,C.
\]

Therefore the residual three-level Smith-defect object is not a new parameter space. It is precisely the cubic-tail coefficient space already used in the finite irreducibility and q-line ledgers. The constant coefficient `D` is the diagonal/translation direction and is treated separately by the affine orbit and punctual terms.

This removes a further transport ambiguity: once clean integral Fourier elimination through the first `p-4` Jordan levels is proved, the surviving local variables land directly in the existing cubic family with no unidentified change of coordinates or `p`-adic denominator.

## 4. Relation to the q-line normal form

On the open cell `A!=0`, affine translation and scaling act on `(A,B,C,D)`. The established normal-form ledger depresses the quadratic coefficient and records the remaining linear coefficient by

\[
q=-3/c
\]

and the split/nonsplit class by the quadratic character of the scaled cubic coefficient.

Since the residual Jordan coordinates are `(3A,2B,C)`, all transformations used in that ledger are transformations of the residual Smith-defect tail itself. The cells `q=2`, `q=infinity`, the discriminant fibres and the Artin--Schreier orbit are therefore exactly the boundary strata of the residual three-level object.

## 5. Exact remaining step

Prove that the integral Fourier transform along the unimodular first `p-4` filtered levels is clean and carries no additional characteristic-zero defect. The resulting residual nearby-cycle complex then lives directly on `(A,B,C)` and can be compared term-by-term with the already proved q-line projector complex.

No additional coefficient dictionary is required.

## 6. Ruling

### PROVED

- the sparse power-sum equations are equivalent to `e_1=...=e_(p-4)=0`;
- the residual Jordan levels are exactly `(3A,2B,C)`;
- the residual local parameter space is the cubic/q-line coefficient space.

### OPEN

- clean integral Fourier elimination through the nonsplit filtered levels;
- the Frobenius trace on the resulting residual q-line complex;
- the crown.

The application wall is now the cohomological cleanliness of one explicit unimodular filtered elimination, not an unknown geometric transport map.
