# Independent finite reconstruction — Papers II and III

## Frozen objects

- Paper II Git blob: `734f24b08e4e07526f7d05c5f3abc1718265372a`
- Paper II SHA-256: `497c5b2a52e8beb93d166b8763646cf03ee315664d31e4d875c6486b3296e22f`
- Paper III Git blob: `6ff5adb496be657b4d0e761fe8508ab6f458ac56`
- Paper III SHA-256: `908eb40bbdfb1e88905d539bf978bbbebabffa874bdae98e0e7547b13b840e5f`

## Independent implementation

Hugging Face CPU job `6a6359807ef3c0846496771d` used a from-scratch Python implementation, not the shipped validators.

It checked:

1. the pair-sum difference-multiplicity dichotomy for `N=2,...,8`, including repeated endpoints;
2. the exact fourth-moment formula for every `N=2,...,8`;
3. the exact sixth-moment formula for every `N=2,...,8`;
4. the exact centred third-moment formula for every `N=2,...,8`;
5. 820 instances of the partial alternating binomial identity used by the cumulative Möbius truncation; and
6. the exact truncated-singular-series divisor identity in four rational-arithmetic panels.

Every case passed. The unedited machine-readable result has SHA-256
`64d58a105af8e2f9f2fd6708b1bcad701d44ab19aecc70e4f0c89c476cef9ef0`.

## Shipped validators

Paper II's archived validator suite was rerun with its declared `sympy` dependency in Hugging Face job `6a635a7bdb23d7a7ec1ca79c`:

- pair-sum fourth moment — passed;
- one-sided identity, 80 trials, maximum residual `8.486e-09` — passed;
- Möbius degree identity, 2,400 cases — passed;
- Fourier-scale conservation, 10,485 cases, maximum residual `8.598e-14` — passed;
- critical-scale coherence diagnostic through `N=10000` — diagnostic passed;
- overall result — `ALL_CHECKS_PASS`.

Paper III's shipped addendum validator was rerun in job `6a6359807ef3c0846496771d`:

- exact multiplicity histograms for `N=8,9` — passed;
- high-moment upper bounds for `k=2,3,4` — passed;
- exact sixth moments for `N=2,...,11` — passed;
- exact centred third moments for `N=3,5,7` — passed;
- sub-Weibull range checks — passed;
- overall result — `ADDENDUM_CHECKS_PASS`.

## Scope

These checks validate the declared finite identities and exact formulas. They do not independently prove asymptotic estimates, source completeness, novelty, or the open reciprocal transference and Hardy--Littlewood hypotheses.
