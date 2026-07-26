# Cayley--Jacobian grading, modular lifting obstruction, and exact `p=11/p=13` hook audit

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** function-field Fortune at `d=1`; sparse smooth complete-intersection surface and its compactified primitive middle cohomology.  
**Status:** the grading is a **PUBLISHED THEOREM** specialized to the present geometry. The root-space lifting obstruction is a **PROVED THEOREM**. The `p=11` and `p=13` character calculations are **EXACT COMPUTER-ASSISTED THEOREMS**, with exact rational arithmetic, two independent Hilbert calculations, Murnaghan--Nakayama certificates, full character-table orthogonality, and dimension checks. The identification of the compactified primitive character uses the standard prime-to-`p` crystalline/étale trace comparison for algebraic correspondences.

## 0. Main ruling

The Cayley grading in the handover is correct:

\[
\boxed{
\kappa=\frac{(p-7)(p-2)}2,
\qquad
J_{(\kappa,0)},\ J_{(\kappa,1)},\ J_{(\kappa,2)}.
}
\]

The corresponding top Dwork second degrees are

\[
\boxed{p-5,\quad p-4,\quad p-3.}
\]

The newly isolated lifting issue is real and has a sharper resolution:

1. the modular root space
   \[
   W=\ker(\sum)/\langle(1,\ldots,1)\rangle
   \]
   has no ordinary `S_p`-equivariant characteristic-zero vector-space lift of dimension `p-2`;
2. the outer Jacobian component `J_(kappa,0)` has a unique **character-theoretic** ordinary lift at `p=11` and `p=13`;
3. the middle component `J_(kappa,1)` has **no** nonnegative ordinary-character extension at either prime;
4. the total
   \[
   2J_{(\kappa,0)}+J_{(\kappa,1)}
   \]
   does have a unique ordinary-character extension, and this is the compactified primitive `H^2` character after the residue sign twist.

Thus the correct model is not an ordinary lift of `W`, and not a componentwise characteristic-zero splitting of the three Jacobian degrees. The viable construction is:

- retain the full permutation lattice or an equivalent Dwork/divided-power model in characteristic `p`;
- treat translation by a derived special-fibre quotient;
- compute prime-to-`p` character data directly;
- allow the three Jacobian degrees to recombine before passage to ordinary `ell`-adic hook multiplicities.

This selects a combination of options 2, 3 and 4 in the handover and rules out the naïve form of option 1.

## 1. Published Cayley--Jacobian grading

Let

\[
n=\dim W=p-2,
\qquad
r=p-5,
\qquad
(d_1,\ldots,d_r)=(2,3,\ldots,p-4).
\]

For the Cayley polynomial

\[
F(x,y)=\sum_{m=2}^{p-4}y_m s_m(x),
\]

Adolphson--Sperber use the bigrading

\[
\deg_1 x_i=1,
\quad
\deg_2 x_i=0,
\quad
\deg_1 y_m=-m,
\quad
\deg_2 y_m=1.
\]

Their complete-intersection theorem identifies the primitive Hodge numbers with

\[
J_{(\sum d_m-n,j)}.
\]

Now

\[
\sum_{m=2}^{p-4}m
=\frac{(p-5)(p-2)}2,
\]

so

\[
\sum d_m-n
=\frac{(p-5)(p-2)}2-(p-2)
=\boxed{\frac{(p-7)(p-2)}2}.
\]

Since the surface dimension is

\[
n-r-1=2,
\]

only `j=0,1,2` occur. In the top de Rham/Dwork complex, the second degree is shifted by `r`, hence

\[
j+r=p-5,p-4,p-3.
\]

### Status

**PUBLISHED THEOREM**, specialized from A. Adolphson and S. Sperber, *On the Jacobian ring of a complete intersection*, arXiv:math/0610228, especially equations (1.1)--(1.3), (1.4)--(1.5), and the top-cohomology identification following them.

## 2. No ordinary lift of the modular root space

Let `sigma=(1 2 ... p)`. Over `F_p`, the permutation module restricted to `C_p=<sigma>` is

\[
\mathbf F_p[C_p]\cong \mathbf F_p[\varepsilon]/(\varepsilon^p),
\qquad
\sigma=1+\varepsilon.
\]

The augmentation kernel is `(epsilon)` and the diagonal line is the norm/socle line `(epsilon^(p-1))`. Therefore

