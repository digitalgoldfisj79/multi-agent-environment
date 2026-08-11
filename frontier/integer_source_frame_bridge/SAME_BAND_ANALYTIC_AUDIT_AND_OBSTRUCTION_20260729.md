# Same-band analytic audit and theorem-level obstruction

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the exact reductions below are **PROVED EXACTLY**; finite stress tests are **COMPUTATIONALLY VERIFIED**; the same-band theorem, the complete variance theorem and Fortune's conjecture are **OPEN**.

## 1. Exact common-source operator

Fix a mesoscopic block `B`, its common cutoff `Z=z_B`, and one dyadic prime band

\[
\mathcal Q_R=\{q:R<q\le\min(2R,H),\ q\text{ prime}\}.
\]

Let

\[
\mathcal M_Z=\{m:Z<m\le H,\ m\text{ prime}\},
\qquad M_Z=|\mathcal M_Z|.
\]

For `q\in\mathcal Q_R`, the corrected frozen discrepancy is

\[
D_j(q)=N_{P_j,Z}(q)-\frac{M_Z-1}{q-1},
\tag{1.1}
\]

where

\[
N_{P_j,Z}(q)=\#\{k:P_j+Z<qk\le P_j+H,\ (k,P_j)=1\}.
\]

Equivalently, by the quotient bijection,

\[
\boxed{
D_j(q)=
\sum_{m\in\mathcal M_Z\atop m\ne q}
\left(\mathbf1_{q\mid P_j+m}-\frac1{q-1}\right).
}
\tag{1.2}
\]

Put

\[
a_{j,q}=\beta_j\frac{q-1}{q-2}D_j(q),
\qquad
T_{B,R}(j)=\sum_{q\in\mathcal Q_R}a_{j,q}.
\tag{1.3}
\]

The open same-band estimate is

\[
\sum_{j\in B}|T_{B,R}(j)|^2
\ll
\sum_{j\in B}\sum_{q\in\mathcal Q_R}|a_{j,q}|^2+E_{B,R}.
\tag{1.4}
\]

## 2. Exact `TT^*`/dispersion identity

Define

\[
C_B(q,s)=\sum_{j\in B}a_{j,q}\overline{a_{j,s}}.
\tag{2.1}
\]

Then

\[
\boxed{
\sum_{j\in B}|T_{B,R}(j)|^2
=D_{B,R}+2\Re\sum_{q<s\atop q,s\in\mathcal Q_R}C_B(q,s),
}
\tag{2.2}
\]

where

\[
D_{B,R}=\sum_{j\in B}\sum_{q\in\mathcal Q_R}|a_{j,q}|^2.
\]

Using (1.2), the cross covariance is exactly

\[
\begin{aligned}
C_B(q,s)
={}&\frac{(q-1)(s-1)}{(q-2)(s-2)}
\sum_{j\in B}\beta_j^2
\sum_{m\in\mathcal M_Z\setminus\{q\}}
\sum_{n\in\mathcal M_Z\setminus\{s\}}\\
&\quad\times
\left(\mathbf1_{q\mid P_j+m}-\frac1{q-1}\right)
\left(\mathbf1_{s\mid P_j+n}-\frac1{s-1}\right).
\end{aligned}
\tag{2.3}
\]

Formula (2.3), not the diagonal, is the missing theorem. The established diagonal theorem proves

\[
\sum_R D_{B,R}\ll\frac{KHX}{\log X}.
\]

It gives no sign information on the aggregate `q\ne s` term in (2.2).

## 3. Sawtooth Fourier attack

The exact rough-quotient formula is

\[
\begin{aligned}
N_{P_j,Z}(q)
={}&\frac{H-Z}{q}\frac{\varphi(P_j)}{P_j}\\
&+\sum_{d\mid P_j}\mu(d)
\left[\psi\!\left(\frac{P_j+Z}{qd}\right)-\psi\!\left(\frac{P_j+H}{qd}\right)\right].
\end{aligned}
\tag{3.1}
\]

A Fourier mode has the exact factorization

\[
e\!\left(\frac{h(P_j+t)}{qd}\right)
=e\!\left(\frac{h(P_j/d)}q\right)e\!\left(\frac{ht}{qd}\right).
\tag{3.2}
\]

Thus the formally truncated signed divisor coefficient is

\[
\mathcal S_{j,q,t}(h)
=\sum_{d\mid P_j}\mu(d)
 e\!\left(\frac{h(P_j/d)}q\right)e\!\left(\frac{ht}{qd}\right).
\tag{3.3}
\]

### Proposition 3.1 — truncation barrier

