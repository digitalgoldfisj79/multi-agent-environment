# Involution-quotient Cartier certificate: exact square-sector ruling

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** function-field `d=1` Fortune sibling.  
**Status:** the quotient certificate and scaling symmetry are **PROVED**. Exact determinant computations show that the square-subgroup restriction gives no uniform simplification.

## 1. Quotient family

Let `p=2n+1`, `a!=0`, and

\[
G_{a,c,e}(Y)=Y(Y^n+aY+c)^2-e.
\]

The proved involution-quotient theorem states that for `d!=0`,

\[
X^p+aX^3+cX+d
\quad\text{is irreducible}
\]

if and only if

\[
G_{a,c,d^2}(Y)
\quad\text{is irreducible}.
\]

Consequently,

\[
N_a(p)=2\#\{(c,e):e\in(\mathbf F_p^*)^2,\ G_{a,c,e}\text{ irreducible}\}.
\]

Expanding gives

\[
G=Y^p+2aY^{n+2}+2cY^{n+1}+a^2Y^3+2acY^2+c^2Y-e.
\]

The coefficient of `Y^3` is `a^2`. The general Cartier cofactor theorem therefore gives the pointwise certificate

\[
\boxed{
C_3(G_{a,c,e})=3a^2\,1_{G_{a,c,e}\mathrm{\ irreducible}}
}
\]

in `F_p`.

## 2. Exact occupation formula

For the full Cartier matrix

\[
H_{u,v}=[Y^{pu-v}]G^{p-1},
\]

let `(i,j,k,l,r,s)` be the occupations of

\[
2aY^{n+2},\quad
2cY^{n+1},\quad
a^2Y^3,\quad
2acY^2,\quad
c^2Y,\quad
-e.
\]

After eliminating the occupation of `Y^p`, an entry contribution satisfies

\[
\boxed{
(n-1)i+n j+(p-3)k+(p-2)l+(p-1)r+ps
=p(p-1-u)+v.
}
\]

Its coefficient is

\[
(-1)^N\frac{N!}{i!j!k!l!r!s!}
(2a)^i2^j(a^2)^k(2a)^l(-1)^s
c^{j+l+2r}e^s,
\]

where `N=i+j+k+l+r+s`.

This formula is implemented in `involution_quotient_cartier_probe.py` and used to construct the selected cofactor as an exact polynomial in `(c,e)`.

## 3. Scaling theorem

For `s in F_p^*`, direct substitution gives

\[
\frac{G_{a,c,e}(sZ)}s
=G_{a',c',e'}(Z),
\]

where

\[
a'=\chi(s)as,
\qquad
c'=\chi(s)c,
\qquad
e'=e/s.
\]

Indeed, `s^n=chi(s)` and `2n+1=p`.

### Corollary: `p=3 mod 4`

Take `s=-1`. Then `chi(-1)=-1`, so

\[
a'=a,\qquad c'=-c,\qquad e'=-e.
\]

Thus at fixed `a`,

\[
1_{G_{a,c,e}\mathrm{\ irr}}
=1_{G_{a,-c,-e}\mathrm{\ irr}}.
\]

Because `-1` exchanges squares and nonsquares when `p=3 mod 4`, the two `e`-sectors have equal irreducible counts. Equivalently, after summing over `c`, the quadratic multiplicative Fourier coefficient in `e` vanishes.

Therefore the square-restricted certificate is exactly half of the complete nonzero-`e` certificate. The apparent improvement from orthogonality modulo `(p-1)/2` disappears.

### `p=1 mod 4`

Now `-1` is a square and does not exchange the two sectors. The quadratic `e`-mode can survive. It is an additional term, not a simplification.

## 4. Exact computation

The exact selected cofactor was computed by subset-DP determinant arithmetic.

| `p` | cofactor degree `(c,e)` | monomials | square survivors | genuinely quadratic `e` survivors | irreducible counts `(square,nonsquare)` |
|---:|---:|---:|---:|---:|---:|
| 5 | `(19,7)` | 72 | 5 | 3 | `(2,3)` |
| 7 | `(33,14)` | 150 | 10 | 0 | `(5,5)` |
| 11 | `(87,36)` | 1034 | 23 | 0 | `(7,7)` |
| 13 | `(123,51)` | 4037 | 59 | 29 | `(5,3)` |

Here a genuinely quadratic survivor has `e`-degree divisible by `(p-1)/2` but not by `p-1`.

At every prime, the summed cofactor agrees with

\[
3a^2\#\{(c,e):e\text{ square and }G_{a,c,e}\text{ irreducible}\}
\pmod p.
\]

The `p=7,11` absence of quadratic survivors is explained by the scaling theorem. The `p=5,13` computations show that the surviving quadratic sector is already large and grows rather than collapsing to one term.

## 5. Ruling

The involution quotient remains a useful exact reformulation and explains parity of `N_a`, but its Cartier certificate does not improve the crown calculation uniformly.

- For `p=3 mod 4`, square restriction is algebraically redundant: the square and nonsquare sectors are exactly equal.
- For `p=1 mod 4`, a new quadratic sector survives and increases the determinant complexity.
- The quotient does not convert the complete cofactor sum into a fixed-length expression or a single Hasse coefficient.

The proposed square-subgroup orthogonality gain is therefore **closed**. The viable Cartier problem remains the original depressed-slice survivor cancellation law, not the involution quotient.
