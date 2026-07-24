# Part II. Bounds, odd-power extraction, and exact spectra

## 7. Unconditional bounds

Separate purity gives a coefficient of order \(p\). Additive orthogonality over \(K=\mathbf F_{p^p}\) improves this:
\[
T_p=\frac1p\sum_{b\in\mathbf F_p}\sum_{x\in K}\psi_K(x^3+bx).
\]
The \(b=0\) term vanishes and the degree-three Weil bound gives
\[
\boxed{|T_p|\le\frac{2(p-1)}{\sqrt p}\,p^{(p-1)/2}.}
\]
The missing theorem replaces the coefficient \(O(\sqrt p)\) by \(O(1)\).

Writing
\[
\alpha_u=\sqrt p\,e^{i\theta_u},\qquad
\beta_u=\sqrt p\,e^{-i\theta_u},
\]
the target is equivalent to
\[
\left|\sum_{u\ne0}\cos(p\theta_u)\right|\ll\sqrt p.
\]

## 8. Odd-power trace extraction

**Lemma.** For \(p\equiv-1\pmod3\) and odd \(m\),
\[
\operatorname{Tr}(F^m|H_k)=\operatorname{Tr}(F^m|U_k).
\]

Frobenius sends a nontrivial \(\mu_3\)-character to its inverse. Every odd power still interchanges the two nontrivial eigenspaces, so its trace there is zero. The lemma avoids projector contamination in an \(F^2\) computation; the first new accessible power is \(F^3\).

## 9. Exact low-rank spectra

Exact three-dimensional DFTs over \(\mathbf F_{p^3}\), complete-homogeneous recurrences, and signed CRT reconstruction give the first and third Frobenius traces.

### \(p=17\), rank two

\[
\bar P_{17}(y)=y^2-\frac{29}{17}y+1,
\]
with eigenvalues
\[
17^8\frac{29\pm3i\sqrt{35}}2.
\]
For \(U_{15}\), the first and third traces vanish and odd traces leave the determinant sign \(y^2\pm1\) unresolved.

### \(p=23\), rank three

\[
\bar P_{23}(y)
=(y-1)\left(y^2+\frac{764}{529}y+1\right),
\]
and, after the Tate twist,
\[
\bar P_{21(-1)}(y)
=(y-1)\left(y^2+\frac{203}{529}y+1\right).
\]
The central eigenvalue \(+23^{12}\) cancels exactly.

### \(p=29\), rank four

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

A quarantined second implementation independently reproduced all six \(F^3\) traces at \(p=17,23,29\). It used a separately selected irreducible cubic, scalar arithmetic modulo coefficient primes \(\ell\equiv1\pmod p\), a separable three-dimensional DFT, nine-prime signed CRT reconstruction, and a tenth unused coefficient prime. All internal DFT anchors and prediction comparisons passed.
