# Fortune mechanism map — corrected authoritative boundary

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`  
Audit base: branch head `72d821630cd5f32a2f31f7a73f1b124bf508b66f`; Fable mechanism-map commit `926ec1a31cc284bd1071d40d9783bb7e933b0e36`.

This document supersedes the future-dated synthesis `FORTUNE_MECHANISM_MAP_20260801.md`. It preserves that document's useful causal organization while correcting its scope and theorem labels.

## 1. Primary integer causal chain

```text
Fortune's conjecture
  ⇐ prime below the square threshold
  ⇐ prime-pair detection (m, P_j+m)
  ⇐ Hardy–Littlewood-strength block variance
  ⇐ primorial-orbit discrepancy covariance
  ⇐ signed first-physical-band cross-modulus T3 cancellation
```

The status of the links is:

1. **PROVED EXACTLY.** Below `p_{n+1}^2`, candidate collapse converts a valid Fortune offset into a prime offset. The target becomes detection of a pair `m` and `P_j+m` with both entries prime.
2. **PROVED EXACTLY as a reduction; estimate OPEN.** The one-failure argument reduces blockwise detection to a variance estimate beating the trivial scale by `o(log X)`.
3. **PROVED EXACTLY.** The two-level Heath–Brown identity, punctured-centre transport and true-range completion convert the first physical coordinate to
   
   `A_{j,p} = -(p-1)/(p-2) D_p(-P_j) + log(p)/(p-2)`.
4. **PROVED EXACTLY.** The cross-modulus physical kernel splits into `T1+T2+T3`.
5. **OPEN.** `T3` contains the remaining open analytic content of the **first physical-band cross-modulus covariance**. It is not the entirety of the full signed detector.
6. **OPEN after T3.** Signed physical/higher-conductor contraction and survivor-martingale recombination remain separate interfaces before the block-variance theorem.

The physical-scale estimate, orbit sampling at random scale and Cauchy reach the Fortune allowance with zero reserve. The required `o(log X)` margin must therefore come from signed cross-modulus cancellation; no unsigned or separately positive surrogate is admissible.

## 2. Integer gates

| Gate | Status | Exact role |
|---|---|---|
| `PBDH_P(X)` | **OPEN** | All-residue prime-band variance at the required physical scale. Necessary scale gate, not the decision point. |
| `PORS(X)` | **OPEN** | Deterministic sampling of all-residue energy by consecutive primorial centres. |
| `PORC(X)` / physical `T3` | **OPEN** | Signed cross-modulus cancellation on the primorial orbit. First major integer abyss. |
| Higher-conductor contraction | **OPEN** | Retain cancellation across conductor/source variables after the physical band. |
| Block variance | **OPEN** | Hardy–Littlewood-strength detector variance. |
| Fortune | **OPEN** | Consequence only after all preceding interfaces close. |

GRH-shaped fixed-modulus information does not supply the required cross-modulus coherence. No current integer theorem found in the audited literature reaches this geometry.

## 3. Function-field laboratory: exact reductions

Work in `F_q[t]`, with degree-`k` prime moduli, source degree `m <= 2k-1`, monic centre degree `R`, and puncture `L`, including `L=t^q-t`.

The following are established.

- **PROVED EXACTLY:** the monic degree-`R` family is an affine coset and samples every residue modulo a single degree-`k` prime exactly fairly. Coset `PORS_FF` is an identity.
- **PROVED EXACTLY:** same-modulus distinct-character cross terms vanish past the relevant `L`-polynomial degree.
- **PROVED EXACTLY:** affine-subspace completion has canonical frequencies `deg theta < 2k-R`; the zero frequency cancels the centred density term.
- **PROVED EXACTLY:** at fixed nonzero `theta`, the source phase separates into two one-variable von Mangoldt additive twists
  
  `Ahat_P(mu)=sum_{deg f=m} Lambda(f) psi_P(mu f)`.
- **PROVED EXACTLY:** the sampled local frequency is nonzero throughout the family; there is no algebraically trivial local character.
- **PROVED EXACTLY:** Plancherel gives
  
  `sum_{mu != 0}|Ahat_P(mu)|^2 = q^k sum_r |N_P(r)-q^(m-k)|^2`.
  
  The full nonzero-frequency mass is consequently on the `q^(m+k)` scale in the relevant large-`q` regime. Keating–Rudnick supplies the asymptotic scale for the all-residue variance in its literal fixed-degree, large-field range; it does not prove the scale of the deterministic sampled subset `mu_PS`, sampled-frequency control, or a growing-parameter theorem.
- **PROVED EXACTLY:** one-source dispersion has an exact completion dichotomy and endpoint coincidence classes consisting of the diagonal plus multiplicative prime-pair classes.
- **PROVED EXACTLY:** for `L=t^q-t` at the endpoint, affine symmetry gives theta-independence; class terms decompose into Galois orbit traces and the aggregate class correlation is an integer.

## 4. Corrected endpoint boundary

Define the actual completed endpoint aggregate

`T_corr(theta) = sum_{P != S} [Ahat_P(mu_PS) Ahat_S(nu_SP) - Delta_PS] psi_theta(-t^R)`.

The target is

`|T_corr(theta)| << q^(m+3k/2) poly(k,m)`

uniformly in nonzero canonical `theta` and in the true primorial puncture.

Three corrections are load-bearing.

### 4.1 Class correlation is not uniformly bounded yet

Affine symmetry proves theta-independence, integrality and orbit-trace structure. It does **not** prove `C(theta) <= Diag` or a universal factor-2 second-moment estimate. Those inequalities are **EMPIRICAL-EXACT FINITE PANEL** observations only.

### 4.2 Exact positive diagonal and the sampled-frequency alternative

The first dispersion contains the exact positive diagonal

`q^m M_samp(theta)`,  where  `M_samp(theta)=sum_{P!=S}|Ahat_P(mu_PS)|^2`.

If `M_samp` has its natural sampled scale `q^(m+2k) poly`, source Cauchy yields

`|T| << q^(3m/2+k) poly(k,m)`.

Against `q^(m+3k/2)`, the deficit is `q^((m-k)/2)`, hence `q^((k-1)/2)` at `m=2k-1`. Thus `C=O(Diag)` **alone** cannot imply endpoint `FFPR`: it must be accompanied either by the much stronger sampled-diagonal estimate

`M_samp(theta) << q^(3k) poly(k,m)`

or by a centered signed assembly that avoids paying the positive diagonal. The natural scale of `M_samp` is supported by the committed panels and by the all-frequency variance heuristic, but is not an unconditional lower bound on the deterministic sampled subset.

### 4.3 The explicit diagonal correction must remain in the theorem

The earlier dispersion verifier estimated the uncorrected product aggregate. The exact `f=f'` correction `Delta_PS` is nonzero and is not automatically absorbed by that computation. It must either be bounded at the target scale or retained inside a signed, diagonally centered bilateral assembly.

