# Four-point dilation kernel and signed conductor autocorrelation

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the four-point collision kernel, its common-dilation interpretation, the exact completion by nontrivial dilation modes, the low-dilation spectral localization and the sharp arbitrary-weight point-evaluation obstruction are **PROVED EXACTLY**. The collision-only Heath--Brown/Linnik attack does not by itself estimate the deterministic Fortune transfer: it is the conductor-diagonal/model component and omits the cross-conductor autocorrelation. The remaining arithmetic sampling theorem is still open.

## 1. Purpose

The primitive-character survivor expansion suggested a four-point kernel involving source--centre pairs

\[
\alpha=(j,m),\qquad \beta=(k,n),
\]

and the collision integer

\[
D_{\alpha,\beta}=mP_k-nP_j.
\]

The intended next step was to collapse the signed conductor system to this kernel and then attack the congruences

\[
p\mid D_{\alpha,\beta}
\]

by lower-band dispersion.

The collapse is exact, but a crucial qualification is required. The resulting positive kernel is:

1. the covariance after averaging over a common multiplicative CRT dilation; and equivalently
2. the `Q=Q'`, `\chi=\psi` diagonal of the conductor expansion.

It is not the complete deterministic square. This note proves the kernel, computes the omitted spectrum exactly and identifies the corrected lower-band target.

## 2. Universal survivor on the multiplicative CRT group

Let

\[
\Omega_R=\prod_{p\in\mathcal P_R}\mathbb F_p^\times,
\qquad
V_R=\prod_{p\in\mathcal P_R}\frac{p-2}{p-1}.
\]

For `x=(x_p)_p\in\Omega_R`, define

\[
S_R(x)=V_R^{-1}\mathbf 1_{x_p\ne1\ \forall p},
\qquad
g_R(x)=S_R(x)-1.
\tag{2.1}
\]

For an ordinary arithmetic source--centre pair with `(mP_j,\Pi_R)=1`, put

\[
x_{j,m,p}\equiv -mP_j^{-1}\pmod p.
\tag{2.2}
\]

Then

\[
g_{P_j,R}(m)=g_R(x_{j,m}).
\tag{2.3}
\]

If `\chi\in\widehat\Omega_R` has exact squarefree conductor `Q`, the Fourier coefficient of `S_R` is

\[
a(\chi)=\frac{\mu(Q)}{\varphi^\dagger(Q)},
\qquad
\varphi^\dagger(Q)=\prod_{p\mid Q}(p-2).
\tag{2.4}
\]

The Fourier coefficients of `g_R` are

\[
c(\chi)=
\begin{cases}
0,&\chi=1,\\[3pt]
a(\chi),&\chi\ne1.
\end{cases}
\tag{2.5}
\]

Every nontrivial character occurs with a nonzero coefficient.

## 3. Exact four-point common-dilation kernel

For `x,y\in\Omega_R`, write

\[
r=xy^{-1}.
\]

Define

\[
\mathcal K_R(r)
=
\mathbb E_{u\in\Omega_R}g_R(ru)\overline{g_R(u)}.
\tag{3.1}
\]

### Theorem 3.1 -- four-point kernel

One has

\[
\boxed{
\mathcal K_R(r)
=
\sum_{\substack{Q\mid\Pi_R\\Q>1}}
\frac1{\varphi^\dagger(Q)^2}
\sum_{\chi\bmod Q}^{\dagger}\chi(r).
}
\tag{3.2}
\]

Equivalently,

\[
\boxed{
\mathcal K_R(r)
=
\prod_{\substack{p\in\mathcal P_R\\r_p=1}}
\frac{p-1}{p-2}
\prod_{\substack{p\in\mathcal P_R\\r_p\ne1}}
\frac{(p-1)(p-3)}{(p-2)^2}
-1.
}
\tag{3.3}
\]

Writing

\[
A_R=\prod_{p\in\mathcal P_R}
\left(1-\frac1{(p-2)^2}\right),
\]

this is

\[
\boxed{
\mathcal K_R(r)
=
A_R
\prod_{p:r_p=1}\frac{p-2}{p-3}
-1.
}
\tag{3.4}
\]

### Proof

The common dilation `u_p` has one forbidden value for each survivor. If the two forbidden values agree, equivalently `r_p=1`, there are `p-2` allowed dilation residues. Otherwise there are `p-3`. Normalizing by `V_R^2` gives (3.3).

Alternatively, insert the Fourier expansion (2.5). Orthogonality in `u` forces the two exact-conductor characters to be identical. The Möbius signs therefore square to `+1`, giving (3.2). Local nonprincipal-character orthogonality gives (3.3). `\square`

