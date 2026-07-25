# Complete finite-boundary vanishing at p=53 and p=71

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Classification:** **EXACT COMPUTER-ASSISTED RESULT**.  
**Scope:** boundary-only bypasses for the function-field `d=1` crown.

## 1. Boundary families

For `p congruent 5 mod 6`, the two finite boundary locations in the exact q-line ledger are:

### q=infinity

\[
X^p+aX^3+d.
\]

### q=2

The split and nonsplit readings are

\[
X^p+\frac12X^3-\frac32X+d
\]

and

\[
X^p+\frac1{2\eta}X^3-\frac32X+d,
\]

where `eta` is any fixed nonsquare.

Their counts are

\[
I_+(\infty),\ I_-(\infty),\ I_+(2),\ I_-(2).
\]

The branch proves uniformly that

\[
I_+(\infty)=0,
\]

and proves `I_+(2)=0` when `chi(2)=+1`. At the earlier calibrated primes, some nonsquare infinity counts were positive, suggesting a possible boundary bypass.

## 2. Exact complete-boundary counterexamples

The deterministic verifier gives the stronger identities

\[
\boxed{
I_+(\infty)=I_-(\infty)=I_+(2)=I_-(2)=0
\quad\text{at }p=53
}
\]

and

\[
\boxed{
I_+(\infty)=I_-(\infty)=I_+(2)=I_-(2)=0
\quad\text{at }p=71.
}
\]

The nonsquare infinity representatives are `a=2` at `p=53` and `a=7` at `p=71`.

For the nonsquare infinity slice, the complete factor diagnostic is:

| `p` | nonsquare `a` | fibres with a linear factor | remaining reducible fibres | irreducible fibres |
|---:|---:|---:|---:|---:|
| 53 | 2 | 35 | 18 | 0 |
| 71 | 7 | 47 | 24 | 0 |

Both q=2 readings also have zero irreducible fibres at both primes.

Thus the complete boundary counts satisfy

\[
\boxed{B_+=B_-=0}
\]

at `p=53` and `p=71`.

## 3. Exact certification method

For a monic polynomial `f` of prime degree `p` over `F_p`, irreducibility is equivalent to:

1. `gcd(f,X^p-X)=1`; and
2. `X^(p^p)=X mod f`.

The verifier applies these exact polynomial-arithmetic tests to every constant coefficient in all four boundary readings. No floating-point computation, probabilistic factorization or sampling is used.

## 4. Ruling

### Closed

1. Uniform positivity of the nonsquare q=infinity boundary.
2. Any proof that uses only the two finite boundary locations `q=2` and `q=infinity`.
3. Any assertion that one of the four finite boundary readings must contain an irreducible fibre.

At `p=53` and `p=71`, the crown—if true—must be supplied entirely by the generic q-line cells.

### Still possible

A theorem using the generic invariant/quadratic q-line projectors, possibly combined with congruence information. The counterexamples do not address those generic cells.

## 5. Verification

`q_infinity_nonsquare_counterexample_verify.py` reproduces the two complete four-reading boundary censuses.
