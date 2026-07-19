# CRT character-diagonal theorem

Let

\[
m=\prod_{s=1}^tq_s
\]

be squarefree and let all primorial prefixes `P_j` be units modulo `m`. For

\[
F_m(A)=\sum_{j<N}e_m(AP_j),
\]

multiplicative Fourier inversion gives

\[
F_m(A)=\frac1{\varphi(m)}
\sum_{\chi\bmod m}\tau_m(\overline\chi)\chi(A)S_m(\chi).
\]

Writing

\[
|F_m(A)|^2=\mathfrak D_m+\mathfrak O_m(A),
\]

the equal-character sector is exactly

\[
\boxed{
\mathfrak D_m=
\sum_{i,j<N}
\prod_{q\mid m}
\frac{q\mathbf1_{P_i\equiv P_j\pmod q}-1}{q-1}.}
\]

This follows from

\[
\frac1{(q-1)^2}
\sum_{\chi\bmod q}|\tau_q(\overline\chi)|^2\chi(z)
=
\frac{q\mathbf1_{z=1}-1}{q-1}
\]

and CRT factorisation.

Consequences:

- `D_m` is independent of the additive coefficient and sign pattern.
- With no off-diagonal collisions and four prime factors,
  \[
  \mathfrak D_m=N+\frac{N(N-1)}{\varphi(m)}=N+o(1).
  \]
- Shell-divisor conditions `q | R_{i,j}-1` enter this diagonal sector.
- Sign-dependent reciprocal fluctuation lies in `O_m(A)`.

The identity and the complete diagonal/off-diagonal energy reconstruction were validated on finite prime through four-prime systems with worst absolute residual below `2e-12`.
