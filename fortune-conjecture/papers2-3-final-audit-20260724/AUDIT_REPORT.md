# Adversarial audit — Papers II and III

## Current decision

**SOURCE-LEVEL PASS — COMPILED-ARTIFACT AND HUMAN-REVIEW GATES OPEN.**

The original seven-page structural drafts did not contain the complete load-bearing proof record. Paper II has been rebuilt from its four-part archived manuscript. Paper III retains its concise narrative but now includes the complete frozen kernel, singular-series and conditional-theorem proofs as appendices.

## Exact reviewed objects

Publication commit: `00d2a67d9963848e35596ea153917e73c2dfeb17`.

### Paper II

- Path: `publications/fortune-papers-ii-vi-20260724/paper2_revised/manuscript.md`
- Git blob: `3ccd6a9b5487b9b97e79d366fcb5e6d581a6569e`
- SHA-256: `632bb8f4fd89a51020069327a11fe57f8ae882e57bd4ae1a9ed0829030c32ce1`
- Size: 43,951 bytes

### Paper III

- Path: `publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md`
- Git blob: `05463cd60819598045ad41658d6bfd491e572691`
- SHA-256: `1753e5991ccab15142d9bd076554c283a69bfa3bd8aa9448b2edf62f50c4c7cb`
- Size: 37,342 bytes

## Paper II result boundary

Paper II proves the structural integer-side results it labels proved:

1. the Fortunate-number square barrier;
2. prime-power contamination bounds;
3. the deterministic block-variance criterion;
4. exact reciprocal-frame and pair-sum identities;
5. the weighted harmonic reduction and diagonal estimate;
6. the exact fourth moment;
7. cumulative Möbius truncation and the Frobenius tail;
8. the semiprime resonance obstruction;
9. exact character-diagonal and ratio-collapse identities;
10. the density-one failure certificate;
11. critical-scale phase coherence and conductor migration;
12. harmonic aggregation and Fourier-scale conservation; and
13. the divisor-pinning obstruction.

It does **not** prove the source-to-frame transference step, the reciprocal sampling target, the direct block-variance estimate or Fortune's conjecture. The imported transference step is identified explicitly and is not asserted equivalent to the direct variance target.

The reconstruction repaired six substantive presentation or claim-boundary defects: reciprocal-weight admissibility, zero-mass quotients, an unstated diagonal estimate, an invalid fixed-`epsilon` level-set threshold, an implicit singular-series lower bound and an abbreviated moving-interval prime-power argument.

## Paper III result boundary

Paper III proves unconditionally:

1. bounded-coefficient rigidity;
2. the exact `N`-or-`1` pair-difference multiplicity dichotomy;
3. the two-scale energy decomposition;
4. high-moment bounds;
5. the uniform sub-Weibull tail in the stated range;
6. exact computer-assisted sixth and centred third moments;
7. the exceptional-set failure certificate;
8. the truncated singular-series local factors and exact divisor identity; and
9. the bound `|T_j(H)| <= 2H log X`.

It proves conditionally that the stated block-averaged first-moment and Hardy--Littlewood pair-correlation hypotheses imply the deterministic variance criterion and hence Fortune's conjecture for sufficiently large indices. The hypotheses themselves and the reciprocal exceptional-set transference theorem remain open.

An unused unsupported assertion about the omitted infinite Euler-product tail was removed rather than reconstructed. The sharper Dickman--de Bruijn constant remains explicitly non-load-bearing.

## Independent reconstruction

Hugging Face CPU job `6a6359807ef3c0846496771d` independently enumerated pair-sum multiplicities and moments through `N=8`, checked 820 cumulative Möbius identities and verified four exact rational singular-series divisor identities. All panels passed.

The shipped Paper II suite returned `ALL_CHECKS_PASS` in job `6a635a7bdb23d7a7ec1ca79c`. The shipped Paper III addendum suite returned `ADDENDUM_CHECKS_PASS` in job `6a6359807ef3c0846496771d`.

## Fresh hostile manuscript-only review

The exact final objects were supplied sequentially to `Qwen/Qwen3-14B-AWQ` in Hugging Face job `6a6365fedb23d7a7ec1ca8a6`.

- Paper II prompt SHA-256: `3e8b31b537ca364afead5631f7e2c2b6afd0749d07bf504fabe2ba93719554d6`
- Paper III prompt SHA-256: `32bd0a46b61552ee94458042806275336505fcf4684c05e2469a81a66013dd6e`

The Paper II review states that the actually claimed theorems are proved, then incorrectly treats the explicitly imported transference step as an asserted equivalence and overlooks the definition `P_j=A_XQ_j` when objecting to semiprime divisibility.

The Paper III review labels the whole paper “not proved” because it counts explicitly open hypotheses as missing proofs. It separately acknowledges that the rigidity, tail and singular-series theorems are solid. `HOSTILE_REVIEW_DISPOSITION.md` resolves every listed objection against the exact text. No fatal or major issue survives disposition.

## Gate ledger

1. Frozen-source fidelity — **passed**.
2. Independent finite reconstruction — **passed**.
3. Fresh manuscript-only hostile review — **passed after disposition**.
4. Compiled PDF/DOCX/ZIP integrity — **open**.
5. External human specialist review — **open**.

This is an internal technical audit, not human peer review, publication acceptance or a proof of Fortune's conjecture.
