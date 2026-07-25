# Orientation-odd local inertia of the exceptional rank-four Laurent--Airy family

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** first analytic boulder for function-field `d=1`, primes `p congruent 5 mod 6`, `p>=11`.  
**Status:** the determinant identity and the generic boundary inertia statements below are **PROVED**, using the quoted local Fourier-transform theorems and the explicit stationary-phase expansions. They prove bounded **virtual local conductor**, not bounded actual global Betti complexity.

## 1. Family and projector

On

\[
B=\mathbf A^1_u\times\mathbf G_{m,s}
\]

put

\[
\mathscr H_B(u,s)
=H_c^1\!\left(
\mathbf G_{m,x},
\mathcal L_{\chi_2}(x)
\otimes
\mathcal L_\psi(x^3+ux+s/x)
\right).
\]

This is lisse of rank four on all of `B`.  The terminal generic class is

\[
\boxed{
\mathscr V_p
=
\Psi^p(\mathscr H_B)
\otimes
(\mathcal L_{\chi_2}(s)-\mathbf 1).
}
\]

## 2. The Kummer projector is the orientation character

Invert the integration variable, `y=1/x`.  Since the quadratic character is self-inverse,

\[
x^3+ux+s/x
=
y^{-3}+uy^{-1}+sy.
\]

For fixed `u`, this is the Laurent--Airy sheaf

\[
G(f,0,1,\chi_2),
\qquad
f(Y)=Y^3+uY,
\]

with parameter `s`.  Both `f` and the exponent `a=1` are odd.  Katz--Rojas-Leon--Tiep's determinant theorem for odd Laurent--Airy data gives

\[
\det(\mathscr H_B|_{u=u_0})
\cong
\mathcal L_{\chi_2}(s)
\]

for every `u_0`.  As `H^1(A^1_u,Z/2Z)=0`, no additional quadratic factor can vary in the `u` direction.  Therefore

\[
\boxed{
\det\mathscr H_B
\cong
\mathcal L_{\chi_2}(s)
}
\]

geometrically on `B`.

Consequently

\[
\boxed{
\mathscr V_p
=
\Psi^p(\mathscr H_B)\otimes(\det\mathscr H_B-\mathbf1).
}
\]

This is the orientation-odd Adams class of an orthogonally self-dual rank-four family.

## 3. A representation lemma for Adams operations on induced wild blocks

Let `I` be an inertia group, let `I_d` be the subgroup obtained after a tame extension of degree `d`, with `gcd(d,p)=1`, and let

\[
V=\operatorname{Ind}_{I_d}^{I}(\theta)
\]

where the wild part of the rank-one character `theta` has order `p`.

### Lemma 3.1

In the Grothendieck group of inertia representations,

\[
\boxed{
\Psi^p(V)
\text{ is tame and is a character twist of }
\operatorname{Reg}(\mu_d).
}
\]

### Proof

After restriction to wild inertia,

\[
V|_P=\bigoplus_{j=0}^{d-1}\theta_j.
\]

Adams operations commute with direct sums and send a rank-one character to its `p`-th power.  The wild part of every `theta_j` has order `p`, hence

\[
\theta_j^p|_P=1.
\]

Thus `Psi^p(V)` is tame.  On the tame quotient, for a generator `tau`,

\[
\operatorname{Tr}(\tau^k|\Psi^p(V))
=
\operatorname{Tr}(\tau^{kp}|V).
\]

Because `p` is invertible modulo `d`, `tau^(kp)` fixes an induction coset exactly when `d|k`.  Therefore the tame character vanishes off the identity of `mu_d` and has value `d` at the identity, up to a common rank-one tame twist.  This is the regular character.  \(\square\)

Any character twist of a regular representation is regular.  Hence

\[
\operatorname{Reg}(\mu_d)\otimes\kappa
\cong
\operatorname{Reg}(\mu_d)
\]

for every tame character `kappa` of `mu_d`.

## 4. The divisor `s=0`

The published local Fourier-transform formula gives

\[
\boxed{
\mathscr H_B|_{I(s=0)}
\cong
\mathbf1^{\oplus3}\oplus\chi_2.
}
\]

This can also be seen from the critical equation

\[
3x^4+ux^2-s=0.
\]

For generic `u!=0`, two critical branches remain finite and unramified, while the two branches approaching `x=0` are exchanged by the tame quadratic cover `s^(1/2)`.

Because `p` is odd,

\[
\Psi^p(\mathbf1^{\oplus3}\oplus\chi_2)
=
\mathbf1^{\oplus3}\oplus\chi_2.
\]

Therefore

\[
\boxed{
\mathscr V_p|_{I(s=0)}
=
2(\chi_2-\mathbf1).
}
\]

