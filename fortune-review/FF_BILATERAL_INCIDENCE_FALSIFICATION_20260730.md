# Function-field bilateral incidence falsification

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Companion verifier: `fortune-review/scripts/ff_endpoint_incidence_falsification.py`  
Frozen output: `fortune-review/data/ff_endpoint_incidence_falsification.json`

## Result

The finite-panel suggestion that simultaneous completion in both source variables always collapses to the diagonal, or to the diagonal plus transpose, is **FALSIFIED**.

At the endpoint `m=2k-1`, for ordered degree-`k` prime pairs `a=(P,S)` and `b=(P',S')`, the bilateral incidence is

`deg(nu_a S' - nu_b S) <= 0`

and

`deg(mu_a P' - mu_b P) <= 0`.

The expanded exact panels are:

| q | k | ordered pairs | one-sided incidences in each source | simultaneous | diagonal | transpose | other |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 3 | 1560 | 2380 | 1560 | 1560 | 0 | 0 |
| 3 | 4 | 306 | 336 | 318 | 306 | 0 | 12 |

At `(q,k,m)=(3,4,7)`, the 12 non-diagonal, non-transpose incidences form exactly two `AGL(1,3)` orbits of size six. The verifier archives representatives of both orbits.

## Status

### MACHINE-VERIFIED IDENTITY

- every incidence count in the two panels;
- the classification into diagonal, transpose and other;
- the two affine orbit sizes and their exhaustion of the 12 exceptions.

### EMPIRICAL-EXACT FINITE PANEL

- diagonal collapse at `(q,k)=(5,3)`;
- the two exceptional affine components at `(q,k)=(3,4)`.

### RETRACTED

- any universal conjecture that the simultaneous endpoint incidence is only diagonal or diagonal-plus-transpose.

### OPEN

- a general algebraic classification of the simultaneous incidence variety;
- whether the exceptional components are confined to small characteristic, recur in growing degree, or contribute a structured main term;
- a signed estimate for their Lambda-weighted contribution at the `CBEA_FF` target scale.

## Consequence for the endpoint theorem

The centered bilateral assembly theorem remains the correct target, but it cannot be reduced to diagonal subtraction alone. Its degeneracy analysis must:

1. classify all irreducible components of the simultaneous incidence;
2. isolate diagonal and transpose components;
3. identify small-characteristic or primorial-resonant exceptional components;
4. subtract any forced main term exactly;
5. prove cancellation on the residual components while retaining the von Mangoldt weights and `Delta_PS`.

This narrows the theorem statement and prevents a false diagonal-rigidity shortcut. It does not weaken the diagonal-floor obstruction: ordinary positive first dispersion still cannot reach endpoint `FFPR`.
