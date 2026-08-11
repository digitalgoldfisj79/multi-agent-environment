# Fable addendum intake: orbit restriction and cross-modulus covariance

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`  
Reviewed mathematical head: `723737453feaf8530c93c4f6f64bcf3cdbd0c7b5`  
Review addendum: PR #33 issue comment `5127068265`

## Executive decision

The addendum is accepted, with two scope qualifications.

1. `PBDH_P(X)` is the correct all-residue physical variance and a necessary scale gate, but it is not the integer Fortune decision point.
2. The load-bearing integer statement is the restriction of those residue discrepancies to the deterministic primorial orbit, together with cancellation between distinct physical moduli.
3. The Keating--Rudnick function-field theorem establishes the all-residue physical variance in the laboratory ring. It does not by itself establish the primorial-orbit restriction or the signed higher-conductor transfer.
4. The published asymptotic large sieve is a serious lead, but its literal theorems do not reach the endpoint `N asymp Q^2` for the prime-conductor family required here.

Fortune's conjecture remains **OPEN**.

## 1. Accepted independent audit

The independent audit on branch `claude/fortunes-conjecture-mechanisms-fuuz4z` rechecked, without using the branch verifiers:

- `Lambda = mu_{<=Y} * c_Y` on the complete source range;
- completion of every true long cell to `psi(H;p,a)` for every residue;
- character collapse to the ordinary von Mangoldt character sum;
- isolation of `n=p` as the only non-unit source;
- the exact first-order coordinate

  \[
  A_{j,p}=-\frac{p-1}{p-2}D_p(-P_j)+\frac{\log p}{p-2};
  \]

- the centred determinant expansion of the prime-band variance.

The archived maximum discrepancy in the direct first-order identity is below `5.4e-15` on the audited panels. The audit also independently reproduces the scale diagnostics for `PBDH_P(X)` and the density obstruction to every uncentred determinant formulation.

The reviewer's uncentred `SDD(X)` box is therefore formally retracted. This branch will use centred determinant kernels only.

## 2. Why `PBDH_P(X)` is a scale gate

Write

\[
D_p(a)=\psi(H;p,a)-\frac{\Psi_p(H)}{p-1},
\qquad
\mathcal V_{\mathcal P_R}(H)
=\sum_{p\in\mathcal P_R}\sum_{a\in\mathbb F_p^\times}|D_p(a)|^2.
\]

The physical all-residue target is

\[
\boxed{
\mathrm{PBDH}_{\mathbb P}(X):
\quad
\mathcal V_{\mathcal P_R}(H)\ll HX\,X^{o(1)},
\qquad H=\eta X^2.
}
\]

For a block `B` of `K` primorial centres, typical-residue sampling predicts

\[
\sum_{j\in B}\sum_{p\in\mathcal P_R}|D_p(-P_j)|^2
\asymp
\frac KX\,\mathcal V_{\mathcal P_R}(H).
\]

If one then applies Cauchy across the `asymp X/log X` physical primes, the resulting first-order energy sits at the Fortune allowance, with no reserve for the higher-conductor covariance or cross-band recombination. Thus `PBDH_P(X)` prevents a power loss but does not settle the deterministic orbit.

## 3. The actual orbit gates

The programme now separates two statements that were previously conflated.

### 3.1 `PORS(X)` -- primorial-orbit residue sampling

For the physical weights `w_p=(p-1)/(p-2)`, prove

\[
\boxed{
\sum_{j\in B}\sum_{p\in\mathcal P_R}
 w_p^2|D_p(-P_j)|^2
\ll
\frac KX
\sum_{p\in\mathcal P_R}\sum_{a\in\mathbb F_p^\times}
 w_p^2|D_p(a)|^2\,X^{o(1)}.
}
\]

This is a deterministic sampling theorem: the consecutive primorial residues must not concentrate on atypically energetic residue classes.

### 3.2 `PORC(X)` -- primorial-orbit cross-modulus covariance

Prove

\[
\boxed{
\sum_{j\in B}
\left|\sum_{p\in\mathcal P_R}w_pD_p(-P_j)\right|^2
\ll
X^{o(1)}
\sum_{j\in B}\sum_{p\in\mathcal P_R}
 w_p^2|D_p(-P_j)|^2
+E_{\rm self}(B,R).
}
\]

The self term is the explicit drift already isolated in the exact first-order coordinate. The theorem must be stated with the actual block, physical band and source conventions; it is not an arbitrary-coefficient large-sieve assertion.

`PORC(X)` is the present decision point. A proof would show that the Cauchy modulus-count loss is artificial on the primorial orbit. A counterexample with coherence growing like `|\mathcal P_R|` would close the current route.

## 4. Standing covariance falsification test

The new standing verifier computes, for multiple consecutive-centre blocks,

\[
R_{\rm sample}
=
\frac{\sum_{j,p}|D_p(-P_j)|^2}
{K\sum_p (p-1)^{-1}\sum_a|D_p(a)|^2},
\]

\[
R_{\rm coh}
=
\frac{\sum_j|\sum_pD_p(-P_j)|^2}
{\sum_{j,p}|D_p(-P_j)|^2},
\]

and `R_total=R_sample R_coh`, against deterministic random-residue controls.

Committed panels use

- `X = 101, 199, 307, 503, 701, 1009`;
- six centre blocks per `X`;
- 128 random controls per block.

Across all 36 blocks:

- `R_sample` lies in `[0.8691, 1.1165]`;
- `R_coh` lies in `[0.1185, 1.9862]`;
- `R_total` lies in `[0.1165, 1.9037]`.

The largest physical bands in the panels contain hundreds of primes, so these ratios show no drift toward the Cauchy bound. The orbit samples the all-residue diagonal at random scale and its cross-modulus coherence is compatible with random controls.

This is **EMPIRICAL ONLY**. It is a falsification test, not evidence sufficient for `PORS(X)` or `PORC(X)`.

## 5. Function-field scope

Keating and Rudnick prove a function-field analogue of the Hooley variance for primes in arithmetic progressions, using Katz equidistribution. In the large-base limit their theorem gives the expected all-residue variance in the regime corresponding to `x=|Q|^beta`, `1<beta<2`.

This supports the following laboratory programme:

1. formulate the exact function-field counterpart of `PBDH_P(X)`;
2. identify the squarefree-modulus and degree range covered directly by Keating--Rudnick;
3. then define the function-field primorial orbit and test whether Katz equidistribution also controls `PORS_FF` and `PORC_FF`.

Only the first item is presently supplied by the published theorem. A proved function-field orbit-transfer theorem would be a genuinely new end-to-end model component.

## 6. Asymptotic-large-sieve scope

The Conrey--Iwaniec--Soundararajan asymptotic large sieve averages primitive characters over smoothly weighted moduli `q asymp Q`.

Its general theorem treats coefficient length below `Q^{1-epsilon}`. Its special long-polynomial theorem reaches `N <= Q^{2-epsilon}` under additional Euler-product structure. The Fortune physical endpoint has

\[
N=H\asymp Q^2,
\]

with moduli restricted to primes in a dyadic band and coefficients generated by the von Mangoldt source. Therefore the published theorem is not a black-box proof of `PBDH_P(X)`, `PORS(X)` or `PORC(X)`.

The concrete analytic question is now:

> Can the asymptotic large sieve be extended to the endpoint `N=cQ^2`, with prime conductors and the von Mangoldt coefficient family, while retaining the off-diagonal main term needed for orbit sampling?

A negative literal parameter audit would establish that this route needs a new endpoint theorem rather than a repackaging of existing technology.

## 7. Corrected hierarchy

### PROVED EXACTLY

- full-source completion and centred determinant reduction from the preceding sequence;
- exact first-order physical coordinate and self drift;
- exact signed physical/higher-conductor interface.

### PROVED IN THE FUNCTION-FIELD LITERATURE

- the all-residue physical variance analogue in the Keating--Rudnick large-base regime.

This does not include the primorial-orbit restriction.

### COMPUTATIONALLY VERIFIED

- the independent addendum audit of all new exact identities;
- the standing orbit covariance verifier on 36 finite blocks through `X=1009`.

### EMPIRICAL

- random-scale orbit sampling and cross-modulus coherence on the committed panels.

### OPEN

1. `PBDH_P(X)` -- all-residue prime-band scale gate;
2. `PORS(X)` -- deterministic primorial-orbit sampling;
3. `PORC(X)` -- cross-modulus covariance, the current decision point;
4. signed physical/higher-conductor contraction;
5. the function-field orbit-transfer theorem;
6. an endpoint prime-conductor asymptotic large sieve, or a proof that it is insufficient;
7. the first physical-band theorem, `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

## Verdict

The addendum is accepted. It does not weaken the repaired sequence; it identifies the correct theorem hierarchy. The physical variance is a necessary scale theorem. The decisive integer obstruction is deterministic primorial-orbit sampling with cross-modulus covariance, followed by signed one-point-conductor transfer.
