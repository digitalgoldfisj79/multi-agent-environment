# Programme status after single-walk stability reduction and calibration

Date: 28 July 2026

## Exact progress

The centred source-to-frame identity has been strengthened from an unspecified
lower-frame condition to one scalar single-walk target.

Let

\[
\mathcal S_X=
 \sum_{j\ne k}\mathcal K_X(P_j-P_k).
\]

Then

\[
\|\mathbf K_X-I\|_{\mathrm{op}}\le\mathcal S_X.
\]

Therefore \(\mathcal S_X<1\) gives a uniform lower frame bound for every
residual vector, not merely the actual von-Mangoldt residual.

The exact decomposition is

\[
\mathcal S_X
 =
 2N(N-1)\sum_a\frac{\kappa_{2,a}}{m_a}
 +
 2\sum_a\frac{\mathcal R^{(1)}_a}{m_a}.
\]

The same-modulus term is unconditionally

\[
O_\rho\!\left(\frac{N^2\log H}{H}\right)
 =O_\rho(1/\log X)=o(1).
\]

The sole lower-frame obstruction is now the distinct-modulus single-walk
dispersion

\[
\sum_a\frac{\mathcal R^{(1)}_a}{m_a}=o(1).
\]

This is not HTE4, the old pair-sum frame, or Paper IV derandomisation.

## Finite integer calibration

The exact kernel matrix and the shifted-detector residual Rayleigh quotient were
computed on thirteen primorial blocks:

\[
X=11,17,23,29,37,43,53,61,73,89,101,113,131.
\]

Parameters:

- \(H=0.8X^2\);
- reciprocal shell primes \(q\in[H,2H)\);
- \(\rho(t)=e^{-\pi t^2}\);
- symmetric harmonics \(|a|\le6\);
- omitted signed Gaussian tail below \(3.9\times10^{-17}\);
- detector \(\Psi_j(H)=\sum_{m\le H}\Lambda(P_j+m)\);
- Hardy--Littlewood baseline used only for the displayed residual Rayleigh
  quotient.

Observed frame spectrum over the complete panel:

- minimum eigenvalue: `0.8566096743`;
- maximum eigenvalue: `1.1829843015`;
- minimum actual-residual Rayleigh quotient: `0.9952869939`;
- maximum actual-residual Rayleigh quotient: `1.1414776104`;
- total off-diagonal mass: `0.3807780101` to `0.7307087177`;
- maximum off-diagonal row sum: `0.0254246465` to `0.1885391292`.

At the largest block \(X=131\):

- \(N=24\);
- reciprocal shell size `1376`;
- largest centre has `101` decimal digits;
- frame spectrum:
  \[
  0.9927869734\le\lambda\le1.0217601907;
  \]
- actual-residual Rayleigh quotient:
  \[
  0.9999630461;
  \]
- maximum off-diagonal row sum:
  \[
  0.0295725759.
  \]

## Interpretation

The calibration is consistent with the heuristic that the reciprocal rows form
an increasingly Parseval-like frame on the primorial-prefix frequencies.
Crucially, the full matrix lower bound is already positive throughout the panel,
so this observation does not depend on the conjectural detector baseline.

The data do **not** prove:

- \(\mathcal S_X=o(1)\);
- a uniform positive lower frame bound;
- the distinct-modulus reciprocal estimate;
- the source-frame upper bound;
- Fortune's conjecture.

## Current priority

1. Attack
   \[
   \sum_a\mathcal R^{(1)}_a/m_a=o(1)
   \]
   using reciprocal-fraction cancellation for the single increasing
   prime-product walk.
2. Derive the centred source-frame upper bound with the baseline cross term
   retained.
3. Use weighted pair-sum geometry only if it contributes to either of those
   estimates.

The old coefficient-free pair frame remains secondary.
