# The characteristic-three primorial-resonant bilateral component

**Date:** 30 July 2026  
**Branch:** `gpt56/fortune-mesoscopic-cotlar-20260728`  
**Programme:** `FERP-0.1`, Gates 2–3

## 0. Result

The twelve non-diagonal bilateral incidences previously found at `(q,k,m)=(3,4,7)` are not sporadic. They are the first visible points of an explicit characteristic-three primorial-resonant family.

The family has a coherent, nonoscillatory pair of same-source Gram phases. Nevertheless, its raw Gram contribution is smaller than the squared endpoint target by the elementary factor

`<= 2 m^2 3^(-k-3)`.

Thus this component is a **forced phase but negligible by parameter dimension** before its still-open interaction with the exact `Delta_PS` correction.

This removes the known exceptional affine orbits as a possible endpoint obstruction. It does not classify every bilateral component and it does not prove `CBEA_FF`.

## 1. Exact resonant family

Work over `F_3[t]` with

`L=t^3-t`.

Let `k>=3`. Choose:

- a monic irreducible `P` of degree `k`;
- a polynomial `Q` of degree `k-3` with leading coefficient `-1=2`;
- `epsilon in F_3^*`.

Define the involution

`J_Q(T)=LQ-T`

and set

`S=P+epsilon Q`,

`P'=J_Q(P)=LQ-P`,

`S'=J_Q(S)=LQ-S=P'-epsilon Q`.

Because the leading coefficients of `LQ` and `P` are `-1` and `1`, respectively, `P'` and `S'` are again monic precisely because the characteristic is three:

`-1-1=-2=1`.

Assume `P,S,P',S'` are distinct irreducibles of degree `k`.

For scalar `theta in F_3^*`, define

`mu=-theta (LS)^(-1) mod P`,

`mu'=-theta (LS')^(-1) mod P'`,

`nu=-theta (LP)^(-1) mod S`,

`nu'=-theta (LP')^(-1) mod S'`.

### Theorem PRC1 — exact completion numerators

The endpoint completion numerators are constants:

`mu P' - mu' P = -theta epsilon^(-1)`,

`nu S' - nu' S = theta epsilon^(-1)`.

In particular, both endpoint incidence conditions hold and the two constants sum to zero.

### Proof

Modulo `P`, the relations `S=P+epsilon Q` and `P'=LQ-P` give

`LS == epsilon LQ == epsilon P' (mod P)`.

Hence

`mu P' == -theta epsilon^(-1) (mod P)`.

Modulo `P'`, the relations `S'=P'-epsilon Q` and `P=LQ-P'` give

`LS' == -epsilon LQ == -epsilon P (mod P')`,

so

`mu' P == theta epsilon^(-1) (mod P')`.

Therefore

`F=mu P'-mu'P+theta epsilon^(-1)`

is divisible by both distinct degree-`k` primes `P` and `P'`. But `deg F<2k`, so `F=0`.

The second identity is symmetric. Modulo `S`, one has `P=-epsilon Q` and `S'=LQ-S`, hence `LP=-epsilon S'`. Modulo `S'`, one has `P'=epsilon Q` and `S=LQ-S'`, hence `LP'=epsilon S`. The same degree argument gives

`nu S'-nu'S=theta epsilon^(-1)`.

∎

## 2. Exact Gram phase

Let

`B_m=sum_(deg f=m) Lambda(f)^2`.

The same-source completed Gram kernel associated with a constant endpoint numerator `c` is

`G(c)=sum_(deg f=m) Lambda(f)^2 psi_(PP')(c f)`.

At `m=2k-1`, `deg(cf)<2k`, so no reduction modulo the degree-`2k` product occurs. Since every source polynomial is monic, the extracted top coefficient is exactly `c`. Thus

`G(c)=psi(c) B_m`.

For the resonant pair of sources, Theorem PRC1 gives constants `-theta/epsilon` and `theta/epsilon`. Consequently

