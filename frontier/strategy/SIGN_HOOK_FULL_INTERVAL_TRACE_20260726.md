# Exact sign-hook trace on the full four-parameter interval

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Target:** aggregate `h=4` Betti programme for function-field Fortune at `d=1`.  
**Status:** the trace formula below is **PROVED**. The verification is exact and independent of the cyclotomic `C_wedge` computation.

## 0. Statement

Let `p>3` be an odd prime and let

\[
\mathcal I_4=
\left\{
X^p-X+aX^3+bX^2+cX+d:
(a,b,c,d)\in\mathbf F_p^4
\right\}.
\]

Put `u=c-1`, so the same interval is parametrized by

\[
f_{a,b,u,d}(X)=X^p+aX^3+bX^2+uX+d.
\]

Extend the quadratic character `chi` of `F_p` by `chi(0)=0`. For squarefree `f`, the sign of the Frobenius permutation equals `chi(Disc(f))`; for nonsquarefree `f`, both the sign factorization function and this extended discriminant character are zero.

Define the full sign-hook trace

\[
S_{\mathrm{sgn}}(p)
=
\sum_{a,b,u,d\in\mathbf F_p}
\chi\!\left(\operatorname{Disc}f_{a,b,u,d}\right).
\]

### Theorem 0.1

\[
\boxed{
S_{\mathrm{sgn}}(p)
=
\frac{1-\chi(-1)}2\,\chi(-6)\,p^2(p-1).
}
\]

Equivalently,

\[
S_{\mathrm{sgn}}(p)=
\begin{cases}
0,&p\equiv1\pmod4,\\
\chi(-6)p^2(p-1),&p\equiv3\pmod4.
\end{cases}
\]

For the admitted primes `p congruent 5 mod 6`, this becomes

\[
\boxed{
S_{\mathrm{sgn}}(p)=
\begin{cases}
0,&p\equiv5,17\pmod{24},\\
+p^2(p-1),&p\equiv11\pmod{24},\\
-p^2(p-1),&p\equiv23\pmod{24}.
\end{cases}
}
\]

## 1. Reduction to critical-value collisions

Let

\[
\varepsilon_p=(-1)^{(p-1)/2}.
\]

Since `p` is odd and the polynomial is monic,

