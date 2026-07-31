# Bilateral defect dichotomy and authoritative correction to Round 12

**Date:** 30 July 2026  
**Branch:** `gpt56/fortune-mesoscopic-cotlar-20260728`  
**External intake audited:** `ebcbcf766b7addc8512e11bf48febf79b1b30694`  
**Programme:** `FF_LARGE_FIELD_DIAGONAL_COLLAPSE_PROGRAMME_V0_1_20260730.md`

## 0. Decisive result

The Round-12 claim

`q>k  =>  the cross-distinct bilateral endpoint incidence is empty`

is **false**. Its companion claim `c+d=0` is also **false**.

The first exact counterexample occurs at `(q,k)=(11,3)`. There are 220 cross-distinct simultaneous incidences there, forming two full `AGL(1,11)` orbits. Further exact cubic censuses find nonzero incidence at `q=17,19,29,31,37,41,43,47,53,59`.

The correction is structural rather than merely computational:

- Round 12 classified the **zero-defect component**.
- Zero defect is forced when `q<2k`.
- The fixed-degree large-field regime eventually has `q>=2k`, where a nonzero low-degree defect polynomial can and does occur.

Thus the exceptional geometry does not disappear in the first large-field regime. A new nonzero-defect component must be classified and bounded before a centred bilateral endpoint theorem can close.

## 1. Audit verdict on the Round-12 statements

### Accepted and independently rederived

1. The correspondence form: `(P,S,c,d)` uniquely determines `(P',S')`.
2. Same-modulus contact `P'=P` and `S'=S` is impossible for nonzero witnesses.
3. The transpose classification at `k=q`.
4. Reflection-family inclusion.
5. Translation-family inclusion.
6. Disjointness of reflection and translation for odd characteristic.

### Upgraded

The reflection/translation classification is now proved complete on the entire range `q<2k`, apart from the separately explicit transpose contact. In particular it is complete for `k>=q`.

### Falsified

1. Universal `c+d=0`.
2. Universal emptiness for `q>k`.
3. The inference that the large-field centred bilateral identity has only diagonal support.

The 13 Round-12 panels did not enter the genuinely different range `q>=2k` with `k>=3`; `(11,3)` is the first omitted discriminator.

## 2. Scalar-free inverse-free system

Let `q` be an odd prime and

`L=t^q-t`.

Let `P,S,P',S'` be monic irreducibles of common degree `k`, satisfying the pair conditions and nonzero scalar endpoint witnesses `theta,c,d`.

Set

`lambda=-theta/c`,

`rho=theta/d`.

The four incidence divisibilities are

`P  | LS  - lambda P'`,

`P' | LS' + lambda P`,

`S  | LP  + rho S'`,

`S' | LP' - rho S`.

Define the monic degree-`q` quotient polynomials

`A P  = LS  - lambda P'`,

`B S  = LP  + rho S'`,

`C P' = LS' + lambda P`,

`D S' = LP' - rho S`.

## 3. Theorem BDD1 — the common low-degree defect

Assume `q>k`.

### 3.1 Cross contacts are impossible

If `P=S'`, then the second divisibility gives

`P' | (L+lambda)P`.

Since `P'!=P`, this forces `P'|L+lambda`. The Artin–Schreier polynomial `L+lambda` is irreducible of degree `q`, contradicting `deg P'=k<q`.

Similarly, `S=P'` would force `P|L-lambda`, again impossible.

Therefore `P,S'` are distinct and `S,P'` are distinct.

### 3.2 Defect divisibilities

Substituting the first two quotient equations into the third gives

`L(rho C-lambda B)S + (lambda L^2-rho C A-lambda^2 rho)P = 0`.

Coprimality implies

`P | rho C-lambda B`.

Performing the reverse substitution gives

`S' | rho C-lambda B`.

Hence

`P S' | rho C-lambda B`.

The symmetric calculation gives

`S P' | rho A-lambda D`.

Thus there are polynomials `h_1,h_2` such that

`rho C-lambda B = h_1 P S'`,

`rho A-lambda D = h_2 S P'`.

Now

`(rho C-lambda B)P'S`

and

`(rho A-lambda D)PS'`

both expand exactly to

`L(rho SS'-lambda PP') + lambda rho(PS-P'S')`.

Since the polynomial ring is a domain,

`h_1=h_2=:h`.

Therefore every cross-distinct incidence has a unique common defect polynomial satisfying

`rho C-lambda B = h P S'`,

`rho A-lambda D = h S P'`,

and

`h P P' S S' = L(rho SS'-lambda PP') + lambda rho(PS-P'S')`.

Because the left quotient differences have degree at most `q`,

`deg h <= q-2k`.

This is **PROVED EXACTLY**.

## 4. Theorem BDD2 — zero-defect classification

Assume `h=0`.

The leading coefficients of `rho C-lambda B=0` give

`rho=lambda`.

Consequently

`C=B`, `A=D`, and `c+d=0`.

The first transfer identity then reduces to

`A B = L^2-lambda^2 = (L-lambda)(L+lambda)`.

For nonzero `lambda`, both `L-lambda` and `L+lambda` are irreducible degree-`q` Artin–Schreier polynomials. Since `A` and `B` are monic of degree `q`, unique factorisation gives

`{A,B}={L-lambda,L+lambda}`.

### Case 1: `A=L-lambda`

The equation `AP=LS-lambda P'` gives

`P'=P+LR`,

`S=P+lambda R`.

The remaining equations give

`S'=S+LR`.

This is precisely the translation family.

### Case 2: `A=L+lambda`

The same equation gives

`P'=LQ-P`,

`S=P+lambda Q`,

and the remaining equations give

`S'=LQ-S`.

This is precisely the reflection family.

