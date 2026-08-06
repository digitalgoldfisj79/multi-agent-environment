# Correction record — selected-residue variance range

## Retracted draft claim

The first execution draft asserted that classical Barban–Davenport–Halberstam supplied

\[
V(H,Q)\ll HQ\log H
\]

at `Q=H^(2/3)`, and consequently promoted an unconditional post-terminal divisor-band asymptotic.

That range attribution was incorrect.

## Range correction

The standard unconditional `HQ log H` scale is available when the modulus cutoff is close to `H`, while formulae valid for all `Q<=H` retain an error of size `H^2/(log H)^A`. At `Q=H^(2/3)`, this error is larger than `HQ`.

The unconditional large-sieve estimate

\[
V(H,Q)\ll(H+Q^2)H(\log H)^C
\]

has a `Q^2H` term for every post-terminal `Q>H^(1/2)`. After selected-residue Cauchy, even a collision-free row set has error/main exponent

\[
\frac12+\frac{3\delta}{2}-\frac\rho2.
\]

Since `rho<=1`, this remains positive for every `delta>0`.

## Remediation

- all unconditional M5 wording was removed;
- `INT-SCVAR` was introduced as an explicit additional theorem;
- `verify_large_sieve_obstruction.py` was added;
- the programme sentinel rejects the obsolete promotion text;
- the initial execution job `6a72eaf2a00abefd4b293438` is excluded from closeout evidence;
- all accepted validation jobs postdate the correction.

## Retained result

The primorial collision-energy theorem and the conditional exponent calculation remain valid. Under `INT-SCVAR`, the selected-residue band works exactly for

\[
2\delta<\rho<1-\delta,
\]

with conditional optimum `rho=2/3`, `delta<1/3`.

No unconditional post-terminal variance or divisor-band theorem is claimed.