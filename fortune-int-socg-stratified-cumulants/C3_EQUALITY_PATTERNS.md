# C3 — equality patterns and diagonal elimination

For ordinary cumulants,

\[
c_{k,b}=\sum_{m_1,\ldots,m_k}
\operatorname{Cum}_b(I_{m_1},\ldots,I_{m_k}).
\]

The sum includes repeated offsets. Group ordered tuples by their equality partition `rho` of `[k]`. If `rho` has `r` blocks, assign `r` distinct candidate columns injectively to those blocks; indicator idempotence collapses repeated occurrences inside joint moments.

## Tasks

1. derive the exact partition-lattice coefficient system;
2. verify it over exact rational finite incidence matrices;
3. isolate one-column, partial-diagonal and fully distinct contributions;
4. measure the smallest `D_diag` satisfying the target bound for all diagonal classes;
5. pass only the fully distinct connected core to C4.

## Pass condition

An exact identity and a proof that all repeated-column classes are compatible with `D_b=o(X/log X)`, or an explicit diagonal obstruction.

## Safety rule

The false factorial-cumulant/distinct-column formula is permanently excluded.