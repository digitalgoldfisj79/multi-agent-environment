# Programme status after the centred source-to-frame identity

Date: 28 July 2026

## Completed

The algebraic source-to-frame gap in corrected Paper II has been resolved.

For the one-sided shifted detector residual

\[
c_j=\Psi_j(H)-\mu_j,
\]

the principal term is subtracted in source space before any harmonic square or
pair lift.  The resulting centred walk is

\[
C_X(\theta)=\sum_jc_je(P_j\theta)
 =\int\mathscr R_X(\alpha)F_X(\theta-\alpha)\,d\alpha.
\]

The exact block variance is its Lebesgue energy:

\[
\sum_j|c_j|^2=\int_0^1|C_X(\theta)|^2\,d\theta.
\]

Using the reciprocal rows of Paper II gives the exact aggregate kernel

\[
\mathcal K_X(L)=2\sum_a\frac{|\Theta_{a,X}(L)|^2}{m_a},
\qquad \mathcal K_X(0)=1,
\]

and the exact centred reciprocal frame

\[
\mathfrak G_X(c)
 =\sum_{j,k}c_j\overline{c_k}\mathcal K_X(P_j-P_k).
\]

Thus

\[
\mathfrak G_X(c)-\sum_j|c_j|^2
 =c^*(\mathbf K_X-I)c.
\]

The shifted detector itself has a direct all-centres variance criterion: proper
prime-power output terms are only `O(X log X)` at a failed centre, while the
baseline is of order `H`.

## Pair-sum consequence

The pair-sum architecture survives only after retaining source coefficients.
The canonically normalised pair coefficient is

\[
d_{jk}=\sqrt{2-\delta_{jk}}\,c_jc_k,
\]

and its diagonal mass is exactly

\[
\sum_{j\le k}|d_{jk}|^2
 =\left(\sum_j|c_j|^2\right)^2.
\]

Replacing these coefficients by one gives the old unweighted frame and erases
the detector.  A coefficient-independent frame cannot be the algebraic
source-to-frame identity.

## Validation

`centred_source_frame_verify.py` checks, for multiple deterministic seeds:

1. recovery of the centred Fourier coefficients from the source;
2. the source convolution identity;
3. Parseval for the detector variance;
4. the direct dual-row energy against the Gram-kernel formula;
5. the literal and normalised pair lifts;
6. the diagonal-mass formulas;
7. baseline subtraction before squaring;
8. the kernel normalisation and range.

All checks pass with maximum numerical discrepancy below `3e-10` in the
reciprocal pair-lift tests and below `3e-12` in the source tests.

## New exact theorem boundary

The corrected source-to-frame theorem is now split into two precise estimates.
For the actual von-Mangoldt residual vector, prove:

1. **lower frame stability**

   \[
   c^*\mathbf K_Xc\ge\kappa\|c\|_2^2
   \]

   for some fixed `kappa>0`; and

2. **centred source-frame upper bound**

   \[
   \mathfrak G_X(c)\ll NHXL(X),
   \qquad L(X)=o(\log X).
   \]

Together these imply the corrected block variance and hence every centre in the
block succeeds.

The stronger but potentially unnecessary source-independent route is

\[
\|\mathbf K_X-I\|_{op}<1.
\]

The residual-restricted lower bound may be substantially weaker and is the
preferred target.

## Priority

1. Measure the Rayleigh quotient
   `c^* K_X c / ||c||^2` on accessible primorial blocks using the corrected
   detector residuals.
2. Determine whether lower-frame stability follows from the reciprocal row
   geometry or requires arithmetic information about the residual signs.
3. Derive the sampled source-energy formula after inserting the explicit
   von-Mangoldt transform and retain the baseline cross term.
4. Use pair-sum collision geometry only for the weighted symmetric-square lift;
   do not return to the unweighted frame or Paper IV derandomisation as the
   principal route.

Fortune's conjecture remains open.  The previous unspecified bridge has been
replaced by exact identities and two named analytic estimates.