For arithmetic pairs,

\[
r_p=1
\iff
p\mid mP_k-nP_j.
\tag{3.5}
\]

If `j<k` and `P_k=P_jL_{jk}`, every band prime is coprime to `P_j`, so

\[
\boxed{
p\mid mP_k-nP_j
\iff
p\mid mL_{jk}-n.
}
\tag{3.6}
\]

Thus the proposed linear collision congruence is exact.

## 4. Self coordinates

If the source is the band prime `p_0`, the exact identity already proved on the branch is

\[
g^{[p_0]}_{j,R}
=
\frac{p_0-1}{p_0-2}g_{j,R\setminus\{p_0\}}
+
\frac1{p_0-2}.
\tag{4.1}
\]

The centred self coordinate is therefore

\[
\widetilde g^{[p_0]}_{j,R}
=
\frac{p_0-1}{p_0-2}g_{j,R\setminus\{p_0\}}.
\tag{4.2}
\]

Common-dilation covariances involving self coordinates are obtained by deleting every self prime from the kernel band and multiplying by the corresponding factors `(p-1)/(p-2)`. The constants `1/(p-2)` remain in the explicit zeroth/self drift. No self source is omitted.

## 5. Why the collision kernel is not the deterministic square

For a coefficient family `b_\alpha`, set

\[
B(\chi)=\sum_\alpha b_\alpha\chi(x_\alpha).
\]

The deterministic survivor sum is

\[
T=\sum_\alpha b_\alpha g_R(x_\alpha)
=
\sum_{\chi\ne1}c(\chi)B(\chi).
\tag{5.1}
\]

Its square is

\[
\boxed{
|T|^2
=
\sum_{\chi,\psi\ne1}
 c(\chi)\overline{c(\psi)}
 B(\chi)\overline{B(\psi)}.
}
\tag{5.2}
\]

The four-point collision kernel accounts only for the diagonal `\chi=\psi` part

\[
\sum_{\chi\ne1}|c(\chi)|^2|B(\chi)|^2.
\tag{5.3}
\]

All `\chi\ne\psi` terms are removed by common-dilation averaging. In conductor language, these are precisely the `Q\ne Q'` terms together with distinct characters at common conductor. They contain the cross-conductor cancellation which `SMHLS(X)` was introduced to preserve.

Therefore the statement that (3.3) evaluates the signed conductor sum before Cauchy--Schwarz is false. It evaluates the conductor diagonal after an exact model average.

## 6. Exact dilation-Wigner completion

The omitted terms can nevertheless be organized exactly rather than left as an undifferentiated defect.

For `\theta\in\widehat\Omega_R`, define

\[
\mathcal D_\theta(r)
=
\sum_{\chi\in\widehat\Omega_R}
 c(\chi)\overline{c(\chi\overline\theta)}\chi(r).
\tag{6.1}
\]

### Theorem 6.1 -- signed dilation autocorrelation

For every `r,y\in\Omega_R`,

\[
\boxed{
 g_R(ry)\overline{g_R(y)}
 =
 \sum_{\theta\in\widehat\Omega_R}
 \mathcal D_\theta(r)\theta(y).
}
\tag{6.2}
\]

Moreover,

\[
\boxed{
\mathcal D_1(r)=\mathcal K_R(r).
}
\tag{6.3}
\]

Hence

\[
 g_R(ry)\overline{g_R(y)}
 =
 \mathcal K_R(r)
 +
 \sum_{\theta\ne1}\mathcal D_\theta(r)\theta(y).
\tag{6.4}
\]

The second term is the complete signed cross-conductor sampling defect.

### Product formula

Let

\[
\mathcal A_\theta(r)
=
\mathbb E_y S_R(ry)S_R(y)\overline{\theta(y)}.
\]

It factorizes as

\[
\mathcal A_\theta(r)
=
\prod_{p\in\mathcal P_R}\mathcal A_{p,\theta_p}(r_p),
\tag{6.5}
\]

where

\[
\mathcal A_{p,1}(r_p)
=
\begin{cases}
\dfrac{p-1}{p-2},&r_p=1,\\[6pt]
\dfrac{(p-1)(p-3)}{(p-2)^2},&r_p\ne1,
\end{cases}
\tag{6.6}
\]

and, for `\theta_p\ne1`,

\[
\boxed{
\mathcal A_{p,\theta_p}(r_p)
=
-\frac{p-1}{(p-2)^2}
\left(1+\theta_p(r_p)-\mathbf1_{r_p=1}\right).
}
\tag{6.7}
\]

Consequently,

\[
\mathcal D_1(r)=\mathcal A_1(r)-1,
\tag{6.8}
\]

