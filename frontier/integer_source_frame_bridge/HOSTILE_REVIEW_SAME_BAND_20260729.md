# Hostile review: rough-quotient and same-band package

Date: 29 July 2026

## Verdict

The new reductions are substantive and exact after correction, but they do not prove the same-band estimate. The correct endpoint is a theorem-level cross-modulus dispersion obstruction, not a completed first-order theorem.

## Defects found and corrected

1. **General frozen cutoff.** The original rough-quotient paper used the largest prime factor `z` simultaneously as the physical lower cutoff. On a frozen block the correct lower cutoff is `Z=z_B\ge z_j`. All quotient, floor, sawtooth and centring identities were generalized and reverified.
2. **Dyadic partition.** The earlier notation `R_\ell=2^\ell R_0` did not specify `R_0` and could omit the first physical band. The corrected partition starts at `Z` and uses exact half-open bands.
3. **Malformed formulae.** The orbit operator bound and reciprocal phase factorization contained broken LaTeX. Their intended formulae were correct and are now explicit.
4. **Global reinsertion inequality.** The passage from frozen to physical rows now explicitly uses `|u+v|^2\le2|u|^2+2|v|^2`.

## Claims retained

**PROVED EXACTLY**

- coprimality transport;
- quotient bijection;
- Möbius-floor and sawtooth identities;
- reciprocal phase separation;
- mesoscopic freezing and orbit frame;
- exact same-band recombination;
- exact covariance identity isolating the missing cross-modulus term.

**COMPUTATIONALLY VERIFIED**

- all exact identities on finite panels with `Z>z`;
- exact dyadic coverage and outer Cauchy;
- small finite same-band ratios, with no extrapolation to a theorem.

**OPEN**

- uniform same-band Bessel/dispersion;
- physical first-order Fortune-scale variance;
- complete covariance with the rough coordinate and Buchstab tail;
- Fortune's conjecture.

## Strategic criticism

The programme's instruction to control the physical first-order component before reinsertion is a valid sufficient strategy but may be unnecessarily strong. The exact detector explicitly permits cancellation between chaos levels. If the same-band theorem resists a new signed divisor or rough-interval theorem, the correct response is to reinsert the other coordinates earlier rather than to pretend that standard Cotlar, large-sieve or positive-sieve machinery has solved the cross-modulus covariance.
