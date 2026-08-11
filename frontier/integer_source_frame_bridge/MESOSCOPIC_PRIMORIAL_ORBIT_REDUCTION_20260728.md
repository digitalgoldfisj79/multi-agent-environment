# Mesoscopic primorial-orbit reduction

Date: 29 July 2026  
Status: **PROVED EXACTLY** for freezing, the orbit kernel and the bounded orbit frame; the joint common-source dispersion theorem is **OPEN**.

## 1. Setup

Let

\[
H=\eta X^2,
\qquad 0<\eta<1,
\]

and let `P_0,\ldots,P_{N-1}` be consecutive primorial centres whose largest prime factors `z_j` lie in `[X,2X)`. Thus

\[
P_{j+1}=z_{j+1}P_j.
\tag{1.1}
\]

For candidate primes `z_j<m\le H`, use

\[
b_{j,m}=\log(P_j+m)V(z_j,Y_j),
\qquad Y_j=\sqrt{P_j+H}.
\tag{1.2}
\]

The locally centred physical first-order term is

\[
G_j^{(1)}=-\sum_{z_j<r\le H\atop r\text{ prime}}\frac{r-1}{r-2}\Delta_{j,r}.
\tag{1.3}
\]

## 2. Mesoscopic blocks

Choose

\[
1\le K\le c\sqrt X
\tag{2.1}
\]

and partition the centre indices into consecutive blocks `B` of size at most `K`. Put

\[
z_B=\max_{j\in B}z_j,
\]

\[
\mathcal M_B=\{m:z_B<m\le H,\ m\text{ prime}\},
\qquad
\mathcal R_B=\{r:z_B<r\le H,\ r\text{ prime}\},
\tag{2.2}
\]

and

\[
\beta_j=\log P_j\,V(z_j,Y_j).
\tag{2.3}
\]

## 3. Freezing

### Lemma 3.1 — weight freezing

Uniformly for `2\le m\le H`,

\[
b_{j,m}=\beta_j+O\!\left(V(z_j,Y_j)\frac H{P_j}\right).
\tag{3.1}
\]

The aggregate error is exponentially smaller than any negative power of `X`, because `\log(P_j+m)-\log P_j=O(H/P_j)` and `P_j=\exp((1+o(1))X)`. \(\square\)

The candidate and modulus sets of two indices in one block differ by at most `K` primes.

### Lemma 3.2 — one-offset cost

For a fixed candidate prime `m`,

\[
\left|b_{j,m}\sum_{z_j<r\le H}\xi_r(P_j+m)\right|\ll X.
\tag{3.2}
\]

The baseline reciprocal-prime sum is bounded. Every active hit prime exceeds `X` and divides `P_j+m`, so there are at most `\log(P_j+H)/\log X\ll X/\log X` such primes. Since `|b_{j,m}|\ll\log X`, the result follows. \(\square\)

### Lemma 3.3 — one-modulus cost

Uniformly for `z_j<r\le H`, the complete locally centred contribution of one modulus is `O(X)`.

For `r\le H/2`, Brun--Titchmarsh gives `O(H/(r\log(H/r)))` candidate-prime hits. Multiplication by the logarithmic Euler weight is `O(X)` uniformly for `r>X`; the centred baseline has the same scale. For `r>H/2`, the residue class contains at most two physical integers. \(\square\)

Define `\widetilde G_j^{(1)}` by replacing the candidate and modulus sets by `\mathcal M_B,\mathcal R_B` and replacing `b_{j,m}` by `\beta_j`.

### Theorem 3.4 — mesoscopic freezing

For `j\in B`,

\[
\boxed{|G_j^{(1)}-\widetilde G_j^{(1)}|\ll KX}
\tag{3.3}
\]

apart from an exponentially negligible term. Consequently

\[
\boxed{
\sum_{j<N}|G_j^{(1)}-\widetilde G_j^{(1)}|^2\ll NK^2X^2.
}
\tag{3.4}
\]

This is `O(NHX)` whenever

\[
K^2X\ll H,
\tag{3.5}
\]

which holds for `K\le c\sqrt X` with an admissible fixed `c` because `H=\eta X^2`.

## 4. Exact centre Gram kernel

For `\mathcal R\subseteq\mathcal R_B`, define

\[
\Phi_j(r,a)=\frac1r e(aP_j/r),
\qquad r\in\mathcal R,
\quad 1\le a<r.
\tag{4.1}
\]

Its centre Gram kernel is

