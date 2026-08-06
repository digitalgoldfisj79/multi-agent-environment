# Function-field nonzero-defect orbit programme v0.1

**Date:** 31 July 2026  
**Repository:** `digitalgoldfisj79/multi-agent-environment`  
**Working branch:** `gpt56/fortune-mesoscopic-cotlar-20260728`  
**Frozen input head:** `170c8aeb2545f9bf164258a01857360cc2d50789`  
**Publication base:** `publication/fortune-papers-ii-vi-20260724`  
**Predecessor:** `FF_LARGE_FIELD_DIAGONAL_COLLAPSE_PROGRAMME_V0_1_20260730.md`  
**Status:** preregistered, executable, and deliberately geometry-first

## 0. Objective

Resolve the new large-field obstruction isolated by the bilateral defect dichotomy.

For fixed modulus degree `k`, prime `q>=2k`, scalar nonzero completion frequency and puncture

`L=t^q-t`,

classify or sharply bound the **nonzero-defect bilateral endpoint incidence**, determine its literal contribution to the diagonally centred completed second moment, and decide whether corrected endpoint `FFPR` follows.

The primary target is not a pointwise local-transform estimate. It is the orbit-level theorem

`NDC_FF(k): after quotienting by AGL(1,q), the nonzero-defect incidence has bounded geometric complexity for fixed k`,

with a first sufficient form

`# I_nd(q,k) <<_k q^2`.

If this is false, the programme must determine the true dimension and test it against the endpoint exponent before attempting cancellation estimates.

No finite orbit census is promoted to a theorem. No trace-function theorem is cited until the literal orbit phase, conductor and degeneracy locus have been derived.

## 1. Frozen exact input

Let `P,S,P',S'` be monic irreducibles of degree `k`, with the pair and cross-distinct conditions required by the bilateral endpoint completion. Put

`lambda=-theta/c`, `rho=theta/d`.

The inverse-free incidence is

`P  | LS  - lambda P'`,

`P' | LS' + lambda P`,

`S  | LP  + rho S'`,

`S' | LP' - rho S`.

For `q>k`, the monic degree-`q` quotients `A,B,C,D` satisfy the exact common-defect identities

`rho C-lambda B = h P S'`,

`rho A-lambda D = h S P'`,

`hPP'SS' = L(rho SS'-lambda PP') + lambda rho(PS-P'S')`,

with unique `h` and `deg h<=q-2k`.

The zero-defect locus `h=0` is exactly the reflection/translation union, with transpose contact at `k=q`. Hence:

- `q<2k` forces zero defect;
- `k<q<2k` is empty;
- every genuinely new large-field component lies in `q>=2k` and has `h!=0`, equivalently `lambda!=rho`.

The explicit `(q,k)=(11,3)` incidence and the exact cubic census through `q=59` are frozen falsification anchors, not asymptotic evidence.

## 2. New exact baseline: bounded-degree Frobenius-root form

### Theorem FRC1 — root-cycle equivalence

Choose ordered root cycles

`alpha=(alpha_0,...,alpha_(k-1))`, `beta`, `alpha'`, `beta'`

with Frobenius shifting each tuple cyclically. The four inverse-free divisibilities are equivalent, on the root-separation open locus, to the `4k` equations

`(alpha_(i+1)-alpha_i) product_j(alpha_i-beta_j)
     = lambda product_j(alpha_i-alpha'_j)`,

`(alpha'_(i+1)-alpha'_i) product_j(alpha'_i-beta'_j)
     = -lambda product_j(alpha'_i-alpha_j)`,

`(beta_(i+1)-beta_i) product_j(beta_i-alpha_j)
     = -rho product_j(beta_i-beta'_j)`,

`(beta'_(i+1)-beta'_i) product_j(beta'_i-alpha'_j)
     = rho product_j(beta'_i-beta_j)`,

for `i mod k`.

Each equation has degree at most `k+1`, independent of `q`. The dependence on `q` is moved entirely into the twisted Frobenius rationality condition: geometric Frobenius sends every ordered tuple to its cyclic shift.

This is the key reformulation. The nonzero-defect problem is a twisted-point problem on a bounded-degree root-configuration variety, not a family of coefficient schemes whose degrees grow with `q`.

### Theorem AGL1 — affine covariance and canonical gauge

For `a in F_q^*`, `b in F_q`, send every root `r` to `ar+b`. Then

