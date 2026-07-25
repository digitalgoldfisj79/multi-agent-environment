# Boundary discriminant obstruction and Fourier-projector calibration

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` application main branch.  
**Status:** the boundary discriminant statements are **PROVED**; the displayed calibration is an **EXACT COMPUTER-ASSISTED THEOREM** using the already committed irreducibility counts.

## 0. Notation

For `p=5 mod 6`, let

\[
F_{a,c,d}(X)=X^p+aX^3+cX+d,
\qquad A=\chi(a).
\]

The exact q-line ledger writes

\[
N_A=(p-2)+B_A-\frac{S_0+A S_\chi}{2p},
\]

where

\[
B_A=I_A(\infty)+I_{A\chi(2)}(2).
\]

This note determines one uniform boundary vanishing and tests the simplest proposed identification of the normalized Airy trace with either q-line projector.

## 1. Discriminant of the q=infinity boundary

At `c=0`, put

\[
f(X)=X^p+aX^3+d.
\]

If `d=0`, the polynomial is reducible. Assume `d!=0`. Since

\[
f'(X)=3aX^2,
\]

the resultant is

\[
\operatorname{Res}(f,f')=(3a)^p d^2.
\]

For a monic polynomial of odd degree `p`,

\[
\operatorname{Disc}(f)
=(-1)^{p(p-1)/2}\operatorname{Res}(f,f'),
\]

so its square class is

\[
\boxed{
\chi(\operatorname{Disc}(f))
=
\chi\left((-1)^{(p-1)/2}3a\right).
}
\]

An irreducible separable polynomial of odd prime degree has Frobenius cycle type `(p)`, an even permutation. By the discriminant--Frobenius sign criterion, its discriminant must be a square.

For `p=5 mod 6` and `A=chi(a)=+1`, the displayed square class is always `-1`:

- if `p=5 mod 12`, the sign is positive and `(3/p)=-1`;
- if `p=11 mod 12`, the sign is negative, `(-1/p)=-1`, and `(3/p)=+1`.

Therefore

\[
\boxed{
I_+(\infty)=0
\qquad(p=5\bmod6).
}
\]

This is a uniform exact boundary theorem.

## 2. The split q=2 cell

The split normalized polynomial at `q=2` is

\[
g(X)=X^p+\frac12X^3-\frac32X+\delta.
\]

Its derivative is

\[
g'(X)=\frac32(X^2-1),
\]

and

\[
g(1)=g(-1)=\delta.
\]

Hence

\[
\operatorname{Res}(g,g')
=\left(\frac32\right)^p\delta^2,
\]

and the discriminant square class is

\[
\chi\left((-1)^{(p-1)/2}\frac32\right)
=-\chi(2)
\qquad(p=5\bmod6).
\]

Consequently,

\[
\boxed{
\chi(2)=+1
\quad\Longrightarrow\quad
I_+(2)=0.
}
\]

When `chi(2)=-1`, the discriminant condition is compatible with irreducibility and supplies no vanishing theorem. The observed zeros in that sector require another mechanism.

## 3. Exact calibrated projector table

Using the committed exact class counts and direct boundary enumeration gives:

| `p` | `B_+` | `B_-` | `S_0` | `S_chi` | `T_p / p^((p-3)/2)` |
|---:|---:|---:|---:|---:|---:|
| 11 | 0 | 6 | -44 | -66 | 22 |
| 17 | 0 | 4 | 34 | -136 | 29 |
| 23 | 0 | 6 | 322 | 92 | -561/23 |
| 29 | 0 | 2 | -232 | -290 | -65419/841 |

The separate boundary values are:

| `p` | `I_+(infinity)` | `I_-(infinity)` | `I_+(2)` | `I_-(2)` |
|---:|---:|---:|---:|---:|
| 11 | 0 | 4 | 0 | 2 |
| 17 | 0 | 4 | 0 | 0 |
| 23 | 0 | 2 | 0 | 4 |
| 29 | 0 | 2 | 0 | 0 |

The normalized Airy trace is the trace of

\[
\mathcal R_p\left(\frac{p-1}{2}\right)
\]

on the weight-two scale. It is not equal, with a uniform sign, to either `S_0` or `S_chi` in the calibrated cases. Nor is the discrepancy explained by the two finite boundary counts `B_A`.

For example, at `p=11`,

\[
(S_0,S_\chi)=(-44,-66),
\qquad
T_p/p^4=22,
\]

while at `p=17`,

\[
(S_0,S_\chi)=(34,-136),
\qquad
T_p/p^7=29.
\]

Thus the simplest proposed application identity

> one q-line projector equals the half-twisted Airy trace plus only `q=2` and `q=infinity` corrections

is false.

## 4. Interpretation with the Fourier localization theorem

The exact localization triangle in
`FOURIER_CAYLEY_ZERO_FREQUENCY_OBSTRUCTION_20260725.md` proves that the canonical zero-frequency ambient term has the full twist `(p-7)`, whereas the normalized Airy term has the half twist `(p-7)/2`.

The calibration is consistent with that theorem:

- neither global q-line projector is the canonical zero-frequency Airy trace;
- finite boundary corrections do not repair the mismatch;
- substantial trace remains in the nonzero-frequency Fourier sector.

The table is not used to prove the weight obstruction. It is an independent exact falsification of the simplest projector formula.

## 5. Status

### PROVED

1. `I_+(infinity)=0` for every prime `p=5 mod 6`.
2. `I_+(2)=0` whenever additionally `chi(2)=+1`.
3. The exact reconstruction formulas for `S_0` and `S_chi` from `N_+`, `N_-`, `B_+`, `B_-`.

### EXACT COMPUTER-ASSISTED THEOREM

The complete table for `p=11,17,23,29`, using direct irreducibility certification and the committed exact Airy traces.

### CLOSED

A uniform identification of either `S_0` or `S_chi` with the normalized Airy trace modulo only the two finite boundary cells.

### OPEN

1. The generic nonzero-frequency Fourier contribution.
2. The remaining `chi(2)=-1` split `q=2` vanishing seen in the calibrated cases.
3. The full Airy correlation estimate.
4. The crown.