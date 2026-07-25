# The sparse frequency quotient is one symplectic Jordan block

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** refinement of `SPARSE_FREQUENCY_SYMPLECTIC_POLARIZATION_20260725.md`.  
**Status:** **PROVED** for every odd prime `p>=11`.

## 1. Translation is a regular nilpotent action

Let

\[
\mathcal V_p=k[T]_{\le p-4}/k[T]_{\le3}
\]

in characteristic `p`, with basis

\[
e_a=[T^a],
\qquad 4\le a\le p-4.
\]

The infinitesimal translation operator is

\[
D=\frac d{dT}.
\]

On the quotient,

\[
D e_4=0,
\qquad
D e_a=a e_{a-1}\quad(a>4).
\]

Every coefficient `a` is nonzero in `k`. Therefore, after rescaling the basis,

\[
\boxed{
D\text{ is one nilpotent Jordan block of length }p-7.
}
\]

Since `p-7<p`, all factorials through `(p-7)!` are invertible and

\[
\tau_b=\exp(bD)
\]

is exactly the translation action `f(T)->f(T+b)` on `V_p`.

Thus the additive affine subgroup acts through the indecomposable unipotent module

\[
J_{p-7}.
\]

## 2. The Wronskian form is infinitesimally symplectic

Recall

\[
\omega_p(f,g)
=[T^{p-1}](f'g-fg').
\]

Translation invariance implies

\[
\boxed{
\omega_p(Df,g)+\omega_p(f,Dg)=0.
}
\]

Hence

\[
D\in\mathfrak{sp}(\mathcal V_p,\omega_p).
\]

Because `p-7` is even, this is the regular nilpotent orbit in the symplectic Lie algebra of dimension `p-7`.

The canonical Lagrangian

\[
\mathcal L_p
=
\ker D^{(p-7)/2}
=
\operatorname{span}
\{e_4,\ldots,e_{(p-1)/2}\}
\]

is exactly the lower half of the unique Jordan flag. It is therefore intrinsic to the affine translation action, not a coordinate-dependent choice of half the monomials.

## 3. Uniqueness of the affine-conformal alternating form

Let `B` be an alternating bilinear form on `V_p` satisfying:

1. translation invariance;
2. conformal scaling of weight `p`,
   \[
   B(f(aT),g(aT))=a^pB(f,g).
   \]

Scaling characters force

\[
B(e_a,e_b)=0
\qquad\text{unless }a+b=p.
\]

Write

\[
c_a=B(e_a,e_{p-a}).
\]

Infinitesimal translation invariance applied to

\[
e_a,\quad e_{p+1-a}
\]

for `5<=a<=p-4` gives

\[
a c_{a-1}+(p+1-a)c_a=0.
\]

In characteristic `p`, this is

\[
(a-1)c_a=a c_{a-1}.
\]

Therefore

\[
\frac{c_a}{a}=\frac{c_{a-1}}{a-1},
\]

and induction yields

\[
\boxed{
c_a=\kappa a}
\]

for one scalar `kappa`.

The Wronskian form has

\[
\omega_p(e_a,e_{p-a})=2a-p=2a
\]

in characteristic `p`. Thus it is the case `kappa=2`.

Consequently:

\[
\boxed{
\text{Every affine-conformal alternating form on }\mathcal V_p
\text{ is a scalar multiple of }\omega_p.
}
\]

In particular, the symplectic polarization is canonical up to the unavoidable scalar on the one-dimensional value character.

## 4. Relation to the full modular normal block

The full cyclic normal representation at the Smith diagonal is

\[
J_{p-1}=k[\varepsilon]/(\varepsilon^{p-1}).
\]

The cubic multiplier directions remove four levels: the constant direction and the three degrees `1,2,3`. The surviving sparse-frequency quotient is the even block

\[
\boxed{J_{p-7}.}
\]

The half-dimensional Lagrangian is the first half of its monodromy filtration. Therefore the number

\[
\frac{p-7}{2}
\]

appearing in the required Airy Tate twist is simultaneously:

- half the sparse-frequency codimension;
- the dimension of the canonical Lagrangian;
- half the length of the residual symplectic Jordan block;
- the exponent in the punctured-affine factor
  \[
  R\Gamma_c(\mathbf A^{(p-7)/2}\setminus0).
  \]

## 5. Exact remaining lemma

The remaining wild-infinity problem is now a representation-compatible vanishing-cycle statement rather than a search for a cancellation pattern:

> **Symplectic Jordan oscillator lemma.** The Airy-isotypic wild-infinity Smith-defect complex attached to the regular symplectic Jordan block `(V_p,omega_p,D)` is the oscillator complex induced from its intrinsic Lagrangian `L_p`; after deleting the origin its virtual Weil class is
> \[
> \mathcal D_p\otimes R\Gamma_c(\mathcal L_p\setminus0)
> =\mathcal D_p(-(p-7)/2)-\mathcal D_p.
> \]

This lemma is sufficient for the Airy constituent in the global Fourier--Cayley transport. The complementary non-Airy blocks must still be matched to the committed q-line and boundary ledger.

## 6. Scientific status

### Proved

- the frequency translation representation is one Jordan block `J_(p-7)`;
- the Wronskian form makes it a regular symplectic nilpotent module;
- the lower half of the Jordan flag is the intrinsic Lagrangian;
- the affine-conformal symplectic form is unique up to scalar.

### Open

- identification of the integral wild-infinity nearby cycles with the oscillator complex;
- Frobenius normalization of that identification;
- the complementary boundary ledger and final crown.
