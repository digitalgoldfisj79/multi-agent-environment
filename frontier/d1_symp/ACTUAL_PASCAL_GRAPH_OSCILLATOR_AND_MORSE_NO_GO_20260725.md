# Actual Pascal graph oscillator and classical Morse no-go

**Date:** 2026-07-25  
**Branch:** `gpt56/airy-gaussian-independent-audit-20260725`  
**Scope:** the linear kernel attached to the proved high Pascal coefficient--normal correspondence, and the exact boundary of ordinary stationary phase.  
**Status:** the block theorem, generating function, all-power oscillator sum and classical Morse no-go below are **PROVED**. The nonlinear divided-power nearby-cycle realization remains **OPEN**.

## 1. Setup

Let

\[
 p\ge 11
\]

be odd, put

\[
 m=\frac{p-7}{2},
 \qquad
 H=\{4,5,\ldots,p-4\},
\]

and let

\[
 \mathcal V_p=\operatorname{span}\{e_a:a\in H\}
\]

with residue symplectic form

\[
 \omega(e_a,e_b)=(a-b)\mathbf 1_{a+b=p}.
\]

The actual Laurent/Pascal coefficient--normal map is

\[
 D_{j,a}=(-1)^j\binom{a+j-1}{j}
 \quad(j,a\in H)
\]

in characteristic `p`. The preceding Pascal theorem proves

\[
 D^tWD=-W.
\]

Thus `D` is anti-symplectic.

Put

\[
 L=\operatorname{span}\{e_a:4\le a\le(p-1)/2\}.
\]

For each such `a`, define

\[
 f_a=(2a-p)^{-1}e_{p-a}.
\]

Then

\[
 \omega(e_a,f_b)=\delta_{a,b},
\]

so

\[
 \mathcal V_p=L\oplus L^+
\]

is the intrinsic lower/upper Jordan polarization in standard symplectic coordinates.

## 2. Exact block form of the actual Pascal map

Write `D` in the ordered basis `(e_a,f_a)` as

\[
 D=
 \begin{pmatrix}
 A&B\\
 C&E
 \end{pmatrix}.
\]

### Theorem 2.1

One has

\[
 \boxed{
 E=0,
 \qquad
 B\text{ is invertible},
 \qquad
 C=B^{-t},
 \qquad
 B^{-1}A=(B^{-1}A)^t.
 }
\]

Moreover `B` is upper triangular and

\[
 \boxed{
 B_{a,a}=(2a-p)^{-1}.
 }
\]

### Proof

For an upper-row degree `p-a` and upper-column degree `p-b`,

\[
 (p-a)+(p-b)>p
\]

because `a+b\le p-1`. Lucas support for the Pascal matrix therefore gives `E=0`.

For a lower row `a` and upper input `p-b`, the matrix entry is zero exactly when

\[
 a+p-b>p,
\]

that is, when `a>b`. Hence `B` is upper triangular. On the diagonal,

\[
 D_{a,p-a}=(-1)^a\binom{p-1}{a}=1
\]

in `F_p`. The normalization of `f_a` consequently gives

\[
 B_{a,a}=(2a-p)^{-1},
\]

so `B` is invertible.

In standard symplectic coordinates the anti-symplectic identity is

\[
 D^tJD=-J,
 \qquad
 J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}.
\]

Substituting `E=0` gives

\[
 C^tB=I,
 \qquad
 A^tC=C^tA.
\]

Thus

\[
 C=B^{-t}
\]

and

\[
 A^tB^{-t}=B^{-1}A,
\]

which is the asserted symmetry. \(\square\)

## 3. Canonical generating function

Let

\[
 x\in L,
 \qquad
 y\in L
\]

be the input and output lower-polarization coordinates. Since `B` is invertible, the graph of `D` projects isomorphically to `(x,y)`.

Define

\[
 \boxed{
 S_D(x,y)
 =x^tB^{-1}y
 -\frac12x^tB^{-1}Ax.
 }
\]

The symmetry proved above makes this a well-defined quadratic form.

If the input upper coordinate is `u` and the output upper coordinate is `v`, then the graph equations are

\[
 y=Ax+Bu,
 \qquad
 v=Cx=B^{-t}x.
\]

Therefore

\[
 u=B^{-1}(y-Ax),
\]

and differentiation gives

\[
 \frac{\partial S_D}{\partial x}=u,
 \qquad
 \frac{\partial S_D}{\partial y}=v.
\]

Thus `S_D` is the canonical quadratic generating function of the **actual** Pascal Lagrangian graph. No conjugacy to degree reversal is required.

## 4. Exact all-power oscillator normalization

Let `q=p^r` and let `psi_q` be any nontrivial additive character of `F_q`.

### Theorem 4.1

