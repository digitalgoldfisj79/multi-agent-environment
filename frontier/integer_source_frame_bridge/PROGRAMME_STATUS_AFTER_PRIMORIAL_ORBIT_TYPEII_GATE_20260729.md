# Programme status after the primorial-orbit Type-II gate

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

## Current status

The proposed next programme has been run through the critical Type-II, centre-orbit, high-conductor and literature gates. It produced two new frame theorems and one sharper obstruction. Fortune's conjecture remains **OPEN**.

## 1. New exact Type-II coordinate

For the additively centred bilinear progression discrepancy,

\[
\Delta_{j,p}^{+}
=
\sum_{u,v}\alpha_u\gamma_v
\left(\mathbf1_{uv\equiv-P_j\pmod p}-\frac1p\right),
\]

one has the exact inverse-orbit identity

\[
\boxed{
\Delta_{j,p}^{+}
=
\sum_u\alpha_u\frac1p
\sum_{\ell=1}^{p-1}
 e(\ell P_j\overline u/p)\widehat\gamma_p(\ell).
}
\]

The actual unit-residue centre differs by the explicit drift

\[
\Delta_{j,p}^{\times}
=
\Delta_{j,p}^{+}-\frac{(\sum_u\alpha_u)(\sum_v\gamma_v)}{p(p-1)}.
\]

Thus one complete Type-II variable can be fused with the consecutive-primorial centre before any inequality is applied.

## 2. New bounded inverse-orbit frame

For

\[
\Phi_{j,u}(p,\ell)=p^{-1}e(\ell P_j\overline u/p),
\]

the fixed-modulus Gram is