\[
\operatorname{Disc}(f)
=
\varepsilon_p\operatorname{Res}(f,f').
\]

The derivative is

\[
f'(X)=3aX^2+2bX+u.
\]

### 1.1 The sector `a=0`

If `b` is nonzero, the derivative is linear and the resultant is a nonconstant affine function of `d`; its quadratic-character sum over `d` is zero.

If `b=0` and `u` is nonzero, the derivative is constant and

\[
\operatorname{Res}(f,u)=u^p.
\]

The sum over `d` contributes a factor `p`, but summing `chi(epsilon_p u)` over nonzero `u` gives zero.

If `a=b=u=0`, the derivative vanishes and the discriminant is zero. Therefore the entire `a=0` sector contributes zero.

### 1.2 The sector `a` nonzero

Let `r,s` be the roots of

\[
g(X)=3aX^2+2bX+u,
\]

and put

\[
\delta=b^2-3au.
\]

Then

\[
(r-s)^2=\frac{4\delta}{9a^2}.
\]

Write

\[
F(X)=X^p+aX^3+bX^2+uX.
\]

The resultant, as a polynomial in `d`, is

\[
(3a)^p\bigl(d+F(r)\bigr)\bigl(d+F(s)\bigr).
\]

Consequently,

\[
\sum_{d\in\mathbf F_p}
\chi\!\left(\varepsilon_p\operatorname{Res}(f,g)\right)
=
\begin{cases}
(p-1)\chi(\varepsilon_p3a),&F(r)=F(s),\\
-\chi(\varepsilon_p3a),&F(r)\ne F(s).
\end{cases}
\]

This is the standard quadratic-character sum for a quadratic polynomial in `d`, including the repeated-root case.

## 2. Exact collision criterion

Set

\[
\Delta=r-s.
\]

Using `r+s=-2b/(3a)` and `rs=u/(3a)`, direct simplification gives

\[
a(r^2+rs+s^2)+b(r+s)+u
=-\frac a2\Delta^2.
\]

Hence

\[
F(r)-F(s)
=
\Delta^p-\frac a2\Delta^3.
\]

The case `delta=0` is automatically a collision. Assume `delta` is nonzero. Since `Delta^2` lies in `F_p`,

\[
\Delta^p=\chi(\delta)\Delta.
\]

Therefore

\[
F(r)=F(s)
\iff
\Delta^{p-3}=\frac a2
\iff
2\delta=9a\chi(\delta).
\]

The possible nonzero collision values are thus

\[
\delta=\frac{9a}{2}
\quad\text{with}\quad
\chi(2a)=+1,
\]

and

\[
\delta=-\frac{9a}{2}
\quad\text{with}\quad
\chi(-2a)=-1.
\]

Let

\[
n(a)
=
\mathbf1_{\chi(2a)=1}
+
\mathbf1_{\chi(-2a)=-1}
\]

be the number of nonzero collision values for fixed `a`.

For each fixed `a` and each fixed `delta`, the equation

\[
\delta=b^2-3au
\]

has exactly `p` solutions `(b,u)`, one for each `b`. Including `delta=0`, the number of collision pairs is `p(1+n(a))`.

Substitution into the two-valued `d`-sum yields the exact fixed-`a` contribution

\[
\boxed{
p^2\chi(\varepsilon_p3a)n(a).
}
\]

## 3. Summation over `a`

If `chi(-1)=1`, then exactly one of `chi(2a)=1` and `chi(-2a)=-1` holds, so

\[
n(a)=1
\]

for every nonzero `a`. The remaining sum is a complete nontrivial quadratic-character sum over `a`, hence is zero.

If `chi(-1)=-1`, then the two conditions coincide. Thus

\[
n(a)=
\begin{cases}
2,&\chi(2a)=1,\\
0,&\chi(2a)=-1.
\end{cases}
\]

There are `(p-1)/2` admissible values, and on them `chi(a)=chi(2)`. Therefore

\[
S_{\mathrm{sgn}}(p)
=p^2(p-1)\chi(6\varepsilon_p).
\]

In this case `p` is `3 mod 4`, so `epsilon_p=-1`, giving

\[
S_{\mathrm{sgn}}(p)=\chi(-6)p^2(p-1).
\]

This proves Theorem 0.1.

## 4. Consequence for the aggregate Sawin programme

Remove the trivial and sign hooks from the alternating-hook decomposition and write

\[
\pi_+^{\mathrm{mid}}
=
\bigoplus_{\substack{2\le i\le p-3\\i\ \mathrm{even}}}
\bigwedge^i\operatorname{Std}_p,
\qquad
\pi_-^{\mathrm{mid}}
=
\bigoplus_{\substack{1\le i\le p-2\\i\ \mathrm{odd}}}
\bigwedge^i\operatorname{Std}_p.
\]

Let

\[
B_{\mathrm{mid}}
=B(\pi_+^{\mathrm{mid}})+B(\pi_-^{\mathrm{mid}}).
\]

The full von Mangoldt sum has the exact decomposition

\[
\boxed{
\sum_{f\in\mathcal I_4}\Lambda(f)
=p^4+S_{\mathrm{sgn}}(p)+E_{\mathrm{mid}},
}
\]

with Sawin's estimate

\[
|E_{\mathrm{mid}}|
\le B_{\mathrm{mid}}p^3.
\]

Assume the Betti-compatible comparison proves

\[
B_{\mathrm{mid}}\le p-1.
\]

Then:

- for `p congruent 5 or 17 mod 24`, the weighted sum is at least `p^3`, hence strictly exceeds `p^2`;
- for `p congruent 11 mod 24`, the explicit sign trace is positive and the lower bound is larger still;
- for `p congruent 23 mod 24`, the crude bound lands exactly at
  \[
  p^2.
  \]

Thus sign extraction closes three of the four admitted residue classes once the `p-1` mid-hook Betti budget is proved. The sole marginal sector is

\[
\boxed{p\equiv23\pmod{24}.}
\]

There one needs only a strict nonsaturation statement

\[
E_{\mathrm{mid}}>-(p-1)p^3,
\]

rather than a wholesale improvement of the Betti count. Sufficient substitutes include:

1. `B_mid<=p-2`;
2. one lower-weight constituent;
3. one Frobenius phase not aligned with the extremal negative Tate phase;
4. an exact congruence excluding equality.

Equality in the crude triangle bound would force every one of the `p-1` remaining units of Betti mass to occur at maximal weight and with the same extremal Frobenius phase. The marginal theorem is therefore a rigidity/non-saturation problem, not another full Betti collapse.

## 5. Verification

`sign_hook_full_interval_trace_verify.py` performs two independent checks.

1. It verifies the collision-count derivation for every odd prime through `499`.
2. It computes the discriminant by an independent Sylvester-resultant determinant and exhaustively sums over all `p^4` polynomials at
   \[
   p=5,7,11,13,17,19,23.
   \]

Every value agrees with the theorem. In particular,

\[
S_{\mathrm{sgn}}(5)=0,
\quad
S_{\mathrm{sgn}}(11)=1210,
\quad
S_{\mathrm{sgn}}(17)=0,
\quad
S_{\mathrm{sgn}}(23)=-11638.
\]

The verifier also records and guards against the earlier implementation error in which one extra trailing zero accidentally changed the polynomial from degree `p` to degree `p+1`.
