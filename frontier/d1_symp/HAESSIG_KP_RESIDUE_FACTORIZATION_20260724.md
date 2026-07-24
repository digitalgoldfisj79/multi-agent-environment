# Explicit residue factorization of the critical `k=p` Airy connection

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-haessig-kp-resonance-20260724`  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** the localized residue factorization and the `mu_3` count below are **PROVED**. No Frobenius trace bound follows from them.

## 0. Result

Let

\[
G_p q_i=A(p-i)q_{i+1}+Bi q_{i-1},
\qquad 0\le i\le p,
\]

where

\[
A=\pi a,
\qquad
B=-\frac{\pi a^2}{3},
\]

and missing terms are omitted. Work over the localized coefficient ring

\[
R=\mathbf Z_{(p)}[A^{\pm1},B^{\pm1}].
\]

Put

\[
n=\frac{p+1}{2}.
\]

The previous Smith audit proves that `G_p` has exactly two elementary `p`-divisors. The complete residue of its inverse is

\[
\boxed{
\begin{aligned}
pG_p^{-1}\pmod p
={}&q_0\otimes
\sum_{j=0}^{n-1}
\frac{B^j}{A^{j+1}}q_{2j+1}^{\vee}\\
&+q_p\otimes
\sum_{j=0}^{n-1}
\frac{A^{n-1-j}}{B^{n-j}}q_{2j}^{\vee}.
\end{aligned}
}
\]

Thus every terminal `1/p` coefficient in Haessig's reduction factors through one of two endpoint lines:

\[
\mathbf F_p q_0
\qquad\text{or}\qquad
\mathbf F_p q_p.
\]

However, after restoring the powers of `a`, the residue is not bounded-dimensional over the constant field in the exact `mu_3` sector. If

\[
p=6r+5,
\]

then the invariant Laurent residue contains exactly

\[
\boxed{2(r+1)=\frac{p+1}{3}}
\]

independent endpoint monomials before Dwork cohomological reduction.

This gives a precise form of the previously qualitative statement:

\[
\text{rank two over the localized function ring}
\not\Rightarrow
\text{bounded rank over constants after symmetry projection}.
\]

## 1. Right and left kernels modulo `p`

Modulo `p`,

\[
G_pq_0=G_pq_p=0.
\]

The Smith audit proves that the rank is `p-1`, hence

\[
\ker(G_p\bmod p)=\langle q_0,q_p\rangle.
\]

For a left-kernel row vector `lambda=(lambda_i)`, the column relation is

\[
A(p-i)\lambda_{i+1}+Bi\lambda_{i-1}=0.
\]

For `1<=i<=p-1`, division by the unit `i` gives

\[
\lambda_{i+1}=\frac BA\lambda_{i-1}\pmod p.
\]

Therefore the left kernel is the direct sum of the two parity chains

\[
\lambda_{2j+1}=\left(\frac BA\right)^j\lambda_1,
\qquad
\lambda_{2j}=\left(\frac BA\right)^j\lambda_0.
\]

## 2. PROVED: residue factorization

Set

\[
\mathcal R_p=pG_p^{-1}\pmod p.
\]

From

\[
G_p\mathcal R_p=pI
\]

we obtain

\[
G_p\mathcal R_p=0\pmod p.
\]

Hence every column of `mathcal R_p` lies in the right kernel, so only its `q_0` and `q_p` rows can be nonzero.

Similarly,

\[
\mathcal R_pG_p=0\pmod p
\]

forces each nonzero row to lie in one of the two left-kernel parity chains.

The normalizations are exact. Column `q_0` of `G_p` has the sole entry `pA` in row `q_1`, so

\[
(G_p^{-1}G_p)_{0,0}
=(G_p^{-1})_{0,1}pA=1.
\]

Consequently

\[
(pG_p^{-1})_{0,1}=A^{-1}.
\]

Likewise, column `q_p` has the sole entry `pB` in row `q_{p-1}`, giving

\[
(pG_p^{-1})_{p,p-1}=B^{-1}.
\]

Propagating these two normalizations along the left-kernel recurrences gives

\[
(pG_p^{-1})_{0,2j+1}
=\frac{B^j}{A^{j+1}}\pmod p
\]

and

\[
(pG_p^{-1})_{p,2j}
=\frac{A^{n-1-j}}{B^{n-j}}\pmod p.
\]

All remaining entries vanish. This proves the displayed factorization.

## 3. Restoring the Airy parameter

Substitute

\[
A=\pi a,
\qquad
B=-\frac{\pi a^2}{3}.
\]

Up to `p`-adic units and powers of `pi`, the first parity chain has parameter exponent

\[
\frac{B^j}{A^{j+1}}
\sim a^{j-1},
\]

while the second has exponent

\[
\frac{A^{n-1-j}}{B^{n-j}}
\sim a^{j-n-1}.
\]

Thus the two endpoint lines carry many distinct Laurent powers. They are rank two over the localized function ring but linearly growing over the constant field when the Laurent grading is retained.

The negative exponents also explain why this factorization does not itself produce an integral effective decomposition on Haessig's original Banach module at `a=0`: localization has exposed the resonance but has not solved the growth and completion problem.

## 4. PROVED: exact `mu_3`-invariant count

Under

\[
(a,x)\longmapsto(\zeta a,\zeta^{-1}x),
\qquad \zeta^3=1,
\]

use weights

\[
\operatorname{wt}(a)=1,
\qquad
\operatorname{wt}(v)=-1,
\qquad
\operatorname{wt}(w)=1
\]

modulo `3`. For

\[
q_i=v^{p-i}w^i,
\]

and `p=2 mod 3`,

\[
\operatorname{wt}(q_i)=-p+2i\equiv1+2i\pmod3.
\]

Hence

\[
q_i\text{ is invariant}\iff i\equiv1\pmod3.
\]

Write `p=6r+5`, so

\[
n=3r+3.
\]

### Odd parity chain

The input indices are

\[
i=2j+1,
\qquad 0\le j\le n-1.
\]

They are invariant exactly when

\[
2j+1\equiv1\pmod3,
\]

that is, `j=0 mod 3`. The indices

\[
j=0,3,\ldots,3r
\]

contribute `r+1` invariant Laurent endpoint monomials.

### Even parity chain

The input indices are

\[
i=2j,
\qquad 0\le j\le n-1.
\]

They are invariant exactly when

\[
2j\equiv1\pmod3,
\]

that is, `j=2 mod 3`. The indices

\[
j=2,5,\ldots,3r+2
\]

also contribute `r+1` invariant Laurent endpoint monomials.

Therefore

\[
\boxed{
\dim_{\mathbf F_p}
(\text{invariant Laurent residue support})
=2r+2=\frac{p+1}{3}.
}
\]

This count concerns distinct Laurent monomials before the completed Dwork quotient. It is not a cohomology-dimension statement.

## 5. Consequences for the proof programme

### PROVED

1. All critical `1/p` losses factor through two explicit endpoint residue lines over the localized function ring.
2. The residue covectors are explicit geometric progressions in `B/A`.
3. The exact `mu_3` projection leaves `(p+1)/3` distinct Laurent endpoint monomials before cohomological reduction.
4. Therefore the `mu_3` symmetry does not reduce the localized resonance to `O(1)` constant-field support.

### CLOSED naive inference

The following argument is invalid:

> the coefficient skeleton has only two elementary `p`-divisors, therefore the completed invariant Frobenius defect is a bounded two-dimensional block.

The two divisor classes acquire linearly many parameter degrees before the Dwork quotient, and the original integral growth conditions have not yet been restored.

### STILL OPEN

A Frobenius-dependent cancellation may identify or annihilate most of these Laurent classes after completion and cohomological reduction. Proving or refuting that requires the actual Dwork operator

\[
\beta_p=\psi_a\circ\operatorname{Sym}^p(A(a)),
\]

not merely the connection matrix.

The smallest remaining Dwork theorem is therefore:

> Compute the action of `beta_p` on the two explicit residue covectors above, restore the integral growth filtration at `a=0`, and determine the rank and trace of their image in the `mu_3`-invariant primitive quotient.

The present factorization supplies exact input data for that calculation but not its outcome.

## 6. Verification

`haessig_kp_residue_verify.py` performs exact rational inversion after several unit specializations of `(A,B)` and checks the predicted reduction of `pG_p^{-1}` modulo `p`, together with the invariant-support count. The specializations are regression checks of the proved symbolic formulas, not evidence replacing the proof.
