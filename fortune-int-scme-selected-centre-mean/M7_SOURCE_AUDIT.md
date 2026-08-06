# M7 — source and switching audit

**Status:** `STANDARD_DIRECT_METHODS_CLOSED_AT_REGISTERED_SCALE`

The target is the signed tail `INT-SCPT`, not the already proved divisor-band mass.

## Möbius-log expansion

The exact identity

\[
\Lambda(P_j+m)=-\sum_{d\mid P_j+m}\mu(d)\log d
\]

extends to divisors of size `P_j`. For `d<=H`, the congruence selects prime offsets in one residue class. For `d>H`, each row contains at most one offset in that residue class. Absolute divisor-sum estimates therefore lose rowwise progression averaging immediately beyond `H`.

The selected BDH argument improves a signed prime-modulus band only to `X^(4/3-epsilon)`. Its exponent conditions prove that the same Cauchy/BDH/collision mechanism cannot reach `delta>=1/3`.

## Vaughan and Heath–Brown identities

Applied to the output variable, every exact source identity factorizes integers of size

\[
P_j=\exp((1+o(1))X).
\]

The resulting Type II variables include factors near `sqrt(P_j)`, exponentially larger than the offset length and the number of selected rows. Ordinary prime-progression or large-sieve input in the offset variable cannot control these ranges.

## Asymptotic sieve

The literal Friedlander–Iwaniec hypotheses require distribution past `P_j^(2/3)` and a bilinear estimate around exponential factor scales. The available selected-residue theorem is polynomial in `X`, so the direct theorem remains ineligible.

## Switching

Switching a detected band prime `q` introduces the cofactor

\[
r=(P_j+m)/q\asymp P_j/q.
\]

The switched interval has length `H/q`, but its centre and cofactor size remain exponential. Standard weighted switching can detect or bound almost-prime configurations; it does not provide the signed prime-versus-composite tail required by `INT-SCPT`.

## Ruling

No standard source or switching theorem found in the audit proves `INT-SCPT`. The viable successor must exploit signed cancellation on the selected primorial path at large divisor/cofactor scales, or derive a new positive identity that bypasses this tail.