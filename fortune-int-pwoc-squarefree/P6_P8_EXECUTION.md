# P6 and P8 execution — signed structure and arithmetic transfer

**Status:** `SOURCE_WEIGHT_CONTRACT_NOT_AVAILABLE; NO_TRANSFER_TO_RUHL_OR_SOCG`

## P6 signed and dyadic audit

The inherited source documents permit Heath--Brown identities, Vaughan identities, divisor switching and Dirichlet-polynomial decompositions, but they do not commit an exact term whose modulus coefficient can be read as a signed family `gamma(q)` on the selected-centre row variable.

In particular, the repository contains no frozen data for:

- the truncation order and divisor ranges;
- the dyadic conductor blocks;
- the coefficient normalization after Cauchy--Schwarz or completion;
- the recombination that preserves actual-prime detection;
- the map from signed source coefficients to the nonnegative energy weight `beta(q)`;
- the retained row variable after all source variables are summed.

Therefore Möbius signs or dyadic cancellation cannot honestly be tested. Introducing a generic `mu(q)` profile would be another surrogate and would violate P0/P4.

## P8 transfer to RUHL-FM

The proved fixed-order estimate is

\[
\mathcal E_\beta(a)
\le
\left(D_\beta+U_r{n-1\choose r+1}\right)\|a\|_2^2.
\tag{1}
\]

A transfer to the RUHL-FM residual `A_{b,k}` would require an exact source inequality of the form

\[
|A_{b,k}^{(r)}|
\le C_{b,k,r}\,\mathcal E_{\beta_r}(a_{b,k,r})^{1/2}
\tag{2}
\]

with displayed `C_{b,k,r}`, coefficient mass, conductor range and summation over all source blocks. No such inequality is committed. Thus (1) cannot be inserted into the detector margin in equation (A5) of the RUHL-FM arithmetic interface.

## P8 transfer to INT-SOCG

A transfer to the connected-cumulant radius would require a source-to-connected-frame identity producing a contribution

\[
D_{\mathrm{walk},r}
\le F_r(D_\beta,U_r,n,\text{source masses})
\]

inside the exact C6 recombination. The inherited C6/C7 documents identify this need but do not provide the identity or the source masses. The fixed-order energy theorem therefore does not yield the required bound

\[
D_b\ll X/(\log X)^{1+\delta}.
\]

## Decision

PWOC-SF1 is a valid standalone fixed-order composite-modulus theorem. The current repository does not contain the coefficient contract needed to prove PWOC-SF2 or to quantify any contribution to RUHL-FM or INT-SOCG.

This is a missing-interface result, not a claim that every possible source decomposition must fail.