and, for `\theta\ne1`,

\[
\boxed{
\mathcal D_\theta(r)
=
\mathcal A_\theta(r)
-
\frac{\mu(\operatorname{cond}\theta)}
{\varphi^\dagger(\operatorname{cond}\theta)}
\left(1+\theta(r)\right).
}
\tag{6.9}
\]

Formula (6.9) retains every cross-order Möbius sign.

## 7. Exact energy of the omitted spectrum

Put

\[
\delta_R=V_R^{-1}-1,
\qquad
\kappa_R(r)=\mathcal K_R(r).
\]

Parseval in the dilation variable gives

\[
\sum_\theta|\mathcal D_\theta(r)|^2
=
\mathbb E_y|g_R(ry)g_R(y)|^2.
\tag{7.1}
\]

### Theorem 7.1 -- fourth-energy identity

One has

\[
\boxed{
\sum_\theta|\mathcal D_\theta(r)|^2
=
\delta_R^2
+
\kappa_R(r)(1-\delta_R)^2.
}
\tag{7.2}
\]

Therefore

\[
\boxed{
\sum_{\theta\ne1}|\mathcal D_\theta(r)|^2
=
\delta_R^2
+
\kappa_R(r)(1-\delta_R)^2
-
\kappa_R(r)^2.
}
\tag{7.3}
\]

### Proof

The random variable `g_R` equals `\delta_R` on a survivor and `-1` otherwise. If

\[
J_R(r)=\mathbb P(y\text{ and }ry\text{ both survive}),
\]

then

\[
\kappa_R(r)=J_R(r)V_R^{-2}-1.
\]

Expanding the four possibilities for the two survivor events and simplifying gives (7.2). Subtracting the trivial dilation mode gives (7.3). `\square`

If `c_R(r)` band primes satisfy `r_p=1`, the already-proved collision bounds give

\[
\sum_{\theta\ne1}|\mathcal D_\theta(r)|^2
\ll
\frac1{\log^2R}
+
\frac{c_R(r)}R
+
\frac1{R\log R}.
\tag{7.4}
\]

Thus the omitted spectrum has small complete-model energy. The unresolved issue is deterministic sampling, not model size.

## 8. Low dilation conductors localize at collision primes

At the Fortune scale `H=\eta X^2`, every dilation conductor containing at least two band primes exceeds `H`. The low dilation spectrum is therefore exactly `\operatorname{cond}\theta=p`.

Fix `p\in\mathcal P_R` and a nonprincipal character `\theta\bmod p`, extended principally at every other band prime. Let

\[
\kappa_{-p}(r)
=
\prod_{q\ne p}\mathcal A_{q,1}(r_q)-1.
\tag{8.1}
\]

### Theorem 8.1 -- exact single-prime mode

If `r_p\ne1`, then

\[
\boxed{
\mathcal D_\theta(r)
=
-\frac{(1+\theta(r_p))
\left(1+(p-1)\kappa_{-p}(r)\right)}{(p-2)^2}.
}
\tag{8.2}
\]

If `r_p=1`, then

\[
\boxed{
\mathcal D_\theta(r)
=
\frac{p-3-(p-1)\kappa_{-p}(r)}{(p-2)^2}.
}
\tag{8.3}
\]

Summing over the `p-2` nonprincipal characters gives

\[
\boxed{
\sum_{\theta\ne1\bmod p}|\mathcal D_\theta(r)|^2
=
\frac{2(p-3)
\left(1+(p-1)\kappa_{-p}(r)\right)^2}{(p-2)^4}
}
\tag{8.4}
\]

when `r_p\ne1`, and

\[
\boxed{
\sum_{\theta\ne1\bmod p}|\mathcal D_\theta(r)|^2
=
\frac{(p-2)
\left(p-3-(p-1)\kappa_{-p}(r)\right)^2}{(p-2)^4}
}
\tag{8.5}
\]

when `r_p=1`.

For `p\asymp R`, the noncollision energy is `O(R^{-3})` up to the reduced-band collision factor, whereas the collision energy is `O(R^{-1})`. Hence the low dilation spectrum is sharply concentrated on

\[
p\mid mP_k-nP_j,
\]

or equivalently

\[
p\mid mL_{jk}-n.
\]

This is the valid form of the collision reduction: it describes the dominant part of the **completed signed dilation spectrum**, not the whole deterministic square by itself.

## 9. Sharp arbitrary-weight point-evaluation obstruction

Because every nontrivial Fourier coefficient `c(\chi)` is nonzero, the translates of `g_R` span the entire mean-zero space `L^2_0(\Omega_R)`.

