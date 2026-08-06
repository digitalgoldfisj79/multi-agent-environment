# Integer Fortune — stratified ordinary-cumulant programme

**Programme:** `FORTUNE_INT_SOCG_STRATIFIED_CUMULANTS_V0_1`  
**Branch:** `gpt56/fortune-int-socg-stratified-cumulants-v01-20260805`  
**Parent:** PR #55 / issue #56  
**Base commit:** `1d6ace4553bb88492dfceb894abd9e5d6713d426`  
**State:** `BUILT_NOT_EXECUTED`

## Frozen target

For each deterministic terminal-prime stratum `B_b`, let `J` be uniform on its rows and let

\[
Z_J=\sum_m 1_{\mathbb P}(m)1_{\mathbb P}(P_J+m).
\]

Write `c_{k,b}` for the ordinary cumulants of `Z_J`. The target `INT-SOCG` is

\[
c_{1,b}\ge L_b\ge cX,
\qquad
|c_{k,b}|\le c_{1,b}k!D_b^{k-1}\quad(k\ge2),
\qquad
D_b\ll X/(\log X)^{1+\delta}.
\]

With preregistered

\[
\tau_b=(1+3\varepsilon)\log(n_bB)/L_b\le\tau_A,
\]

this implies the stratified exponential detector, `INT-AOD`, and eventual Fortune.

## Programme design

The programme separates four logically distinct tasks:

1. prove the first-cumulant lower bound without using observed occupancies;
2. remove repeated-column and diagonal combinatorics exactly;
3. renormalize local singular-series interactions before absolute values;
4. prove signed cancellation along the selected primorial walk at dependence scale `o(X/log X)`.

A method is closed immediately when its best rigorous norm cannot reach that scale.

## Entry points

- `PROGRAMME.md` — gate sequence and stop conditions;
- `PREREGISTERED_GATES.json` — immutable execution contract;
- `METHOD_LEDGER.md` — admitted and prohibited lanes;
- `EXPONENT_LEDGER.json` — required scales and kill tests;
- `LITERATURE_AUDIT.md` — exact permitted use of external results;
- `RUNBOOK.md` — execution and compute discipline;
- `scripts/verify_programme.py` — static and exact build sentinel.

No proof of `INT-SOCG`, `INT-AOD`, or Fortune is claimed.