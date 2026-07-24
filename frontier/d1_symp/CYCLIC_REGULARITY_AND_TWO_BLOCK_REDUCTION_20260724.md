# Cyclic regularity and the exact two-block reduction

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling only.  
**Status:** all statements labelled **PROVED** below are exact. The absolute Frobenius trace bound remains **OPEN**.

## 0. Main theorem

Let

\[
X_p=X_p^{\mathrm{perm}}
=
\left\{
\sum_i x_i=\sum_i x_i^2=\sum_i x_i^3=0
\right\}
\bigg/
\overline{\mathbf F}_p(1,\ldots,1)
\]

be the smooth `(2,3)` complete intersection of dimension

\[
m=p-5
\]

and let

\[
H_p=H^{p-5}_{\mathrm{prim}}
(X_{p,\overline{\mathbf F}_p},\mathbf Q_\ell).
\]

Let `sigma=(0 1 ... p-1)` be the cyclic coordinate shift and

\[
C_p=\langle\sigma\rangle.
\]

Then

\[
\boxed{
H_p\big|_{C_p}
\cong
\mathbf Q_\ell[C_p]^{\oplus q_p},
\qquad
q_p=\frac{2^{p-1}-1}{3p}.
}
\]

In particular,

\[
\boxed{
\operatorname{Tr}(\sigma^a\mid H_p)=0
\qquad(1\le a\le p-1).
}
\]

Let

\[
N_p=C_p\rtimes\mathbf F_p^*
\subset S_p
\]

be the affine normalizer of the `p`-cycle, and let `rho_p` be its unique irreducible representation of dimension `p-1`, induced from any nontrivial character of `C_p`. Then there are Frobenius-stable multiplicity spaces `M_{0,p}` and `M_{1,p}`, both of dimension `q_p`, such that

\[
\boxed{
H_p
\cong
M_{0,p}\oplus(\rho_p\otimes M_{1,p})
}
\]

as a representation of `N_p` commuting with geometric Frobenius. Here

\[
M_{0,p}=H_p^{C_p},
\qquad
M_{1,p}=\operatorname{Hom}_{N_p}(\rho_p,H_p).
\]

Consequently, for every `r>=1` and every `a!=0 mod p`,

\[
\boxed{
\operatorname{Tr}
(\sigma^aF^r\mid H_p)
=
\operatorname{Tr}(F^r\mid M_{0,p})
-
\operatorname{Tr}(F^r\mid M_{1,p}).
}
\]

Define the rank-zero virtual Weil module

\[
\mathcal D_p=M_{0,p}-M_{1,p}.
\]

The remaining analytic target is exactly

\[
\boxed{
|\operatorname{Tr}(F\mid\mathcal D_p)|
\le C p^{(p-5)/2}.
}
\]

Thus the cyclic geometry reduces the target from one exponentially large actual cohomology group to a difference of two equal-rank Frobenius multiplicity spaces. It does not yet bound that difference.

## 1. The fixed schemes of all nontrivial powers coincide

The projective fixed scheme of `sigma` on `X_p` was computed in
`COMPLETED_FIXED_SCHEME_AND_CORRESPONDENCE_CORRECTION.md`:

\[
\widehat{\mathcal O}_{\operatorname{Fix}(\sigma,X_p),[v]}
\cong
\overline{\mathbf F}_p[[t]]/(t^{p-4}).
\]

It is supported at the unique point represented by

\[
v=(0,1,2,\ldots,p-1).
\]

For `1<=a<=p-1`, in the group algebra of `C_p`,

\[
\sigma^a-1
=(\sigma-1)u_a(\sigma),
\qquad
u_a(T)=1+T+\cdots+T^{a-1}.
\]

Since

\[
u_a(1)=a\ne0
\]

and `sigma-1` is nilpotent in characteristic `p`, `u_a(sigma)` is a unit. Hence the images of `sigma^a-1` and `sigma-1` on every local coordinate module coincide. Therefore

\[
\boxed{
\operatorname{Fix}(\sigma^a,X_p)
=
\operatorname{Fix}(\sigma,X_p)
}
\]

scheme-theoretically for every nontrivial power.

## 2. Graph--diagonal intersection

The variety `X_p` is smooth projective of dimension `m=p-5`. The graph

\[
\Gamma_{\sigma^a}
\]

and diagonal

\[
\Delta_{X_p}
\]

are both regular embeddings of codimension `m` in the smooth `2m`-dimensional variety `X_p\times X_p`. Their intersection is the zero-dimensional fixed scheme above, so the intersection is proper.

Locally, the combined defining equations form a system of parameters in a regular local ring. A system of parameters in a Cohen--Macaulay local ring is a regular sequence. Thus the local intersection multiplicity is the length of the fixed local ring:

\[
\Gamma_{\sigma^a}\cdot\Delta_{X_p}
=
\operatorname{length}\operatorname{Fix}(\sigma^a,X_p)
=p-4.
\]

The Weil-cohomology Lefschetz formula for a smooth projective variety identifies this graph--diagonal intersection number with the alternating cohomological trace. Hence

\[
\boxed{
\sum_i(-1)^i\operatorname{Tr}
(\sigma^a\mid H^i(X_p))
=p-4.
}
\]

