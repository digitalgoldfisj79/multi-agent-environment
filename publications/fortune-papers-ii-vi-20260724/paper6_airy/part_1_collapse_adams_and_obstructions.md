# Part I. Collapse, Adams identity, and structural obstructions

## 1. Cubic trace collapse

Let
\[
K=\mathbf F_{p^p},\qquad H=\ker(\operatorname{Tr}_{K/\mathbf F_p}),
\]
\[
N_b=\#\{x\in H:\operatorname{Tr}(x^3)=b\},\qquad D_b=N_b-p^{p-2},
\]
and
\[
T_p=\sum_{x\in H}\psi(\operatorname{Tr}(x^3)).
\]

**Theorem.** If \(p\equiv2\pmod3\), all \(D_b\) with \(b\ne0\) are equal and
\[
D_b=-T_p/p,\qquad D_0=(p-1)T_p/p.
\]

Scaling by \(s\in\mathbf F_p^\times\) sends \(b\) to \(s^3b\). Cubing is bijective on \(\mathbf F_p^\times\), so the nonzero fibres are equal. The total deviation is zero and additive orthogonality gives the displayed identities.

## 2. Airy Adams identity

Let \(\mathcal A=\mathrm{Ai}_{x^3}\), with local inverse roots \(\alpha_u,\beta_u\) at \(u\in\mathbf F_p\). Orthogonality gives
\[
T_p=-\frac1p\sum_u(\alpha_u^p+\beta_u^p).
\]
For a rank-two representation,
\[
\alpha^p+\beta^p=
\operatorname{Tr}(\operatorname{Sym}^p)
-\alpha\beta\operatorname{Tr}(\operatorname{Sym}^{p-2}).
\]
Thus
\[
\Psi^p(\mathcal A)=
\operatorname{Sym}^p\mathcal A-
\det(\mathcal A)\otimes\operatorname{Sym}^{p-2}\mathcal A.
\]

For \(p=6r+5\), put
\[
U_k=H_c^1(\mathbf A^1_{\overline{\mathbf F}_p},
\operatorname{Sym}^k\mathcal A)^{\mu_3}.
\]
Arithmetic Frobenius interchanges the two nontrivial \(\mu_3\)-eigenspaces, so their trace is zero. After the special-fibre correction,
\[
\dim U_p=\dim U_{p-2}=r
\]
and, with the positive convention for \(T_p\),
\[
\boxed{pT_p=\operatorname{Tr}(F|U_p)-p\operatorname{Tr}(F|U_{p-2}).}
\]

## 3. Local conductor collapse

On the quadratic inertia cover at infinity,
\[
\mathcal A|_{I'}=(\chi\kappa)\oplus(\chi^{-1}\kappa),
\]
where \(\chi\) is wild of order \(p\) and \(\kappa\) is tame quadratic. The \(p\)-th Adams operation kills \(\chi\), yielding
\[
\Psi^p(\mathcal A)|_{I_\infty}^{\mathrm{ss}}
\cong\operatorname{Ind}_{I'}^{I_\infty}(\kappa),
\qquad
\operatorname{Swan}_\infty(\Psi^p(\mathcal A))=0.
\]
The wild parts cancel exactly in the local virtual character.

## 4. Why local rank two does not globalise

For \(p>5\), the geometric monodromy is \(SL_2\). In the characteristic-zero representation ring,
\[
[\Psi^p(\mathrm{Std})]
=[\operatorname{Sym}^p(\mathrm{Std})]-[\operatorname{Sym}^{p-2}(\mathrm{Std})].
\]
The second irreducible has coefficient \(-1\). Hence the Adams class is not an actual global rank-two representation. Zero Swan conductor controls virtual Euler characteristic, not the number or correlation of global Frobenius eigenvalues.

## 5. Modular sequence and full-rank defect

In characteristic \(p\), every rank-two bundle \(E\) has
\[
0\to F^*E\to\operatorname{Sym}^pE
\to\det(E)\otimes\operatorname{Sym}^{p-2}E\to0.
\]
In Haessig's Airy frame, the natural integral lift has defect
\[
P_p\partial_p-\partial_{p-2}P_p
=-p\pi aJ_p+\frac{p(p-1)\pi a^2}{3}E_p.
\]
The principal map \(J_p\) has full target-module rank \(p-1\). Its projection to primitive target cohomology has rank \((p-1)/2\); after the \(\mu_3\) projector it has full rank \((p-5)/6\) on the surviving trace space. The modular exact sequence is a genuine boundary mechanism, but its direct characteristic-zero lift does not have a bounded cone.

## 6. Hodge obstruction

The odd Airy Hodge spectra for \(k=p\) and the Tate-twisted \(k=p-2\) space have first coordinates
\[
\left\{\frac{p+2i}{3}\right\},\qquad
\left\{\frac{p+1+2j}{3}\right\}.
\]
Equality would require \(2(i-j)=1\), impossible. The corresponding characteristic-zero Hodge structures have no nonzero morphism. Any successful pairing must be special to \(k=p=\operatorname{char}\) and must depend on Frobenius.
