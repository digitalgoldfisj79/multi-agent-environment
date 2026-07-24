# Rebuilt Paper IV fidelity matrix

## Exact objects compared

- Frozen proof source: `RQM_PROOF.md`, blob `53f63f662f5a9d6e750a592ba8bcba6cf4bc9095`, branch `gpt56/d1-gate-bridge-terminal-20260724`.
- Final rebuilt manuscript: `publications/fortune-papers-ii-vi-20260724/paper4_random_order/manuscript.md`, publication branch head after final repairs, blob `c0e9d84769fddaea77219313c10c0aaf6cf0295c`, SHA-256 `f6c6ad4faa9386cc2e3f9044f475d4a700a671d41a873b6c98b5159b2c6fa44f`.
- Editorial rule: internal adjudication language, session-specific scratchpad paths, and non-load-bearing diagnostics were removed or moved to the verification section; no theorem hypothesis, exponent, multiplicity, or load-bearing proof step was intentionally weakened or strengthened.
- Source-integrity scan: 30,717 characters, 1,043 lines, no control characters and no unresolved editorial placeholders.

This is an editorial claim-level comparison. It does not itself certify the mathematical correctness of the frozen proof. Fresh hostile review of the final exact SHA-256 remains a separate gate.

## Claim and dependency map

| Load-bearing item | Frozen source | Rebuilt manuscript | Fidelity status | Notes |
|---|---|---|---|---|
| Random path, centres, pair indices, `N`, `M` | RQM §0 | §§1–2 | Verbatim-equivalent | Converted inline code notation to displayed mathematics. |
| Reciprocal weights `w`, `D_X`, `p`, `Psi`, `m` | RQM §0 | §2 | Verbatim-equivalent | `sum_{a>=1}m_a=1/2` and the zero-mass convention are explicit. |
| Fixed-harmonic energy and distinct-modulus decomposition | RQM §0 and §8 | §2, equations (2.1)–(2.2) | Verbatim-equivalent with expanded derivation | The equal- and unequal-modulus expansion is displayed term by term. |
| Frobenius comparison | RQM §0 and §8 | §2, equation (2.3), and §9 | Precise external dependency | The comparison is isolated and cited to Paper II; it is the only mathematical import not reproved in Paper IV. |
| Quantitative frame admissibility `(N1)` | RQM §0 | §2, `(N1)` | Verbatim-equivalent | Preserves `rho >= delta_rho` on `[1/2,1]`, necessity discussion, and use in diagonal/tail bounds. |
| Effective block-size bounds `(N2)` | RQM §0 | §2, equation (2.4) | Verbatim-equivalent | Same constants and consequences for `M`. |
| Theorem quantifiers and uniformity in `q,r,a,X,eta,rho` | RQM §0 | Theorem 2.1 and Proposition 2.2 | Verbatim-equivalent | Random-order expectation explicitly identified as cancellation source. |
| Path rigidity and unit multipliers | RQM §1 | Lemmas 3.1–3.2 | Verbatim-equivalent | Proofs retained. |
| Coefficient taxonomy | RQM §2, Lemma 2.1 | Lemma 3.3 | Verbatim-equivalent | All `m=2,3,4` patterns retained. |
| Sliding-family multiplicity and completeness identity | RQM §2, Lemma 2.2 | Lemma 3.4, equation (3.3) | Verbatim-equivalent | Direct expansion replaces the frozen polynomial check. |
| Exact ordered set-partition identity, including empty cells | RQM §3.1 | Lemma 4.1 | Verbatim-equivalent | Full coefficient-extraction proof retained. |
| Multivariate contour estimate and `C_*K^2` prefactor | RQM §3.2 | Lemma 4.2 | Verbatim-equivalent | Stirling prefactor and phase-uniform deficit proof retained. |
| Additive-slot factorisation | RQM §4 | §5, equation (5.1) | Verbatim-equivalent | All active slots retained. |
| Gauss/CRT expansion and coefficient norms | RQM §4, Lemma 4.1 | Lemma 5.1 | Verbatim-equivalent with expanded proof | Prime Gauss-sum facts are inlined. |
| Cell-character bookkeeping, empty-`W_0` collapse, non-collapsing tail slot | RQM §4 | §5, equations (5.4)–(5.6) | Verbatim-equivalent | Former synopsis omissions are explicit. |
| One-slot and two-slot group norms | RQM §4, Lemma 4.2 | equations (5.7)–(5.8) | Verbatim-equivalent | Same sup and `l1` costs. |
| Sixth-moment exceptional-character count | RQM §5 | Lemma 5.2 | Verbatim-equivalent with expanded counting proof | Unit support, congruence-to-equality and the `6K^3` count are explicit. |
| Macro cell and ratio coordinates | RQM §6 | §6, equations (6.1)–(6.3) | Verbatim-equivalent | Front/back orphan distinctions retained. |
| Triangular coordinate bijection | RQM §6.1 | Lemma 6.1 | Verbatim-equivalent | Invertibility argument retained. |
| Good-coordinate contour decay | RQM §6, equation (6.1) | equation (6.4) | Verbatim-equivalent | Same `X^{-30f}` rate. |
| Path matching lemma | RQM §6.2 | Lemma 6.2 | Verbatim-equivalent | Outer-to-inner summation, no-orphan convention and one-use-per-edge accounting are explicit. |
| Pattern domination | RQM §6.3 | Lemma 6.3 | Verbatim-equivalent with expanded arithmetic | The exact ratio to the all-bad bound and the `X^{-23f}` margin are displayed. |
| Master per-configuration bound | RQM Proposition B | Proposition 6.4 | Verbatim-equivalent | Same orphan, bad-character, and edge-sup factors. |
| Trivial ledger classes `T1–T3` | RQM §7 | §7 | Verbatim-equivalent, partition clarified | Counts remain upper bounds of the same order. |
| `C1` all-big four-rank class | RQM §7 | equation (7.5) | Verbatim-equivalent | Same four one-slot savings. |
| Binding `C2a` interior-micro class | RQM §7 | equation (7.6) | Verbatim-equivalent | Same `N^3 w_0`, `beta^3`, and two `X^{-2}` savings. |
| Binding `C2b` front-orphan class | RQM §7 | equation (7.7) | Verbatim-equivalent | Orphan cost retained. |
| `C2c` empty initial cell | RQM §7 | equation (7.8) | Verbatim-equivalent | Slot-one collapse retained. |
| Binding `C2d` back-orphan/empty-tail class | RQM §7 | equation (7.9) | Verbatim-equivalent | Tail slot explicitly does not collapse. |
| `C3` all-big three-rank class | RQM §7 | equation (7.10) | Verbatim-equivalent | Same three coordinate savings. |
| `C4` all-big sliding/doubled class | RQM §7 | equation (7.11) | Verbatim-equivalent | Type-S multiplicity `N` retained. |
| Ledger exhaustiveness | RQM §7 | opening and closing paragraphs of §7 | Verbatim-equivalent, made disjoint | Every `(m,h)` case and unique-micro position is explicitly assigned. |
| No-cushion statement and source of exponent `9` | RQM §§7–8 | §8 | Verbatim-equivalent | Binding scale stated as `X^2 log^7 X = M log^9 X`. |
| Fixed-harmonic assembly and diagonal | RQM §8(i) | §9 through equation (9.1) | Verbatim-equivalent | `kappa <= m max p` and shell PNT retained. |
| Aggregate small-harmonic assembly | RQM §8(ii) | equation (9.2) | Verbatim-equivalent | Uses exact positive-harmonic mass `1/2` and zero-mass convention. |
| Schwartz tail | RQM §8(ii) | equation (9.3) | Verbatim-equivalent with expanded derivation | The Schwartz seminorm and `Ha/q >= a/2` estimate are displayed. |
| Frobenius assembly | RQM §8(ii) | final part of §9 | Verbatim-equivalent modulo precise Paper II citation | Same diagonal summation and aggregate comparison. |
| Effective constants and largeness conditions | RQM §8 constants ledger | §10 | Verbatim-equivalent | Numerical rates retained. |
| Verification status | RQM §9 | §10 | Faithful compression | Exact checks are described as non-proof validation. |
| Scope limitation | RQM header and §10 | §§1 and 11 | Verbatim-equivalent | Explicitly says no Fortune or increasing-order theorem. |
| LLM provenance | Audit correction and prior manuscript disclosure | disclosure after §11 | Strengthened disclosure | Rebuild and failed prior hostile review are disclosed. |

