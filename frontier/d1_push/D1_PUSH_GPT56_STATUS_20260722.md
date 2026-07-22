# d=1 crown push — GPT-5.6 continuation status

**Date:** 2026-07-22  
**Base:** Claude commit `aede75b7590555d843322fd24de2ca958ecd25ee`  
**Branch:** `gpt56/d1-push-weight0-collapse-20260722`

## Scientific status

The function-field `d=1` Fortune crown remains open. The integer Fortune conjecture remains separate and open.

Claude's post-pushforward spectra package was materially correct and exposed the right geometry. This continuation converts four of its principal patterns into uniform exact theorems.

## New exact results

### 1. General weight-zero collapse

For every prime `p>=5` and every generic `q`, the alternating weight-zero hook cohomology cancels to exactly one quadratic module:

`sum_i (-1)^i Gr^W_0 H_c^1(U,V_i) = kappa_q`,

with Frobenius trace `chi(u_q)^n` in extension degree `n`.

The proof uses the boundary exact sequence and the exact local coset count of p-cycles:

- finite transposition punctures contribute zero;
- infinity contributes `1+chi(u_q)^n`;
- the global invariant line subtracts `1`.

The arithmetic/geometric quadratic discrepancy at infinity is therefore the required survivor, not a nuisance.

### 2. Uniform extremal weight-one curves

The two curve families observed at `p=5,7` persist for all `p`:

- `IH^1(V_2)=H^1(B_q)^-`, where
  `3s^2=12-d^2-4q d^(p-1)`;
- `IH^1(V_(p-2))=H^1(D_q)`, where
  `D_q: w^2=u_q g_(q,+)g_(q,-)`.

Their exact ranks are

`dim H^1(B_q)^- = 2 floor((p-1)/4)`,

`g(D_q)=p-3`, `dim H^1(D_q)=2p-6`.

Thus the genus-2 and genus-4 twist curves at `p=5,7` are the first members of a uniform genus-`p-3` family.

### 3. Complete configuration-curve presentation

Let `C_k(q)` be the sign-isotypic `H^1` of the ordered distinct k-root configuration curve. Then

`C_k=H_k direct_sum H_(k-1)`,

where `H_i=IH^1(exterior^i V)`. Consequently

`H_i=sum_(k=2)^i (-1)^(i-k) C_k`

and the complete alternating weight-one object is

`sum_i (-1)^i H_i = sum_(k=2)^(p-1)(p-k)(-1)^k C_k`.

This proves completeness of the geometric configuration list, but not its effective `O(p)` cancellation.

### 4. Exact q-average of the pair survivor

For

`B_p=sum_(q!=0,2) Tr(Frob_p | H^1(B_q)^-)`,

one has `B_5=0`, and for `p>5`:

`B_p=chi(3)(chi(5)-5)/2` if `p=1 mod 4`,

`B_p=chi(3)((3+chi(5))/2-chi(2))` if `p=3 mod 4`.

Therefore

`|B_p|<=3`.

The pair family has linear pointwise rank but bounded total q-trace. It is harmless in the final constant battle.

## Exact audits

All new calculations have reproducible independent audit scripts and committed results.

- Weight-zero finite group audit: PASS at `p=5,7,11,13,17,19`.
- Extremal curve algebra audit: PASS for every admissible q at the same primes.
- Configuration character audit: PASS over every conjugacy class at `p=5,7,11,13,17`.
- Pair q-average direct point-count audit: PASS for every admissible q and every prime `5<=p<=199`.

## Revised frontier

The old target “prove weight-zero collapse” is complete.

The current highest-value targets are now:

1. **D-family total-space theorem.** Evaluate or sharply decompose
   `sum_(q!=0,2) Tr(Frob_p | H^1(D_q))`.
   This is the first remaining explicit linear-rank contribution to the final constant.

2. **Primitive configuration cancellation.** Pair the common semisimple constituents in
   `sum_(k=2)^(p-1)(p-k)(-1)^k C_k`,
   leaving `O(p)` unmatched rank and q-conductor.

3. **Boundary and split/nonsplit assembly.** Add q=2, q=infinity, the Kummer term, and the quadratic descent signs with exact constants.

4. **Positivity ledger.** Determine whether the resulting exact main term dominates the surviving linear constant; finite certification already handles `p<1200`.

## Epistemic classification

- Four results above: exact theorems, with stated dependencies checked.
- Audit outputs: machine-certified finite exact computation.
- Linear total survivor rank suggested by `p=5,7,11`: strong empirical evidence, not yet a theorem.
- Completeness after effective semisimple cancellation: open.
- General-p crown: open.
