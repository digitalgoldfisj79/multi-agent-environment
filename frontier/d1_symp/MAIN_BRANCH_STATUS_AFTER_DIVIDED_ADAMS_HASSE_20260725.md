# Main d=1 status after the divided-Adams Hasse reduction

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only. Papers V and VI remain frozen.

## Ruling

The crown remains open. The resonant `k=p` Dwork programme produced a new exact initial-form theorem but did not prove the required archimedean trace bound.

## Proved resonant trace reduction

For a rank-two Frobenius matrix `A`, let `P:Sym^p -> det tensor Sym^(p-2)` be the canonical mixed-monomial quotient. The divided Frobenius commutator

`C_p(A)=(Sym^p(A)P-P det(A) Sym^(p-2)(A))/p`

is integral, but has generic rank `p-1`. Thus the hoped-for bounded-rank Frobenius collapse is false.

After the canonical mixed-monomial section, its trace is the scalar divided-Adams polynomial

`d_p(A)=(Tr(A^p)-A_11^p-A_22^p)/p`.

For the Airy Frobenius `A(a)`, Hopf--Dwork converts the resonant trace to the Teichmuller sum of this scalar function plus one explicit endpoint correction.

## Hasse coefficient theorem

Write `p=3h+2` and define

`F_h(u)=sum_(n=0)^h (-1)^n u^n /(9^n n! product_(j=0)^(n-1)(3j+4))` in `F_p[u]`.

Put

`H_p = h!/(6((2h+1)!)^2) + (1/h!)[u^h] log F_h(u)`.

The divided-Adams initial-form calculation proves

`v_p(T_p) >= (p+4)/3`

and

`T_p / p^((p+4)/3) = -H_p mod p`.

Therefore `H_p != 0` implies the exact valuation law

`v_p(T_p)=(p+4)/3`.

The logarithmic coefficient is computed by the Rayleigh recurrence. If

`F_h'(u)/F_h(u)=sum_(n>=0) r_n u^n`, then

`r_0=-1/36`,

`(3n+4)r_n=-3 sum_(i=0)^(n-1) r_i r_(n-1-i)`,

and `[u^h]log F_h=r_(h-1)/h`.

## Verification

The deterministic verifier reproduces the exact normalized residues for `p=11,17,23,29,41,47,53` and scans every prime `p=5 mod 6` below `1500`. Only the known exceptional case `p=5`, where `T_5=0`, has vanishing Hasse coefficient in that range.

## Closed mechanisms

- endpoint Frobenius thinning to `O(1)` modes;
- a bounded-rank lift of the modular Adams sequence;
- certified fixed-degree truncation of the resonant `k=p` Dwork complex;
- obtaining the archimedean bound from p-adic divisibility alone.

## Exact remaining theorems

1. Prove or refute `H_p != 0` for every prime `p=5 mod 6`, `p>=11`.
2. Prove the genuinely load-bearing estimate

`|T_p| <= C p^((p-1)/2)`

with absolute `C`.

Even the exact valuation law does not imply this estimate. After dividing by the proved p-power, the missing bound is

`|T_p/p^((p+4)/3)| <= C p^((p-11)/6)`.

The next valid route must therefore control the archimedean cancellation of the scalar divided-Adams trace function, or produce an equivalent bounded-conductor/Jacobi-sum description. Another modular-rank or associated-graded argument cannot close the theorem.
