# Replacement Paper VI: source intake and gate status

**Working title:** *Secondary Traces and Kummer Quotients for the Function-Field Fortune Crown*  
**Date opened:** 2026-07-27  
**Status:** Gate 1 — clean-room source intake and independent reconstruction.

## Frozen predecessor input

Replacement Paper VI inherits the notation and crown theorem of replacement Paper V:

\[
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2},
\qquad W_p>0.
\]

It must not silently revert to the old `N_+`, `N_-` notation in compiled artefacts. The existing Airy manuscript is a superseded technical draft and is not an input to the main theorem chain except where a historical obstruction is explicitly cited.

## Primary proof sources

Research branch: `gpt56/fortune-strategy-synthesis-audit-20260726`.

| Source | Load-bearing content | Git blob | Status |
|---|---|---:|---|
| `FIXED_CLASS_FIRST_MOMENT_AND_CYCLOTOMIC_TANGENT_WALL_20260726.md` | Cartier cofactor moment, translation projector, reciprocal q-line moment, cyclotomic tangent, three-mode form | `b104d985719a677e40031ffea5855b862e73d136` | PROVED; moment nonvanishing OPEN |
| `CYCLOTOMIC_TANGENT_TATE_COMPLEX_AND_DIVIDED_HOOK_PRECISION_OBSTRUCTION_20260726.md` | tangent extension, Tate complex, Bockstein, Frobenius ambiguity, `pi^(p+1)` precision obstruction | `48c657379047544d921620848cf549da9edf3d4e` | PROVED |
| `DIVIDED_HOOK_IS_NOT_A_PERFECT_COMPLEX_AND_SECONDARY_TRACE_TARGET_20260726.md` | `Theta_p=p*1-Reg`, no ordinary divided-hook character, exact secondary moment formula | `d6a060daa320735a039ed6912508f33c92780351` | PROVED |
| `SECONDARY_HATTORI_STALLINGS_TRACE_AND_ARTIN_SCHREIER_QUOTIENT_20260726.md` | Hattori--Stallings coefficient extraction, cyclic transfer, Artin--Schreier coordinate, irreducibility section, no-split theorem | `55fc19ba40841ef1a8a7ddc421800374ee34a383` | PROVED; rational-point existence OPEN |
| `SECONDARY_TRACE_ARTIN_SCHREIER_HOSTILE_AUDIT_20260726.md` | hostile audit and scope restrictions on secondary trace/quotient chain | pending intake | AUDIT SOURCE |
| `KUMMER_TWIST_AND_PROJECTIVE_QUOTIENT_COMPACTIFICATION_OBSTRUCTION_20260726.md` | Kummer forms, sign-twist correction, common quotient, unique projective fixed point, exact compactified counts | `fcb5bbeecd03f53850f7f10be00c82eab243b90c` | PROVED; wild local singularity properties OPEN |
| `KUMMER_TWIST_COMPACTIFICATION_HOSTILE_AUDIT_20260726.md` | hostile audit and retraction of automatic quotient general-type claims | pending intake | AUDIT SOURCE |
| `PROGRAMME_STATUS_AFTER_KUMMER_TWIST_COMPACTIFICATION_AUDIT_20260726.md` | authoritative terminal theorem and closed continuations | `711159cc6d64f9f859276cbb491ca7e9894b9094` | STATUS SOURCE |

## Required theorem inventory

1. Fixed-class first moment `M_a` and Cartier cofactor identity.
2. Full-family translation projector and reciprocal q-line moment.
3. First cyclotomic tangent `(F_a-N_a)/pi=M_a mod pi`.
4. Nonsplit tangent `k[C_p]` extension, Tate complex and Bockstein.
5. Frobenius tangent ambiguity and Smith blindness.
6. Precision shift `H_a=pF_a`, with `N_a` at order `pi^(p-1)` and `M_a` at order `pi^p`.
7. Character identity `Theta_p=p*1-Reg`.
8. Nonexistence of an ordinary characteristic-zero divided-hook complex.
9. Hattori--Stallings coefficient formula `Tr_Z(Phi sigma^{-r})=p h_r`.
10. Free root-cycle action on every nonzero cubic slice.
11. Explicit cyclic transfer and coordinate `sigma(y)=y+1`.
12. Artin--Schreier quotient `T^p-T=g`.
13. Exact `g=r` Frobenius-shift interpretation and `g=1` irreducibility section.
14. No-split theorem and `#Y_a(F_p)=(p-1)N_a` for `p>5`.
15. Kummer classification by `H^1(F_p,mu_(p-3))`.
16. Sign represents the nontrivial form iff `p=1 mod 4`.
17. Common quotient counts `#D_p=(N_sq+N_ns)/2` and `#U_p=(p-1)(N_sq+N_ns)/2`.
18. Unique projective root-cycle fixed point `[0,1,...,p-1]`.
19. Exact compactified count `#Q_p=1+(p-1)W_p` and boundary formula.
20. Proof that a standard `1 mod p` point congruence cannot distinguish failure from success.
21. Exact remaining one-sided compactly-supported Frobenius/nonvanishing theorem.

## Required scope restrictions

- First-moment nonvanishing is empirical, not proved.
- The Hattori--Stallings formula constructs the trace carrier; it does not itself force nonvanishing.
- The Artin--Schreier coordinate alone does not force the `g=1` level to have a rational point.
- The two arithmetic classes are Kummer forms, not universally quadratic sign twists.
- The modular quotient has one isolated wild singularity. `Q`-Gorenstein, discrepancy, Witt-rational and resolution claims are not assumed.
- A standard proper-point congruence is insufficient even under favourable hypotheses.
- The crown remains open.

## Gate ledger

- [x] Superseded Paper VI frozen for provenance.
- [x] Clean replacement directory opened.
- [x] Paper V notation inherited.
- [ ] Complete source manifest.
- [ ] Claim-status ledger.
- [ ] Independent reconstruction.
- [ ] Self-contained manuscript.
- [ ] Frozen hash and fidelity matrix.
- [ ] Manuscript-only independent referee review.
- [ ] Findings disposition and refreeze.
- [ ] Canonical PDF/DOCX build.
- [ ] Extraction, preflight, accessibility and page-level visual QA.
- [ ] Checksums, release ZIP and Zenodo metadata.
- [ ] Internal technical pass.
- [ ] External human specialist review.
