# O7 — rowwise parity-breaking execution

**Status:** CLOSED AS A DIRECT METHOD; NEW BILINEAR INPUT IS EXPLICIT

## Exact divisor identity

For every positive integer `n`,

\[
\Lambda(n)=\sum_{d\mid n}\mu(d)\log(n/d).
\]

Therefore

\[
S_j(H)
=
\sum_{d\le P_j+H}\mu(d)
\sum_{\substack{m\le H\\m\equiv-P_j\pmod d}}
\Lambda(m)\log\frac{P_j+m}{d}.
\]

This is the exact Type-I/source identity. It has three qualitatively different ranges.

## Range I: `d<=sqrt(H)`

The inner sum is a prime-weighted progression sum of length `H` and modulus `d`. Classical average distribution can address parts of this range. It does not break parity by itself and does not reach the least output factors relevant after candidate collapse.

## Range II: `sqrt(H)<d<=H`

There are at most `H/d+1=O(sqrt(H))` offsets per modulus, declining to `O(1)`. The first admissible least output factor already satisfies

\[
r>\ell_j>\sqrt H.
\]

Thus every genuinely relevant output factor begins beyond the classical positive lower-sieve and square-root progression boundary.

## Range III: `d>H`

For fixed `d`, the congruence contains at most one offset in the full window. No progression averaging remains. Writing

\[
P_j+m=de
\]

produces a sparse hyperbola with the primality of `m=de-P_j` still present. Absolute divisor switching loses the sign needed to distinguish a prime output from a semiprime or higher almost prime.

## Smallest sufficient bilinear theorem

The independent rowwise route reduces to:

> **INT-RPBH — rowwise primorial bilinear-hyperbola bound.** In the exact divisor decomposition above, after the classical `d<=sqrt(H)` main and error terms are removed, the signed aggregate of the ranges `d>sqrt(H)`, including the switched hyperbola and proper-prime-power remainder, has an error strictly smaller than the positive prime-pair main term for every registered row.

Together with the explicit prime-power cap, `INT-RPBH` gives `S_j(H)>0` from an actual prime-prime pair for every row, hence `INT-AOD`.

## Obstruction ruling

No established theorem found in the audit supplies `INT-RPBH`:

- Bombieri--Vinogradov-type input stops before the post-level factor range;
- direct asymptotic-sieve use assumes a parity-breaking bilinear estimate of this type;
- weighted switching requires distribution in both coordinates and normally concludes prime/almost-prime;
- Cauchy--Schwarz or unsigned band estimates lose the one-row sign.

This lane is therefore closed as a direct application at the explicit boundary `d=sqrt(H)`. `INT-RPBH` is a valid sufficient theorem but is stronger and less aggregate than the stratified connected target `INT-SCG`; it is not selected as the primary successor.
