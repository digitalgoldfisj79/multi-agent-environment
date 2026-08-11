# Single-prime dilation layer and the lower-band logarithmic gap

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the complete conductor-`p` dilation layer has been collapsed exactly to a first-order local survivor martingale defect. Its leading arithmetic form is exactly a one-residue prime-distribution discrepancy. The generic multiplicative large sieve reaches `KHX log X`, while the Fortune variance programme requires `KHX L(X)` with `L(X)=o(log X)`. The collision/noncollision split cannot be estimated independently without discarding load-bearing cancellation. Fortune's conjecture remains **OPEN**.

## 1. Purpose

The preceding four-point calculation proved that the low dilation spectrum is exactly

\[
\operatorname{cond}\theta=p,\qquad p\in\mathcal P_R,
\]

and gave the individual coefficients

\[
\mathcal D_\theta(r).
\]

Their complete-model energy is concentrated at

\[
p\mid mP_k-nP_j.
\]

The next proposed attack was to retain the full `\theta`-sum, use a vector-valued multiplicative large sieve away from collisions, and apply Linnik dispersion on the collision set. This note carries out the algebra before any inequality is applied.

The result is more rigid: after the nonprincipal characters modulo `p` are summed, the character oscillation disappears. The low layer is the first-order Hoeffding/martingale projection of the pair survivor process. Its leading term is a centred count in one residue class modulo `p`.

## 2. Local factors

For `z\in\mathbb F_p^\times`, put

\[
s_p(z)=\frac{p-1}{p-2}\mathbf1_{z\ne1},
\qquad
\xi_p(z)=s_p(z)-1.
\tag{2.1}
\]

Thus

\[
\xi_p(z)=
\begin{cases}
-1,&z=1,\\[3pt]
\dfrac1{p-2},&z\ne1.
\end{cases}
\tag{2.2}
\]

For `r\in\mathbb F_p^\times`, define the complete local covariance

\[
\kappa_p(r)
=
\mathbb E_{u\in\mathbb F_p^\times}
\xi_p(ru)\xi_p(u)
=
\begin{cases}
\dfrac1{p-2},&r=1,\\[6pt]
-\dfrac1{(p-2)^2},&r\ne1.
\end{cases}
\tag{2.3}
\]

For a full band, write

\[
\kappa_{-p}(r)
=
\prod_{\substack{q\in\mathcal P_R\\q\ne p}}
\left(1+\kappa_q(r_q)\right)-1.
\tag{2.4}
\]

This is the complete common-dilation covariance of the band with the coordinate `p` deleted.

## 3. Exact conductor-`p` conditional projection

Let

\[
\mathcal L_p(r,y)
=
\sum_{\substack{\theta\ne1\\\operatorname{cond}\theta=p}}
\mathcal D_\theta(r)\theta(y_p).
\tag{3.1}
\]

### Theorem 3.1 — first-order conditional projection

For every `r,y\in\Omega_R`,

\[
\boxed{
\mathcal L_p(r,y)
=
\mathbb E_{u_{-p}}
\left[
g_R(r_py_p,r_{-p}u_{-p})
g_R(y_p,u_{-p})
\right]
-
\mathcal K_R(r).
}
\tag{3.2}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
\mathcal L_p(r,y)
={}&
\left[
\xi_p(r_py_p)\xi_p(y_p)-\kappa_p(r_p)
\right]\\
&+
\kappa_{-p}(r)
\left[
s_p(r_py_p)s_p(y_p)
-\left(1+\kappa_p(r_p)\right)
\right].
\end{aligned}
}
\tag{3.3}
\]

### Proof

The sum in (3.1) is exactly the nonprincipal Fourier projection in the coordinate `y_p`. Average the pair product over every other coordinate. Since

\[
S_R(y)=s_p(y_p)S_{-p}(y_{-p}),
\qquad
g_R=S_R-1,
\]

and