It is tame and has bounded virtual Artin conductor.

## 5. The divisor `s=infinity`: exact cancellation

The same local Fourier-transform theorem gives an irreducible rank-four inertia representation, all of whose slopes are

\[
\frac34.
\]

After the tame fourth-root cover `s=z^(-4)`, the four stationary branches satisfy

\[
x=a z^{-1}-\frac{u}{12a}z+O(z^3),
\qquad
3a^4=1,
\]

and the critical value is

\[
\boxed{
4a^3z^{-3}+ua z^{-1}+O(z).
}
\]

Thus the inertia representation is a tame degree-four induction of a rank-one Artin--Schreier character whose wild part has order `p`.  Lemma 3.1 yields

\[
\Psi^p(\mathscr H_B)|_{I(s=\infty)}
\cong
\operatorname{Reg}(\mu_4)\otimes\lambda
\]

for some tame character `lambda`.

The determinant character `chi_2(s)` restricts to the quadratic character of `mu_4`.  Since the regular representation is invariant under every character twist,

\[
\boxed{
\mathscr V_p|_{I(s=\infty)}=0
}
\]

in the Grothendieck group.  The entire generic wild-infinity contribution cancels, not merely its Swan conductor.

## 6. The divisor `u=infinity`

Put `u=z^(-2)` and retain `s!=0`.  The critical equation has two large and two small branches.

### Large branches

For `a^2=-1/3`,

\[
x=a z^{-1}-\frac{s}{2a}z^3+O(z^5),
\]

and, using the critical-point identity

\[
\phi(x)=4x^3+2ux,
\]

one obtains

\[
\boxed{
\phi(x)=\frac{2a}{3}z^{-3}+\frac{s}{a}z+O(z^3).
}
\]

This is a rank-two tame induction with slope `3/2`.

### Small branches

For `a^2=s`,

\[
x=az+O(z^5),
\]

and

\[
\boxed{
\phi(x)=2az^{-1}+O(z^3).
}
\]

This is a rank-two tame induction with slope `1/2`.

Hence

\[
\boxed{
\mathscr H_B|_{I(u=\infty)}
=V_{3/2}\oplus V_{1/2},
}
\]

where each `V` is induced from a rank-one order-`p` wild character on a quadratic tame cover.

Lemma 3.1 gives

\[
\boxed{
\Psi^p(\mathscr H_B)|_{I(u=\infty)}
\cong
\operatorname{Reg}(\mu_2)^{\oplus2}
}
\]

up to tame character twists.  In particular, it is tame of bounded rank.  The Kummer factor in `s` has no transverse `u`-inertia, so the two terms of `V_p` have identical `u`-inertia.  Therefore the virtual Artin conductor of `V_p` along generic `u=infinity` is zero.

## 7. No interior discriminant divisor

The stationary critical cover has equation

\[
3x^4+ux^2-s=0
\]

and branch discriminant

\[
\Delta=u^2+12s.
\]

However, `H_B` itself is lisse on all of `A^1_u x G_m,s`: the pole orders at `x=0` and `x=infinity` and their nonzero leading coefficients are constant there.  The divisor `Delta=0` is only the ramification locus of the stationary-phase splitting cover, not a singular divisor of `H_B`.  It contributes no Artin conductor to the original sheaf or to its Adams class.

## 8. Result of the requested local calculation

### Proved

1. The Kummer projector is exactly `det(H_B)-1`.
2. At `s=infinity`, the Kummer-projected `p`-th Adams class vanishes identically in the local Grothendieck group.
3. At `s=0`, the residual class is the bounded tame class `2(chi_2-1)`.
4. At generic `u=infinity`, the Adams class becomes two tame regular quadratic blocks and the Kummer difference has zero virtual transverse conductor.
5. There is no interior discriminant conductor.

Thus every generic codimension-one boundary has bounded virtual local complexity; the largest wild block cancels exactly.

### Not yet proved

This does **not** by itself construct an actual bounded-rank global complex representing `V_p`.  The standard Schur realization still has rank of order `p^3`.  Virtual local conductor cancellation does not automatically bound the total dimensions of the positive and negative global cohomology groups.

The next exact question is now narrower:

> **Orientation-cover tensor-induction theorem.** On the quadratic orientation cover `s=r^2`, prove that `H_B` is the tensor product of two rank-two local systems exchanged by the deck involution, and identify the orientation-odd `p`-th Adams trace with the `p`-th Adams trace of the resulting rank-two norm representation at nonsplit points.

If this holds, the rank-four Adams problem collapses object-wise to a rank-two family.  If it fails, the local calculation still closes any claim that unbounded wild boundary conductor is the obstruction.