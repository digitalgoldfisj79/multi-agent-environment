# B2 — defect propagation audit

The centre recurrence is

\[
P_{j+1}=\ell_{j+1}P_j.
\]

If an output at row `j` is written as `P_j+m`, multiplication by `ell_{j+1}` gives

\[
\ell_{j+1}(P_j+m)=P_{j+1}+\ell_{j+1}m.
\]

Thus the only canonical offset transport is

\[
m\longmapsto m'=\ell_{j+1}m.
\]

For an admissible candidate, `m>ell_j>=X`. Since `ell_{j+1}>=X`,

\[
m'>X^2>\eta X^2=H.
\]

Therefore no admissible offset at row `j` is transported into the registered window at row `j+1`.

## Consequence

The multiplicative primorial recurrence does not force a failed row to produce a neighbouring failed or low-source row. The source windows are arithmetically linked at scales larger than the registered window, not inside it.

## Surrogate obstruction

Because successive intervals are separated by

\[
P_{j+1}-P_j=(\ell_{j+1}-1)P_j\gg H,
\]

one may assign local weights independently on the disjoint windows while preserving:

- the exact centre recurrence;
- the local rule `p|P_j+m iff p|m` for every `p|P_j`;
- the candidate mask `(m,P_j)=1`;
- ordinary source size on all but one row.

Setting one selected row to zero gives an isolated-defect surrogate. This is not a counterexample for primes; it proves that recurrence and local congruence geometry alone cannot yield defect propagation.

## Ruling

`DEFECT_PROPAGATION_REDUCTION` is unavailable through the natural primorial map. Any future propagation theorem must use genuinely global prime correlations, not centre nesting alone.
