# Balanced-certificate dispersion identity

Date: 28 July 2026  
Status: exact second-moment and shifted-product identities proved; a previous standalone Fortune-scale interpretation of the diagonal is retracted.

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

The inequality `h!=0` follows because a prime `q>H` cannot divide two distinct
outputs in an interval of length `H`.  Moreover

\[
q\le k,\qquad r\le\ell,
\qquad P^-(k)\ge q,
\qquad P^-(\ell)\ge r.
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

Thus the balanced certificate has a fixed-complexity shifted-product
parametrisation.  This is an exact structural result, not yet a variance theorem
for the centred Fortune detector.

## 4. Absolute diagonal bound

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

Equation (4.2) is a correct absolute estimate.  It must not be compared directly
with the `NHX` variance scale of the one-sided von Mangoldt detector unless the
weights and centring define that same detector.

In particular:

1. for prime-count or `log p` certificate weights, the prime-output main term is
   much smaller than the one-sided von Mangoldt main term;
2. for the double-von-Mangoldt normalization, the natural certificate weights
   also contain a factor of size `log P_j asymp X`;
3. the balanced count is a large component in an exact subtraction identity, not
   the centred detector residual itself.

Therefore the former conclusion that the balanced diagonal was automatically
below the load-bearing Fortune scale is retracted.  The diagonal, off-diagonal,
small-certificate sector, total candidate mass and centring must be combined
before estimation.

## 5. Exact centred identity for the certificate alone

Let `beta_j` be any deterministic sequence.  Algebraically,

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

This identity is exact, but an arbitrary `beta_j` is not the Fortune principal
term.  The load-bearing centring comes only after the balanced certificate is
reinserted into the complete signed source or the exact prime/composite
subtraction identity.

## 6. Scale decomposition

For dyadic `Q,R>H`, let `mathcal O_X(Q,R;h)` denote the contribution to (3.3)
with

\[
q\asymp Q,
\qquad
r\asymp R.
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

1. **near-physical least factors**, `Q` or `R` polynomially close to `H`;
2. **intermediate factors**, where reciprocal completion can create bilinear or
   trilinear Kloosterman-fraction phases;
3. **exponential factors**, where the primorial shrinking-target theorem bounds
   the centre multiplicity of each fixed column.

This partition is diagnostic.  It is not permission to majorise the positive
certificate sectors separately.

## 7. Correct load-bearing placement

Let `mathcal N_j` denote the exact one-new-prime small-modulus term,
`mathcal L_j` the signed large-divisor Möbius term, and `mu_j^red` the exact
reduced principal term after subtraction of the deterministic smooth sector.  The
actual residual is

\[
\boxed{
R_j=\mathcal N_j+\mathcal L_j-\mu_j^{\mathrm{red}}.
}
\tag{7.1}
\]

The Fortune programme requires a bound for

\[
\boxed{
\sum_j|R_j|^2,
}
\tag{7.2}
\]

not a separate bound for `C_j^bal`.  Expanding (7.2) retains

\[
\sum_j|\mathcal N_j|^2,
\quad
\sum_j|\mathcal L_j|^2,
\quad
2\operatorname{Re}\sum_j\mathcal N_j\overline{\mathcal L_j},
\]

and all baseline cross terms.  The large cancellations observed in the exact
finite decomposition occur across these terms.

The least-factor identity and (3.3) remain useful for organising the parity
sector, but the next theorem must be a **joint signed cross-sector covariance
estimate** for (7.2).

## 8. Boundary

Proved:

1. exact diagonal/off-diagonal expansion (2.1);
2. exact shifted-product parametrisation (3.3);
3. absolute diagonal estimate (4.2);
4. exact certificate-centred identity (5.1);
5. exact identification of the certificate's place inside the full signed
   residual.

Retracted:

1. comparison of (4.2) with `NHX` as though the certificate and one-sided
   von Mangoldt detectors had the same normalization;
2. the claim that a balanced-sector off-diagonal estimate alone would close the
   Fortune variance theorem.

Computationally supported:

1. the balanced sector is substantial in complete finite candidate panels;
2. proper prime powers are absent in those panels;
3. the signed large-divisor component can be either positive or negative and is
   of main-term size in small blocks.

Open:

1. the joint signed covariance estimate for (7.2);
2. its reciprocal/shifted-product reduction without coefficient erasure;
3. Fortune's conjecture.
