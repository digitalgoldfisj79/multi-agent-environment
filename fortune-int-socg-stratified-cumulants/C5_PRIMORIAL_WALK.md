# C5 — primorial-walk orbit identity

The row variable is not an ordinary interval centre. It satisfies

\[
P_{j+1}=\ell_{j+1}P_j.
\]

For moduli supported on primes above the current terminal prime, derive the exact recurrence of `P_j mod q` and Fourier-expand the selected-centre error terms left by C4.

## Required ledger

For every frequency family record:

- modulus/conductor range;
- stratum length `n_b`;
- frequency multiplicity;
- trivial, completion and large-sieve norms;
- required absolute error after summing connected offset patterns.

## Candidate theorem — INT-PWOC

A selected primorial-walk orthogonality estimate strong enough that the orbit contribution has dependence radius

\[
D_{walk}\ll X/(\log X)^{1+\delta}.
\]

## Kill gate

If the best available norm exceeds the one-stratum budget, stop with `REDUCED_TO_SELECTED_PRIMORIAL_WALK_CORRELATION` or a quantified obstruction. Dense-centre equidistribution is not a substitute.