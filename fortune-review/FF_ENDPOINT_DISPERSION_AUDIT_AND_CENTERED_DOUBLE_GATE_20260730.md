# Function-field endpoint audit: the diagonal floor and the centered bilateral gate

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`  
Independent audit target: Fable commits through `926ec1a31cc284bd1071d40d9783bb7e933b0e36` and the complete recent PR #33 discussion.

Companion verifier: `fortune-review/scripts/ff_endpoint_centered_dispersion_audit.py`  
Frozen output: `fortune-review/data/ff_endpoint_centered_dispersion_audit.json`

## 0. Decisive result

The function-field route is materially narrower, but endpoint `FFPR` is not proved.

The new theorem-level obstruction is:

> **First-dispersion diagonal-floor obstruction.** Any proof that first applies positive Cauchy in one source and then bounds the resulting class correlation by `O(Diag)` is confined to `q^(3m/2+k) poly`, leaving `q^((m-k)/2)` above `FFPR`, or `q^((k-1)/2)` at `m=2k-1`. The missing saving cannot be recovered by estimating the same positive second moment more sharply up to a constant. The assembly must be centered before positivity or remain genuinely signed in both source variables.

This is **PROVED EXACTLY** by the exponent ledger below. It corrects the mechanism-map suggestion that class absorption plus an ordinary second dispersion is sufficient.

A second correction is also mandatory: the existing dispersion computation treats the uncorrected product aggregate, whereas the exact completed target contains the explicit `f=f'` subtraction `Delta_PS`. The correction is nonzero on every audited panel and must be retained or separately controlled.

The smallest remaining target is therefore a **Lambda-weighted, diagonally centered bilateral endpoint assembly theorem**, not a standalone pointwise `FFV-generic` theorem and not merely `C(theta)=O(Diag)`.

## 1. Independently verified Fable structure

The following Fable results were rederived and accepted.

### PROVED EXACTLY

1. Canonical completion frequencies: `deg theta < 2k-R`.
2. Source separability at fixed `theta`.
3. Local form
   
   `Ahat_P(mu)=sum_{deg f=m} Lambda(f) psi_P(mu f)`,  
   `mu=-theta Lbar_P Sbar_P mod P`.
4. The algebraically trivial local locus is empty for nonzero canonical `theta`.
5. Exact Plancherel:
   
   `sum_{mu != 0}|Ahat_P(mu)|^2 = q^k sum_r |N_P(r)-q^(m-k)|^2`.
6. One-source completion dichotomy and endpoint diagonal/multiplicative-class classification.
7. Affine theta-independence for `L=t^q-t`, Galois orbit-trace structure and integrality of the class aggregate.

### RETRACTED OR CORRECTED

1. Fixed-source Theorem D and its unexplained `q^-m` factor remain retracted.
2. `C(theta)<=Diag` and a universal factor-2 second-moment bound are not theorems; they are finite-panel observations.
3. The all-frequency Plancherel mass is on the `q^(m+k)` scale in the relevant regime. Wording assigning the left-hand side the `q^m` scale drops the exact factor `q^k`; only the unmultiplied residue variance is on the `q^m` scale.
4. Keating–Rudnick applies to the all-residue variance in its stated large-field/fixed-degree regime. It does not prove deterministic sampled-frequency bounds, uniformity with growing `k,m`, or the prime-pair assembly.
5. The existing first-dispersion verifier computes the product aggregate without the `Delta_PS` correction.

## 2. Literal exponent ledger

Let the number of ordered degree-`k` prime pairs be `~q^(2k)/k^2`. Plancherel and band sampling place

`sum_{P!=S}|Ahat_P(mu_PS)|^2`

on the scale

`q^(m+2k) poly(k,m)`.

After expanding in the second source and applying Cauchy against

`sum_{deg f=m} Lambda(f)^2 <= m q^m`, 

the completed second moment has diagonal

`q^m * q^(m+2k) = q^(2m+2k)`.

Taking the square root after source Cauchy gives

`|T(theta)| << q^(3m/2+k) poly(k,m)`.

The target is

`q^(m+3k/2) poly(k,m)`.

The exact deficit is therefore

`q^((m-k)/2)`.

At `m=2k-1` this becomes

`q^((k-1)/2)`.

No estimate of the form `|C(theta)| <= A*Diag` with `A=poly(k,m)` changes this exponent. It can at most change the constant multiplying the positive diagonal floor.

## 3. Why a second dispersion must be centered

