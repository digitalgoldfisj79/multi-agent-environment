# Characteristic-boundary cubic Airy moments in a function-field Fortune problem

**Draft research note — 2026-07-24**  
**Author:** Edward Stewart Anthony Bozzard  
**ORCID:** `0009-0002-4052-0994`

## Abstract

Let \(P_1=T^p-T\in\mathbf F_p[T]\). A function-field analogue of Fortune's
problem asks whether the least-degree nonconstant offset \(m\) for which
\(P_1+m\) is irreducible must itself be irreducible. This note records an
exact reduction of the sector \(p\equiv2\pmod3\) to a characteristic-boundary
correlation between adjacent symmetric powers of the cubic Airy sheaf,
together with exact low-rank spectra and a set of certified failure results
for natural proof strategies.

The cubic-fibre deviation on the trace-zero hyperplane collapses to a single
sum
\[
 T_p=\sum_{\operatorname{Tr}(x)=0}\psi(\operatorname{Tr}(x^3)),
\]
and
\[
 pT_p=\operatorname{Tr}(F\mid U_p)
      -p\operatorname{Tr}(F\mid U_{p-2}),
\qquad
 \dim U_p=\dim U_{p-2}=\frac{p-5}{6}.
\]
Local wild inertia cancels in the \(p\)-th Adams virtual sheaf, but the
corresponding global characteristic-zero class does not reduce to bounded
rank. Exact \(F^3\) computations determine the characteristic polynomials in
ranks \(2,3,4\). These spectra rule out uniform common-factor cancellation,
uniform slope pairing, torsion phases and bounded-degree period reduction.

The general theorem remains open. Two independent inputs are required:
an absolute global Frobenius-correlation bound and an object-level
nearby-cycle comparison transporting that bound into the irreducibility
ledger. The note is intended as a reproducible terminal account of the
proved mathematics, the computational evidence and the precise boundary.

## 1. The function-field target

For a prime \(p\), put
\[
 P_1(T)=T^p-T.
\]
The \(d=1\) function-field Fortune statement asks whether the
least-degree nonconstant polynomial \(m\) such that \(P_1+m\) is irreducible
is itself irreducible.

The established sparse-family reduction shows that it is enough to find an
irreducible polynomial
\[
 T^p+aT^3+bT^2+cT+d,\qquad (a,b)\ne(0,0).
\]
The full exact incidence ledger is recorded in `D1_ATTACK.md`. It proves the
statement for \(p=3\), machine-certifies every odd prime \(p<1200\), and
reduces the general problem to one aggregate character-sum inequality.

## 2. Cubic trace-zero collapse

Let \(K=\mathbf F_{p^p}\) and
\[
 H=\ker(\operatorname{Tr}_{K/\mathbf F_p}).
\]
For \(b\in\mathbf F_p\), set
\[
 N_b=\#\{x\in H:\operatorname{Tr}(x^3)=b\},
 \qquad D_b=N_b-p^{p-2}.
\]
If \(p\equiv2\pmod3\), cubing permutes \(\mathbf F_p^\times\), so all
nonzero \(D_b\) are equal. With
\[
 T_p=\sum_{x\in H}\psi(\operatorname{Tr}(x^3)),
\]
orthogonality gives
\[
 D_b=-T_p/p\quad(b\ne0),\qquad
 D_0=(p-1)T_p/p.
\]
Thus the entire numerical nonuniformity is one integer per prime.

## 3. Airy Adams formulation

Let \(\mathcal A=\mathrm{Ai}_{x^3}\) be the rank-two cubic Airy sheaf. If its
local inverse roots at \(u\) are \(\alpha_u,\beta_u\), then
\[
 T_p=-\frac1p\sum_{u\in\mathbf F_p}
       (\alpha_u^p+\beta_u^p).
\]
The rank-two identity
\[
 \alpha^p+\beta^p=
 \operatorname{Tr}(\operatorname{Sym}^p)
 -\alpha\beta\operatorname{Tr}(\operatorname{Sym}^{p-2})
\]
identifies this with the \(p\)-th Adams virtual sheaf.

For \(p=6r+5\), the nontrivial \(\mu_3\) eigenspaces have zero arithmetic
Frobenius trace. After the special-fibre correction,
\[
 U_k=H_c^1(\mathbf A^1_{\overline{\mathbf F}_p},
           \operatorname{Sym}^k\mathcal A)^{\mu_3}
\]
satisfies
\[
 \dim U_p=\dim U_{p-2}=r,
\]
and, with the positive convention for \(T_p\),
\[
 \boxed{
 pT_p=\operatorname{Tr}(F\mid U_p)
      -p\operatorname{Tr}(F\mid U_{p-2}).
 }
\]
The analytic target is therefore
\[
 |T_p|\le C p^{(p-1)/2}
\]
with \(C\) independent of \(p\).

## 4. Unconditional estimates

Purity gives a linear-rank loss. Additive orthogonality followed by the
degree-three Weil bound improves this to
\[
 |T_p|\le
 \frac{2(p-1)}{\sqrt p}\,p^{(p-1)/2}.
\]
Equivalently, after writing
\(\alpha_u=\sqrt p\,e^{i\theta_u}\), the missing estimate is
\[
 \left|\sum_{u\ne0}\cos(p\theta_u)\right|\ll\sqrt p.
\]
This is a characteristic-boundary problem: the symmetric-power frequency
equals the field characteristic.

