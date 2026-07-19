# Character-ratio collapse and CRT de-tensorisation no-go theorem

## Local identity

Let `q` be prime, let `a,x,y` be units modulo `q`, and let `rho` be a multiplicative character. For each character `chi`, set

\[
\psi=\chi\overline\rho.
\]

Then

\[
\frac1{(q-1)^2}
\sum_{\chi\bmod q}
\tau_q(\overline\chi)
\overline{\tau_q(\overline\psi)}
\chi(ax)\overline{\psi(ay)}
=
\begin{cases}
\mathbf 1_{\rho=1},&x=y,\\[4pt]
\displaystyle
\frac{\tau_q(\overline\rho)}{q-1}
\rho(a(x-y)),&x\ne y.
\end{cases}
\]

Summing over `rho` gives exactly

\[
e_q(a(x-y)).
\]

## Composite consequence

For `m=q_1q_2q_3q_4`, applying this identity at each CRT factor to the unequal-character sector reconstructs

\[
\prod_{s=1}^4e_{q_s}(\epsilon_s(P_i-P_j))
=e_m(A(P_i-P_j)).
\]

Thus CRT de-tensorisation of the cross-character sector reconstructs the original additive kernel exactly. It does not produce four independent modulus averages.

Four-shell divisibility controls only the zero branches and the character diagonal. An estimate such as

\[
\sum_{i<j}\binom{\nu_Q(R_{i,j}-1)}4\ll N^2X^{o(1)}
\]

may be true, but cannot imply PGD2 through this transform.

## Decision

The chain

\[
\text{Gauss/CRT}
\to\text{character orthogonality}
\to\text{four shell divisors}
\to\text{PGD2}
\]

fails at its second arrow. Orthogonality isolates the non-load-bearing character diagonal; exact treatment of the cross-character terms returns PGD2.
