# C1 execution — deterministic stratum geometry

**Status:** `PASSED_EXACT`

Fix

\[
\sigma=\tfrac12,
\qquad
W_X=\left\lfloor\frac{X}{(\log X)^{3/2}}\right\rfloor.
\]

Partition `[X,2X)` into deterministic half-open terminal-prime cells of width `W_X`, merging only the final short remainder into its predecessor. The construction uses terminal-prime locations but never output primality, row occupancy or fitted temperatures.

For a stratum `B_b`, let `U_b` be its upper terminal-prime endpoint and use the common restricted candidate universe

\[
\mathcal M_b=\{m:U_b<m\le H,\ m\text{ prime}\}.
\]

A proof on this restricted universe is stronger than the original rowwise statement. At most `W_X=o(X)` integer offsets are discarded from any row, so the restriction also preserves any lower count with a fixed linear margin.

The number of strata is

\[
B\asymp(\log X)^{3/2},
\]

and the prime number theorem in intervals of this polylogarithmic relative width gives

\[
n_b\asymp\frac{X}{(\log X)^{5/2}}.
\]

Primes crossing the terminal boundary inside one stratum have total reciprocal mass

\[
\sum_{L_b<p\le U_b}\frac1p
\ll \frac{W_X}{X\log X}
\ll(\log X)^{-5/2},
\]

so the row-dependent small-prime transition is subcritical.

Lower scales `L_b=c_0X` and temperatures

\[
\tau_b=(1+3\varepsilon)\frac{\log(n_bB)}{L_b}
\]

are admissible only after a fixed constant `c_0>0` is supplied by C2. They are not inferred from observed occupancies.
