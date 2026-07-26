# Invariant q-line saturation gap equals the cubic irreducible count

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** fallback invariant q-line route after the fixed-class transfer obstruction.  
**Status:** all identities and equivalences below are **PROVED**. The crown remains **OPEN**.

## 1. Exact q-line ledger

For the two depressed cubic square classes `A=+1,-1`, the proved q-line formula is

\[
N_A
=(p-2)+B_A-rac{S_0+A S_\chi}{2p},
\]

where:

- `N_A` is the complete irreducible count in the class;
- `B_A` is the sum of the `q=2` and `q=infinity` boundary counts;
- `S_0` is the invariant q-line trace;
- `S_chi` is the quadratic anti-invariant trace.

Adding the two classes removes `S_chi`:

\[
N_++N_-
=2(p-2)+B_++B_--\frac{S_0}{p}.
\]

## 2. Saturation-defect theorem

Define the formal saturation value

\[
S_0^{\mathrm{sat}}
=p\bigl(2(p-2)+B_++B_-\bigr).
\]

Then:

### Theorem 2.1

\[
\boxed{
S_0^{\mathrm{sat}}-S_0
=p(N_++N_-).
}
\]

This is simply the exact ledger multiplied by `p`, but it changes the interpretation of the proposed nonsaturation programme.

Since the counts are nonnegative,

\[
\boxed{S_0\le S_0^{\mathrm{sat}}.}
\]

Moreover,

\[
\boxed{
S_0<S_0^{\mathrm{sat}}
\iff N_++N_->0.
}
\]

Thus strict invariant q-line nonsaturation is not a weaker analytic lemma. It is exactly the assertion that at least one depressed cubic class contains an irreducible.

## 3. Quantized gap

For every fixed `c`, the involution `d -> -d` pairs irreducible fibres, and `d=0` is reducible. Hence each `N_A` is even. Therefore:

### Corollary 3.1

\[
\boxed{
S_0^{\mathrm{sat}}-S_0
\in2p\mathbf Z_{\ge0}.
}
\]

The first possible nonsaturated value lies exactly `2p` below saturation. A proof cannot obtain the crown from an arbitrarily small strict real inequality unless it also respects the integral trace normalization that forces this quantum.

Equivalently,

\[
\boxed{
\frac{S_0^{\mathrm{sat}}-S_0}{2p}
=\frac{N_++N_-}{2}
\in\mathbf Z_{\ge0}.
}
\]

## 4. Boundary implication

Each boundary irreducible is included in the corresponding complete class count, so

\[
0\le B_A\le N_A.
\]

If saturation occurs, Theorem 2.1 gives

\[
N_+=N_-=0,
\]

and consequently

\[
B_+=B_-=0.
\]

Thus the hypothetical failure value simplifies automatically to

\[
\boxed{S_0=2p(p-2).}
\]

There is no separate boundary configuration at a failure prime.

## 5. Relation to the complete crown

The aggregate orbit theorem gives

\[
W_p=N_2+\frac{N_++N_-}{2},
\]

and the function-field crown is `W_p>0`.

Using the gap theorem,

\[
\boxed{
W_p
=N_2+rac{S_0^{\mathrm{sat}}-S_0}{2p}.
}
\]

Therefore:

- if the quadratic normal-form count `N_2` is positive, the crown is already proved at that prime;
- when `N_2=0`, strict invariant q-line nonsaturation is exactly equivalent to the full crown;
- simultaneous failure is precisely `N_2=0` and `S_0=S_0^sat`.

## 6. Ruling on congruence-only continuations

The following observations do not advance the theorem:

1. `S_0` is divisible by `p`;
2. the saturation defect is even;
3. `S_0` is an integer Frobenius trace;
4. the anti-invariant trace cancels in the class sum;
5. the boundary terms vanish under hypothetical saturation.

All are already encoded in

\[
S_0^{\mathrm{sat}}-S_0=p(N_++N_-).
\]

A useful q-line theorem must therefore supply a genuinely new one-sided Frobenius estimate, phase-nonsaturation mechanism, or categorical parity reversal. Merely proving a congruence already forced by the ledger cannot distinguish the zero gap from a positive `2p` multiple.

## 7. Exact stopping point

The invariant q-line route remains a possible **proof mechanism**, but its advertised target is not a smaller problem:

\[
\text{strict nonsaturation}
\quad\Longleftrightarrow\quad
\text{cubic-class positivity}.
\]

No existing weight, determinant, valuation, boundary or character-support result in the repository excludes the saturated value. The remaining q-line theorem must contain new arithmetic cancellation rather than another reformulation of the ledger.
