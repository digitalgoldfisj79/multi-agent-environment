# Function-field endpoint resolution programme v0.1

**Date:** 30 July 2026  
**Repository:** `digitalgoldfisj79/multi-agent-environment`  
**Working branch:** `gpt56/fortune-mesoscopic-cotlar-20260728`  
**Frozen input head:** `05d493078a69587b3e8a3bcd707215a0846a6e7e`  
**Primary target:** corrected endpoint `FFPR` for the complete monic coset  
**Programme name:** `FERP-0.1` — Sampled Spectrum versus Centered Bilateral Geometry

This is the next autonomous research programme after the corrected mechanism map, the endpoint-dispersion audit, the sampled-scale correction and the bilateral-incidence falsification. It is a preregistered decision programme, not a literature survey and not a claim that the endpoint is nearly proved.

## 0. Frozen boundary

Work over `F_q[t]`. Let `P,S` be distinct monic irreducibles of degree `k`, let the source degree be

`m = 2k-1`,

let `k <= R <= 2k-1`, let `theta` be a nonzero canonical completion frequency with `deg theta < 2k-R`, and let the true puncture be

`L = t^q-t`.

The separated local transforms are

`Ahat_P(mu) = sum_{deg f=m} Lambda(f) psi_P(mu f)`,

with

`mu_PS = -theta Lbar_P Sbar_P mod P`,  
`nu_SP = -theta Lbar_S Pbar_S mod S`.

The exact completed endpoint aggregate is

`T_corr(theta) = sum_{P!=S} [Ahat_P(mu_PS) Ahat_S(nu_SP) - Delta_PS] psi_theta(-t^R)`.

The target is

`|T_corr(theta)| << q^(m+3k/2) poly(k,m,deg L)`.

The first dispersion contains the exact positive diagonal

`D_diag(theta) = q^m M_samp(theta)`,  
`M_samp(theta) = sum_{P!=S}|Ahat_P(mu_PS)|^2`.

Class control after source Cauchy reaches `FFPR` only if

`M_samp(theta) << q^(3k) poly(k,m)`.

The natural-scale deficit `q^((m-k)/2)` is conditional on `M_samp` having scale `q^(m+2k)`. It is not an unconditional theorem.

Accordingly, there are exactly two admitted endpoint routes:

1. **Route A — exceptional sampled diagonal:** prove `M_samp(theta) << q^(3k) poly`, then control the class term and `Delta_PS`.
2. **Route B — centered bilateral assembly:** prove a signed theorem that removes both source Gram diagonals before positivity, retains `Lambda`, reciprocity and `Delta_PS`, and controls every component of the simultaneous incidence.

No third route may be inserted by silently replacing the deterministic sampled set with all frequencies, dropping `Delta_PS`, or applying positivity before the required cancellation.

## 1. New exact starting theorem: sampled-frequency image

For fixed `P`, define

`Phi_P(S) = -theta Lbar_P Sbar_P mod P`

on degree-`k` irreducibles `S != P`.

### Theorem SF1 — fixed-modulus injectivity

`Phi_P` is injective.

**Proof.** If `Phi_P(S)=Phi_P(S')`, multiplication by the nonzero unit `-theta Lbar_P` and inversion give `S=S' mod P`. Since `S` and `S'` are monic of degree `k`, `S-S'` has degree below `k`. A degree-`k` polynomial `P` can divide it only when `S-S'=0`. ∎

### Corollary SF2 — explicit inverse and translate image

On the image,

`S mod P = -theta Lbar_P mu^(-1) mod P`.

Because `P` and `S` are both monic of degree `k`,

`S mod P = S-P`.

Thus, for fixed `P`, the deterministic frequencies are the inverse image of the irreducible-translate set

`{S-P : S irreducible, deg S=k, S!=P}`.

The set has exactly `pi_q(k)-1` elements inside the `q^k-1` nonzero local frequencies, hence density

`(pi_q(k)-1)/(q^k-1) ~ 1/k`.

Changing the puncture from `L` to a unit puncture `L'` dilates the image by the unit `L/L' mod P`; it does not change its cardinality.

**Status:** `PROVED EXACTLY`.  
**Machine audit:** `fortune-review/scripts/ff_sampled_frequency_image_audit.py`.

