# Global integral Fourier elimination to the cubic-tail complex

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** characteristic-zero Fourier side of the Smith-defect master object.  
**Status:** the integral Fourier-delta identity, Frobenius compatibility, cyclic-character compatibility and residual cubic-tail trace formula below are **PROVED**. They do not by themselves prove the Airy absolute bound.

## 1. Setup

Put

\[
n=p-4,
\qquad
X=(\mathbf A^1)^p,
\qquad
A=\mathbf A^n_a,
\]

and let `C_p=<sigma>` cyclically permute the `p` factors of `X`. For

\[
1\le m\le n
\]

write

\[
s_m(x)=\sum_{i=1}^p x_i^m,
\qquad
S=(s_1,\ldots,s_n):X\longrightarrow\mathbf A^n.
\]

Let `ell != p`, let `O` be the ring of integers of a finite extension of `Q_ell` containing the values of a nontrivial additive character of `F_p`, and put on `X x A`

\[
\mathcal L
=
\mathcal L_\psi\!\left(\sum_{m=1}^{n}a_ms_m(x)\right).
\]

Let

\[
\pi:X\times A\longrightarrow X
\]

be projection and let

\[
i:Z=S^{-1}(0)\hookrightarrow X.
\]

All constructions are defined over `F_p`, are `S_p`-equivariant, and carry their natural Frobenius structures.

## 2. Exact integral Fourier elimination

### Theorem 2.1

There is a canonical isomorphism in the integral `ell`-adic derived category

\[
\boxed{
R\pi_!\mathcal L
\cong
i_!\mathcal O(-n)[-2n].
}
\]

### Proof

At a geometric point `x` of `X`, the stalk is

\[
R\Gamma_c\!\left(
\mathbf A^n_a,
\mathcal L_\psi(\langle a,S(x)\rangle)
\right).
\]

If `S(x) != 0`, one coefficient direction carries a nontrivial additive linear character. Compactly supported cohomology in that direction vanishes, and hence the whole stalk vanishes.

If `S(x)=0`, the sheaf is constant and

\[
R\Gamma_c(\mathbf A^n,\mathcal O)
\cong
\mathcal O(-n)[-2n].
\]

These stalk identifications are canonical and compatible with specialization, so they glue to the displayed isomorphism. The calculation is integral because the Artin--Schreier character takes values in units of `O`. It is Frobenius-compatible because the pairing and the zero section are defined over `F_p`. \(\square\)

## 3. The nonsplit Jordan extensions cannot add another term

The formal normal representation of the cyclic diagonal is a nonsplit Jordan block in base characteristic `p`. The Pascal calculation identifies a unimodular pairing only on its associated graded. The theorem above is stronger than an associated-graded calculation:

- it is performed on the full global phase before choosing a splitting of the Jordan filtration;
- it gives the derived pushforward itself, not merely its graded Euler class;
- every extension between Jordan levels is already present in `L` and is carried through the canonical stalk computation;
- no extension class can create an additional summand because every stalk off `Z` is zero and every stalk on `Z` is the single forced Tate complex.

Thus the first `p-4` coefficient/normal pairs contribute exactly

\[
\boxed{\mathcal O(-(p-4))[-2(p-4)]}
\]

and nothing else on the characteristic-zero Fourier side.

This proves clean Fourier elimination without asserting a nonexistent equivariant splitting of the modular normal block.

## 4. Compatibility with the cyclic hook difference

Since `ell != p`, the integer `p` is a unit in `O`. The idempotents for the trivial character and any nontrivial character `xi` of `C_p` therefore exist integrally after adjoining the required roots of unity. Consequently the functors

\[
K\longmapsto K^{C_p},
\qquad
K\longmapsto K_\xi
\]

are exact direct-summand functors and commute with `R pi_!`, compact support and Frobenius.

Using

\[
\Lambda_p
=
\operatorname{Ind}_{C_p}^{S_p}{\bf1}
-
\operatorname{Ind}_{C_p}^{S_p}\xi,
\]

one obtains

\[
\boxed{
\operatorname{HookAlt}(R\pi_!\mathcal L)
\cong
\operatorname{HookAlt}(i_!\mathcal O)(-n)[-2n].
}
\]

