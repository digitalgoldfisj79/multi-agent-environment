# Common-base quotient projector and conductor concentration

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the common-base collapse, common Ramanujan projector, conductor probability law, exponential conductor-tail estimate and joint `qd` Fourier representation below are **PROVED EXACTLY** or from classical Mertens input as labelled. The deterministic incomplete-interval sampling theorem remains **OPEN**.

## 1. Setup

Let `B` be one mesoscopic block of consecutive primorial centres. Write

\[
P_*\mid P_j,
\qquad j\in B,
\]

where `P_*` is the first primorial in the block, with largest prime factor `z_*`. Put

\[
Z=\max_{j\in B}z_j,
\qquad
z_*<Z<H<(z_*^+)^2.
\]

For a physical prime `q>Z`, define

\[
I_j(q)=\left\{k:\frac{P_j+Z}{q}<k\le\frac{P_j+H}{q}\right\}.
\]

The previously corrected quotient count is

\[
N_j(q)=\#\{k\in I_j(q):(k,P_j)=1\}.
\]

## 2. Exact common-base collapse

### Theorem 2.1

For every `j\in B`, every physical prime `q>Z`, and every `k\in I_j(q)`,

\[
\boxed{(k,P_j)=1\iff(k,P_*)=1.}
\]

Consequently,

