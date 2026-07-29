# Programme status after the next two levels

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: both requested levels have been executed through theorem-level boundaries. Fortune's conjecture remains **OPEN**.

## 1. Level one — signed same-band covariance

The termwise Möbius--sawtooth route still fails because discarding signs costs the full smooth-divisor count. A different exact expansion has now been proved:

\[
\mathbf1_{(k,P)=1}
=
\frac{\varphi(P)}P
\sum_{d\mid P}\frac{\mu(d)}{\varphi(d)}c_d(k).
\]

Its coefficients satisfy

\[
\sum_{d\mid P}|\lambda_P(d)|=1,
\qquad
\sum_{d\mid P}|\lambda_P(d)|^2\varphi(d)=\frac{\varphi(P)}P.
\]

Therefore the raw `2^{pi(X)}` coefficient explosion is not intrinsic. The exact quotient count is an incomplete Ramanujan projector on the moving interval

\[
(P+Z)/q<k\le(P+H)/q.
\]

This is real progress: the signed smooth-divisor system now has a finite natural coefficient budget.

The new obstruction is sharper. The `d=1` density term and the `d>1` Ramanujan spectrum each have main-size contributions and must cancel jointly. Complete-period Ramanujan orthogonality does not control the microscopic moving intervals. The remaining first-level theorem is `JIRP(X)`, a joint incomplete Ramanujan-projector estimate across primorial centres and same-band prime moduli.

`JIRP(X)` is an exact reformulation/refinement of `SBD(X)`, not a proof of it.

## 2. Level two — full detector reinsertion

The complete Euler detector has been reinserted as exact ordered and dyadic band increments:

\[
\prod_{z<r\le Y}(1+\xi_r)-1
=
\sum_\ell
M_{\ell-1}
\left(
\prod_{r\in\mathcal R_\ell}(1+\xi_r)-1
\right).
\]

Under the complete candidate-residue CRT measure these increments have mean zero, are pairwise orthogonal across bands and satisfy an exact quadratic-variation identity. This preserves physical, tail-prime and higher-order factor-cluster cancellation inside one martingale system.

The actual candidate-prime source is not the complete CRT measure. The remaining second-level theorem is `BMST(X)`: transfer this martingale cancellation to the deterministic prime-offset sample along mesoscopic blocks of consecutive primorial centres, at total scale

\[
KHX\,L(X),
\qquad L(X)=o(\log X).
\]

Summed over blocks, this is the full Fortune variance theorem.

## 3. Finite audit

The committed verifier checks exactly:

1. the Ramanujan projector and coefficient identities;
2. complete-period Ramanujan orthogonality;
3. the incomplete quotient-interval identity;
4. the Euler band telescope;
5. complete-CRT martingale orthogonality and quadratic variation.

Small full-chaos panels at `X=7,11,13,17` show complete-to-physical energy ratios between approximately `0.024` and `37.117`, with cross-covariances of both signs. These are empirical diagnostics only. They rule out a monotone-contraction reinsertion argument.

## 4. Technology audit

The newest bilinear Kloosterman-sum result of Blomer--Pascadi (`arXiv:2607.24311`) and the 2026 Kloosterman-fraction results of Dong--Robles--Zeindler (`arXiv:2601.00292`) and Wright (`arXiv:2604.25177`) do not directly match the exact system. Their settings use fixed-modulus or long dyadic convolution geometry; the Fortune source has primorial divisors, modulus-dependent numerators, microscopic moving quotient intervals, density/spectrum cancellation and a one-point top tail.

No direct published black-box theorem closing `JIRP(X)` or `BMST(X)` was identified.

## 5. Current critical path

The programme has passed from a diffuse same-band obstruction to two nested, explicit sampling theorems:

1. `JIRP(X)`: deterministic incomplete Ramanujan-projector cancellation for the physical same-band layer;
2. `BMST(X)`: deterministic transfer of the complete Euler--Buchstab martingale, incorporating the physical layer, sparse tail and higher chaos.

The preferred final target is `BMST(X)`. A proof of `JIRP(X)` would supply its physical-band input, but separate physical control is sufficient rather than logically necessary.

## 6. Stop condition

No proof or refutation of Fortune has been obtained. Both requested levels have been run to a precise theorem-level boundary. Further progress requires a genuinely new deterministic sampling theorem, not another exact identity or routine application of the currently audited operator tools.