Hence the characteristic-zero cyclic trivial-minus-nontrivial trace also passes through the elimination with only the forced Tate shift.

## 5. Exact trace formula in every extension degree

Let `q=p^r`, put `L=F_(q^p)`, and for

\[
a=(a_1,\ldots,a_n)\in F_q^n
\]

write

\[
f_a(T)=\sum_{m=1}^{n}a_mT^m.
\]

Recall

\[
\operatorname{Def}_q(f_a)
=
\sum_{\alpha\in L}
\psi_q\!\left(
\operatorname{Tr}_{L/F_q}(f_a(\alpha))
\right)-q.
\]

### Theorem 5.1

For every `r>=1`,

\[
\boxed{
q^{-n}\sum_{a\in F_q^n}\operatorname{Def}_q(f_a)
=
\#\left\{
\alpha\in L:
\operatorname{Tr}(\alpha^m)=0
\text{ for }1\le m\le p-4
\right\}-q.
}
\]

### Proof

Interchange the two finite sums. For fixed `alpha`, additive orthogonality gives

\[
q^{-n}\sum_{a\in F_q^n}
\psi_q\!\left(
\sum_{m=1}^{n}a_m\operatorname{Tr}(\alpha^m)
\right)
=
\prod_{m=1}^{n}
{\bf1}_{\operatorname{Tr}(\alpha^m)=0}.
\]

The average of the constant Smith-diagonal subtraction `-q` is still `-q`. \(\square\)

This is the Frobenius trace of Theorem 2.1 and holds simultaneously at every Frobenius power.

## 6. Exact reduction to the cubic-tail root cover

For an element `alpha` of degree `p` over `F_q`, its conjugates are the roots of its monic minimal polynomial. Their power sums are

\[
\operatorname{Tr}(\alpha^m).
\]

Newton identities, with `1,...,p-4` invertible, give

\[
\operatorname{Tr}(\alpha^m)=0
\quad(1\le m\le p-4)
\]

if and only if the first `p-4` elementary symmetric coefficients vanish. Hence the minimal polynomial has the form

\[
\boxed{
T^p+AT^3+BT^2+CT+D.
}
\]

Every element of `F_q` satisfies all trace equations because the relative trace multiplies by `p=0`; these are exactly the `q` elements removed by the Smith-diagonal term. Since `p` is prime, all remaining elements have degree `p`, and every irreducible polynomial contributes its `p` conjugate roots. Therefore

\[
\boxed{
q^{-n}\sum_{a\in F_q^n}\operatorname{Def}_q(f_a)
=
p\,N_{\mathrm{cubic}}(q),
}
\]

where `N_cubic(q)` is the number of irreducible polynomials

\[
T^p+AT^3+BT^2+CT+D
\]

with coefficients in `F_q`.

At the sheaf level, the residual object is consequently the alternating-hook complex of the finite-flat cubic-tail ordered-root cover. On its separable open this is the exact `S_p`-torsor already proved in `SPARSE_ROOT_COVER_FINITE_FLAT_OVER_CUBIC_TAIL_20260725.md`. The normal-form `q`-line, `q=2`, `q=infinity`, discriminant, translation, scaling and punctual pieces are its established open-chart and boundary decomposition.

## 7. What this proves and what it does not

### PROVED

1. Clean integral `ell`-adic Fourier elimination of all first `p-4` coefficient directions.
2. The sole contribution of those directions is the forced Tate shift and even cohomological shift.
3. The statement is on the full complex and therefore controls all nonsplit Jordan extension data on the characteristic-zero Fourier side.
4. Frobenius and cyclic-character projectors commute with the elimination.
5. The averaged characteristic-zero Smith defect is exactly the residual cubic-tail/q-line root complex in every extension degree.

### NOT PROVED BY THIS THEOREM

1. A modular residue-characteristic-`p` Smith comparison in the same coefficient category.
2. A bound for the single degree-drop fibre at the cubic origin.
3. An absolute bound for
   \[
   \operatorname{Tr}(F|R_p).
   \]

Global coefficient averaging proves the application-side reduction. The analytic Airy trace is a distinguished residual fibre, not the total coefficient average. Controlling that fibre requires an additional characteristic-zero Frobenius theorem on the residual complex.