\[
\boxed{
W\big|_{C_p}
\cong
(\varepsilon)/(\varepsilon^{p-1}),
}
\]

one indecomposable Jordan block of length `p-2`.

For `p>=7`, the least degree of a nonlinear ordinary irreducible representation of `S_p` is `p-1`. Hence an ordinary representation of dimension `p-2` is a sum of trivial and sign lines. An odd-length `p`-cycle is even, so it acts trivially on both. Its reduction cannot be the nontrivial Jordan block above.

### Theorem 2.1 — ordinary root-space lift obstruction

\[
\boxed{
W\text{ has no ordinary }S_p\text{-equivariant characteristic-zero lift of dimension }p-2.
}
\]

The exact `p=11` and `p=13` degree claims are independently certified by hook-length enumeration in `modular_root_space_lift_obstruction_verify.py`. The uniform minimal-degree input is Rasala's theorem on the minimal degrees of ordinary characters of `S_n`.

There is also an integral derived obstruction to the naïve three-term quotient. Over `Z_p`, diagonal inclusion and coordinate sum satisfy

\[
\boxed{
(\mathrm{sum})\circ(\mathrm{diag})=p,
}
\]

not zero. The apparent complex

\[
\mathbf1\longrightarrow\mathrm{Perm}_p\longrightarrow\mathbf1
\]

is a complex only after reduction modulo `p`. Translation removal is therefore intrinsically a special-fibre, divided-power, matrix-factorization or derived-mod-`p` operation; it is not an ordinary flat quotient of representations.

## 3. Prime-to-`p` character formula

Let

\[
R=\operatorname{Sym}(W^*)/(s_2,\ldots,s_{p-4}).
\]

For a `p`-regular permutation `g` of cycle type

\[
\mu=(\mu_1,\ldots,\mu_c),
\]

the cyclic subgroup generated by `g` is linearly reductive. The sum and diagonal lines split, and

\[
\boxed{
\det(1-tg\mid W)
=
\frac{\prod_{a=1}^c(1-t^{\mu_a})}{(1-t)^2}.
}
\]

Since the defining regular sequence is invariant,

\[
\boxed{
\sum_{k\ge0}\operatorname{BrTr}(g\mid R_k)t^k
=
\frac{(1-t)^2\prod_{m=2}^{p-4}(1-t^m)}
{\prod_{a=1}^c(1-t^{\mu_a})}.
}
\]

Put

\[
r_k(g)=\operatorname{BrTr}(g\mid R_k).
\]

Then

\[
\boxed{
\operatorname{BrTr}(g\mid J_{(\kappa,0)})=r_\kappa(g).
}
\]

The bidegree-one Cayley--Jacobian/Koszul identity gives

\[
\boxed{
\operatorname{BrTr}(g\mid J_{(\kappa,1)})
=
\sum_{m=2}^{p-4}r_{\kappa+m}(g)
-\operatorname{BrTr}(g\mid W)r_{\kappa+1}(g)
+r_\kappa(g),
}
\]

where

\[
\operatorname{BrTr}(g\mid W)
=\#\{\text{fixed letters of }g\}-2.
\]

The outer components have equal prime-to-`p` characters by Cayley duality, so the total Jacobian character is

\[
\boxed{
2J_{(\kappa,0)}+J_{(\kappa,1)}.
}
\]

The residue identification with primitive cohomology carries the determinant of the root representation. On `p`-regular classes

\[
\det W=\operatorname{sgn},
\]

so the cohomological hook profile is the Jacobian hook profile reversed by

\[
\bigwedge^i\mathrm{Std}\otimes\operatorname{sgn}
\cong
\bigwedge^{p-1-i}\mathrm{Std}.
\]

## 4. The one-dimensional wild ambiguity

For `S_p`, the only `p`-singular conjugacy class is the class of `p`-cycles. Hence restriction of ordinary class functions to `p`-regular classes has a one-dimensional kernel.

That kernel is generated by

\[
\Lambda_p
=
\sum_{i=0}^{p-1}(-1)^i\bigwedge^i\mathrm{Std},
\]

whose character is `p` on a `p`-cycle and zero elsewhere.

Therefore every ordinary extension of a fixed `p`-regular character differs by

\[
c\Lambda_p,
\qquad c\in\mathbf Z.
\]

At the hook level this changes multiplicities by

