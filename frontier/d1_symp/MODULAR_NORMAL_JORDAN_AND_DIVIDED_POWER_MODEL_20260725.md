# Modular normal Jordan block and the divided-power local model

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** local geometry of the Smith-defect master object.  
**Status:** the normal-representation and Hasse-expansion statements are **PROVED**. The resulting integral vanishing-cycle calculation is **OPEN**.

## 1. The cyclic diagonal does not split in characteristic `p`

Let `k` be a field of characteristic `p`, let

\[
W=k^p
\]

with `C_p=<sigma>` acting by cyclic permutation, and let `D` be the fixed diagonal line.

Identify the regular representation with

\[
k[C_p]\cong k[\varepsilon]/(\varepsilon^p),
\qquad
\sigma=1+\varepsilon.
\]

The fixed line is the socle

\[
D=k\varepsilon^{p-1}.
\]

### Theorem 1.1

The normal representation

\[
N=W/D
\]

is the indecomposable Jordan module

\[
\boxed{
N\cong k[\varepsilon]/(\varepsilon^{p-1}).
}
\]

Thus `sigma-1` is one nilpotent Jordan block of length `p-1`. In particular, the exact sequence

\[
0\to D\to W\to N\to0
\]

has no `C_p`-equivariant splitting.

This is the normal representation to the fixed diagonal in `(A^1)^p` and also at the diagonal point at infinity in `(P^1)^p`.

## 2. Exact Tate cohomology of the normal block

In characteristic `p`, the group norm is

\[
1+\sigma+\cdots+\sigma^{p-1}
=(\sigma-1)^{p-1}
=\varepsilon^{p-1}.
\]

It vanishes on `N`. Therefore

\[
\widehat H^0(C_p,N)
=\ker(\varepsilon:N\to N),
\]

and

\[
\widehat H^{-1}(C_p,N)
=N/\varepsilon N.
\]

Both are one-dimensional. By periodicity,

\[
\boxed{
\dim_k\widehat H^n(C_p,N)=1
\quad\text{for every }n.
}
\]

The cyclic diagonal consequently carries one universal Tate line in each parity. This is compatible with, but does not by itself identify, Chuang's single arithmetic Picard--Lefschetz correction line in the cubic invariant sector.

## 3. Canonical divided-power flag

The Jordan module has a unique `C_p`-stable filtration

\[
0\subset\varepsilon^{p-2}N\subset\cdots
\subset\varepsilon N\subset N.
\]

Every successive quotient is a one-dimensional trivial representation. There is no semisimple normal-coordinate decomposition; the correct local replacement is this `epsilon`-adic divided-power flag.

Any characteristic-`p` Fourier--secant or stationary-phase theorem at the Smith diagonal must be formulated relative to this filtration. A proof that diagonalizes the cyclic normal action into nontrivial characters is invalid in the load-bearing characteristic.

## 4. Exact phase expansion along the diagonal

Let `f in k[T]` have degree `d<p`. Write a formal point near the diagonal as

\[
x_i=t+y_i.
\]

Using Hasse derivatives,

\[
f(t+y)=\sum_{j=0}^{d} f^{[j]}(t)y^j.
\]

Summing over the `p` factors and using `p f(t)=0` gives the exact identity

\[
\boxed{
\sum_{i=1}^{p}f(t+y_i)
=
\sum_{j=1}^{d}f^{[j]}(t)
\left(\sum_{i=1}^{p}y_i^j\right).
}
\]

Since `d<p`, every factorial `j!` is invertible and the Hasse derivatives agree with ordinary derivatives divided by `j!`. No hidden `p`-th divided-power term occurs.

For the sparse generalized Airy phase

\[
f_{\lambda,u}(T)
=P_\lambda(T)+u_1T+u_2T^2+u_3T^3,
\]

the local coefficients are therefore the explicit Hasse derivatives of this polynomial, and the normal invariants are exactly the power sums

\[
s_j(y)=\sum_i y_i^j.
\]

This explains why the same power-sum system appears in the sparse root geometry and in the Smith diagonal expansion.

## 5. Consequences for the master defect

The local structure now has no unspecified representation-theoretic component:

1. the fixed locus is the diagonal;
2. its normal representation is the single module `J_(p-1)`;
3. the Tate contribution is one line per parity;
4. the phase on the formal normal space is the displayed Hasse/power-sum polynomial;
5. the only unresolved operation is the integral vanishing-cycle calculation along the canonical Jordan filtration, especially at infinity where the polynomial degree drops.

This also explains the failure of direct tame transference. Dobrovolska-type secant support uses semisimple characteristic-zero normal geometry. Here the normal bundle is maximally nonsemisimple and the Fourier phase must be analysed by divided powers.

## 6. Exact next local theorem

On the formal completion of `(P^1)^p` along the cyclic diagonal at infinity:

1. express the Laurent phase of `f_(lambda,u)` in the `epsilon`-adic flag of `J_(p-1)`;
2. construct the integral Artin--Schreier/Dwork vanishing-cycle complex of each graded step;
3. prove that the sole cubic boundary correction is Chuang's Tate line plus the Airy pair `R_p((p-1)/2)`;
4. prove that higher-degree steps either cancel in the cyclic-character difference or map to the explicit q-line ledger.

This is the local form of the uniform integral Smith-defect theorem.

## 7. Ruling

### PROVED

- the cyclic normal representation is one Jordan block of length `p-1`;
- it has one Tate line in every parity;
- it has a canonical one-dimensional divided-power flag;
- the phase expansion is exactly the Hasse-derivative/power-sum expansion.

### OPEN

- integral vanishing cycles along this flag at infinity;
- cancellation or transport of the higher-degree graded pieces;
- the crown.

The normal geometry is now explicit. The remaining wall is a calculation in this universal modular Jordan model, not a search for another representation.