The phrase “disperse in the second source” is ambiguous. Two different operations must be separated.

1. **Invalid as a closing argument:** first form the positive one-source second moment, retain its full diagonal, and then apply another Cauchy or upper bound. The diagonal floor is already present and survives.
2. **Potentially closing:** derive a bilinear identity in which both source Gram diagonals and the explicit `Delta_PS` term are subtracted before positivity, then exploit exact reciprocity and the simultaneous completion incidence.

The second operation is a new theorem. It is not contained in D1–D3.

## 4. The actual corrected endpoint aggregate

For ordered distinct degree-`k` primes `P,S`, set

`mu_PS=-theta Lbar_P Sbar_P mod P`,  
`nu_SP=-theta Lbar_S Pbar_S mod S`.

The exact separated aggregate is

`T_corr(theta) = sum_{P!=S} [Ahat_P(mu_PS) Ahat_S(nu_SP)-Delta_PS] psi_theta(-t^R)`.

Here `Delta_PS` is the exact `f=f'` contribution. The old dispersion verifier's `T` omits it.

### EMPIRICAL-EXACT FINITE PANEL

For `L=t^q-t`, `k=2`, `m=R=3`, `theta=1`, exact arithmetic in `Z[zeta_q]` gives:

| q | ordered pairs | `|product aggregate|` | `|Delta aggregate|` | `|T_corr|` | `|T_corr|/q^(m+3k/2)` |
|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 216 | 54 | 270 | 0.3704 |
| 5 | 90 | 6250 | 1350 | 7600 | 0.4864 |
| 7 | 420 | 30870 | 8918 | 39788 | 0.3382 |
| 11 | 2970 | 921052 | 98252 | 1019304 | 0.5754 |

These values are exact cyclotomic sums; the displayed absolute values are numerical evaluations of exact vectors. They show only that the omitted correction is not identically zero or negligible by identity. They do not establish an asymptotic bound.

## 5. Simultaneous endpoint incidence

For pair indices `a=(P,S)` and `b=(P',S')`, the two source completions impose

`deg(nu_a S' - nu_b S) <= 2k-m-1`

and

`deg(mu_a P' - mu_b P) <= 2k-m-1`.

At the endpoint the threshold is zero. The first condition alone produces the known multiplicative class family. The second is its reciprocal counterpart. Their intersection is the geometric support relevant to a centered bilateral dispersion.

### EMPIRICAL-EXACT FINITE PANEL

The independent verifier enumerates the simultaneous incidence exactly:

| q | k | m | pair count | first-source incidences | second-source incidences | simultaneous | diagonal | transpose | other |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 3 | 6 | 12 | 12 | 6 | 6 | 0 | 0 |
| 5 | 2 | 3 | 90 | 150 | 150 | 90 | 90 | 0 | 0 |
| 7 | 2 | 3 | 420 | 1092 | 1092 | 420 | 420 | 0 | 0 |
| 3 | 3 | 5 | 56 | 64 | 64 | 58 | 56 | 2 | 0 |

Thus each one-sided class family collapses almost completely under the reciprocal condition in the audited panels. At `k=2` it collapses to the diagonal; at the first `k=3` panel only a transpose pair survives beyond the diagonal.

This is a useful discovery and falsification target. It is not an asymptotic theorem. The next proof must classify the simultaneous incidence for general `q,k`, including stabilizers, transpose components and any exceptional subvarieties.

## 6. Exact theorem now required

A sufficient endpoint theorem can be stated without demanding unnecessary pointwise control of every `Ahat_P(mu)`.

### OPEN — Centered bilateral endpoint assembly (`CBEA_FF`)

Uniformly for:

- prime powers `q` in the chosen asymptotic regime;
- degree-`k` monic irreducibles `P,S` with `P!=S`;
- `m=2k-1` and `k<=R<=2k-1`;
- nonzero canonical `theta`, `deg theta<2k-R`;
- `L=t^q-t`, or unit punctures with polynomial dependence on `deg L`;

prove

`|T_corr(theta)| << q^(m+3k/2) poly(k,m,deg L)`.

A proof must expose a centered bilateral form whose off-diagonal support is the simultaneous incidence above, with:

1. both source Gram diagonals removed before positivity;
2. the exact `Delta_PS` retained;
3. von Mangoldt signs/weights retained rather than replaced by arbitrary coefficients;
4. exact residue reciprocity used before any absolute-value split;
5. conductor and degeneracy loci stated literally.

