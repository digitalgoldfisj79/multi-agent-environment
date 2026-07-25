# The sparse Pascal coefficient--normal block is anti-symplectic

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** associated-graded wild-infinity coefficient--normal pairing after separating the cubic multiplier directions.  
**Status:** **PROVED** for every odd prime `p>=11`.

## 1. Sparse coefficient and normal indices

Put

\[
H=\{4,5,\ldots,p-4\}.
\]

Both the sparse coefficient quotient and the surviving high normal levels have dimension

\[
|H|=p-7.
\]

The Laurent/Pascal expansion at infinity gives the high coefficient--normal matrix

\[
\boxed{
D_{j,m}
=(-1)^j\binom{m+j-1}{j},
\qquad j,m\in H,
}
\]

computed in characteristic `p`.

Lucas' theorem gives

\[
D_{j,m}=0
\qquad\Longleftrightarrow\qquad j+m>p.
\]

On the antidiagonal `j+m=p`,

\[
D_{j,p-j}
=(-1)^j\binom{p-1}{j}=1.
\]

Thus `D` is antitriangular with unit antidiagonal and is invertible.

## 2. The residue symplectic form

On either copy of the high space, use

\[
W_{a,b}
=(a-b)\mathbf1_{a+b=p}.
\]

This is the matrix of the previously proved wild-infinity residue form

\[
\omega_p(f,g)
=[T^{p-1}](f'g-fg')
=
\operatorname{Res}_{z=0}z^p(F\,dG-G\,dF).
\]

## 3. Main theorem

\[
\boxed{
D^tWD=-W.
}
\]

Equivalently,

\[
\boxed{
\omega_p(Dv,Dw)=-\omega_p(v,w).
}
\]

Hence the sparse coefficient--normal Pascal transform is an anti-symplectic isomorphism.

## 4. Proof

For `a,b in H`,

\[
(D^tWD)_{a,b}
=
\sum_{j\in H}
D_{j,a}(2j-p)D_{p-j,b}.
\]

In characteristic `p`, `2j-p=2j`. The two signs multiply to `-1`, so

\[
(D^tWD)_{a,b}
=
-2\sum_j
j\binom{a+j-1}{j}
\binom{b+p-j-1}{p-j}.
\]

The summand is nonzero only when

\[
b\le j\le p-a.
\]

For this range, the negative-binomial congruence gives

\[
\binom{b+p-j-1}{p-j}
\equiv
(-1)^{p-b}\binom{j-1}{b-1}
\pmod p.
\]

Using

\[
j\binom{j-1}{b-1}=b\binom jb
\]

and

\[
\binom{a+j-1}{j}\binom jb
=
\binom{a+b-1}{b}
\binom{a+j-1}{j-b},
\]

one obtains

\[
(D^tWD)_{a,b}
=
-2(-1)^{p-b}b
\binom{a+b-1}{b}
\sum_{r=0}^{p-a-b}
\binom{a+b+r-1}{r}.
\]

The hockey-stick identity gives

\[
\sum_{r=0}^{p-a-b}
\binom{a+b+r-1}{r}
=
\binom p{p-a-b}.
\]

There are three cases.

### `a+b<p`

Then

\[
0<p-a-b<p,
\]

so

\[
\binom p{p-a-b}=0
\quad\text{in }\mathbf F_p.
\]

### `a+b>p`

The summation range is empty.

### `a+b=p`

The final binomial is one and

\[
\binom{p-1}{b}=(-1)^b.
\]

Therefore

\[
(D^tWD)_{a,b}=2b.
\]

But `a=-b` in `F_p`, so

\[
2b=-(a-b)=-W_{a,b}.
\]

This proves the theorem.

## 5. Geometric consequence

The graph

\[
\Gamma_D=\{(v,Dv):v\in\mathcal V_p\}
\]

is Lagrangian in

\[
(\mathcal V_p\oplus\mathcal V_p,\omega_p\oplus\omega_p),
\]

because

\[
(\omega_p\oplus\omega_p)((v,Dv),(w,Dw))
=
\omega_p(v,w)+\omega_p(Dv,Dw)=0.
\]

Thus the exact Pascal expansion already supplies a canonical Lagrangian correspondence between sparse coefficient directions and high wild-normal levels.

This is stronger than the earlier determinant-one statement. It explains why the half-dimensional Fourier normalization is structurally available, but it does not yet identify the integral nearby-cycle complex with the corresponding oscillator kernel.

## 6. Relation to the quadratic candidate

The degree-reversal involution from

`CANONICAL_QUADRATIC_OSCILLATOR_ON_SPARSE_FREQUENCIES_20260725.md`

is one simple anti-symplectic polarization and yields an exactly evaluable quadratic oscillator. The actual Pascal map is the matrix `D` above, not degree reversal. Therefore the quadratic form in that note remains a candidate normal form until one proves an integral symplectic conjugacy or directly computes the wild-infinity Hessian.

No identification of `D` with degree reversal is asserted.

## 7. Exact remaining theorem

The Airy transport problem is reduced further to:

> **Pascal oscillator nearby-cycle lemma.** Show that the cyclic trivial-minus-nontrivial wild-infinity nearby-cycle complex associated to the Lagrangian graph `Gamma_D` is the canonical oscillator kernel of this anti-symplectic correspondence. Compute its Frobenius/Weil index and prove that its punctured Airy-isotypic virtual class is
> \[
> \mathcal D_p(-(p-7)/2)-\mathcal D_p.
> \]

The linear algebra and the Lagrangian correspondence are now proved. The unresolved content is the integral nearby-cycle realization and its Frobenius normalization.

## 8. Verification

`pascal_sparse_antisymplectic_verify.py` checks the identity directly at every odd prime below `200`, including all calibrated half-theorem primes.