\[
 \boxed{
 \sum_{x,y\in\mathbf F_q^m}
 \psi_q(S_D(x,y))
 =q^m.
 }
\]

After deleting the origin,

\[
 \boxed{
 \sum_{(x,y)\ne(0,0)}
 \psi_q(S_D(x,y))
 =q^m-1.
 }
\]

### Proof

For fixed `x`, the dependence on `y` is the nondegenerate linear character

\[
 y\longmapsto\psi_q(x^tB^{-1}y).
\]

Its sum is zero unless `x=0`, and is `q^m` when `x=0`. At `x=0`, the quadratic term also vanishes. This proves the first identity. The phase at the deleted origin is one, giving the second. \(\square\)

Consequently the punctured actual-Pascal oscillator has virtual Weil class

\[
 \boxed{
 \mathbf Q_\ell(-m)-\mathbf Q_\ell.
 }
\]

There is no quadratic Kummer sign and no unresolved metaplectic orientation. Tensoring with the ambient Airy block gives exactly

\[
 \boxed{
 \mathcal D_p(-m)-\mathcal D_p.
 }
\]

This upgrades the earlier degree-reversal model: the required normalization is now proved for the canonical generating function of the actual Pascal graph itself.

## 5. Classical Morse linearization is impossible

The preceding theorem evaluates the **linear Lagrangian kernel**. It does not identify the actual wild Smith-defect phase with that kernel.

After the first three multiplier/normal levels have been removed, the actual high formal phase has the form

\[
 \Phi_H(\lambda,w;z)
 =
 \sum_{m\in H}\lambda_m z^{-m}
 \sum_{j\in H}
 (-1)^j\binom{m+j-1}{j}s_j(w),
\]

on the associated high block, where

\[
 s_j(w)=\sum_iw_i^j.
\]

Since `j>=4`,

\[
 s_j(w)\in\mathfrak m_w^j\subseteq\mathfrak m_w^4.
\]

Hence

\[
 \boxed{
 \Phi_H\in(\lambda)\mathfrak m_w^4.
 }
\]

All ordinary first and second derivatives of the high phase vanish at the cyclic diagonal. Its ordinary Hessian is zero.

By contrast, the Hessian of `S_D` is nondegenerate because `B` is invertible. Hessian rank and the order of a formal function are preserved by an ordinary formal or etale coordinate change. Therefore:

### Theorem 5.1

\[
 \boxed{
 \text{The actual high wild phase is not ordinarily right-equivalent to }S_D.
 }
\]

In particular, the missing realization cannot be proved by an ordinary formal Morse lemma, a direct Hessian computation, or classical nondegenerate stationary phase on smooth normal coordinates.

The Pascal matrix is the perfect pairing on the **divided-power/Jordan associated graded**, not the ordinary Hessian of the nonlinear phase.

## 6. Exact remaining theorem

The linear and normalization parts of the oscillator programme are now closed. The remaining statement is strictly narrower:

> **Divided-power Rees invariance theorem.** Construct the Rees deformation of the cyclic Jordan/divided-power filtration for the actual wild-infinity Smith-defect phase. Prove that, after the cyclic trivial-minus-nontrivial projector and Airy-isotypic extraction, specialization from the nonlinear phase to the Pascal associated-graded Lagrangian kernel is universally locally acyclic and Frobenius compatible. Identify the complementary specialization cones with the committed q-line, discriminant, Tate, affine, `q=2` and `q=infinity` boundary ledger.

If this theorem holds, Theorem 4.1 supplies the Airy class automatically:

\[
 [\mathcal K_\times]_{\mathcal D_p}
 =\mathcal D_p(-m)-\mathcal D_p.
\]

No further Gauss-sum, sign, symplectic-conjugacy or oscillator-normalization calculation is required.

## 7. Scientific ruling

### Proved here

1. The actual Pascal map has the displayed triangular symplectic block form.
2. Its graph has an explicit canonical quadratic generating function.
3. The complete and punctured sums are exactly `q^m` and `q^m-1` in every extension degree.
4. The actual Pascal oscillator has trivial arithmetic sign.
5. Ordinary quadratic/Morse linearization of the nonlinear wild phase is impossible.

### Closed routes

- replacing the actual Pascal map by degree reversal;
- searching for an integral symplectic conjugacy to that involution;
- recomputing a Weil index or metaplectic sign;
- claiming that the Pascal matrix is the ordinary Hessian;
- applying the ordinary formal Morse lemma.

### Theorem-level obstruction

The sole remaining oscillator-side issue is invariance of the Airy-isotypic cyclic nearby cycles under the divided-power Rees degeneration from the nonlinear modular Jordan phase to its Pascal associated graded.

## 8. Verification

`pascal_actual_oscillator_verify.py` verifies the block theorem for every odd prime through `199`, enumerates the complete oscillator sum at `p=11`, and checks the classical Hessian no-go.