This theorem changes the interpretation of Route A. The required `q^(3k)` bound is not a repeated-frequency or tiny-sample phenomenon. It requires the additive Fourier energy to avoid an injective, asymptotic density-`1/k` prime-translate subset by a power at the endpoint.

## 2. Programme decision tree

```text
Gate 0: freeze identities and verify SF1/SF2
   |
   v
Gate 1: determine the deterministic sampled-diagonal scale
   |-------------------------------|
   |                               |
exceptional q^(3k) plausible       natural/larger scale established
   |                               |
Route A theorem attack             Route A closed
   |                               |
   +---------------+---------------+
                   v
Gate 2: classify bilateral incidence components
                   |
                   v
Gate 3: compute exact signed component contributions, including Delta_PS
                   |
                   v
Gate 4: derive centered bilateral identity before positivity
                   |
                   v
Gate 5: prove residual trace/bilinear estimate or isolate exact sheaf wall
                   |
                   v
Gate 6: corrected endpoint FFPR
                   |
                   v
Gate 7: theta sum and coset PORC_FF
                   |
                   v
Gate 8: signed higher-conductor coupling
                   |
                   v
Gate 9: complete-coset first-band theorem
                   |
                   v
Gate 10: thinning sequence and only then a chosen walk
```

Gates 1 and 2 begin in parallel after Gate 0, but no analytic proof attempt may bypass their exact outputs.

## 3. Gate 0 — baseline and contract

### Objective

Freeze the exact notation, status labels, endpoint target and disallowed inferences.

### Required outputs

- this programme document;
- machine-readable contract `FF_ENDPOINT_RESOLUTION_PROGRAMME_V0_1_20260730.json`;
- contract verifier and frozen output;
- SF1/SF2 verifier and frozen output;
- dedicated GitHub Actions workflow.

### Pass condition

Every exact identity compiles and reproduces the frozen panels. Every open statement remains labelled `OPEN` or `CONDITIONAL`.

### Stop condition

Any mismatch between the exact aggregate used by a verifier and `T_corr(theta)` stops the programme until corrected.

## 4. Gate 1 — sampled-diagonal discriminator

This gate decides whether Route A is a genuine route or merely a restatement of the missing source cancellation.

### 4.1 Exact object

For every nonzero canonical `theta`, compute

`M_samp(theta) = sum_P sum_{S!=P}|Ahat_P(Phi_P(S))|^2`.

Maintain three normalizations:

- `M_samp/q^(3k)` — the Route A threshold;
- `M_samp/q^(m+2k)` — the natural sampled scale;
- `M_samp/M_full`, where
  
  `M_full = sum_P sum_{mu!=0}|Ahat_P(mu)|^2`.

The third ratio must be compared with the exact sample density `(pi_q(k)-1)/(q^k-1)`.

### 4.2 Exact decomposition

Expand

`M_samp = sum_{f,g} Lambda(f)Lambda(g) K_samp(f-g)`,

where

`K_samp(h) = sum_{P!=S} psi_P(Phi_P(S) h)`.

Separate:

- the exact source diagonal `f=g`;
- prime-power coincidences;
- the signed off-diagonal.

No positivity may be applied to the off-diagonal before testing whether it cancels the source diagonal.

### 4.3 Mathematical targets

#### Route A target `SAD_FF`

Prove uniformly

`M_samp(theta) << q^(3k) poly(k,m)`.

A proof must identify the mechanism giving the endpoint saving `q^(m-k)=q^(k-1)` against the natural scale. “Sampled frequencies are generic” is insufficient; genericity predicts the wrong scale for Route A.

#### Route A falsification target `NSAD_FF`

Any of the following closes Route A:

- an asymptotic `M_samp ~ c q^(m+2k)/poly` with `c>0`;
- a lower bound `M_samp >> q^(3k+delta)` on an infinite parameter family;
- a forced positive component after exact expansion whose size exceeds the Route A allowance and cannot be cancelled.

Finite growth panels do not prove `NSAD_FF`; they only select the next theorem attempt.

### 4.4 Computational panels

#### CI exact panel

- `(q,k)=(3,2),(5,2),(7,2),(11,2)`;
- `(q,k)=(3,3),(5,3)`;
- `(q,k)=(3,4)`;
- all nonzero canonical `theta` where feasible;
- true primorial and at least one fixed unit puncture control.