\[
\boxed{m_i\longmapsto m_i+c(-1)^i.}
\]

Thus nonnegativity supplies an exact interval for `c`. If the interval is empty, the modular component has no genuine ordinary-character lift. If it is a singleton, the extension and the `p`-cycle trace are uniquely forced.

## 5. Exact Hodge dimensions

Two independent Hilbert-series computations and an independent Chern-class calculation give:

| `p` | `kappa` | `dim J_(kappa,0)` | `dim J_(kappa,1)` | `dim J_(kappa,2)` | primitive `b_2` |
|---:|---:|---:|---:|---:|---:|
| 11 | 18 | 231,419 | 681,239 | 231,419 | 1,144,077 |
| 13 | 33 | 53,524,799 | 140,071,679 | 53,524,799 | 247,121,277 |

Here

\[
\dim J_{(\kappa,0)}
=[t^\kappa]
\frac{\prod_{m=2}^{p-4}(1-t^m)}{(1-t)^{p-2}},
\]

and

\[
\dim J_{(\kappa,1)}
=
\sum_{m=2}^{p-4}\dim R_{\kappa+m}
-(p-2)\dim R_{\kappa+1}
+\dim R_\kappa.
\]

The latter equals the independent Chern/Noether value

\[
e(Y_p)-3-2p_g.
\]

## 6. Exact `p=11` character calculation

### 6.1 Outer component

The unique genuine ordinary extension of `J_(18,0)` has hook multiplicities

\[
\boxed{(1,1,1,3,4,1,0,0,0,0,0).}
\]

Its `p`-cycle trace is `1`. Its even/odd hook totals are `6` and `5`. The same statement holds for `J_(18,2)`.

### 6.2 Middle component

The unique integral residue class for the unknown `p`-cycle trace gives the base hook vector

\[
(0,0,5,5,7,3,1,-1,1,-1,1).
\]

Every extension is `m_i(c)=m_i(0)+c(-1)^i`. Even-hook nonnegativity requires `c>=0`; odd-hook nonnegativity requires `c<=-1`. Hence

\[
\boxed{[0,-1]=\varnothing.}
\]

### Theorem 6.1

\[
\boxed{J_{(18,1)}\text{ has no genuine ordinary }S_{11}\text{-character extension.}}
\]

### 6.3 Recombined primitive middle cohomology

The total Jacobian character has the unique hook profile

\[
(1,3,6,12,14,6,0,0,0,0,0),
\]

with `11`-cycle trace `0`. After the residue sign twist, the actual compactified primitive `H^2` hook profile is

\[
\boxed{(0,0,0,0,0,6,14,12,6,3,1).}
\]

All nontrivial compactified hook multiplicities occur in cohomological degree `2`. The parity-separated multiplicity dimensions are

\[
\boxed{B_{\mathrm{even}}^{\mathrm{prim}}=21,
\qquad B_{\mathrm{odd}}^{\mathrm{prim}}=21.}
\]

The sign hook contributes exactly one. Removing it leaves non-sign multiplicity mass `41`. Thus the compactified primitive Jacobian page does not reproduce the `p=11` budget `10`. The discriminant/open-boundary cone must remove at least

\[
\boxed{41-10=31}
\]

non-sign multiplicity dimensions before the Sawin interval complex can satisfy the target.

## 7. Exact `p=13` character calculation

### 7.1 Outer component

The unique genuine ordinary extension of `J_(33,0)` has hook multiplicities

\[
\boxed{(1,1,5,8,11,12,9,2,0,0,0,0,0).}
\]

Its `13`-cycle trace is `3`. Its even/odd hook totals are `26` and `23`. The same statement holds for `J_(33,2)`.

### 7.2 Middle component

The integral base hook vector is

\[
(-1,1,7,17,28,26,18,6,1,-1,1,-1,1).
\]

Even-hook nonnegativity requires `c>=1`; odd-hook nonnegativity requires `c<=-1`. Hence

\[
\boxed{[1,-1]=\varnothing.}
\]

### Theorem 7.1

\[
\boxed{J_{(33,1)}\text{ has no genuine ordinary }S_{13}\text{-character extension.}}
\]

### 7.3 Recombined primitive middle cohomology

The unique total Jacobian hook profile is

\[
(0,4,16,34,49,51,35,11,0,0,0,0,0),
\]

