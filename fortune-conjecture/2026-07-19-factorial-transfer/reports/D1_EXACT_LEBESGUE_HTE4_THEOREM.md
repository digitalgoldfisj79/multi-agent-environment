# D1 — exact Lebesgue fourth-moment theorem

Let
\[
S=\{S_{ij}=P_i+P_j:1\le i\le j\le N\},\qquad M=|S|=\frac{N(N+1)}2,
\]
and
\[
H_2(\theta)=\sum_{1\le i\le j\le N} e(\theta S_{ij}).
\]
Assume the established bounded-relation rigidity in the four-copy range: an equality
\(S_{ij}+S_{k\ell}=S_{ab}+S_{cd}\) holds exactly when the endpoint multiplicity vectors agree.

## Theorem

\[
\int_0^1 |H_2(\theta)|^4\,d\theta
=E_4(S)
=\frac{N(3N^3-2N^2+2N-1)}2.
\]
Consequently,
\[
\int_0^1\bigl(|H_2(\theta)|^2-M\bigr)^2\,d\theta
=\frac{N(N-1)(5N^2-N+2)}4
=5M^2\bigl(1+O(N^{-1})\bigr).
\]

## Proof by endpoint-multiset type

For a multiset of four endpoints, let \(r\) be the number of ordered decompositions into two unordered pairs. The five partition types contribute:

| endpoint type | number of endpoint multisets | \(r\) | contribution to \(E_4\) |
|---|---:|---:|---:|
| \(1+1+1+1\) | \(\binom N4\) | 6 | \(36\binom N4\) |
| \(2+1+1\) | \(N\binom{N-1}2\) | 4 | \(16N\binom{N-1}2\) |
| \(2+2\) | \(\binom N2\) | 3 | \(9\binom N2\) |
| \(3+1\) | \(N(N-1)\) | 2 | \(4N(N-1)\) |
| \(4\) | \(N\) | 1 | \(N\) |

Summing gives the displayed polynomial. Parseval gives \(\int|H_2|^2=M\); expanding the centred square yields \(E_4-M^2\), which simplifies to the second formula.

At \(N=55\), the formula gives exactly \(13,562,560\), matching the independent Claude count.

## Correct implication for PGD2

Put \(K_X(\theta)=|H_2(\theta)|^2-M\) and write PGD2 as
\[
\mathcal R_a=\sum_{q\ne r}w_{q,r,a}K_X\!\left(a\left(\frac1q-\frac1r\right)\right),
\qquad w_{q,r,a}=p_{q,a}p_{r,a}\ge0.
\]
By weighted Cauchy–Schwarz,
\[
|\mathcal R_a|^2\le
\left(\sum_{q\ne r}w_{q,r,a}\right)
\left(\sum_{q\ne r}w_{q,r,a}K_X(\theta_{q,r})^2\right).
\]
Thus the open content is a sampling-transfer estimate comparing the weighted reciprocal-prime-pair sample of \(K_X^2\) with its Lebesgue mass \(\asymp M^2\). D1 solves the kernel-size side exactly; it does not prove the transfer.
