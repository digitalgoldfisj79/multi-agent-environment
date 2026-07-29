# Fixed-conductor hybrid orbit frame and the noncommuting-orthogonalities boundary

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the fixed-conductor frame, its Gram kernel and the source-energy formula below are **PROVED EXACTLY**. They control the primorial-centre side uniformly in the Ramanujan conductor. Recombination across conductors at the Fortune scale remains **OPEN**.

## 1. Common-base hybrid expansion

Use the common base `P_*` from `COMMON_BASE_CONDUCTOR_REDUCTION_20260729.md`. Put

\[
\delta_*=\frac{\varphi(P_*)}{P_*},
\qquad
W_M(h)=\sum_{Z<m\le H}e(hm/M).
\]

For a physical prime `q>Z`, the exact quotient count is

\[
N_j(q)
=
\frac{\delta_*}{q}
\sum_{d\mid P_*}\frac{\mu(d)}{\varphi(d)}
\sum_{h\bmod qd\atop(h,d)=1}
 e\!\left(\frac{hP_j}{qd}\right)W_{qd}(h).
\]

The divisor system and source coefficients are common across the block.

## 2. Fixed-conductor synthesis frame

Fix one divisor `d\mid P_*` and one dyadic physical prime band `\mathcal Q_R`. Define

\[
\Phi_j^{(d)}(q,h)
=
\frac1{q\sqrt{\varphi(d)}}
 e\!\left(\frac{hP_j}{qd}\right),
\]

for

\[
q\in\mathcal Q_R,
\qquad
h\bmod qd,
\qquad(h,d)=1.
\]

### Theorem 2.1 — fixed-conductor frame

For every coefficient family `c_{q,h}`,

\[
\boxed{
\sum_{j\in B}
\left|
\sum_{q\in\mathcal Q_R}
\sum_{h\bmod qd\atop(h,d)=1}
\frac{c_{q,h}}{q\sqrt{\varphi(d)}}
 e\!\left(\frac{hP_j}{qd}\right)
\right|^2
\ll
\left(1+\frac{K^2}{X}\right)
\sum_{q,h}|c_{q,h}|^2.
}
\]

The implied constant is absolute and independent of `d`.

### Proof

Let `\Delta_{jk}=P_j-P_k`. Since `d\mid P_*\mid P_j,P_k`, one has `d\mid\Delta_{jk}`. The centre Gram is

\[
\mathcal K_{jk}^{(d)}
=
\frac1{\varphi(d)}
\sum_{q\in\mathcal Q_R}\frac1{q^2}
\sum_{h\bmod qd\atop(h,d)=1}
 e\!\left(\frac{h\Delta_{jk}}{qd}\right).
\]

CRT factorization gives

\[
\sum_{h\bmod qd\atop(h,d)=1}
 e\!\left(\frac{h\Delta}{qd}\right)
=
q\varphi(d)\mathbf1_{q\mid\Delta}
\]

whenever `d\mid\Delta`. Therefore

\[
\mathcal K_{jj}^{(d)}
=
\sum_{q\in\mathcal Q_R}\frac1q
\ll1,
\]

and, for `j\ne k`,

\[
\boxed{
\mathcal K_{jk}^{(d)}
=
\sum_{q\in\mathcal Q_R\atop q\mid P_j-P_k}\frac1q.
}
\]

The primorial-prefix criterion gives at most `O(|j-k|)` such primes, all exceeding `X`, hence

\[
|\mathcal K_{jk}^{(d)}|\ll\frac{|j-k|}{X}.
\]

The Schur row sum is `O(1+K^2/X)`, proving the theorem. \(\square\)

### Consequence

For the fixed-conductor component

\[
T_{j,d}
=
\frac{\delta_*\mu(d)}{\varphi(d)}
\sum_{q\in\mathcal Q_R}\frac1q
\sum_{h\bmod qd\atop(h,d)=1}
 e\!\left(\frac{hP_j}{qd}\right)W_{qd}(h),
\]

Theorem 2.1 yields

\[
\boxed{
\sum_{j\in B}|T_{j,d}|^2
\ll
\frac{\delta_*^2}{\varphi(d)}
\sum_{q\in\mathcal Q_R}
\sum_{h\bmod qd\atop(h,d)=1}|W_{qd}(h)|^2.
}
\]

Thus the primorial orbit is controlled uniformly for each conductor. The centre side is no longer the unresolved part of the fixed-`d` problem.

## 3. Exact source-energy identity

Let

\[
L=H-Z.
\]

### Theorem 3.1

For `(q,d)=1`,

