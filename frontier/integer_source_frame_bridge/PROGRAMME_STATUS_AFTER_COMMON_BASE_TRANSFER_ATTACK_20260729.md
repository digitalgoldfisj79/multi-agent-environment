# Programme status after the common-base transfer attack

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the requested programme has been executed through all five proposed stages. It produced new exact reductions and a new uniform fixed-conductor frame, but not the Fortune variance theorem. Fortune's conjecture remains **OPEN**.

## 1. Stage one — spectral conductor concentration

The exact Ramanujan coefficient law is now identified as a probability measure:

\[
\mathbb P(D=d)=|\lambda_P(d)|,
\]

under which each prime `p\mid P` enters `D` independently with probability `1/p`.

Rankin--Markov with the classical Mertens estimate proves

\[
\sum_{d>z^A}|\lambda_P(d)|\ll e^{-A},
\qquad
\sum_{d>z^A}|\lambda_P(d)|^2\varphi(d)
\ll \frac{\varphi(P)}P e^{-A}.
\]

This proves the proposed conductor concentration theorem.

A necessary correction also emerged: this is complete-period/model-energy concentration. It does not permit deterministic truncation of the moving quotient intervals without a sampling-transfer theorem. Finite panels show pointwise and block-energy concentration can be much worse than complete-period energy.

## 2. Stronger exact result — common-base collapse

For every mesoscopic block, let `P_*` be its first primorial. Then for every later centre `P_j`, every physical prime `q`, and every quotient integer in the corrected interval,

\[
(k,P_j)=1\iff(k,P_*)=1.
\]

Thus all centres in the block use one common roughness function and one common Ramanujan coefficient system. The moving smooth-divisor spectrum has been removed exactly, not approximately.

This is a genuine simplification of `JIRP(X)`.

## 3. Stage two — truncated joint Gram

The common projector yields the exact hybrid representation

\[
N_j(q)
=
\frac{\delta_*}{q}
\sum_{d\mid P_*}\frac{\mu(d)}{\varphi(d)}
\sum_{h\bmod qd\atop(h,d)=1}
 e\!\left(\frac{hP_j}{qd}\right)W_{qd}(h).
\]

For every fixed conductor `d`, a new frame theorem is proved:

\[
\sum_{j\in B}
\left|
\sum_{q,h}
\frac{c_{q,h}}{q\sqrt{\varphi(d)}}
 e\!\left(\frac{hP_j}{qd}\right)
\right|^2
\ll
\left(1+\frac{K^2}{X}\right)
\sum_{q,h}|c_{q,h}|^2.
\]

Its Gram kernel is exactly

\[
\mathcal K_{jk}^{(d)}
=
\sum_{q\mid P_j-P_k}\frac1q,
\]

independent of `d`. Therefore the primorial-centre geometry is controlled uniformly at every fixed conductor.

The exact source energy is also reduced to a Fejér-weighted Ramanujan sum.

## 4. Stage three — does the hybrid frame close?

No. The obstruction is now sharper.

- Summing the conductors first reconstructs the candidate-prime source and returns to the known factorised source/orbit loss.
- Diagonalizing the conductors first destroys the main-size cancellation between the density coordinate and nontrivial Ramanujan spectrum.
- The density coordinate by itself is supercritical by a factor of order `X/(log X)^3` in the lower physical bands.

The orbit frame and Ramanujan orthogonality are each valid, but they cannot be applied sequentially. Their cancellation must occur jointly. This is the **noncommuting-orthogonalities obstruction**.

The remaining physical theorem is the explicit common-base joint hybrid Gram estimate `JHGF(X)`, equivalent in target strength to `JIRP(X)`.

## 5. Stage four — sparse one-point Carleson attack

The full Euler process is rewritten exactly as a normalized survivor martingale:

\[
M_R(n)=V(z,R)^{-1}\mathbf1_{(n,\Pi(z,R))=1}.
\]

A top-tail band increment has the exact decomposition

\[
B(n)
=
M_H(n)(A-1)
-
M_H(n)A\mathbf1_{\text{tail hit}}.
\]

The tail hit has one-point support, but the first term is a dense normalization drift of the same main size. These two terms cancel.

Finite panels make the failure decisive. For example:

- at `X=11`, total top-tail block energy is approximately `9.84`, while drift and hit energies are approximately `288.87` and `350.90`, with cross term approximately `-629.92`;
- at `X=13`, total energy is approximately `18.41`, while drift and hit energies are approximately `686.58` and `620.88`, with cross term approximately `-1289.05`.

These are empirical diagnostics, but the drift/hit algebra is exact. A separate positive sparse Carleson bound therefore cannot be glued to the physical estimate.

## 6. Stage five — martingale square-function transfer

The final theorem is now expressed directly through normalized sifted survivor counts.

### Open theorem `NSMT(X)`

Transfer the complete-CRT martingale square function to the deterministic candidate-prime/primorial sample:

\[
\sum_{j\in B}
\left|
\sum_\ell\mathcal B_{j,\ell}
+
\text{zeroth-centred coordinate}
\right|^2
\ll
KHX\,L(X),
\qquad L(X)=o(\log X).
\]

This must preserve:

1. density/nontrivial-conductor cancellation in physical bands;
2. normalization-drift/sparse-hit cancellation in tail bands;
3. cross-band martingale covariance;
4. primorial-prefix collision rigidity.

`NSMT(X)` is an explicit normalized-sieve form of `BMST(X)`.

## 7. What was genuinely closed

The programme has now removed:

1. moving roughness projectors across a mesoscopic block;
2. exponential coefficient-count loss as an intrinsic obstruction;
3. fixed-conductor primorial-orbit growth;
4. uncertainty about the correct top-tail decomposition;
5. the proposed support-only sparse-tail route;
6. the proposed sequential use of Ramanujan and orbit orthogonality.

## 8. Current theorem-level obstruction

The remaining theorem is not another identity. It is a deterministic transfer principle that must make two model cancellations hold simultaneously on the actual primorial sample:

- cross-conductor cancellation in the common-base hybrid physical system (`JHGF(X)`);
- cross-band normalized-survivor cancellation in the full Euler martingale (`NSMT(X)`).

A proof of `JHGF(X)` would supply the physical component of `NSMT(X)`. It would not justify an independently positive tail bound; the tail must remain centred inside the martingale.

No proof or refutation of these transfer theorems was obtained. Further progress requires a genuinely new joint source--conductor sampling theorem, not additional algebraic compression or a routine application of the existing large sieve, Cotlar, dispersion, Ramanujan orthogonality or sparse-support estimates.

## 9. Labels

**PROVED EXACTLY**

- common-base quotient collapse;
- common Ramanujan projector;
- conductor probability law;
- joint `qd` Fourier representation;
- fixed-conductor hybrid frame and Gram;
- normalized survivor martingale and drift/hit decomposition.

**PROVED FROM CLASSICAL INPUT**

- exponential conductor concentration.

**COMPUTATIONALLY VERIFIED**

- all new exact identities on finite panels.

**EMPIRICAL ONLY**

- conductor-truncation and top-tail energy ratios.

**OPEN**

- `JHGF(X)` / `JIRP(X)`;
- `NSMT(X)` / `BMST(X)`;
- the Fortune variance theorem;
- Fortune's conjecture.
