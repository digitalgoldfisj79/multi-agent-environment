# Function-field large-field bilateral diagonal-collapse programme v0.1

**Date:** 30 July 2026  
**Repository:** `digitalgoldfisj79/multi-agent-environment`  
**Working branch:** `gpt56/fortune-mesoscopic-cotlar-20260728`  
**Publication base:** `publication/fortune-papers-ii-vi-20260724`  
**External intake:** Fable Round 12 commit `ebcbcf766b7addc8512e11bf48febf79b1b30694`  
**Status:** preregistered and immediately executable

## 0. Objective

Prove, falsify, or reduce to a minimal new theorem the proposed large-field collapse

`q > k  =>  no cross-distinct simultaneous bilateral endpoint incidence`

for scalar nonzero completion frequency, prime field `F_q`, puncture `L=t^q-t`, degree-`k` monic irreducible moduli, and endpoint source degree `m=2k-1`.

If proved, derive the exact centred bilateral identity in the resulting diagonal-support regime and determine whether the corrected endpoint estimate `FFPR` follows without a residual exceptional-component theorem.

No conclusion from Fable Round 12 is accepted without independent derivation or reproduction. Future-dated metadata in the intake is non-authoritative; all accepted work is dated 30 July 2026.

## 1. Exact setup

Let `P,S,P',S'` be monic irreducibles of degree `k`, with `P!=S`, `P'!=S'`, `P!=P'`, and `S!=S'`. Let `theta,c,d in F_q^*`. The simultaneous endpoint incidence is

`E_mu = mu_PS P' - mu_P'S' P = c`,

`E_nu = nu_SP S' - nu_S'P' S = d`,

where

`mu_PS = -theta (LS)^(-1) mod P`,

`nu_SP = -theta (LP)^(-1) mod S`.

Equivalently, with

`lambda = -theta/c`, `rho = theta/d`,

the four inverse-free divisibilities are

`P  | LS  - lambda P'`,

`P' | LS' + lambda P`,

`S  | LP  + rho S'`,

`S' | LP' - rho S`.

## 2. Gate ordering

### Gate 0 — intake and branch audit

1. Verify the external commit and its parentage.
2. Reproduce the correspondence enumeration independently.
3. Separate proved statements from panel classifications.
4. Integrate by rederivation on the current PR branch; do not cherry-pick the divergent history blindly.

**Pass:** exact reproduction of the correspondence theorem and all frozen counts used later.  
**Fail:** any mismatch closes the dependent claim until corrected.

### Gate 1 — correspondence and known-family audit

Independently prove and verify:

- `CORR_FF`: partner primes are uniquely determined by `(P,S,c,d)`;
- same-modulus contact is impossible for `c,d!=0`;
- transpose points are precisely the Artin–Schreier pairs at `k=q`;
- reflection-family inclusion for `k>=q`;
- translation-family inclusion for `k>q`;
- disjointness of reflection and translation for odd `q`.

Extend exact falsification panels to all feasible prime-field pairs with `q>k`, including at least `(11,2)`, `(13,2)`, `(17,2)`, and further fixed-`k=2` panels if feasible.

### Gate 2 — universal scalar coupling `CD0_FF`

Prove or falsify

`c+d=0`, equivalently `lambda=rho`,

for every cross-distinct simultaneous incidence.

Required subprogramme:

1. Define monic degree-`q` quotients `A,B,C,D` by

   `AP  = LS  - lambda P'`,
   `BS  = LP  + rho S'`,
   `CP' = LS' + lambda P`,
   `DS' = LP' - rho S`.

2. Derive the exact transfer-matrix defect identities.
3. Prove the easy range `q<2k` first by degree and coprimality.
4. In the range `q>=2k`, isolate the unique low-degree defect polynomial `h`, `deg h<=q-2k`, satisfying

   `rho C-lambda B = h P S'`,
   `rho A-lambda D = h S P'`,

   and the exact product identity

   `h P P' S S' = L(rho S S' - lambda P P') + lambda rho(PS-P'S')`.

5. Prove `h=0` and `lambda=rho`, or exhibit a genuine counterexample.

**Pass:** written proof of `CD0_FF`.  
**Falsification:** one exact incidence with `c+d!=0`.  
**Theorem-level obstruction:** a minimal explicit low-degree-defect statement whose proof is exactly equivalent to `CD0_FF`.

