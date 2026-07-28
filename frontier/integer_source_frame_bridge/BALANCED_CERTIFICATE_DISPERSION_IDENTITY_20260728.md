# Balanced-certificate dispersion identity

Date: 28 July 2026  
Status: exact second-moment identity and diagonal estimate proved; off-diagonal covariance estimate open.

## 1. Setup

Let `P_j` range over the primorial centres in a dyadic block, let `z_j` be the
largest prime dividing `P_j`, and choose a common physical cutoff `H` satisfying

\[
z_j<H<(z_j^+)^2
\]

for every centre under consideration.  Put

\[
\mathcal P_j(H)=\{p:z_j<p\le H,\ p\text{ prime}\}.
\]

For a prime `q>H`, define

\[
k_j(q)=\left\lceil\frac{P_j}{q}\right\rceil,
\qquad
p_j(q)=qk_j(q)-P_j.
\tag{1.1}
\]

Let `b_{j,p}` be arbitrary complex weights on `mathcal P_j(H)`.  Define

\[
A_j(q)=
 b_{j,p_j(q)}
 \mathbf1_{q\le\sqrt{P_j+H}}
 \mathbf1_{p_j(q)\in\mathcal P_j(H)}
 \mathbf1_{P^-(k_j(q))\ge q},
\tag{1.2}
\]

where `P^-(1)=+infinity`, and set

\[
C_j^{\mathrm{bal}}=\sum_{q>H\atop q\text{ prime}}A_j(q).
\tag{1.3}
\]

By the balanced least-factor theorem, this counts each prime-offset output whose
least prime factor exceeds `H` exactly once.

## 2. Exact second moment

### Theorem 2.1

One has

\[
\boxed{
\sum_j|C_j^{\mathrm{bal}}|^2
=
\mathcal D_X(b)+\mathcal O_X(b),
}
\tag{2.1}
\]

where

\[
\mathcal D_X(b)
=
\sum_j\sum_{q>H\atop q\text{ prime}}|A_j(q)|^2
\tag{2.2}
\]

and

\[
\mathcal O_X(b)
=
\sum_j
\sum_{q\ne r\atop q,r>H\text{ prime}}
A_j(q)\overline{A_j(r)}.
\tag{2.3}
\]

This is the literal diagonal/off-diagonal expansion of (1.3).

## 3. Shifted-product form of the off-diagonal

Whenever a summand in (2.3) is active, put

\[
p=p_j(q),\quad p'=p_j(r),\quad
k=k_j(q),\quad \ell=k_j(r).
\]

Then

\[
qk=P_j+p,
\qquad
r\ell=P_j+p',
\]

and hence

\[
\boxed{
qk-r\ell=h,
\qquad
h=p-p',
\qquad
0<|h|<H.
}
\tag{3.1}
\]

The inequality `h ne 0` follows because `q>H`: a fixed modulus cannot divide two
distinct outputs in an interval of length `H`.  Moreover

\[
q\le k,\qquad r\le\ell,
\qquad P^-(k)\ge q,\qquad P^-(\ell)\ge r.
\tag{3.2}
\]

### Theorem 3.1 (exact shifted-product identity)

Let `mathcal P_X={P_j}` be the centre set.  Then

