# Exact `p=13` obstruction to the literal `C_wedge` terminal Betti budget

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** diagnostic of the unmodified rank-two quantum-bar page underlying the aggregate `h=4` Betti programme.  
**Status:** the hook-nullity statements below are an **EXACT COMPUTER-ASSISTED THEOREM** over `Q(zeta_13)`. The geometric consequences are exact. Since `p=13` is not in the admitted `p congruent 5 mod 6` sector, this is a model obstruction, not a counterexample to the crown.

## 0. Result

Let `zeta=zeta_13`, put

\[
\eta=-\zeta^{-1},
\]

and let

\[
\Omega_{1,12}(\eta)
=\sum_{j=1}^{13}\eta^{j-1}(j\ j-1\ \cdots\ 1)
\]

act on the hook representations

\[
\bigwedge^r\operatorname{Std}_{13}.
\]

The following characteristic-zero kernel dimensions are exact:

\[
\boxed{
\begin{aligned}
\dim\ker\Omega|_{\wedge^3\mathrm{Std}_{13}}&=2,\\
\dim\ker\Omega|_{\wedge^4\mathrm{Std}_{13}}&=5,\\
\dim\ker\Omega|_{\wedge^5\mathrm{Std}_{13}}&=5,\\
\dim\ker\Omega|_{\wedge^6\mathrm{Std}_{13}}&=5.
\end{aligned}
}
\]

Therefore these four **non-sign** hooks alone contribute

\[
\boxed{2+5+5+5=17.}
\]

The multiplicity-one Sawin budget at `p=13` would be

\[
p-1=12.
\]

Hence

\[
\boxed{17>12.}
\]

In the doubled `C_wedge` model, the same four hooks already contribute at least

\[
34>24=2(p-1),
\]

before the sign hook is included.

## 1. Why this is the full terminal first-homology operator

The twist `eta` has order `26`. For every total degree `2<=i<=12`,

\[
26\nmid i(i-1).
\]

Thus every lower quantum-shuffle multiplication is nonresonant. Exactly as in the `p=11` proof,

\[
\sum_{a=1}^{12}A_aA_{13-a}=A_1A_{12},
\]

and

\[
H_1(B_{13}(A))=\operatorname{coker}\Omega_{1,12}(\eta).
\]

The displayed hook kernels are therefore actual terminal indecomposable classes, not artefacts of selecting one multiplication map.

## 2. Exact certificate

`p13_cwedge_budget_obstruction_verify.py --exact` proves the four nullities by the same certificate architecture used at `p=11`:

1. compute canonical left kernels for every Galois embedding of `zeta_13` in several auxiliary prime fields;
2. interpolate into the power basis of `Q(zeta_13)`;
3. combine reductions by CRT;
4. apply rational reconstruction;
5. clear denominators;
6. verify the lifted kernel vectors exactly in
   \[
   \mathbf Z[x]/(1+x+\cdots+x^{12});
   \]
7. use a matching nonzero modular maximal minor to prove no additional characteristic-zero rank loss.

The exact certificate denominators are

| hook degree | exact nullity | common denominator |
|---:|---:|---:|
| 3 | 2 | 7787 |
| 4 | 5 | 6071 |
| 5 | 5 | 27659567 |
| 6 | 5 | 53205883679 |

The quick verifier independently reproduces the same profile modulo three auxiliary primes.

## 3. Scientific consequence

The `p=11` calculation had suggested that, after removing the sign hook, the literal multiplicity-one terminal `C_wedge` mass might equal the Sawin budget `p-1`.

The exact `p=13` result disproves that as a uniform algebraic pattern.

Even after sign removal, the unmodified rank-two terminal bar page can carry substantially more homology than the Sawin budget. Therefore the desired Betti-compatible comparison cannot consist only of:

1. taking the terminal `C_wedge` bar homology;
2. deleting the sign representation;
3. descending by the formal multiplicity-two factor.

At least one additional sparse-geometric mechanism is mandatory:

- a differential created by the Fourier sparse section;
- a quotient imposed by the coefficient constraints;
- a weight exclusion preventing some bar classes from entering Sawin's non-top compactly supported cohomology;
- an arithmetic projector killing whole hook sectors.

At `p=13`, any multiplicity-one comparison must remove at least

\[
17-12=5
\]

of the classes already visible in hook degrees `3` through `6`.

## 4. Scope caveat

The function-field half-theorem programme currently targets primes

\[
p\equiv5\pmod6.
\]

Since `13 congruent 1 mod 6`, the present theorem does not refute a comparison that uses arithmetic specific to the admitted sector. It does refute any proposed **uniform, unmodified** `C_wedge` terminal-budget theorem.

The first larger admitted diagnostic is `p=17`. Modular calculations at two independent auxiliary primes give

\[
\dim\ker(\wedge^3)=2,
\qquad
\dim\ker(\wedge^4)=8.
\]

These values are diagnostic only; they have not yet been promoted to characteristic-zero theorems, and their sum `10` does not by itself exceed the admitted budget `16`.

## 5. Revised active theorem

The active theorem is no longer merely sign/discriminant absorption.

> **Sparse-section terminal cancellation theorem.** Construct the parity-separated Fourier--Cayley/Rees comparison from the full configuration-space quantum-bar object to the sparse four-parameter interval complex. Identify the additional differentials, quotients, weight truncations and arithmetic projectors created by the sparse section, and prove that their surviving multiplicity-one non-top mass is at most `p-1` in the admitted sector. Treat the sign hook by the exact trace formula of `SIGN_HOOK_FULL_INTERVAL_TRACE_20260726.md`.

The `p=13` exact classes provide the first concrete regression target for that theorem: a valid sparse comparison must explain where at least five non-sign terminal dimensions go.

## 6. Ruling

The exact `p=11` sign overage was real but exceptional as a complete explanation. The next wall is now sharper:

\[
\boxed{
\text{the sparse Fourier section must cancel genuine non-sign terminal bar homology.}
}
\]

This is a theorem-level geometric obstruction, not a remaining normalization issue.
