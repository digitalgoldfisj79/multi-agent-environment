# R1 — the signed condition is the truncated detector discrepancy

Put

\[
B_K(z;q)=\sum_{k=0}^{K}\frac{(-q)^k}{k!}(z)_k,
\qquad
T_K(x)=\sum_{k=0}^{K}\frac{(-x)^k}{k!}.
\]

By the definitions of the factorial moments and errors,

\[
\boxed{
\mathcal E_{b,K}
=
\frac1{n_b}\sum_{j\in B_b}B_K(Z_j;q_b)
-
\frac1{n_b}\sum_{j\in B_b}T_K(q_b\lambda_j).
}
\]

This identity is exact. The first average is the even Bonferroni truncation of the actual occupancy detector; the second is the registered model approximation.

Therefore the signed RUHL condition is not, by itself, an independent arithmetic simplification. A proof must expose a non-circular mechanism that estimates this jointly signed expression. Splitting into moment orders and taking absolute values produces an independent sufficient theorem, but that theorem is substantially stronger, as R2 shows.
