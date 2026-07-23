# Full Fourier transform of the root permutation sheaf

**Date:** 2026-07-23  
**Status:** exact Fourier–Deligne calculation for every prime `p>=5`. Away from zero dual d-frequency, the rank-p root permutation sheaf transforms into a single rank-one Legendre sheaf. On the c-pencil slice at nonzero frequency, the original root sheaf contributes zero; all nonzero primitive Fourier mass comes from the cyclic Adams convolution.

## 1. Root cover as a graph

Let

`X_a=A^2_(x,c)`

and define the finite degree-p map

`q_a:X_a -> Y=A^2_(c,d)`

by

`q_a(x,c)=(c,-x^p-a x^3-cx).`

The root permutation sheaf is

`P_a=q_(a,! ) Q_l`.

Let `(kappa,lambda)` be the dual coordinates to `(c,d)`.

## 2. Fourier kernel

Using the unnormalized Fourier–Deligne transform for clarity, the pullback of the Fourier kernel to `X_a` is

`L_psi(kappa c+lambda d)`

`=L_psi(-lambda x^p-a lambda x^3+c(kappa-lambda x)).`

Thus

`FT_(c,d)(P_a)`

is the compactly supported pushforward in `(x,c)` of this rank-one sheaf.

## 3. Exact integration in c

For fixed `(x,kappa,lambda)`,

`R Gamma_c(A^1_c,L_psi(c(kappa-lambda x)))`

vanishes when

`kappa-lambda x!=0`,

and is the one-dimensional top Tate class when

`kappa-lambda x=0`.

### Theorem RFF.1 — rank-one Fourier transform

On the open set `lambda!=0`, there is a unique solution

`x=kappa/lambda`,

and, up to the standard Fourier shift and Tate twist,

`boxed(FT_(c,d)(P_a)|_(lambda!=0)`

` =L_psi(-kappa^p/lambda^(p-1)-a kappa^3/lambda^2).)`

In particular this is a rank-one lisse sheaf on the appropriate open subset of the dual plane.

## 4. Frobenius-coboundary form

Over the perfection of the lambda-line, choose `nu` with

`nu^p=lambda`.

Then

`kappa^p/lambda^(p-1)`

`=(kappa/nu^(p-1))^p`.

Since `L_psi(g^p)` is isomorphic to `L_psi(g)`, the first term is an Artin–Schreier Frobenius coboundary reduction. The genuinely nonlinear part is the fixed cubic rational phase

`-a kappa^3/lambda^2`.

Thus even before the Adams operation, the full Fourier kernel has fixed algebraic complexity after a universal purely inseparable base change.

## 5. The lambda=0 slice

When `lambda=0`, the c-integral is

`R Gamma_c(A^1_c,L_psi(kappa c)).`

It vanishes for `kappa!=0`. At `(kappa,lambda)=(0,0)` it contributes only the constant top Tate class from `A^2_(x,c)`.

### Corollary RFF.2 — no nonzero c-frequency from P

`boxed(FT_(c,d)(P_a)|_(lambda=0,kappa!=0)=0.)`

Hence, on the nonzero c-pencil Fourier locus, the defect

`W_a=Psi^p(P_a)-P_a`

has the same Fourier transform as `Psi^p(P_a)` alone.

The constant/main correction from `-P_a` is confined to Fourier frequency zero.

## 6. Convolution form of the terminal object

Fourier transform exchanges tensor product in `(c,d)` with additive convolution on the dual plane. Therefore

`FT(Psi^p(P_a))`

is the cyclic trace of the p-fold additive convolution of the rank-one sheaf in RFF.1.

The terminal c-pencil object is its restriction to

`lambda_total=0`,  `kappa_total!=0`.

Thus the remaining rank-four problem is precisely:

> compute the cyclic p-fold convolution of one explicit rank-one Legendre sheaf on the zero-sum lambda fibre, and show that its stationary-phase contribution is the isolated A2 Adams difference after the known Kummer and Artin–Schreier pieces are removed.

This formulation contains no hidden rank-p input sheaf: the only growth is in the cyclic convolution length.

## 7. Function-field trace form

At a finite field point, the cyclic trace of the p-fold convolution is equivalently a sum over a Frobenius orbit in the rank-one Fourier kernel. The trace constraints are the Fourier-dual form of the Moore conditions

`x^p+a x^3 in span_(F_p){1,x}`.

This explains why the Moore–Artin–Schreier reduction and the cyclic Fourier route are exact dual descriptions of the same residual object.

## 8. Epistemic classification

### Exact

- graph description of the root cover;
- Fourier kernel after pullback;
- compact c-integration;
- rank-one formula on `lambda!=0`;
- vanishing on `lambda=0,kappa!=0`;
- confinement of the original `P_a` term to zero c-frequency;
- reduction of the nonzero-frequency problem to cyclic convolution of one rank-one sheaf.

### Open

- stationary phase of the p-fold cyclic convolution on `lambda_total=0`;
- exact wild-corner subtraction;
- rank-four theorem and conductor bound.
