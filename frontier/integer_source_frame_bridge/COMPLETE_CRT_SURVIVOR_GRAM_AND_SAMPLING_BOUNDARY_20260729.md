# Complete-CRT survivor Gram and the prime-candidate sampling boundary

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the Hilbert-valued complement-divisor identity, the full-band normalized-survivor centre Gram, its operator bound, and its conditional martingale consequence are **PROVED EXACTLY**. They prove the complete-CRT model component of the band transfer while retaining every Euler order. Transfer to the deterministic candidate-prime source remains **OPEN**.

## 1. Why this is the next object

The common-base and normalized-survivor reductions isolated two cancellations which positive estimates destroy:

1. density against nontrivial conductors in the physical range;
2. normalization drift against sparse hits in the upper range.

The correct response is not another conductor truncation. It is to keep the entire Euler product over one prime band and compute its covariance before diagonalizing any Euler divisor.

Let `B` be a mesoscopic block of consecutive primorial centres `P_j`, of cardinality

\[
K\ll \sqrt X.
\]

Fix a dyadic band

\[
\mathcal P_R=\{p:R<p\le 2R,\ p\ {\rm prime}\},
\qquad R\ge X,
\]

with every `p` larger than the largest prime entering the centres in `B`.

## 2. A Hilbert-valued complement-divisor identity

The following identity is the vector-valued form of the scalar complement-divisor identity highlighted by Friedlander in arXiv:2607.05707, equation (2.3). The proof below is independent and uses only divisor algebra.

Let

\[
\Pi=\prod_{p\in\mathcal P}p,
\qquad
U=\frac{\varphi(\Pi)}{\Pi}.
\]

Let `\mathcal H` be a real or complex Hilbert space and let `\lambda_m\in\mathcal H` for `m\mid\Pi`.

### Theorem 2.1 — complement-divisor Plancherel identity

\[
\boxed{
\sum_{d\mid\Pi}\varphi(d)
\left\|
\sum_{\substack{m\mid\Pi\\d\mid m}}\frac{\lambda_m}{m}
\right\|_{\mathcal H}^{2}
=
U
\sum_{\delta\mid\Pi}\frac1{\varphi(\delta)}
\left\|
\sum_{m\mid\delta}\lambda_m
\right\|_{\mathcal H}^{2}.
}
\tag{2.1}
\]

### Proof

After expanding the left side, the coefficient of
`\langle\lambda_m,\lambda_n\rangle` is

\[
\frac1{mn}\sum_{d\mid(m,n)}\varphi(d)
=
\frac{(m,n)}{mn}
=
\frac1{[m,n]}.
\tag{2.2}
\]

On the right side, with `\ell=[m,n]`, the same coefficient is

\[
U\sum_{\substack{\delta\mid\Pi\\\ell\mid\delta}}
\frac1{\varphi(\delta)}.
\tag{2.3}
\]

Because `\Pi` is squarefree,

\[
\sum_{\substack{\delta\mid\Pi\\\ell\mid\delta}}
\frac1{\varphi(\delta)}
=
\frac1{\varphi(\ell)}
\prod_{\substack{p\mid\Pi\\p\nmid\ell}}
\left(1+\frac1{p-1}\right).
\tag{2.4}
\]

Multiplication by `U` cancels the factors outside `\ell` and leaves

\[
\frac{\varphi(\ell)/\ell}{\varphi(\ell)}
=
\frac1\ell.
\tag{2.5}
\]

Thus the two quadratic forms have the same coefficient kernel. `\square`

### Corollary 2.2 — exact Möbius collapse

For `\lambda_m=\mu(m)v`, with fixed `v\in\mathcal H`,

\[
\sum_{m\mid\delta}\mu(m)
=
\mathbf1_{\delta=1},
\]

so (2.1) becomes

\[
\boxed{
\sum_{d\mid\Pi}\varphi(d)
\left|
\sum_{\substack{m\mid\Pi\\d\mid m}}\frac{\mu(m)}m
\right|^2
=
U.
}
\tag{2.6}
\]

