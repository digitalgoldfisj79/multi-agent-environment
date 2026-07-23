# Discriminant Fourier phase collapses to a fixed cubic

**Date:** 2026-07-23  
**Status:** exact discriminant parametrization and exact Artin–Schreier/Frobenius reduction for every prime `p>=5`. The two-dimensional Fourier transform of the normalized discriminant branch has fixed cubic complexity and generic rank two. Connecting its multiplicity to the complete cyclic Adams characteristic cycle remains part of the bridge lemma.

## 1. Discriminant parametrization

For

`f_(a,c,d)(X)=X^p+aX^3+cX+d`,

a repeated root `x` satisfies

`f'(x)=3a x^2+c=0`.

Hence

`c=-3a x^2`.

Substituting in `f(x)=0` gives

`d=-x^p-a x^3-cx`

`  =-x^p+2a x^3.`

### Theorem DCA.1 — normalized discriminant branch

The normalization of the finite discriminant is the affine `x`-line with map

`boxed(delta_a(x)=(-3a x^2,-x^p+2a x^3).)`

Root negation `x -> -x` fixes `c` and sends `d -> -d`, as required by the exact quadratic descent.

## 2. Square-value discriminant

Putting `Y=x^2` and `e=d^2` gives

`e=Y(Y^m-2aY)^2`,  `m=(p-1)/2`.

Equivalently,

`e=Y^p-4aY^(m+2)+4a^2Y^3.`

The square root is the odd polynomial

`d=-(x^p-2a x^3).`

The derivative of the square-value map is

`d/dY [Y(Y^m-2aY)^2]`

`=-6aY(Y^m-2aY),`

so every finite critical point maps to `e=0`. This recovers the exact two-branch-value geometry of the normal form.

## 3. Two-dimensional Fourier phase

Let `(kappa,lambda)` be dual coordinates to `(c,d)`. Pulling the Fourier kernel back along `delta_a` gives the rank-one Artin–Schreier phase

`Phi_(a,kappa,lambda)(x)`

`=-3a kappa x^2+lambda(-x^p+2a x^3).`

Over the perfection of the dual parameter space, choose `mu` with

`mu^p=lambda`.

For every function `g`, the Artin–Schreier sheaves satisfy

`L_psi(g^p) isomorphic to L_psi(g)`,

because `g^p-g` is an Artin–Schreier coboundary. Therefore

`L_psi(-lambda x^p)`

`=L_psi(-(mu x)^p)`

`isomorphic to L_psi(-mu x)`.

### Theorem DCA.2 — cubic phase collapse

After the universal purely inseparable change `lambda=mu^p`,

`boxed(L_psi(Phi_(a,kappa,lambda)(x))`

` isomorphic to`

` L_psi(2a lambda x^3-3a kappa x^2-mu x).)`

The right side has degree at most three in `x`, independently of `p`.

## 4. Fourier ranks

### 4.1 Generic dual d-frequency

For `lambda!=0`, the cubic coefficient `2a lambda` is nonzero. The compactly supported Fourier integral in `x` is the standard cubic Airy construction. Its geometrically generic rank is

`degree-1=2`.

All local complexity is fixed: two critical points counted with multiplicity, one wild slope `3/2` after the standard Airy normalization.

### 4.2 The c-pencil slice

For `lambda=0` and `kappa!=0`, the phase is

`-3a kappa x^2`.

This is a quadratic Gauss/Kummer object of rank one. It is precisely the Fourier image of the critical double cover

`c=-3a x^2`

identified in `CRITICAL_PARABOLA_KUMMER_DECOMPOSITION.md`.

At `(kappa,lambda)=(0,0)` one obtains only the constant/main contribution.

## 5. Microlocal consequence

The normalized finite discriminant is not a degree-growing Fourier object. Its complete dual behavior is:

- rank two on the generic two-dimensional Fourier locus `lambda!=0`;
- rank one on the nonzero `c`-pencil slice `lambda=0,kappa!=0`;
- constant/Tate at the origin.

Thus any characteristic-cycle component carried by the discriminant normalization has uniformly bounded Fourier multiplicity. The degree `p` term is a Frobenius coboundary in the Fourier phase and contributes no new stationary points.

## 6. Relation to the rank-four bridge

The Adams defect vanishes on the generic transposition stratum of the discriminant, so the rank-one quadratic slice is already removed as main/Kummer. The only finite primitive correction is the `A_2` collision at the ramification point of the quadratic projection, with effective Adams dimension at most four.

The theorem supplies a second route to the same fixed-complexity conclusion:

1. the full discriminant Fourier geometry has rank at most two;
2. the c-pencil restriction is exactly the known Kummer term;
3. the residual punctual Adams difference has effective dimension at most four.

What remains is to identify the wild specialization cone at the weighted Artin–Schreier corner with these microlocal pieces plus the already explicit AS/Tate class.

## 7. Epistemic classification

### Exact

- discriminant normalization;
- root-negation action;
- square-value discriminant formula and derivative;
- Artin–Schreier equivalence removing `x^p`;
- fixed cubic Fourier phase after perfection;
- generic rank-two Airy and rank-one quadratic cases as standard Fourier–Deligne consequences.

### Open

- multiplicity of the discriminant component in the complete cyclic Adams characteristic cycle;
- derived equality at the wild weighted corner;
- rank-four theorem for `FT_c(E_a^prim)`;
- conductor bound and crown.
