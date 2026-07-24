# Rebuilt Paper IV fidelity matrix

## Exact objects compared

- Frozen proof source: `RQM_PROOF.md`, blob `53f63f662f5a9d6e750a592ba8bcba6cf4bc9095`, branch `gpt56/d1-gate-bridge-terminal-20260724`.
- Rebuilt manuscript: `publications/fortune-papers-ii-vi-20260724/paper4_random_order/manuscript.md`, corrected commit `a082ec8d839e200fe568373ef9b81e2d8f0a72bd`, blob `cc7031d9731dee70432cacb821f1945efcfcd448`, SHA-256 `c7e337fd38a58cac2e98a2237eae6ad48681241f167504a546cb6fa978cbb7fa`, branch `publication/fortune-papers-ii-vi-20260724`.
- Editorial rule: internal adjudication language, session-specific scratchpad paths, and non-load-bearing diagnostics were removed or moved to the verification section; no theorem hypothesis, exponent, multiplicity, or load-bearing proof step was intentionally weakened or strengthened.
- Source-integrity scan: 28,748 characters, 992 lines, no control characters, no malformed `\frac`, and no unresolved editorial placeholders.

This is an editorial claim-level comparison. It does not itself certify the mathematical correctness of the frozen proof. Fresh hostile review of the rebuilt exact SHA-256 remains a separate gate.

## Claim and dependency map

| Load-bearing item | Frozen source | Rebuilt manuscript | Fidelity status | Notes |
|---|---|---|---|---|
| Random path, centres, pair indices, `N`, `M` | RQM §0 | §§1–2 | Verbatim-equivalent | Converted inline code notation to displayed mathematics. |
| Reciprocal weights `w`, `D_X`, `p`, `Psi`, `m` | RQM §0 | §2 | Verbatim-equivalent | `sum_{a>=1}m_a=1/2` made explicit from evenness. |
| Fixed-harmonic energy and distinct-modulus decomposition | RQM §0 and §8 | §2, equations (2.1)–(2.2) | Verbatim-equivalent | `R_a` defined explicitly rather than by a vague Paper II pointer. |
| Frobenius comparison | RQM §0 and §8 | §2, equation (2.3), and §9 | Precise external dependency | The comparison is isolated and cited to Paper II; it is the only mathematical import not reproved in Paper IV. |
| Quantitative frame admissibility `(N1)` | RQM §0 | §2, `(N1)` | Verbatim-equivalent | Preserves `rho >= delta_rho` on `[1/2,1]`, necessity discussion, and use in diagonal/tail bounds. |
| Effective block-size bounds `(N2)` | RQM §0 | §2, equation (2.4) | Verbatim-equivalent | Same constants and consequences for `M`. |
| Theorem quantifiers and uniformity in `q,r,a,X,eta,rho` | RQM §0 | Theorem 2.1 and Proposition 2.2 | Verbatim-equivalent | Random-order expectation explicitly identified as cancellation source. |
| Path rigidity and unit multipliers | RQM §1 | Lemmas 3.1–3.2 | Verbatim-equivalent | Proofs retained. |
| Coefficient taxonomy | RQM §2, Lemma 2.1 | Lemma 3.3 | Verbatim-equivalent | All `m=2,3,4` patterns retained. |
| Sliding-family multiplicity and completeness identity | RQM §2, Lemma 2.2 | Lemma 3.4, equation (3.3) | Verbatim-equivalent | Replaced polynomial-at-five-points verification by direct expansion; no claim change. |
| Exact ordered set-partition identity, including empty cells | RQM §3.1 | Lemma 4.1 | Verbatim-equivalent | Full coefficient-extraction proof retained. |
| Multivariate contour estimate and `C_*K^2` prefactor | RQM §3.2 | Lemma 4.2 | Verbatim-equivalent | Stirling prefactor and phase-uniform deficit proof retained. |
| Additive-slot factorisation | RQM §4 | §5, equation (5.1) | Verbatim-equivalent | All active slots retained. |
| Gauss/CRT expansion and coefficient norms | RQM §4, Lemma 4.1 | Lemma 5.1 | Verbatim-equivalent with expanded proof | Prime Gauss-sum facts are inlined rather than merely referenced. |
| Cell-character bookkeeping, empty-`W_0` collapse, non-collapsing tail slot | RQM §4 | §5, equations (5.4)–(5.6) and following paragraph | Verbatim-equivalent | These former synopsis omissions are now explicit. |
| One-slot and two-slot group norms | RQM §4, Lemma 4.2 | equations (5.7)–(5.8) | Verbatim-equivalent | Same sup and `l1` costs. |
| Sixth-moment exceptional-character count | RQM §5 | Lemma 5.2 | Verbatim-equivalent | Congruence-to-equality largeness condition and UFD count retained. |
| Macro cell and ratio coordinates | RQM §6 | §6, equations (6.1)–(6.3) | Verbatim-equivalent | Front/back orphan distinctions retained. |
| Triangular coordinate bijection | RQM §6.1 | Lemma 6.1 | Verbatim-equivalent | Full invertibility argument retained. |
| Good-coordinate contour decay | RQM §6, equation (6.1) | equation (6.4) | Verbatim-equivalent | Same `X^{-30f}` rate. |
| Path matching lemma | RQM §6.2 | Lemma 6.2 | Verbatim-equivalent | Outer-to-inner summation and one-use-per-edge accounting retained. |
| Pattern domination | RQM §6.3 | Lemma 6.3 | Verbatim-equivalent | Same `X^{-23}` per-free-coordinate margin. |
| Master per-configuration bound | RQM Proposition B | Proposition 6.4 | Verbatim-equivalent | Same orphan, bad-character, and edge-sup factors. |
| Trivial ledger classes `T1–T3` | RQM §7 | §7 | Verbatim-equivalent, partition clarified | Rebuilt text makes the assignment disjoint; counts remain upper bounds of the same order. |
| `C1` all-big four-rank class | RQM §7 | equation (7.5) | Verbatim-equivalent | Same four one-slot savings. |
| Binding `C2a` interior-micro class | RQM §7 | equation (7.6) | Verbatim-equivalent | Same `N^3 w_0`, `beta^3`, and two `X^{-2}` savings. |
| Binding `C2b` front-orphan class | RQM §7 | equation (7.7) | Verbatim-equivalent | Orphan cost retained. |
| `C2c` empty initial cell | RQM §7 | equation (7.8) | Verbatim-equivalent | Slot-one collapse retained. |
| Binding `C2d` back-orphan/empty-tail class | RQM §7 | equation (7.9) | Verbatim-equivalent | Tail slot explicitly does not collapse. |
| `C3` all-big three-rank class | RQM §7 | equation (7.10) | Verbatim-equivalent | Same three coordinate savings. |
| `C4` all-big sliding/doubled class | RQM §7 | equation (7.11) | Verbatim-equivalent | Type-S multiplicity `N` retained. |
| Ledger exhaustiveness | RQM §7 | opening and closing paragraphs of §7 | Verbatim-equivalent, made disjoint | Every configuration is assigned by `m` and micro-cell count/position. |
| No-cushion statement and source of exponent `9` | RQM §§7–8 | §8 | Verbatim-equivalent | Binding scale stated as `X^2 log^7 X = M log^9 X`. |
| Fixed-harmonic assembly and diagonal | RQM §8(i) | §9 through equation (9.1) | Verbatim-equivalent | `kappa <= m max p` and shell PNT retained. |
| Aggregate small-harmonic assembly | RQM §8(ii) | equation (9.2) | Verbatim-equivalent | Uses exact positive-harmonic mass `1/2`. |
| Schwartz tail | RQM §8(ii) | equation (9.3) | Verbatim-equivalent | Same sixth-power decay and `X^4H^{-5}` bound. |
| Frobenius assembly | RQM §8(ii) | final part of §9 | Verbatim-equivalent modulo precise Paper II citation | Same diagonal summation and aggregate comparison. |
| Effective constants and largeness conditions | RQM §8 constants ledger | §10 | Verbatim-equivalent | Session-only `Lambda` terminology omitted; numerical rates retained. |
| Verification status | RQM §9 | §10 | Faithful compression | Exact checks are described as non-proof validation, not used inferentially. |
| Scope limitation | RQM header and §10 | §§1 and 11 | Verbatim-equivalent | Explicitly says no Fortune or increasing-order theorem. |
| LLM provenance | Audit correction and prior manuscript disclosure | disclosure after §11 | Strengthened disclosure | Rebuild and failed prior hostile review are disclosed. |

