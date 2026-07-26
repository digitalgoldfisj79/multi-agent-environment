# Hayes logarithmic transfer and the fixed-class full-support obstruction

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** orbit-first continuation of the fixed-class Cartier transfer route.  
**Status:** the truncated-log, von Mangoldt and projector statements below are **PROVED**. The group-algebra generating identity is the standard Hayes/Gao--Kuttner--Wang framework. The crown remains **OPEN**.

## 1. Type-II coefficient group at the resonant length

Fix an odd prime `p>=5` and put

\[
\ell=p-2.
\]

For a monic polynomial

\[
f(X)=X^n+f_1X^{n-1}+\cdots,
\]

write its reciprocal leading-coefficient class as

\[
\langle f\rangle_\ell
=
1+f_1z+\cdots+f_\ell z^\ell
\pmod {z^{\ell+1}}.
\]

Multiplication of polynomials induces multiplication in

\[
\mathcal E_\ell
=
1+z\mathbf F_p[z]/(z^{p-1}).
\]

This is the Type-II equivalence group used in the Hayes group-algebra method for prescribed leading coefficients.

Because the ring has characteristic `p`,

\[
(1+u)^p=1+u^p=1
\]

for every `u in z F_p[z]/(z^(p-1))`. Thus `mathcal E_ell` is an elementary abelian `p`-group of order

\[
\boxed{|\mathcal E_\ell|=p^{p-2}.}
\]

## 2. Truncated logarithm

Since every denominator `1,...,p-2` is invertible modulo `p`, the finite series

\[
\log(1+u)
=
\sum_{j=1}^{p-2}\frac{(-1)^{j+1}}j u^j
\]

is defined in the truncated ring.

### Theorem 2.1

The map

\[
\boxed{
\log:\mathcal E_\ell
\longrightarrow
z\mathbf F_p[z]/(z^{p-1})
}
\]

is a group isomorphism from multiplication to addition.

### Proof

The ring is commutative and its augmentation ideal is nilpotent of index below `p`. The usual formal identities

\[
\log(uv)=\log u+\log v,
\qquad
\exp(\log u)=u
\]

therefore truncate before any denominator divisible by `p` occurs. ∎

This gives canonical additive coordinates of dimension `p-2` for the complete coefficient-class group.

## 3. The Fortune plane is the final two logarithmic coordinates

Consider

\[
F_{a,b,c,d}(X)
=X^p+aX^3+bX^2+cX+d.
\]

Its reciprocal class at length `p-2` is

\[
\langle F_{a,b,c,d}\rangle_{p-2}
=1+a z^{p-3}+b z^{p-2}.
\]

The terms involving `c,d` lie beyond the truncation. Moreover, every product of two terms of degree at least `p-3` vanishes modulo `z^(p-1)`. Hence

\[
\boxed{
\log\langle F_{a,b,c,d}\rangle_{p-2}
=a z^{p-3}+b z^{p-2}.
}
\]

Thus the full nonconstant Fortune coefficient pair `(a,b)` is exactly the final two-dimensional additive plane

\[
U=\operatorname{span}\{z^{p-3},z^{p-2}\}
\subset \log\mathcal E_{p-2}.
\]

The depressed cubic line is `b=0`, and a fixed cubic class is one point `a z^(p-3)`.

## 4. Exact von Mangoldt identity

For a class `epsilon in mathcal E_(p-2)`, define

\[
\mathcal M_p(\epsilon)
=
\sum_{\substack{f\text{ monic},\ \deg f=p\\
\langle f\rangle=\epsilon}}
\Lambda(f).
\]

Because `p` is prime, a degree-`p` prime power is either:

1. an irreducible polynomial of degree `p`, with weight `p`; or
2. the `p`-th power of a monic linear polynomial.

In characteristic `p`,

\[
(X-r)^p=X^p-r,
\]

so every linear `p`-th power has identity leading-coefficient class.

### Theorem 4.1

For every nonidentity class `epsilon`,

\[
\boxed{\mathcal M_p(\epsilon)=pI_p(\epsilon),}
\]

where `I_p(epsilon)` is the number of irreducible degree-`p` polynomials in that class.

For the identity class,

\[
\boxed{\mathcal M_p(1)=pI_p(1)+p.}
\]

The identity class in the Fortune plane consists of

\[
X^p+cX+d.
\]

If `c!=-1`, this polynomial has the `F_p`-root `-d/(1+c)`. If `c=-1` and `d!=0`, a root `alpha` satisfies

\[
\alpha^{p^j}=\alpha-jd,
\]

so its first Frobenius return is `j=p`; the polynomial is irreducible. Therefore

\[
\boxed{I_p(1)=p-1.}
\]

This is the known excluded Artin--Schreier line.

## 5. Exact character formula

Let `widehat(mathcal E_ell)` be the character group. For a character `lambda`, put

\[
L_\lambda(z)
=
\sum_{f\text{ monic}}
\lambda(\langle f\rangle)z^{\deg f}
\]

and

\[
m_p(\lambda)=p[z^p]\log L_\lambda(z).
\]

For the trivial character,

\[
L_0(z)=(1-pz)^{-1},
\qquad
m_p(0)=p^p.
\]

The Euler product and character orthogonality give the standard exact Hayes formula

