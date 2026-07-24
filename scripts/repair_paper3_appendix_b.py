#!/usr/bin/env python3
from pathlib import Path
import hashlib

path = Path('publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md')
text = path.read_text(encoding='utf-8')
expected = '1753e5991ccab15142d9bd076554c283a69bfa3bd8aa9448b2edf62f50c4c7cb'
assert hashlib.sha256(text.encode()).hexdigest() == expected

start_marker = '# Appendix B. Truncated singular-series proof'
end_marker = '# Appendix C. Corrected conditional Hardy--Littlewood theorem'
assert text.count(start_marker) == 1
assert text.count(end_marker) == 1
start = text.index(start_marker)
end = text.index(end_marker)

appendix = r'''# Appendix B. Truncated singular-series proof

This appendix gives the complete proof of the only singular-series estimate used
by the conditional theorem.  The sharper Dickman--de Bruijn constant in Remark
B.4 is explicitly non-load-bearing.

For a fixed centre \(P_j\), put

\[
A_j=\prod_{p\le \ell_j}p,
\qquad
A'_j=A_j/2,
\qquad
\varphi_2(u)=\prod_{p\mid u}(p-2),
\]

where every divisor of \(A'_j\) is odd and squarefree.  Also write

\[
C_j=\prod_{2<p\le\ell_j}\frac{p(p-2)}{(p-1)^2}.
\]

## B.1 Local factors and the finite singular series

**Lemma B.1.**  For the pair
\((P_j+m,P_j+m+d)\), the local factor at a prime \(p\le\ell_j\) is

\[
\delta_p(d)=
\begin{cases}
\dfrac{p(p-2)}{(p-1)^2},&p\nmid d,\\[6pt]
\dfrac{p}{p-1},&p\mid d.
\end{cases}
\tag{B.1}
\]

Consequently the truncated singular series is

\[
\mathfrak S_j(d)
 =\prod_{p\le\ell_j}\delta_p(d)
 =\mathbf 1_{2\mid d}\,2C_j
   \prod_{\substack{2<p\le\ell_j\\p\mid d}}
   \frac{p-1}{p-2}.
\tag{B.2}
\]

**Proof.**  Since \(p\mid P_j\), the forbidden residue classes for \(m\)
modulo \(p\) are \(0\) and \(-d\).  They are distinct when \(p\nmid d\),
leaving \(p-2\) admissible residues, and coincide when \(p\mid d\), leaving
\(p-1\).  Multiplication by the two von Mangoldt normalising factors
\((p/(p-1))^2\) gives (B.1).  At \(p=2\), the factor is \(0\) for odd \(d\)
and \(2\) for even \(d\), which yields (B.2).  \(\square\)

For later use define

\[
\lambda_p(d)=\delta_p(d)-1
=-\frac{1}{(p-1)^2}
 +\mathbf 1_{p\mid d}\frac{p}{(p-1)^2}.
\]

Expanding the finite Euler product gives the exact identity

\[
\mathfrak S_j(d)-1
 =\sum_{\substack{r\mid A_j\\r>1}}
   \frac{1}{\varphi(r)^2}
   \sum_{s\mid r}\mu(r/s)s\,\mathbf 1_{s\mid d}.
\tag{B.3}
\]

No estimate for the omitted infinite Euler-product tail is asserted or used:
the conditional theorem is formulated entirely with the finite product
\(\mathfrak S_j(d)\).

## B.2 Exact divisor identity

For an integer \(s\ge1\), let

\[
W_H(s)=\sum_{\substack{1\le d<H\\s\mid d}}(H-d).
\]

If \(s\ge H\), then \(W_H(s)=0\).  If \(1\le s<H\) and
\(\rho_s\) is the least nonnegative residue of \(H\) modulo \(s\), then

\[
W_H(s)=\frac{H^2}{2s}-\frac H2+E_H(s),
\qquad
E_H(s)=\frac{\rho_s}{2}\left(1-\frac{\rho_s}{s}\right),
\tag{B.4}
\]

and therefore

\[
0\le E_H(s)\le \frac{s}{8}.
\tag{B.5}
\]

Recall

\[
T_j(H)=2\sum_{1\le d<H}(H-d)\bigl(\mathfrak S_j(d)-1\bigr).
\]

**Lemma B.2 (exact divisor identity).**

\[
T_j(H)
=-H(H-1)
 +4C_j
  \sum_{\substack{u\mid A'_j\\2u<H}}
  \frac{W_H(2u)}{\varphi_2(u)}.
\tag{B.6}
\]

**Proof.**  Insert (B.3), interchange the finite sums and collect the
coefficient of \(W_H(s)\).  For \(s=1\), that coefficient is

\[
\prod_{p\mid A_j}\left(1-\frac{1}{(p-1)^2}\right)-1=-1,
\]

because the factor at \(p=2\) vanishes.  For \(s>1\), the coefficient is zero
unless \(s\) is even.  Writing \(s=2u\), with \(u\mid A'_j\), direct
multiplication gives \(2C_j/\varphi_2(u)\).  Since
\(W_H(1)=H(H-1)/2\), formula (B.6) follows.  \(\square\)

As a check, for \(A_j=2\cdot3\) and \(H=5\), one has
\(C_j=3/4\), \(W_H(2)=4\), and (B.6) gives
\(-20+4(3/4)4=-8\), equal to the direct sum.

## B.3 Uniform second-moment bound

Define

\[
\beta_j(H)=2C_j
\sum_{\substack{u\mid A'_j\\u<H/2}}
\frac{1}{\varphi_2(u)}.
\tag{B.7}
\]

**Lemma B.3.**  Uniformly in \(j\),

\[
T_j(H)=-\beta_j(H)H+O(H),
\tag{B.8}
\]

with an absolute implied constant.  Moreover,

\[
2C_j\le\beta_j(H)
\le\prod_{p\le\ell_j}\frac{p}{p-1}
=(e^\gamma+o(1))\log\ell_j.
\tag{B.9}
\]

Consequently, in the regime \(H\asymp X^2\) and
\(X\le\ell_j<2X\),

\[
|T_j(H)|\le 2H\log X
\tag{B.10}
\]

for all sufficiently large \(X\), uniformly in the block.

**Proof.**  Insert (B.4) into (B.6).  The complete \(H^2\)-coefficient
cancels because

\[
C_j\sum_{u\mid A'_j}\frac{1}{u\varphi_2(u)}
 =\prod_{2<p\le\ell_j}
  \frac{p(p-2)}{(p-1)^2}
  \left(1+\frac{1}{p(p-2)}\right)=1.
\tag{B.11}
\]

It remains to bound the truncated tail in (B.11) and the error in (B.4).
Put

\[
f(u)=\frac{u}{\varphi_2(u)}
\]

on odd squarefree integers.  Then

\[
f(u)=\sum_{b\mid u}h(b),
\qquad
h(p)=\frac{2}{p-2},
\]

with \(h\) multiplicative and squarefree-supported.  The Euler product

\[
\sum_b\frac{h(b)}b
 =\prod_{p>2}\left(1+\frac{2}{p(p-2)}\right)
\tag{B.12}
\]

converges.  Hence, for \(V\ge1\),

\[
\begin{aligned}
\sum_{\substack{u\ge V\\u\ {m odd,\ squarefree}}}
 \frac{1}{u\varphi_2(u)}
&\le
 \sum_b\frac{h(b)}{b^2}
 \sum_{m\ge V/b}\frac{1}{m^2}\\
&\ll \frac1V\sum_{b\le V}\frac{h(b)}b
   +\sum_{b>V}\frac{h(b)}{b^2}
 \ll \frac1V.
\end{aligned}
\tag{B.13}
\]

Taking \(V=H/2\), the omitted \(H^2\)-tail is \(O(H)\).
Also, by (B.5),

\[
4C_j\sum_{2u<H}\frac{E_H(2u)}{\varphi_2(u)}
 \le C_j\sum_{u<H/2}f(u)
 \ll H,
\tag{B.14}
\]

where (B.12) was used after expanding \(f=1*h\).  Equations
(B.6)--(B.14) give (B.8).

The lower bound in (B.9) is the term \(u=1\).  Extending the positive sum in
(B.7) over every divisor of \(A'_j\) gives

\[
\begin{aligned}
\beta_j(H)
&\le 2C_j\prod_{2<p\le\ell_j}
       \left(1+\frac{1}{p-2}\right)\\
&=\prod_{p\le\ell_j}\frac{p}{p-1},
\end{aligned}
\]

and Mertens' theorem proves (B.9).  Finally, (B.8), (B.9),
\(\ell_j<2X\), and \(e^\gamma<2\) imply (B.10) for sufficiently large
\(X\).  Notice that no sign assertion for \(T_j(H)\) is needed or made.
\(\square\)

**Remark B.4 (sharper constant; non-load-bearing sketch).**  Let

\[
\theta_j=\frac{\log H}{\log\ell_j},
\qquad
I(\theta)=\int_0^\theta\rho(v)\,dv,
\]

where \(\rho\) is the Dickman function.  Standard smooth-number asymptotics
suggest

\[
T_j(H)=-I(\theta_j)H\log\ell_j\,(1+o(1)).
\tag{B.15}
\]

In the Paper II regime \(H=\eta X^2\), one has
\(\theta_j\to2\) and
\(I(2)=3-2\log2\).  This refinement is not used anywhere in the
conditional theorem; only the proved bound (B.10) is used.

---

'''

text = text[:start] + appendix + text[end:]
path.write_text(text, encoding='utf-8')
print(hashlib.sha256(text.encode()).hexdigest())
