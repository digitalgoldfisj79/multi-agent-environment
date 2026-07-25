# Affine-group torsor calibration of the cubic Airy origin

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** cubic-origin fibre of the affine hook Fourier/Smith-defect complex.  
**Status:** **PROVED** for primes `p=5 mod 6`, in every Frobenius degree.

## 1. The affine trace-constraint locus

Let `q=p^r`, `L=F_(q^p)`, and consider degree-`p` elements

\[
\alpha\in L\setminus\mathbf F_q
\]

satisfying

\[
\operatorname{Tr}(\alpha)
=
\operatorname{Tr}(\alpha^2)
=
\operatorname{Tr}(\alpha^3)=0.
\]

The affine root-change group

\[
\operatorname{Aff}_1(\mathbf F_q)
=
\mathbf F_q\rtimes\mathbf F_q^*
\]

acts by

\[
\alpha\longmapsto a\alpha+b.
\]

The three trace conditions are preserved. For example,

\[
\operatorname{Tr}((a\alpha+b)^j)
\]

is a triangular combination of the lower traces, and every constant term is multiplied by the extension degree `p`, hence vanishes in characteristic `p`.

## 2. Freeness on the degree-p sector

Suppose

\[
a\alpha+b=\alpha.
\]

If `a!=1`, then

\[
\alpha=-\frac b{a-1}\in\mathbf F_q,
\]

contrary to `deg(alpha)=p`. Therefore `a=1`, and then `b=0`.

Thus

\[
\boxed{
\operatorname{Aff}_1(\mathbf F_q)
\text{ acts freely on the degree-p trace-constraint locus.}
}
\]

Every orbit has size

\[
q(q-1).
\]

The quotient is exactly the cyclic relative form of the separable ambient projective complete intersection

\[
X_p=\{s_2=s_3=0\}\subset\mathbf P(W),
\]

because translation quotients by the diagonal line and scaling projectivizes the trace-zero root tuple.

## 3. Exact all-power quotient trace

Let `h_(p,r)(0)` be the affine cubic-origin hook trace. The proved decomposition gives

\[
h_{p,r}(0)
=q^{p-3}-q+q(q-1)\operatorname{Tr}(F^r|\mathcal D_p).
\]

Since

\[
q^{p-3}-q
=q(q-1)(1+q+\cdots+q^{p-5}),
\]

one obtains

\[
\boxed{
\frac{h_{p,r}(0)}{q(q-1)}
=
1+q+\cdots+q^{p-5}
+
\operatorname{Tr}(F^r|\mathcal D_p).
}
\]

The first terms are the ordinary projective Tate cohomology of the smooth `(2,3)` complete intersection. The final term is its alternating-hook primitive module.

This independently recovers the ambient identity

\[
\mathcal K_{\mathrm{ambient}}^{\mathrm{prim}}=\mathcal D_p
\]

from the affine Smith-defect origin and the free affine quotient.

## 4. Semisimplified torsor factorization

The compactly supported affine-group class is

\[
R\Gamma_c(\mathbf A^1\times\mathbf G_m)
=
\mathbf Q_\ell(-2)-\mathbf Q_\ell(-1)
\]

in the Grothendieck group. Put

\[
\mathcal T_p
=
\bigoplus_{j=0}^{p-5}\mathbf Q_\ell(-j).
\]

Then the all-power trace equality gives

\[
\boxed{
\mathcal H_{p,0}^{ss}
=
R\Gamma_c(\mathbf A^1\times\mathbf G_m)
\otimes
(\mathcal T_p\oplus\mathcal D_p).
}
\]

Expanding the Tate product telescopes:

\[
(\mathbf Q_\ell(-2)-\mathbf Q_\ell(-1))
\otimes\mathcal T_p
=
\mathbf Q_\ell(-(p-3))-\mathbf Q_\ell(-1),
\]

and the primitive part is

\[
\mathcal D_p(-2)-\mathcal D_p(-1).
\]

This is exactly the affine cubic-origin decomposition proved separately.

## 5. Consequence for the Fourier--Cayley wall

Translation and scaling at the cubic origin are no longer part of the unknown comparison. Their complete contribution is the explicit affine-group torsor factor above.

The remaining half-twist cannot come from a missed affine quotient correction at `lambda=0`. It must arise from the punctured nonzero-frequency/wild-infinity sector, as required by the localization theorem.

Writing

\[
p-7=2m,
\]

the exact Airy block required from that open sector is

\[
\mathcal D_p(-m)-\mathcal D_p
=
\mathcal D_p\otimes
R\Gamma_c(\mathbf A^m\setminus0).
\]

The affine origin supplies the calibrated boundary fibre; the sparse symplectic polarization identifies the only natural half-dimensional normal model capable of supplying the missing twist.

## 6. Scientific status

### Proved

- freeness of the affine root-change action on the degree-p trace-constraint locus;
- the exact factor `q(q-1)` in every extension degree;
- the projective Tate plus primitive Airy quotient trace;
- the semisimplified affine-group torsor factorization;
- exact closure of translation/scaling bookkeeping at the cubic origin.

### Open

- the polarized wild-infinity nearby-cycle theorem on nonzero sparse frequencies;
- the non-Airy q-line and boundary blocks;
- the terminal estimate and crown.

## 7. Verification

The trace identities and direct `p=5` affine count are checked by

`frontier/d1_symp/affine_cubic_origin_decomposition_verify.py`.