Let

\[
M_R=|\Omega_R|=\prod_{p\in\mathcal P_R}(p-1).
\]

On normalized `L^2(\Omega_R)`, point evaluation on the mean-zero space has squared norm exactly

\[
\boxed{M_R-1.}
\tag{9.1}
\]

Indeed,

\[
F(u)=M_R\mathbf1_{u=1}-1
\]

has mean zero and satisfies

\[
\frac{|F(1)|^2}{\mathbb E|F|^2}=M_R-1.
\tag{9.2}
\]

Therefore no arbitrary-weight inequality can transfer the common-dilation average (3.1) to the deterministic point `u=1` with a bounded constant. Any successful theorem must exploit the rigid prime source, primorial centres and previous-band survivor history. This is a sharp group-theoretic version of the earlier factorization no-go.

## 10. Lower-band dispersion gate

The proposed collision-only programme now has a precise verdict.

### Passed exactly

1. the four-point collision formula;
2. the reduction `p\mid mP_k-nP_j \iff p\mid mL_{jk}-n`;
3. exact self-coordinate removal and drift retention;
4. an exact decomposition of the deterministic square into the collision kernel plus signed nontrivial dilation modes;
5. exact energy and low-conductor localization of those modes.

### Failed as originally stated

Applying Heath--Brown/Vaughan decomposition and Linnik dispersion only to `\mathcal K_R` estimates the common-dilation or conductor-diagonal model. It does not estimate the deterministic Fortune square because it has already removed the nontrivial dilation modes in (6.4).

This is not a technical error that a stronger large sieve fixes. It is an algebraic projection of the required cancellation.

### Corrected analytic target

The lower-band attack must retain

\[
\sum_{\theta\ne1}
\mathcal D_\theta(r_{\alpha,\beta})
\theta(x_\beta)
\tag{10.1}
\]

through the source decomposition. The low modes `\operatorname{cond}\theta=p` have the favourable localization (8.4)--(8.5): their noncollision energy is two powers of `p` smaller than their collision energy. Higher dilation conductors all exceed `H`.

A viable next proof would need to combine:

1. multiplicative large-sieve control of the noncollision low modes;
2. a dispersion estimate for the sparse incidences `p\mid mL_{jk}-n`;
3. high-conductor source orthogonality;
4. summation over `\theta` without replacing the deterministic point by the complete-dilation average.

That joint statement is a sharpened form of `SMHLS(X)` / `PCRST(X)`, not a proof of it.

## 11. Exact finite verification

The committed verifier checks:

1. 441 exact conductor-sum/collision-kernel identities on the band `[13,17,19]`;
2. complete common-dilation averages on a CRT group of size 3456;
3. 882 primorial collision reductions, including 100 genuine collisions;
4. 696 exact self-coordinate reductions;
5. the fourth-energy identity on all 240 ratios for `[5,7,11]`;
6. the sharp point-evaluation ratio `3455` on a group of size `3456`;
7. full cyclotomic Wigner reconstruction on `[5,7]` to error below `2\times10^{-15}`;
8. an exact 51-point prime-source panel on which the cross-conductor defect is not lower order:

\[
|T|^2=\frac{74529}{7225}\approx10.3154,
\]

\[
T_{\mathrm{diag}}=\frac{4397031}{874225}\approx5.02963,
\]

\[
T_{\mathrm{off}}=\frac{4620978}{874225}\approx5.28580.
\]

The off-diagonal defect exceeds the conductor-diagonal form on this panel. Single-point examples show both signs of the defect.

## 12. Boundary

**PROVED EXACTLY**

1. four-point common-dilation/conductor-diagonal kernel;
2. linear primorial collision reduction;
3. self-coordinate covariance reduction;
4. signed dilation-Wigner completion;
5. exact fourth and nontrivial-mode energies;
6. exact single-prime dilation-mode localization;
7. sharp arbitrary-weight point-evaluation obstruction.

**COMPUTATIONALLY VERIFIED**

1. every exact identity above on finite rational panels;
2. the cyclotomic reconstruction numerically to machine precision;
3. non-negligibility and sign-indefiniteness of the cross-conductor defect.

**CLOSED AS STATED**

1. the collision-only `TT^*`/Linnik route which identifies the common-dilation kernel with the deterministic square;
2. any arbitrary-weight transfer from complete-dilation energy to one deterministic dilation with bounded constant.

**OPEN**

1. deterministic sampling of the nontrivial dilation modes for the rigid prime-candidate source;
2. the completed low-mode collision dispersion estimate;
3. `SMHLS(X)` / `PCRST(X)`;
4. `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.