A standard pointwise Fourier truncation of each sawtooth, followed by an absolute bound on the divisor-indexed remainder, is exponentially too large. Indeed

\[
\tau(P_j)=2^{\pi(z_j)},
\]

so any termwise remainder estimate loses at least the complete divisor count at the stage where the `\mu(d)` signs are discarded. A Vaaler or Fejér positive majorant has the same defect: positivity removes precisely the signed divisor cancellation that (3.1) introduced.

Therefore a useful truncation requires a new estimate for the **signed sum of the truncation remainders over `d\mid P_j`**. Neither the orbit-frame theorem nor the first-order diagonal theorem supplies such an estimate.

This is a theorem-level obstruction to applying double large sieve or reciprocal phase estimates mechanically after (3.1). The obstruction is not parity alone; it is the absence of a signed smooth-divisor truncation theorem.

## 4. What the standard operator tools reduce to

### Halász--Montgomery

Let `v_q=(a_{j,q})_{j\in B}`. Then (1.4) asks for

\[
\left\|\sum_{q\in\mathcal Q_R}v_q\right\|_2^2
\ll\sum_q\|v_q\|_2^2+E_{B,R}.
\]

Halász--Montgomery bounds this by row sums of the normalized Gram matrix `\langle v_q,v_s\rangle`. With only Cauchy--Schwarz one obtains

\[
\left\|\sum_qv_q\right\|_2^2
\le|\mathcal Q_R|\sum_q\|v_q\|_2^2,
\tag{4.1}
\]

losing `|\mathcal Q_R|\asymp R/\log R`. The method becomes useful only after a new cross-modulus estimate for (2.3) is supplied.

### Cotlar--Stein

Writing the band as a sum of modulus operators `T_q`, Cotlar--Stein requires summability of `\|T_q^*T_s\|^{1/2}`. The existing bounded orbit frame controls a single common additive synthesis operator after its coefficients are fixed; it does not control the common-source products `T_q^*T_s` for `q\ne s`. Source/orbit factorization reintroduces the proved factorised-frame loss.

### Linnik dispersion

Linnik dispersion expands exactly to (2.2)--(2.3). The diagonal is known. The remaining term is the signed correlation of two rough quotient intervals with independent prime moduli `q,s\asymp R`. No further cancellation follows from the identity itself.

### Double large sieve

Applying a double large sieve after absolute values in the divisor variable costs `2^{\pi(z_j)}`. Retaining the divisor signs leaves the exponential sum (3.3), for which no bound at the required scale is present in the merged package. Thus the double large sieve does not close any of the three physical ranges without a new signed divisor input.

## 5. Range-by-range result

### 5.1 Lower band: `R\asymp X`

The quotient interval has length `H/R\asymp X`. This is the longest and analytically most favourable physical interval. However, the sifting limit is also `z_j\asymp X`; a pointwise interval sieve has no spare level. Classical prime-progression mean-square input controls sums of individual modulus discrepancies, which is the already-proved diagonal scale. Cauchy in the modulus variable still loses `R/\log R` as in (4.1). The same-band estimate is therefore **OPEN** even at the lower endpoint.

### 5.2 Mesoscopic bands: `X^{1+\varepsilon}<R<X^{2-\varepsilon}`

Here

\[
X^{\varepsilon}\ll H/R\ll X^{1-\varepsilon}.
\]

The quotient interval is shorter than the full sifting range. The floor formula is exact, but positive sieve bounds or termwise Möbius bounds lose the required scale. The missing input is a signed averaged theorem for translated `P_j`-rough intervals, jointly over `j` and `q`.

### 5.3 Top band: `R\asymp H`

Now `H/q=O(1)`. Each `N_{P_j,Z}(q)` is a bounded integer determined by whether one or two residues near `-P_j\pmod q` cross the cutoff and remain `P_j`-rough. Smooth Fourier truncation cannot average this endpoint jump. The same-band theorem becomes a shrinking-target variance theorem for the reciprocal map

\[
q\longmapsto-P_j\pmod q
\]

over prime `q\asymp H`. The existing primorial-prefix collision theorem concerns collisions between centres at a fixed modulus; it does not prove this cross-modulus shrinking-target theorem.

## 6. Exact short-mechanism audit

### 6.1 Neighbouring-centre forcing

The recurrence `P_{j+1}=z_{j+1}P_j` gives no exact monotonicity or conservation law for `N_{P_j,Z}(q)`. Multiplication changes the reciprocal residue modulo every new prime `q`. The finite panels contain adjacent rows with both sign reversals and unequal magnitudes in the same band. Therefore a deterministic “one failed centre forces the same anomaly at its neighbour” rule is **EMPIRICALLY REJECTED**. A statistical correlation theorem remains possible but would itself be new input.