## 5. New exact target: sampled diagonal or centered bilateral endpoint assembly

The corrected boundary has two logically possible routes.

1. **Sampled-diagonal route:** prove the exceptional deterministic estimate `M_samp(theta) << q^(3k) poly` together with adequate class control and the `Delta_PS` correction.
2. **Centered bilateral route (`CBEA_FF`):** prove a Lambda-weighted, diagonally centered bilateral dispersion estimate on ordered prime pairs, retaining the signed source structure before positivity.

For the bilateral route, the parameter space is:

- `P,S,P',S'` monic irreducibles of degree `k`, with `P != S` and `P' != S'`;
- source degree `m=2k-1`;
- nonzero canonical `theta`, `deg theta < 2k-R`;
- puncture `L=t^q-t` or a unit puncture with polynomial conductor dependence;
- local parameters `mu_PS=-theta Lbar_P Sbar_P` and `nu_SP=-theta Lbar_S Pbar_S`.

The bilateral completion incidence is the simultaneous locus

`deg(mu_PS P' - mu_P'S' P) <= 2k-m-1`

and

`deg(nu_SP S' - nu_S'P' S) <= 2k-m-1`.

The required estimate must subtract both single-source Gram diagonals before positivity, retain the `Lambda` weights and `Delta_PS`, and yield the missing `q^((m-k)/2)` saving at the natural sampled scale. A second Cauchy inequality applied after the first positive diagonal has been formed cannot do this.

