# Literature audit

## Friedlander–Iwaniec — Asymptotic sieve for primes

The theorem detects primes in a nonnegative sequence under classical divisor-sum information plus a Möbius-weighted bilinear axiom. In its published form the sequence parameter `x` is the magnitude of the integers whose primality is detected, the remainder level satisfies `D>x^(2/3)`, and the bilinear range is tied to `sqrt(x)`.

**Use here:** exact eligibility audit and identification of the parity-breaking bilinear anatomy.

**Failure here:** `x asymp P_j=exp((1+o(1))X)`, while ordinary offset distribution is polynomial in `X`.

## Barban–Davenport–Halberstam and Montgomery–Hooley variance

The standard unconditional `HQ log H` variance scale is obtained when the modulus cutoff is close to `H`, for example `Q>=H/(log H)^A`. More precise formulae for all `Q<=H` retain a term of size `H^2/(log H)^A`, which dominates the desired `HQ` scale when `Q=H^(2/3)`.

The general unconditional large-sieve estimate is

\[
V(H,Q)\ll (H+Q^2)H(\log H)^C.
\]

At `Q=X^(1+delta)>H^(1/2)`, its `Q^2H` term gives the explicit M4 obstruction.

Under GRH, variance asymptotics are available in ranges extending to `Q>=H^(1/2+epsilon)`. This provides a conditional benchmark for `INT-SCVAR`, not an unconditional input.

## Bombieri–Vinogradov

The first-moment modulus average reaches only the square-root scale of the offset length, up to logarithmic losses. Since outputs are already pre-sieved through primes of size `X=H^(1/2)` and the clean uniform band begins above `2X`, this supplies no post-terminal interval.

## Friedlander–Iwaniec weighted switching and descendants

These methods can break parity when a sequence-specific bilinear or switched-coordinate theorem is available.

**Not supplied:** a theorem uniform over deterministic primorial microblocks with output factors at exponential scale or the signed `INT-SCPT` tail.

## Correction record

The first execution draft incorrectly applied the `HQ log H` BDH variance at `Q=H^(2/3)`. The literature range check rejected that step. All unconditional M5 language was removed, a large-sieve obstruction verifier was added, and the clean-room evidence must postdate this correction.

## Governing bridge test

An external theorem is admitted only if:

1. its modulus range contains the actual `Q`;
2. its row averaging is over the deterministic primorial path or all residue classes with multiplicities retained;
3. its offset window includes `H=X^2/2`;
4. its error is uniform for every registered microblock;
5. its final conclusion controls the signed parity tail, not merely divisor incidence or almost primes.