\[
\boxed{
\mathcal M_p(\epsilon)
=
\frac1{p^{p-2}}
\sum_{\lambda\in\widehat{\mathcal E}_{p-2}}
\lambda(\epsilon)^{-1}m_p(\lambda).
}
\]

Using the logarithmic coordinates, write a character as

\[
\lambda=(\lambda_1,\ldots,\lambda_{p-2})
\in\mathbf F_p^{p-2},
\]

with evaluation through a fixed additive character `psi`. On the Fortune plane,

\[
\lambda(\epsilon_{a,b})
=
\psi(\lambda_{p-3}a+\lambda_{p-2}b).
\]

This is an exact orbit-first transfer: coefficient classes are summed before any Frobenius state is constructed.

## 6. Fixed-class full-support theorem

The point mass at a fixed class has nonzero Fourier coefficient at every character. The sparse target point therefore does **not** yield sparse dual support.

The same remains true after selecting either cubic square class.

Let `chi` be the quadratic character and let `A in {+1,-1}`. The projector onto cubic coefficients of square class `A` has top-coordinate Fourier weight

\[
W_A(t)
=
\frac12
\sum_{a\ne0}(1+A\chi(a))\psi(-ta).
\]

If `t=0`, then

\[
W_A(0)=\frac{p-1}{2}.
\]

If `t!=0`, then

\[
W_A(t)
=
\frac12\left(-1+A\chi(-t)G(\chi)\right).
\]

This cannot vanish: vanishing would force the quadratic Gauss sum to be `+1` or `-1`, whereas

\[
G(\chi)^2=\chi(-1)p.
\]

### Theorem 6.1

For either fixed cubic square class, the Hayes projector has structural support on **all**

\[
\boxed{p^{p-2}}
\]

characters of `mathcal E_(p-2)`.

The separate trivial and quadratic `a`-averages have support sizes

\[
\boxed{p^{p-2}}
\]

and

\[
\boxed{(p-1)p^{p-3}}
\]

respectively. In particular, square-class averaging does not produce a bounded, polynomial-size or lower-dimensional character family.

This is a projector-support theorem. It does not assert that every individual coefficient `m_p(lambda)` is nonzero; it proves that no character is removed merely by the sparsity or square-class symmetry of the fixed-class target.

## 7. The only orthogonality reduction is the aggregate plane

Summing over the complete plane `U` gives

\[
\sum_{a,b\in\mathbf F_p}
\psi(-\lambda_{p-3}a-\lambda_{p-2}b)
=
\begin{cases}
p^2,&\lambda_{p-3}=\lambda_{p-2}=0,\\
0,&\text{otherwise}.
\end{cases}
\]

Thus exactly the annihilator

\[
U^\perp
\cong\mathbf F_p^{p-4}
\]

survives, containing

\[
\boxed{p^{p-4}}
\]

characters.

Let `I_4` be the number of irreducibles in the complete four-parameter Fortune interval. Summing Theorem 4.1 over the plane gives

\[
\sum_{a,b,c,d}\Lambda(F_{a,b,c,d})
=pI_4+p.
\]

The character formula becomes

\[
\boxed{
pI_4+p
=p^4
+p^{4-p}
\sum_{\substack{\lambda\in U^\perp\\\lambda\ne0}}
m_p(\lambda).
}
\]

The main term `p^4` is the trivial character. Since the identity class contains exactly `p-1` irreducibles, the nonconstant Fortune crown is

\[
\boxed{I_4>p-1.}
\]

Therefore complete-plane averaging is exactly the already-isolated aggregate `p`-cycle/full-interval route. It changes coordinates but does not make the crown inequality smaller.

If one instead sums only over the nonzero plane `U\setminus{0}`, the Fourier coefficient equals `p^2-1` on `U^perp` and `-1` outside it; all characters return. Subtracting the excluded identity class therefore destroys the orthogonality compression unless the known `p-1` contribution is kept separately, which is precisely the aggregate formulation above.

## 8. Ruling on the corrected transfer route

The two natural transfer orders are now exhausted:

1. **Transfer first, then sum.** The generic tail is a primitive degree-`p` generator, so no nontrivial linear state quotient exists.
2. **Sum coefficient orbits first, then transfer.** A fixed class or fixed square class has full Hayes character support. The only exact dimensional reduction is complete-plane averaging, which is the aggregate full-interval crown already proved circular under the `p`-cycle fixed-point identity.

Thus a corrected fixed-class Cartier transfer cannot arise merely from:

- the sparse three-term tail;
- a smaller Krylov realization;
- truncated-log sparsity of the target class;
- trivial or quadratic averaging in `a`;
- ordinary character orthogonality.

A genuine advance would require a new identity among the nontrivial `m_p(lambda)`, not another transfer representation.

## 9. Verification and literature

`hayes_logarithmic_transfer_verify.py` performs no irreducible-polynomial census. At `p=5,7,11` it checks:

- exponent `p` of the truncated-unit group;
- the logarithmic homomorphism;
- exact placement of `(a,b)` in the final two log coordinates;
- additive-character orthogonality on the full plane;
- the stated structural support counts.

Frozen output:

`hayes_logarithmic_transfer_results_20260726.json`.

The group-algebra generating framework is from:

Z. Gao, S. Kuttner and Q. Wang, *Counting irreducible polynomials with prescribed coefficients over a finite field*, arXiv:2109.02000 (2021), especially the Type-II equivalence group, character-idempotent decomposition and logarithmic generating formula.
