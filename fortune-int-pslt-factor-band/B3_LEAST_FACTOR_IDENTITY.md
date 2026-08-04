# B3 — exact least-factor/Buchstab partition

For a registered row define the candidate set

\[
\mathcal A_j=\{m:\ell_j<m\le H,\ m\text{ prime}\}.
\]

Below the square threshold this is exactly the set of offsets coprime to `P_j`, apart from the irrelevant offset `1`.

Let

\[
Z_j(H)=\#\{m\in\mathcal A_j:P_j+m\text{ prime}\}.
\]

For a composite output `n=P_j+m`, let `r=P^-(n)` be its least prime factor and define

\[
M_j(r)=\#\{m\in\mathcal A_j:P^-(P_j+m)=r\}.
\]

## Lemma B3.1 — the factor starts beyond the primorial

If `r<=ell_j`, then `r|P_j`. From `r|P_j+m` it follows that `r|m`. But `m` is prime and `m>ell_j>=r`, a contradiction. Hence

\[
\boxed{r>\ell_j.}
\]

Since `r` is the least factor of a composite number,

\[
r\le\sqrt{P_j+H}.
\]

## Exact identity

Every candidate output is either prime or composite with a unique least prime factor. Therefore

\[
\boxed{
|\mathcal A_j|
=Z_j(H)+
\sum_{\ell_j<r\le\sqrt{P_j+H}\atop r\text{ prime}}M_j(r).
}
\]

This is the exact first Buchstab partition with no probabilistic main term inserted.

## Parity-boundary geometry

Because `H=eta X^2`, `0<eta<1`, and `ell_j>=X`,

\[
\sqrt H=\sqrt\eta X<X\le\ell_j<r.
\]

Thus every factor in the exact composite partition begins strictly beyond the square root of the offset-variable length.

A failed row is equivalent to complete least-factor coverage:

\[
Z_j(H)=0
\quad\Longleftrightarrow\quad
\sum_rM_j(r)=|\mathcal A_j|.
\]
