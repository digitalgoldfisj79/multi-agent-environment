# Exact q-line surface assembly audit after weight-zero collapse

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** generic split normal-form q-line; all statements labelled computational are exact finite-field computations.  
**Status:** the weight-zero theorem and the weight-one end-piece identifications are proved separately. This note records the exact global trace experiments that locate the remaining middle-hook obstruction.

## 1. Complete generic q-line trace

For `Q=p^r`, let `I_r(q)` be the number of `t in F_Q` for which

\[
qz^p+z^3-3z-(q-2)t
\]

is irreducible of degree `p` over `F_Q`. The fixed-cell hook identity gives

\[
E_r(q)=Q-pI_r(q).
\]

Therefore the complete split generic q-line trace is

\[
\boxed{
S_r^{split}
=\sum_{q\in F_Q\setminus\{0,2\}}E_r(q)
=(Q-2)Q-p\sum_q I_r(q).
}
\]

Script: `qline_global_trace_probe.py`.

## 2. Exact small-prime power traces

The following values were obtained by exact factorisation over the indicated extension fields.

| `p` | `S_1` | `S_2` | `S_3` | `S_4` |
|---:|---:|---:|---:|---:|
| 5 | `-5` | `25` | `-125` | not needed |
| 7 | `-7` | `35` | `-343` | `2499` |
| 11 | `-11` | `231` | `-7007` | — |
| 13 | `39` | `-559` | — | — |
| 17 | `51` | `-765` | — | — |
| 23 | `69` | — | — | — |

At `p=7`, the four traces agree exactly with the degree-three factor

\[
(1+7T)(1+7T^2),
\]

whose Frobenius eigenvalues are

\[
-7,\quad +\sqrt{-7},\quad-\sqrt{-7}.
\]

The fourth-power census covered all

\[
(q,t)\in(\mathbf F_{7^4}\setminus\{0,2\})\times\mathbf F_{7^4}
\]

and returned

\[
S_4=2499=7^4+2\cdot7^2.
\]

This is an out-of-sample validation of the factor, not a fit to the first three traces.

At `p=11`, the first two traces are consistent with

\[
(1+11T)(1-11T^2)^5,
\]

but the independent third trace is

\[
S_3=-7007\ne-11^3.
\]

Thus the low-degree q-line factor at `p=5,7` is exceptional and does not extend uniformly.

## 3. End-piece surface assembly

The proved weight-one end pieces are:

- the discriminant Kummer line `epsilon_q`;
- the pair-curve Prym `B_q` from `V_2`;
- the hyperelliptic discriminant-twist curve `D_q` from `V_(p-2)`.

For `p=5`, the middle-hook interval is empty and exact point counts give

\[
\sum_{q\ne0,2}
\left(\varepsilon_q^r+a_r(B_q)-a_r(D_q)\right)
=(-5)^r
\]

for `r=1,2,3,4`. In particular the complete generic q-line surface has only one surviving Tate eigenvalue in this base case.

For `p=7`, the same end pieces give

| `r` | Kummer + pair - D |
|---:|---:|
| 1 | `-1` |
| 2 | `-11` |
| 3 | `-1009` |

whereas the full q-line traces are `-7,35,-343`. Therefore the exact middle-hook q-line traces begin

\[
\boxed{
-6,\quad46,\quad666.
}
\]

The middle block is already nonzero at `p=7`; the complete `p=5` pair/D description cannot be the general theorem.

## 4. First-trace scan

For `p=5 mod 6`, the normalized split trace

\[
S_1^{split}/p=(p-2)-\sum_qI_1(q)
\]

was computed exactly through the following initial primes:

\[
-1,-1,3,3,-7,11,1,7,7,7,-17,13,23,7,\ldots
\]

for

\[
p=5,11,17,23,29,41,47,53,59,71,83,89,101,107,\ldots
\]

The value is much smaller than the raw `O(p)` normalized conductor scale at these primes, but it is not bounded and does not obey a finite-state congruence law visible in the data. The scan was stopped once this no-go was clear.

The crown uses the invariant/quadratic combination of the split and nonsplit readings, not the split trace alone. Hence this scan is diagnostic only.

## 5. Ruling

### Proved elsewhere in this push

1. All weight-zero hook cohomology cancels except the discriminant Kummer line.
2. `V_1` and `V_(p-1)` have no weight-one part.
3. `V_2` is the explicit pair-curve Prym.
4. `V_(p-2)` is the explicit genus-`p-3` curve `D_q`.

### Exact computational conclusions

1. The p=5 q-line surface is entirely algebraic after the pair/D decomposition.
2. The p=7 complete q-line factor is genuinely degree three and validated through four powers.
3. The analogous low-degree proposal fails at p=11.
4. The middle-hook q-line block is nonzero from p=7 onward.

### Remaining theorem

The load-bearing object is now precisely

\[
\mathcal M_q
=
\sum_{i=3}^{p-3}(-1)^i
H^1(\mathbf P^1,j_*\bigwedge^i\operatorname{Std}),
\]

assembled with both arithmetic q-line projectors. One must either:

- construct a parity-reversing correspondence reducing `M_q` to `O(p)` effective rank and conductor; or
- bypass fixed-q effectivity and compute its invariant/quadratic q-line trace directly.

The weight-zero and end-piece parts no longer contribute uncertainty.