\[
\mathbb E S_{-p}=1,
\qquad
\mathbb E S_{-p}(r_{-p}u)S_{-p}(u)=1+\kappa_{-p}(r),
\]

the conditional expectation is

\[
(1+\kappa_{-p})s_p(r_py_p)s_p(y_p)
-s_p(r_py_p)-s_p(y_p)+1.
\]

Subtracting

\[
\mathcal K_R(r)
=
(1+\kappa_{-p}(r))(1+\kappa_p(r_p))-1
\]

gives (3.3). `\square`

The first line of (3.3) is the purely local deterministic-point defect. The second line is the exact reduced-band correction.

## 4. Endpoint formula after summing the characters

Put

\[
H_p(z)
=
\sum_{\substack{\theta\bmod p\\\theta\ne1}}\theta(z)
=
\begin{cases}
p-2,&z=1,\\
-1,&z\ne1.
\end{cases}
\tag{4.1}
\]

Let

\[
x_p=r_py_p.
\]

The individual-mode formulas from the preceding note now sum exactly.

### Theorem 4.1 — endpoint collapse

If `r_p\ne1`, then

\[
\boxed{
\mathcal L_p(r,y)
=
-\frac{1+(p-1)\kappa_{-p}(r)}{(p-2)^2}
\left(H_p(x_p)+H_p(y_p)\right).
}
\tag{4.2}
\]

If `r_p=1`, then

\[
\boxed{
\mathcal L_p(r,y)
=
\frac{p-3-(p-1)\kappa_{-p}(r)}{(p-2)^2}
H_p(y_p).
}
\tag{4.3}
\]

The proof is nonprincipal character orthogonality:

\[
\sum_{\theta\ne1}\theta(z)=H_p(z).
\]

For arithmetic source-centre points,

\[
x_{j,m,p}\equiv -mP_j^{-1}\pmod p,
\]

so

\[
x_{j,m,p}=1
\iff
p\mid P_j+m.
\tag{4.4}
\]

Thus the completed conductor-`p` sum is governed by the endpoint hit events

\[
p\mid P_j+m,\qquad p\mid P_k+n.
\]

The collision condition

\[
p\mid mP_k-nP_j
\]

determines whether the two forbidden endpoint residues coincide, but it is not the support of the completed low layer.

## 5. Exact local residue discrepancy

For fixed `j,p`, let `a_{j,m}` be any weights supported on source integers coprime to `p`. Then

\[
E_{j,p}
=
\sum_m a_{j,m}\xi_p(x_{j,m,p}).
\tag{5.1}
\]

Put

\[
A_{j,p}
=
\sum_{(m,p)=1}a_{j,m},
\qquad
A_{j,p}(a)
=
\sum_{m\equiv a\pmod p}a_{j,m}.
\]

### Theorem 5.1 — one-residue discrepancy identity

\[
\boxed{
E_{j,p}
=
-\frac{p-1}{p-2}
\left[
A_{j,p}(-P_j)
-\frac{A_{j,p}}{p-1}
\right].
}
\tag{5.2}
\]

### Proof

The local factor is `-1` on the residue `m\equiv-P_j` and `1/(p-2)` on every other unit residue. Hence

\[
E_{j,p}
=
-A_{j,p}(-P_j)
+
\frac{A_{j,p}-A_{j,p}(-P_j)}{p-2},
\]

which is (5.2). `\square`

Equivalently, using multiplicative characters,

\[
\boxed{
E_{j,p}
=
-\frac1{p-2}
\sum_{\substack{\chi\bmod p\\\chi\ne\chi_0}}
\overline{\chi(-P_j)}
\sum_m a_{j,m}\chi(m).
}
\tag{5.3}
\]

The leading low-mode problem is therefore not an unspecified character tensor. It is a weighted Barban--Davenport--Halberstam problem for one moving residue class, at prime moduli `p\asymp X`, with the preceding survivor history inside `a_{j,m}`.

## 6. Quadratic form

