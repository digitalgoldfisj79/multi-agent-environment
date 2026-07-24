# Kummer averaging and the full Airy--primitive Weil bridge

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling, primes `p=5 mod 6`.  
**Status:** the trace identities and virtual Frobenius-character identity below are **PROVED**. The absolute trace estimate and the final hook/irreducibility transport remain **OPEN**.

## 0. Main theorem

Let

\[
\mathcal D_p=M_{0,p}-M_{1,p}
\]

be the rank-zero cyclic multiplicity difference from
`CYCLIC_REGULARITY_AND_TWO_BLOCK_REDUCTION_20260724.md`.

Let

\[
U_k=H_c^1
(\mathbf A^1_{\overline{\mathbf F}_p},\operatorname{Sym}^k\mathcal A)^{\mu_3}
\]

and

\[
\mathcal R_p=U_p-U_{p-2}(-1).
\]

Then, for every integer `r>=1`,

\[
\boxed{
\operatorname{Tr}(F^r|\mathcal R_p)
=
p^{3r}\operatorname{Tr}(F^r|\mathcal D_p).
}
\]

Equivalently,

\[
\boxed{
\operatorname{Tr}(F^r|\mathcal R_p)
=
\operatorname{Tr}(F^r|\mathcal D_p(-3))
\qquad(r\ge1).
}
\]

The two virtual Weil modules therefore have the same Frobenius characteristic series. In the Grothendieck group of semisimple Weil representations,

\[
\boxed{
\mathcal R_p^{ss}
=
\mathcal D_p(-3)^{ss}.
}
\]

In determinant form,

\[
\boxed{
\frac{\det(1-TF|U_p)}
     {\det(1-TF|U_{p-2}(-1))}
=
\frac{\det(1-p^3TF|M_{0,p})}
     {\det(1-p^3TF|M_{1,p})}.
}
\]

Thus the enormous cyclic multiplicity ratio collapses exactly to the already isolated small Airy virtual ratio. This is an object-level statement in the semisimple virtual Weil category, not only a first-trace equality.

## 1. Full Airy module and its `mu_3` action

Before projection, put

\[
\widetilde H_k
=H_c^1
(\mathbf A^1_{\overline{\mathbf F}_p},\operatorname{Sym}^k\mathcal A)
\]

and

\[
\widetilde{\mathcal R}_p
=
\widetilde H_p-\widetilde H_{p-2}(-1).
\]

The cubic Airy family has the geometric `mu_3` symmetry

\[
(u,x)\longmapsto(\zeta u,\zeta^{-1}x),
\qquad \zeta^3=1,
\]

which preserves

\[
x^3+ux.
\]

The invariant virtual module is exactly

\[
\widetilde{\mathcal R}_p^{\mu_3}
=
\mathcal R_p.
\]

## 2. Coefficient twists are Kummer twists

Let

\[
k=\mathbf F_Q,
\qquad Q=p^r,
\]

and let `c in k^*`. Write `A_c` for the cubic Airy sheaf with trace function

\[
u\longmapsto-
\sum_{x\in k}
\psi_k(c x^3+ux).
\]

Choose `s in kbar` with

\[
s^3=c.
\]

The substitution

\[
y=sx
\]

gives

\[
cx^3+ux
=y^3+(u/s)y.
\]

Thus, over `kbar`, `A_c` is obtained from `A_1` by the scalar change of parameter

\[
u\longmapsto u/s.
\]

Its descent cocycle is

\[
\frac{s^Q}{s}\in\mu_3.
\]

Changing `c` by a cube changes `s` by an element of `k^*` and leaves the cocycle class unchanged. Consequently the coefficient classes

\[
k^*/(k^*)^3
=H^1(k,\mu_3)
\]

are exactly the Kummer twists of the geometric Airy module.

Let

\[
\widetilde{\mathcal R}_{p,c}
=
H_c^1(\operatorname{Sym}^p A_c)
-
H_c^1(\operatorname{Sym}^{p-2}A_c)(-1).
\]

After choosing a geometric trivialization, Frobenius on this twist is

\[
g_cF^r
\]