\[
\boxed{
\begin{aligned}
\mathcal O_X(b)
={}&
\sum_{0<|h|<H}
\sum_{p-p'=h\atop p,p'\text{ prime}}
\sum_{q,r>H\atop q\ne r\text{ prime}}
\sum_{k,\ell\ge1}
 b_{qk-p,p}\,\overline{b_{r\ell-p',p'}}\\
&\times
\mathbf1_{qk-p=r\ell-p'\in\mathcal P_X}
\mathbf1_{q\le k}\mathbf1_{r\le\ell}
\mathbf1_{P^-(k)\ge q}
\mathbf1_{P^-(\ell)\ge r}.
\end{aligned}
}
\tag{3.3}
\]

Here `b_{P,p}` means the weight attached to offset `p` at the unique centre `P`,
and is zero when `P` is not in the block or `p` is outside its candidate range.

### Proof

Map every active ordered pair `(j,q,r)` in (2.3) to

\[
(h,p,p',q,r,k,\ell).
\]

Equations (1.1)--(1.2) give every displayed condition.  Conversely, a tuple in
(3.3) determines the common centre `P=qk-p=r\ell-p'` and hence the unique index
`j`; the least-factor conditions recover the two active certificate columns.
The correspondence is bijective.  \(\square\)

Thus the remaining covariance is a fixed-complexity shifted-product problem.  No
Möbius subset sum or growing convolution depth remains.

## 4. The diagonal is below the Fortune scale

Assume

\[
|b_{j,p}|\le B_X.
\]

For a fixed centre, a balanced certificate is attached to one candidate prime
offset, and each offset has at most one least prime factor.  Therefore

\[
\mathcal D_X(b)
\le
B_X^2\sum_j|\mathcal P_j(H)|.
\tag{4.1}
\]

By the prime number theorem,

\[
|\mathcal P_j(H)|\ll\frac H{\log H}
\]

uniformly in the dyadic block.  Hence

\[
\boxed{
\mathcal D_X(b)
\ll
B_X^2\frac{NH}{\log H}.
}
\tag{4.2}
\]

For the natural prime-offset weights `B_X ll log H`,

\[
\boxed{
\mathcal D_X(b)
\ll NH\log H
=o(NHX).
}
\tag{4.3}
\]

Thus the diagonal cannot be the obstruction to the required Fortune-scale second
moment.

## 5. Centred identity

Let `beta_j` be any deterministic centring sequence.  Then

\[
\boxed{
\begin{aligned}
\sum_j|C_j^{\mathrm{bal}}-\beta_j|^2
={}&\mathcal D_X(b)+\mathcal O_X(b)\\
&-2\operatorname{Re}\sum_j\overline{\beta_j}C_j^{\mathrm{bal}}
+\sum_j|\beta_j|^2.
\end{aligned}
}
\tag{5.1}
\]

No sector may be bounded independently before the last three terms are combined:
the principal pair contribution in `mathcal O_X` must cancel the centring terms.

## 6. Scale decomposition

For dyadic `Q,R>H`, let `mathcal O_X(Q,R;h)` denote the contribution to (3.3)
with

\[
q\asymp Q,\qquad r\asymp R.
\]

Then

\[
\boxed{
\mathcal O_X(b)
=
\sum_{0<|h|<H}
\sum_{Q,R}\mathcal O_X(Q,R;h).
}
\tag{6.1}
\]

The ranges have different available structure:

1. **near-physical least factors**, `Q` or `R` polynomially close to `H`, where
   prime-modulus dispersion must supply cancellation;
2. **intermediate factors**, where reciprocal completion produces bilinear or
   trilinear Kloosterman-fraction phases;
3. **exponential factors**, where the primorial shrinking-target theorem bounds
   the centre multiplicity of each fixed column.

A proof must retain the signed/centred sum across these ranges; (6.1) is a
partition, not permission to replace each part by a positive majorant.

## 7. Load-bearing theorem

The remaining balanced-sector theorem is now precisely an off-diagonal covariance
estimate for (3.3).  A sufficient form is

\[
\boxed{
\mathcal O_X(b)
-2\operatorname{Re}\sum_j\overline{\beta_j}C_j^{\mathrm{bal}}
+\sum_j|\beta_j|^2
\ll NHX\,L(X),
\quad L(X)=o(\log X),
}
\tag{7.1}
\]

because the diagonal (4.3) is already smaller.  The exact centring `beta_j` must
come from the combined small-certificate and balanced-certificate principal term;
it is not inserted heuristically.

## 8. Boundary

Proved:

1. exact diagonal/off-diagonal expansion (2.1);
2. exact shifted-product parametrisation (3.3);
3. diagonal estimate (4.2)--(4.3);
4. exact centred identity (5.1);
5. reduction of the balanced obstruction to off-diagonal covariance.

Computationally supported:

1. the balanced sector is substantial in complete finite candidate panels;
2. proper prime powers are absent in those panels.

Open:

1. the principal term for the shifted-product covariance;
2. the off-diagonal estimate (7.1);
3. its signed coupling to the one-new-prime small-modulus sector;
4. Fortune's conjecture.