\[
\boxed{
\sum_{h\bmod qd\atop(h,d)=1}|W_{qd}(h)|^2
=
q
\sum_{t\in\mathbb Z\atop |qt|<L}
(L-|qt|)c_d(t).
}
\]

### Proof

Expand the square and sum in `h`. For two source points `m,n`, CRT gives

\[
\sum_{h\bmod qd\atop(h,d)=1}
 e\!\left(\frac{h(m-n)}{qd}\right)
=
q\mathbf1_{q\mid m-n}c_d(m-n).
\]

Since `(q,d)=1`, if `m-n=qt` then `c_d(m-n)=c_d(t)`. The number of ordered pairs in a consecutive interval of length `L` with difference `qt` is `L-|qt|`. \(\square\)

This is a nonnegative Fejér-weighted Ramanujan sum despite the signed expression on the right.

## 4. Universal interval-energy bound

For a consecutive interval of length `L` and modulus `M`, complete Fourier orthogonality gives

\[
\sum_{h=1}^{M-1}|W_M(h)|^2
=r(M-r),
\qquad
r\equiv L\pmod M,
\quad0\le r<M.
\]

Hence

\[
\sum_{h=1}^{M-1}|W_M(h)|^2
\le M\min(L,M).
\]

For `d>1`, the condition `(h,d)=1` excludes `h=0`, so

\[
\boxed{
\sum_{h\bmod qd\atop(h,d)=1}|W_{qd}(h)|^2
\le qd\min(L,qd).
}
\]

For `d=1`, the same estimate applies after the zero mode is combined with the explicit local centring rather than bounded separately.

## 5. What this frame does and does not solve

The theorem proves that **for every fixed conductor** the mesoscopic primorial orbit has a bounded synthesis norm. This is stronger than the previous prime-modulus orbit frame because it incorporates the composite hybrid modulus `qd` and remains uniform in `d`.

It does not prove `JIRP(X)`. There are two incompatible positive reductions:

1. **Sum the conductors first.**  The Ramanujan projector then reconstructs the candidate-prime source, and the argument returns to the already-proved factorised source/orbit loss.
2. **Diagonalize the conductors first.**  The fixed-conductor frame and complete-period Ramanujan orthogonality then remove the cross-conductor terms which must cancel the main-size `d=1` density drift.

The two useful orthogonalities therefore do not commute:

- orbit orthogonality is effective after fixing the source coefficients;
- Ramanujan orthogonality is effective under complete-period source sampling;
- the Fortune source requires their joint action before either family is diagonalized positively.

This is the **noncommuting-orthogonalities obstruction**.

## 6. Density coordinate remains supercritical

In a physical band, the separately treated density coordinate has row size

\[
\asymp\frac{H}{(\log X)(\log R)}.
\]

Its block square is therefore

\[
\asymp
K\frac{H^2}{(\log X)^2(\log R)^2}.
\]

At `R\asymp X` and `H\asymp X^2`, this exceeds the Fortune band scale by a factor of order

\[
\frac{X}{(\log X)^3}.
\]

Consequently no proof may apply Cauchy--Schwarz in `d` before the density coordinate has cancelled against the nontrivial Ramanujan spectrum.

## 7. Revised joint theorem

### Open theorem `JHGF(X)` — joint hybrid Gram frame

Prove directly, for the common-base expansion,

\[
\sum_{j\in B}
\left|
\sum_{q\in\mathcal Q_R}
\left[
\frac{\delta_*}{q}
\sum_{d\mid P_*}\frac{\mu(d)}{\varphi(d)}
\sum_{h\bmod qd\atop(h,d)=1}
 e\!\left(\frac{hP_j}{qd}\right)W_{qd}(h)
-
\frac{M_Z-1}{q-1}
\right]
\right|^2
\]

at diagonal scale with dyadically summable errors, **without** first diagonalizing either the conductor variable or the source/orbit variables.

`JHGF(X)` is an explicit common-base form of `JIRP(X)`.

## 8. Boundary

**PROVED EXACTLY**

1. fixed-conductor hybrid Gram kernel;
2. fixed-conductor Bessel frame uniform in `d`;
3. exact source-energy/Fejér--Ramanujan identity;
4. universal interval Fourier-energy bound;
5. independence of the collision kernel from the conductor.

**CLOSED AS POSITIVE ROUTES**

1. summing the conductors before applying the orbit frame;
2. applying conductorwise Cauchy or complete-period Ramanujan orthogonality before density cancellation;
3. treating the `d=1` density coordinate independently.

**OPEN**

1. the joint non-factorized hybrid Gram theorem `JHGF(X)`;
2. `JIRP(X)` and `BMST(X)`;
3. the Fortune variance theorem and Fortune's conjecture.
