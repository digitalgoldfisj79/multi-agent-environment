# M2 — local density and direct asymptotic-sieve audit

**Status:** `DIRECT_FI_ROUTE_CLOSED_AT_SCALE`

For a row set `C`, define the nonnegative output sequence

\[
a_C(n)=\frac1{|C|}\sum_{j\in C}\sum_{m\in M}
\log m\,1_{n=P_j+m}.
\]

Then

\[
T_C=\sum_n a_C(n)\Lambda(n),
\qquad
A_C=\sum_n a_C(n)=\sum_{m\in M}\log m\sim H.
\]

For squarefree `d`,

\[
A_C(d)=\sum_{d\mid n}a_C(n)
=\frac1{|C|}\sum_{j\in C}
\sum_{\substack{m\in M\\m\equiv-P_j\pmod d}}\log m.
\]

For primes below every terminal prime, the divisor sum is exactly zero. For primes above the parent-stratum upper terminal prime, the local density is `1/(p-1)`. The resulting formal Euler factor is the primorial small-prime enhancement multiplied by the usual two-linear-form factors above the terminal boundary; it has order `log X`.

## Direct Friedlander–Iwaniec eligibility

The published asymptotic sieve is indexed at the size of the integers whose primality is detected. Here that size is

\[
x\asymp P_j=\exp((1+o(1))X),
\]

while the sequence mass is only `A_C asymp H asymp X^2`.

Its remainder hypothesis requires a distribution level `D>x^(2/3)`, and its parity-breaking bilinear range lies around factors of size `sqrt x`. Prime-progression information in the offset variable has natural length `H` and classical mean-square level at most polynomial in `X`.

Thus

\[
D_{available}=X^{O(1)}
\quad\text{versus}\quad
D_{required}=\exp((2/3+o(1))X).
\]

The direct theorem is therefore ineligible by an exponential scale gap. Reindexing by the offset `m` is invalid because the von Mangoldt factor is `Lambda(P_j+m)`, not `Lambda(m)`.

This closes only the literal direct application. A translated parity-breaking theorem tailored to the selected primorial path remains admissible.