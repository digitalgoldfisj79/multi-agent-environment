# Measuring the residual gate, and a p-adic constraint on the transport sign

**Date:** 2026-07-25
**Branch:** `claude/airy-next-after-circularity-8jlrek`
**Scope:** the conditional ledger gate of `CONDITIONAL_LEDGER_GATE_AFTER_ACTUAL_PASCAL_OSCILLATOR_20260725.md`.
**Status:** the gate arithmetic is confirmed. Two observations follow from measuring `E_A` on committed data, which had not been done.

## 1. What was checked

Both new verifiers were run independently and pass:
`pascal_actual_oscillator_verify.py` (42 primes to 199; `p=11` oscillator sum
`121 = 11^2`, punctured `120`; joint order `>= 5` with zero ordinary Hessian)
and `terminal_quantum_bar_verify.py` (`p = 3,5,7,11`, terminal homology
`{1:1, 2:1}`).

The gate arithmetic is also confirmed. With `C_A = p-2+B_A`,
`d_A = min{C_A, 2p-C_A}` and `N_A = C_A - S_A/(2p)`, the chain
`|S_A| < 2p d_A` `=>` `0 < N_A < 2p`, and
`|E_A| < 2p d_A - 2(p-1) sqrt p` after subtracting the Airy term, is correct.
`N_A` is a non-negative integer at all six committed primes.

## 2. `E_A` is exactly computable, and the gate already passes

`S_A = S_0 + A S_chi` is committed at `p = 11,17,23,29` and (via `N_+`, `N_-`)
at `p = 53,71`; `p rho_p = T_p/p^((p-3)/2)` is exactly computable. So
`E_A = S_A - eps_A p rho_p` is exact for each `eps_A in {0,+1,-1}`.

Result: **the sufficient condition holds at every committed prime, for every
`eps_A`, with one marginal exception** (`p=11`, `A=+1`, `eps=+1`, giving
`132` against a threshold of `131.7`). The margin then widens rapidly. Usage
of the tolerance `2p d_A` is

| `p` | 11 | 17 | 23 | 29 | 53 | 71 |
|---|---:|---:|---:|---:|---:|---:|
| `max_A |S_A| / 2p d_A` | `0.56` | `0.33` | `0.43` | `0.33` | `0.25` | `0.10` |

## 3. The gate unwinds to the original main-term statement

The sufficient condition `|S_A| < 2p d_A` is *identically* `0 < N_A < 2p`,
i.e. `|N_A - C_A| < d_A` where the deviation is `|S_A|/(2p)`. When `B_A = 0`
this reads `|N_A - (p-2)| < p-2`; `B_+ = 0` is proved uniformly, and
`B_- = 0` holds at `p = 53,71`, but **`B_- = 6,4,6,2` at `p = 11,17,23,29`**,
so the `A=-1` threshold there is `d_- = min(C_-, 2p-C_-)`, not `p-2`.

Deviation `|S_A|/(2p)` against its own threshold `d_A`:

| `p` | 11 | 17 | 23 | 29 | 53 | 71 |
|---|---|---|---|---|---|---|
| dev `A=+1` | `5` | `3` | `9` | `9` | `5` | `3` |
| `d_+` | `9` | `15` | `21` | `27` | `51` | `69` |
| dev `A=-1` | `1` | `5` | `5` | `1` | `13` | `7` |
| `d_-` | `7` | `15` | `19` | `29` | `51` | `69` |
| `1.5 sqrt p` | `5.0` | `6.2` | `7.2` | `8.1` | `10.9` | `12.6` |

**Correction.** An earlier version of this table gave `p-2` as the threshold
for both classes and reported `N_- = 8, 10` at `p = 11, 17`. That used
`B_- = 0`, which is false at those primes. The correct counts are

\[
N_-=14,\,14,\,22,\,28\quad(p=11,17,23,29),
\]

verified by direct census below. The deviations and the `d_A` column in
`residual_gate_measurement_verify.py` were already correct; only this prose
table was wrong.

### Independent census

