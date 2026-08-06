# Inverse-free algebraization of the bilateral endpoint incidence

**Date:** 30 July 2026  
**Branch:** `gpt56/fortune-mesoscopic-cotlar-20260728`  
**Programme:** `FERP-0.1`, Gate 2

## 0. Result

For scalar completion frequency, the cross-modulus bilateral endpoint incidence is exactly equivalent to four polynomial divisibilities with no modular inverses.

This converts the remaining component-classification problem into a literal coefficient scheme with auxiliary quotient variables. It also identifies the characteristic-three primorial resonance as an explicit linear subfamily of that scheme.

The theorem does not classify all components. It supplies the algebraic object that must now be classified.

## 1. Setup

Let `P,S,P',S'` be monic irreducibles of degree `k`, with

`P!=P'` and `S!=S'`.

Let `L` be coprime to all four primes and let scalar `theta in F_q^*`. Define

`mu=-theta (LS)^(-1) mod P`,

`mu'=-theta (LS')^(-1) mod P'`,

`nu=-theta (LP)^(-1) mod S`,

`nu'=-theta (LP')^(-1) mod S'`.

At source degree `m=2k-1`, the two endpoint incidences are

`E_mu=mu P'-mu' P in F_q`,

`E_nu=nu S'-nu' S in F_q`.

## 2. Theorem IFA1 — inverse-free equivalence

For `c,d in F_q`:

`E_mu=c`

if and only if

`P  divides cLS + theta P'`,

`P' divides cLS' - theta P`.

Similarly,

`E_nu=d`

if and only if

`S  divides dLP + theta S'`,

`S' divides dLP' - theta S`.

The witnesses `c` and `d` are unique.

### Proof for the first source

If `E_mu=c`, reduction modulo `P` gives

`mu P'=c`.

Since `mu=-theta(LS)^(-1) mod P`, this is equivalent to

`cLS+theta P'=0 mod P`.

Reduction modulo `P'` gives

`-mu'P=c`,

which is equivalent to

`cLS'-theta P=0 mod P'`.

Conversely, assume both divisibilities. They imply

`mu P'-mu'P-c=0 mod P`

and

`mu P'-mu'P-c=0 mod P'`.

Because `P` and `P'` are distinct degree-`k` primes, their product divides the left-hand side. But

`deg(mu P'-mu'P-c)<2k`.

Therefore the left-hand side is zero. Uniqueness follows immediately.

The second-source proof is identical after interchanging `(P,P')` with `(S,S')`.

∎

## 3. Coefficient scheme

Introduce quotient polynomials `U,U',V,V'`. The cross-modulus simultaneous incidence is the projection of

`cLS + theta P' = P U`,

`cLS' - theta P = P' U'`,

`dLP + theta S' = S V`,

`dLP' - theta S = S' V'`.

Let

`h=max(deg L, deg theta)`.

The quotient degrees may be restricted to at most `h`.

With `P,S,P',S'` represented by their `k` free lower coefficients, one affine presentation has:

- `4k` prime-polynomial coefficient variables;
- two scalar variables `c,d`;
- at most `4(h+1)` quotient coefficients.

The four polynomial identities provide coefficient equations of degree at most two in these variables. The open locus is cut out by:

- irreducibility of all four degree-`k` polynomials;
- `Res(P,P') Res(S,S') != 0`;
- the pair conditions `P!=S`, `P'!=S'`;
- `Res(L,PP'SS') != 0`.

Same-modulus strata `P=P'` or `S=S'` are excluded from Theorem IFA1 and must be treated as separate diagonal/class components. They are not silently absorbed into this scheme.

## 4. Resonant subfamily

Over `F_3[t]`, with `L=t^3-t`, the primorial-resonant construction

`S=P+epsilon Q`,

`P'=LQ-P`,

`S'=LQ-S`

satisfies the inverse-free equations with

`c=-theta epsilon^(-1)`,

`d= theta epsilon^(-1)`.

Thus the previously discovered exceptional affine orbits are a linear, small-characteristic subfamily of the inverse-free incidence scheme rather than unexplained isolated points.

## 5. Machine audit

Verifier:

`fortune-review/scripts/ff_bilateral_incidence_algebraization.py`

Frozen output:

`fortune-review/data/ff_bilateral_incidence_algebraization.json`

The verifier checks both implications and uniqueness of `c,d` for every cross-modulus pair-of-pairs on:

- `(q,k)=(3,2),(5,2),(7,2)`;
- `(q,k)=(3,3),(3,4)`.

At `(3,4)` it recovers exactly twelve cross-distinct simultaneous incidences, the resonant family classified separately.

## 6. Remaining classification theorem

`BIC_FF` is now the following concrete problem:

1. decompose the inverse-free coefficient scheme into geometric components;
2. remove the same-modulus diagonal/class strata separately;
3. identify characteristic-dependent and primorial-dependent factors;
4. determine which components meet the four-prime open locus with the required dimension;
5. attach the literal corrected amplitude `B_a conjugate(B_b)` to each surviving component.

A component classification based only on finite irreducible points remains empirical. The next proof must work at the coefficient-scheme level.

## 7. Status

### PROVED EXACTLY

- Theorem IFA1;
- uniqueness of the scalar incidence witnesses;
- the quotient-variable scheme presentation;
- inclusion of the characteristic-three resonant family.

### MACHINE-VERIFIED IDENTITY

- both directions and uniqueness on the committed panels.

### OPEN

- geometric irreducible-component decomposition;
- singular loci and dimensions of all residual components;
- corrected component amplitudes beyond the finite resonant audit;
- `CBI_FF`, `RBK_FF` and endpoint `FFPR`.