Thus the Round-12 reflection and translation families are not merely examples: they are exactly the zero-defect incidence.

## 5. Exact consequences

### 5.1 Complete classification when `q<2k`

If `q<2k`, the degree bound `deg h<=q-2k` forces `h=0`.

Therefore every four-distinct incidence is reflection or translation.

Cross contact is handled separately:

- at `k=q`, it is exactly the Artin–Schreier transpose locus;
- at `k>q`, it is impossible by degree.

Hence the Round-12 two-family classification is **PROVED EXACTLY for every `k>=q`**, with transpose as the degenerate reflection contact at `k=q`.

### 5.2 Empty intermediate strip

If

`k<q<2k`,

then `h=0`, but both reflection and translation require a nonzero polynomial whose product with `L` has degree at most `k`. This is impossible because `deg L=q>k`.

Therefore

`k<q<2k  =>  no cross-distinct incidence`.

This explains all of the successful Round-12 `k<q` panels: they lay either in this forced-zero-defect strip or in the special quadratic panels.

### 5.3 The true large-field boundary

For fixed `k` and growing `q`, one eventually has

`q>=2k`.

Only in this range can `h` be nonzero. The hoped-for large-field diagonal collapse therefore extrapolated across the exact point at which a new degree of freedom appears.

## 6. Explicit falsification at `(q,k)=(11,3)`

Over `F_11[t]`, let

`P  = t^3+4t^2+1`,

`S  = t^3+10t^2+9t+1`,

`P' = t^3+10t^2+6t+7`,

`S' = t^3+4t^2+3t+10`.

All four are distinct irreducible cubics.

Take `theta=1`, `c=2`, `d=8`. Then

`lambda=5`, `rho=7`,

so

`c+d=10 != 0`, `lambda!=rho`.

The original local frequencies are

`mu_(P,S)   = 7+10t+6t^2`,

`mu_(P',S') = 3+2t+6t^2`,

`nu_(S,P)   = 2+5t+4t^2`,

`nu_(S',P') = 1+3t+4t^2`.

Direct polynomial multiplication gives

`mu_(P,S)P' - mu_(P',S')P = 2`,

`nu_(S,P)S' - nu_(S',P')S = 8`.

Thus this is a literal simultaneous endpoint incidence, not an artefact of the correspondence enumerator.

Its common defect is

`h=2t^5+5t^4+6t^2+6t+4`,

with

`deg h=5=q-2k`.

It satisfies both quotient-defect identities and the exact product identity from Theorem BDD1.

Consequently both `C12-2` and the proposed `q>k` emptiness theorem are rigorously falsified.

## 7. Extended exact cubic census

An independent orbit-reduced C++ implementation enumerates the complete scalar cubic correspondence, checks irreducibility and all four inverse-free divisibilities, and expands the resulting seeds under exact `AGL(1,q)` covariance.

| `q` | cubic defect orbits | incidences |
|---:|---:|---:|
| 5 | 0 | 0 |
| 7 | 0 | 0 |
| 11 | 2 | 220 |
| 13 | 0 | 0 |
| 17 | 2 | 544 |
| 19 | 2 | 684 |
| 23 | 0 | 0 |
| 29 | 2 | 1,624 |
| 31 | 2 | 1,860 |
| 37 | 4 | 5,328 |
| 41 | 6 | 9,840 |
| 43 | 6 | 10,836 |
| 47 | 2 | 4,324 |
| 53 | 6 | 16,536 |
| 59 | 4 | 13,688 |

Every nonzero count is a union of full affine orbits of size `q(q-1)` on these panels. This orbit pattern is **EMPIRICAL-EXACT FINITE PANEL**, not yet a uniform component theorem.

## 8. Consequences for the endpoint programme

The proposed shortcut

`q>k emptiness => centred identity has diagonal support only`

is closed.

The corrected function-field route is now:

1. retain the exact common defect `h`;
2. classify the nonzero-defect incidence components in `q>=2k`;
3. determine their corrected `Delta_PS` amplitudes;
4. derive the centred bilateral identity with those components explicit;
5. prove the residual/component contribution is within the endpoint allowance.

The cubic census suggests a finite-orbit quotient after affine symmetry, hence potentially dimensionally small support, but no uniform `O(q^2)` theorem has yet been proved.

## 9. Minimal new theorem

### `NDC_FF` — nonzero-defect component theorem

For fixed `k` and prime `q>=2k`, classify or bound the solutions of

`rho C-lambda B = h P S'`,

`rho A-lambda D = h S P'`,

with

`deg h<=q-2k`,

all four degree-`k` polynomials irreducible, and the literal corrected amplitude retained.

A sufficient first theorem would show that, after affine quotient, the nonzero-defect locus has bounded degree and dimension zero for fixed `k`, yielding `O_k(q^2)` ordered incidences before amplitude estimates.

## 10. Status

### PROVED EXACTLY

- correspondence form and same-modulus exclusion;
- Theorem BDD1 and uniqueness of the common defect;
- zero-defect reflection/translation classification;
- completeness for `k>=q`;
- emptiness in the strip `k<q<2k`;
- the explicit `(11,3)` counterexample;
- falsity of universal `c+d=0` and universal `q>k` emptiness.

### MACHINE-VERIFIED IDENTITY

- original local-frequency and defect identities for the explicit counterexample;
- independent cubic orbit census implementation.

### EMPIRICAL-EXACT FINITE PANEL

- the cubic orbit and incidence counts through `q=59`;
- the apparent finite affine-orbit quotient.

### OPEN

- `NDC_FF`;
- corrected component amplitudes;
- centred bilateral identity with nonzero defect;
- endpoint `FFPR`;
- theta restoration, conductor coupling, thinning;
- every integer transfer interface and Fortune's conjecture.
