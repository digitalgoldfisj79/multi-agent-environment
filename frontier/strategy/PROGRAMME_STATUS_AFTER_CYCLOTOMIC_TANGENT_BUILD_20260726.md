# Programme status after the cyclotomic tangent build

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Crown:** **OPEN**.

## Requested construction

The requested mod-`pi^2` cyclic Fourier object has been constructed at coefficient level.

For `R=Z_p[zeta_p]/(pi^2)`, the additive coefficient character is

\[
\tau\mapsto1+\pi.
\]

It is the unique nonsplit self-extension of the trivial `F_p[C_p]` module. Its Tate complex is

\[
\cdots\to R\xrightarrow{\pi}R\xrightarrow0R\xrightarrow\pi R\to\cdots,
\]

with one-dimensional Tate groups in both parities and nonzero coefficient Bockstein.

## Decisive obstruction

The root-cycle alternating hook class is

\[
\Theta_p=p\mathbf1-\operatorname{Reg}_{C_p}.
\]

Its normalized character `Theta_p/p` is the indicator of nonidentity elements, with character multiplicities

\[
\frac{p-1}{p},\qquad-\frac1p.
\]

It is not an integral virtual character. Therefore no ordinary perfect divided-hook complex exists.

Moreover

\[
p=u\pi^{p-1},
\]

so the raw hook trace places the fixed-class count and first coefficient moment at cyclotomic orders `p-1` and `p`. A raw complex modulo `pi^2` is blind to both.

## Corrected exact object

The first moment is the secondary trace

\[
\boxed{
M_a
\equiv
\frac{\mathcal H_a-pN_a}{p\pi}
\pmod\pi,
}
\]

where `H_a` is the undivided root-hook Fourier trace.

There are only two honest formulations:

1. construct the raw bi-equivariant integral complex modulo `pi^(p+1)` and extract the order-`p` coefficient;
2. construct a root-cycle secondary Hattori--Stallings trace that canonically performs the displayed division and retains the coefficient Bockstein.

## What the tangent build does not supply

The coefficient extension, Tate groups and Bockstein do not determine the required Frobenius tangent. The family

\[
\Phi_\lambda=1+\lambda\pi
\]

has identical modular, Tate and Bockstein data for every `lambda in F_p`, but arbitrary first-order trace coefficient.

Thus the missing datum remains the Frobenius trace on the free root-cycle summand. This is not formal Smith theory.

## Closed continuations

Do not continue with:

- an ordinary perfect mod-`pi^2` divided-hook complex;
- modular Tate localization alone;
- the coefficient Bockstein without a free-orbit Frobenius trace;
- further prime scans;
- discriminant parity or q-line cross-ratio pairing;
- the refuted bounded Cartier-support law.

## Single remaining theorem

> Construct the actual geometric secondary trace, or equivalently the raw integral Fourier/Adams complex through `pi^(p+1)`, and prove that the resulting two square-class first moments cannot both vanish.

This is now the unique continuation of the frozen first-moment route.

## Files

- `CYCLOTOMIC_TANGENT_TATE_COMPLEX_AND_DIVIDED_HOOK_PRECISION_OBSTRUCTION_20260726.md`
- `cyclotomic_tangent_tate_precision_verify.py`
- `cyclotomic_tangent_tate_precision_results_20260726.json`
- `DIVIDED_HOOK_IS_NOT_A_PERFECT_COMPLEX_AND_SECONDARY_TRACE_TARGET_20260726.md`
- `divided_hook_character_secondary_trace_verify.py`
- `divided_hook_character_secondary_trace_results_20260726.json`