An equivalent theorem on the centered bilateral incidence kernel is acceptable if its exponent ledger yields exactly the missing `q^((m-k)/2)`.

## 7. Literature applicability audit

### PROVED FROM PUBLISHED INPUT

Keating–Rudnick proves the all-residue arithmetic-progression variance asymptotic in the large-field limit with the polynomial degrees in the theorem fixed. Under the dictionary `X=q^m`, `|Q|=q^k`, the Fortune laboratory range is `k<m<2k`; however, the theorem does not provide a deterministic theorem on the sampled set `mu_PS`, nor uniform asymptotics with `k,m` growing.

### RELEVANT BUT NOT A BLACK-BOX APPLICATION

Sawin–Shusterman proves cancellation for special trace-function sums and applications to primes; Bagshaw proves bilinear Kloosterman bounds and averaged-modulus consequences. Their objects support the plausibility of a bilinear reciprocity attack, but the present theorem has a moving prime-pair modulus, two reciprocal local parameters, a von Mangoldt product, the explicit diagonal subtraction and the simultaneous endpoint incidence. No literal theorem located supplies `CBEA_FF` with the required parameter uniformity.

The literature therefore changes the proof technology available, not the status label.

## 8. Consequences if `CBEA_FF` closes

Only then may one:

1. restore the canonical `theta` sum and prove the required function-field `T3` saving;
2. prove coset `PORC_FF`;
3. couple to higher-conductor signed terms;
4. state a complete-coset first-band theorem;
5. begin thinning from all monic centres to squarefree product families and then a chosen walk.

No complete-coset result is yet the literal Fortune analogue.

## 9. Integer extraction dictionary

| FF mechanism | Integer replacement | Current status | Loss |
|---|---|---|---|
| Exact affine completion | Poisson/incomplete completion | Partial | Boundary terms and no exact zero-error dichotomy. |
| Exact reciprocal residue identity | Kloosterman reciprocity/spectral summation | Partial | Smooth/incomplete ranges and prime-modulus restrictions. |
| Simultaneous incidence rigidity | Integer determinant/congruence classification | OPEN | Potential semiprime resonances and no affine geometry. |
| Weil/Katz or trace-function cancellation | GRH-shaped/spectral bilinear cancellation | OPEN in required family | Must supply the whole logarithmic reserve. |
| Affine/Galois orbit traces | Character orthogonality/arithmetic symmetries | Partial | No analogue forcing primorial-orbit equidistribution. |
| Complete coset fairness | Consecutive primorial sampling | OPEN | `PORS` and `PORC/T3`. |

This is not a transfer theorem.

## 10. Boundary table

### PROVED EXACTLY

- Fable separability/local-character identities listed in Section 1;
- exact Plancherel normalization including the factor `q^k`;
- the first-dispersion diagonal-floor obstruction;
- the necessity of retaining `Delta_PS` in the exact target.

### PROVED FROM PUBLISHED INPUT

- all-residue variance scale in Keating–Rudnick's literal large-field/fixed-degree regime.

### MACHINE-VERIFIED IDENTITY

- independent Plancherel equality on `q=3,5,7` panels;
- exact cyclotomic decomposition of product, correction and corrected aggregate;
- exact simultaneous-incidence counts.

### EMPIRICAL-EXACT FINITE PANEL

- the corrected aggregate values and ratios;
- double-incidence rigidity on the four listed panels;
- `C<=Diag` on previously committed panels.

### CONDITIONAL

- D3 under sampled class-term `FFV` assumptions;
- any coset `PORC_FF` consequence from endpoint `FFPR`.

### RETRACTED OR CORRECTED

- universal factor-2 class bound;
- left-hand Plancherel mass stated as `q^m`;
- ordinary post-Cauchy double dispersion as a claimed automatic recovery of `q^((k-1)/2)`;
- dispersion tests that identify the uncorrected product with the exact completed target.

### OPEN

- general simultaneous-incidence classification;
- `CBEA_FF` / corrected endpoint `FFPR`;
- uniform class control or its absorption in the centered theorem;
- theta summation, coset `PORC_FF`, conductor coupling and thinning;
- every integer `T3` interface and Fortune's conjecture.

## Verdict

The function-field route is closer in the sense that the failure of the first dispersion is now exactly diagnosed and the relevant bilateral incidence is explicit. It is not closer by virtue of a proved endpoint estimate: the endpoint theorem remains open. The next new mathematics is a centered, Lambda-weighted bilateral reciprocity theorem on the simultaneous prime-pair incidence, with the exact diagonal correction retained.