#### Extended CPU panel

- fixed `k=2`, prime `q` through the feasible exact range;
- fixed `q=3`, `k` through at least `5`;
- fixed `q=5`, `k` through at least `4` using streaming transforms;
- source diagonal, off-diagonal and total archived separately.

#### External compute panel

Use chunked `(P,S)` blocks and exact modular/cyclotomic accumulation. Do not replace exact sums with floating point until the final presentation layer.

### 4.5 Decision rule

- If `M_samp/q^(3k)` remains bounded and a structural cancellation is identified, continue Route A for one theorem cycle.
- If it grows at the natural exponent and no exact exceptional mechanism appears, prioritize `NSAD_FF`; do not spend further cycles trying to prove ordinary sampled `FFV` as though it closed the endpoint.
- Route B continues regardless, because it is required if Route A fails.

## 5. Gate 2 — simultaneous incidence geometry

### 5.1 Endpoint incidence

For pair indices `a=(P,S)` and `b=(P',S')`, define

`I_nu(a,b): deg(nu_a S' - nu_b S) <= 0`,

`I_mu(a,b): deg(mu_a P' - mu_b P) <= 0`.

The bilateral support is

`I_bi = I_nu intersect I_mu`.

The universal diagonal/transpose-only conjecture is retracted. The `(q,k)=(3,4)` panel contains two genuine exceptional affine orbits.

### 5.2 Algebraization

Clear every modular inverse using Bezout/resultant coordinates. Produce a polynomial incidence scheme over the coefficient space of

`(P,S,P',S',e_mu,e_nu)`.

The deliverable must state:

- ambient dimension;
- defining equations and degrees;
- open conditions for irreducibility and pairwise distinctness;
- diagonal and transpose ideals;
- characteristic-dependent factors;
- puncture-dependent factors;
- Jacobian rank and singular locus on each candidate component.

A relation found only after enumerating irreducibles is an empirical pattern until it is derived as a polynomial identity.

### 5.3 Candidate generation

Do not use an `O(N^2)` blind pair-of-pairs scan beyond the CI panel. Generate the one-source coincidence candidates from their exact scalar relations, then apply the reciprocal condition. Archive the candidate count before and after each filter.

### 5.4 Component classification target `BIC_FF`

Classify every geometrically irreducible component of `I_bi` into:

1. diagonal;
2. transpose;
3. affine-symmetry orbit components;
4. small-characteristic components;
5. primorial-resonant components;
6. residual components.

For each component record dimension, degree, stabilizer, field of definition and expected number of prime points.

### 5.5 Falsification rule

If a component has enough prime points and coherent phase to contribute above `q^(m+3k/2)` after the exact diagonal corrections, the unmodified `CBEA_FF` target is false. The programme must then derive and subtract the forced component main term before continuing.

## 6. Gate 3 — exact component contributions

Geometry alone is not the analytic theorem. For every component from `BIC_FF`, compute the literal summand

`Lambda(f)Lambda(g)Lambda(f')Lambda(g') * phase`

or its separated transform form, with `Delta_PS` included.

### Required classifications

- **forced main term:** nonoscillatory after all symmetries;
- **paired main term:** cancels only after transpose/Galois/affine pairing;
- **oscillatory residual:** eligible for trace-function cancellation;
- **degenerate residual:** contains an Artin–Schreier or geometrically trivial factor;
- **negligible by dimension:** point count alone is below target.

### Required exact tests

- transpose conjugacy;
- affine covariance;
- Galois orbit traces;
- dependence on `theta`;
- dependence on the puncture;
- exact interaction with `Delta_PS`.

The output is a subtractable component formula, not a qualitative statement that the exceptions are “rare”.

## 7. Gate 4 — centered bilateral identity

### Target `CBI_FF`

Derive an exact identity for `|T_corr(theta)|^2` or an equivalent bilinear form in which:

1. both single-source Gram diagonals are subtracted before positivity;
2. `Delta_PS` is retained literally;
3. diagonal, transpose and forced exceptional components appear as explicit terms;
4. the residual support is the residual part of `I_bi` from Gate 2;
5. exact residue reciprocity is applied before any absolute-value split;
6. every coefficient remains the actual von Mangoldt weight, not an arbitrary sequence.

### Ledger requirement

