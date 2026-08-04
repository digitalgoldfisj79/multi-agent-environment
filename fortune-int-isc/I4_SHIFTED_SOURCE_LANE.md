# Gate I4 — shifted von Mangoldt / short-interval source lane

**Date:** 4 August 2026  
**Ruling:** REDUCED TO A STRICTLY SMALLER NEW THEOREM; EXISTING METHODS FAIL AT AN EXPLICIT SCALE

## 1. Exact one-form source

Define

\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m).
\]

Candidate collapse gives

\[
\Psi_j(H)=Y_j(H)+R_j(H),
\]

where `Y_j` is the prime-output contribution and the proper-prime-power remainder satisfies

\[
R_j(H)=O(X\log X)
\]

uniformly in the block.  If the interval contains no prime, then

\[
\Psi_j(H)=R_j(H)=O(X\log X).
\]

Thus the direct arithmetic problem is a one-form lower-tail problem for primes in
`(P_j,P_j+H]`.  The binary prime-pair description is exact, but a four-prime second moment
is not logically required.

## 2. A strictly smaller sufficient theorem

Set

\[
B_X=X(\log X)^2
\]

and define

\[
\mathcal D_{\Psi}^-(X)=
\sum_{j<N}\bigl(B_X-\Psi_j(H)\bigr)_+^2.
\]

Freeze the theorem:

> **INT-PSLT — primorial selected lower-tail theorem.**
> \[
> \boxed{\mathcal D_{\Psi}^-(X)=o(B_X^2).}
> \]

At a failed centre,

\[
B_X-\Psi_j(H)
=B_X\left(1+O\left(\frac1{\log X}\right)\right),
\]

so one failure contributes `(1+o(1))B_X^2`.  `INT-PSLT` therefore excludes every
failure.

This theorem is substantially weaker than a prime-number-theorem asymptotic:

\[
\frac{B_X}{H}=\frac{(\log X)^2}{X}\longrightarrow0.
\]

It asks only for weighted prime mass well above the proper-prime-power ceiling, not for
the conjectural mass of order `H`.

It is also strictly weaker than `INT-LTQ`.  `INT-LTQ` forces every `Z_j` to be of order
`X`, hence `\Psi_j\gg X^2`, whereas `INT-PSLT` permits `\Psi_j` to be only of order
`X(log X)^2`.

## 3. Registered scales

Writing `x=P_j`,

\[
\log x\asymp X,
\qquad
H\asymp X^2\asymp(\log x)^2,
\qquad
B_X\asymp \log x\,(\log\log x)^2.
\]

The source theorem is therefore at logarithmic-square interval length and a mesoscopic
lower threshold far below the expected total mass.

The scale relations are checked in `scripts/i4_source_scale_audit.py`.

## 4. Generic short-interval technology

The registered interval is exponentially shorter than the ranges of available all-centre
theorems.

- Guth–Maynard prove a prime-number-theorem asymptotic in every interval of length
  `x^(17/30+o(1))`.
- Runbo Li's current preprint gives existence in every interval of length `x^0.52`.
- Almost-all results do not restrict their exceptional sets to the increasing primorial
  centres.
- Under RH, the classical explicit-formula error remains on square-root scale.

Every fixed power of `x` is exponential in `X`; the required length is polynomial in `X`.

## 5. Short-variable / large-value sieve mismatch

The variable `m` ranges only over `H=X^2`, while the linear form `P_j+m` has size
`exp(Theta(X))`.

For prime offsets `m>X`, every prime `q\le X` already fails to divide `P_j+m`, because
`q|P_j` and `q\nmid m`.  Bombieri–Vinogradov distribution for primes `m\le H` reaches
moduli only up to approximately

\[
H^{1/2}=X,
\]

exactly where the automatic primorial exclusion ends.  It therefore supplies no new
sieving range for the output form.

More recent weighted distribution exponents can enter a polynomial range beyond `X`, but
primality of an integer of size `P_j` depends on possible factors up to

\[
P_j^{1/2}=\exp(\Theta(X)),
\]

and the lower-bound parity obstruction remains.  Such results currently yield refined
upper bounds for prime pairs, not the required lower tail.

This is the central scale mismatch: varying `m` provides only polynomially sized modulus
information, while the output has exponentially large factor range.

## 6. Explicit-formula route

For a generic centre `x`, an explicit formula gives a zero sum with natural square-root
barrier.  On RH the classical pointwise error is vastly larger than both `H` and `B_X` at
the registered scale.

Averaging over `j` would require a new zero-correlation theorem for phases

\[
P_j^{i\gamma}.
\]

No existing zero-density, pair-correlation or large-values theorem is uniform on this
prescribed lacunary path.  Moreover, the ordinary main term `H` cannot simply be used:
Maier-type logarithmic-interval effects and the primorial local sieve produce an order-`H`
local bias.  The Buchstab/Maier principal term must be isolated before any residual zero
estimate.

## 7. Exact missing analytic input

A successful shifted-source proof must establish one of:

1. `INT-PSLT` directly;
2. a primorial-specific lower-bound sieve that breaks the short-variable/large-value
   mismatch;
3. a source decomposition into the correct local principal term plus a residual whose
   lower-tail energy is `o(B_X^2)`;
4. a zero-correlation theorem on the primorial logarithmic walk strong enough to imply the
   same bound.

None is currently established.

## 8. Gate ruling

I4 achieves the allowed outcome `REDUCED_TO_SMALLER_NEW_THEOREM`:

- the four-prime covariance is replaced by the strictly smaller one-form theorem
  `INT-PSLT`;
- the implication to Fortune is exact;
- existing all-centre, almost-all, sieve and explicit-formula methods are obstructed at
  quantified scales;
- the remaining theorem is new rather than an equivalent reciprocal or quotient
  reformulation.

The programme continues through I5 and I6 to determine whether geometry of the primorial
walk or an adversarial model further reduces or kills the available approaches.