with `13`-cycle trace `0`. After sign twist, the compactified primitive `H^2` hook profile is

\[
\boxed{(0,0,0,0,0,11,35,51,49,34,16,4,0).}
\]

The parity-separated multiplicity dimensions in cohomological degree `2` are

\[
\boxed{B_{\mathrm{even}}^{\mathrm{prim}}=100,
\qquad B_{\mathrm{odd}}^{\mathrm{prim}}=100.}
\]

There is no sign or trivial hook. The compactified non-sign multiplicity mass is `200`. Any comparison to a multiplicity-one budget `12` must therefore remove at least

\[
\boxed{200-12=188}
\]

hook multiplicity dimensions through the discriminant/open-boundary and exceptional-chart cones.

This strengthens the previous raw-bar regression. The old theorem required an explanation for at least five non-sign terminal classes. The actual compactified Cayley--Jacobian regression requires a much larger boundary differential.

## 8. What is proved, refuted, and still open

### PROVED THEOREM

1. `W` has no ordinary `S_p`-equivariant characteristic-zero lift of dimension `p-2`.
2. The naïve integral complex `1 -> Perm -> 1` is obstructed by `sum o diag=p`.
3. Ordinary extensions of a `p`-regular character differ by the single hook-alternating class `Lambda_p`.
4. The three Jacobian degrees cannot be treated as separately lifted ordinary representations: the middle degree fails nonnegativity at both regression primes.

### PUBLISHED THEOREM

1. The Adolphson--Sperber Cayley grading and primitive-Hodge/Jacobian dimension theorem.
2. Prime-to-`p` comparison of traces of algebraic correspondences in crystalline and `ell`-adic cohomology.
3. Rasala's minimal-degree theorem for ordinary representations of symmetric groups.

### EXACT COMPUTER-ASSISTED THEOREM

1. The Hodge dimensions and primitive Betti numbers displayed above.
2. The exact outer-component hook profiles.
3. The empty middle-component ordinary-lift intervals.
4. The exact recombined primitive `H^2` hook profiles and parity totals.
5. The forced `p`-cycle trace `0` on total primitive `H^2` at `p=11` and `p=13`.

### REFUTED

1. Silent replacement of `W` by the characteristic-zero standard representation.
2. A componentwise ordinary lift of the three Jacobian degrees.
3. The compactified primitive Jacobian ring as the final Betti-bounded page.
4. The hypothesis that the `p=13` boundary only has to kill the five classes seen in the raw terminal bar model.

### OPEN

1. The `S_p`-equivariant localization triangle for `D_p=Y_p\setminus Y_p^{sep}` with the frequency-infinity and exceptional coefficient charts included.
2. The actual Gysin/residue map
   \[
   R\Gamma(D_p)(-1)[-2]\longrightarrow R\Gamma(Y_p)
   \]
   on hook multiplicity complexes.
3. Proof that this boundary map removes at least `31` non-sign multiplicity dimensions at `p=11`, at least `188` at `p=13`, and uniformly leaves at most `p-1` in the admitted sector.
4. Frobenius compatibility and the exact sign/discriminant extraction inside that localization triangle.

## 9. Exact next theorem

> **Equivariant discriminant-Gysin cancellation theorem.** Let `D_p` be the discriminant divisor in the smooth sparse root surface `Y_p`, augmented by the root-infinity, frequency-infinity, `q=0`, `q=2`, `q=infinity`, translation, scaling and punctual boundary strata. Construct its parity-separated `S_p`-equivariant residue/Gysin complex and prove that the image in `H^2_prim(Y_p)` contains all but at most `p-1` hook multiplicity dimensions after exact sign extraction. At `p=11` the map must have non-sign hook rank at least `31`; at `p=13` it must have hook rank at least `188`.

This is now the highest-value theorem. The mixed Cayley derivative identifies the differential algebraically, but the load-bearing cancellation occurs in the compactified discriminant/Gysin map, not inside a separately lifted middle Jacobian component.

## 10. Verification

Run:

```bash
python frontier/strategy/cayley_jacobian_hook_lift_verify.py
python frontier/strategy/modular_root_space_lift_obstruction_verify.py
```

The first command also writes

```text
frontier/strategy/cayley_jacobian_hook_results_20260726.json
```

with all exact profiles, lift intervals, Hodge dimensions and parity totals.