## 5. Local cancellation and global obstruction

On the quadratic inertia cover at infinity, the Airy sheaf splits into two
order-\(p\) wild characters times a tame quadratic character. The \(p\)-th
Adams operation kills the wild characters, and the virtual sheaf has zero
Swan conductor.

This local rank-two representative does not globalize directly. In the
characteristic-zero representation ring,
\[
 [\operatorname{Sym}^p]-[\operatorname{Sym}^{p-2}]
\]
has a negative irreducible multiplicity. The canonical integral lift of the
modular Adams quotient has a connection defect of full target rank, and its
principal component remains full rank after projection to the actual
\(\mu_3\)-invariant cohomology.

The Hodge spectra of the two characteristic-zero motives are disjoint.
Accordingly, any successful relation must depend genuinely on the exceptional
reduction \(k=p=\operatorname{char}\).

## 6. Odd-power trace extraction

For \(p\equiv-1\pmod3\), every odd power \(F^m\) interchanges the two
nontrivial \(\mu_3\) eigenspaces. Therefore
\[
 \operatorname{Tr}(F^m\mid H_k)
 =
 \operatorname{Tr}(F^m\mid U_k)
 \qquad(m\ {\rm odd}).
\]
This avoids the projector contamination in an \(F^2\)-based experiment and
makes \(m=3\) the first new ordinary Airy power trace.

Exact three-dimensional DFT calculations over \(\mathbf F_{p^3}\), certified
by CRT and independent coefficient-prime checks, give the \(F^3\) traces at
\(p=17,23,29\).

## 7. Exact low-rank spectra

Normalize eigenvalues by the common purity radius.

### 7.1 \(p=17\)

\[
 \bar P_{17}(y)=y^2-\frac{29}{17}y+1,
\]
so
\[
 \lambda=17^8\frac{29\pm3i\sqrt{35}}2.
\]
The \(U_{15}\) factor has zero first and third traces, leaving determinant
sign \(y^2\pm1\).

### 7.2 \(p=23\)

\[
 \bar P_{23}(y)=(y-1)
 \left(y^2+\frac{764}{529}y+1\right),
\]
and
\[
 \bar P_{21(-1)}(y)=(y-1)
 \left(y^2+\frac{203}{529}y+1\right).
\]
The central \(+23^{12}\) eigenvalue cancels exactly.

### 7.3 \(p=29\)

\[
 \bar P_{29}(y)=
 y^4+\frac{48674}{24389}y^3
 +\frac{1531538}{707281}y^2
 +\frac{48674}{24389}y+1,
\]
whereas
\[
 \bar P_{27(-1)}(y)=
 y^4-\frac{16745}{24389}y^3
 +\frac{140088}{707281}y^2
 -\frac{16745}{24389}y+1.
\]
Their exact gcd is one.

A second implementation independently reproduced all six \(F^3\) traces.

## 8. Certified route failures

The computations and structural audits close the following direct routes:

1. uniform cancellation by a growing common Frobenius factor;
2. root-of-unity or bounded-period phases;
3. uniform Newton-slope pairing;
4. a characteristic-zero cross-\(k\) correspondence;
5. a bounded-cone lift of the modular Adams sequence;
6. direct globalization of local Swan collapse;
7. bare cyclic-shift localization;
8. bounded-degree Gaussian-period reduction.

These are failure certificates for proof strategies, not evidence against the
absolute trace estimate itself.

## 9. The application boundary

The Airy estimate is not yet a proved implication to the Fortune crown.
A separate comparison must identify the cubic Airy boundary complex with the
load-bearing component of the post-pushforward hook/nearby-cycle ledger,
including:

- main, Tate and Artin--Schreier subtraction;
- the punctual \(b=0\) term;
- the arithmetic quadratic twist at infinity;
- the \(q=2\) and \(q=\infty\) boundary cells;
- the final positivity certificate.

Until the exact transport multiplicity is known, it is also unknown whether
the full crown truly requires an absolute \(C\) or could tolerate logarithmic
slack.

## 10. Open problems

### Analytic correlation theorem

Prove
\[
 \left|\operatorname{Tr}(F\mid U_p)
 -p\operatorname{Tr}(F\mid U_{p-2})\right|
 \le C p^{(p+1)/2}
\]
for \(p\equiv5\pmod6\) with absolute \(C\).

### Application comparison theorem

Construct an object-level, trace-compatible comparison between the Airy
boundary complex and the irreducibility hook complex, with every punctual,
Tate, arithmetic-twist and boundary term explicit.

## 11. Reproducibility and epistemic status

The repository separates proved algebraic statements, exact
computer-assisted theorems, statistical observations, failed strategies and
open conjectures. The low-rank spectra have two independent implementations.
The general Fortune statement and both open theorems above remain unproved.

## References

1. C. D. Haessig and A. Rojas-León, *L-functions of symmetric powers of the
   generalized Airy family of exponential sums: ell-adic and p-adic methods*,
   arXiv:0908.1240.
2. C. Sabbah and J.-D. Yu, *Hodge properties of Airy moments*,
   arXiv:2112.13405.
3. Y. Qin, *Hodge numbers of motives attached to Kloosterman and Airy
   moments*, arXiv:2302.05365.
4. P.-H. Chuang, *On the Generalized Arithmetic Picard--Lefschetz Formula*,
   arXiv:2607.05757.