After normalizing the Möbius coefficients by `U^{-1}`, the energy is exactly `U^{-1}`.

This identity preserves the complete alternating Euler cancellation. It replaces the exponential divisor count by lower-divisor Möbius differences. For source-dependent coefficients, the quantities

\[
\Theta_\delta
=
\sum_{m\mid\delta}\lambda_m
\tag{2.7}
\]

measure precisely how far the source is from the coherent Möbius direction.

## 3. The full-band survivor coordinate

The candidate offset is nonzero modulo every physical prime in the band. The complete local model is therefore

\[
\Omega_R
=
\prod_{p\in\mathcal P_R}\mathbb F_p^\times
\]

with uniform product measure.

Put

\[
V_R
=
\prod_{p\in\mathcal P_R}\frac{p-2}{p-1}.
\tag{3.1}
\]

For `j\in B`, define the normalized survivor coordinate

\[
S_{j,R}(\omega)
=
V_R^{-1}
\mathbf1_{\omega_p\ne-P_j\ ({\rm mod}\ p)\ {\rm for\ every}\ p\in\mathcal P_R}
\tag{3.2}
\]

and its centred version

\[
g_{j,R}=S_{j,R}-1.
\tag{3.3}
\]

Every Euler order inside the band is contained in (3.2). No conductor or hit layer has been separated.

### Lemma 3.1 — exact centring

\[
\boxed{\mathbb E_{\Omega_R}S_{j,R}=1,\qquad
\mathbb E_{\Omega_R}g_{j,R}=0.}
\tag{3.4}
\]

At each prime, one of the `p-1` nonzero source residues is forbidden, so the local survival probability is `(p-2)/(p-1)`.

## 4. Exact survivor centre Gram

Let

\[
\mathcal K^{\rm surv}_{jk}(R)
=
\mathbb E_{\Omega_R}\bigl[g_{j,R}\overline{g_{k,R}}\bigr].
\tag{4.1}
\]

### Theorem 4.1 — complete-CRT survivor Gram

On the diagonal,

\[
\boxed{
\mathcal K^{\rm surv}_{jj}(R)=V_R^{-1}-1.
}
\tag{4.2}
\]

For `j\ne k`,

\[
\boxed{
\mathcal K^{\rm surv}_{jk}(R)
=
\prod_{\substack{p\in\mathcal P_R\\p\mid P_j-P_k}}
\frac{p-1}{p-2}
\prod_{\substack{p\in\mathcal P_R\\p\nmid P_j-P_k}}
\frac{(p-1)(p-3)}{(p-2)^2}
-1.
}
\tag{4.3}
\]

Equivalently, putting

\[
A_R
=
\prod_{p\in\mathcal P_R}
\left(1-\frac1{(p-2)^2}\right),
\tag{4.4}
\]

one has

\[
\boxed{
\mathcal K^{\rm surv}_{jk}(R)
=
A_R
\prod_{\substack{p\in\mathcal P_R\\p\mid P_j-P_k}}
\frac{p-2}{p-3}
-1.
}
\tag{4.5}
\]

### Proof

For `j=k`, both survivor indicators forbid the same source residue at every prime. Hence

\[
\mathbb E S_{j,R}^2
=
V_R^{-2}V_R
=
V_R^{-1}.
\]

For `j\ne k`, at a prime dividing `P_j-P_k` the two forbidden residues coincide, leaving `p-2` allowed residues. At a noncollision prime the forbidden residues are distinct, leaving `p-3` allowed residues. Dividing the resulting product probability by `V_R^2` proves (4.3). Factoring the noncollision local term proves (4.5). `\square`

The negative noncollision covariance and the positive collision correction are both retained. Formula (4.3) is the all-Euler-order analogue of the earlier additive orbit Gram.

## 5. Operator bound from primorial-prefix rigidity

For `j<k`, write `h=k-j`. Since every band prime exceeds the primes entering the centres,

\[
p\mid P_k-P_j
\iff
p\mid
\prod_{j<u\le k}z_u-1.
\tag{5.1}
\]

