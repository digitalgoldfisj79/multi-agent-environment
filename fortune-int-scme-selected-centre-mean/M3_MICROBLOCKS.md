# M3 — deterministic microblocks

**Status:** `PASSED_EXACT`

Fix `0<rho<1`. Within each inherited parent stratum, order rows by terminal prime and split them consecutively into blocks of

\[
R=\lfloor X^\rho\rfloor
\]

rows. If the final block has fewer than `R/2` rows, merge it with the preceding block. Every retained microblock then has between `R/2` and `2R` rows.

The construction depends only on terminal-prime order and `X`. It does not inspect `P_j+m`, primality, occupancies or factor profiles.

If every microblock `C` in a parent stratum satisfies

\[
T_C\ge \kappa X^2\log X,
\]

then the parent mean is the row-count-weighted average of its microblock means and satisfies the same lower bound.

The programme optimizes at `rho=2/3`. This is a proof device inside each frozen parent stratum; it does not alter the inherited `INT-SCME` statement.