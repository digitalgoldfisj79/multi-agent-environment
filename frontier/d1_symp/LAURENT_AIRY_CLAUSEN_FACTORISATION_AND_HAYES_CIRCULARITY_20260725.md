# Laurent--Airy Clausen factorisation and exact circularity of the Hayes route

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** terminal analytic `d=1` correlation, primes `p congruent 5 mod 6`.  
**Status:** the all-extension Clausen identity, the Spin-factor identification and the Hayes circularity theorem below are **PROVED**.  The pointwise identity is exhaustively verified at `p=5,11,17,23` over the base field.

## 1. Rank-two cubic Airy and rank-four Laurent--Airy traces

For a finite extension `k/F_p`, write

\[
t_k(a)
=-\sum_{z\in k}\psi_k(z^3+az)
\]

for the rank-two cubic Airy trace, and

\[
h_k(U,s)
=-\sum_{x\in k^*}\chi_k(x)
\psi_k(x^3+Ux+s/x)
\]

for the rank-four Laurent--Airy trace.

Put

\[
G_k=\sum_{z\in k}\psi_k(z^2).
\]

Because `p congruent 2 mod 3`, cubing is a bijection of `F_p^*`.  Let

\[
\alpha\in\mathbf F_p^*,
\qquad
\alpha^3=4.
\]

Since `4` is a square and the inverse of `3` modulo `p-1` is odd,

\[
\chi(\alpha)=1.
\]

Moreover

\[
\chi(-3\alpha)=-1
\]

for `p congruent 5 mod 6`.

## 2. Exact Clausen identity

### Theorem 2.1

Let `u,r in k`, with `r!=0`, and put

\[
U=\alpha u,
\qquad
s=-\frac{r^2}{3\alpha}.
\]

Then

\[
\boxed{
t_k(u+r)t_k(u-r)
=
-\chi_k(3)G_k\,h_k(U,s).
}
\]

### Proof

Expand the product and put

\[
x=z+y,
\qquad
y=x-z.
\]

The exponent becomes

\[
\begin{aligned}
&z^3+(x-z)^3+(u+r)z+(u-r)(x-z)\\
&\qquad=
3xz^2+(-3x^2+2r)z+x^3+ux-rx.
\end{aligned}
\]

When `x=0`, the inner sum is

\[
\sum_z\psi_k(2rz)=0.
\]

For `x!=0`, evaluate the quadratic Gauss sum in `z`:

\[
\sum_z\psi_k(3xz^2+(-3x^2+2r)z)
=
\chi_k(3x)G_k
\psi_k\!\left(
-\frac{(-3x^2+2r)^2}{12x}
\right).
\]

After adding the constant term, the phase simplifies exactly to

\[
\frac{x^3}{4}+ux-\frac{r^2}{3x}.
\]

Now substitute `x=alpha y`.  Since `alpha^3=4` and `chi_k(alpha)=1`, the phase becomes

\[
y^3+Uy+s/y.
\]

The remaining sum is `-h_k(U,s)`, proving the formula.  \(\square\)

## 3. The identity covers exactly the nonsquare sector

For `r!=0`,

\[
\chi(s)
=
\chi\!\left(-\frac1{3\alpha}\right)
=-1.
\]

Conversely, every nonsquare `s in F_p^*` has exactly two representations

\[
s=-\frac{r^2}{3\alpha},
\qquad
r\in\mathbf F_p^*.
\]

Thus the Clausen identity identifies precisely the nonsquare fibres retained by the factor `chi(s)-1` in the terminal Hayes projector.

## 4. Sheaf-theoretic Spin factors

Let `A` denote the rank-two cubic Airy sheaf with trace `t_k(a)`.  Let `C` be the constant rank-one sheaf whose arithmetic Frobenius eigenvalue is

\[
c=-\chi(3)G_p.
\]

Hasse--Davenport gives, for every extension degree `n`,

\[
c^n=-\chi_{p^n}(3)G_{p^n}.
\]

Therefore Theorem 2.1 holds for every Frobenius power and gives an isomorphism of semisimplified Weil sheaves on the nonsquare orientation cover:

\[
\boxed{
\mathcal A_{u+r}\otimes\mathcal A_{u-r}
\cong
\mathcal C\otimes
\mathscr H_B(\alpha u,-r^2/(3\alpha)).
}
\]

Equivalently,

\[
\boxed{
\mathscr H_B(\alpha u,-r^2/(3\alpha))
\cong
\mathcal C^{-1}
\otimes
\mathcal A_{u+r}
\otimes
\mathcal A_{u-r}.
}
\]

This explicitly identifies the two abstract `Spin_4` factors from the orientation-cover theorem: they are the two shifted cubic Airy sheaves.

## 5. The generic Hayes projector

Put

\[
f_p(a)=\operatorname{Tr}(F^p\mid\mathcal A_a)
=D_p(t_p(a),p).
\]

The frozen sign convention is

\[
\boxed{
\sum_{a\in\mathbf F_p}f_p(a)=-pT_p.
}
\]

For the rank-four fibre, the Hayes coefficient is

\[
I_B(U,s)
=-\frac1p
\operatorname{Tr}(F^p\mid\mathscr H_{B,(U,s)}).
\]

Using the all-power Clausen identity and the two-to-one map `r -> s` gives

