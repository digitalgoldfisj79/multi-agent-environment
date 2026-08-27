# Primorial Incidence Transfer v0.1

Date: 27 August 2026
Branch: `gpt56/fortune-primorial-incidence-transfer-v01-20260827`

## Question

Does the fractional-linear/incidence mechanism of Xiyu Hu, *Factorial residues modulo a prime: beyond the square-root bound* (arXiv:2608.01781), transfer exactly to the deterministic increasing primorial-prefix path?

## Frozen target

Let `q_1<...<q_N` be the primes in `[X,2X]`, let

`B_X = product_{p<X} p`, `P_0=B_X`, `P_j=B_X product_{i<=j} q_i`,

and for a prime modulus `varpi>2X` let

`A_X(varpi)={P_j mod varpi:0<=j<=N}`.

Target theorem: for all sufficiently large X and every prime `varpi>2X`,

`|A_X(varpi)| >> (X/(log X)^2)^(8/15)`.

Consequently, choosing `2X<varpi<4X`,

`|A_X(varpi)| >> varpi^(8/15)/(log varpi)^(16/15)`,

which is asymptotically beyond `varpi^(1/2)`.

## Preregistered gates

G1. Exact integer recurrence:
`P_{j+2}=g_j P_{j+1}+P_{j+1}^2/P_j`, where `g_j=q_{j+2}-q_{j+1}`.

G2. For fixed nonzero gap d in `F_varpi`, define
`T_{a,d}(x)=d a+a^2/x`.
Prove `T_{b,d} o T_{a,d}^{-1}` is affine and every nonidentity resulting line has multiplicity at most two.

G3. Prove unconditionally that some even gap `d<=C log X` occurs `>>X/(log X)^2` times among consecutive prime gaps internal to `[X,2X]`, using only PNT-scale prime count plus telescoping total gap length.

G4. Verify all hypotheses of the Stevens--de Zeeuw Cartesian-product incidence theorem exactly as in Hu's argument, with transition population T replacing `p-2`.

G5. Derive `|A|>>T^(8/15)` and hence the frozen target.

G6. Run exact finite checks for recurrence, line composition, line multiplicity and numerical residue-set inequality diagnostics over multiple dyadic blocks/moduli. Finite checks are evidence only.

G7. Cold novelty search for primorial/prefix-prime-product residue value-set theorems and incidence-geometric predecessors. A literature collision does not invalidate the theorem but changes its novelty status.

## Kill rules

- If the fixed-gap line multiplicity exceeds O(1), close the programme.
- If repeated-gap population requires an unproved bounded-gap-in-every-block hypothesis, close the programme.
- If the incidence theorem yields no exponent strictly above 1/2 after the repeated-gap loss, close the programme as non-headline.
- If an existing paper contains the same primorial-prefix value-set theorem or an immediately stronger specialization, classify as `KNOWN` and do not add as a new Paper I theorem.

## Scope discipline

This programme does **not** claim Fortune's conjecture, does not reopen the selected-centre prime-pair mainline, and does not establish source-to-reciprocal transference. A successful result is a deterministic modular anti-concentration theorem for the increasing primorial path and would be considered for Paper I only after hostile proof and novelty review.
