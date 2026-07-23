# Fast collapse theorem and audit of the Fermat fixed-point route

**Date:** 2026-07-23  
**Status:** exact collapse theorem; rigorous linear-loss fallback; precise obstruction to the naive fixed-character argument. The absolute-constant estimate remains open.

**Integration provenance:** selectively preserved from commit `88c760155643045f1ffe74bb584a8eab1bb0cc1f`; no branch merge performed.

## 1. Setup

Let

\[
K=\mathbf F_{p^p},\qquad H=\{x\in K:\operatorname{Tr}_{K/\mathbf F_p}(x)=0\},
\]

and

\[
N_b=\#\{x\in H:\operatorname{Tr}(x^3)=b\},\qquad
D_b=N_b-p^{p-2}.
\]

Let \(\psi\) be a fixed nontrivial additive character of \(\mathbf F_p\), and define

\[
T_p=\sum_{x\in H}\psi(\operatorname{Tr}(x^3)).
\]

Throughout this note assume \(p\equiv2\pmod3\).

## 2. Exact collapse

### Theorem 2.1

For every \(b\ne0\), all \(D_b\) have one common value \(D_*\), and

\[
\boxed{D_*=-\frac{T_p}{p}},\qquad
\boxed{D_0=\frac{p-1}{p}T_p=-(p-1)D_*}.
\]

### Proof

Scaling \(x\mapsto sx\), \(s\in\mathbf F_p^\times\), gives

\[
N_{s^3b}=N_b.
\]

Because \(p\equiv2\pmod3\), cubing is a bijection of \(\mathbf F_p^\times\). Hence \(D_b=D_*\) for every \(b\ne0\).

Also

\[
\sum_{b\in\mathbf F_p}N_b=\#H=p^{p-1}
=\sum_{b\in\mathbf F_p}p^{p-2},
\]

so

\[
D_0+(p-1)D_*=0.
\]

Finally,

\[
T_p=\sum_bN_b\psi(b)=\sum_bD_b\psi(b),
\]

because \(\sum_b\psi(b)=0\). Since \(\sum_{b\ne0}\psi(b)=-1\),

\[
T_p=D_0-D_*=-(p-1)D_*-D_*=-pD_*.
\]

This proves both identities. \(\square\)

### Consequence

At the level of the trace function, the value at \(b=0\) is not an independent analytic quantity in the \(p\equiv2\pmod3\) sector. Bounding one nonzero fibre automatically bounds the punctual value, and conversely. A separate categorical localization check is still required when transporting this numerical identity into the original nearby-cycle ledger.

## 3. Equivalent Airy moment

For

\[
S_r(u,v)=\sum_{x\in\mathbf F_{p^r}}
\psi\!\left(\operatorname{Tr}(ux+vx^3)\right),
\]

orthogonality gives

\[
T_p=\frac1p\sum_{u\in\mathbf F_p}S_p(u,1).
\]

If \(v=s^3\), the substitution \(y=sx\) gives

\[
S_p(u,v)=S_p(u/s,1).
\]

Since cubing is bijective on \(\mathbf F_p^\times\), the inner \(u\)-sum is independent of \(v\), and WTCK Fourier inversion immediately yields the same formula \(D_*=-T_p/p\).

Writing the degree-two Airy inverse roots as \(\alpha_u,\beta_u\),

\[
S_p(u,1)=-(\alpha_u^p+\beta_u^p),
\]

so

\[
T_p=-\frac1p\sum_u(\alpha_u^p+\beta_u^p).
\]

The remaining half-theorem estimate is therefore exactly

\[
\left|\sum_{u\in\mathbf F_p}(\alpha_u^p+\beta_u^p)\right|
\ll p^{(p+1)/2}
\]

with an absolute implied constant.

## 4. Rigorous baseline bound

For a rank-two representation,

\[
\alpha^p+\beta^p
=\operatorname{tr}(\operatorname{Sym}^p)
-\alpha\beta\,\operatorname{tr}(\operatorname{Sym}^{p-2}).
\]

Thus the moment is the first Frobenius trace of the virtual Airy sheaf