`lambda -> a lambda`, `rho -> a rho`.

The common defect transforms by

`h(t) -> a^(2-2k) h((t-b)/a)`.

In the range `q>=2k`, hence `char(F_q)>k`, every incidence orbit has a unique representative satisfying

`lambda=1`,

`coefficient of t^(k-1) in P = 0`.

Indeed `a=lambda^(-1)` is forced, and the unique translation is

`b=a p_(k-1)/k`.

Thus the `q(q-1)` affine factor can be removed exactly before geometry or counting. Finite cyclic rotations of each root tuple remain and must be accounted for separately.

The companion verifier checks FRC1, all `q(q-1)=110` affine transforms of the explicit cubic counterexample, the defect covariance law, and uniqueness of the canonical gauge.

## 3. Programme architecture

The programme has two synchronized workstreams.

**Geometry stream:** determine the dimension, degree and components of the affine-normalized nonzero-defect root variety.

**Assembly stream:** derive the exact centred bilateral identity and the affine-orbit transformation law of its literal corrected amplitudes.

The geometry stream is the first discriminator. The assembly stream may proceed algebraically in parallel, but no analytic estimate is attempted until the component coefficients are known.

## 4. Gate 0 — freeze, reproduce, and guard the boundary

### Deliverables

1. Reproduce the explicit `(11,3)` counterexample from the original local-frequency definitions.
2. Reproduce the defect identities and cubic orbit census anchors.
3. Verify Theorems FRC1 and AGL1 independently.
4. Freeze a machine-readable contract listing every gate, pass condition, falsification condition and stop rule.

### Pass

All exact anchors and covariance checks reproduce with exact arithmetic.

### Failure

Any mismatch retracts dependent programme statements before further work.

## 5. Gate 1 — cubic normalized root ideal `NDRI_3`

Set `k=3`, normalize `lambda=1` and `sum_i alpha_i=0`, and retain `rho!=0,1`.

Construct the fixed polynomial ideal generated by the twelve FRC1 equations in

`alpha_i, beta_i, alpha'_i, beta'_i, rho`.

Saturate by:

- all within-tuple discriminants;
- all pair/cross-resultants required by the incidence;
- `rho(rho-1)`;
- the zero-defect component.

The zero-defect saturation must be performed algebraically, not by deleting census points.

### Required computations

1. Compute Krull dimension and degree over characteristic zero where meaningful.
2. Repeat over several good finite characteristics, including holdout characteristics not used in the census.
3. Compute the Jacobian rank and singular locus on every surviving component.
4. Produce Gröbner/primary-decomposition certificates in a reproducible CAS format.
5. Compare geometric degree with the observed number of affine-normalized cubic orbits.

### Target `QZD_3`

The saturated normalized ideal is zero-dimensional of bounded degree `D_3`.

### Falsification

A positive-dimensional component meeting the root-separation open locus.

If falsified, record its dimension `r`, degree, generic stabilizer and expected incidence scale `q^(r+2)` before deciding whether it threatens the endpoint.

## 6. Gate 2 — twisted Frobenius point theorem `TFP_k`

A geometric component theorem is not yet an arithmetic incidence theorem. Prove the exact dictionary between:

- affine-normalized polynomial incidences over `F_q` with irreducible degree-`k` moduli; and
- geometric points of the normalized root variety fixed by Frobenius composed with the four cyclic shifts.

Account explicitly for:

- the `C_k^4` root-rotation multiplicity;
- shorter Frobenius cycles and reducible-polynomial contamination;
- component fields of definition;
- affine stabilizers;
- collisions excluded by saturation.

### Sufficient conclusion

If the normalized variety is zero-dimensional of degree `D_k`, then

`# I_nd(q,k) <= k^4 D_k q(q-1)`.

No Lang–Weil theorem is needed for a zero-dimensional bound; degree controls the geometric point count directly.

### Failure mode

If geometric components are positive-dimensional, derive the correct twisted Lang–Weil or trace-of-Frobenius count rather than substituting ordinary rational-point heuristics.

## 7. Gate 3 — exact census and invariant fingerprinting

Extend the independent orbit-reduced census without changing the theorem status.

### Cubic panel

- all feasible odd primes through at least `q=251`;
- extend to `q=503` if runtime remains practical;
- archive seeds, full orbit sizes and stabilizers;
- record the canonical gauge representative for every orbit.

