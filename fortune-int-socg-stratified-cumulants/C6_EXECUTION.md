# C6 execution — signed cumulant assembly

**Status:** `BLOCKED_BY_C2; HIGHER_CONNECTED_CORE_REDUCED`

C3 removes repeated-column ordinary-cumulant combinatorics at an additive dependence-radius cost of one. The remaining higher-order route may therefore be written using the correctly defined factorial cumulants

\[
f_{k,b}=
\sum_{\pi\in\Pi_k}
(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{C\in\pi}M_{|C|,b},
\]

where `M_r` is the distinct-offset factorial moment.

A sufficient higher connected theorem is

\[
|f_{k,b}|
\le c_{1,b}k!D_{F,b}^{k-1},
\qquad
D_{F,b}\ll X/(\log X)^{1+\delta}.
\]

By C3 this implies the ordinary `INT-SOCG` estimate with radius `D_{F,b}+1`.

C4 shows that the pairwise local edge row-sum is compatible with `D_F=O(X/log^2 X)`. C5 proves the required average orthogonality for prime moduli. The unresolved higher core consists of:

1. an all-orders connected local hypergraph/tree bound (`INT-LCSK`);
2. a weighted squarefree-composite primorial-walk extension (`INT-PWOC`);
3. their signed recombination before absolute values.

However, even a proof of all three would not establish `INT-SOCG` without

\[
c_{1,b}\ge c_0X.
\]

The C2 theorem `INT-SCME` is logically prior and is currently unproved. The registered terminal status is therefore determined by C2 rather than by the residual higher connected core.
