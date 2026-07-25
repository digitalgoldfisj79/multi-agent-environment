# Divided-Adams Hasse coefficient at the resonant Airy boundary

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** analytic main branch for primes `p = 5 mod 6`.  
**Status:** the universal divided-Adams identities, Newton-edge calculation, and leading Hasse formula are **PROVED**. Uniform nonvanishing of the resulting Hasse coefficient and the archimedean Airy bound remain **OPEN**.

## 1. Result

Write

\[
p=3h+2,
\qquad
h=\frac{p-2}{3}.
\]

For the admitted primes `p = 5 mod 6`, the integer `h` is odd. Let

\[
\mathcal A(a)=
\begin{pmatrix}
x(a)&y(a)\\
z(a)&w(a)
\end{pmatrix}
\]

be Haessig's rank-two relative cubic-Airy Frobenius matrix, in the convention in which the local Dwork inverse roots have sum equal to the negative of the complete Airy sum. Define the scalar divided-Adams defect

\[
\mathfrak d_p(a)
=
\frac{\operatorname{Tr}(\mathcal A(a)^p)-x(a)^p-w(a)^p}{p}.
\]

Put

\[
F_h(u)
=
\sum_{n=0}^{h}
\frac{(-1)^n}{9^n n!\prod_{j=0}^{n-1}(3j+4)}u^n
\in \mathbf F_p[u].
\]

Equivalently, because `p=3h+2`,

\[
F_h(u)
=
\sum_{n=0}^{h}
\frac{(2h-n)!}{27^n n!(2h)!}u^n
\quad\text{in }\mathbf F_p[u].
\]

Define

\[
\boxed{
\mathcal H_p
=
\frac{h!}{6((2h+1)!)^2}
+
\frac1{h!}[u^h]\log F_h(u)
\in\mathbf F_p.
}
\]

Then the first possible nonzero initial form of the exact integer `T_p` is

\[
\boxed{
\frac{T_p}{p^{(p+4)/3}}
\equiv -\mathcal H_p\pmod p
}
\]

whenever the left side is integral. More precisely:

### Theorem 1.1

For every prime `p>=11` with `p=5 mod 6`,

\[
v_p(T_p)\ge \frac{p+4}{3},
\]

and

\[
\boxed{
\operatorname{in}_{(p+4)/3}(T_p)=-\mathcal H_p.
}
\]

Consequently,

\[
\boxed{
\mathcal H_p\ne0
\quad\Longrightarrow\quad
v_p(T_p)=\frac{p+4}{3}.
}
\]

The formula reproduces every committed exact value at

\[
p=11,17,23,29,41,47,53.
\]

A deterministic recurrence check finds `mathcal H_p != 0` for every prime `p=5 mod 6` with `11<=p<1500`; the exceptional prime `p=5` has `T_5=0` and `mathcal H_5=0`. This scan is a verification result, not a proof of uniform nonvanishing.

## 2. Universal divided Frobenius commutator

Let

\[
A=\begin{pmatrix}x&y\\z&w\end{pmatrix}
\]

be a universal rank-two matrix over `Z[x,y,z,w]`. Use the monomial bases

\[
q_i=X^{p-i}Y^i
\quad(0\le i\le p),
\]

and

\[
r_j=X^{p-2-j}Y^j
\quad(0\le j\le p-2).
\]

Let

\[
P:\operatorname{Sym}^p\longrightarrow
\det\otimes\operatorname{Sym}^{p-2}
\]

be the integral lift of the modular quotient map,

\[
P(q_i)=i r_{i-1}
\quad(1\le i\le p-1),
\qquad
P(q_0)=P(q_p)=0.
\]

The mod-`p` Adams exact sequence proves

\[
P\operatorname{Sym}^p(A)
\equiv
\det(A)\operatorname{Sym}^{p-2}(A)P
\pmod p.
\]

Therefore

\[
\boxed{
\mathcal C_p(A)
=
\frac{\operatorname{Sym}^p(A)P
-P\det(A)\operatorname{Sym}^{p-2}(A)}p
}
\]

is an integral polynomial matrix.

### Proposition 2.1: no rank collapse