\[
\boxed{N_j(q)=\#\{k\in I_j(q):(k,P_*)=1\}.}
\]

### Proof

The forward implication is immediate from `P_*\mid P_j`.

For the reverse implication, put

\[
m=qk-P_j.
\]

Then `Z<m\le H`. Since `P_*\mid P_j` and `(q,P_*)=1`, the assumption `(k,P_*)=1` gives `(m,P_*)=1`. The interval condition

\[
z_*<m\le H<(z_*^+)^2
\]

therefore forces `m` to be prime. Since `m>Z\ge z_j`, one has `(m,P_j)=1`. Coprimality transport for `m=qk-P_j` then gives `(k,P_j)=1`. \(\square\)

This removes the moving primorial from the quotient roughness condition. Every centre in the block uses one common periodic roughness function.

## 3. Common Ramanujan projector

Put

\[
\delta_* = \frac{\varphi(P_*)}{P_*},
\qquad
\lambda_*(d)=\delta_*\frac{\mu(d)}{\varphi(d)},
\qquad d\mid P_*.
\]

The exact roughness projector is

\[
\mathbf1_{(k,P_*)=1}
=
\sum_{d\mid P_*}\lambda_*(d)c_d(k).
\]

By Theorem 2.1,

\[
\boxed{
N_j(q)=
\sum_{d\mid P_*}\lambda_*(d)
\sum_{k\in I_j(q)}c_d(k).
}
\]

Thus the divisor coefficient system is now independent of `j`. Only the translated incomplete intervals retain the centre dependence.

## 4. Exact conductor probability law

Since `P_*` is squarefree,

\[
|\lambda_*(d)|=\frac{\delta_*}{\varphi(d)}.
\]

The coefficient identities imply

\[
\sum_{d\mid P_*}|\lambda_*(d)|=1,
\]

and

\[
|\lambda_*(d)|^2\varphi(d)
=
\delta_*|\lambda_*(d)|.
\]

Hence the normalized quadratic-energy law is exactly the same probability measure as the absolute coefficient law:

\[
\boxed{
\mathbb P_*(D=d)=|\lambda_*(d)|
=
\frac{|\lambda_*(d)|^2\varphi(d)}{\delta_*}.
}
\]

This law factorizes over the primes `p\mid P_*`. A prime `p` is included in the random divisor `D` independently with probability

\[
\boxed{\mathbb P_*(p\mid D)=\frac1p.}
\]

Indeed, the local weights are `1-1/p` for exclusion and `1/p` for inclusion.

## 5. Conductor concentration

### Theorem 5.1

There is an absolute constant `C` such that, for every `A\ge0`,

\[
\boxed{
\sum_{d\mid P_*\atop d>z_*^A}|\lambda_*(d)|
\le Ce^{-A},
}
\]

and

\[
\boxed{
\sum_{d\mid P_*\atop d>z_*^A}
|\lambda_*(d)|^2\varphi(d)
\le C\delta_*e^{-A}.
}
\]

### Proof

Take `\theta=1/\log z_*`. Under the probability law of Section 4,

\[
\mathbb E_*(D^\theta)
=
\prod_{p\le z_*}
\left(1+\frac{p^\theta-1}{p}\right).
\]

For `p\le z_*`, one has `p^\theta\le e` and

\[
p^\theta-1\le e\theta\log p.
\]

Therefore

\[
\log\mathbb E_*(D^\theta)
\le
\frac e{\log z_*}
\sum_{p\le z_*}\frac{\log p}{p}
=O(1),
\]

using the classical Mertens estimate

\[
\sum_{p\le z}\frac{\log p}{p}=\log z+O(1).
\]

Markov's inequality gives

\[
\mathbb P_*(D>z_*^A)
\le
z_*^{-A\theta}\mathbb E_*(D^\theta)
\ll e^{-A}.
\]

The first claim follows because `\mathbb P_*(D=d)=|\lambda_*(d)|`. The second follows from

\[
|\lambda_*(d)|^2\varphi(d)=\delta_*|\lambda_*(d)|.
\]

\(\square\)

### Qualification

This is a complete-period or model-energy theorem. It does **not** by itself justify deleting the high-conductor terms on the deterministic moving intervals `I_j(q)`. The omitted projector can have large pointwise values even when its complete-period mean square is small.

To make the tail `o(1)` by conductor truncation alone requires `A\to\infty`; the corresponding cutoff `z_*^A` then grows beyond every fixed polynomial if `A` grows. A fixed polynomial cutoff captures all but an arbitrarily small fixed proportion of model energy, but not an asymptotically vanishing proportion unless its exponent grows.

## 6. Exact joint `qd` Fourier representation

Define

\[
W_M(h)=\sum_{Z<m\le H}e(hm/M).
\]

### Theorem 6.1

For every `j\in B` and physical prime `q>Z`,

\[
\boxed{
N_j(q)
=
\frac{\delta_*}{q}
\sum_{d\mid P_*}\frac{\mu(d)}{\varphi(d)}
\sum_{h\bmod qd\atop(h,d)=1}
 e\!\left(\frac{hP_j}{qd}\right)W_{qd}(h).
}
\]

### Proof

Insert the common projector into the count over `k`, or equivalently write `m=qk-P_j` and impose `q\mid P_j+m` by additive orthogonality. For `d\mid P_*\mid P_j` and `(q,d)=1`, multiplication by `q` permutes the reduced residues modulo `d`, so the Ramanujan phase may be written in the `m` variable.

The pair

\[
a\bmod d,\quad(a,d)=1,
\qquad
b\bmod q
\]

maps bijectively to

\[
h=aq+bd\bmod qd,
\qquad(h,d)=1.
\]

Because `d\mid P_j`, the combined centre and source phase is

\[
e\!\left(\frac{b(P_j+m)}q+\frac{am}d\right)
=
e\!\left(\frac{h(P_j+m)}{qd}\right).
\]

Summing over `m` gives the stated formula. \(\square\)

This is the exact hybrid kernel requested by the programme. It keeps the density coordinate and nontrivial Ramanujan spectrum in one expression and freezes the divisor system across the block.

## 7. Why conductor concentration does not close the Gram

Let

\[
R_{>D}(k)=
\sum_{d\mid P_*\atop d>D}\lambda_*(d)c_d(k).
\]

Complete-period orthogonality gives exactly

\[
\frac1{P_*}\sum_{k\bmod P_*}|R_{>D}(k)|^2
=
\sum_{d>D}|\lambda_*(d)|^2\varphi(d).
\]

Theorem 5.1 therefore gives a small **uniform-residue mean square**. The actual sample, however, consists of the short translated intervals `I_j(q)` and is not known to be equidistributed modulo `P_*` or modulo the conductors `d`.

Applying positive Cauchy--Schwarz in `d` is also insufficient. It diagonalizes the Ramanujan spectrum and destroys the main-size cancellation between the `d=1` density coordinate and the `d>1` spectrum. The density coordinate by itself exceeds the Fortune scale in the lower physical bands by a factor of order `X/(\log X)^3`.

Thus the concentration theorem supplies a finite-energy basis and a rigorous tail law, but using it requires the same missing deterministic sampling transfer that `JIRP(X)` and `BMST(X)` were designed to express.

## 8. Revised analytic target

The first-level target may now be stated with one common projector.

### Open theorem `CB-JIRP(X)`

For every mesoscopic block `B`, with common base `P_*`, and every physical dyadic prime band, prove the same-band second-moment estimate for the locally centred counts

\[
N_j(q)=
\sum_{d\mid P_*}\lambda_*(d)C_d(I_j(q)),
\]

while retaining cancellation between the density coordinate and the nontrivial conductors.

The theorem must control the deterministic translated intervals, not merely the complete-period Ramanujan energy. It is equivalent in final strength to `JIRP(X)`, but it removes the moving divisor coefficient system from the problem.

## 9. Boundary

**PROVED EXACTLY**

1. common-base quotient roughness collapse;
2. one common Ramanujan projector across every mesoscopic block;
3. exact conductor probability law with independent inclusion probability `1/p`;
4. exact relation between coefficient mass and quadratic energy;
5. exact joint `qd` Fourier representation.

**PROVED FROM CLASSICAL INPUT**

1. exponential conductor-tail estimate from Mertens and Rankin--Markov.

**COMPUTATIONALLY VERIFIED**

1. common-base collapse and projector identities on complete finite panels;
2. joint `qd` Fourier formula;
3. complete-period conductor-tail energy.

**EMPIRICAL ONLY**

Finite panels show that low/high conductor block energies have cross terms of both signs and that truncation is not a monotone `L^2` contraction.

**OPEN**

1. deterministic incomplete-interval sampling for the common projector;
2. `CB-JIRP(X)` / `JIRP(X)`;
3. full martingale transfer `BMST(X)`;
4. the Fortune variance theorem and Fortune's conjecture.
