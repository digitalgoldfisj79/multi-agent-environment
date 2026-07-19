# D2 — structured random-matrix gate

The exact identities
\[
A=V^*PV,\qquad K=P^{1/2}VV^*P^{1/2},
\]
imply that \(A\) and \(K\) have the same non-zero spectrum. For \(E=A-WI\), every trace moment is a binomial combination of the moments of \(A\). This is a useful compression of the ECM bookkeeping.

## Gate decision

The identity is retained as a specialist-handoff formulation, but stopped as a black-box proof route.

Existing local-law and no-outlier theorems for Gram/sample-covariance matrices are probabilistic. Their hypotheses include independent random entries or independent random sample vectors, concentration of quadratic forms, correlation decay, or controlled cumulant tensors. Here the columns/rows are deterministic functions of the same consecutive-prime product walk. None of the required randomness or concentration statements is available independently of the reciprocal-cancellation problem.

A no-outlier bound would be sufficient but is stronger than the second-moment target: if \(\operatorname{rank}E\asymp M\) and \(\|E\|_{op}\le X^{o(1)}\), then \(\|E\|_F^2\le MX^{o(1)}\). The difficulty is proving the operator bound from arithmetic. Rebranding the same arithmetic correlations as a deterministic Gram matrix does not supply it.

## Status

- exact algebra: accepted;
- communication value: high;
- direct theorem applicability: none identified;
- active use: one-page brief to structured-RMT specialists, not further internal moment computation.
