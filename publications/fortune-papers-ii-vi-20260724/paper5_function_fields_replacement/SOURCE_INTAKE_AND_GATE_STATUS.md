# Replacement Paper V: source intake and gate status

**Working title:** *Fortunate Polynomials over Finite Fields: Exact Normal Forms, Sparse Geometry, and the Function-Field `d=1` Crown*  
**Date opened:** 2026-07-27  
**Status:** Gate 1 — source intake in progress. No manuscript prose is frozen.

## Series inputs

| Source | Role | Git blob | Status |
|---|---|---:|---|
| `paper3_pair_sum/manuscript.md` | Establishes the integer-side arithmetic transference boundary | `06fe9116d42fd056bf9727dfbaa63ccb7398562d` | Frozen predecessor manuscript |
| `paper4_random_order/manuscript.md` | Proves the random-order model and isolates increasing-order derandomisation | `1a3d39d974bfa37d31c100f536dcaa1b74f6d688` | Internal technical pass |

Paper V must state the logical bridge from these two papers and must not imply that the function-field programme proves or formally transfers to the integer conjecture.

## Primary mathematical proof sources

Research branch: `gpt56/fortune-strategy-synthesis-audit-20260726`.

| Source file | Load-bearing content | Git blob | Provisional claim class |
|---|---|---:|---|
| `frontier/strategy/P_CYCLE_PROJECTOR_FIXED_POINT_AND_QLINE_BRIDGE_20260726.md` | Exact full-interval orbit decomposition; crown variable `W_p`; failure certificate; alternating-hook projector; fixed-point circularity; q-line bridge | `64d1fabc14372bfc75807470c4f1c6c6a4efa565` | PROVED plus exact finite regression |
| `frontier/strategy/SPARSE_SURFACE_GLOBAL_SMOOTHNESS_AND_MIXED_CAYLEY_DIFFERENTIAL_20260726.md` | Global smoothness of the sparse projective surface; complete-intersection structure; Lefschetz concentration | `802eb3f59a461605cb2977099d85310b372751c4` | PROVED; mixed-Cayley comparison remains open and must be excluded from theorem claims |
| `frontier/strategy/INVARIANT_QLINE_SATURATION_GAP_EQUALS_CUBIC_COUNT_20260726.md` | Exact q-line ledger, saturation-defect identity, quantised gap and equivalence to cubic positivity | `1f2a670ccfa5bf5477b232bf7711b5bf11fd46d2` | PROVED |
| `frontier/strategy/DISCRIMINANT_COMPONENT_AND_SAWIN_CONE_BETTI_OBSTRUCTION_20260726.md` | Affine cone transfer, exact nontrivial Betti contribution and discriminant-component support | pending intake | PROVED / exact computer-assisted components; must be re-audited for manuscript scope |
| `frontier/strategy/SIGN_HOOK_FULL_INTERVAL_TRACE_20260726.md` | Sign endpoint and full-interval trace normalisation | pending intake | PROVED subject to current sign convention audit |
| `frontier/strategy/P_CYCLE_FIXED_POINT_CIRCULARITY_HOSTILE_AUDIT_20260726.md` | Hostile review of the projector/fixed-point chain | pending intake | AUDIT SOURCE |
| `frontier/strategy/DISCRIMINANT_COMPONENT_SAWIN_CONE_HOSTILE_AUDIT_20260726.md` | Hostile audit of the cone/Betti chain | pending intake | AUDIT SOURCE |

## Required Paper V theorem inventory

The manuscript may not be drafted as final until the following have complete proof-source rows and independent reconstruction records:

1. Polynomial primorial definition and degree barrier.
2. Exact `d=1` full interval.
3. Affine normal forms and definitions of `N_2`, `N_+`, `N_-`.
4. Exact orbit decomposition
   \[
   I_4=(p-1)+p(p-1)N_2+\frac{p(p-1)}2(N_++N_-).
   \]
5. Crown variable and failure certificate
   \[
   W_p=N_2+\frac{N_++N_-}{2},
   \qquad W_p>0,
   \qquad W_p=0\iff N_2=N_+=N_-=0.
   \]
6. Sparse ordered-root surface and global smoothness.
7. Lefschetz concentration of nontrivial representation sectors.
8. Alternating-hook `p`-cycle projector.
9. Fixed-point formula
   \[
   \#\operatorname{Fix}(F\sigma\mid X_p)=pI_4+p.
   \]
10. Proof that the proposed direct trace inequality is exactly equivalent to the crown.
11. q-line class-sum/class-difference ledger.
12. Saturation identity
    \[
    S_0^{\mathrm{sat}}-S_0=p(N_++N_-).
    \]
13. Precise terminal theorem: a genuinely one-sided nonsaturation statement remains open.

## Exclusions from replacement Paper V

The following must not be presented as the paper's endpoint:

- the superseded general Weil-RH window without a full independent proof;
- the early master-incidence/Kloosterman narrative as the principal reduction;
- the claim that an absolute Airy correlation theorem and an Airy transport theorem are the two terminal gaps;
- any mixed-Cayley comparison that remains open;
- empirical scans as evidence of a uniform theorem.

## Independent reconstruction queue

- [ ] Reconstruct the affine orbit decomposition and `W_p` crown formula from group actions.
- [ ] Reconstruct the sparse-surface Jacobian/singularity proof independently.
- [ ] Reconstruct the alternating-hook character evaluation and projector normalisation.
- [ ] Reconstruct the `F\sigma` fixed-point count directly from Frobenius orbits.
- [ ] Reconstruct the q-line saturation identity and boundary implication.
- [ ] Cross-check all exceptional primes and sign conventions.
- [ ] Freeze exact verification scripts and outputs used in the manuscript.

## Gate ledger

- [x] Superseded manuscript frozen for provenance.
- [x] Clean replacement directory opened.
- [x] Series dependency identified.
- [ ] Complete source manifest.
- [ ] Claim-status ledger.
- [ ] Independent reconstruction.
- [ ] Self-contained manuscript.
- [ ] Frozen source hash and fidelity matrix.
- [ ] Manuscript-only hostile review.
- [ ] Findings disposition and refreeze.
- [ ] Canonical PDF/DOCX build.
- [ ] Extraction, preflight, accessibility and page-level visual QA.
- [ ] Checksums, release ZIP and Zenodo metadata.
- [ ] Internal technical pass.
- [ ] External human specialist review.