The identity must display where the required endpoint saving enters. Every power of `q` must be tagged as one of:

- exact cardinality;
- exact orthogonality;
- published theorem;
- proved component subtraction;
- conditional estimate;
- open cancellation.

An identity that reproduces the first positive diagonal without a new signed term has failed this gate.

## 8. Gate 5 — residual trace-function theorem

Only after `CBI_FF` and `BIC_FF` are complete may the residual be presented as a trace-function or bilinear Kloosterman problem.

### 8.1 Literal sheaf audit

State:

- base parameter space and excluded divisors;
- rational phase map;
- rank and conductor bounds in `k,m,deg L`;
- local monodromy and slopes at infinity;
- Artin–Schreier trivial locus;
- tensor-product coincidences;
- diagonal automorphisms;
- characteristic restrictions;
- dependence on the prime-pair irreducibility constraints.

### 8.2 Published-input audit

The nearest proof technologies are to be tested literally, not cited by resemblance:

- Keating–Rudnick, arXiv:1204.0708 — all-residue variance in the fixed-degree, large-field regime;
- Bagshaw, arXiv:2401.10399 and arXiv:2304.05014 — weighted bilinear Kloosterman sums in polynomial rings;
- Sawin–Shusterman, arXiv:2512.24080 — short trace-function sums under explicit squarefree-modulus, slope and non-Artin–Schreier hypotheses;
- Fu–Lau–Li–Xi, arXiv:2406.10106 — joint equidistribution for different Kloosterman sums in specified function-field families.

For each candidate theorem, include a variable-by-variable mapping and list every failed hypothesis. No result is labelled `PROVED FROM PUBLISHED INPUT` until the literal ranges and sheaf conditions match.

### 8.3 Residual theorem `RBK_FF`

Prove the residual component contribution is

`<< q^(m+3k/2) poly(k,m,deg L)`

after the exact component subtractions.

If it cannot be proved, isolate the smallest remaining exponential sum or sheaf statement, including its exact parameter space, degeneracy locus, conductor and required saving.

## 9. Gate 6 — corrected endpoint `FFPR`

Combine:

- Route A `SAD_FF`, or Route B `CBI_FF + BIC_FF + RBK_FF`;
- exact class-main-term treatment;
- exact `Delta_PS` treatment;
- uniformity in nonzero canonical `theta`;
- polynomial dependence on `k,m,deg L`.

### Pass condition

A written proof of

`|T_corr(theta)| << q^(m+3k/2) poly(k,m,deg L)`

with no unexplained exponent saving.

### Failure condition

A forced component or explicit panel violating the target after all required subtractions rigorously falsifies the endpoint formulation. The programme then records the corrected main term or closes the route.

## 10. Gate 7 — restore completion frequencies

Only after Gate 6:

1. restore the factor `q^(R-2k)`;
2. sum all nonzero canonical `theta`;
3. retain any theta-correlated component main terms;
4. prove the complete-coset `T3` estimate;
5. state coset `PORC_FF` with its exact `R,k,m` range.

A pointwise theorem may be replaced by an averaged-theta theorem only if the full ledger closes after the exact frequency count.

## 11. Gate 8 — signed higher-conductor coupling

The physical result is not the whole detector. Reintroduce the remaining conductor variables without sequential diagonalization.

The theorem must preserve:

- physical cross-conductor cancellation;
- dense drift/sparse hit cancellation;
- cross-band martingale covariance;
- primorial-prefix rigidity.

This is the function-field analogue of the integer `JHGF/NSMT` interface. A complete-coset physical theorem is not enough by itself.

## 12. Gate 9 — complete-coset first-band theorem

State exactly what first-band detection theorem follows for all monic degree-`R` centres. Do not call it Fortune in the laboratory.

Required outputs:

- centre family;
- source and modulus ranges;
- density/main term;
- variance or detection conclusion;
- excluded punctures and characteristics;
- dependence on `q,k,R`;
- interface to thinning.

## 13. Gate 10 — thinning

Proceed only in this order:

`all monic degree-R`

`-> squarefree products of fixed-degree irreducibles`

`-> thin product family`

`-> chosen walk`.

At each arrow record:

- exact affine symmetry lost;
- completion identity lost;
- replacement theorem required;
- density loss;
- new correlations;
- whether a canonical order exists.

