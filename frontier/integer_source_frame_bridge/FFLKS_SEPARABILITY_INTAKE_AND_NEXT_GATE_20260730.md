# FFLKS separability intake and revised function-field gate

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`  
Reviewed contribution: PR #33 issue comment `5129926592`; commits `a1f591bdd33407cf12ffe37e9d467f4a37d0f4de` and `32f83dd3b0bda8b2651f56933d0560da5fc522a6` on `claude/fortunes-conjecture-mechanisms-fuuz4z`.

## Executive decision

The separability theorem is accepted. It is a genuine reduction of the corrected function-field target.

The exact completed `T3` phase is not irreducibly coupled in the two source variables. At each canonical completion frequency `theta`, the source dependence factors into two one-variable von Mangoldt additive twists. The remaining difficulty is now split into:

1. a one-variable square-root theorem for the actual parameter family;
2. a classification and count of exceptional/major-arc parameters;
3. an additional `q^(k/2)` cancellation when the two prime-modulus parameters are assembled.

The function-field first-band theorem and Fortune's conjecture remain **OPEN**.

## 1. Accepted exact statements

Let `W=PS`, where `P,S` are distinct monic irreducibles of degree `k`, and let the monic degree-`R` centre family be `t^R+V`, `V={deg<R}`.

### 1.1 Canonical completion frequencies

For the top-coefficient residue pairing used in the completed `T3` identity,

\[
V^\perp=\{\theta:\deg\theta<2k-R\}.
\]

This description is independent of `P`, `S` and `W=PS`. The nonzero completion modes are therefore global low-degree parameters rather than pair-dependent frequency spaces.

### 1.2 Source separability

With CRT idempotents

\[
e_P=S(S^{-1}\bmod P),\qquad e_S=P(P^{-1}\bmod S),
\]

and puncture-inverse lifts `Lbar_P,Lbar_S`, the completed phase satisfies

\[
\psi_\theta(c(f,f';P,S)-t^R)
=
\psi_\theta(-e_P\overline L_P f)
\psi_\theta(-e_S\overline L_S f')
\psi_\theta(-t^R).
\]

Consequently

\[
T(\theta)
=
\sum_{P\ne S}
\left(A(\lambda_1)A(\lambda_2)-\Delta_{P,S}\right)
\psi_\theta(-t^R),
\]

where

\[
A(\lambda)=\sum_{\deg f=m}\Lambda(f)\psi(\lambda,f),
\]

and `Delta_{P,S}` is the exact `f=f'` correction.

The equality follows directly from the CRT decomposition of `c` and additivity of the character. The independent verifier checks the separated and direct double-source sums exactly on all committed `q=3` panels for both punctures.

## 2. What the reduction does and does not prove

The theorem removes the need for a four-source/modulus sheaf solely to recover the missing `q^(-m)` source saving. It replaces that part with a family of one-variable prime-polynomial Fourier coefficients `A(lambda)`.

It does **not** by itself prove `FFLKS`. Even a uniform pointwise bound

\[
|A(\lambda)|\ll q^{m/2}\operatorname{poly}(k,m,\deg L)
\]

leaves

\[
\sum_{P\ne S}|A(\lambda_1)A(\lambda_2)|
\ll q^{2k+m}/k^2,
\]

which is still `q^(k/2)` above the required `q^(m+3k/2)` scale. The pair-family assembly is therefore still load-bearing.

## 3. Correct next theorem package

### Gate FF5.1 -- local conductor identification

Express each character

\[
f\mapsto\psi_\theta(-e_P\overline L_P f)
\]

as a standard additive character on the local residue field `F_q[t]/P`. Determine its exact local parameter, conductor and dependence on `(theta,P,S,L)`.

This step is required before citing any short-interval, Artin--Schreier or factorization-function theorem.

### Gate FF5.2 -- major-arc/degenerate locus

Classify the parameter tuples for which the induced local additive character is trivial or geometrically exceptional. Prove a uniform count strong enough that their total contribution is at most the `FFLKS` allowance.

The finite panels contain no detected near-trivial parameters, but this remains empirical.

### Gate FF5.3 -- `FFV-generic`

For every nonexceptional local parameter in the image of the CRT map, prove

\[
|A(\lambda)|
\ll q^{m/2}\operatorname{poly}(k,m,\deg L).
\]

The theorem must be uniform over the explicit parameter family and retain polynomial dependence on `deg L`, so that `L=t^q-t` is admissible.

### Gate FF5.4 -- pair-family assembly

Gain the remaining `q^(k/2)` over the ordered pairs `(P,S)`. Three admissible routes remain:

1. a fixed-`S` trace-function estimate over `P`, followed by the `S` sum;
2. a second-moment/large-sieve theorem for the parameter images `lambda_1,lambda_2`;
3. a joint sheaf on the prime-pair parameter space after the source variables have already been summed into `A(lambda)`.

This is the present decision point for the coset `PORC_FF` theorem.

### Gate FF5.5 -- restore completion frequencies and puncture

Sum the canonical `theta` family, retain the exact diagonal correction, and prove constants polynomial in `deg L`. Then specialize to the true puncture `L=t^q-t`.

### Gate FF5.6 -- thinning

Only after the coset theorem is proved should the programme thin from all monic degree-`R` centres to algebraic squarefree-product families and then to a chosen walk analogue.

## 4. Empirical status

On the committed `k=2,R=3,m=3` panels:

- `max_theta |T(theta)|/q^(m+3k/2)` is below `0.5` for `q=3,5,7` and both punctures;
- `|A(lambda)|/q^(m/2)` has median near `1`, maximum below `1.70`, and no detected near-trivial parameter among up to `5040` samples;
- the pair family supplies an apparent additional saving of order `q^(k/2)`.

These observations support the revised target but prove none of Gates FF5.2--FF5.5.

## 5. Corrected boundary

### PROVED

- canonical, pair-independent completion-frequency space;
- exact source separability through CRT idempotents;
- exact `T(theta)` product formula with diagonal correction.

### COMPUTATIONALLY VERIFIED

- direct versus separated source sums on the committed finite panels;
- the exponent-gap and empirical `FFLKS`/`FFV` diagnostics.

### OPEN

- local conductor formula and exceptional-locus classification;
- `FFV-generic`;
- the `q^(k/2)` prime-pair assembly saving;
- puncture-uniform `FFLKS`;
- coset `PORC_FF` and thinning;
- the function-field first-band theorem;
- every integer-side orbit and higher-conductor theorem;
- Fortune's conjecture.

## Verdict

This round materially improves the function-field route. The missing source cancellation is no longer an opaque four-variable phenomenon. It is now a one-variable von Mangoldt additive-twist theorem followed by one explicit prime-pair assembly estimate. The latter remains essential and cannot be inferred from pointwise `FFV-generic` alone.