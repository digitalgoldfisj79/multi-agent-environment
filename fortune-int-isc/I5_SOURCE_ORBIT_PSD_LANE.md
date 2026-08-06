# Gate I5 — deterministic source/orbit and PSD lane

**Date:** 4 August 2026  
**Ruling:** CLOSED AT A MAXIMAL-COHERENCE OBSTRUCTION

## 1. Exact primorial coherence

Let

\[
F_X(\alpha)=\sum_{j<N}e(P_j\alpha),
\qquad P_j=A_XQ_j,
\qquad A_X=\prod_{p<X}p.
\]

For every divisor `q|A_X` and every integer `a`,

\[
P_j\equiv0\pmod q
\]

for all `j`.  Hence

\[
\boxed{F_X(a/q)=N.}
\]

The increasing primorial centres are therefore maximally coherent at every rational phase
whose denominator divides the frozen primorial base.  This is an exact theorem, not a
finite-data pattern.

The finite regression in `scripts/i5_coherence_audit.py` checks the identity and the
associated frame lower bound on representative blocks.

## 2. Consequence for frame and large-sieve routes

In the finite Fourier space modulo such a `q`, all sampling points `P_j mod q` coincide at
zero.  For any frame inequality sampling these points, the rank-one coherent mode forces
an operator constant at least `N`.  There is no square-root cancellation across `j` on
these modes.

This explains why generic large-sieve averaging over the centre index cannot manufacture
the missing theorem.  The small-modulus modes are precisely the modes that encode the
primorial local bias.

## 3. Centring requirement

Removing the constant mode `alpha=0` is insufficient.  There are exponentially many
squarefree denominators dividing `A_X`, and each produces the same coherent value `N`.
A valid source-to-operator theorem must:

1. identify the full Buchstab/Maier principal contribution carried by these modes;
2. subtract it before applying any norm inequality;
3. retain the one-sided lower-tail information after subtraction.

A reparametrization, CRT factorization or orbit average that leaves the coherent source
unchanged does not create new cancellation.

## 4. Positive-semidefinite formulations

The full variance already has a Gram representation and is positive semidefinite.  That
fact does not solve the problem:

- its norm contains both upper and lower deviations;
- the coherent rational modes contribute on the raw main scale;
- projecting them out requires arithmetic knowledge of the correct principal term;
- the nonlinear lower-tail functional is not recovered from an operator norm without
  returning to the overstrong full variance.

No strictly smaller PSD theorem was found that implies `INT-PSLT` while avoiding this
principal-mode calculation.

## 5. Gate ruling

The deterministic geometry of the primorial walk supplies **coherence**, not
orthogonality.  I5 is closed for the existing frame/operator family.

The exact obstruction is:

\[
q\mid A_X\quad\Longrightarrow\quad |F_X(a/q)|=N.
\]

Any future source/orbit route must combine the centre geometry with genuinely new
arithmetic cancellation in the source coefficients after a complete local main-term
subtraction.  Geometry alone cannot meet the lower-tail target.