There is no canonical increasing order on equal-degree irreducibles. A walk is a chosen model and must be preregistered independently.

## 14. Integer mechanism extraction

Only after a decisive function-field theorem or wall, update the non-transfer dictionary:

| Function-field mechanism | Integer replacement | Required theorem | Current status |
|---|---|---|---|
| Exact affine completion | Poisson/incomplete completion | primorial-centre completion with controlled boundary | `OPEN` |
| Exact reciprocal identity | Kloosterman reciprocity/spectral rearrangement | prime-band reciprocal bilinear theorem | `OPEN` |
| Component classification | integer congruence/determinant geometry | signed semiprime-resonance classification | `OPEN` |
| Weil/Katz/trace cancellation | GRH-shaped or spectral cancellation | cross-prime-modulus coherent estimate | `OPEN` |
| Affine/Galois orbit traces | character orthogonality/arithmetic symmetry | deterministic primorial-orbit theorem | `OPEN` |
| Complete coset fairness | consecutive primorial sampling | `PORS(X)` and `PORC(X)` | `OPEN` |

This remains a dictionary, not a transfer theorem.

## 15. Verification architecture

Every gate that creates an exact identity must add:

1. an independent verifier;
2. frozen semantic JSON output;
3. a dedicated GitHub Actions workflow;
4. a note stating what the panel proves and cannot prove;
5. an exponent ledger checked by machine-readable assertions.

### Required status vocabulary

- `PROVED EXACTLY`
- `PROVED FROM PUBLISHED INPUT`
- `MACHINE-VERIFIED IDENTITY`
- `EMPIRICAL-EXACT FINITE PANEL`
- `EMPIRICAL`
- `CONDITIONAL`
- `RETRACTED`
- `OPEN`

No other status wording is authoritative.

## 16. Stop rules

The autonomous run stops only at one of these decisive outcomes:

1. `SAD_FF` is proved and Route A closes endpoint `FFPR` with class and `Delta` control;
2. `NSAD_FF` closes Route A and `CBEA_FF/RBK_FF` proves endpoint `FFPR`;
3. a forced exceptional component rigorously falsifies the corrected endpoint target;
4. the residual is reduced to one precisely stated new exponential-sum or sheaf theorem that cannot be discharged by exact algebra, current published input or the committed computations;
5. a complete-coset theorem is proved and the next genuine wall is thinning or higher-conductor coupling.

The run must not stop at a restatement of `CBEA_FF`, a list of papers, a numerical trend, or a generic request for “new cancellation”.

## 17. Immediate execution order

The next autonomous run should execute, in order:

1. extend the SF1/SF2 verifier to all CI panels and freeze output;
2. implement exact `M_samp`, `M_full`, source-diagonal and signed off-diagonal ledgers;
3. run the Route A discriminator panels;
4. generate one-source incidence candidates and reciprocal filters without blind pair-squaring;
5. classify the two `(q,k)=(3,4)` exceptional affine orbits and search for their defining equations;
6. test whether their signed contribution is a main term, a transpose/Galois cancellation, or a residual;
7. derive the first exact centered bilateral identity retaining `Delta_PS`;
8. only then conduct the sheaf/literature applicability audit.

The first decision point is the sampled-diagonal discriminator. The first algebraic decision point is the exceptional-component contribution. Both precede any large sheaf construction.

## 18. Current status after programme construction

### PROVED EXACTLY

- the frozen endpoint identities from the authoritative map;
- SF1 fixed-modulus injectivity;
- SF2 inverse translate description and puncture unit dilation;
- the exact threshold `M_samp << q^(3k)` required by a post-Cauchy Route A proof.

### MACHINE-VERIFIED IDENTITY

- SF1/SF2 on the committed finite panels.

### EMPIRICAL-EXACT FINITE PANEL

- sampled-set densities on the committed panels;
- the previously archived bilateral incidence counts and exceptional affine orbits.

### OPEN

- the scale of `M_samp` on the deterministic sampled image;
- `SAD_FF` or `NSAD_FF`;
- general bilateral component classification;
- exact exceptional-component contributions;
- `CBI_FF`, `RBK_FF`, corrected endpoint `FFPR`;
- theta summation, coset `PORC_FF`, higher-conductor coupling, first-band theorem and thinning;
- every integer-side theorem through Fortune's conjecture.
