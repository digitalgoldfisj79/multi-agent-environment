# Growing Möbius-degree truncation gate

## Exact degree identity

For \(n\in[H,2H)\), put

\[
s_X(n)=\omega((n,A_X)),
\qquad A_X=\prod_{p<X}p.
\]

Because \(n<X^2\), primality is exactly equivalent to \((n,A_X)=1\). Define

\[
T_k(n)=
\sum_{\substack{d\mid(n,A_X)\\\omega(d)\le k}}\mu(d).
\]

The binomial identity gives

\[
\boxed{
T_k(n)=
\begin{cases}
1,&s_X(n)=0,\\
0,&1\le s_X(n)\le k,\\
(-1)^k\binom{s_X(n)-1}{k},&s_X(n)>k.
\end{cases}}
\]

Thus

\[
\mathbf1_{n\ \mathrm{prime}}=T_k(n)-R_k(n),
\qquad
R_k(n)=T_k(n)\mathbf1_{s_X(n)>k}.
\]

The identity was exhaustively checked for \(0\le s,k<40\).

## High-degree tail bound

For \(s>k\),

\[
|T_k(n)|=\binom{s-1}{k}\le\binom{s}{k+1}.
\]

Therefore

\[
\sum_{n<2H}|R_k(n)|
\le
2H
\sum_{\substack{d\mid A_X\\\omega(d)=k+1}}\frac1d
\le
\frac{2H}{(k+1)!}
\left(\sum_{p<X}\frac1p\right)^{k+1}.
\]

For

\[
k=\left\lceil(1+\eta)\frac{\log X}{\log\log X}\right\rceil,
\qquad \eta>0,
\]

Mertens' theorem and Stirling give

\[
\sum_{n<2H}|R_k(n)|\le H X^{-1-\eta+o(1)}.
\]

Let

\[
\mathcal C(c)=
\sum_{n\in I}\gamma_{n,a}c(n)
\bigl(z_{n,a}z_{n,a}^{*}-I_M\bigr),
\qquad
|\gamma_{n,a}|\ll\frac{\log H}{H}.
\]

Since

\[
\|z_{n,a}z_{n,a}^{*}-I_M\|_F\le M,
\]

we obtain

\[
\boxed{
\|\mathcal C(R_k)\|_F^2
\le M^2X^{-2-2\eta+o(1)}
=MX^{-2\eta+o(1)}.}
\]

Hence the high-Möbius-degree tail is admissible. PGD2 may be reduced to the globally coupled detector \(T_k\) with growing degree
\(k\sim(1+\eta)\log X/\log\log X\).

## Conditioning audit

The cumulative degree detector was evaluated exactly at
\(X=30,50,80,100,120\). Low truncation degrees are highly ill-conditioned: the retained and tail centred Frobenius norms were typically tens of times the final prime norm.

At the near-maximal finite degree \(k=\max s_X-1\), the cumulative detector became comparable to the prime operator, but splitting that retained detector by divisor size was catastrophic:

| \(X\) | \(k\) | sum of band energies / prime energy | sum of band norms / prime norm |
|---:|---:|---:|---:|
| 30 | 3 | 207.36 | 27.21 |
| 50 | 4 | 821.11 | 54.42 |
| 80 | 4 | 2139.95 | 88.55 |
| 100 | 4 | 2872.68 | 100.37 |

Exact recombination errors were at floating-point roundoff.

## Decision

This is a valid new reduction, but not yet a proof engine:

\[
\boxed{
\text{high Möbius degree is negligible, but the retained growing-degree detector must remain fully coupled.}}
\]

Separate Type-I/Type-II or divisor-size estimates remain red. Leaving all retained degrees coupled gives a new precise target, but no current theorem estimates that signed reciprocal operator.
