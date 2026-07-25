# Counterexamples to uniform positivity of the nonsquare q=infinity boundary

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Classification:** **EXACT COMPUTER-ASSISTED RESULT**.  
**Scope:** the proposed boundary-only bypass for the function-field `d=1` crown.

## 1. Boundary family

For `p congruent 5 mod 6`, the `q=infinity` boundary is

\[
F_{a,d}(X)=X^p+aX^3+d.
\]

Its irreducible count depends only on

\[
A=\chi(a).
\]

The branch proves uniformly that

\[
I_+(\infty)=0.
\]

At the calibrated primes `p=11,17,23,29`, the nonsquare count was respectively

\[
I_-(\infty)=4,4,2,2.
\]

This suggested a possible bypass: prove `I_-(infinity)>0` uniformly and obtain an irreducible member without the Airy estimate.

## 2. Exact counterexamples

The deterministic verifier gives

\[
\boxed{I_-(\infty)=0\quad\text{at }p=53}
\]

for the least nonsquare `a=2`, and

\[
\boxed{I_-(\infty)=0\quad\text{at }p=71}
\]

for the least nonsquare `a=7`.

Thus no value of `d in F_p` makes

\[
X^p+aX^3+d
\]

irreducible in either case.

The complete diagnostic is:

| `p` | nonsquare `a` | fibres with a linear factor | remaining reducible fibres | irreducible fibres |
|---:|---:|---:|---:|---:|
| 53 | 2 | 35 | 18 | 0 |
| 71 | 7 | 47 | 24 | 0 |

## 3. Exact certification method

For a monic polynomial `f` of prime degree `p` over `F_p`, irreducibility is equivalent to:

1. `gcd(f,X^p-X)=1`; and
2. `X^(p^p)=X mod f`.

The verifier applies these two exact polynomial-arithmetic tests to every `d in F_p`. No floating-point computation, probabilistic factorization or sampling is used.

## 4. Ruling

### Closed

The route

\[
I_-(\infty)>0\quad\text{for every }p\equiv5\pmod6
\]

is false.

Consequently the `q=infinity` boundary alone cannot bypass the q-line/Airy wall.

### Still possible

A boundary-assisted theorem could still combine several cells or use a congruence involving the generic q-line projectors. The counterexamples close only the proposed uniform positivity of the single nonsquare `q=infinity` slice.

## 5. Verification

`q_infinity_nonsquare_counterexample_verify.py` reproduces the two complete boundary censuses.