For source-centre coefficients `b_\alpha`, `\alpha=(j,m)`, the purely local part of the conductor-`p` layer is

\[
\boxed{
\sum_{\alpha,\beta}
b_\alpha\overline{b_\beta}
\left[
\xi_p(x_\alpha)\xi_p(x_\beta)
-\kappa_p(x_\alpha x_\beta^{-1})
\right]
=
\left|\sum_\alpha b_\alpha\xi_p(x_\alpha)\right|^2
-
\sum_{\alpha,\beta}
b_\alpha\overline{b_\beta}
\kappa_p(x_\alpha x_\beta^{-1}).
}
\tag{6.1}
\]

The second term is the complete local model energy. The first is the actual one-residue discrepancy.

The remaining exact correction is

\[
\kappa_{-p}(x_\alpha x_\beta^{-1})
\left[
s_p(x_\alpha)s_p(x_\beta)
-
\left(1+\kappa_p(x_\alpha x_\beta^{-1})\right)
\right].
\tag{6.2}
\]

It retains the covariance with all other band coordinates. It cannot be dropped merely because `\kappa_{-p}` is small in complete-model energy: deterministic point evaluation of the first-order spectrum is unbounded for arbitrary weights.

## 7. Standard large-sieve gate

From (5.3) and Cauchy--Schwarz,

\[
|E_{j,p}|^2
\le
\frac1{p-2}
\sum_{\chi\ne\chi_0\bmod p}
\left|\sum_m a_{j,m}\chi(m)\right|^2.
\tag{7.1}
\]

For `p\asymp X` and source length `H`, the multiplicative large sieve gives

\[
\boxed{
\sum_{p\asymp X}|E_{j,p}|^2
\ll
\frac{H+X^2}{X}
\sum_m|a_{j,m}|^2.
}
\tag{7.2}
\]

At the Fortune scale

\[
H=\eta X^2,
\]

and already for the unsieved logarithmic prime source,

\[
\sum_m|a_{j,m}|^2\ll H\log H.
\]

Therefore the generic bound is

\[
\boxed{
\sum_{j\in B}\sum_{p\asymp X}|E_{j,p}|^2
\ll
KHX\log X.
}
\tag{7.3}
\]

The normalized-survivor target is

\[
KHX\,L(X),
\qquad
L(X)=o(\log X).
\tag{7.4}
\]

Thus the standard large sieve reaches the correct polynomial scale but misses the required theorem by one logarithm. The earlier survivor weights do not supply this saving automatically; they are the principal additional dependence that must be preserved.

This is the decisive lower-band gate:

- generic large-sieve/BDH input gives `log X`;
- Fortune requires a strict `o(log X)` improvement;
- taking absolute values across the local drift and hit terms destroys the only visible mechanism for such a saving.

## 8. Collision/noncollision verdict

The complete-model energy of the individual `\theta` modes is concentrated at

\[
p\mid mP_k-nP_j.
\]

After the `\theta`-sum is performed, however, (4.2)--(4.3) show that both collision and noncollision terms contain the endpoint drift/hit cancellation. They are not independent positive pieces.

The exact 51-point arithmetic panel with

\[
\mathcal P_R=\{13,17,19\},
\quad
P_j\in\{30,210,2310\},
\]

and prime sources `23\le m\le97` gives

\[
\mathcal L_{\rm total}
=
-\frac{516138}{874225}
\approx-0.590395,
\]

while

\[
\mathcal L_{\rm coll}
=
-\frac{2345818}{174845}
\approx-13.4166,
\]

and

\[
\mathcal L_{\rm noncoll}
=
\frac{11212952}{874225}
\approx12.8262.
\]

Hence

\[
\frac{
|\mathcal L_{\rm coll}|+|\mathcal L_{\rm noncoll}|
}{
|\mathcal L_{\rm total}|
}
=
\frac{11471021}{258069}
\approx44.45.
\]

This is a finite exact warning, not an asymptotic theorem: separate positive estimates can discard more than an order of magnitude of cancellation even on the first nontrivial arithmetic panel.