\[
\mathcal K_{jk}=\sum_{r\in\mathcal R}\frac1{r^2}\sum_{a=1}^{r-1}e(a(P_j-P_k)/r).
\tag{4.2}
\]

Complete additive orthogonality gives, for `j\ne k`,

\[
\boxed{
\mathcal K_{jk}=-\sum_{r\in\mathcal R}\frac1{r^2}
+\sum_{r\in\mathcal R\atop r\mid P_j-P_k}\frac1r,
}
\tag{4.3}
\]

and

\[
\mathcal K_{jj}=\sum_{r\in\mathcal R}\frac{r-1}{r^2}.
\tag{4.4}
\]

## 5. Primorial-prefix rigidity

If `j<k` are in one block and `r>z_B`, then

\[
\boxed{
r\mid P_k-P_j\iff r\mid\prod_{j<u\le k}z_u-1.
}
\tag{5.1}
\]

For `h=k-j`, the right-hand integer is smaller than `(2X)^h`, so it has `O(h)` prime divisors exceeding `X`. Therefore

\[
\boxed{
\sum_{r\in\mathcal R\atop r\mid P_k-P_j}\frac1r\ll\frac hX.
}
\tag{5.2}
\]

Also

\[
\sum_{r>X}\frac1{r^2}\ll\frac1{X\log X},
\qquad
\sum_{X<r\le H}\frac1r\ll1.
\tag{5.3}
\]

## 6. Bounded orbit frame

### Theorem 6.1

For every block of size at most `K`,

\[
\boxed{
\|\mathcal K\|_{\mathrm{op}}
\ll1+\frac{K^2}{X}+\frac{K}{X\log X}.
}
\tag{6.1}
\]

In particular, for `K\ll\sqrt X`,

\[
\|\mathcal K\|_{\mathrm{op}}\ll1.
\tag{6.2}
\]

Equivalently,

\[
\boxed{
\sum_{j\in B}\left|\sum_{r\in\mathcal R}\sum_{a=1}^{r-1}\frac{c_{r,a}}r e(aP_j/r)\right|^2
\ll\sum_{r,a}|c_{r,a}|^2.
}
\tag{6.3}
\]

The proof uses (4.3)--(5.3) and the Schur row-sum bound. The collision contribution in one row is `O(K^2/X)`, the dense negative term is `O(K/(X\log X))`, and the diagonal is `O(1)`. \(\square\)

## 7. Factorised-frame no-go

The frozen source Fourier coefficient is

\[
T_{B,r}(a)=\sum_{m\in\mathcal M_B}e(am/r).
\tag{7.1}
\]

Parseval gives

\[
\sum_{a\bmod r}|T_{B,r}(a)|^2=r\sum_{c\bmod r}\nu_{B,r}(c)^2,
\tag{7.2}
\]

and the singleton contribution alone is `r|\mathcal M_B|`. More generally, for positive scalar redistributions `w_r`,

\[
\left(\sum_r rw_r^2\right)\left(\sum_r\frac1{rw_r^2}\right)\ge(\#\mathcal R)^2.
\tag{7.3}
\]

### Proposition 7.1

An argument that first bounds a source Fourier norm independently of the primorial orbit norm cannot reach the Fortune scale throughout `X<r\le H`. The load-bearing estimate must retain the joint phases

\[
e\!\left(\frac{a(P_j+m)}r-\frac{b(P_j+n)}s\right)
\]

until source and orbit averaging have been combined.

## 8. Revised target

It suffices, as a first-order subproblem, to prove on every block

\[
\boxed{
\sum_{j\in B}|\widetilde G_j^{(1)}|^2
\ll KHX\,L_1(X),
\qquad L_1(X)=o(\log X).
}
\tag{8.1}
\]

The same-band reduction isolates a sufficient version of (8.1). The normalized rough coordinate and ordered Buchstab tail must subsequently be reinserted with their exact covariance.

## 9. Boundary

**PROVED EXACTLY**

1. weight and cutoff freezing at cost (3.4);
2. exact orbit kernel (4.3)--(4.4);
3. primorial-prefix collision criterion and bound (5.1)--(5.2);
4. bounded orbit frame (6.1)--(6.3);
5. factorised-frame no-go (7.3).

**COMPUTATIONALLY VERIFIED**

The companion verifier checks the complete additive kernel, collision counts and Schur bound on finite panels.

**OPEN**

1. the joint common-source block estimate (8.1), including its same-band form;
2. exact covariance with the rough coordinate and Buchstab tail;
3. Fortune's conjecture.
