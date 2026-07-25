# Exact generic-q-line crown at p=53 and p=71 with zero boundary ledger

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Classification:** **EXACT COMPUTER-ASSISTED RESULT**.  
**Scope:** targeted continuation of the complete finite-boundary counterexamples.

## 1. Setup

For a fixed nonzero cubic coefficient `a`, put

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d.
\]

Let `N_+` and `N_-` be the total numbers of irreducible members as `(c,d)` range over `F_p^2`, for a square and a nonsquare cubic coefficient respectively.

The separate boundary verifier proves at both `p=53` and `p=71` that

\[
I_+(\infty)=I_-(\infty)=I_+(2)=I_-(2)=0.
\]

Thus

\[
B_+=B_-=0,
\]

and every irreducible member counted below lies on a generic q-line cell.

## 2. Exact totals

A complete exact factorization census gives

\[
\boxed{
p=53:\qquad N_+=56,\qquad N_-=38.
}
\]

For the nonsquare class the representative was `a=2`.

At `p=71`, with nonsquare representative `a=7`, the census gives

\[
\boxed{
p=71:\qquad N_+=72,\qquad N_-=76.
}
\]

Every one of the

\[
2p^2
\]

polynomials for each prime was factored exactly over `F_p`.

## 3. Exact q-line projectors

Since `B_+=B_-=0`, the class formula

\[
N_A=(p-2)-\frac{S_0+A S_\chi}{2p}
\]

gives

\[
S_0=p\left(2(p-2)-N_+-N_-\right),
\qquad
S_\chi=p(N_--N_+).
\]

Therefore

\[
\boxed{
p=53:\qquad S_0=424,\qquad S_\chi=-954
}
\]

and

\[
\boxed{
p=71:\qquad S_0=-710,\qquad S_\chi=284.
}
\]

These are generic-sector projector traces: no finite boundary term is present.

## 4. Parity certificate

At `p=53`,

\[
56,38\notin106\mathbf Z_{\ge0},
\]

and at `p=71`,

\[
72,76\notin142\mathbf Z_{\ge0}.
\]

Thus both arithmetic classes satisfy the parity certificate at both primes.

In fact each fixed-`c` count is even: the involution

\[
X\mapsto-X
\]

pairs the constant coefficients `d` and `-d`, while the `d=0` member is reducible. The complete census is consistent with this exact cellwise parity.

## 5. Scientific consequence

The first complete-boundary failures do not threaten the crown. They show instead that the crown can be supported entirely by the generic q-line complex, with neither `q=2` nor `q=infinity` contributing a single irreducible fibre.

This closes any strategy that treats the finite boundary cells as a necessary source of positivity. It also supplies two exact out-of-sample calibrations for future proposed formulas relating the generic projectors to the Airy module.

It does not prove a uniform generic-q-line theorem.

## 6. Verification

`generic_qline_p53_p71_verify.py` reproduces the complete square/nonsquare factorization census and the displayed projector values.

Remote compute jobs:

- `6a64e68c7ef3c0846496877c` — joint `p=53,71` census;
- `6a64e6c77ef3c08464968780` — independent `p=53` total recovery.
