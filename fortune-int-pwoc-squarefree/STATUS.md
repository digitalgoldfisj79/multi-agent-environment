# Execution status

**Programme:** `FORTUNE_INT_PWOC_SQUAREFREE_V0_1`  
**Date:** 6 August 2026  
**Branch:** `gpt56/fortune-int-pwoc-sf-v01-20260806`  
**State:** `EXECUTED_AND_VALIDATED`

## Gates

- P0: passed for W0/W1; W2/W3 unavailable.
- P1: exact character/kernel identity proved and regression checked.
- P2: deterministic Lean bridge and fixed-order summation kernel checked.
- P3: exact order-`r` collision count bound proved.
- P4: W0 falsified as a uniform subcritical class; W1 frozen; W2/W3 unavailable.
- P5: fixed-order bounded-weight extension proved.
- P6: not executable without actual signed source coefficients.
- P7: exact and adversarial panels passed.
- P8: no exact transfer to RUHL-FM or INT-SOCG is available.
- P9: exact regressions, targeted Lean, full-package Lean and trust scan passed.

## Main theorem

For `omega(q)=r`, prime factors above `2X`, and `0<=beta(q)q<=U_r`,

\[
R_\beta\le U_r{n-1\choose r+1}
\]

and therefore

\[
\mathcal E_\beta(a)
\le
\left(D_\beta+U_r{n-1\choose r+1}\right)\|a\|_2^2.
\]

## Validation record

Workflow run `31078608311` at head `429f514257c9c1317d6ae0884805983cc16d56a8`:

- static trust audit and exact execution regressions: **PASS**;
- targeted Lean build: **PASS**;
- full formal package build: **PASS**;
- new-file `sorry` / `admit` / `axiom` / `unsafe` scan: **PASS**;
- Lean version: `4.32.0`.

## Terminal classification

- `FIXED_ORDER_COMPOSITE_EXTENSION_PROVED`
- `SOURCE_WEIGHT_CONTRACT_NOT_AVAILABLE`
- `NO_TRANSFER_TO_RUHL_OR_SOCG`

PWOC-SF2 remains open.

No actual source-compatible squarefree coefficient family has been bounded.  
No proof of INT-PWOC, INT-AOD or Fortune is claimed.
