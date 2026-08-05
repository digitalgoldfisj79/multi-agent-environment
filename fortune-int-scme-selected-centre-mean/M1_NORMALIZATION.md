# M1 — normalization and output prime powers

**Status:** `PASSED_EXACT_ERRATUM_CORRECTED`

For a deterministic row set `C` and common candidate universe `M`, define

\[
T_C=\frac1{|C|}\sum_{j\in C}\sum_{m\in M}\log m\,\Lambda(P_j+m).
\]

Let `Z_C` be the corresponding average number of actual prime outputs.

The previous wording that every proper prime power in `(P_j,P_j+H]` is a square was false. Squares dominate. Cubes and higher powers are spaced by `gg P_j^(2/3)`, hence contribute only `O(1)` terms per row because `H` is polynomial in `X` while `P_j` is exponential. Together all proper prime powers remain within the inherited `O(X(log X)^2)` weighted budget per row.

For an actual prime output,

\[
\log m\,\log(P_j+m)\le \log H\,\log(P_j+H)=O(X\log X).
\]

Consequently

\[
T_C\ge \kappa X^2\log X
\]

implies `Z_C>=c_0X` after subtracting proper prime powers. This is only a first-cumulant implication; it does not establish any higher-cumulant component of `INT-SOCG`.