**EMPIRICAL-EXACT FINITE PANEL:** the initial panels are diagonal only for `(k,m)=(2,3)` at `q=3,5,7`; `(q,k,m)=(3,3,5)` has two transpose incidences; and `(5,3,5)` is again diagonal only. However, `(q,k,m)=(3,4,7)` has 12 genuine non-diagonal, non-transpose incidences, forming two `AGL(1,3)` orbits of size six. Thus the naive universal diagonal/transpose rigidity conjecture is **FALSIFIED**. The theorem must classify and control exceptional components rather than assume they are absent.

## 6. Function-field route after the endpoint gate

Only after one of the two endpoint routes is proved may the programme:

1. sum the canonical `theta` frequencies and prove coset `PORC_FF`;
2. couple the physical result to the remaining signed conductor terms;
3. obtain a complete-coset first-band theorem;
4. thin centres in the order
   
   `all monic degree-R -> squarefree products of fixed-degree irreducibles -> thin product family -> chosen walk`.

The complete-coset theorem must not be called the literal Fortune analogue before thinning. There is no canonical increasing order on equal-degree irreducibles, so a walk is an additional modelling choice and theorem.

## 7. Parallel crown / d=1 line

The crown or `d=1` function-field programme is a separate research line. It may share algebraic tools, but it is not a link in the primary integer variance chain and must not be counted as progress on integer `T3` without an explicit bridge.

## 8. Function-field / integer dictionary — not a transfer theorem

| Function-field input | Integer replacement required | Known theorem? | Exact loss or missing interface |
|---|---|---|---|
| Exact affine-subspace completion | Poisson or incomplete completion at primorial centres | Partial only | Boundary errors and no exact annihilator. |
| Exact residue reciprocity | Kloosterman reciprocity / spectral rearrangement | Partial only | Archimedean weights and incomplete ranges. |
| Weil/Katz cancellation | GRH-shaped, spectral or new bilinear prime cancellation | No theorem in required geometry | Cross-modulus coherence supplies the entire logarithmic margin. |
| Affine/Galois symmetry of `t^q-t` | Character orthogonality and arithmetic symmetries | Partial only | Primorial orbit is deterministic and non-affine. |
| Finite class-main-term extraction | Exact integer density/main-term subtraction | Partial only | Must retain signs across conductor and source variables. |
| Complete coset sampling | Consecutive primorial-orbit sampling | No | `PORS(X)` and `PORC(X)` are open. |

This table is a mechanism dictionary only. No function-field-to-integer transfer theorem is known.

## 9. Authoritative status

### PROVED EXACTLY

Candidate collapse; one-failure reduction; integer first-coordinate and physical kernel identities; function-field coset fairness, completion, separability, local nondegeneracy, Plancherel identity, one-source completion dichotomy, affine theta-independence and orbit-trace integrality; the exact first-dispersion positive-diagonal identity; and the logical insufficiency of class control alone.

### PROVED FROM PUBLISHED INPUT

Keating–Rudnick's all-residue variance asymptotic in its stated fixed-degree, large-`q` regime only.

### MACHINE-VERIFIED IDENTITY

Independent finite checks of the exact identities and corrected aggregate decomposition.

### EMPIRICAL-EXACT FINITE PANEL

`C/Diag <= 1` on the committed panels; exact cyclotomic values of the actual corrected aggregate; the natural sampled-diagonal scale on the committed panels; and the listed simultaneous-incidence counts and affine exception orbits.

### CONDITIONAL

The `q^((m-k)/2)` first-dispersion deficit, conditional on the natural sampled scale `M_samp ~ q^(m+2k) poly`.

### RETRACTED OR CORRECTED

The uncentred integer `SDD`; fixed-source Theorem D; the unexplained `q^-m`; a universal factor-2 class bound; an unconditional first-dispersion diagonal-floor exponent claim; the claim that ordinary double dispersion after first Cauchy automatically recovers the endpoint deficit; the claim that coset `PORC_FF` is already Fortune in the laboratory; any universal diagonal-or-diagonal-plus-transpose classification of the bilateral incidence.

### OPEN

The sampled-diagonal estimate at the exceptional `q^(3k)` scale or a centered bilateral replacement; a general classification and estimate for exceptional bilateral-incidence components; uniform class-main-term control or exact absorption; the `Delta_PS` contribution; corrected `FFPR`; coset `PORC_FF`; signed conductor coupling; every thinning step; integer `PBDH_P`, `PORS`, `PORC/T3`, higher-conductor contraction, block variance and Fortune's conjecture.