The integer on the right is smaller than `(2X)^h`. Therefore the number of collision primes in `\mathcal P_R` is `O(h)` for `R\ge X`.

Also,

\[
1-A_R
\ll
\sum_{p\in\mathcal P_R}\frac1{p^2}
\ll
\frac1{R\log R},
\tag{5.2}
\]

and

\[
V_R^{-1}-1
\ll
\sum_{p\in\mathcal P_R}\frac1p
\ll
\frac1{\log R}.
\tag{5.3}
\]

Using (4.5) and the collision count,

\[
\boxed{
|\mathcal K^{\rm surv}_{jk}(R)|
\ll
\frac{|j-k|}{R}
+
\frac1{R\log R}
\qquad(j\ne k).
}
\tag{5.4}
\]

### Theorem 5.1 — bounded complete-survivor frame

\[
\boxed{
\|\mathcal K^{\rm surv}(R)\|_{\rm op}
\ll
\frac1{\log R}
+
\frac{K^2}{R}
+
\frac{K}{R\log R}.
}
\tag{5.5}
\]

In particular, for `K\ll\sqrt X` and `R\ge X`,

\[
\|\mathcal K^{\rm surv}(R)\|_{\rm op}\ll1.
\tag{5.6}
\]

### Proof

Apply the Schur row-sum bound to (4.2) and (5.4). `\square`

This theorem controls an entire dyadic Euler band at once. It does not diagonalize conductors, split drift from hits, or discard higher-order factor-cluster cancellation.

## 6. Conditional martingale consequence

Let `\mathcal F_{<R}` contain all residue coordinates from earlier bands. The current band is independent of `\mathcal F_{<R}` in the complete CRT model.

### Corollary 6.1 — conditional survivor Bessel inequality

For arbitrary `\mathcal F_{<R}`-measurable coefficients `A_j`,

\[
\boxed{
\mathbb E\left(
\left|
\sum_{j\in B}A_j g_{j,R}
\right|^2
\Bigm|\mathcal F_{<R}
\right)
\le
\|\mathcal K^{\rm surv}(R)\|_{\rm op}
\sum_{j\in B}|A_j|^2.
}
\tag{6.1}
\]

Thus the complete-CRT model supports the required bandwise square-function mechanism even when `A_j` contains the full normalized survivor product from all preceding bands.

For independent model source samples `\omega^{(1)},\ldots,\omega^{(M)}`,

\[
\mathbb E
\left|
\sum_{t=1}^{M}\sum_{j\in B}c_jg_{j,R}(\omega^{(t)})
\right|^2
\le
M\|\mathcal K^{\rm surv}(R)\|_{\rm op}
\sum_j|c_j|^2.
\tag{6.2}
\]

This proves the model side of the normalized-survivor transfer, not the arithmetic sampling step.

## 7. Exact self-coordinate correction

For an actual candidate prime `m` outside the modulus band,

\[
\rho_R(m)=(m\bmod p)_{p\in\mathcal P_R}\in\Omega_R.
\tag{7.1}
\]

If `m=p_0\in\mathcal P_R`, its `p_0`-coordinate is zero and is not an element of `\mathbb F_{p_0}^{\times}`. This source point is not discarded. Its band survivor has the exact decomposition

\[
\boxed{
g^{[p_0]}_{j,R}
=
\frac{p_0-1}{p_0-2}\,
g_{j,R\setminus\{p_0\}}
+
\frac1{p_0-2}.
}
\tag{7.2}
\]

Indeed, the factor at `p_0` always survives because `p_0\nmid P_j`, while all other coordinates remain nonzero. The first term in (7.2) is a centred survivor coordinate on the reduced band and obeys Theorem 5.1. The second is the explicit self-normalization drift already represented by the zeroth/self coordinate in the locally centred formulation.

Thus the complete-CRT Gram theorem covers ordinary source points and the centred part of every self source point. No `m=p` term is silently removed.

## 8. Exact remaining arithmetic theorem

