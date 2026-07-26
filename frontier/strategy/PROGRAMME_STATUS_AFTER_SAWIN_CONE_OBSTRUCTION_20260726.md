# Programme status after the exact Sawin-cone Betti obstruction

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** function-field Fortune `d=1` only.  
**Crown:** **OPEN**.  
**Absolute aggregate Betti route:** **CLOSED**.

## 1. New theorem-level obstruction

Sawin's affine variety for the full four-parameter Fortune interval is

\[
X_{p,p-4,0}=\{e_1=\cdots=e_{p-4}=0\}\subset\mathbf A^p.
\]

It is an `S_p`-equivariant diagonal `A^1` torsor over the affine cone on the smooth sparse projective surface `Y_p`.

For every nontrivial representation `rho`, if `M_rho` is its multiplicity space in `H^2_prim(Y_p)`, then

\[
H_c^5(X)_\rho=M_\rho(-1),
\qquad
H_c^6(X)_\rho=M_\rho(-2).
\]

Therefore

\[
\boxed{B(\rho)=2\dim M_\rho.}
\]

## 2. Exact admitted-prime failure

At `p=11`, the exact compactified primitive profile is

\[
(0,0,0,0,0,6,14,12,6,3,1).
\]

It gives

\[
B_{\mathrm{mid}}=82>10=p-1,
\]

and a full nontrivial-hook contribution `84` to `B_Lambda`.

Hence the condition `B_Lambda<=p-1` remains a correct sufficient condition, but it is false for the actual Fortune variety. The aggregate absolute-Betti strategy cannot prove the crown.

At `p=13`, the exact corresponding contribution is `400>12`.

## 3. Ordinary discriminant audit

Every pair-collision divisor is geometrically irreducible. The component representation of the reduced ordinary discriminant is the permutation module on unordered pairs:

\[
\operatorname{Ind}_{S_2\times S_{p-2}}^{S_p}1
=
S^{(p)}\oplus S^{(p-1,1)}\oplus S^{(p-2,2)}.
\]

Its hook profile is `(1,1,0,...)`. It cannot touch any of the primitive hooks, which begin at degree `5` in the exact regression profiles.

## 4. Correct surviving trace route

The same cone computation gives

\[
E_{\mathrm{mid}}=p(p-1)T_{\mathrm{mid}}(p),
\]

where

\[
T_{\mathrm{mid}}(p)
=
\sum_{i=1}^{p-2}(-1)^i
\operatorname{Tr}
\left(F\mid\operatorname{Hom}_{S_p}
(\wedge^i\mathrm{Std},H^2_{\mathrm{prim}}(Y_p))\right).
\]

Writing

\[
S_{\mathrm{sgn}}=s_p p^2(p-1),
\qquad s_p\in\{0,+1,-1\},
\]

the crown follows from

\[
\boxed{T_{\mathrm{mid}}(p)>-p(p+1+s_p).}
\]

For `p=23 mod 24`, this is the strict threshold

\[
\boxed{T_{\mathrm{mid}}(p)>-p^2.}
\]

## 5. Next theorem

> **Primitive parity Frobenius theorem.** Construct a Frobenius-compatible parity correspondence or Fourier--Cayley identity on the primitive hook multiplicity spaces of `Y_p` and prove the displayed direct trace inequality for every admitted prime.

The exact profiles at `p=11` and `p=13` have equal total even and odd multiplicities. This supports a parity-cancellation strategy, but does not itself control Frobenius.

## 6. Closed routes

Do not continue with:

- attempts to prove `B_Lambda<=p-1`;
- discriminant-Gysin rank targets `31` and `188` as a way to reduce Sawin's actual Betti constant;
- componentwise ordinary lifts of the Jacobian degrees;
- raw terminal-bar mass as the final page;
- larger raw-bar prime sweeps.

## 7. Verification

```bash
python frontier/strategy/discriminant_component_sawin_cone_verify.py
```

Machine-readable output:

```text
frontier/strategy/discriminant_component_sawin_cone_results_20260726.json
```