### Invariants per orbit

- `rho` in the `lambda=1` gauge;
- normalized defect coefficients and degree;
- discriminants and resultants of the four cubics;
- traces and norms of root differences;
- cyclic and transpose symmetries;
- exact corrected-amplitude placeholders once available.

### Holdout rule

Use only the first half of primes to formulate any proposed component polynomial. Predict orbit counts and invariant values on the untouched half before inspecting them.

Finite interpolation, congruence patterns and orbit counts remain `EMPIRICAL-EXACT FINITE PANEL` until derived from the normalized ideal.

## 8. Gate 4 — general fixed-degree geometry `QZD_k`

Use the FRC1 system to attack arbitrary fixed `k`.

### Primary route

Prove that, after the two affine gauge equations and saturation by collisions and `rho(rho-1)`, the `4k` root equations form a zero-dimensional complete intersection on the nonzero-defect open locus.

Required checks:

1. display the full Jacobian block structure;
2. identify all rank-loss equations;
3. prove every rank-loss component is zero defect, collision, reducible, or explicitly exceptional;
4. bound the degree `D_k` by an explicit function of `k`;
5. state whether the bound is polynomial, exponential or merely effective.

### Secondary route

If complete-intersection regularity fails, construct an elimination tree in the order

`alpha' -> beta' -> beta -> rho`,

preserving the cyclic symmetry and avoiding a generic doubly-exponential Gröbner bound where structure gives a smaller one.

### First acceptable theorem

For each fixed `k`, the affine-normalized nonzero-defect locus has dimension zero and effective degree `D_k`.

Uniform control of `D_k` may be deferred if fixed-`k` endpoint `FFPR` is the current asymptotic regime, but the dependence must be explicit.

## 9. Gate 5 — centred bilateral identity `CBI_ND`

Derive the exact completed second-moment identity before positivity, with:

1. both single-source Gram diagonals subtracted;
2. the literal `Delta_PS` retained;
3. diagonal, transpose and zero-defect components displayed separately;
4. the nonzero-defect support represented through FRC1 or the common defect `h`;
5. exact reciprocity applied before absolute values;
6. the actual von Mangoldt weights retained;
7. every completion factor and power of `q` labelled.

The identity must state the exact coefficient attached to an ordered nonzero-defect incidence `(a,b)`. A raw pair-of-pairs census without this coefficient is not an amplitude theorem.

### Failure

If the first positive diagonal reappears unchanged, the centering has failed and the identity does not pass.

## 10. Gate 6 — affine-orbit amplitude covariance `OAC_FF`

For the literal coefficient from `CBI_ND`, derive its transformation under

`t -> at+b`.

Separate:

- local transform covariance;
- the centre/completion phase;
- `Delta_PS` covariance;
- any character introduced by root ordering;
- stabilizer effects.

For each geometric orbit classify the aggregate as:

1. forced coherent main term;
2. exactly annihilated by translation orthogonality;
3. exactly annihilated by dilation orthogonality;
4. a one- or two-dimensional trace-function sum;
5. a degenerate nonoscillatory residual.

This gate is deliberately ahead of pointwise local-transform bounds. The observed incidence is already organized into full `AGL(1,q)` orbits; exact orbit summation may be stronger and cheaper than bounding every point.

## 11. Gate 7 — exact corrected-amplitude panels

After `CBI_ND` and `OAC_FF`, compute the literal orbit contributions for the first nonzero cubic panels:

`q=11,17,19,29,31`,

then holdouts where feasible.

Use exact residue-count transforms or exact cyclotomic accumulation. Do not enumerate all degree-`m` sources when a residue-count identity is available, and do not use floating point before the presentation layer.

Archive separately:

- product-product;
- product-Delta;
- Delta-product;
- Delta-Delta;
- total corrected orbit contribution;
- diagonal and zero-defect controls;
- normalization by the squared endpoint allowance.

The panels choose the next theorem; they do not prove it.

## 12. Gate 8 — nonzero-defect component theorem `NDC_FF`

Combine Gates 1–7 into one of the following theorem forms.

### Geometry-only form

`# I_nd(q,k) << D_k k^4 q^2`.

This passes only if the trivial or proved orbit-amplitude bound already lies within the centred endpoint ledger.

### Orbit-cancellation form

For every normalized geometric component, its full affine-orbit contribution is within its allocated share of