The generic rank of `mathcal C_p(A)` is `p-1`.

At the anti-diagonal specialization

\[
A_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

one has

\[
\mathcal C_p(A_0)(q_i)=r_{p-1-i}
\quad(1\le i\le p-1).
\]

Thus the divided Frobenius defect is already surjective at `A_0`. The hoped-for bounded-rank Frobenius lift of the modular exact sequence is false.

## 3. Canonical-section trace identity

On the mixed quotient choose the canonical rational section

\[
S(r_j)=\frac1{j+1}q_{j+1}.
\]

Define

\[
\mathcal E_p(A)
=
\frac{S\operatorname{Sym}^p(A)P
-\det(A)\operatorname{Sym}^{p-2}(A)}p.
\]

Although this section is not a connection morphism, its trace is canonical.

### Theorem 3.1

\[
\boxed{
\operatorname{Tr}\mathcal E_p(A)
=
\frac{\operatorname{Tr}(A^p)-x^p-w^p}{p}.
}
\]

Indeed,

\[
\operatorname{Tr}
\left(S\operatorname{Sym}^p(A)P\right)
=
\sum_{i=1}^{p-1}
\left(\operatorname{Sym}^p(A)\right)_{ii}
=
\operatorname{Tr}(\operatorname{Sym}^p(A))-x^p-w^p,
\]

while the rank-two Adams identity gives

\[
\operatorname{Tr}(\operatorname{Sym}^p(A))
-\det(A)\operatorname{Tr}(\operatorname{Sym}^{p-2}(A))
=
\operatorname{Tr}(A^p).
\]

The numerator is divisible by `p` coefficientwise. Moreover,

\[
\operatorname{Tr}\mathcal E_p(A)
=yz(x+w)Q_{p-3}(x,y,z,w)
\]

for an integral homogeneous polynomial `Q_(p-3)`: the trace vanishes for `y=0`, for `z=0`, and for `x+w=0`.

At the anti-diagonal matrix,

\[
\mathcal E_p(A_0)(r_j)
=
\frac1{j+1}r_{p-2-j},
\]

so the defect is full rank but has trace zero. The global trace is generated entirely by deformation away from the anti-diagonal Airy Frobenius.

## 4. Exact relation to `T_p`

With Haessig's Dwork sign convention, the pointwise local trace is the negative of the repo's positively normalized Airy Adams trace. Therefore

\[
-pT_p
=
\sum_{a\in\mathbf F_p}
\operatorname{Tr}(\mathcal A(a)^p).
\]

At `a=0`, the relative Frobenius is anti-diagonal and the odd-power trace is zero. Thus

\[
\boxed{
T_p
=-\sum_{a\in\mathbf F_p^*}\mathfrak d_p(a)
-\frac1p\sum_{a\in\mathbf F_p^*}
\left(x(a)^p+w(a)^p\right).
}
\]

For a power series `f(a)` convergent on Teichmuller points,

\[
\sum_{a^{p-1}=1}f(a)
=(p-1)\sum_{m\ge0}[a^{m(p-1)}]f(a).
\]

The problem is therefore the initial Newton weight of two scalar coefficient sums.

## 5. Newton-edge Frobenius equations

Haessig's relative Frobenius satisfies the horizontality equation

\[
a\mathcal A'(a)
=G(a)\mathcal A(a)
-p\mathcal A(a)G(a^p),
\]

with

\[
G(a)=
\begin{pmatrix}
0&\pi a\\
-\pi a^2/3&0
\end{pmatrix},
\qquad
\pi^{p-1}=-p.
\]

For degrees below `p`, the second term has no contribution. Put

\[
u=\pi^2a^3.
\]

The lowest Newton-edge pieces are

\[
\begin{aligned}
x(a)&=\pi^{h+1}aX(u)+\text{higher Newton weight},\\
y(a)&=\pi^{2h+1}Y(u)+\text{higher Newton weight},\\
z(a)&=\pi^hZ(u)+\text{higher Newton weight},\\
w(a)&=\pi^{2h+2}a^2W(u)+\text{higher Newton weight}.
\end{aligned}
\]

Horizontality gives

\[
X+3uX'=Z,
\qquad
Z'=-X/9,
\]

and

\[
W=3Y',
\qquad
2W+3uW'=-Y/3.
\]

Writing `X=sum X_nu^n` and similarly, one obtains

\[
\boxed{
X_{n+1}=-\frac{X_n}{9(n+1)(3n+4)},
\qquad
Z_n=(3n+1)X_n,
}
\]

and

\[
\boxed{
Y_{n+1}=-\frac{Y_n}{9(n+1)(3n+2)},
\qquad
W_n=3(n+1)Y_{n+1}.
}
\]

Haessig's leading relative-Frobenius formula gives

\[
X_0=Z_0=\frac1{h!},
\qquad
Y_0=\frac1{(2h+1)!},
\qquad
W_0=-\frac{Y_0}{6}
\quad\text{in }\mathbf F_p.
\]

In particular,

\[
F_h(u)=X(u)/X_0
\]

through degree `h`.

## 6. First scalar divided-Adams coefficient

A monomial in `Tr(A^p)` is a closed walk of length `p` on two states. Let

- `r` be the number of `y` transitions and also the number of `z` transitions;
- `n_w` be the number of `w` loops;
- `s` be the total number of `u`-edge increments.

Then the number of `x` loops is

\[
n_x=p-2r-n_w.
\]

If the parameter degree is `p-1`, then

\[
p-2r+n_w+3s=p-1,
\]

so

\[
n_w=2r-1-3s.
\]

The product has pi-exponent

\[
E=(p-1)(h+r-s+1).
\]

The minimum occurs exactly when `r-s=1`. Nonnegativity leaves only two cases:

1. `r=1`, `s=0`, `n_w=1`, giving `x^(p-3)wyz`;
2. `r=2`, `s=1`, `n_w=0`, giving `x^(p-4)(yz)^2` with exactly one edge correction.

All other closed walks and every off-edge term have strictly larger Newton weight.

After division by `p`, the coefficient of the first monomial is `1`, while the coefficient of the second is `(p-3)/2`.

Put

\[
B=X_0^{p-2}Y_0^2.
\]

The first contribution is

\[
U_1=X_0^{p-3}W_0Y_0Z_0=-B/6.
\]

For the second contribution,

\[
(p-4)\frac{X_1}{X_0}
+2\frac{Y_1}{Y_0}
+2\frac{Z_1}{Z_0}
=-\frac29,
\]

and `(p-3)/2=-3/2` in `F_p`, so

\[
U_2=B/3.
\]

Therefore

\[
U_1+U_2=B/6.
\]

Since `p-2=3h`, Fermat and Wilson give

\[
X_0^{p-2}=h!,
\qquad
(2h+1)!=1/h!
\]

because `h` is odd. Hence:

### Theorem 6.1

Let

\[
E_0=(p-1)\frac{p+4}{3}.
\]

Then

\[
\boxed{
\pi^{-E_0}[a^{p-1}]\mathfrak d_p(a)
\equiv
\frac{h!}{6((2h+1)!)^2}
\pmod\pi.
}
\]

This residue is nonzero for every admitted prime.

For a later Teichmuller degree `m(p-1)`, `m>=2`, the same walk bookkeeping gives

\[
E_m=(p-1)\left(m(h+1)+r-s\right).
\]

The constraints imply

\[
m(h+1)+r-s>h+2,
\]

so every later scalar selected coefficient is strictly more divisible.

## 7. Endpoint `p`-th-power coefficient

The term `x(a)^p` has no coefficient at degree `p-1`. Its first possible Teichmuller coefficient is at degree `2(p-1)`. On the Newton edge,

\[
x(a)^p
=\pi^{p(h+1)}a^pX_0^pF_h(u)^p.
\]

The required `u`-degree is exactly `h`. Since `0<h<p`, the coefficient `[u^h]F_h(u)^p` is divisible by `p`. The standard divided-Frobenius congruence gives

\[
\boxed{
\frac1p[u^h]F_h(u)^p
\equiv
[u^h]\log F_h(u)\pmod p.
}
\]

Indeed, for a composition of total length `M<p`,

\[
\frac1p\binom pM
\equiv\frac{(-1)^{M-1}}M\pmod p,
\]

which is exactly the coefficient expansion of the logarithm.

The extra divisibility by `p` cancels the external division by `p`, and the resulting pi-exponent is again

\[
p(h+1)+2h=E_0.
\]

The term `w(a)^p` and every later endpoint Teichmuller coefficient have strictly larger Newton weight.

### Theorem 7.1

\[
\boxed{
\pi^{-E_0}
[a^{2(p-1)}]
\frac{x(a)^p+w(a)^p}{p}
\equiv
\frac1{h!}[u^h]\log F_h(u)
\pmod\pi.
}
\]

## 8. Hasse initial form of `T_p`

Combining Theorems 6.1 and 7.1 with Teichmuller summation and `pi^(p-1)=-p` gives

\[
\boxed{
\frac{T_p}{p^{(p+4)/3}}
\equiv
-\left(
\frac{h!}{6((2h+1)!)^2}
+
\frac1{h!}[u^h]\log F_h(u)
\right)
\pmod p.
}
\]

This is Theorem 1.1.

The logarithmic coefficient may be computed without formal logarithms. If

\[
R(u)=\frac{F_h'(u)}{F_h(u)}
=\sum_{n\ge0}r_nu^n,
\]

then

\[
r_0=-\frac1{36},
\]

and the differential equation for `F_h` gives the Rayleigh recurrence

\[
\boxed{
(3n+4)r_n
=-3\sum_{i=0}^{n-1}r_i r_{n-1-i}
\quad(n\ge1).
}
\]

Moreover,

\[
[u^h]\log F_h(u)=r_{h-1}/h.
\]

This yields an `O(h^2)` deterministic computation of `mathcal H_p` using only arithmetic in `F_p`.

## 9. Exact calibration

For the committed exact integers:

\[
\begin{array}{c|c|c|c}
p&v_p(T_p)&T_p/p^{(p+4)/3}\bmod p&-\mathcal H_p\\ \hline
11&5&2&2\\
17&7&12&12\\
23&9&14&14\\
29&11&5&5\\
41&15&13&13\\
47&17&4&4\\
53&19&10&10
\end{array}
\]

The independent script `divided_adams_hasse_verify.py` checks the recurrence, all seven exact calibrations, and the nonvanishing scan below `1500`.

## 10. What this changes

### PROVED

1. The universal divided Frobenius commutator is integral but generically full rank.
2. Its canonical-section trace is the scalar divided-Adams polynomial.
3. The anti-diagonal Airy specialization has full-rank weighted reversal and trace zero.
4. The first scalar Teichmuller coefficient has exact valuation `(p+4)/3` and an explicit nonzero factorial residue.
5. The endpoint correction lies on the same valuation line and is the displayed logarithmic/Rayleigh coefficient.
6. The exact leading Hasse formula for `T_p` follows.

### VERIFIED, NOT PROVED UNIFORMLY

\[
\mathcal H_p\ne0
\]

for every prime `p=5 mod 6`, `11<=p<1500`.

### OPEN

1. Prove `mathcal H_p != 0` for every admitted prime.
2. Convert the divided-Adams initial form into an archimedean trace cancellation theorem.
3. Prove
   \[
   |T_p|\le C p^{(p-1)/2}
   \]
   with absolute `C`.
4. The crown.

The p-adic boundary is no longer an unexplained empirical valuation. It is controlled by one explicit Airy Hasse/Rayleigh coefficient. This is genuine main-branch progress, but p-adic nonvanishing alone does not remove the remaining archimedean factor of order `p`.

## References

- C. Haessig, *L-functions of symmetric powers of cubic exponential sums*, 2006, especially the relative Frobenius, effective decomposition, and Frobenius-estimate sections.
- The repo notes `MOD_P_ADAMS_FROBENIUS_EXACT_SEQUENCE.md`, `HAESSIG_KP_RESIDUE_FACTORIZATION_20260724.md`, and `AIRY_ARITHMETIC_PL_CORRELATION_OBSTRUCTION_20260725.md`.
