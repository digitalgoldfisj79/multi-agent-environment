# Two-sided signed divisor frame for the corrected Fortune source

Date: 27 July 2026  
Status: exact finite identity proved; truncation and analytic estimation open.

## Source

For a primorial centre `P_j` and `H<ell_{j+1}^2`, define

\[
T_j(H)=\sum_{2\le m\le H}\Lambda(m)\Lambda(P_j+m).
\]

This is the analytically natural corrected source because it retains both prime variables. At a failed centre it is `O(X(log X)^2)`, while its conjectural main term is `S(P_j)H asymp H log X`.

## Exact divisor expansion

Use the exact identity

\[
\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d.
\]

For positive integers `d,e`, put

\[
C_j(d,e;H)=\#\{2\le m\le H:d\mid m,\ e\mid P_j+m\}.
\]

Then all sums below are finite and

\[
\boxed{
T_j(H)=
\sum_{d\le H}\sum_{e\le P_j+H}
\mu(d)\mu(e)\log d\log e\,C_j(d,e;H).
}
\tag{1}
\]

This is the first exact two-sided signed frame. Neither divisor system may be replaced by a positive density before the principal term is removed.

## CRT geometry

Let `g=(d,e)` and `l=[d,e]`. The simultaneous congruences

\[
m\equiv0\pmod d,
\qquad
m\equiv-P_j\pmod e
\]

are soluble if and only if

\[
g\mid P_j.
\]

When soluble, they define one residue class modulo `l`. Therefore

\[
C_j(d,e;H)
=\mathbf1_{(d,e)\mid P_j}
\left(\frac{H-1}{[d,e]}+\Delta_j(d,e;H)\right),
\]

where `|Delta_j(d,e;H)|<=1` after the exact endpoint convention is absorbed into `Delta`.

Consequently

\[
T_j(H)=M_j(H)+R_j(H),
\]

with

\[
M_j(H)=(H-1)
\sum_{d,e}
\frac{\mu(d)\mu(e)\log d\log e}{[d,e]}
\mathbf1_{(d,e)\mid P_j},
\tag{2}
\]

and

\[
R_j(H)=
\sum_{d,e}
\mu(d)\mu(e)\log d\log e\,
\mathbf1_{(d,e)\mid P_j}\Delta_j(d,e;H).
\tag{3}
\]

Equations (1)--(3) are exact finite identities. The notation `M_j` does not assert that the unrestricted finite sum in (2) is already the Hardy--Littlewood main term: cancellation and truncation are load-bearing.

## What this resolves

The missing source-to-frame object now exists. The exact corrected source is a two-dimensional signed divisor lattice with:

- a CRT solvability projector `(d,e)|P_j`;
- a local scale `[d,e]`;
- a signed endpoint discrepancy `Delta_j`;
- both von Mangoldt divisor systems retained.

This is not the old one-sided reciprocal pair-sum frame. The latter can become relevant only after a proved transformation or domination of (3).

## New obstruction

The full sums range over `d<=H` and `e<=P_j+H`. Taking absolute values in (3) is catastrophic. The main and discrepancy sums are not separately useful without a signed truncation theorem. Thus the next boulder is now precise:

> Construct a two-sided Heath--Brown/Vaughan truncation for (1), subtract the primorial singular-series main term, and prove that the discarded tails are below the all-centres variance scale.

The existing growing-degree Mobius theorem controls a prime indicator on a critical shell. It does not by itself control the output-side divisor range in (1).

## Verified finite cases

An independent script recomputed `T_j` in three ways:

1. directly from von Mangoldt weights;
2. by the double divisor identity;
3. by the swapped CRT frame and the principal-plus-discrepancy split.

All checks passed for primorial endpoints `p=5,7,11,13,17,19` at `H=40`, with maximum floating residual below `9e-13`.

## Programme status

Phase C has advanced from “missing identity” to “exact identity, missing signed truncation.” This is genuine narrowing. The next work should target the truncation and tail ledger, not HTE4 or random-order derandomisation.