The ledger was checked against a direct count, not merely re-read. For
`f = X^p + aX^3 + cX + d` one has `X^p = -(aX^3+cX+d) mod f`, so the Frobenius
is composition with a **fixed cubic** and `f` is irreducible iff
`phi^{o p}(X) = X mod f` and `f` has no root in `F_p`. This makes each test
`O(p^3)` rather than generic modular exponentiation. The resulting census
reproduces `N_A = C_A - S_A/(2p)` exactly at `p = 11,17,23,29` for both
classes (`14,14 / 18,14 / 12,22 / 36,28`), independently confirming both the
ledger and the committed `S_0, S_chi, B_A`. Extending the census past `p = 71`
with this algorithm is the concrete way to test whether the deviation really
grows like `sqrt p`.

This should be stated plainly in the programme status: **the residual gate is
not a new, easier problem.** It is the original error-versus-main-term
statement in its sharpest form. Among `p^2` polynomials each irreducible with
probability `~1/p`, the count has mean `~p` and standard deviation `~sqrt p`;
the observed deviations are `1..13` against `1.5 sqrt p = 5.0..12.6`, entirely
consistent. Failure needs a `~sqrt p`-sigma fluctuation, exactly as
`D1_ATTACK.md` said at the outset.

What the Pascal and quantum-bar theorems genuinely deliver is the *terminal
skeleton* of the object and the retirement of the Airy boulder. They do not
bound the deviation, and no reformulation so far has made that bound easier.

## 4. A p-adic constraint on `eps_A` that has not been recorded

`S_A` is a rational integer. But `p rho_p = T_p/p^((p-3)/2)` is **not** a
`p`-adic integer for `p > 17`. Using the proved valuation
`v_p(T_p) = (p+4)/3`,

\[
v_p\!\left(p\rho_p\right)=\frac{p+4}3-\frac{p-3}2=-\frac{p-17}6,
\]

confirmed exactly at all six primes (`0, 0, -1, -2, -6, -9` for
`p = 11,17,23,29,53,71`, against `-(p-17)/6 = -(-1), 0, 1, 2, 6, 9`).

Therefore, if `eps_A != 0`, then

\[
\boxed{\ v_p(E_A)=-\frac{p-17}6\ }
\]

exactly: the complementary complex must carry a Tate twist supplying precisely
that growing `p`-power denominator. This is a hard, checkable constraint on the
bridge that is currently unstated, and it forces a dichotomy:

- **If `E_A` is an ordinary integer** — as it would be if the complementary
  object is assembled from honest `q`-line and boundary point counts — then
  `eps_A = 0` is forced for every `p > 17`. The Airy constituent then does not
  appear in either arithmetic projector, `S_A = E_A`, and **the entire Airy
  input is irrelevant to the crown.** That would be a major structural finding,
  and would explain why the transport has resisted construction.
- **If `E_A` is a twisted trace**, its denominator must match
  `p^((p-17)/6)` on the nose. Since the Pascal oscillator twist is
  `m = (p-7)/2`, there is room, but the normalisation
  `Tr(F | D_p(m)) = T_p/p^((p-3)/2)` divides by `p^((p-3)/2)` rather than
  `p^m`, and the discrepancy between `(p-3)/2` and `(p-7)/2` should be
  reconciled explicitly before the gate is relied on.

**Recommended check, cheap and decisive:** state which of the two holds. If the
first, the conditional gate is vacuous in its Airy term and the programme
should say so; if the second, verify the twist bookkeeping against
`v_p(E_A) = -(p-17)/6` at `p = 23, 29, 53, 71`, where every quantity is
already committed.

## 5. Repository hygiene

The branch head `c4d0432` is built on `06b5fc0`, **not** on the corrected
`55adf06`. It therefore still carries, in
`AIRY_GAUSSIAN_LAW_AND_TARGET_FALSIFICATION_20260725.md`:

- the title and section 3 ruling asserting the target "is false", which the
  independent audit itself required be demoted to the finite exclusion
  `C < 4.8468292139`;
- **Lemma 5.1 stated for "every odd prime", which is false at `p = 3`**, where
  `Tr(x^3) = (Tr x)^3 = Tr(x)` vanishes identically on `ker Tr`;
- the withdrawn recommendation to obtain `(M_p, S_p)` by scalar fitting.

`55adf06` should be merged before PR #17 is merged, or the false lemma enters
the main line.

## 6. Verification

`residual_gate_measurement_verify.py` recomputes `p rho_p` exactly from the
committed `T_p`, reproduces `N_A` from `S_0`, `S_chi`, `B_A` at all six primes,
evaluates `E_A` for each `eps_A`, and asserts the valuation identity
`v_p(p rho_p) = -(p-17)/6`.