### 6.2 Hyperbola symmetry

The formal exchange `q\leftrightarrow k` does not preserve the physical domain. Since `q\le H`,

\[
k>\frac{P_j+Z}{H}.
\]

Because `P_j=\exp((1+o(1))X)` while `H\asymp X^2`, one has `k>H` for all sufficiently large `X`. Hence the exchanged variable lies outside the physical prime band `(Z,H]`. There is no same-band involution. This route is **REJECTED EXACTLY**.

### 6.3 Smooth-divisor projector or telescoping

Changing variables `u=P_j/d` in one Fourier mode gives

\[
\sum_{d\mid P_j}\mu(d)e\!\left(\frac{h(P_j+t)}{qd}\right)
=\mu(P_j)\sum_{u\mid P_j}\mu(u)e\!\left(\frac{hu}{q}+\frac{htu}{qP_j}\right).
\tag{6.1}
\]

This is not the established Ramanujan projector

\[
\frac{\varphi(P_j)}{P_j}\sum_{d\mid P_j}\frac{\mu(d)}{\varphi(d)}c_d(m).
\]

The coefficients, kernels and denominators differ. The existing projector cannot be substituted into (6.1), and no telescoping follows from divisor inclusion. Finite exact values are non-idempotent and vary with both endpoint and modulus. The proposed reuse of the existing projector is **REJECTED EXACTLY**; a new primorial-divisor exponential-sum theorem remains conceivable.

### 6.4 Least-rough-factor stopping time

Ordering the factors of `k` above `z_j` by their least factor gives an exact Buchstab decomposition. It is the quotient-side image of the existing ordered Buchstab expansion. The identity partitions the same rough set but supplies no new orthogonality or `L^2` contraction. As an identity-only improvement this route is **REJECTED EXACTLY**.

### 6.5 Selberg/duality shortcut

Hilbert-space duality converts (1.4) into a bound for the Gram form `(C_B(q,s))_{q,s}` against the all-ones vector. It does not estimate the off-diagonal entries. With the currently proved inputs it reduces to (4.1). Thus duality is an equivalent formulation, not a proof. The identity-only route is **REJECTED EXACTLY**.

## 7. Finite diagnostics

The exact finite verifier checks:

1. the generalized cutoff `Z\ge z`;
2. quotient transport and the Möbius-floor identity;
3. the sawtooth formula in exact rational arithmetic;
4. the exact dyadic partition and recombination;
5. outer Cauchy;
6. finite same-band ratios, labelled only **EMPIRICAL**.

On the committed complete panels `X=7,11,13,17`, the largest observed same-band ratio is below `3`. This supports plausibility but supplies no uniform constant and no asymptotic theorem.

## 8. Rigorously identified theorem-level obstruction

After the rough-quotient and same-band reductions, the remaining physical first-order problem is exactly the following new theorem.

### Open theorem `SBD(X)`

Uniformly for every mesoscopic primorial block `B` of size `K\ll\sqrt X` and every physical dyadic prime band `R<q\le2R`, prove a signed cross-modulus dispersion bound

\[
2\Re\sum_{q<s}C_B(q,s)\ll D_{B,R}+E_{B,R},
\]

with dyadically summable errors at the Fortune scale.

The merged package supplies:

1. the exact diagonal `D_{B,R}`;
2. bounded centre-orbit Gram for a fixed coefficient family;
3. exact rough-quotient and signed divisor representations;
4. no-go theorems for positive, support-only and factorised-frame estimates.

It does **not** supply either of the two inputs that would close `SBD(X)`:

1. a signed smooth-divisor Fourier truncation theorem for (3.3); or
2. a direct joint rough-interval covariance theorem for (2.3).

All listed Phase B and Phase C mechanisms reduce to one of these two missing inputs or lose at least `R/\log R` or `2^{\pi(X)}`. This is the current **THEOREM-LEVEL OBSTRUCTION**.

## 9. Reinsertion boundary

Phase D cannot be claimed complete because the physical first-order gate remains open. Moreover separate first-order control is a sufficient route, not a logically necessary one: the exact Euler--Buchstab detector allows coherent cross covariance between the zeroth, physical first-order, sparse first-order and higher-order terms.

The next viable alternatives are therefore:

1. prove `SBD(X)` by a genuinely new signed divisor or rough-interval dispersion theorem; or
2. abandon separate first-order control and attack the complete centred detector with the normalized rough coordinate and Buchstab tail reinserted from the start.

Neither alternative is completed here. Fortune's conjecture remains **OPEN**.
