# Replacement Paper VI: independent reconstruction record

**Date:** 2026-07-27  
**Scope:** integral tangent, secondary trace, Artin--Schreier/Kummer quotient and compactified count chain.

## 1. Cyclotomic tangent

For
\[
\mathcal F_a=\sum_{c,d}1_{\mathrm{irr}}\zeta^c,
\qquad \pi=\zeta-1,
\]
the binomial expansion gives
\[
\mathcal F_a=N_a+\pi M_a+O(\pi^2),
\qquad
M_a=\sum_{\mathrm{irr}}c\pmod p.
\]
Thus nonzero `M_a` is a sufficient fixed-class existence certificate, but the reconstruction does not assume it is uniformly nonzero.

## 2. Tangent module and Tate maps

Over `R=F_p[epsilon]/(epsilon^2)`, let `tau=1+epsilon`. Then `tau^p=1`, `tau-1` is multiplication by `epsilon`, and
\[
1+\tau+\cdots+\tau^{p-1}=0.
\]
The periodic Tate complex therefore alternates `epsilon` and zero. Kernel and image of multiplication by `epsilon` are both the line `epsilon R`, giving one copy of `F_p` in each parity. Lifting the quotient generator shows the coefficient Bockstein is the identity.

For every `lambda in F_p`, multiplication by `1+lambda epsilon` commutes with `tau`, acts identically on both graded lines and both Tate groups, and preserves the Bockstein, while its first trace coefficient is `lambda`. Hence these modular data do not determine the cyclotomic Frobenius tangent.

The clean-room script verifies these statements at `p=5,7,11`.

## 3. Divided-hook character obstruction

On the regular root cycle,
\[
\Theta_p=\lambda_{-1}(\operatorname{Std})=p\mathbf1-\operatorname{Reg}_{C_p}.
\]
Dividing its character by `p` gives the nonidentity indicator. Its Fourier multiplicity is `(p-1)/p` at the trivial character and `-1/p` at every nontrivial character. These are not integers, so the divided hook is not an ordinary characteristic-zero virtual representation and cannot be realised by an ordinary perfect complex.

The independent script records these fractional multiplicities at `p=5,7,11`.

## 4. Hattori--Stallings coefficient extraction

Let a finite free `Z[C_p]`-complex have alternating Hattori--Stallings trace
\[
h_\Phi=\sum_r h_r\sigma^r.
\]
On a regular lattice, multiplication by `sigma^j`, followed by `sigma^{-r}`, has ordinary trace `p` if `j=r` and zero otherwise. Summing diagonal group-ring entries gives
\[
\boxed{\operatorname{Tr}_{\mathbf Z}(\Phi\sigma^{-r})=p h_r.}
\]
This supplies an integral divided trace without asserting that the divided hook is a representation. Random group-ring matrices were used as clean-room regressions at `p=5,7`.

## 5. Cyclic transfer and Artin--Schreier coordinate

On the fixed nonzero cubic ordered-root slice, the root cycle acts freely: a fixed tuple would be diagonal, but then `e_(p-3)=0`, contradicting `a!=0`.

Every `(p-3)`-subset has a free translation orbit. Choosing one representative from each orbit gives a polynomial `t` with
\[
\sum_j\sigma^j(t)=e_{p-3}=a.
\]
For
\[
U=\sum_j j\sigma^j(t),
\]
reindexing gives `(sigma-1)U=-a`. Therefore
\[
y=-U/a,
\qquad \sigma(y)=y+1,
\qquad g=y^p-y
\]
is invariant and presents the quotient in the root-cycle direction as
\[
T^p-T=g.
\]
If `z` is a rational quotient point and `F(x)=sigma^r x` above it, then `g(z)=r`. The level `g=1` is therefore in bijection with irreducible fibres in the fixed class.

## 6. No-split theorem

If
\[
f=X^p+aX^3+cX+d,
\qquad a\ne0,
\]
split over `F_p`, then for `x in F_p` every distinct root would be a root of
\[
aX^3+(c+1)X+d.
\]
Let `R` be the product of the distinct root factors. Then `deg R<=3`. The reduced logarithmic derivative gives
\[
f'R=Pf,
\]
with nonzero `P`; the left side has degree at most five, while the right side has degree at least `p`. Thus `p<=5`. For `p>5`, the split quotient level is empty and
\[
\boxed{\#Y_a(F_p)=(p-1)N_a.}
\]
Finite regressions find no squarefree completely split case at `p=7,11`.

## 7. Kummer forms

Scalar dilation changes the fixed cubic coefficient by `lambda^(p-3)`. The two arithmetic forms are classified by
\[
H^1(F_p,\mu_{p-3})\cong F_p^*/(F_p^*)^{p-3}.
\]
Because `gcd(p-3,p-1)=2`, there are exactly two classes. In exponent notation Frobenius coboundaries are even, while `-1` has exponent `(p-3)/2`. Hence sign represents the nontrivial form exactly when
\[
p\equiv1\pmod4.
\]
The script checks this at `p=5,11,17,23,29`.

The full Kummer quotient packages the class sum:
\[
\#D_p(F_p)=\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2},
\qquad
\#U_p(F_p)=\frac{p-1}{2}(N_{\mathrm{sq}}+N_{\mathrm{ns}}).
\]
This is a positive carrier, but its rational-point theorem is exactly cubic positivity.

## 8. Proper quotient count

The root cycle has one projective fixed point, represented by
\[
[0,1,\ldots,p-1].
\]
Away from it the action is free. Every nonlinear irreducible affine orbit contributes one rational quotient point for each of the `p-1` nonzero Frobenius shifts. With
\[
W_p=N_2+\frac{N_{\mathrm{sq}}+N_{\mathrm{ns}}}{2},
\]
this gives
\[
\boxed{\#\mathscr Q_p(F_p)=1+(p-1)W_p.}
\]
The boundary has `1+(p-1)N_2` points and the cubic open has `(p-1)(N_sq+N_ns)/2` points. The independent ledger reproduces these formulas at `p=7,11,17,23`; at `p=17`, `W_p=17` and `#Q_p=273=1 mod 17`.

Consequently even a favourable standard congruence `#Q_p=1 mod p` permits both the failure value `W_p=0` and a known positive value `W_p=p`.

## 9. Boundary

The reconstructions establish the integral carriers and quotient geometry. They do not prove that the first moment is nonzero or that the quotient open has a rational point. The exact remaining theorem is a one-sided compactly-supported Frobenius/nonvanishing statement excluding the zero-point value.
