# Main d=1 status after the general weight-zero hook collapse

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only. Papers V and VI remain frozen.

## Ruling

The crown remains open, but Route B has advanced from a computational pattern to a general theorem.

The complete weight-zero part of the exponentially large hook ledger now cancels for every prime. The uncancelled line is exactly the discriminant Kummer character already seen at `p=5,7`. The remaining fixed-`q` obstruction is purely weight one.

## New proved theorem: weight-zero collapse

For

\[
U=\mathbf P^1_t\setminus\{1,-1,\infty\},
\qquad
V_i=\bigwedge^i\operatorname{Std},
\]

the boundary exact sequence and the alternating exterior-power identity give

\[
\sum_i(-1)^i[W_0H_c^1(U,V_i)]^{ss}
=[\mathcal L_{\varepsilon_q}],
\]

where `L_(epsilon_q)` is the discriminant Kummer line

\[
\chi(u_q(t^2-1)).
\]

The proof is an exact p-cycle count:

- `lambda_(-1)(Std)` has trace `p` on a p-cycle and zero on every other permutation;
- a Frobenius coset at either transposition puncture contains no p-cycle;
- the affine inertia coset at infinity contributes `1+epsilon_q^r` on the r-th Frobenius power;
- subtracting the unique global trivial line leaves `epsilon_q^r`.

Thus the statement holds for every Frobenius power and hence as a semisimplified virtual module.

Files:

- `WEIGHT_ZERO_HOOK_COLLAPSE_THEOREM_20260725.md`
- `weight_zero_hook_collapse_verify.py`

The verifier passes at `p=5,7,11,13,17,23`.

## New proved theorem: weight-one end pieces

For the normal-form root cover `t=f_q(z)`:

1. `V_1=Std` has no parabolic weight-one cohomology because the compactified root curve is `P^1_z`.
2. `V_(p-1)=sgn` has no weight-one cohomology because its discriminant double cover is genus zero.
3. `V_2` is the anti-invariant cohomology of the ordered-pair curve
   \[
   3s^2=12-\delta^2-4q\delta^{p-1}.
   \]
   Its Prym has dimension `floor((p-1)/4)`, so the hook rank is
   \[
   2\lfloor(p-1)/4\rfloor.
   \]
4. `V_(p-2)=Std tensor sgn` is
   \[
   H^1(D_q),
   \qquad
   D_q:w^2=u_qg_{q,+}g_{q,-},
   \]
   where `D_q` has genus `p-3` and rank `2p-6`.

File:

- `WEIGHT_ONE_END_PIECES_THEOREM_20260725.md`

This proves an explicit `O(p)` portion of the weight-one survivor for every prime.

## Closed in this push

### Bounded Mellin support

The multiplicative Mellin transform of the local divided-Adams trace has the exact factorisation

\[
\mathcal M_p(\chi)
=-G(\chi)G(\chi^{-1/3})
\sum_{\operatorname{Tr}y=1}
\chi^{1/3}(\operatorname{Tr}(y^3)).
\]

Its support is full at `p=17,23,29,41`; only the quadratic mode vanishes at the exceptional prime `p=11`. The values span the full real cyclotomic field dimension at the calibrated primes. The residual sum is the original cubic linear section, not a bounded-conductor curve.

Files:

- `DIVIDED_ADAMS_MELLIN_FULL_SUPPORT_20260725.md`
- `divided_adams_mellin_probe.py`

### Involution-quotient Cartier shortcut

For

\[
G_{a,c,e}(Y)=Y(Y^{(p-1)/2}+aY+c)^2-e,
\]

the exact cofactor `C_3(G)=3a^2 1_(G irreducible)` was constructed and tested.

- If `p=3 mod 4`, scaling `(c,e)->(-c,-e)` makes the square and nonsquare sectors equal, so square restriction gives no new orthogonality gain.
- If `p=1 mod 4`, a large quadratic `e`-sector survives and increases complexity.

Files:

- `INVOLUTION_QUOTIENT_CARTIER_NO_GAIN_20260725.md`
- `involution_quotient_cartier_probe.py`

### Original Cartier support cutoff

The earlier empirical support law is not live: `D1_PUSH.md` records the exact `p=223` counterexample. This push did not revive that closed route.

## Q-line surface audit

Exact complete q-line traces were computed with

\[
S_r=(p^r-2)p^r-p\sum_q I_r(q).
\]

- At `p=5`, the Kummer, pair and `D` surfaces give exactly `(-5)^r` through `r=4`; there is no middle-hook interval.
- At `p=7`, the complete factor `(1+7T)(1+7T^2)` is validated through `r=4`.
- At `p=11`, an apparent degree-11 factor fitted to `r=1,2` is refuted by the exact third trace `S_3=-7007`.
- The split first trace divided by `p` is not bounded across the prime scan; the invariant/quadratic two-reading projector remains essential.

Files:

- `Q_LINE_SURFACE_ASSEMBLY_AUDIT_20260725.md`
- `qline_global_trace_probe.py`

## Exact remaining object

After removing the proved weight-zero line and the explicit end hooks, the fixed-`q` obstruction is

\[
\boxed{
\mathcal M_q
=
\sum_{i=3}^{p-3}(-1)^i
H^1(\mathbf P^1,j_*\bigwedge^i\operatorname{Std}).
}
\]

At `p=5` it is empty. At `p=7` it is the measured `V_3-V_4` block. It is nonzero and cannot be replaced uniformly by only the pair and `D` curves.

The next theorem must do one of two things:

1. construct a parity-reversing correspondence reducing `M_q` to `O(p)` effective rank and conductor, then assemble its invariant/quadratic q-line projectors; or
2. bypass fixed-`q` effectivity and compute those two global q-line traces directly.

## Analytic wall unchanged

The absolute Airy estimate

\[
|T_p|\le C p^{(p-1)/2}
\]

remains open. The divided-Adams Hasse theorem controls the p-adic initial form, not the archimedean size. The Mellin no-go proves that ordinary bounded-support character diagonalisation does not supply the missing cancellation.

## Scientific position

The push has not proved the crown. It has, however, discharged the first general-p hook-collapse lemma and removed every weight-zero ambiguity. The only remaining Route B uncertainty is now a pure weight-one middle-hook theorem, with the outer `O(p)` curve pieces already explicit.
