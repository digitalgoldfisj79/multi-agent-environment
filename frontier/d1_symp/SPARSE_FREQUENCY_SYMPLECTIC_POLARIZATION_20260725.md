# Canonical symplectic polarization of the sparse frequency quotient

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** the nonzero sparse-frequency space in the function-field `d=1` Fourier--Cayley/Smith-defect programme.  
**Status:** **PROVED** for every odd prime `p>=11`.

## 1. The frequency quotient

Let `k` be a field of characteristic `p`. The complete generalized-Airy coefficient space is

\[
k[T]_{\le p-4}.
\]

The constant coefficient has zero extension trace, and the multiplier directions are the cubic tail

\[
k[T]_{\le3}.
\]

The genuine sparse-frequency quotient is therefore

\[
\boxed{
\mathcal V_p
=
k[T]_{\le p-4}/k[T]_{\le3}.
}
\]

It has basis represented by

\[
T^4,T^5,\ldots,T^{p-4}
\]

and dimension

\[
\dim\mathcal V_p=p-7.
\]

Since `p` is odd, write

\[
p-7=2m,
\qquad
m=\frac{p-7}{2}.
\]

## 2. Characteristic-p Wronskian pairing

For representatives `f,g` of classes in `V_p`, define

\[
\boxed{
\omega_p([f],[g])
=
[T^{p-1}]\left(f'(T)g(T)-f(T)g'(T)\right).
}
\]

### Well-definedness

If `deg f<=3` and `deg g<=p-4`, then

\[
\deg(f'g-fg')\le p-2,
\]

so the coefficient of `T^(p-1)` is zero. Thus `k[T]_(<=3)` lies in the radical before quotienting, and the formula descends to `V_p`.

The form is visibly alternating because `p` is odd.

## 3. Exact monomial matrix and nondegeneracy

For `4<=a,b<=p-4`,

\[
\boxed{
\omega_p(T^a,T^b)
=(a-b)\,\mathbf1_{a+b=p}.
}
\]

Hence every degree `a` is paired only with the complementary degree `p-a`. The antidiagonal entry is

\[
a-(p-a)=2a-p,
\]

which is nonzero in characteristic `p` because `1<=a<=p-1` and `p` is odd.

Therefore

\[
\boxed{
\omega_p\text{ is nondegenerate on }\mathcal V_p.
}
\]

Over a `p`-adic integral coefficient ring, every antidiagonal entry `2a-p` is a unit. Thus the pairing is integrally perfect at `p`; no new `p`-adic denominator or resonance is introduced.

## 4. Canonical half-dimensional polarization

Put

\[
\mathcal L_p
=
\operatorname{span}
\left\{
T^4,T^5,\ldots,T^{(p-1)/2}
\right\}.
\]

Then

\[
\dim\mathcal L_p=m=\frac{p-7}{2}.
\]

If `a,b<=(p-1)/2`, then `a+b<=p-1`, so

\[
\omega_p(T^a,T^b)=0.
\]

Because `L_p` has half the dimension of `V_p`, it is Lagrangian:

\[
\boxed{
\mathcal L_p=\mathcal L_p^{\perp}.
}
\]

A complementary Lagrangian is

\[
\mathcal L_p^+
=
\operatorname{span}
\left\{
T^{(p+1)/2},\ldots,T^{p-4}
\right\},
\]

with perfect pairings

\[
T^a\longleftrightarrow T^{p-a}.
\]

## 5. Affine invariance

Translation acts on polynomial phases by

\[
(\tau_bf)(T)=f(T+b).
\]

It preserves `k[T]_(<=3)` and hence acts on `V_p`.

For a polynomial `H` of degree at most `2p-9`, the coefficient of `T^(p-1)` is translation invariant in characteristic `p`:

\[
[T^{p-1}]H(T+b)=[T^{p-1}]H(T).
\]

Indeed, a possible contribution from a term `T^n` with `p<=n<=2p-9` is multiplied by

\[
\binom n{p-1},
\]

which vanishes modulo `p` by Lucas' theorem. Derivatives commute with translation, so

\[
\boxed{
\omega_p(\tau_bf,\tau_bg)=\omega_p(f,g).
}
\]

The lower-degree Lagrangian `L_p` is stable under translation because translation is degree triangular. It is also stable under root scaling. Thus `L_p` is a canonical `Aff_1`-invariant Lagrangian in the sparse-frequency quotient.

For scaling `rho_a f(T)=f(aT)`,

\[
\omega_p(\rho_af,\rho_ag)=a^p\omega_p(f,g),
\]

so the full affine group acts conformally symplectically; the multiplier is the natural Frobenius character on the value line.

## 6. Exact relation to the required half twist

The Fourier frequency codimension is

\[
c=p-7=2m.
\]

The localization triangle shows that transporting the ambient Airy block `D_p` into the sparse weight-two normalization requires the open-sector virtual identity

\[
\boxed{
\mathcal D_p(-m)-\mathcal D_p.
}
\]

But

\[
R\Gamma_c(\mathbf A^m\setminus\{0\},\mathbf Q_\ell)
=
\mathbf Q_\ell(-m)-\mathbf Q_\ell
\]

in the Grothendieck group. Therefore

\[
\boxed{
\mathcal D_p(-m)-\mathcal D_p
=
\mathcal D_p\otimes
R\Gamma_c(\mathbf A^m\setminus\{0\},\mathbf Q_\ell).
}
\]

The half-codimension Tate shift in the desired theorem is therefore not numerology. It is exactly the compactly supported cohomology of a punctured affine space modelled on the canonical Lagrangian `L_p`.

## 7. Consequence for the wild-infinity programme

The broad open-sector problem can now be replaced by a precise local mechanism:

> **Polarized wild-infinity lemma.** After subtracting the explicit Tate, discriminant, affine-quotient and q-line boundary ledger, the Airy-isotypic part of the nonzero-frequency Smith-defect nearby-cycle complex is the external product of `D_p` with the punctured canonical Lagrangian `L_p minus {0}`.

Equivalently,

\[
\left[\mathcal K_\times\right]_{\mathcal D_p}
=
\mathcal D_p(-m)-\mathcal D_p.
\]

Combined with the exact localization triangle, this gives

\[
\left[\mathcal K_Y\right]_{\mathcal D_p}
=
\mathcal D_p(m)
=
\mathcal R_p\left(\frac{p-1}{2}\right),
\]

which is precisely the required weight-two Airy constituent.

## 8. Scientific status

### Proved

1. The sparse-frequency quotient has even dimension `p-7`.
2. It carries the displayed nondegenerate characteristic-p symplectic form.
3. Complementary polynomial degrees `a` and `p-a` are exact symplectic partners.
4. The lower-degree half is a canonical affine-invariant Lagrangian of dimension `(p-7)/2`.
5. The required Airy open-sector virtual class is exactly `D_p` tensored with the punctured Lagrangian cohomology.

### Open

The wild-infinity nearby-cycle complex has not yet been identified with this polarized oscillator model. That identification, including Frobenius and the cyclic trivial-minus-nontrivial projector, is the remaining new mathematical lemma.