This use of the graph--diagonal intersection is valid for the wild automorphism itself; it does not replace the distinct arithmetic correspondence `sigma Frob` by the bare shift.

## 3. Primitive trace vanishing

Weak Lefschetz and Poincare duality give the projective-space cohomology outside degree `m`. Since `m=p-5` is even, the ambient classes occur in the even degrees

\[
0,2,\ldots,2m
\]

and contribute

\[
m+1=p-4
\]

to the Lefschetz number. The coordinate permutation preserves the hyperplane class, so it acts trivially on every ambient Tate line.

The only remaining summand is the primitive middle cohomology, also in even degree. Therefore

\[
p-4
=
(p-4)+\operatorname{Tr}(\sigma^a\mid H_p),
\]

and

\[
\boxed{
\operatorname{Tr}(\sigma^a\mid H_p)=0
\quad(a\ne0).
}
\]

## 4. Regularity as a `C_p`-module

The exact primitive rank is

\[
\dim H_p=\frac{2^{p-1}-1}{3}.
\]

Fermat's congruence gives

\[
p\mid 2^{p-1}-1,
\]

so

\[
q_p=\frac{2^{p-1}-1}{3p}
\]

is an integer for every prime `p=2 mod 3`.

Over a characteristic-zero coefficient field, representations of `C_p` are semisimple. The character of `H_p` is

\[
\chi_{H_p}(1)=pq_p,
\qquad
\chi_{H_p}(\sigma^a)=0\quad(a\ne0).
\]

This is exactly `q_p` times the regular character. Therefore

\[
H_p|_{C_p}\cong\mathbf Q_\ell[C_p]^{\oplus q_p}.
\]

Every character of `C_p`, including the trivial character, consequently occurs with the same multiplicity `q_p`.

## 5. The affine normalizer and two multiplicity spaces

The full symmetric group `S_p` acts on `X_p`; in particular the affine normalizer

\[
N_p=\operatorname{AGL}_1(\mathbf F_p)
=C_p\rtimes\mathbf F_p^*
\]

acts. Its complement `F_p^*` acts transitively on the nontrivial characters of `C_p`.

The irreducible characteristic-zero representations of `N_p` are:

1. one-dimensional representations inflated from `N_p/C_p=F_p^*`;
2. one irreducible representation `rho_p` of dimension `p-1`, induced from any nontrivial character of `C_p`.

The restriction of `rho_p` to `C_p` is the direct sum of every nontrivial character once, and

\[
\operatorname{Tr}(\sigma^a\mid\rho_p)=-1
\qquad(a\ne0).
\]

Since `H_p|_{C_p}` is `q_p` copies of the regular representation, the nontrivial character sector is exactly `q_p` copies of `rho_p`. The remaining `q_p` dimensions are the invariant sector. This proves

\[
H_p\cong M_{0,p}\oplus(\rho_p\otimes M_{1,p}),
\qquad
\dim M_{0,p}=\dim M_{1,p}=q_p.
\]

All coordinate permutations are defined over `F_p`, so geometric Frobenius commutes with `N_p` and preserves this decomposition.

## 6. Exact trace reduction

For `a!=0 mod p`, `sigma^a` acts trivially on `M_{0,p}` and has trace `-1` on `rho_p`. Hence

\[
\operatorname{Tr}(\sigma^aF^r\mid H_p)
=
\operatorname{Tr}(F^r\mid M_{0,p})
-
\operatorname{Tr}(F^r\mid M_{1,p}).
\]

Under the twisted descent theorem,

\[
T_p=p^2\operatorname{Tr}(\sigma^{\pm1}F\mid H_p),
\]

so

\[
\boxed{
T_p
=p^2\operatorname{Tr}(F\mid\mathcal D_p).
}
\]

The target

\[
|T_p|\le C p^{(p-1)/2}
\]

is therefore exactly equivalent to

\[
|\operatorname{Tr}(F\mid\mathcal D_p)|
\le C p^{(p-5)/2}.
\]

## 7. What this changes

### PROVED

- every nontrivial cyclic power has the same curvilinear fixed scheme;
- the graph--diagonal intersection number is exactly `p-4`;
- the cyclic shift has zero trace on primitive cohomology;
- the primitive cohomology is a multiple of the regular `C_p` representation;
- the cyclic-Frobenius trace is the difference of two equal-rank Frobenius multiplicity traces.

### NOT PROVED

- an isomorphism between `M_{0,p}` and `M_{1,p}`;
- a bounded-rank cone between them;
- the absolute trace bound.

The next admissible analytic step is to identify the virtual difference

\[
\mathcal D_p=M_{0,p}-M_{1,p}
\]

with the already isolated Airy cross-symmetric-power virtual module, including its Tate normalization and the even-power/projector defect.

## 8. Verification

`cyclic_regularity_verify.py` checks:

- integrality of `q_p` and the regular-character identities for odd primes through `p=199`;
- direct enumeration of the six geometric points of `X_5` over `F_5`;
- the unique fixed point of every nontrivial power of the 5-cycle;
- primitive trace zero in the `p=5` permutation model.

The script is a regression check. The general proof is the intersection-theoretic argument above.
