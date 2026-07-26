# Revised aggregate `h=4` Betti programme after the Sawin, sign and `C_wedge` audits

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Target:** function-field Fortune crown at `d=1`.  
**Status:** programme updated after exact `p=11`, exact sign-trace and exact `p=13` calculations. The crown remains open.

## 0. Authoritative target

For the full four-parameter interval

\[
\mathcal I_4=
\{T^p-T+aT^3+bT^2+cT+d:(a,b,c,d)\in\mathbf F_p^4\},
\]

let

\[
\pi_+=\bigoplus_{i\ \mathrm{even}}\bigwedge^i\mathrm{Std}_p,
\qquad
\pi_-=\bigoplus_{i\ \mathrm{odd}}\bigwedge^i\mathrm{Std}_p,
\]

and

\[
B_\Lambda=B(\pi_+)+B(\pi_-).
\]

Sawin's estimate and the exact weighted-count identity prove that

\[
\boxed{B_\Lambda\le p-1}
\]

is sufficient for the `d=1` crown.

## 1. Completed corrections

1. `B(pi)` is defined for aggregate representations; there is no per-hook counting lower bound.
2. The fixed-class `h=2` package is unsuitable for a generic absolute Betti estimate.
3. Virtual Pascal/Airy identities do not bound unsigned Betti mass.
4. The scalar two-line quantum-bar theorem does not imply a small rank-two aggregate page.
5. The exact degree-one local factor is evidence for a singular series, not a proved replacement main term.

## 2. Exact sign-hook theorem

The sign factorization-function trace on the complete interval is

\[
\boxed{
S_{\mathrm{sgn}}(p)
=
\frac{1-\chi(-1)}2\chi(-6)p^2(p-1).
}
\]

For admitted primes:

\[
S_{\mathrm{sgn}}(p)=
\begin{cases}
0,&p\equiv5,17\pmod{24},\\
+p^2(p-1),&p\equiv11\pmod{24},\\
-p^2(p-1),&p\equiv23\pmod{24}.
\end{cases}
\]

After removing trivial and sign hooks, let `B_mid` denote the remaining aggregate Betti constant. A bound

\[
B_{\mathrm{mid}}\le p-1
\]

closes the residue classes `5`, `11` and `17 mod 24`. In the class `23 mod 24`, it reduces the problem to excluding saturation of the triangle bound.

## 3. Exact terminal-bar results

### `p=11`

The exact hook-kernel profile is

\[
(0,0,1,1,1,3,3,1,0,0,1).
\]

Deleting the unique sign hook leaves total multiplicity-one mass

\[
10=p-1.
\]

### `p=13`

Exact cyclotomic certificates give

\[
\dim\ker(\wedge^3)=2,
\quad
\dim\ker(\wedge^4)=5,
\quad
\dim\ker(\wedge^5)=5,
\quad
\dim\ker(\wedge^6)=5.
\]

These four non-sign hooks alone contribute

\[
17>12=p-1.
\]

Thus the `p=11` sign-only reconciliation is not a uniform feature of the raw configuration-space bar complex.

## 4. Closed raw-bar route

The following proposed mechanism is false:

> take the full `C_wedge` terminal bar homology, delete the sign hook, divide by multiplicity two, and obtain the Sawin budget.

It fails exactly at `p=13` before the remaining hooks are counted.

The failure does not refute the admitted crown because `13` is not `5 mod 6`. It proves that any valid proof must use geometry introduced by the sparse interval section rather than the unmodified full configuration-space bar object.

## 5. Active theorem

> **Sparse-section terminal cancellation theorem.** Construct a parity-separated, Frobenius-compatible Rees filtration from the wild nonzero-frequency Fourier--Cayley complex of the sparse four-parameter interval to the full configuration-space quantum-bar object. Determine the additional differentials, quotients, weight exclusions and arithmetic projectors created by the sparse section. After exact sign extraction, prove that the surviving multiplicity-one non-top associated-graded mass is at most `p-1` for `p congruent 5 mod 6`.

A valid construction must pass the exact regression:

- at `p=11`, account for the sign class;
- at `p=13`, remove at least five non-sign dimensions already present in hook degrees `3` through `6`.

The second regression prevents a proposed comparison from succeeding merely by reproducing the full `C_wedge` bar page.

## 6. Marginal admitted class

For

\[
p\equiv23\pmod{24},
\]

the exact sign trace is negative and a `p-1` mid-hook mass bound lands exactly at the weighted threshold. One additional nonsaturation input is required:

\[
E_{\mathrm{mid}}>-(p-1)p^3.
\]

It is enough to prove any one of:

1. `B_mid<=p-2`;
2. one lower-weight surviving class;
3. one Frobenius phase not aligned with the extremal negative phase;
4. a congruence excluding equality.

## 7. Dependency order

1. **Completed:** Sawin audit and exact aggregate target.
2. **Completed:** virtual-to-Betti no-go.
3. **Completed:** exact `p=11` cyclotomic terminal profile.
4. **Completed:** exact full-interval sign trace.
5. **Completed:** exact `p=13` non-sign raw-bar obstruction.
6. **Active:** construct the sparse-section differential/quotient and test it against `p=11` and `p=13`.
7. Prove the admitted-sector associated-graded mass bound.
8. Prove nonsaturation for `p congruent 23 mod 24`.
9. Insert the resulting trace bound into Sawin's weighted inequality and conclude the crown.

## 8. Stop rule

Do not spend the main programme on larger unmodified raw-bar profiles, scalar virtual transport, fixed-class absolute Weil estimates, empirical recentering or integer Fortune. The next mathematical advance must explain the sparse-section cancellation itself.