\[
\Psi^p(\mathcal A)
=\operatorname{Sym}^p\mathcal A
-\det(\mathcal A)\otimes\operatorname{Sym}^{p-2}\mathcal A.
\]

For the cubic Airy family, the exact degree formula of Haessig--Rojas-León gives

\[
\deg L(\mathbf A^1,\operatorname{Sym}^p\mathcal A,T)=\frac{p-5}{2},
\]

and

\[
\deg L(\mathbf A^1,\det(\mathcal A)\otimes
\operatorname{Sym}^{p-2}\mathcal A,T)=\frac{p-1}{2}.
\]

(The determinant is geometrically constant, so it does not change the Euler-characteristic degree.) Deligne purity therefore gives the unconditional estimate

\[
\left|\sum_u(\alpha_u^p+\beta_u^p)\right|
\le (p-3)p^{(p+1)/2},
\]

hence

\[
\boxed{|D_*|\le(p-3)p^{(p-3)/2}.}
\]

This is the clean Katz/GOS fallback. It is nontrivial and rigorous, but it loses a factor of order \(p\) and does not prove the half-theorem.

## 5. Audit of the proposed Fermat/Jacobi argument

After base change to \(\overline{\mathbf F}_p\), restriction of scalars splits and the pair \((H,\operatorname{Tr}(x^3))\) becomes

\[
H_{\bar{\mathbf F}_p}=\{(x_0,\ldots,x_{p-1}):\sum_i x_i=0\},
\qquad f=\sum_i x_i^3,
\]

with arithmetic Frobenius composed with the cyclic shift of the coordinates.

This is exact. However, the following shortcut is **not** yet justified:

> label the primitive cohomology by independent cubic characters in each coordinate and conclude that shift followed by character inversion has no fixed label when \(p\) is odd.

That binary character basis is the tensor-product decomposition for the ambient diagonal cubic. The trace-zero condition is a linear section. Eliminating one coordinate changes the phase to

\[
\sum_{i=1}^{p-1}x_i^3-\left(\sum_{i=1}^{p-1}x_i\right)^3,
\]

which is not diagonal. Equivalently, enforcing the hyperplane by a Lagrange multiplier introduces the Airy parameter \(u\). Therefore the primitive cohomology is that of a cyclically twisted \((1,3)\) complete intersection (or its Cayley-trick model), not the unrestricted tensor product of \(p\) one-variable cubic eigenspaces.

Consequently, “no fixed binary character vector” proves cancellation only for an ambient tensor sector. To prove the required result one must additionally give one of the following:

1. an explicit Jacobi-sum decomposition for the diagonal cubic **linear section**, with the cyclic-Frobenius action on its admissible character classes; or
2. a Frobenius-equivariant cancellation theorem between
   \(H_c^1(\operatorname{Sym}^p\mathcal A)\) and
   \(H_c^1(\det\mathcal A\otimes\operatorname{Sym}^{p-2}\mathcal A)\), leaving bounded-dimensional virtual cohomology.

The observed \(C\approx4\) profile is consistent with such a bounded residual, but does not establish it.

## 6. Precise terminal statement

The half-theorem follows if the virtual global Frobenius trace satisfies

\[
\left|\operatorname{Tr}\left(\operatorname{Frob}_p\mid
R\Gamma_c(\mathbf A^1,\Psi^p(\mathcal A))\right)\right|
\le C p^{(p+1)/2}
\]

for an absolute \(C\). A sufficient stronger statement is that the virtual cohomology above is represented, after cancelling common Frobenius factors, by a complex of uniformly bounded total dimension.

## 7. Verdict on the long-running agent

- The collapse identity is elementary and complete; it should not consume an extended run.
- The fixed-character claim is potentially valuable but must be carried out on the \((1,3)\) linear section, not on the ambient Fermat tensor product.
- Continue the agent only if it is explicitly constructing that complete-intersection/Jacobi decomposition or a bounded virtual-cohomology cancellation.
- Stop it if it is merely enumerating ambient binary character vectors, extending prime tables, or returning only the \((p-3)\)-loss GOS bound proved above.
