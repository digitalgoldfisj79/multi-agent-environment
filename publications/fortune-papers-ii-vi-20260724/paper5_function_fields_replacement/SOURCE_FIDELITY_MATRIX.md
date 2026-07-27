# Replacement Paper V: frozen-source fidelity matrix

**Candidate source:** `manuscript.md`  
**Candidate SHA-256:** `e2fd325e81b0ed10241387f92b8f0df248c3dd0cedb84e4d9cf3a9a16cf836e4`  
**Lines:** 779  
**Date:** 2026-07-27

This matrix is a theorem-level fidelity audit. It does not itself confer publication status; the candidate must still pass manuscript-only hostile review and all compiled-artifact gates.

| Manuscript lines | Claim or section | Frozen source | Fidelity ruling |
|---:|---|---|---|
| 45--89 | Series bridge from Papers III--IV and no-transfer disclaimer | Paper III blob `06fe...`; Paper IV blob `1a3d...` | Accurate. Paper III ends at arithmetic transference; Paper IV covers random order only. No integer implication claimed. |
| 90--120 | Polynomial primorial and degree barrier | superseded Paper V elementary proof; independent reconstruction | Exact elementary proof. General Weil--RH window deliberately omitted. |
| 122--154 | `P_1=T^p-T`, exclusion of nonconstant linear offsets, crown threshold `I_4>p-1` | function-field programme definitions; strategy audit correction of degree-one micro-lemma | Correctly restricts the root argument to nonconstant linear offsets. Constant Artin--Schreier irreducibles supply exactly `p-1`. |
| 156--246 | Quadratic/cubic affine normal forms, orbit decomposition, `W_p`, failure certificate | `P_CYCLE_PROJECTOR_FIXED_POINT_AND_QLINE_BRIDGE_20260726.md`, blob `64d1...`, Section 4; independent census | Exact factors `p`, `p-1`, `1/2` preserved. Manuscript notation `N_sq,N_ns` is explicitly the source notation `N_+,N_-`. |
| 248--327 | Sparse ordered-root cone and global smoothness | `SPARSE_SURFACE_GLOBAL_SMOOTHNESS_AND_MIXED_CAYLEY_DIFFERENTIAL_20260726.md`, blob `802e...`, Sections 1--3; independent `p=7` enumeration | Proof reproduced. Open mixed-Cayley comparison excluded. Smoothness scoped to `p>=11`. |
| 329--390 | Affine cone transfer and exact absolute-Betti obstruction | `DISCRIMINANT_COMPONENT_AND_SAWIN_CONE_BETTI_OBSTRUCTION_20260726.md`, blob `e69b...`, Sections 1--5 | Exact shifts, Tate twists and factor `2` retained. `p=11` profile explicitly labelled computer-assisted. No claim against trace cancellation. |
| 392--464 | Exact sign-hook trace | `SIGN_HOOK_FULL_INTERVAL_TRACE_20260726.md`, blob `ab928...`, Sections 0--3 | Full collision proof reproduced with current sign convention. Admitted residue-class table agrees with source. |
| 466--499 | Alternating-hook projector | `P_CYCLE_PROJECTOR_FIXED_POINT_AND_QLINE_BRIDGE_20260726.md`, blob `64d1...`, Section 1; hostile audit blob `688f...` | Character normalisation exact; no missing factor of `p`. Independently checked on all cycle types for primes through 11. |
| 501--559 | `F sigma` fixed-point count, prime-power correction, primitive trace quantisation and circularity | same projector source, Sections 2--4; hostile audit | Uses affine `X_p`, not projective quotient. Extra `p` retained. Trace inequality stated only as an equivalence to crown. |
| 561--652 | q-coordinate, split/nonsplit normal forms, fixed-cell trace and class projectors | `NORMAL_FORM_CELL_LEDGER_20260724.md`, blob `1493...`; `HOOK_Q_LINE_CLASS_PROJECTORS_20260724.md`, blob `bb1f...` | Coordinate `q=-3/c`, sign `epsilon=A chi(q)`, boundaries `q=2,infinity`, factor `1/(2p)` all retained. Obsolete Airy transport language omitted. |
| 654--703 | Saturation-defect theorem and crown synthesis | `INVARIANT_QLINE_SATURATION_GAP_EQUALS_CUBIC_COUNT_20260726.md`, blob `1f2a...` | Exact identity and `2p` quantum retained. Correctly states nonsaturation as equivalent, not weaker. |
| 705--733 | Exact computation and reproducibility | new clean-room Python/C++ scripts and committed repository verifiers | Finite statements clearly labelled exact computer-assisted results; no asymptotic inference. |
| 735--760 | Closed routes and Paper VI boundary | post-PR19 programme status and hostile audits | Matches current stopping point: one-sided nonvanishing/Frobenius theorem. Does not restore obsolete two-Airy-gap narrative. |
| 762--778 | Disclosure and availability | publication protocol | Scope language is accurate; no peer-review or crown claim. |

## Normalisation audit

- Full interval: `T^p-T+aT^3+bT^2+cT+d`.
- Depressed fixed-class family: `T^p+aT^3+cT+d`.
- Manuscript `N_sq,N_ns` correspond to source `N_+,N_-`.
- Sign calculation uses `u=c-1` only inside Section 7.
- Arithmetic Frobenius convention matches the source trace formulas.
- Prime-power correction is `+p`, not zero and not `+p^2`.
- Cone transfer is `H_c^5=M(-1)`, `H_c^6=M(-2)`.
- q-line class formula has denominator `2p`; class sum has `-S_0/p`.
- The crown is `I_4>p-1`, equivalently `W_p>0`.

## Scope exclusions confirmed

The candidate contains no theorem asserting:

1. the superseded general Weil--RH Fortunate window;
2. the function-field crown for all primes;
3. an implication to integer Fortune;
4. an absolute Airy correlation theorem;
5. an Airy-to-Fortune bridge;
6. the open mixed-Cayley comparison;
7. generic `Q`-Gorenstein or Witt-rational properties of the later wild quotient.

## Internal fidelity verdict

**PASS FOR FROZEN MANUSCRIPT-ONLY HOSTILE REVIEW.**
