# Replacement Paper VI: frozen-source fidelity matrix

**Candidate source:** `manuscript.md`  
**Candidate Git blob:** `e50c8be02090519a693b67ca189f455a40fded49`  
**Candidate SHA-256:** `05fc66fb98d067d8fa5ea350d106fa4a3c794e1a9ffb3f51eee9f986995c5376`  
**Lines:** 768  
**Date:** 2026-07-27

| Manuscript lines | Claim or section | Frozen source | Fidelity ruling |
|---:|---|---|---|
| 56--88 | Input from Paper V and exact crown | replacement Paper V blob `78d8b8f30a2fc89b2f76940c86252e28bc828399` | Notation `N_2,N_sq,N_ns,W_p` inherited exactly; crown remains open. |
| 89--124 | Fixed-class Cartier moment and evidence boundary | `FIXED_CLASS_FIRST_MOMENT_AND_CYCLOTOMIC_TANGENT_WALL_20260726.md`, blob `b104...` | Pointwise cofactor identity retained. Uniform nonvanishing explicitly labelled empirical/open. |
| 125--183 | Translation and reciprocal q-line projectors | same source, Sections 2--3 | Coefficients, signs and `-3 q^{-1}` weight retained. No bounded-rank sheaf claim. |
| 184--226 | First cyclotomic tangent and three-mode form | same source, Sections 4--5 | Expansion modulo `pi^2`, `M_0=1`, and simultaneous-vanishing condition preserved. |
| 227--278 | Tangent module, Tate complex and Bockstein | `CYCLOTOMIC_TANGENT_TATE_COMPLEX_AND_DIVIDED_HOOK_PRECISION_OBSTRUCTION_20260726.md`, blob `48c6...` | Nontrivial extension, maps `pi,0`, one line in each parity and identity Bockstein preserved. |
| 279--321 | Frobenius ambiguity and precision shift | same source, Sections 5--7 | Family `Phi_lambda`, `p=u pi^(p-1)`, and required `pi^(p+1)` precision preserved. Two cyclic directions kept distinct. |
| 322--352 | Divided-hook character obstruction | `DIVIDED_HOOK_IS_NOT_A_PERFECT_COMPLEX_AND_SECONDARY_TRACE_TARGET_20260726.md`, blob `d6a0...` | `Theta_p=p*1-Reg`, fractional multiplicities and trace-level secondary formula preserved. |
| 353--392 | Hattori--Stallings coefficient trace | `SECONDARY_HATTORI_STALLINGS_TRACE_AND_ARTIN_SCHREIER_QUOTIENT_20260726.md`, blob `55fc...`, Sections 3--4 | Integral coefficient extraction and quotient-defect formula reproduced. No claim of automatic nonvanishing. |
| 393--478 | Free action, cyclic transfer, Artin--Schreier coordinate and irreducibility levels | same source, Sections 2,5--7 | Transfer normalisation, sign in `y=-U/a`, and `g=r` Frobenius-shift formula preserved. |
| 479--523 | No-split theorem and quotient count | same source, Section 8 | Logarithmic-derivative proof and restriction `p>5` preserved. |
| 524--585 | Kummer classification and common quotient | `KUMMER_TWIST_AND_PROJECTIVE_QUOTIENT_COMPACTIFICATION_OBSTRUCTION_20260726.md`, blob `fcb5...`, Sections 1--3 | Corrected Kummer, not universal quadratic-twist, formulation retained; factors of two preserved. |
| 586--634 | Unique projective fixed point and wild-local restriction | same source, Sections 4--5 | Unique progression point and isolated wild quotient stated. Automatic `Q`-Gorenstein/Witt claims expressly excluded. |
| 635--686 | Compactified point-count ledger and congruence obstruction | same source, Sections 6--7 | Exact count, boundary, open and `p=17` positive congruence example retained. |
| 687--709 | Independent finite reconstruction | clean-room script/result blob `15c21...` | Exact regressions only; no uniform inference. |
| 710--767 | Terminal theorem and closed continuations | programme status blob `7111...` | Exact one-sided Frobenius/nonvanishing wall. Crown and integer conjecture not claimed. |

## Normalisation audit

- Paper V notation `N_sq,N_ns` is used throughout.
- `M_a` is an element of `F_p`, not an integer-valued count.
- Coefficient cyclic group and root-cycle group are never identified.
- The raw hook trace is `H_a=p F_a`.
- `N_a` appears at `pi^(p-1)` and `M_a` at `pi^p`.
- Hattori--Stallings extraction has factor `p`, not `1/p` on the ordinary trace side.
- Artin--Schreier level `g=r` uses arithmetic Frobenius.
- Kummer stabiliser order over `F_p` is two.
- Compactified count is `1+(p-1)W_p`.
- No local claim about resolution of the wild quotient is imported.

## Scope exclusions confirmed

The candidate does not assert uniform first-moment nonvanishing, a divided-hook perfect complex, rational-point existence from trace-surjectivity, a universal quadratic sign twist, automatic Witt-rationality, or a proof of the crown.

## Internal fidelity verdict

**PASS FOR FROZEN MANUSCRIPT-ONLY INDEPENDENT REFEREE REVIEW.**
