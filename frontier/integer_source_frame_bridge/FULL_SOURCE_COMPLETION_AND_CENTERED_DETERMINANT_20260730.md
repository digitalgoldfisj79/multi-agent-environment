# Full-source completion and centred determinant reduction

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

## Status

The repaired sequence has been run through:

1. exact completion of the true long source cells;
2. exact resummation of the Heath--Brown coefficients;
3. exact determinant reordering of the physical prime-modulus diagonal;
4. actual-coefficient numerical calibration;
5. reinsertion into the complete Euler survivor.

The unbalanced-cell support flaw is closed at amplitude level. The resulting physical source is simpler than the provisional Möbius fourth-moment formulation: after all source cells are recombined, it is exactly the ordinary von Mangoldt progression discrepancy.

This does **not** prove the first physical-band theorem or Fortune's conjecture. It replaces the incorrect uncentred `SDD(X)` target by a centred prime-band Barban--Davenport--Halberstam theorem and leaves the signed higher-conductor recombination open.

## 1. Exact source coefficient

Let

\[
H=\eta X^2,\qquad 0<\eta<1,
\]

and

\[
Y=\lceil\sqrt H\rceil<X.
\]

Define

\[
c_Y(m)
=
\log m+(\mu_{>Y}*1*\log)(m).
\tag{1.1}
\]

The accepted two-level source identity is equivalent to

\[
\boxed{
\Lambda(n)
=
\sum_{\substack{d\mid n\\d\le Y}}
\mu(d)c_Y(n/d)
\qquad(n\le H).
}
\tag{1.2}
\]

The coefficient `c_Y` is independent of `d`; only the support condition `m\le H/d` varies with `d`. This point is essential. The sign-bearing large-variable arithmetic remains present in `c_Y`, but it recombines exactly to `Lambda` before any norm is taken.

## 2. Gate U0: exact completion of every long cell

Fix a first-band prime `p>X`. For `d\le Y` and `r\pmod p`, define the complete residue-block sum

\[
B_{d,p}(r)
=
\sum_{\substack{m\le H/d\\m\equiv r\pmod p}}c_Y(m).
\tag{2.1}
\]

This definition includes every complete `p`-block and the final remainder. No assumption `m<p` is made.

For every residue `a\pmod p`, exact source resummation gives

\[
\begin{aligned}
\sum_{d\le Y}\mu(d)B_{d,p}(a\bar d)
&=
\sum_{d\le Y}\mu(d)
\sum_{\substack{m\le H/d\\dm\equiv a\pmod p}}c_Y(m)\\
&=
\sum_{\substack{n\le H\\n\equiv a\pmod p}}\Lambda(n).
\end{aligned}
\]

Hence

\[
\boxed{
\sum_{d\le Y}\mu(d)B_{d,p}(a\bar d)
=
\psi(H;p,a).
}
\tag{2.2}
\]

For the Fortune centre, `a=-P_j`, and `a\bar d=-P_j/d\pmod p`; thus (2.2) is the completed punctured-centre formula.

### 2.1 Multiplicative dual form

Let

\[
\Psi_p(H)=\sum_{\substack{n\le H\\(n,p)=1}}\Lambda(n).
\]

For `a\ne0`, define

\[
D_p(a)
=
\psi(H;p,a)-\frac{\Psi_p(H)}{p-1}.
\tag{2.3}
\]

Character orthogonality gives

\[
\boxed{
D_p(a)
=
\frac1{p-1}
\sum_{\chi\ne\chi_0}
\overline{\chi(a)}
\sum_{n\le H}\Lambda(n)\chi(n).
}
\tag{2.4}
\]

The apparent Möbius-weighted character family completes exactly:

\[
\boxed{
\sum_{d\le Y}\mu(d)\chi(d)
\sum_{\substack{m\le H/d\\(m,p)=1}}
c_Y(m)\chi(m)
=
\sum_{n\le H}\Lambda(n)\chi(n).
}
\tag{2.5}
\]

Thus the long-cell repair does not produce a new arbitrary bilinear character coefficient. Once the actual source signs are retained, it produces the ordinary `Lambda` character sum.

### 2.2 Non-unit terms are exactly the known self coordinates

Since `p>X` and `H<X^2`,

\[
p^2>H.
\]

If `p\mid n\le H` and `\Lambda(n)\ne0`, then `n` is a power of `p`; therefore

\[
\boxed{
p\mid n,\ n\le H,\ \Lambda(n)\ne0
\iff n=p.
}
\tag{2.6}
\]

All non-unit source terms are therefore the already-known band-prime self coordinates. There is no residual long-cell non-unit family after full source recombination.

## 3. Exact first-order Fortune coordinate

Let

\[
w_p=\frac{p-1}{p-2}.
\]

