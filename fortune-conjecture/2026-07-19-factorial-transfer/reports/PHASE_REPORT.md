# Fortune factorial-transfer and reframing phase — final report

## Verdict

This phase produced one exact theorem and closed two proposed proof routes.

### New exact theorem

The Lebesgue fourth moment is now known in closed form:
\[
\int_0^1|H_2(\theta)|^4d\theta
=\frac{N(3N^3-2N^2+2N-1)}2,
\]
and
\[
\int_0^1(|H_2(\theta)|^2-M)^2d\theta
=\frac{N(N-1)(5N^2-N+2)}4.
\]
Thus the centred kernel has exactly the correct \(L^2\) size; PGD2 is a transfer problem from Lebesgue measure to the weighted reciprocal prime-pair sampling measure.

### D2

The one-operator spectral identity is exact and useful for external communication. Current random-matrix local laws do not apply to this deterministic walk-generated matrix without proving concentration/cumulant stability assumptions that contain the unresolved arithmetic cancellation. D2 is retained as a specialist brief, not an active internal route.

### D3

The factorial literature does not transfer directly. Every load-bearing proof inspected uses bounded-degree polynomials formed from consecutive-integer shifts. The prime-prefix quotient has no analogous bounded-degree index polynomial. Moreover, the principal individual GLS bound is asymptotically worse than trivial at \(N\asymp q^{1/2}/\log q\). Direct transfer is stopped.

### D4

The almost-all-n objective remains worthwhile, but the proposed three-shell null experiment lacks an exact exceptional-set implication and was stopped before compute.

## Active frontier after this phase

A useful next theorem must exploit the weighted reciprocal sampling measure itself. D1 identifies the precise form:
\[
\sum_{q\ne r}p_{q,a}p_{r,a}
\left(|H_2(a(1/q-1/r))|^2-M\right)^2
\ll M^2X^{o(1)}.
\]
This would imply PGD2 by weighted Cauchy–Schwarz, assuming the established bounded total row mass. Unlike prior fourth-moment routes, this is a positive sampling-transfer statement with the Lebesgue benchmark solved exactly.

The phase does not prove PGD2 or Fortune's conjecture.