### Gate 3 — large-field emptiness `QGT_K_EMPTY`

Assuming or proving `CD0_FF`, set `lambda=rho`. Show that the quotient system factors through

`A B = L^2-lambda^2`

with `A,B` monic degree `q`. Since `L-lambda` and `L+lambda` are irreducible Artin–Schreier polynomials of degree `q`, deduce

`{A,B}={L-lambda,L+lambda}`.

Recover the two algebraic families:

- translation: `P'=P+LR`, `S'=S+LR`, `S=P+lambda R`;
- reflection: `P'=LQ-P`, `S'=LQ-S`, `S=P+lambda Q`.

Then use degree to prove both are impossible when `q>k` and `P!=S`.

**Pass:** theorem `q>k => empty cross-distinct incidence`.  
**Falsification:** explicit exact counterexample.  
**Boundary:** if `CD0_FF` is open, state the conditional classification and the exact missing defect theorem.

### Gate 4 — complete small-field classification `BIC_FF`

Only after Gate 3, prove completeness for `k>=q`:

`incidence = reflection union translation`,

with transpose as the degenerate `k=q` reflection locus.

This gate is not allowed to delay the large-field endpoint if Gate 3 is already proved.

### Gate 5 — corrected exceptional amplitude

For `k>=q`, retain the literal corrected amplitude

`B_(P,S)=Ahat_P(mu_PS) Ahat_S(nu_SP)-Delta_PS`.

Prove a uniform exponential-in-`k` saving on reflection and translation components, or isolate the minimal fixed-field local-transform theorem. Finite `k=3..6` decay is evidence only.

### Gate 6 — centred bilateral identity `CBI_FF`

Derive an exact identity before positivity in which:

1. both source Gram diagonals are subtracted;
2. `Delta_PS` is retained;
3. diagonal, transpose, reflection and translation terms are explicit;
4. the residual support is exactly the residual simultaneous incidence;
5. reciprocity is used before absolute values;
6. the von Mangoldt weights remain literal.

In the regime `q>k`, insert `QGT_K_EMPTY` and simplify the identity to diagonal support only.

### Gate 7 — corrected endpoint `FFPR`

Determine whether diagonal-only support closes

`|T_corr(theta)| << q^(m+3k/2) poly(k,m,deg L)`

uniformly for nonzero scalar `theta` in the fixed-degree large-field regime.

Every power of `q` must be labelled exact, published-input, proved subtraction, conditional, or open.

### Gates 8–11 — post-endpoint chain

Only after Gate 7:

8. restore all canonical completion frequencies;
9. prove coset `PORC_FF`;
10. couple the higher-conductor signed terms;
11. thin centres explicitly from all monic centres to squarefree product families, thin products, and finally a chosen walk.

No complete-coset theorem is called Fortune before thinning. No function-field statement is counted as integer progress without an explicit transfer theorem.

## 3. Computational contract

The verifier package must:

- use exact finite-field arithmetic;
- ground-truth the correspondence enumerator against pair-squared scans on small panels;
- archive stage counts before and after each residual divisibility;
- classify transpose/reflection/translation/other separately;
- test `c+d=0` on every incidence;
- search extended `q>k` panels;
- archive any first counterexample in full polynomial coordinates;
- never promote finite-panel emptiness to a theorem.

## 4. Decision rules

1. A proof of `CD0_FF` followed by Artin–Schreier factorisation closes Gate 3.
2. A counterexample to `CD0_FF` does not automatically falsify `QGT_K_EMPTY`; test whether the low-degree defect can still be excluded for `q>k`.
3. A counterexample to `QGT_K_EMPTY` forces a new exceptional component and invalidates diagonal-only Gate 6.
4. If `QGT_K_EMPTY` is proved, proceed immediately to `CBI_FF`; do not spend the main cycle classifying fixed-field components.
5. Stop only at a proof, a falsification, or a minimal theorem-level obstruction with exact variables, degree ranges and required saving.

## 5. Status labels

Every result must be labelled one of:

- `PROVED EXACTLY`;
- `PROVED FROM PUBLISHED INPUT`;
- `MACHINE-VERIFIED IDENTITY`;
- `EMPIRICAL-EXACT FINITE PANEL`;
- `CONDITIONAL`;
- `OPEN`;
- `RETRACTED/CORRECTED`.
