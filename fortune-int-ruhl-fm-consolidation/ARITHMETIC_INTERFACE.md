# Arithmetic interface for the RUHL-FM error

## Exact factorial-moment expansion

Let `mathcal M_b` be the frozen candidate-offset universe in stratum `b`, and let

\[
I_{j,m}=1_{\mathbb P}(m)1_{\mathbb P}(P_j+m).
\]

Then

\[
Z_j=\sum_{m\in\mathcal M_b}I_{j,m}
\]

and, for every `k>=1`,

\[
(Z_j)_k
=
\sum_{(m_1,\ldots,m_k)\in\mathcal M_b^{\underline{k}}}
\prod_{a=1}^k I_{j,m_a},
\]

where `mathcal M_b^{underline k}` denotes ordered tuples of distinct offsets.

Consequently

\[
M_{b,k}
=
\frac1{n_b}
\sum_{j\in B_b}
\sum_{\mathbf m\in\mathcal M_b^{\underline{k}}}
\prod_{a=1}^k
1_{\mathbb P}(m_a)1_{\mathbb P}(P_j+m_a).
\tag{A1}
\]

This identity is exact and contains no cumulant or independence approximation.

## Model decomposition

Let `H_{j,k}(mathbf m)` denote the exact registered Hardy--Littlewood model term for the forms

\[
P_j+m_1,\ldots,P_j+m_k,
\]

with the primality of the offsets themselves already frozen into the candidate universe or retained explicitly in the weight. The model must include the correct local admissibility factor and archimedean weight; it must not be replaced by a heuristic product without a proved averaging step.

Define

\[
A_{b,k}
=
\frac1{n_b}
\sum_{j\in B_b}
\sum_{\mathbf m\in\mathcal M_b^{\underline{k}}}
\left(
\prod_{a=1}^k I_{j,m_a}
-
H_{j,k}(\mathbf m)
\right)
\tag{A2}
\]

and

\[
S_{b,k}
=
\frac1{n_b}
\sum_{j\in B_b}
\sum_{\mathbf m\in\mathcal M_b^{\underline{k}}}
H_{j,k}(\mathbf m)
-
\frac1{n_b}
\sum_{j\in B_b}\lambda_j^k.
\tag{A3}
\]

After adding any explicitly registered boundary or prime-power correction `Q_{b,k}`, the factorial-moment error is

\[
E_{b,k}=A_{b,k}+S_{b,k}+Q_{b,k}.
\tag{A4}
\]

## Sufficient weighted arithmetic theorem

The sharp absolute RUHL-FM condition follows from

\[
\sum_{k=0}^{K_b}
\frac{q_b^k}{k!}
\left(
|A_{b,k}|+|S_{b,k}|+|Q_{b,k}|
\right)
<
\frac1{n_bB}
-e^{-q_bL_b}
-
\frac{(q_bU_b)^{K_b+1}}{(K_b+1)!}.
\tag{A5}
\]

A signed version may exploit cancellation across `k`, but a proof that obtains (A5) termwise is more clearly independent of the detector target.

## What existing inputs cover

- Growing-set singular-series averages can plausibly address portions of `S_{b,k}` when the offset family is sufficiently dense and `k=O(log X)`.
- The local pair-scale and connected-cluster work in `INT-SOCG` informs correlation geometry, but does not bound `A_{b,k}` through growing order.
- The prime-modulus primorial-walk theorem controls one prime-modulus energy. It does not supply the weighted squarefree-composite estimates needed to derive (A2) from a source decomposition.
- `INT-SCME` concerns the first moment. It does not supply the full family `A_{b,k}` for `k>=2`.

## Exact missing input

The unresolved arithmetic core of the conditional theorem is therefore:

> Uniformly over every registered terminal-prime stratum and every `k<=K_b=Theta(log X)`, control the aggregate selected-centre prime-tuple residual `A_{b,k}` strongly enough that its Bonferroni-weighted sum, together with the model-collapse and correction terms, lies below the one-row detector margin in (A5).

No audited theorem currently supplies this estimate on the exponentially sparse primorial path.
