# P7 execution — exact finite and adversarial panels

**Status:** `P7_PASSED_DIAGNOSTIC_ONLY`

The execution script enumerates all supported order-one and order-two squarefree moduli, computes exact primorial centres, verifies the pair support cap

\[
N_r(j,k)\le {|j-k|-1\choose r},
\]

and checks the uniform row cap

\[
R_\beta\le U_r{n-1\choose r+1}
\]

for the profile `beta(q)q=1`. It also evaluates the inverse-square profile `beta(q)q=1/q` and constructs unrestricted adversarial weights concentrated on an observed collision modulus.

## Registered panel results

| X | Q | n | r | moduli | D, beta*q=1 | R | R/D | D, beta*q=1/q | R | R/D |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 400 | 4 | 1 | 70 | 70 | 1 | 0.014286 | 0.603299 | 0.043478 | 0.072068 |
| 10 | 400 | 4 | 2 | 0 | 0 | 0 | — | 0 | 0 | — |
| 10 | 1000 | 4 | 2 | 6 | 6 | 0 | 0 | 0.007261 | 0 | 0 |
| 20 | 4000 | 4 | 2 | 37 | 37 | 0 | 0 | 0.012578 | 0 | 0 |
| 30 | 12000 | 7 | 1 | 1421 | 1421 | 7 | 0.004926 | 0.804659 | 0.032188 | 0.040002 |
| 30 | 12000 | 7 | 2 | 130 | 130 | 0 | 0 | 0.015784 | 0 | 0 |
| 50 | 50000 | 10 | 1 | 5108 | 5108 | 9 | 0.001762 | 0.840433 | 0.025853 | 0.030761 |
| 50 | 50000 | 10 | 2 | 714 | 714 | 1 | 0.001401 | 0.023678 | 0.0000391 | 0.001650 |

All exact support and row-cap assertions pass.

## Adversarial W0 result

At `X=50`, `Q=50000`, order two, the modulus

\[
q=25591
\]

collides rows `j=3` and `k=6`. Concentrating the weight on this modulus with `beta(q)q=1` gives

\[
D_\beta=1,
\qquad R_\beta\ge1.
\]

This finite witness instantiates the general W0 falsifier. Similar order-one witnesses occur on every nontrivial registered panel.

## Interpretation

The inverse and inverse-square ratios are small on these panels, but those profiles are diagnostic surrogates. They do not establish a source theorem because no inherited source decomposition identifies either profile as its actual modulus energy weight.

The finite results validate the exact combinatorics and falsify unrestricted uniform subcriticality. They are not asymptotic evidence for PWOC-SF2.