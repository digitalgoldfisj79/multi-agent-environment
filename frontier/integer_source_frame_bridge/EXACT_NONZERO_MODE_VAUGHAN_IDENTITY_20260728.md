# Exact nonzero-mode Vaughan identity

Date: 28 July 2026  
Status: exact finite identity proved; nonzero reciprocal-mode variance estimate open.

## 1. Notation

Let `w_m` be deterministic weights supported on `2<=m<=H`.  For a modulus `q`,
define

\[
\widehat w_q(r)=\sum_{m=2}^{H}w_m e(rm/q),
\qquad r\bmod q.
\tag{1.1}
\]

For Type I, define the logarithmically weighted transform

\[
\widehat g_{j,d}(r)
=
\sum_{m=2}^{H}
 w_m\log\frac{P_j+m}{d}\,e(rm/d).
\tag{1.2}
\]

Use the cutoff

\[
Y=\lfloor P_0^{1/3}\rfloor>H,
\]

and the quotient coefficients

\[
A_Y(q)=
\sum_{dc=q,\ d,c\le Y}\mu(d)\Lambda(c),
\tag{1.3}
\]

\[
C_Y(q)=
\sum_{ac=q,\ a,c>Y}\mu(a)\Lambda(c).
\tag{1.4}
\]

Put `Z_j=P_j+H`.  All modulus sums below are finite: Type II has `q<=Y^2`, and
Type III has `Y^2<q<=Z_j`.

## 2. Centred divisibility projector

Additive orthogonality gives, exactly,

\[
\sum_mw_m\mathbf1_{q\mid P_j+m}
=
\frac1q\sum_{r\bmod q}
\widehat w_q(r)e(rP_j/q).
\tag{2.1}
\]

Separating the zero mode yields

\[
\boxed{
R_{j,q}(w)
:=
\sum_mw_m\mathbf1_{q\mid P_j+m}
-rac{W_H}{q}
=
\frac1q\sum_{r=1}^{q-1}
\widehat w_q(r)e(rP_j/q).
}
\tag{2.2}
\]

Similarly,

\[
\boxed{
G_{j,d}(w)
:=
\sum_mw_m\mathbf1_{d\mid P_j+m}
\log\frac{P_j+m}{d}
-rac{L_j-W_H\log d}{d}
=
\frac1d\sum_{r=1}^{d-1}
\widehat g_{j,d}(r)e(rP_j/d).
}
\tag{2.3}
\]

Here

\[
W_H=\sum_mw_m,
\qquad
L_j=\sum_mw_m\log(P_j+m).
\]

## 3. Exact nonzero Vaughan pieces

### Proposition 3.1 (Type I)

After subtracting its exact zero mode, the Type I contribution is

\[
\boxed{
\mathcal E_{I,j}
=
\sum_{d\le Y}\mu(d)G_{j,d}(w)
=
\sum_{d\le Y}
\frac{\mu(d)}d
\sum_{r=1}^{d-1}
\widehat g_{j,d}(r)e(rP_j/d).
}
\tag{3.1}
\]

### Proposition 3.2 (subtraction term)

After subtracting its exact zero mode,

\[
\boxed{
\mathcal E_{II,j}
=-
\sum_{q\le Y^2}A_Y(q)R_{j,q}(w)
=-
\sum_{q\le Y^2}
\frac{A_Y(q)}q
\sum_{r=1}^{q-1}
\widehat w_q(r)e(rP_j/q).
}
\tag{3.2}
\]

### Proposition 3.3 (large-large term)

After subtracting its exact zero mode,

\[
\boxed{
\mathcal E_{III,j}
=
\sum_{Y^2<q\le Z_j}C_Y(q)R_{j,q}(w)
=
\sum_{Y^2<q\le Z_j}
\frac{C_Y(q)}q
\sum_{r=1}^{q-1}
\widehat w_q(r)e(rP_j/q).
}
\tag{3.3}
\]

The lower bound `q>Y^2` follows from `a,c>Y` in (1.4).

## 4. Exact centred source

Let `mu_j^(0)` be the zero-frequency principal term from
`EXPLICIT_ZERO_FREQUENCY_PRINCIPAL_TERM_20260728.md`.

### Theorem 4.1 (nonzero-mode source identity)

One has exactly

\[
\boxed{
\sum_{m=2}^{H}w_m\Lambda(P_j+m)-\mu_j^{(0)}
=
\mathcal E_{I,j}+\mathcal E_{II,j}+\mathcal E_{III,j}.
}
\tag{4.1}
\]

### Proof

Insert the exact Vaughan identity, apply (2.1) to every divisibility condition,
and subtract the three zero modes already identified in the principal-term note.
All rearrangements are finite.  Equations (3.1)--(3.3) are the surviving nonzero
characters.  \(\square\)

## 5. Modulus trichotomy

The residual source is now divided into three explicit ranges:

1. **Type I:** `d<=Y=P_0^(1/3)` with coefficient `mu(d)` and a logarithmic physical transform;
2. **middle range:** `q<=Y^2=P_0^(2/3)` with coefficient `A_Y(q)`;
3. **high range:** `Y^2<q<=P_j+H` with coefficient `C_Y(q)`.

The quotient-coefficient theorem gives

\[
|A_Y(q)|,|C_Y(q)|\le2\log q.
\tag{5.1}
\]

Thus the decomposition has fixed convolution complexity and logarithmic
coefficients throughout.

## 6. Exact analytic target

The Fortune variance theorem is now equivalent to proving

\[
\boxed{
\sum_{j<N}
|\mathcal E_{I,j}+\mathcal E_{II,j}+\mathcal E_{III,j}|^2
\ll NHX L(X),
\qquad L(X)=o(\log X).
}
\tag{6.1}
\]

The signed sum must remain intact: separate positive majorants recreate the known
`X/log X` loss.

The shrinking-target theorem supplies bounded primorial support for the large
routed factors underlying (3.1)--(3.3).  The remaining step is a signed
completion/dispersion argument that converts the phases

\[
e(rP_j/q)
\]

into fixed-complexity bilinear or trilinear reciprocal forms without discarding
the `j`-sum.

## 7. Boundary

Proved:

1. exact centred projectors (2.2), (2.3);
2. exact nonzero-mode pieces (3.1)--(3.3);
3. exact identity (4.1);
4. finite low/middle/high modulus partition;
5. logarithmic coefficient complexity.

Open:

1. the signed nonzero-mode estimate (6.1);
2. a parameter-valid reduction to current Kloosterman-fraction theorems;
3. Fortune's conjecture.