on `widetilde R_p`, where `g_c in mu_3` represents the Kummer cocycle.

## 3. Kummer averaging equals the invariant projector

Put

\[
d_r=|H^1(\mathbf F_Q,\mu_3)|
=\gcd(3,Q-1).
\]

### Odd `r`

Then `Q=2 mod 3`, so `d_r=1`. There is one coefficient class. Arithmetic Frobenius exchanges the two nontrivial geometric `mu_3` character spaces, and its odd power has zero trace on their direct sum. Hence

\[
\operatorname{Tr}(F^r|\widetilde{\mathcal R}_p)
=
\operatorname{Tr}(F^r|\mathcal R_p).
\]

This is the existing odd-power extraction theorem.

### Even `r`

Then `Q=1 mod 3`, `mu_3` is split over `k`, and

\[
H^1(k,\mu_3)\cong\mu_3.
\]

As the coefficient class `c` runs over `k^*/(k^*)^3`, the cocycle `g_c` runs over all three elements of `mu_3`. Therefore

\[
\frac13
\sum_{c\in k^*/(k^*)^3}
\operatorname{Tr}(F_Q|\widetilde{\mathcal R}_{p,c})
=
\frac13
\sum_{g\in\mu_3}
\operatorname{Tr}(gF^r|\widetilde{\mathcal R}_p).
\]

The operator

\[
\frac13\sum_{g\in\mu_3}g
\]

is the projector onto the invariant subspace. Hence

\[
\boxed{
\frac1{d_r}
\sum_{c\in k^*/(k^*)^3}
\operatorname{Tr}(F_Q|\widetilde{\mathcal R}_{p,c})
=
\operatorname{Tr}(F^r|\mathcal R_p)
}
\]

for every `r`, odd or even.

This proves that the even discrepancy `Delta_{p,r}` defined in
`ALL_COPRIME_EXTENSION_THREE_TWIST_BRIDGE_20260724.md` is identically zero.

## 4. Relative Artin--Schreier twist in every degree

For each `r>=1`, let

\[
k_r=\mathbf F_{p^r},
\qquad
L_r=\mathbf F_{p^{rp}}.
\]

The extension

\[
L_r/k_r
\]

is a cyclic torsor of degree `p`. Twist the split permutation complete intersection `X_p^perm` by this torsor and the fixed generator `sigma in C_p`. Denote the resulting `k_r`-form by

\[
X_{p,r}^{rel}.
\]

After choosing an embedding ordering, its geometric Frobenius is

\[
\sigma^{\pm1}F^r
\]

on the split model. The sign is harmless because the two cyclic orientations are conjugate in the affine normalizer.

The descended equations are exactly

\[
\operatorname{Tr}_{L_r/k_r}(x)=0,
\qquad
\operatorname{Tr}_{L_r/k_r}(x^2)=0,
\qquad
\operatorname{Tr}_{L_r/k_r}(x^3)=0,
\]

modulo translation by `k_r`. Thus `X_{p,r}^{rel}` is the relative trace-form variety attached to the degree-`p` field extension used by the Airy Adams moment.

This relative twist exists for every `r`, including `p|r`.

## 5. Distinction from base change of one fixed twist

The fixed `F_p`-form `X_p^AS` has descent cocycle `sigma`. After base extension to `F_{p^r}`, its cocycle becomes

\[
\sigma^r.
\]

Therefore:

- if `p` does not divide `r`, `sigma^r` is nontrivial and conjugate to `sigma`, so the base-changed fixed twist is isomorphic to the relative twist;
- if `p|r`, `sigma^r=1`, so the fixed twist becomes split, whereas the relative degree-`p` field twist remains nontrivial.

The Airy moment always uses the relative twist, not the base change of one fixed `F_p`-form. This is the exact geometric meaning of the previously identified Adams-through-pushforward noncommutation.

## 6. Relative projective trace in every degree

For a coefficient class `c in k_r^*/(k_r^*)^3`, define

\[
T_{p,r}^{(c)}
=
\sum_{x\in L_r,\ \operatorname{Tr}(x)=0}
\psi_r(\operatorname{Tr}(c x^3)).
\]

