# Gate I2 — sparse first-moment diagnostic audit

**Date:** 4 August 2026  
**Status:** CLOSED AS NON-MANDATORY; CURRENT METHODS DO NOT REACH THE SELECTED-CENTRE SCALE

## 1. Why I2 ceased to be a prerequisite

The full variance target implies, by Cauchy–Schwarz,

\[
\left|\sum_{j<N}(Z_j-\lambda_j)\right|
\le \sqrt N\,V_X^{1/2}
\ll N\sqrt{XL(X)}.
\]

After Gate I1, the primary target is the one-sided lower-tail energy

\[
D_X^-=\sum_j(\lambda_j-Z_j)_+^2.
\]

`D_X^-` places no restriction on positive surpluses.  The exact witnesses in
`scripts/i1_strictness_check.py` have zero lower-tail energy but arbitrarily large signed
first-moment error.  Therefore a sparse signed first moment is not logically necessary for
the corrected one-failure proof.

## 2. Direct shifted-prime source

Candidate collapse gives

\[
Z_j(H)>0
\quad\Longleftrightarrow\quad
(P_j,P_j+H]\text{ contains a prime},
\]

with

\[
\log P_j\asymp X,
\qquad
H\asymp X^2\asymp(\log P_j)^2.
\]

Thus the direct source is the Chebyshev sum

\[
\Theta_j(H)=\sum_{P_j<n\le P_j+H}\theta(n).
\]

The selected-centre problem lies at logarithmic-square length, not at a power of the
centre.

## 3. Comparison with known generic short-interval results

The strongest available generic theorems remain separated from the registered scale by an
exponential gap in `X`.

- Guth–Maynard, *Annals of Mathematics* 203 (2026), obtain a prime-number-theorem
  asymptotic for all intervals of length `x^(17/30+o(1))`.
- Runbo Li's current preprint obtains existence for all large `x` in intervals of length
  `x^0.52`.
- Almost-all interval results can reach substantially smaller powers, but their exceptional
  sets are not restriction theorems for the increasing primorial centres.
- Even the Riemann hypothesis gives intervals on approximately square-root scale, still
  exponentially longer than `(log x)^2`.

Putting `x=P_j=exp(Theta(X))`, every power `x^delta` is exponential in `X`, while the
required length is only polynomial in `X`.

## 4. Why almost-all results do not transfer

A dyadic primorial block contains

\[
N\asymp X/\log X\asymp \log x/\log\log x
\]

centres inside an ambient interval of exponential size.  An exceptional set of density
zero, or even of power-saving size, may contain all of these centres.  No available theorem
establishes that the increasing primorial path avoids the exceptional set.

This is not a technicality.  The centres are maximally structured:

\[
P_j\equiv0\pmod q
\]

for every small `X`-smooth modulus `q`.  They cannot be modelled as generic points without
a separate restriction theorem.

## 5. Logarithmic intervals and local bias

Maier's matrix method shows that prime counts in intervals of logarithmic-power length can
deviate from the naive short-interval prime-number-theorem prediction.  The construction
itself uses primorial-type moduli.  Consequently, an ordinary baseline `H` cannot simply be
inserted as a proved main term at these centres; the local primorial calibration must be
retained.

This does not prove that the Fortune intervals are empty or irregular.  It proves that a
uniform logarithmic-interval asymptotic cannot be imported from the global prime number
theorem.

## 6. Exact diagnostic conclusion

No established theorem found in the audit supplies

\[
\sum_{j<N}\Theta_j(H)
\]

with an error strong enough to control the registered centres at `H=(log P_j)^2`, and no
known exceptional-set theorem restricts to the primorial path.

The smallest missing first-moment statement would be a **primorial selected-centre
short-interval theorem**, not a denser Bombieri–Vinogradov or almost-all interval theorem.
It would itself be major new input.

## 7. Gate ruling

- I2 is not required after the I1 target substitution.
- As a diagnostic lane, I2 is closed: existing generic short-interval and almost-all
  technology does not reach the required selected-centre scale.
- Full covariance lanes may proceed only if they exploit the primorial path or bypass a
  generic short-interval theorem.