\[
\begin{aligned}
\mathcal C_{\mathrm{gen}}
&:=
\sum_{U\in\mathbf F_p}
\sum_{s\in\mathbf F_p^*}
(\chi(s)-1)I_B(U,s)\\
&=
\frac{c^{-p}}p
\sum_{u\in\mathbf F_p}
\sum_{r\in\mathbf F_p^*}
 f_p(u+r)f_p(u-r).
\end{aligned}
\]

The map

\[
(u,r)\longmapsto(a,b)=(u+r,u-r)
\]

is a bijection from `F_p x F_p^*` to the ordered pairs `a!=b`.  Hence

\[
\boxed{
\mathcal C_{\mathrm{gen}}
=
\frac{c^{-p}}p
\left[
\left(\sum_a f_p(a)\right)^2
-
\sum_a f_p(a)^2
\right].
}
\]

## 6. Exact boundary identities

Let

\[
\mathcal A_{0,p}=\sum_u I_A(u,0),
\qquad
\mathcal B_{0,p}=\sum_u I_B(u,0).
\]

### Theorem 6.1

\[
\boxed{
\mathcal A_{0,p}=G_p^p.
}
\]

### Proof

Additive orthogonality in `u` gives

\[
\mathcal A_{0,p}
=
\sum_{\substack{x\in\mathbf F_{p^p}^*\\
\operatorname{Tr}(x)=0}}
\chi_E(x)\Psi(x^{-1}).
\]

Expanding the trace-zero indicator and applying the finite-field Salie identity to

\[
\sum_{x\ne0}\chi_E(x)\Psi(vx+x^{-1})
\]

shows that the `v=0` term contributes `G_E`, while the nonzero square `v` contribute a total of `(p-1)G_E`.  Division by `p` yields `G_E=G_p^p`.  \(\square\)

Put

\[
Q_p=\sum_{a\in\mathbf F_p} f_p(a)^2.
\]

### Theorem 6.2

\[
\boxed{
Q_p
=
p^{p+1}
+p\chi(3)G_p^p\mathcal B_{0,p}.
}
\]

### Proof

Expand the square and sum over `a`.  Orthogonality gives

\[
Q_p
=p
\sum_{\substack{x,y\in E\\
\operatorname{Tr}(x+y)=0}}
\Psi(x^3+y^3).
\]

Put `h=x+y`.  At `h=0`, the inner `x`-sum is `p^p`.  For `h!=0`,

\[
x^3+(h-x)^3
=3hx^2-3h^2x+h^3,
\]

and the quadratic Gauss sum is

\[
\chi_E(3h)G_E\Psi(h^3/4).
\]

Scaling `h=alpha z`, using `alpha^3=4`, identifies the residual trace-zero sum with `B_(0,p)`.  Hasse--Davenport gives `G_E=G_p^p`.  \(\square\)

Since

\[
c=-\chi(3)G_p,
\qquad
G_p^2=\chi(-1)p,
\qquad
\chi(3)=-\chi(-1),
\]

Theorems 6.1 and 6.2 imply

\[
\boxed{
\mathcal A_{0,p}-\mathcal B_{0,p}
=
\frac{c^{-p}}p Q_p.
}
\]

## 7. Exact Hayes circularity theorem

The two-plane reduction gives

\[
\mathcal A_p-\mathcal B_p
=
\mathcal A_{0,p}-\mathcal B_{0,p}
+\mathcal C_{\mathrm{gen}}.
\]

Substituting the two exact formulas above cancels `Q_p` and yields

\[
\boxed{
\mathcal A_p-\mathcal B_p
=
\frac{c^{-p}}p
\left(\sum_a f_p(a)\right)^2
=
c^{-p}pT_p^2.
}
\]

The terminal Hayes identity is

\[
T_p^2
=
\frac{\chi(-1)p^{(p-1)/2}}{G_p}
(\mathcal A_p-\mathcal B_p).
\]

But

\[
c^p=(-\chi(3)G_p)^p
=\chi(-1)G_p^p
\]

and

\[
G_p^{p+1}=p^{(p+1)/2}
\]

for the admitted primes.  Therefore the scalar multiplying `T_p^2` after substitution is exactly one.

### Theorem 7.1

The Hayes two-parameter correlation theorem, after the exact Kummer projection and Spin/Clausen factorisation, is algebraically identical to

\[
\left|\sum_a f_p(a)\right|
\ll p^{(p+1)/2},
\]

which is the original Airy estimate

\[
|T_p|\ll p^{(p-1)/2}.
\]

It does not supply an independent proof of that estimate.

## 8. Ruling

### Proved

- an all-Frobenius finite-field Clausen identity for the exceptional rank-four Laurent--Airy family;
- explicit identification of its two Spin factors as shifted cubic Airy sheaves;
- exact formulas for both zero-parameter boundary sums;
- exact reduction of the full Hayes correlation to the square of the original Airy first moment.

### Closed

- obtaining a new Airy bound from the Hayes two-plane formulation by factorising the rank-four family;
- using the diagonal second moment `Q_p` to gain the missing factor, because it cancels exactly against the boundary difference;
- treating the Hayes correlation as an independent lower-complexity theorem.

### Remaining analytic wall

The wall returns, without loss or gain, to the one-dimensional rank-two Airy Adams first moment

\[
\boxed{
\left|
\sum_{a\in\mathbf F_p}
D_p(t_p(a),p)
\right|
\ll p^{(p+1)/2}.
}
\]

Equivalently, prove the absolute Frobenius correlation between the two adjacent invariant Airy moment motives already isolated on the branch.