The cube-class orthogonality calculation gives

\[
\#X_{p,r}^{rel}(k_r)
-
\#\mathbf P^{p-5}(k_r)
=
\frac1{d_rp^{2r}}
\sum_c T_{p,r}^{(c)}.
\]

On primitive cohomology, relative twisted descent and cyclic regularity give

\[
\operatorname{Tr}
(\sigma^{\pm1}F^r|H_p)
=
\operatorname{Tr}(F^r|\mathcal D_p).
\]

Therefore

\[
\boxed{
\operatorname{Tr}(F^r|\mathcal D_p)
=
\frac1{d_rp^{2r}}
\sum_c T_{p,r}^{(c)}
}
\]

for every `r>=1`.

## 7. Airy trace in every degree

For each coefficient class, the rank-two Adams identity and additive orthogonality give

\[
\operatorname{Tr}
(F_Q|\widetilde{\mathcal R}_{p,c})
=
Q T_{p,r}^{(c)}.
\]

Average over Kummer classes and apply the invariant-projector identity:

\[
\operatorname{Tr}(F^r|\mathcal R_p)
=
\frac{Q}{d_r}
\sum_c T_{p,r}^{(c)}.
\]

Combining with the relative projective formula yields

\[
\operatorname{Tr}(F^r|\mathcal R_p)
=
Q^3\operatorname{Tr}(F^r|\mathcal D_p).
\]

Since `Q=p^r`, this proves the main theorem for every `r`.

## 8. Virtual Weil-module identity

For a virtual Frobenius module `V`, put

\[
L(V,T)=\det(1-TF|V)^{-1}.
\]

The formal logarithm satisfies

\[
\log L(V,T)
=
\sum_{r\ge1}
\operatorname{Tr}(F^r|V)\frac{T^r}{r}.
\]

The equality of all power traces therefore gives

\[
L(\mathcal R_p,T)
=
L(\mathcal D_p(-3),T).
\]

Both virtual modules have rank zero:

\[
\dim U_p=\dim U_{p-2}=(p-5)/6,
\qquad
\dim M_{0,p}=\dim M_{1,p}.
\]

Thus their semisimplified virtual Frobenius eigenvalue multisets coincide, proving

\[
\mathcal R_p^{ss}=\mathcal D_p(-3)^{ss}.
\]

## 9. What this closes

### CLOSED

1. The Airy-to-linear-section object comparison in the semisimple virtual Weil category.
2. The even-power `mu_3` projector defect, once all Kummer coefficient twists are included.
3. The apparent `p`-divisible failure, by distinguishing relative twists from base change of a fixed twist.
4. The exact Tate normalization.
5. The full Frobenius characteristic ratio, not only the first trace.

### STILL OPEN — analytic branch

The identity reduces the analytic theorem back to the small Airy virtual module:

\[
|\operatorname{Tr}(F|\mathcal R_p)|
\le C p^{(p+1)/2}.
\]

The equality of virtual modules does not itself prove an absolute constant. It explains the exponential cancellation but leaves the correlation between `U_p` and `U_{p-2}(-1)` open.

### STILL OPEN — application branch

The remaining bridge is no longer Airy versus the cyclic primitive motive. It is the transport of this now-identified virtual module into the exact post-pushforward hook/nearby-cycle irreducibility ledger, including:

- the `q=2` and `q=infinity` cells;
- the arithmetic quadratic twist in the hook normalization;
- Artin--Schreier/main/Tate subtraction;
- endpoint/punctual terms;
- the parity-protected certificate.

## 10. Verification

The existing scripts provide independent checks in every currently accessible sector:

- `twisted_descent_trace_verify.py`: first relative trace and projective normalization;
- `cyclic_regularity_verify.py`: regular `C_p` character and direct `p=5` fixed-point model;
- `odd_extension_bridge_verify.py`: exact `r=1` and certified `r=3` Airy/primitive divisibility at `p=11,17,23,29`;
- `three_twist_bridge_verify.py`: complete even `p=5,r=2` Kummer-average check over `F_25`.

The all-degree Kummer averaging and relative-twist arguments are symbolic proofs, not extrapolations from these checks.
