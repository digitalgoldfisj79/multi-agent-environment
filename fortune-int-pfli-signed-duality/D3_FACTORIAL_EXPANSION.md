# D3 — exact factorial expansion

Put

\[
q_X=1-e^{-\tau_X}\in(0,1).
\]

For every nonnegative integer `Z`,

\[
e^{-\tau_X Z}=(1-q_X)^Z
=\sum_{k=0}^{Z}(-q_X)^k\binom Zk.
\]

Therefore

\[
\mathcal O_X
=\sum_{k\ge0}(-q_X)^kM_k(X),
\qquad
M_k(X)=\sum_{j<N}\binom{Z_j}{k},
\]

where the sum is finite because `binom(Z_j,k)=0` for `k>Z_j`.

## Bonferroni truncations

For every integer `K>=0`, the alternating binomial expansion gives

\[
\sum_{k=0}^{2K+1}(-q_X)^k\binom Zk
\le (1-q_X)^Z
\le
\sum_{k=0}^{2K}(-q_X)^k\binom Zk.
\]

After summing over rows,

\[
\sum_{k=0}^{2K+1}(-q_X)^kM_k(X)
\le\mathcal O_X\le
\sum_{k=0}^{2K}(-q_X)^kM_k(X).
\]

Thus a factorial-moment proof of `INT-AOD` must produce an upper Bonferroni truncation below `1`, or control the full generating function by another all-orders mechanism.

## Warning

The existence of the formal expansion does not make a fixed-order truncation useful. D4 constructs panels with identical factorial moments through order `K` but opposite zero-row status. That obstruction is exact and independent of the value of `q_X` in `(0,1)`.