`G_mu G_nu = B_m^2`.

The component is therefore nonoscillatory at this raw Gram level. It does not cancel under the two source phases.

## 3. Dimension bound

Each resonant ordered pair-of-pairs is determined by `(P,Q,epsilon)`. Hence, without using primality,

`N_res(k) <= 2 * 3^k * 3^(k-3) = 2*3^(2k-3)`.

The standard exact identity

`sum_(deg f=m) Lambda(f)=3^m`

and `Lambda(f)<=m` imply

`B_m <= m 3^m`.

Therefore the total absolute raw resonant contribution satisfies

`N_res(k) B_m^2 <= 2 m^2 3^(2m+2k-3)`.

The squared endpoint target is

`3^(2m+3k)`.

Thus

`resonant raw contribution / squared endpoint target`

`<= 2 m^2 3^(-k-3)`.

At `m=2k-1`, this is an exponential saving in `k`. The resonant family cannot itself violate the endpoint estimate through the raw same-source Gram term.

## 4. Exact classification of the old `(3,4,7)` exceptions

The independent verifier performs a full pair-of-pairs scan at `q=3,k=4` and proves computationally that:

- there are exactly twelve non-diagonal, non-transpose simultaneous incidences;
- all twelve have the form in Section 1;
- six have `epsilon=1` and six have `epsilon=-1`;
- these are exactly the two previously recorded `AGL(1,3)` orbits of size six.

Thus the earlier two affine orbits are now algebraized as the two orientations

`S=P+Q` and `S=P-Q`

inside the involution `T -> LQ-T`.

The completeness assertion is an **EMPIRICAL-EXACT FINITE PANEL** statement at `k=4`. The construction and identities are exact for every `k>=3` whenever the four prime conditions hold.

## 5. Extended exact panels

Candidate generation, rather than blind pair-squaring, gives the following exact prime-point counts:

| `k` | `m=2k-1` | resonant ordered pair-of-pairs | split by `epsilon` |
|---:|---:|---:|---:|
| 3 | 5 | 2 | 1 + 1 |
| 4 | 7 | 12 | 6 + 6 |
| 5 | 9 | 72 | 36 + 36 |
| 6 | 11 | 192 | 96 + 96 |
| 7 | 13 | 1440 | 720 + 720 |

Every generated point satisfies the exact numerator identities for both nonzero scalar values of `theta`.

Verifier:

`fortune-review/scripts/ff_primorial_resonant_component.py`

Frozen output:

`fortune-review/data/ff_primorial_resonant_component.json`

## 6. Delta boundary

This calculation concerns the raw same-source Gram component produced by the bilateral incidence. The corrected endpoint aggregate contains `Delta_PS`, and the centered bilateral identity has not yet been derived.

Accordingly, the following is **OPEN**:

- the exact cross term between the resonant family and `Delta_PS`;
- whether the centered identity subtracts part or all of this raw component automatically;
- the complete classification of all other bilateral components.

The elementary dimension bound shows that no special subtraction is required merely to protect the endpoint exponent from the raw resonant term. The `Delta_PS` interaction must still be written literally in Gate 3.

## 7. Status

### PROVED EXACTLY

- the characteristic-three involution construction;
- Theorem PRC1;
- the coherent Gram phase `G_mu G_nu=B_m^2`;
- the parameter-count and raw-component endpoint saving.

### MACHINE-VERIFIED IDENTITY

- the construction and completion constants for every generated prime point at `3<=k<=7` and both nonzero scalar `theta`.

### EMPIRICAL-EXACT FINITE PANEL

- completeness of the resonant family among all non-diagonal/non-transpose incidences at `q=3,k=4`;
- the listed prime-point counts.

### OPEN

- `Delta_PS` interaction;
- general `BIC_FF` beyond this explicit component;
- the centered bilateral identity and endpoint `FFPR`.