\[
G_p((j,u),(k,u'))
=
\frac1p\mathbf1_{p\mid P_j u'-P_k u}-\frac1{p^2}.
\]

If the `u` interval has length below `p`, every residue has multiplicity at most the centre-block size `K`. Therefore

\[
\|G_p\|_{\rm op}\le K/p,
\]

and

\[
\sum_{j,u}\left|\sum_{p,\ell}c_{p,\ell}\Phi_{j,u}(p,\ell)\right|^2
\le
K\left(\sum_p\frac1p\right)\sum_{p,\ell}|c_{p,\ell}|^2.
\]

Hence the combined centre-plus-one-variable synthesis is bounded on blocks

\[
K\ll\log X.
\]

This shorter block choice is compatible with the established freezing error.

## 3. The Type-II gate still fails after all reorderings

Putting `c_{p,\ell}=\widehat\gamma_p(\ell)` and using Parseval gives the generic bound

\[
\frac{KX^2}{(\log X)^2}
\|\alpha\|_2^2\|\gamma\|_2^2.
\]

At the balanced critical scale `UV\asymp H\asymp X^2`, this is

\[
KX^{4+o(1)}/(\log X)^2,
\]

whereas the Fortune block allowance is

\[
KX^3/\log X.
\]

The remaining loss is therefore

\[
X^{1-o(1)}/\log X.
\]

Compressing the `\alpha` coefficients into the centre Gram first gives the same estimate. There is no hidden gain from changing the order of frame and Cauchy. A successful theorem must use cancellation between both Type-II variables jointly and must exploit the actual arithmetic coefficients.

## 4. New high-conductor frame

For squarefree products `Q` of at least two first-band primes, put

\[
w(Q)=1/\varphi^\dagger(Q),
\]

and let `\rho_{j,Z}(Q)` be the unique representative of `-P_j\pmod Q` in `(Z,Z+Q]`.

For `j<k`, `P_k=L_{jk}P_j`, one has

\[
\rho_{j,Z}(Q)=\rho_{k,Z}(Q)
\iff
Q\mid L_{jk}-1.
\]

The weighted off-diagonal candidate Gram is exactly

\[
\prod_{p\mid L_{jk}-1\atop p\in\mathcal P_R}
\left(1+\frac1{p-2}\right)
-1-
\sum_{p\mid L_{jk}-1\atop p\in\mathcal P_R}\frac1{p-2},
\]

and is

\[
O((k-j+1)^2/X^2).
\]

Consequently

\[
\boxed{
\|\mathcal H\|_{\rm op}
\ll
(\log X)^{-2}+K^3/X^2.
}
\]

The high-conductor complete-model centre geometry is therefore small even for `K\ll\sqrt X`.

## 5. Why this does not close the high orders

The reciprocal weight `1/\varphi^\dagger(Q)` is the aggregate squared primitive-character coefficient. At the deterministic point, summing the character family reconstructs the unweighted divisibility indicator and removes this decay.

The frame proves that repeated candidate locations across primorial centres are not the obstruction. The remaining problem is whether the unique candidate is prime with the correct signed frequency, jointly with the physical first-order contribution.

## 6. Literature gate

The current large-modulus fixed-residue theorems, including the 2026 fixed-residue extension in arXiv:2602.20917, do not directly supply the required result:

1. their residue or shift is fixed, whereas `P_j` grows exponentially and varies with `j`;
2. the required estimate is an `L^2` theorem for a consecutive family of primorial shifts;
3. a rowwise error `H/(\log H)^A`, even if uniform here, misses the Fortune block scale by `X/(\log X)^{2A-1}` after squaring.

Thus the gap is polynomial, not another request for a larger logarithmic exponent.

## 7. New theorem-level obstruction

### `POTD(X)` -- primorial-orbit Type-II dispersion

For the actual balanced Type-II coefficient families, prove a same-band Bessel estimate

\[
\sum_{j\in B}
\left|\sum_{p\in\mathcal P_R}
\lambda_p\Delta_{j,p}^{\times}(\alpha,\gamma)\right|^2
\ll
\sum_{j,p}|\lambda_p\Delta_{j,p}^{\times}(\alpha,\gamma)|^2
+E_{B,R}^{\rm II},
\]

with Fortune-scale summable errors and with the signed Type-I/II recombination retained.

This theorem must save the factor `X^{1-o(1)}/\log X` that generic source Cauchy loses.

It must then be coupled to deterministic sampling of the one-point conductors. The complete remaining object is therefore:

\[
\boxed{
\text{joint bilinear primorial-orbit dispersion plus signed one-point conductor sampling}.
}
\]

## 8. Boundary

**PROVED EXACTLY**

- additive/unit Type-II drift identity;
- inverse-orbit factorization;
- combined centre--Type-II-variable Gram;
- fixed-modulus norm `K/p`;
- high-conductor candidate collision formula;
- small high-conductor complete-model frame.

**PROVED FROM CLASSICAL INPUT**

- bounded combined frame for `K\ll\log X`;
- generic frame/Cauchy loss `X^{1-o(1)}/\log X`;
- fixed rowwise logarithmic estimates are insufficient at the family-square scale.

**COMPUTATIONALLY VERIFIED**

- all exact identities on panels `X=11,17,23`;
- 84,816 inverse-orbit Gram checks;
- 6,246 high-conductor collision checks;
- finite coherent/diagonal Type-II ratios, with no asymptotic inference.

**CLOSED AS DIRECT ROUTES**

- centre-only frame;
- centre-plus-one-variable frame followed by generic Cauchy;
- fixed-shift rowwise large-modulus estimates;
- complete-model high-conductor energy as deterministic sampling;
- separate positive physical/high-conductor bounds.

**OPEN**

- `POTD(X)`;
- deterministic signed one-point conductor sampling;
- `MRPMD(X)` / `SBD(X)`;
- `NSMT(X)`, the Fortune variance theorem and Fortune's conjecture.

Authoritative note:

- `frontier/integer_source_frame_bridge/PRIMORIAL_ORBIT_TYPEII_AND_HIGH_CONDUCTOR_FRAME_20260729.md`