Consequently the proposed route

> multiplicative large sieve on noncollisions, plus positive collision dispersion

is not a valid decomposition unless the two estimates preserve their signed interface.

## 9. Sharp first-order arbitrary-weight obstruction

The first-order dilation space is

\[
\bigoplus_{p\in\mathcal P_R}
\operatorname{span}\{\theta:\operatorname{cond}\theta=p\}.
\]

Its dimension is

\[
\boxed{
d_1(R)=\sum_{p\in\mathcal P_R}(p-2).
}
\tag{9.1}
\]

On normalized `L^2(\Omega_R)`, point evaluation on this subspace has squared norm exactly `d_1(R)`. Thus even the low spectrum alone has no bounded arbitrary-weight model-to-point transfer.

For the panel `[13,17,19]`,

\[
d_1=11+15+17=43.
\]

Any proof must use the actual prime source, moving residue `-P_j`, and previous-band survivor weights.

## 10. Precise remaining theorem

### Open theorem `SW1BDH(X)` — survivor-weighted one-residue BDH with logarithmic saving

For the actual preceding-band coefficients `A^{<R}_{j,m}` and prime moduli `p\in\mathcal P_R`, `R\asymp X`, prove

\[
\boxed{
\sum_{j\in B}
\sum_{p\in\mathcal P_R}
\left|
\sum_m
A^{<R}_{j,m}
\xi_p(-mP_j^{-1})
\right|^2
\ll
KHX\,L(X),
\qquad
L(X)=o(\log X),
}
\tag{10.1}
\]

jointly with the reduced-band correction (6.2), the self-coordinate terms and the zeroth coordinate.

By (5.2), this is equivalently a logarithmically improved variance theorem for

\[
\sum_{\substack{m\\m\equiv-P_j\pmod p}}
A^{<R}_{j,m}
-
\frac1{p-1}
\sum_{(m,p)=1}A^{<R}_{j,m}.
\tag{10.2}
\]

`SW1BDH(X)` is the exact first-order lower-band component of `SMHLS(X)` / `PCRST(X)`. It is not yet the full Fortune variance theorem because higher dilation conductors and cross-band martingale covariance remain.

## 11. Verification

The committed verifier checks:

1. 1152 exact conditional-projection, tensor-decomposition and endpoint identities on the complete group for `[5,7]`;
2. 240 collision and 912 noncollision cases;
3. the exact weighted one-residue identity on a nonconstant rational source panel;
4. the sharp first-order point-evaluation norm;
5. the complete 51-point arithmetic decomposition into:
   - local residue discrepancy;
   - reduced-band correction;
   - collision part;
   - noncollision part.

## 12. Boundary

**PROVED EXACTLY**

1. conductor-`p` dilation modes are first-order conditional projections;
2. tensor decomposition into local discrepancy plus reduced-band correction;
3. endpoint character-sum formulas;
4. one-residue discrepancy identity;
5. local quadratic-form identity;
6. sharp first-order arbitrary-weight point-evaluation obstruction.

**PROVED FROM THE CLASSICAL MULTIPLICATIVE LARGE SIEVE**

1. the generic lower-band bound `KHX log X`.

**COMPUTATIONALLY VERIFIED EXACTLY**

1. every finite identity above;
2. large signed cancellation between collision and noncollision pieces on the frozen arithmetic panel.

**CLOSED AS A SEPARATE POSITIVE ROUTE**

1. a collision/noncollision triangle-inequality proof that does not retain their signed interface;
2. a generic large-sieve proof without an additional logarithmic saving mechanism;
3. arbitrary-weight transfer even after restriction to the first-order dilation spectrum.

**OPEN**

1. `SW1BDH(X)`, the survivor-weighted one-residue logarithmic-saving theorem;
2. the reduced-band correction at the same scale;
3. higher dilation conductors;
4. `SMHLS(X)` / `PCRST(X)`;
5. `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.
