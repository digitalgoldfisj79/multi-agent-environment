# Two-orbit real-cyclotomic trace reduction of the Airy sum

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic `d=1` Airy wall, primes `p congruent 5 mod 6`, `p>=11`.  
**Status:** **PROVED**.

## 1. Local values and sign convention

Let

\[
t_u=-\sum_{x\in\mathbf F_p}\zeta_p^{x^3+ux},
\qquad
f_p(u)=D_p(t_u,p).
\]

With this explicit Haessig/Dwork local sign and the repository's positively normalized `T_p`, the exact identity is

\[
\boxed{
\sum_{u\in\mathbf F_p}f_p(u)=-pT_p.
}
\]

This is the sign recorded in `DIVIDED_ADAMS_HASSE_COEFFICIENT_20260725.md` and reproduced by the exact verifier below. Absolute estimates are of course unchanged.

Since cubing is a bijection of `F_p`,

\[
t_0=-\sum_y\zeta_p^y=0,
\qquad
f_p(0)=0.
\]

Let

\[
K_p^+=\mathbf Q(\zeta_p)^+.
\]

## 2. Galois action and square-class orbits

For `a in F_p^*`, let `sigma_a(zeta_p)=zeta_p^a`, and let `c` be the unique cube root of `a`. Rescaling `x` gives

\[
\boxed{
\sigma_a(f_p(u))=f_p(c^2u).
}
\]

The map

\[
\mathbf F_p^*/\{\pm1\}
\longrightarrow
(\mathbf F_p^*)^2,
\qquad
a\longmapsto c^2
\]

is a bijection. Thus the Galois orbit of `f_p(1)` is the square-class set

\[
\{f_p(s):s\text{ square}\},
\]

and the orbit of `f_p(eta)` is the nonsquare-class set for any nonsquare `eta`.

The local initial-term theorem proves that all these values are distinct and each individual nonzero value generates `K_p^+`.

## 3. Exact two-trace identity

Choose a nonsquare

\[
\eta\ne-1.
\]

Such a choice exists for every admitted prime `p>=11`. Then

\[
\sum_{s\text{ square}}f_p(s)
=
\operatorname{Tr}_{K_p^+/\mathbf Q}(f_p(1))
\]

and

\[
\sum_{s\text{ square}}f_p(\eta s)
=
\operatorname{Tr}_{K_p^+/\mathbf Q}(f_p(\eta)).
\]

Therefore

\[
\boxed{
-pT_p
=
\operatorname{Tr}_{K_p^+/\mathbf Q}
\left(f_p(1)+f_p(\eta)\right).
}
\]

Put

\[
\gamma_p=f_p(1)+f_p(\eta).
\]

## 4. The combined generator is also primitive

Write

\[
p=3h+2,
\qquad
e=\frac{p+1}{3},
\qquad\pi=\zeta_p-1.
\]

The proved local initial term is

\[
\frac{f_p(u)}{p^e}
\equiv
\frac{u}{h!}\pi^e
\pmod{\pi^{e+1}}.
\]

For a square `s`, the conjugate of `gamma_p` indexed by `s` is

\[
f_p(s)+f_p(\eta s).
\]

Its normalized initial coefficient is

\[
\frac{s(1+\eta)}{h!}.
\]

Because `eta!=-1`, these coefficients are pairwise distinct as `s` ranges over the square subgroup. Hence `gamma_p` has `(p-1)/2` distinct conjugates and

\[
\boxed{
\mathbf Q(\gamma_p)=K_p^+.
}
\]

Thus the complete Airy trace does not descend to a proper cyclotomic subfield or a bounded-degree algebraic family.

## 5. Exact archimedean reformulation

The rank-two Airy Frobenius eigenvalues at `u` have complex absolute value `sqrt(p)`. Therefore

\[
|f_p(u)|\le2p^{p/2}
\]

for every embedding, and

\[
|\tau(\gamma_p)|\le4p^{p/2}
\]

for every real embedding `tau` of `K_p^+`.

The trivial field-trace estimate is

\[
|pT_p|
\le
2(p-1)p^{p/2}.
\]

The desired Airy estimate is

\[
|pT_p|
\le
C p^{(p+1)/2}.
\]

Hence the remaining analytic theorem is exactly a square-root saving across the

\[
\frac{p-1}{2}
\]

real embeddings of the primitive cyclotomic element `gamma_p`:

\[
\boxed{
\left|
\operatorname{Tr}_{K_p^+/\mathbf Q}(\gamma_p)
\right|
\le
C p^{(p+1)/2}.
}
\]

## 6. Ruling

### Proved

1. The local values form exactly two full real-cyclotomic Galois orbits, indexed by square class.
2. The signed complete Airy sum is the field trace of `gamma_p=f_p(1)+f_p(eta)`.
3. `gamma_p` itself generates the maximal real cyclotomic field.
4. The terminal bound is one square-root cancellation across its full set of real embeddings.

### Closed

- descent of the complete sum to a proper cyclotomic subfield;
- a bounded-degree Gaussian-period representation of the combined local value;
- a proof based solely on reducing the number of Galois conjugates.

### Open

A sign/correlation theorem for the full real orbit of `gamma_p`, equivalently the original Airy estimate.

## 7. Verification

`two_orbit_cyclotomic_trace_verify.py` checks the two Galois orbits, the signed trace identity and maximal orbit of `gamma_p` at the calibrated primes.
