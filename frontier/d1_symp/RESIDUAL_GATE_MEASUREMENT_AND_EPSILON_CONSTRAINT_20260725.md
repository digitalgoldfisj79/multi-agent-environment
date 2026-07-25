# Measuring the residual gate and the p-adic constraint on the transport sign

**Date:** 2026-07-25  
**Branch:** `gpt56/airy-gaussian-independent-audit-20260725`  
**Scope:** the conditional ledger gate after the actual Pascal oscillator theorem.  
**Status:** the finite measurements and gate arithmetic are confirmed. The residual gate is the original q-line main-term problem, and a nonzero Airy coefficient requires a Tate-normalized virtual residual with an exact denominator.

## 1. Independent checks

Both new verifiers pass independently:

- `pascal_actual_oscillator_verify.py`: block theorem through odd primes `p<=199`, exact `p=11` sum `121=11^2`, punctured sum `120`, and zero ordinary Hessian of the nonlinear high phase;
- `terminal_quantum_bar_verify.py`: terminal homology `{1:1,2:1}` at `p=3,5,7,11`.

The ledger identity

\[
N_A=C_A-\frac{S_A}{2p},
\qquad
C_A=p-2+B_A,
\]

and the implication

\[
|S_A|<2p\min(C_A,2p-C_A)
\Longrightarrow
0<N_A<2p
\]

are exact.

## 2. Exact finite measurement of `E_A`

Every ingredient is committed at

\[
p=11,17,23,29,53,71.
\]

For each `epsilon_A in {0,+1,-1}`, define

\[
E_A=S_A-\epsilon_A p\rho_p,
\qquad
p\rho_p=\frac{T_p}{p^{(p-3)/2}}.
\]

The sufficient Airy-subtracted inequality holds at every committed prime for every `epsilon_A`, except the marginal case

\[
p=11,\quad A=+1,\quad\epsilon_A=+1,
\]

where `132` exceeds the strict threshold `131.7`.

The raw tolerance usage

\[
\max_A\frac{|S_A|}{2p d_A}
\]

is

| `p` | 11 | 17 | 23 | 29 | 53 | 71 |
|---|---:|---:|---:|---:|---:|---:|
| usage | `0.56` | `0.33` | `0.43` | `0.33` | `0.25` | `0.10` |

This is calibration only; it is not an asymptotic estimate.

## 3. The residual gate is not a smaller theorem

When `B_A=0`,

\[
S_A=2p(p-2-N_A),
\]

so

\[
\boxed{
|S_A|<2p d_A
\iff
|N_A-(p-2)|<p-2.
}
\]

Because the Airy contribution is `O(p^(3/2))=o(p^2)`, requiring `E_A=o(p^2)` is equivalent at the main scale to

\[
\boxed{N_A-(p-2)=o(p)}
\]

when `B_A=0`. In general the centre is `p-2+B_A`; the same reduction holds if `B_A=o(p)`.

The observed deviations are of square-root size:

| `p` | 11 | 17 | 23 | 29 | 53 | 71 |
|---|---:|---:|---:|---:|---:|---:|
| `A=+1` | `5` | `3` | `9` | `9` | `5` | `3` |
| `A=-1` | `1` | `5` | `5` | `1` | `13` | `7` |

They are consistent with the original `D1_ATTACK.md` picture of a count of order `p` fluctuating on scale `sqrt(p)`.

The Pascal and quantum-bar theorems therefore deliver the terminal skeleton and retire the absolute Airy bound as a prerequisite. They do not bound the q-line deviation.

## 4. Exact p-adic valuation

The proved valuation is

\[
v_p(T_p)=\frac{p+4}{3}.
\]

Hence

\[
\boxed{
v_p(p\rho_p)
=\frac{p+4}{3}-\frac{p-3}{2}
=-\frac{p-17}{6}.
}
\]

The exact valuations at the six committed primes are

\[
\boxed{1,\ 0,\ -1,\ -2,\ -6,\ -9}
\]

for `p=11,17,23,29,53,71`. The earlier prose value `0` at `p=11` was a transcription error; the formula and verifier give `1`.

Thus `p rho_p` is not a `p`-adic integer for `p>17`.

## 5. Integrality dichotomy

Suppose

\[
S_A=\epsilon_A p\rho_p+E_A.
\]

### If `E_A` is an untwisted integral trace

If `E_A` is the trace of an honest untwisted q-line or boundary complex, then it is algebraically integral. Since `S_A` is an integer, negative valuation of `p rho_p` forces

\[
\boxed{\epsilon_A=0\qquad(p>17).}
\]

Under this interpretation the Airy term does not occur in either raw arithmetic projector.

### If `E_A` is a Tate-normalized virtual trace

A nonzero `epsilon_A` is possible only when `E_A` carries the compensating denominator

\[
\boxed{v_p(E_A)=-\frac{p-17}{6}.}
\]

The exponent bookkeeping is consistent. The Kummer bridge gives

\[
\operatorname{Tr}(F\mid\mathcal D_p)=\frac{T_p}{p^2},
\]

and the oscillator twist is

\[
m=\frac{p-7}{2}.
\]

Therefore

\[
\operatorname{Tr}(F\mid\mathcal D_p(m))
=\frac{T_p}{p^{2+m}}
=\frac{T_p}{p^{(p-3)/2}}
=p\rho_p,
\]

because

\[
2+m=\frac{p-3}{2}.
\]

There is no unresolved exponent gap. The unresolved issue is categorical: the bridge must state whether its residual is raw and integral or Tate-normalized and virtual, and it must exhibit the compensating twists explicitly.

Scalar data alone cannot decide `epsilon_A`; it only imposes this exact valuation constraint.

## 6. Repository hygiene

Corrected commit `55adf068773c88f81790b295165c417a627c8076` and measurement commit `89467e2ceb63cd703ad545d15f12d3b10cd755d2` were merged into the PR #17 head at

`c6334d34d837d89d8d993b6d41c10f8744a3ebef`.

The false global-unboundedness ruling, the characteristic-3 version of Lemma 5.1, and the scalar `(M_p,S_p)` fitting recommendation are no longer present on the PR branch.

## 7. Verification

`residual_gate_measurement_verify.py` recomputes `p rho_p` exactly, reconstructs `N_A` from the committed ledger, evaluates every `E_A`, and asserts

\[
v_p(p\rho_p)=-(p-17)/6.
\]