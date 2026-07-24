# Independent finite reconstruction — Papers II and III

## Exact reviewed objects

- Publication commit: `00d2a67d9963848e35596ea153917e73c2dfeb17`
- Paper II Git blob: `3ccd6a9b5487b9b97e79d366fcb5e6d581a6569e`
- Paper II SHA-256: `632bb8f4fd89a51020069327a11fe57f8ae882e57bd4ae1a9ed0829030c32ce1`
- Paper III Git blob: `05463cd60819598045ad41658d6bfd491e572691`
- Paper III SHA-256: `1753e5991ccab15142d9bd076554c283a69bfa3bd8aa9448b2edf62f50c4c7cb`

## From-scratch reconstruction

Hugging Face CPU job `6a6359807ef3c0846496771d` used an implementation written independently of the shipped validators. It checked:

1. the pair-sum difference-multiplicity dichotomy for `N=2,...,8`, including repeated endpoints;
2. the exact fourth-moment formula for every `N=2,...,8`;
3. the exact sixth-moment formula for every `N=2,...,8`;
4. the exact centred third-moment formula for every `N=2,...,8`;
5. 820 instances of the cumulative Möbius partial-binomial identity; and
6. four exact rational-arithmetic panels of the truncated singular-series divisor identity.

Every case passed. The unedited machine-readable result had SHA-256
`64d58a105af8e2f9f2fd6708b1bcad701d44ab19aecc70e4f0c89c476cef9ef0`.

The later corrections do not alter any checked finite identity. Paper II's final changes concern admissibility, zero-mass quotients, an explicit diagonal estimate, an `X^{o(1)}` threshold, an explicit standard singular-series factor, a translation-uniform prime-power explanation and the status of an imported transference step. Paper III's mathematical repair removes an unused unsupported infinite-tail assertion; its final ORCID and bibliography additions are editorial only.

## Shipped Paper II validators

Hugging Face job `6a635a7bdb23d7a7ec1ca79c` reran the archived suite with its declared `sympy` dependency:

- pair-sum fourth moment — passed;
- one-sided identity, 80 trials, maximum residual `8.486e-09` — passed;
- Möbius degree identity, 2,400 cases — passed;
- Fourier-scale conservation, 10,485 cases, maximum residual `8.598e-14` — passed;
- critical-scale coherence diagnostic through `N=10000` — passed as a diagnostic;
- overall result — `ALL_CHECKS_PASS`.

## Shipped Paper III validator

The addendum validator was rerun in job `6a6359807ef3c0846496771d`:

- exact multiplicity histograms for `N=8,9` — passed;
- high-moment bounds for `k=2,3,4` — passed;
- exact sixth moments for `N=2,...,11` — passed;
- exact centred third moments for `N=3,5,7` — passed;
- sub-Weibull range checks — passed;
- overall result — `ADDENDUM_CHECKS_PASS`.

## Scope

These checks validate the declared finite identities and exact formulas. They do not independently prove asymptotic estimates, completeness, novelty, the imported source-to-frame transference step, the open reciprocal sampling estimate or the conditional Hardy--Littlewood hypotheses.
