# Cyclic Adams fixed diagonal: uniform A1/A2 singularity theorem

**Date:** 2026-07-23  
**Status:** the fixed-locus algebra, normal expansion, critical parabola and local Milnor numbers are exact for every prime `p>=5`. The cyclic/Thom–Sebastiani localization step that identifies these local germs with the complete primitive local Fourier transform remains to be completed.

## 1. The cyclic root fibre product

Fix `a!=0` and put

`f_(a,c,d)(x)=x^p+a x^3+c x+d.`

Let `Z -> A^2_(c,d)` be the degree-`p` root cover and let

`Z^[p]=Z x_(A^2) ... x_(A^2) Z`

be its `p`-fold fibre product. Write its root coordinates as

`x_0,...,x_(p-1)`.

The cyclic group `C_p=<sigma>` acts by

`sigma(x_i)=x_(i+1)`.

The scheme-theoretic fixed locus is the diagonal

`Delta: x_0=...=x_(p-1)=x`.

This is the geometric cyclic-power model for the Adams operation

`Psi^p(P)=Tr(sigma|P^(tensor p))`

on the root permutation sheaf.

## 2. Exact normal equation

Write a displaced root as `x+h`. In characteristic `p`,

`(x+h)^p=x^p+h^p`.

Therefore

`f(x+h)-f(x)`

`=h^p+(3a x^2+c)h+3a x h^2+a h^3.`

### Theorem CDS.1 — critical parabola

The linear normal map to the cyclic fixed diagonal is multiplication by

`L_(a)(x,c)=3a x^2+c.`

Consequently the diagonal is normally transverse away from the single smooth parabola

`boxed(Gamma_a: c=-3a x^2.)`

No term depending on `p` occurs in this linear normal map.

## 3. Normal germs on the critical parabola

On `Gamma_a`, the normal root-difference germ is

`phi_(a,x)(h)=h^p+3a x h^2+a h^3`

`               =h^2(h^(p-2)+3a x+a h).`

Its derivative is

`phi'_(a,x)(h)=6a x h+3a h^2`

`                 =3a h(2x+h).`

### Theorem CDS.2 — uniform local types

For every prime `p>=5`:

1. if `x!=0`, the factor `h^(p-2)+3a x+a h` is a unit at `h=0`; the germ has tame ramification index `2` and Milnor number

   `mu=dim k[[h]]/(phi')=1`;

2. if `x=0`,

   `phi_(a,0)(h)=h^3(a+h^(p-3))`,

   where the parenthetical factor is a unit; the germ has tame ramification index `3` and Milnor number

   `mu=dim k[[h]]/(3a h^2)=2`.

Thus the complete critical family consists of an `A_1` locus on

`Gamma_a-{(x,c)=(0,0)}`

and one `A_2` cusp at

`(x,c)=(0,0)`.

The degree-`p` term creates no growing local Milnor number.

## 4. Exact formal normal forms

Because `2` and `3` are invertible:

- for `x!=0`, there is a unique formal unit `U(h)` with prescribed constant term such that

  `phi_(a,x)(h)=U(h)^2 h^2`;

- for `x=0`, there is a formal unit `V(h)` such that

  `phi_(a,0)(h)=a(V(h)h)^3`.

The second assertion follows explicitly from

`phi_(a,0)(h)=a h^3(1+a^(-1)h^(p-3))`

and the existence of the formal cube root

`(1+a^(-1)h^(p-3))^(1/3)`.

Hence the normal forms are genuinely independent of `p`, not merely equal in Milnor number.

## 5. Cyclic tensor trace

Let `V` be a finite-dimensional graded Frobenius module. On `V^(tensor p)`, let `sigma` cyclically permute the factors. Then

`boxed(Str(sigma o F^(tensor p)|V^(tensor p))=Str(F^p|V).)`

This is the categorical trace formula defining the `p`-th Adams operation.

Consequently a local vanishing-cycle space of dimension `mu` does not contribute dimension `mu^p` to the cyclic trace. Its cyclic contribution is the Adams transform of the original `mu`-dimensional space. For the two germs above, the local cyclic dimensions are therefore controlled by `1` and `2`, respectively.

This statement is exact linear algebra. Applying it to the geometric cyclic convolution requires the local Thom–Sebastiani and wild fixed-locus comparison described below.

## 6. Fourier-phase restriction

For a nonzero additive Fourier frequency `k` in the coefficient `c`, the Fourier kernel restricts to the critical parabola as

`L_psi(kc)|_(Gamma_a)=L_psi(-3a k x^2).`

Thus the `A_1` locus is governed by a quadratic stationary-phase family, while the only higher critical point is the single `A_2` cusp at `x=0`.

This predicts a bounded local Fourier object assembled from:

- a quadratic/Kummer contribution from the punctured `A_1` parabola;
- at most a rank-two Airy-type contribution from the `A_2` cusp;
- the already explicit Artin–Schreier endpoint and Tate classes.

The observed nonzero Fourier envelope below `4 p^(3/2)` is consistent with two rank-two readings after the square-class/root-negation projector, but this numerical consistency is not used as a proof.

## 7. Remaining bridge theorem

The required geometric statement is now:

### Wild cyclic Thom–Sebastiani localization lemma

After Fourier transform in the `d`-coordinate, identify the cyclic trace on the `p`-fold convolution with the local convolution of the vanishing cycles of `phi_(a,x)`. Then prove that, after subtraction of the explicit Kummer, pair, `D`, Tate and Artin–Schreier classes, the local Fourier transform is exhausted by the `A_1` and `A_2` terms above.

The relevant general tools are:

1. the cyclic description of Adams operations;
2. Fourier–Deligne exchange of tensor product and additive convolution;
3. the Thom–Sebastiani theorem for etale vanishing cycles in characteristic `p`;
4. Laumon's stationary-phase decomposition;
5. the Abbes–Saito/Fu calculation of local Fourier transforms of monomial rank-one pieces.

If the bridge lemma is established without additional wild excess terms, the residual local Fourier rank is bounded absolutely. Laumon's rank formula then gives a uniform bound for

`Swan_infinity(E_a^prim)-rank(E_a^prim)`,

which is the remaining conductor-defect lemma.

## 8. Epistemic classification

### Exact

- cyclic fixed locus is the root diagonal;
- normal expansion;
- critical parabola `c=-3a x^2`;
- `A_1` type and Milnor number `1` away from the origin;
- `A_2` type and Milnor number `2` at the origin;
- formal removal of the `h^p` term from both local types;
- cyclic tensor supertrace identity;
- restriction of the Fourier phase to the critical parabola.

### Open

- wild cyclic fixed-locus/Thom–Sebastiani comparison for the complete sheaf;
- exact identification of the `A_1` and `A_2` terms with the already subtracted extremal ledger;
- absolute conductor-defect bound;
- `N_a=p+O(sqrt p)`;
- function-field `d=1` crown.
