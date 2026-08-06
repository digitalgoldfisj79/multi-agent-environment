# Replacement Papers V–VI: theorem reconstruction and direct `d=1` closeout

**Date:** 4 August 2026  
**Authoritative sources:** replacement manuscripts on `publication/fortune-papers-ii-vi-20260724`  
**Scope:** theorem ledger, independent computational reconstruction, dependency audit and terminal-theorem identification

## Executive result

The replacement Papers V–VI form a coherent direct function-field `d=1` reduction programme. Their algebraic identities and finite regression packages reproduce. They do not prove the universal crown.

Both papers terminate at the same statement:

\[
N_{\mathrm{sq}}+N_{\mathrm{ns}}>0
\]

when the quadratic sector fails. Equivalently, the invariant q-line trace must be strictly below its exact saturation value, or the specific Kummer quotient open must have a rational point.

No result in Paper VII supplies this theorem, and no function-field-to-integer transfer is present.

## Paper V reconstruction

### Authoritative replacement

The general-window manuscript `paper5_function_fields/manuscript.md` is superseded. The authoritative paper is

`paper5_function_fields_replacement/manuscript.md`.

### Theorem ledger

| Claim | Status | Reconstruction ruling |
|---|---|---|
| Proposition 2.1: reducible-offset degree barrier | PROVED | Polynomial-primorial divisibility forces every irreducible factor of a reducible successful offset above the preceding degree threshold. |
| Exact `d=1` degree-at-most-three reduction | PROVED | The interval and degree accounting reduce the crown to quadratic and cubic sectors. |
| Theorem 4.1: affine orbit decomposition | PROVED | Translation/depression and scaling split the cubic contribution into the two square classes with explicit orbit sizes. |
| Corollary 4.2: exact crown variable and failure certificate | PROVED | The crown is exactly the nonnegative integer `W_p`; failure is the simultaneous vanishing of its sectors. |
| Theorem 5.1: global smoothness of the sparse ordered-root surface | PROVED | The Jacobian analysis is symbolic; the independent finite singular-locus regression agrees at the tested prime. |
| Theorem 6.1: nontrivial affine-cone transfer | PROVED REDUCTION | It identifies a geometric carrier but the absolute Betti constant is too large to force positivity. |
| Theorem 7.1: sign-hook trace | PROVED | Alternating-hook character isolates the full cycle class exactly. |
| Theorem 8.1: alternating-hook projector | PROVED | Character computation is exact on every cycle type. |
| Theorem 9.1: exact fixed-point count | PROVED | Frobenius orbit classification gives the displayed count. |
| Corollary 9.2: fixed-point circularity | PROVED NO-GO | The fixed-point route rewrites, rather than proves, the crown. |
| Theorem 10.1: q-line class projectors | PROVED | Split/nonsplit readings combine into invariant and anti-invariant trace sums. |
| Theorem 11.1: saturation-defect identity | PROVED | Exact identity `S0_sat-S0=p(N_sq+N_ns)`; parity and nonnegativity follow. |

### Independent reconstruction rerun

The frozen independent script was rerun successfully.

- `p=5`: `I4=124`, `N2=1`, `N_sq=4`, `N_ns=6`, `W_p=6`.
- `p=7`: `I4=426`, `N2=1`, `N_sq=10`, `N_ns=8`, `W_p=10`.
- `p=11`: `I4=1660`, `N2=1`, `N_sq=14`, `N_ns=14`, `W_p=15`.
- The fixed-point formula matches the exhaustive counts.
- The alternating-hook character equals `p` on a `p`-cycle and zero on every other cycle type through the full tested partitions.
- The cubic class counts are even in each census.

These are exact finite theorems at the listed primes and regressions of symbolic formulas. They do not imply uniform nonvanishing.

### Paper V frontier

The exact identities give

\[
W_p=N_2+\frac{S_0^{\mathrm{sat}}-S_0}{2p}.
\]

If `N2=0`, the crown is precisely

\[
S_0<S_0^{\mathrm{sat}}
\quad\Longleftrightarrow\quad
N_{\mathrm{sq}}+N_{\mathrm{ns}}>0.
\]

Divisibility, parity and integrality are already exhausted by this ledger and cannot distinguish zero from a positive multiple.

## Paper VI reconstruction

### Authoritative replacement

The earlier Airy manuscript is not the series Paper VI. The authoritative paper is

`paper6_secondary_quotients_replacement/manuscript.md`.

### Theorem ledger

