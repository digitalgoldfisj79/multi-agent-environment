# M1 — normalization and output prime powers

**Status:** `PASSED_EXACT`

For a deterministic row set `C` and common candidate universe `M`, define

\[
T_C=\frac1{|C|}\sum_{j\in C}\sum_{m\in M}\log m\,\Lambda(P_j+m).
\]

Let

\[
Z_C=\frac1{|C|}\sum_{j\in C}\#\{m\in M:P_j+m\text{ prime}\}.
\]

When `H<2 sqrt(P_j)`, every proper prime power in `(P_j,P_j+H]` is a square. There are `O(H/sqrt(P_j)+1)` such squares per row, hence their total weighted contribution is `O(X(log X)^2)` in the inherited asymptotic regime.

For an actual prime output,

\[
\log m\,\log(P_j+m)\le \log H\,\log(P_j+H)=O(X\log X).
\]

Consequently a uniform lower bound

\[
T_C\ge \kappa X^2\log X
\]

implies

\[
Z_C\ge c_0X
\]

for some fixed `c_0>0`, after subtracting proper output prime powers. Averaging microblock bounds gives the same lower bound for every parent stratum.

This gate is only an implication. It does not claim the weighted lower bound.