`q^(2m+3k) poly(k,m)`

in the squared endpoint identity.

### Trace-function form

After exact orbit reduction, the residual is a specified trace sum with:

- base variety and excluded divisors;
- rational phase map;
- rank and conductor;
- local monodromy and slopes at infinity;
- Artin–Schreier trivial locus;
- tensor-product coincidences;
- characteristic restrictions;
- exact saving required.

Only this literal object may be compared with Bagshaw's bilinear Kloosterman bounds or Sawin–Shusterman's short trace-function theorem. Those works establish relevant technology, not an automatic application to the present moving prime-pair geometry.

## 13. Gate 9 — corrected endpoint `FFPR`

Combine:

- `CBI_ND`;
- zero-defect component treatment;
- `NDC_FF`;
- exact class-main-term treatment;
- literal `Delta_PS` treatment;
- uniformity in nonzero canonical frequency.

### Pass

A complete proof of

`|T_corr(theta)| << q^(m+3k/2) poly(k,m,deg L)`

in the stated fixed-degree large-field regime, with no unexplained exponent saving.

### Falsification

A forced component whose exact corrected contribution exceeds the endpoint allowance. In that case record the missing main term and reformulate `T_corr`; do not hide it in an error term.

## 14. Gates 10–13 — post-endpoint chain

Only after Gate 9:

10. restore every canonical completion frequency and prove the theta-summed first-band estimate;
11. prove coset `PORC_FF`;
12. couple the signed higher-conductor terms without sequential diagonalization;
13. thin centres from all monic centres to squarefree products, thin product families and a chosen walk.

A complete-coset theorem is not called Fortune before thinning. No function-field theorem is counted as integer progress without an explicit transfer theorem.

## 15. Computational implementation

### Committed baseline files

- `fortune-review/scripts/ff_nonzero_defect_root_covariance_audit.py`
- `fortune-review/data/ff_nonzero_defect_root_covariance_audit.json`
- `fortune-review/scripts/ff_nonzero_defect_programme_contract.py`
- `fortune-review/data/ff_nonzero_defect_programme_contract.json`
- `.github/workflows/ff-nonzero-defect-orbit-programme.yml`

### Next generated CAS files

Gate 1 must generate, rather than hand-edit:

- a Singular ideal and saturation script;
- a Magma or Sage cross-check script;
- a machine-readable variable/equation manifest;
- dimension, degree, primary-component and Jacobian certificates.

The generator is part of the audit boundary. A CAS transcript without the exact generated equations is insufficient.

## 16. Decision and stop rules

The autonomous execution stops only at one of these conditions:

1. `QZD_k + TFP_k + CBI_ND + OAC_FF` proves `NDC_FF` and endpoint `FFPR`;
2. a positive-dimensional nonzero-defect component is proved and its endpoint contribution is rigorously classified;
3. a forced corrected component falsifies the present endpoint formulation;
4. the problem is reduced to one precise trace-function or exponential-sum theorem, with literal parameter space, conductor, degeneracy locus and required saving;
5. the fixed-`k` geometry is proved but the next wall is an explicitly stated uniform-in-`k` degree theorem.

The programme may not stop at:

- additional orbit counts;
- a Gröbner computation without a certificate and saturation audit;
- the phrase "bounded complexity" without dimension and degree;
- a generic citation to Weil, Deligne, Katz, Bagshaw or Sawin–Shusterman;
- a pointwise Cauchy bound that recreates the first positive diagonal;
- a numerical corrected-amplitude trend.

## 17. Status at preregistration

### PROVED EXACTLY

- common-defect dichotomy and zero-defect classification;
- FRC1 root-cycle equivalence;
- AGL1 covariance and unique affine gauge in `q>=2k`.

### MACHINE-VERIFIED IDENTITY

- explicit `(11,3)` root equations;
- all 110 affine transforms and defect covariance;
- unique canonical gauge for the frozen counterexample.

### EMPIRICAL-EXACT FINITE PANEL

- cubic nonzero-defect orbit counts through `q=59`;
- apparent full affine orbits and bounded orbit count.

### OPEN

- `QZD_3`, `TFP_k`, `QZD_k`;
- `CBI_ND`, `OAC_FF`, corrected orbit amplitudes;
- `NDC_FF`, endpoint `FFPR`;
- theta restoration, conductor coupling, thinning;
- every integer transfer interface and Fortune's conjecture.
