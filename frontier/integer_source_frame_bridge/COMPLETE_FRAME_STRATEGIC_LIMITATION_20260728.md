# Strategic limitation of the complete-modulus frame

Date: 28 July 2026  
Status: exact interpretation; prevents overstatement of the lower-frame theorem.

## 1. What the theorem closes

The complete prime-modulus frame proves unconditionally that

\[
\mathfrak D_X(c)=(1+O(1/\log X))\|c\|_2^2
\]

for every residual vector.  It therefore removes any logical concern that the
centred residuals could disappear under harmonic sampling.

## 2. What it does not simplify

The frame uses every additive character `a mod q`.  Complete orthogonality then
reconstructs the coefficient norm, apart from the rare congruences
`P_j=P_k (mod q)`.  Consequently, an upper bound

\[
\mathfrak D_X(c)\ll NHX L(X)
\]

is essentially equivalent to the original variance bound

\[
\|c\|_2^2\ll NHX L(X).
\]

The complete frame supplies stability but no automatic analytic saving.  It is
a rigorous bridge and a useful normalisation, not a substitute for the prime
correlation theorem.

## 3. Why the low-frequency frame remains relevant

The reciprocal-difference frame samples frequencies of size approximately
`1/H`, which interact naturally with a physical interval of length `H`.
Its upper energy may therefore admit Poisson, dispersion, or Type I/II analysis
that the complete grid does not expose.

The trade-off is:

- complete grid: unconditional lower frame, upper bound tautologically hard;
- low-frequency reciprocal grid: potentially tractable upper bound, lower-frame
  dispersion still nontrivial;
- double-von-Mangoldt covariance: explicit principal series, genuine signed
  four-prime error remains.

## 4. Correct programme use

The complete frame should be used for two purposes:

1. as an exact benchmark against which any reduced frequency frame is measured;
2. as a proof that coefficient preservation, rather than abstract frame
   existence, is no longer the issue.

It should not be presented as reducing the prime-correlation difficulty.

The critical path remains:

1. derive a signed Heath--Brown/dispersion reduction of the centred source;
2. place the resulting Type II forms within current Kloosterman-fraction bounds;
3. or prove low-frequency reciprocal-frame stability and its source upper bound
   simultaneously.

The positive-diagonal obstruction shows that taking absolute values before this
signed reduction loses `X/log X`.