## Editorial changes that require no new mathematics

1. The earlier 207-line synopsis was replaced rather than patched.
2. Internal labels such as “Assembly A”, “closure judge”, “G1 write-up”, and scratchpad paths were removed.
3. The ledger was presented as a disjoint partition to avoid the frozen source's harmless overlap language for `T1–T3`.
4. The algebraic identity in Lemma 3.4 is justified by direct expansion rather than by checking five polynomial values.
5. Standard prime Gauss-sum facts were expanded into a short proof.
6. The unused optional density-theorem strengthening was omitted.
7. The random-permutation averaging was stated in the abstract and introduction as the substitute source of cancellation.
8. A source-integrity scan found and corrected one missing LaTeX backslash before the review hash was frozen.

## Independent ledger control

`INDEPENDENT_LEDGER_RECONSTRUCTION.md` independently enumerates all ordered pair configurations for `N=3,...,10`, checks the exact `N`-versus-`1` multiplicity dichotomy, and verifies the rebuilt disjoint ledger at three micro thresholds. All panels passed. The independent exponent reconstruction again identifies `C2a`, `C2b`, and `C2d` as exactly binding.

## Current gate assessment

- Frozen-source-to-manuscript dependency coverage: **editorially complete for corrected SHA-256 `c7e337fd…cbb7fa`**.
- Independent reconstruction of the binding ledger: **completed and passed**.
- Fresh hostile review of the corrected exact SHA-256: **running; not yet disposed of**.
- DOCX/PDF/ZIP generation and source-to-binary fidelity: **not yet performed**.
- Human specialist circulation: **not cleared**.
