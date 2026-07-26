# Fixed interior q-line cell no-go

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-boulders-hayes-first-20260725`  
**Classification:** **EXACT COMPUTER-ASSISTED COUNTEREXAMPLE TABLE**.  
**Scope:** constructive bypass by one geometrically distinguished split q-cell.

## 1. Question

For fixed integer `q_0`, reduce it modulo each admitted prime and consider the split normal-form family

\[
q_0Z^p+Z^3-3Z-(q_0-2)t,
\qquad t\in\mathbf F_p.
\]

Could one fixed value of `q_0` contain an irreducible fibre for every prime

\[
p\equiv5\pmod6?
\]

Such a value would prove the crown without the global Airy estimate or q-line comparison.

## 2. Exact failures

The following small geometrically natural values were tested by complete factorisation of every `t`-fibre. Their first zero-cell primes are:

| fixed `q_0` | first admitted prime with no irreducible fibre |
|---:|---:|
| `-2` | `5` |
| `3` | `5` |
| `-5` | `11` |
| `-3` | `11` |
| `-1` | `11` |
| `6` | `11` |
| `-4` | `17` |
| `4` | `17` |
| `7` | `17` |
| `1` | `23` |
| `5` | `53` |

Thus every tested fixed cell fails, and the last survivor `q_0=5` already fails at `p=53`.

## 3. Ruling

This closes the proposed strategy

> choose one small or geometrically distinguished fixed q-cell and prove it always contains an irreducible fibre.

It does not prove that every possible fixed rational q-value eventually fails. It proves that none of the natural low-height candidates used by the programme can carry a uniform theorem.

The complete-boundary failures at `p=53,71` already show that a successful proof cannot be supported only at `q=2` and `q=infinity`. The present table gives the corresponding interior warning: the successful q-cell must genuinely vary with `p`, or the proof must use a global q-line theorem.

## 4. Verification

`fixed_q_cell_no_go_verify.py` reproduces the table using exact `python-flint` factorisation.
