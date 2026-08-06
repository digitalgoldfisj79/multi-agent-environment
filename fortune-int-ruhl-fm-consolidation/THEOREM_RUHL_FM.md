# Exact finite-order RUHL-FM theorem

## Setup

Fix one deterministic terminal-prime stratum `B_b` of size `n_b`. For every row `j` let `Z_j` be the registered non-negative integer prime-pair count, and define

\[
G_b(s)=\frac1{n_b}\sum_{j\in B_b}s^{Z_j},
\qquad
M_{b,k}=\frac1{n_b}\sum_{j\in B_b}(Z_j)_k.
\]

Let deterministic model means satisfy

\[
0<L_b\le\lambda_j\le U_b.
\]

For `k>=0`, put

\[
E_{b,k}=M_{b,k}-\frac1{n_b}\sum_{j\in B_b}\lambda_j^k.
\]

Let `0<q_b<=q_A` and let `K_b` be even.

## Theorem R1 — sharp Bonferroni detector criterion

If

\[
e^{-q_bL_b}
+
R_{b,K_b}
+
\mathcal E_{b,K_b}
<\frac1{n_bB},
\tag{R1}
\]

where

\[
R_{b,K_b}=
\frac{(q_bU_b)^{K_b+1}}{(K_b+1)!}
\]

and

\[
\mathcal E_{b,K_b}
=
\sum_{k=0}^{K_b}\frac{(-q_b)^k}{k!}E_{b,k},
\]

then

\[
G_b(1-q_b)<\frac1{n_bB}.
\]

If (R1) holds in every stratum, then the adaptive occupancy detector is less than one, hence `INT-AOD` and eventual Fortune follow.

### Proof

For each integer `z>=0`, the binomial expansion terminates:

\[
(1-q)^z=\sum_{k=0}^{z}\frac{(-q)^k}{k!}(z)_k.
\]

For even `K`, the even Bonferroni partial sum is an upper bound:

\[
(1-q)^z
\le
\sum_{k=0}^{K}\frac{(-q)^k}{k!}(z)_k.
\]

Averaging over the stratum gives

\[
G_b(1-q_b)
\le
\sum_{k=0}^{K_b}\frac{(-q_b)^k}{k!}M_{b,k}.
\]

Substitute the definition of `E_{b,k}`:

\[
G_b(1-q_b)
\le
\frac1{n_b}
\sum_{j\in B_b}
\sum_{k=0}^{K_b}
\frac{(-q_b\lambda_j)^k}{k!}
+
\mathcal E_{b,K_b}.
\]

Because `K_b` is even, Taylor's theorem for `e^{-x}` gives, for every `x>=0`,

\[
0\le
\sum_{k=0}^{K_b}\frac{(-x)^k}{k!}-e^{-x}
\le
\frac{x^{K_b+1}}{(K_b+1)!}.
\]

Therefore

\[
G_b(1-q_b)
\le
\frac1{n_b}\sum_{j\in B_b}e^{-q_b\lambda_j}
+
R_{b,K_b}
+
\mathcal E_{b,K_b}
\le
 e^{-q_bL_b}+R_{b,K_b}+\mathcal E_{b,K_b}.
\]

Condition (R1) proves the stratum bound. Multiplication by `n_b` and summation over the `B` strata gives a total adaptive detector below one. Since `q_b<=q_A`, termwise monotonicity transfers this to the frozen detector. The inherited detector theorem then gives eventual Fortune. `square`

## Corollary R1A — absolute-error form

It is sufficient that

\[
\mathcal A_{b,K_b}
=
\sum_{k=0}^{K_b}\frac{q_b^k}{k!}|E_{b,k}|
<
\frac1{n_bB}-e^{-q_bL_b}-R_{b,K_b}.
\tag{R1A}
\]

This is the sharp sufficient absolute-error margin delivered by the proof. The previously registered condition

\[
\mathcal A_{b,K_b}\le(n_bB)^{-1-2\varepsilon}
\]

is a stronger convenient subcase, not the weakest sufficient budget.

## Corollary R2 — logarithmic-order truncation

Put

\[
M_b^*=n_bB,
\qquad
q_b=(1+3\varepsilon)\frac{\log M_b^*}{L_b},
\qquad
\rho_b=\frac{U_b}{L_b},
\]

and choose

\[
K_b=\lceil\beta\log M_b^*\rceil_{\mathrm{even}}.
\]

Using `(K+1)!>=((K+1)/e)^(K+1)` and `K_b+1>=beta log M_b^*`,

\[
R_{b,K_b}
\le
\left(
\frac{e(1+3\varepsilon)\rho_b}{\beta}
\right)^{K_b+1}
\le
(M_b^*)^{-\alpha_b},
\]

where

\[
\alpha_b=
\beta\log\!\left(
\frac{\beta}{e(1+3\varepsilon)\rho_b}
\right).
\]

Hence `alpha_b>=1+2 epsilon` gives the registered Taylor budget.

For

\[
\varepsilon=0.10,
\qquad
\rho_b\le1.10,
\]

`beta=5` gives

\[
\alpha_b
=5\log\!\left(\frac5{e\cdot1.30\cdot1.10}\right)
>1.2588>1.20.
\]

Thus the displayed `beta=10` example in the parent programme is valid but non-minimal; `beta=5` already certifies the same asymptotic tail exponent under the registered ratio bound.

## Logical status

This theorem is unconditional as a finite combinatorial implication. Its use for Fortune is conditional because no available theorem supplies the required factorial-moment errors for the selected primorial rows through order `Theta(log X)`.

The signed condition is the weakest condition used by this proof, but it is close to the truncated detector discrepancy itself. Only the absolute or tuple-decomposed versions constitute potentially independent arithmetic hypotheses.
