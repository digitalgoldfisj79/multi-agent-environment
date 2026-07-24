# Independent finite reconstruction — Papers II and III

## Exact reviewed objects

- Publication commit: `4866d113898a48f23feb9752576c350af97c6985`
- Paper II Git blob: `745d262aee6ffb41de580c866246c99a34144c13`
- Paper II SHA-256: `0b9d8c96b0185827085955084507f7c1099803a4a1de46c0db2e3b81f3cdbb7a`
- Paper III Git blob: `06fe9116d42fd056bf9727dfbaa63ccb7398562d`
- Paper III SHA-256: `7275ba02e7ae7a60d4bd3e524a2f1fd4d9fed639589b7d1ab7f08dd80f5fe675`

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

After the publication-quality rewrite of Paper III Appendix B, Hugging Face job `6a6371fe7ef3c08464967840` independently repeated the exact divisor identity in five rational-arithmetic panels, using prime sets through `13` and `H` through `500`. It also checked the finite upper bound for `beta_j(H)`. Every panel passed with the terminal result `APPENDIX_B_EXACT_PANELS_PASS`.

The final source edits do not alter a checked finite identity. Paper II's final edit replaces `a in Z setminus {0}` by the notation-equivalent phrase `a in Z with a != 0`. Paper III's final edits rewrite the same frozen singular-series proof in publication notation, remove an unsupported and unused sign inference, and remove a typesetting-only unsupported set-difference glyph.

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