## Editorial changes that require no new mathematics

1. The earlier 207-line synopsis was replaced rather than patched.
2. Internal labels and scratchpad paths were removed.
3. The ledger was presented as an explicitly disjoint partition.
4. The algebraic identity in Lemma 3.4 is justified by direct expansion.
5. Standard prime Gauss-sum facts were expanded into a short proof.
6. The unused optional density-theorem strengthening was omitted.
7. Random-permutation averaging is stated alongside every no-GRH framing claim.
8. A malformed LaTeX backslash was found and corrected before the final hash.
9. The final hostile-review repairs added only definitions and intermediate derivations: zero-mass convention, exact square expansion, unit support in the sixth moment, no-orphan convention, pattern-ratio arithmetic, exhaustive ledger partition, and the explicit Schwartz-tail estimate.

## Independent ledger control

`INDEPENDENT_LEDGER_RECONSTRUCTION.md` independently enumerates all ordered pair configurations for `N=3,...,10`, checks the exact `N`-versus-`1` multiplicity dichotomy, and verifies the rebuilt disjoint ledger at three micro thresholds. All panels passed. The independent exponent reconstruction again identifies `C2a`, `C2b`, and `C2d` as exactly binding.

## Current gate assessment

- Frozen-source-to-manuscript dependency coverage: **editorially complete for final SHA-256 `f6c6ad4f…6fa44f`**.
- Independent reconstruction of the binding ledger: **completed and passed**.
- Fresh evidence-constrained hostile review of the final exact SHA-256: **submitted; result not yet frozen in this record**.
- DOCX/PDF/ZIP generation and source-to-binary fidelity: **not yet performed**.
- Human specialist circulation: **not cleared**.
