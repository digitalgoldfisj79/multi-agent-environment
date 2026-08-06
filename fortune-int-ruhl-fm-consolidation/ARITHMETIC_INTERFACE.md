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
=\sum_{(m_1,\ldots,m_k)\in\mathcal M_b^{\underline{k}}}
\prod_{a=1}^k I_{j,m_a},
\]

where `mathcal M_b^{underline k}` denotes ordered tuples of distinct offsets. Consequently

\[
M_{b,k}
=\frac1{n_b}
\sum_{j\in B_b}
\sum_{\mathbf m\in\mathcal M_b^{\underline{k}}}
\prod_{a=1}^k
1_{\mathbb P}(m_a)1_{\mathbb P}(P_j+m_a).
\tag{A1}
\]

This identity is exact and contains no cumulant or independence approximation.

## Exact model decomposition

Let `H_{j,k}(\mathbf m)` denote the registered Hardy--Littlewood model term for

\[
P_j+m_1,\ldots,P_j+m_k,
\]

with the primality of the offsets already frozen into the candidate universe or retained explicitly in the weight. The model must contain the registered local admissibility and archimedean factors; it must not be replaced by a heuristic product without a proved averaging step.

Define

\[
A_{b,k}
=\frac1{n_b}
\sum_{j\in B_b}
\sum_{\mathbf m\in\mathcal M_b^{\underline{k}}}
\left(
\prod_{a=1}^k I_{j,m_a}-H_{j,k}(\mathbf m)
\right)
\tag{A2}
\]

and

\[
S_{b,k}
=\frac1{n_b}
\sum_{j\in B_b}
\sum_{\mathbf m\in\mathcal M_b^{\underline{k}}}
H_{j,k}(\mathbf m)
-\frac1{n_b}\sum_{j\in B_b}\lambda_j^k.
\tag{A3}
\]

Then, exactly,

\[
\boxed{E_{b,k}=A_{b,k}+S_{b,k}.}
\tag{A4}
\]

This is a telescoping identity. A boundary, prime-power or support correction must be incorporated into the definition of the observed moment, the candidate universe, or `H_{j,k}` before (A2)--(A3) are formed. It must not be appended as an additional `Q_{b,k}` after (A2)--(A3), because that would double-count the correction. An alternative three-term convention is legitimate only after one of `A_{b,k}` or `S_{b,k}` has been redefined so that the displayed sum remains exact.

## Sufficient weighted arithmetic theorem

Under the exact convention above, the sharp sufficient absolute RUHL-FM condition follows from

\[
\sum_{k=0}^{K_b}
\frac{q_b^k}{k!}
\left(|A_{b,k}|+|S_{b,k}|\right)
<
\frac1{n_bB}
-e^{-q_bL_b}
-\frac{(q_bU_b)^{K_b+1}}{(K_b+1)!}.
\tag{A5}
\]

A signed theorem may exploit cancellation across `k`, tuples and source components. The signed first-order contribution is `-q_bE_{b,1}`: excess actual mean helps, while a deficit must be controlled together with all higher-order signed terms. The absolute envelope deliberately discards this one-sided slack.

## What existing inputs cover

- Growing-set singular-series averages can plausibly address portions of `S_{b,k}` when the offset family is sufficiently dense and `k=O(log X)`.
- The local pair-scale and connected-cluster work in `INT-SOCG` informs correlation geometry, but does not bound `A_{b,k}` through growing order.
- The prime-modulus primorial-walk theorem controls one prime-modulus energy. It does not supply the weighted squarefree-composite source estimate needed to derive (A2).
- `INT-SCME` concerns a linear lower bound for the first moment. It does not supply additive `O(1)` model accuracy or the family `A_{b,k}` for `k>=2`.

## Exact missing input

The unresolved arithmetic core is:

> Uniformly over every registered terminal-prime stratum and every `k<=K_b=Theta(log X)`, control the jointly signed selected-centre prime-tuple residual strongly enough that its Bonferroni-weighted aggregate lies below the one-row detector margin.

No audited theorem currently supplies this estimate on the exponentially sparse primorial path. The identity (A4) is an exact interface, not an unconditional reduction of that analytic problem.
