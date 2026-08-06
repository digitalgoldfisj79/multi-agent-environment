# O1 — detector admissibility execution

**Status:** PASSED

For nonnegative weights `a_m` frozen independently of output primality, define

\[
\mathcal O_X(a)=\sum_{j<N}\exp\!\left(-\sum_m a_m I_{jm}\right),
\qquad
I_{jm}=1_{\mathbb P}(m)1_{\mathbb P}(P_j+m).
\]

If row `j` fails, every `I_{jm}=0`; its detector contribution is exactly one. Hence `O_X(a)<1` excludes all failures.

## Admissibility contract

Weights may depend only on preregistered data available before testing `P_j+m` for primality:

- `X`, `H`, and `m`;
- divisibility and residue data determined by the input centres;
- preregistered local singular-series proxies;
- a deterministic seed fixed in the programme ledger.

They may not depend on:

- observed successful pairs;
- row occupancy values;
- post-hoc identification of failed rows;
- a search over weights whose comparison cost is omitted.

Every searched family must include its cardinality or metric-entropy penalty in the detector threshold. The uniform profile `a_m=tau` remains the default and incurs no search penalty.

## Formal status

The generic one-defect implication is already kernel checked by

`FortuneFormal.Integer.no_failure_of_soft_detector_sum_lt_one`.

No arithmetic theorem is claimed at O1.
