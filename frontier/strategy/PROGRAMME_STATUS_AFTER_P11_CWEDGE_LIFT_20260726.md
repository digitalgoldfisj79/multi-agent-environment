# Programme status after the exact `p=11` `C_wedge` lift

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Target:** function-field Fortune crown at `d=1`.  
**Status:** the `p=11` terminal-rank uncertainty is closed. The crown remains **OPEN**.

## 1. Authoritative full-interval target

For Sawin's aggregate even/odd hook representations,

\[
B_\Lambda=B(\pi_+)+B(\pi_-),
\]

the exact sufficient theorem remains

\[
\boxed{B_\Lambda\le p-1.}
\]

At `p=11`, the budget is `10`.

## 2. Completed phase

The terminal first bar homology of the full rank-two `C_wedge` model has now been computed exactly over `Q(zeta_11)`.

The hook-kernel profile for the single load-bearing shuffle operator is

\[
(d_0,\ldots,d_{10})=(0,0,1,1,1,3,3,1,0,0,1).
\]

Hence:

\[
\sum d_i=11,
\qquad
\sum_{i\ even}d_i=6,
\qquad
\sum_{i\ odd}d_i=5.
\]

Because `C_wedge^{tensor 11}` contains two copies of every hook,

\[
\boxed{\dim H_1(C_\wedge)=22.}
\]

This is an exact characteristic-zero result, certified by Galois interpolation, CRT, rational reconstruction, exact multiplication in `Z[zeta_11]`, and matching modular minors.

## 3. New structural reduction

All lower total degrees are nonresonant. Therefore every lower-degree component of the quantum shuffle algebra is generated on the left by degree one. Associativity implies

\[
\sum_{a=1}^{10}A_aA_{11-a}=A_1A_{10}.
\]

Thus the calculation of `coker Omega_{1,10}` is the complete terminal `H_1`, not a bound from one selected multiplication map.

## 4. Exact location of the overage

The final hook is

\[
\bigwedge^{10}\operatorname{Std}_{11}=\operatorname{sgn},
\]

and contributes exactly one dimension. Therefore

\[
\sum_{i=0}^{9}d_i=10=p-1.
\]

In the doubled `C_wedge` model, the two-dimensional overage

\[
22-20=2
\]

is exactly accounted for by the two copies of the sign-hook class.

This does not yet prove that the sign class disappears from Sawin's sparse interval variety. It identifies the only terminal class that must be killed, quotiented or evaluated separately in the first load-bearing case.

## 5. Active phase

The active theorem is now:

> **Sign/discriminant absorption theorem.** In the parity-separated sparse Fourier--Cayley/Rees comparison, prove that the terminal sign-hook class is either removed by a canonical differential, quotient or weight exclusion, or splits off as an explicitly evaluable discriminant trace that need not be charged to the absolute Betti error budget.

The sign hook is the discriminant-character sector because, for squarefree polynomials, the sign of Frobenius equals the quadratic character of the discriminant.

## 6. Dependency order

1. **Completed:** exact Sawin target `B_Lambda<=p-1`.
2. **Completed:** virtual-to-Betti no-go.
3. **Completed:** exact `p=11` characteristic-zero terminal profile.
4. **Active:** determine the geometric/arithmetic fate of the sign class.
5. Construct the parity-separated sparse Rees filtration after sign extraction.
6. Prove the remaining associated-graded mass is at most `p-1` uniformly in `p`.
7. Descend from doubled `C_wedge` to the multiplicity-one Sawin complexes.
8. Conclude the aggregate Betti bound and the crown.

## 7. Stop rule

Do not return to:

- scalar virtual Airy transport as a Betti bound;
- generic fixed-class `h=2` Weil estimates;
- empirical density recentering without a top-weight theorem;
- larger prime censuses without a mechanism-discriminating prediction.

The next useful work is a direct sign-isotypic calculation on the sparse interval/Fourier complex.
