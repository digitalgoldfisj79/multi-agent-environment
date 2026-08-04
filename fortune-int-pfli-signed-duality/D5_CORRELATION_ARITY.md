# D5 — prime-correlation arity

Write

\[
x_{j,m}=1_{\mathbb P}(m)1_{\mathbb P}(P_j+m),
\qquad
Z_j=\sum_{m\in(\ell_j,H]}x_{j,m}.
\]

For every integer `k>=1`,

\[
\binom{Z_j}{k}
=
\sum_{\ell_j<m_1<\cdots<m_k\le H}
\prod_{a=1}^k x_{j,m_a}.
\]

Thus

\[
M_k(X)=\sum_{j<N}\binom{Z_j}{k}
\]

is exactly

\[
\sum_{j<N}
\sum_{m_1<\cdots<m_k}
\prod_{a=1}^k
1_{\mathbb P}(m_a)
1_{\mathbb P}(P_j+m_a).
\]

Each selected offset contributes two primality conditions. The `k`th factorial moment is therefore a coupled `2k`-prime correlation on a common primorial centre.

D4 proves that a factorial-moment-only proof resolving one row requires

\[
k>\log_2N=\Theta(\log X).
\]

Accordingly, the required prime-correlation arity must grow at least as

\[
\boxed{2k=\Omega(\log X).}
\]

## Ruling

No fixed-order extension of the earlier two-prime or four-prime moment programmes can prove the adaptive occupancy detector through moments alone. Increasing from second to fourth, sixth, or any other fixed moment does not cross the one-defect barrier.

The live alternatives are:

1. control the full occupancy generating function without termwise moment expansion;
2. obtain a rowwise prime-detection theorem;
3. prove a parity-breaking bilinear identity whose positivity acts before moments are truncated;
4. derive a selected-centre restriction theorem retaining information beyond finitely many moments.