| Claim | Status | Reconstruction ruling |
|---|---|---|
| Theorem 2.1: fixed-class Cartier first moment | PROVED REDUCTION | A nonzero moment would suffice, but no uniform nonvanishing is supplied. |
| Theorems 3.1–3.2: translation and reciprocal q-line projectors | PROVED | Exact projector identities; they reorganize the trace data. |
| Theorem 4.1: cyclotomic tangent | PROVED | The dual-number calculation exposes the first wild tangent. |
| Theorem 5.1: nonsplit tangent extension | PROVED | The coefficient module is a nonsplit extension, not a semisimple direct sum. |
| Theorem 6.1: tangent Smith blindness | PROVED NO-GO | Smith data at the split level do not detect the required Frobenius tangent. |
| Theorem 7.1: no ordinary divided-hook complex | PROVED NO-GO | The required multiplicities are nonintegral, so the proposed ordinary virtual object cannot exist. |
| Theorem 8.1: Hattori–Stallings coefficient extraction | PROVED | The coefficient trace identity recovers divided group-ring coefficients. |
| Proposition 9.1 and Theorems 9.2–9.3: Artin–Schreier quotient and irreducibility section | PROVED | The root-cycle action, quotient equation and `g=1` section are explicit. |
| Theorem 10.1: no-split theorem | PROVED | The completely split squarefree fixed-cubic level is empty. |
| Theorem 11.1: Kummer sign criterion | PROVED WITH CORRECTION | The two classes are Kummer forms; they are not universally a quadratic twist. |
| Theorem 11.2: common quotient counts | PROVED | Point counts package the class sum, not its positivity. |
| Theorem 12.1: unique projective fixed point | PROVED | Exact boundary geometry. |
| Theorem 13.1: compactified quotient count | PROVED | The proper quotient has `1+(p-1)W_p` points with the stated boundary/open decomposition. |

### Independent reconstruction rerun

The independent script passed all recorded checks.

- Dual-number tangent identities passed at `p=5,7,11`: `tau^p=1`, norm zero, kernel size equals image size, and every Frobenius tangent occurs.
- Divided-hook multiplicities are `(p-1)/p` and `-1/p`, confirming that they are not an ordinary virtual character.
- Random Hattori–Stallings matrix checks passed at `p=5,7`.
- No squarefree completely split fixed-cubic case was found in the exhaustive `p=7,11` panels, matching the theorem.
- The corrected Kummer sign criterion passed at `p=5,11,17,23,29`.
- Compactified counts reconstructed at `p=7,11,17,23`; for example the quotient counts are `61,151,273,419` and the open counts are `54,140,256,374` respectively.

The rerun conclusion is explicit: all independent algebraic and finite regressions pass; none proves nonvanishing of the quotient open.

## Exact direct `d=1` theorem

The smallest surviving statement is:

> **D1-QLINE-NONSAT.** For every admitted prime for which the quadratic sector has failed,
> \[
> N_{\mathrm{sq}}+N_{\mathrm{ns}}>0.
> \]

Equivalent forms are:

1. `S0 < S0_sat`;
2. the compactly supported Frobenius trace on the specified cubic quotient open does not attain its zero-point value;
3. the Kummer quotient open has an `F_p`-rational point;
4. `W_p>0` after `N2=0`.

These are equivalent formulations, not independent approaches.

## Completed no-go analysis

The following routes cannot close `d=1` without a new ingredient:

- generic absolute-Betti bounds;
- the alternating-hook fixed-point projector by itself;
- congruence, parity or integrality of the saturation defect;
- identification with the former Airy trace;
- a universal quadratic sign twist;
- an ordinary divided-hook perfect complex;
- tangent/Bockstein data without a secondary Frobenius trace;
- generic Artin–Schreier trace surjectivity;
- standard proper-point congruences;
- unproved automatic Fano, rational-connected or Witt-rational properties at the wild point;
- larger finite scans without a uniform structural theorem.

## Relationship to Paper VII

Paper VII studies bilateral endpoint incidences. Its quadratic theorem and proposed cubic true-Frobenius theorem are not identified with `D1-QLINE-NONSAT`. No functor, trace identity, parameter map or implication between the two cubic problems has been proved.

They must remain separate research lanes.

## Final direct `d=1` status

- Degree barrier and exact crown reduction: proved.
- q-line and quotient identities: proved.
- Independent finite reconstructions: passed.
- D1-QLINE-NONSAT: open.
- Universal function-field `d=1`: open.
- Integer transfer: absent.

The direct `d=1` programme is complete as a reduction and no-go classification. Any continuation must prove a genuinely new one-sided Frobenius nonvanishing theorem, rather than create another equivalent quotient or projector.
