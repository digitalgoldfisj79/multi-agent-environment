# Gate I3 — direct four-prime covariance lane

**Date:** 4 August 2026  
**Ruling:** CLOSED AS AN OVERSTRONG ROUTE WITH AN EXPLICIT SCALE OBSTRUCTION

## 1. Exact expansion

For

\[
a_j(m)=1_{\mathbb P}(m)1_{\mathbb P}(P_j+m),
\qquad
Z_j=\sum_{m\le H}a_j(m),
\]

one has

\[
Z_j^2=Z_j+2\sum_{1\le d<H}C_j(H;d),
\]

where `C_j(H;d)` is the four-prime correlation at offsets `m,m+d`.

This identity is exact.  It is the correct expansion of the **full** second moment.

## 2. Scale ledger

With

\[
N\asymp X/\log X,
\quad H\asymp X^2,
\quad \lambda_j\asymp X,
\]

the main second-moment pieces have scale

\[
\sum_j\lambda_j^2\asymp NX^2.
\]

The registered variance target has scale

\[
NXL(X),\qquad L(X)=o(\log X).
\]

Therefore the required relative cancellation is

\[
\frac{NXL(X)}{NX^2}=\frac{L(X)}X.
\]

Any triangle inequality or raw upper bound taken before the baseline cancellation loses a
factor

\[
\frac X{L(X)}\longrightarrow\infty.
\]

There are `NH` displacement pairs `(j,d)`.  A termwise treatment would require average
signed error

\[
\frac{NXL(X)}{NH}=\frac{L(X)}X
\]

per pair.  This tends to zero much faster than the natural size of an individual
four-form count.  Consequently a uniform asymptotic in every `d` is both stronger than
needed and unavailable; only a genuinely aggregate signed theorem could work.

The exact arithmetic is reproduced by `scripts/i3_scale_audit.py`.

## 3. Effect of the I1 target substitution

Gate I1 replaced full variance by the lower-tail energy

\[
D_X^-=\sum_j(\lambda_j-Z_j)_+^2.
\]

The polynomial expansion of `Z_j^2` controls positive and negative deviations together.
It therefore reintroduces precisely the upper-tail burden removed at I1.  The elementary
majorant

\[
(\lambda_j-Z_j)_+^2\le (Z_j-\lambda_j)^2
\]

is valid, but using it returns to the overstrong `INT-ISC` target.

## 4. Available analytic inputs

- Upper-bound sieves can bound `C_j(H;d)` but do not supply the signed main-term
  cancellation.
- Termwise Hardy–Littlewood asymptotics for the four coupled forms are unproved and would
  be much stronger than the aggregate requirement.
- Green–Tao-type finite-complexity results do not apply in this short-variable,
  exponentially large-constant regime with the needed uniformity.
- Taking absolute values after a Vaughan or Heath–Brown decomposition leaves the raw
  `NX^2` scale and fails by `X/L(X)`.

## 5. Gate ruling

The direct four-prime lane is not promoted.

It is closed for this programme because:

1. it targets the discarded upper tail;
2. every available absolute-value implementation misses the loss budget by `X/L(X)`;
3. the only surviving formulation is an aggregate signed four-prime theorem essentially
   equivalent to the original covariance target.

This is a method obstruction, not a proof that no four-prime theorem can exist.  The lane
may reopen only if a new aggregate identity controls the lower tail directly without first
proving the full second moment.
