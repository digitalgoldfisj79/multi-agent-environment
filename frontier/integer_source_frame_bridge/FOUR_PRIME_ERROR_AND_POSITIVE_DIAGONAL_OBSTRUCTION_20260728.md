# Four-prime error and the positive-diagonal obstruction

Date: 28 July 2026  
Status: exact variance expansion and method-level obstruction proved; required signed correlation theorem open.

## 1. Double source and exact second moment

Let

\[
T_j(H)=\sum_{2\le m\le H}\Lambda(m)\Lambda(P_j+m),
\qquad
\nu_j=H\mathfrak S_2(P_j),
\]

and write

\[
a_j(m)=\Lambda(m)\Lambda(P_j+m)\mathbf1_{[2,H]}(m).
\]

Then, exactly,

\[
\boxed{
|T_j-\nu_j|^2
 =\sum_{m=2}^{H}a_j(m)^2
  +\sum_{0<|h|<H}\sum_m a_j(m)a_j(m+h)
  -2\nu_jT_j+\nu_j^2,
}
\tag{1.1}
\]

where the inner sum is over `m,m+h in [2,H]`.

The off-diagonal product is

\[
a_j(m)a_j(m+h)
 =\Lambda(m)\Lambda(P_j+m)
  \Lambda(m+h)\Lambda(P_j+m+h).
\tag{1.2}
\]

The note `PRIMORIAL_PAIR_OF_PAIRS_SINGULAR_SERIES_AVERAGE_20260728.md`
proves that the deterministic four-form singular-series principal term in the
second sum cancels `nu_j^2` after triangular averaging, with aggregate error
negligible at the Fortune variance scale.

What remains is the actual signed correlation error together with the first
moment error in `T_j-nu_j`.

## 2. Required aggregate theorem

A sufficient double-source theorem is

\[
\boxed{
\sum_{j<N}|T_j(H)-\nu_j|^2
 \ll NHX(\log X)^2L(X),
 \qquad L(X)=o(\log X).
}
\tag{2.1}
\]

By corrected Paper II, this excludes every failed centre.

After subtracting the principal series, (2.1) asks for a signed aggregate bound
on

\[
\begin{aligned}
\mathcal E_4={}&
\sum_{j<N}\sum_{0<|h|<H}\sum_m
\bigl[
 \Lambda(m)\Lambda(P_j+m)
 \Lambda(m+h)\Lambda(P_j+m+h)\\
&\hspace{45mm}-\mathfrak S_4(P_j,h)
\bigr]
\end{aligned}
\tag{2.2}
\]

coupled to the diagonal and first-moment terms in (1.1).  A convenient stronger
but not necessary target is

\[
|\mathcal E_4|
 \ll NHX(\log X)^2o(\log X).
\tag{2.3}
\]

The word `signed` is essential: (1.1) permits cancellation between the
four-prime covariance, the diagonal, and `-2 nu_j T_j`.

## 3. Size of the positive diagonal

The diagonal is

\[
\mathcal D_j
 =\sum_{m\le H}\Lambda(m)^2\Lambda(P_j+m)^2.
\tag{3.1}
\]

The Hardy--Littlewood scale is

\[
\mathcal D_j\asymp HX(\log X)^2.
\tag{3.2}
\]

Indeed, the expected number of prime pairs is

\[
\asymp
\frac{\mathfrak S_2(P_j)H}{\log H\log P_j}
\asymp\frac{H}{X},
\]

and each prime-pair term in (3.1) has weight

\[
(\log m)^2(\log(P_j+m))^2
\asymp X^2(\log X)^2.
\]

Thus the diagonal itself naturally occupies the random variance scale in (2.1).

## 4. What a standard positive sieve gives

A dimension-two upper-bound sieve for the two linear forms

\[
m,\qquad m+P_j
\]

at length `H` gives at best the classical scale

\[
\#\{m\le H:m\text{ and }P_j+m\text{ prime}\}
 \ll \frac{\mathfrak S_2(P_j)H}{(\log H)^2}
 \ll\frac{H}{\log X}.
\tag{4.1}
\]

Using the maximal prime weights in (3.1), this yields only

\[
\boxed{
\mathcal D_j
 \ll H X^2\log X.
}
\tag{4.2}
\]

The desired scale is

\[
HX(\log X)^2.
\]

Therefore (4.2) is too large by the factor

\[
\boxed{
\frac{X}{\log X}.
}
\tag{4.3}
\]

The same loss appears if one treats the two prime conditions independently or
uses only a Brun--Titchmarsh bound in the output interval: those methods see the
length `H` but not the full output logarithm `log P_j asymp X`.

## 5. Positive-decomposition no-go

### Proposition 5.1

Any proof of (2.1) that first replaces every term of (1.1) by a nonnegative
majorant and then controls the diagonal by the standard dimension-two sieve
scale (4.1) cannot reach the Fortune variance threshold.  It loses at least the
factor `X/log X` before the off-diagonal terms are considered.

### Proof

The diagonal is a nonnegative subexpression of such a majorant.  Equations
(4.1)--(4.2) give its available upper-bound scale.  Dividing by the required
per-centre scale `HX(log X)^2` gives `X/log X`.  \(\square\)

This is a no-go for a specified proof architecture, not a lower bound on the
true diagonal and not an impossibility theorem for (2.1).

## 6. Consequences for method selection

A successful proof must do at least one of the following:

1. prove a genuinely short-interval prime-pair upper bound at the expected
   `H/X` scale for the primorial centres;
2. retain signed cancellation among the diagonal, off-diagonal covariance, and
   first-moment term throughout a Heath--Brown/Vaughan decomposition;
3. exploit averaging over the primorial index `j` before absolute values;
4. find a source whose diagonal is analytically accessible without reintroducing
   the parity loss.

The double-von-Mangoldt source makes the principal series exact and symmetric,
but does not remove the core prime-correlation difficulty.

The one-sided source has the same underlying issue in less symmetric form: a
positive treatment of its centred energy cannot manufacture the missing output
logarithm.

## 7. Current theorem boundary

Closed:

1. corrected detector implication;
2. exact residual-preserving source-to-frame map;
3. unconditional complete-modulus lower frame;
4. deterministic pair-of-pairs singular-series covariance.

Open:

1. a signed aggregate four-prime/first-moment correlation theorem at scale
   `NHX(log X)^2 o(log X)`;
2. equivalently, a centred source-energy theorem strong enough to exclude every
   failed primorial centre.

The old unweighted frame, HTE4, and Paper IV derandomisation do not address the
factor `X/log X` in Proposition 5.1 and remain secondary.

Fortune's conjecture remains open.