For the first-order Euler coordinate

\[
A_{j,p}
=
\sum_{n\le H}\Lambda(n)
\left(
\frac1{p-2}-w_p\mathbf 1_{p\mid P_j+n}
\right),
\]

(2.3) and the self term (2.6) give

\[
\boxed{
A_{j,p}
=
-w_pD_p(-P_j)+\frac{\log p}{p-2}.
}
\tag{3.1}
\]

This is the corrected all-source version of the physical coordinate. It is valid on the true source range and contains the reduced-band drift explicitly.

## 4. Gate U1: exact centred determinant reordering

For a first-band prime set `\mathcal P_R`, define the full residue variance

\[
\mathcal V_{\mathcal P_R}(H)
=
\sum_{p\in\mathcal P_R}
\sum_{a\in\mathbb F_p^\times}
\left|
\psi(H;p,a)-\frac{\Psi_p(H)}{p-1}
\right|^2.
\tag{4.1}
\]

Expanding the square yields the exact identity

\[
\boxed{
\mathcal V_{\mathcal P_R}(H)
=
\sum_{p\in\mathcal P_R}
\sum_{\substack{n,n'\le H\\p\nmid nn'}}
\Lambda(n)\Lambda(n')
\left(
\mathbf 1_{p\mid n-n'}-\frac1{p-1}
\right).
}
\tag{4.2}
\]

After removing the self sources `n=p`, the unit condition is common across the entire band. Put

\[
\lambda_R=\sum_{p\in\mathcal P_R}\frac1{p-1}.
\]

For `n\ne n'`, one has `|n-n'|<H<X^2`. Two distinct first-band primes cannot divide `n-n'`. Consequently

\[
\sum_{p\in\mathcal P_R}\mathbf 1_{p\mid n-n'}
=
\mathbf 1_{\exists p\in\mathcal P_R:\ p\mid n-n'}.
\tag{4.3}
\]

The band-summed off-diagonal is therefore the single centred determinant kernel

\[
\boxed{
W_R(n-n')
=
\mathbf 1_{\exists p\in\mathcal P_R:\ p\mid n-n'}
-
\lambda_R.
}
\tag{4.4}
\]

The diagonal is

\[
\mathcal D_{\mathcal P_R}(H)
=
\sum_{p\in\mathcal P_R}
\left(1-\frac1{p-1}\right)
\sum_{\substack{n\le H\\p\nmid n}}\Lambda(n)^2.
\tag{4.5}
\]

Thus

\[
\mathcal V_{\mathcal P_R}(H)
=
\mathcal D_{\mathcal P_R}(H)
+
\sum_{n\ne n'}\Lambda(n)\Lambda(n')W_R(n-n')
+
\text{explicit self corrections}.
\tag{4.6}
\]

This is the authoritative determinant reordering. It includes the density subtraction. The uncentred hit indicator alone is not the required object.

## 5. Correction to the proposed `SDD(X)` target

The uncentred full-source hit form is

\[
\mathcal R_R(H)
=
\sum_{p\in\mathcal P_R}
\sum_{a\in\mathbb F_p^\times}
\psi(H;p,a)^2
-
\sum_{p\in\mathcal P_R}
\sum_{\substack{n\le H\\p\nmid n}}\Lambda(n)^2.
\tag{5.1}
\]

By Cauchy--Schwarz,

\[
\sum_{a\in\mathbb F_p^\times}\psi(H;p,a)^2
\ge
\frac{\Psi_p(H)^2}{p-1}.
\]

The prime number theorem and Mertens' theorem on a dyadic prime band imply

\[
\sum_{p\in\mathcal P_R}\frac{\Psi_p(H)^2}{p-1}
\asymp
\frac{H^2}{\log X},
\]

whereas the subtracted integer-product diagonal is `O(HX)`. Hence

\[
\boxed{
\mathcal R_R(H)
\gg
\frac{H^2}{\log X}
}
\tag{5.2}
\]

for a full dyadic first band and sufficiently large `X`.

At `H\asymp X^2`, this is polynomially larger than `H X^{o(1)}`. Therefore the uncentred displayed form of `SDD(X)` cannot be the load-bearing full-source theorem. A cellwise signed estimate may still be meaningful, but it cannot be recombined positively: the density term in (4.4) is indispensable.

## 6. Correct physical theorem

A sufficient all-residue physical estimate is the following.

### `PBDH_P(X)` — prime-band centred BDH at the square-root transition

For `H=\eta X^2` and a first dyadic prime band `\mathcal P_R` with `p\asymp X`, prove

\[
\boxed{
\mathcal V_{\mathcal P_R}(H)
\ll
HX\,X^{o(1)}.
}
\tag{6.1}
\]

The expected scale is `HX`; the finite panels are consistent with a bounded ratio.

The classical multiplicative large sieve gives

\[
\mathcal V_{\mathcal P_R}(H)
\ll
HX\log H,
\]

and therefore loses one logarithm. The sparse-modulus large sieve of Baier--Zhao has the same loss at `H\asymp X^2`: its `\sqrt H` term dominates the cardinality of the prime-modulus set. Their sparse BDH theorem gives arbitrary logarithmic savings from the `H^2` scale, but at `X\asymp\sqrt H` this remains polynomially above `HX`.

The general Montgomery--Hooley/Harper variance theorems average over all moduli and do not supply the prime-density saving required by (6.1). No directly applicable published theorem was identified that proves (6.1) for moduli restricted to the first-band primes.

## 7. Actual-coefficient diagnostics

The committed verifier checks the exact formal identities and then evaluates the actual von Mangoldt source.

On panels through `X=337`:

- `\mathcal V_{\mathcal P_R}(H)/(HX)` remains between approximately `0.36` and `0.69`;
- the energy sampled only at the logarithmic primorial-centre block is smaller still;
- the uncentred hit form is approximately `0.06`--`0.12` times `H^2`, confirming that it retains its density main term;
- the centred off-diagonal is negative and main-sized, cancelling a large part of the positive diagonal.

These are empirical observations, not asymptotic proofs.

## 8. Gate U3: coherent higher-conductor reinsertion

The fully recombined band coordinate is

\[
\mathcal F_{j,R}
=
\sum_{n\le H}\Lambda(n)
\,g_R(-nP_j^{-1}).
\tag{8.1}
\]

Equivalently, inclusion--exclusion gives

\[
\mathcal F_{j,R}
=
(V_R^{-1}-1)\psi(H)
+
V_R^{-1}
\sum_{\varnothing\ne S\subseteq\mathcal P_R}
(-1)^{|S|}
\sum_{\substack{n\le H\\Q_S\mid P_j+n}}\Lambda(n),
\tag{8.2}
\]

where

\[
Q_S=\prod_{p\in S}p.
\]

For `|S|\ge2`,

\[
Q_S>X^2>H,
\]

so the inner sum is a one-point value

\[
\Lambda(\rho_{j}(Q_S))
\]

when the unique representative lies in `[1,H]`, and zero otherwise.

Formula (8.2) is the exact physical/high-conductor interface after the source repair. The physical progression discrepancies, normalization drift and one-point higher-conductor terms still have to remain signed and coherent.

The verifier separates

\[
\mathcal F_{j,R}
=
\mathcal F^{(1)}_{j,R}
+
\mathcal F^{(\ge2)}_{j,R}
\]

and checks

\[
\sum_j|\mathcal F_{j,R}|^2
=
\sum_j|\mathcal F^{(1)}_{j,R}|^2
+
\sum_j|\mathcal F^{(\ge2)}_{j,R}|^2
+2\Re\sum_j
\mathcal F^{(1)}_{j,R}
\overline{\mathcal F^{(\ge2)}_{j,R}}.
\]

The cross term changes sign across the panels and is not negligible. Consequently `PBDH_P(X)` would close only the physical conductor diagonal; it does not justify a positive separation from the higher Euler orders.

## 9. Revised theorem boundary

### PROVED EXACTLY

- exact completion of every long `m`-cell modulo `p`;
- resummation of the completed cells to `psi(H;p,a)`;
- collapse of the Möbius character family to the ordinary `Lambda` character sum;
- exact isolation of `n=p` as the only non-unit source;
- the centred determinant identity (4.2)--(4.6);
- the at-most-one band-prime property;
- the complete physical/high-conductor inclusion--exclusion interface (8.2).

### PROVED FROM CLASSICAL INPUT

- the uncentred full-source hit form has size at least `H^2/log X` and cannot be the desired determinant theorem.

### COMPUTATIONALLY VERIFIED

- all formal source and residue identities on `X=11,17,23`;
- character completion on every nonprincipal character in those panels;
- determinant reordering on finite panels;
- actual-source variance diagnostics through `X=337`;
- exact first/higher/cross energy recombination.

### OPEN

- `PBDH_P(X)`, the one-logarithm prime-band variance saving;
- deterministic restriction from all residues to the primorial-centre orbit with cross-modulus covariance;
- signed physical/higher-conductor survivor contraction;
- the first physical-band theorem;
- `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

## 10. Verdict

The repaired sequence eliminates the unbalanced-cell ambiguity completely, but it also changes the proposed analytic target. The remaining physical difficulty is not an arbitrary Möbius-weighted fourth moment. It is a centred sparse-modulus variance for `Lambda` at prime moduli `p\asymp\sqrt H`, requiring the prime-density logarithmic saving, followed by coherent recombination with the one-point higher conductors.
