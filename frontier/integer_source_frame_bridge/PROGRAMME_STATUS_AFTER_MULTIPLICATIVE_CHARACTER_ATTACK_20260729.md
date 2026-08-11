# Programme status after the multiplicative-character attack

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the full survivor band now has both an exact complete-CRT centre Gram and an exact primitive-character spectral expansion. The higher-conductor source energy is proved small in its natural weighted norm. A factorized source/centre proof is ruled out by an exact exponential lower bound. The remaining theorem is a signed joint hybrid character transfer. Fortune's conjecture remains **OPEN**.

## 1. New spectral theorem

For

\[
\Pi_R=\prod_{p\in\mathcal P_R}p,
\qquad
\varphi^\dagger(Q)=\prod_{p\mid Q}(p-2),
\]

the normalized survivor satisfies, for source and centre units modulo the band,

\[
V_R^{-1}\mathbf1_{(P_j+m,\Pi_R)=1}
=
\sum_{Q\mid\Pi_R}
\frac{\mu(Q)}{\varphi^\dagger(Q)}
\sum_{\chi\bmod Q}^{\dagger}
\chi(m)\overline{\chi(-P_j)}.
\]

The dagger sum runs over primitive characters of exact squarefree conductor `Q`.

Its nonconstant quadratic coefficient mass is exactly

\[
V_R^{-1}-1,
\]

which is the diagonal complete-CRT survivor variance. Its character-level absolute mass is `2^{|\mathcal P_R|}`, so the cross-conductor signs cannot be discarded.

## 2. Low and high conductors

At the Fortune scale `H=\eta X^2`, every conductor with at least two band primes satisfies `Q>H`. Hence:

- `Q=p` is the complete low-conductor/physical layer;
- every higher Euler order is in `Q>H`.

For `Q>H`, complete character orthogonality on an interval of length `H` gives

\[
\sum_{\chi\bmod Q}^{\dagger}
\left|\sum_m a_m\chi(m)\right|^2
\le
\varphi(Q)\sum_m|a_m|^2.
\]

After the exact survivor coefficient is inserted,

\[
\sum_{Q>H}
\frac1{\varphi^\dagger(Q)^2}
\sum_{\chi\bmod Q}^{\dagger}
\left|\sum_m a_m\chi(m)\right|^2
\ll
\frac1{\log R}\sum_m|a_m|^2.
\]

Thus the high-order source spectrum is already controlled at its natural scale.

## 3. Exact factorization no-go

For any multiplicative scalar split

\[
\frac1{p-2}=a_pb_p,
\]

the centre and source diagonal masses have local product

\[
(1+x_p)(1+x_p^{-1})\ge4,
\qquad
x_p=(p-2)|a_p|^2.
\]

Therefore

\[
\mathfrak C(a)\mathfrak S(b)
\ge
4^{|\mathcal P_R|}.
\]

No scalar Cauchy redistribution can simultaneously exploit the bounded centre Gram and the small weighted source energy. This closes the positive route through separate multiplicative-character large sieves.

## 4. Remaining theorem

The exact spectral form of the arithmetic transfer is `SMHLS(X)`, the signed Möbius hybrid large sieve. It must estimate jointly

\[
\sum_{Q\mid\Pi_R,\ Q>1}
\frac{\mu(Q)}{\varphi^\dagger(Q)}
\sum_{\chi\bmod Q}^{\dagger}
\sum_{j\in B}c_j\overline{\chi(-P_j)}
\sum_m a_{j,m}\chi(m),
\]

while preserving:

- cross-conductor Möbius cancellation;
- candidate-prime source phases;
- primorial centre phases;
- previous-band survivor weights;
- reduced-band self coordinates and zeroth/self drift.

`SMHLS(X)` is the spectral form of `PCRST(X)`, not a second independent missing theorem.

Sparse-modulus large-sieve results control positive conductorwise energies and require distribution conditions on their modulus sets. They do not provide this signed cross-conductor tensor estimate.

## 5. Current boundary

**PROVED EXACTLY**

- common-base and full Euler reductions;
- normalized-survivor martingale identities;
- complete-CRT all-order survivor Gram;
- exact self-coordinate decomposition;
- Hilbert complement-divisor identity;
- primitive-character survivor expansion;
- exact coefficient energies;
- low/high conductor separation;
- high-conductor source inequality;
- multiplicative scalar-factorization no-go.

**OPEN**

- `SMHLS(X)` / `PCRST(X)`, the signed deterministic source-centre transfer;
- arithmetic `NSMT(X)`;
- the Fortune variance theorem;
- Fortune's conjecture.

Authoritative notes:

- `frontier/integer_source_frame_bridge/COMPLETE_CRT_SURVIVOR_GRAM_AND_SAMPLING_BOUNDARY_20260729.md`
- `frontier/integer_source_frame_bridge/MULTIPLICATIVE_CHARACTER_SURVIVOR_EXPANSION_20260729.md`