After inserting (7.2), the actual band increment has the form

\[
\mathcal B_{j,R}
=
\sum_{m\in\mathcal M_B}
A^{<R}_{j,m}\,
\widetilde g_{j,R,m}
+
\mathcal D^{\rm self}_{j,R},
\tag{8.1}
\]

where:

1. `A^{<R}_{j,m}` is the frozen logarithmic weight multiplied by the complete normalized survivor product from earlier bands;
2. `\widetilde g_{j,R,m}` is either `g_{j,R}(\rho_R(m))` or the reduced-band centred coordinate from (7.2);
3. `\mathcal D^{\rm self}_{j,R}` is the explicit weighted sum of the drifts `1/(p-2)`.

The complete-CRT theorem predicts the centred part at the scale

\[
\|\mathcal K^{\rm surv}(R)\|_{\rm op}
\sum_{j,m}|A^{<R}_{j,m}|^2,
\tag{8.2}
\]

with the self drift retained jointly with the existing zeroth coordinate.

The remaining theorem is now explicit.

### Open theorem `PCRST(X)` — prime-candidate residue survivor transfer

For the specific arithmetic weights, ordinary residue vectors, reduced-band self coordinates and zeroth/self drift in (8.1), prove

\[
\boxed{
\sum_{j\in B}|\mathcal B_{j,R}|^2
\ll
\left(
\frac1{\log R}
+
\frac{K^2}{R}
\right)
\sum_{j\in B}\sum_{m\in\mathcal M_B}|A^{<R}_{j,m}|^2
+
E_{B,R},
}
\tag{8.3}
\]

with errors whose dyadic sum is at the Fortune scale.

No arbitrary-weight version is asserted. The theorem is required only for the rigid weights generated by the preceding survivor bands and the prime candidate source.

A proof of `PCRST(X)` across all bands, together with the zeroth-centred coordinate already isolated in the branch, would yield `NSMT(X)`. The model covariance and its centre geometry are no longer open.

## 9. Relation to existing results

Friedlander's 2026 sieve note proves strong cancellation for standard beta- and Selberg-sieve coefficients and records the scalar ancestor of (2.1). Its applications average over almost all interval translations. It does not transfer the complete survivor process to the sparse primorial centres.

Gorodetsky's variance theorem for rough numbers, arXiv:2111.00853, computes the variance after averaging over all translations and also gives the exact complete-period primorial variance. It likewise does not control the deterministic candidate-prime sample at the primorial shifts.

These results validate the model cancellation but do not supply `PCRST(X)`.

## 10. What changed

Before this calculation, `NSMT(X)` mixed two possible unknowns:

1. whether the full normalized survivor process has a bounded centre Gram even after all Euler orders are recombined;
2. whether the actual prime candidate source samples that model at the required strength.

Theorem 5.1 settles the first question affirmatively. The only remaining band obstruction is the second.

This is a strict reduction. It is not a proof of the Fortune variance theorem.

## 11. Boundary

**PROVED EXACTLY**

1. Hilbert-valued complement-divisor identity (2.1);
2. exact coherent Möbius collapse (2.6);
3. exact complete-CRT survivor centring;
4. exact all-order survivor centre Gram (4.2)--(4.5);
5. conditional complete-CRT Bessel inequality.

**PROVED USING CLASSICAL PRIME ESTIMATES**

1. the uniform operator bound (5.5), using reciprocal-prime estimates and primorial-prefix rigidity.

**COMPUTATIONALLY VERIFIED**

1. the Hilbert identity on a nontrivial vector-valued finite panel;
2. exact survivor means and Gram on a complete CRT panel;
3. a panel containing a genuine primorial-prefix collision prime;
4. the exact self-coordinate decomposition for every band prime;
5. the Schur quadratic-form bound.

**OPEN**

1. `PCRST(X)`, the deterministic candidate-prime residue transfer;
2. its dyadic martingale recombination into `NSMT(X)`;
3. the Fortune variance theorem;
4. Fortune's conjecture.
