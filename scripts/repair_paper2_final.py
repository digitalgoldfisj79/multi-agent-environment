#!/usr/bin/env python3
from pathlib import Path
import hashlib

path = Path('publications/fortune-papers-ii-vi-20260724/paper2_revised/manuscript.md')
text = path.read_text(encoding='utf-8')
expected = '497c5b2a52e8beb93d166b8763646cf03ee315664d31e4d875c6486b3296e22f'
assert hashlib.sha256(text.encode()).hexdigest() == expected

# 1. Mark the reciprocal-to-prime bridge as an imported architectural input,
# not as a theorem proved in this manuscript.
old = '''The earlier pair-lift and principal-cancellation reductions identify a bound

\[
\mathfrak F_X\ll MX^{o(1)}
\tag{3.6}
\]

as a sufficient local input for the prime-detection architecture. The present paper analyses the exact content of (3.6). The distinction between this sufficient architecture and Theorem 2.4 should be kept explicit: the direct variance theorem is unconditional as an implication, while (3.6) is a harmonic sufficient target arising from the chosen reciprocal-frame reduction.'''
new = '''The preceding pair-lift and principal-cancellation analysis supplies the following architectural input:

\[
\mathfrak F_X\ll MX^{o(1)}.
\tag{3.6}
\]

Within that architecture, (3.6) is a sufficient local estimate. This manuscript does not reprove the source-to-frame transference step and does not assert that (3.6) is equivalent to Theorem 2.4. Theorem 2.4 is an unconditional implication from a direct von Mangoldt variance bound; (3.6) is the separate harmonic target whose exact internal structure is analysed below.'''
assert text.count(old) == 1
text = text.replace(old, new)

# 2. Define zero-mass harmonics before any quotient by m_a.
old = '''\[
\Psi_a(L)=\sum_{q\in\mathcal Q_X}p_{q,a}e(aL/q),
\qquad
m_a=\sum_{q\in\mathcal Q_X}p_{q,a}.
\tag{3.7}
\]

and'''
new = '''\[
\Psi_a(L)=\sum_{q\in\mathcal Q_X}p_{q,a}e(aL/q),
\qquad
m_a=\sum_{q\in\mathcal Q_X}p_{q,a}.
\tag{3.7}
\]

If \(m_a=0\), then every \(p_{q,a}=0\) and hence \(\Psi_a\equiv0\). Such harmonics are omitted from every quotient by \(m_a\); all quotient sums below are therefore over \(a\ge1\) with \(m_a>0\).

Define'''
assert text.count(old) == 1
text = text.replace(old, new)
text = text.replace('2\sum_{a\ge1}\frac{\mathcal E_a}{m_a}.', '2\sum_{\substack{a\ge1\\m_a>0}}\frac{\mathcal E_a}{m_a}.', 1)
text = text.replace('\left(\sum_{a\ge1}m_a\right)\n\left(\sum_{a\ge1}\frac{|\Psi_a(L)|^2}{m_a}\right)', '\left(\sum_{a\ge1}m_a\right)\n\left(\sum_{\substack{a\ge1\\m_a>0}}\frac{|\Psi_a(L)|^2}{m_a}\right)', 1)
text = text.replace('=\frac12\sum_{a\ge1}\frac{|\Psi_a(L)|^2}{m_a}.', '=\frac12\sum_{\substack{a\ge1\\m_a>0}}\frac{|\Psi_a(L)|^2}{m_a}.', 1)
text = text.replace('\sum_{a\ge1}\frac{\mathcal R_a}{m_a}', '\sum_{\substack{a\ge1\\m_a>0}}\frac{\mathcal R_a}{m_a}', 1)

# 3. Supply the previously implicit diagonal estimate used after (3.17).
old = '''because the corresponding weighted sum of diagonal terms is \(o(M)\) for the critical prime shell. Uniform control of every small \(a\) is a convenient sufficient condition, not a necessary quantifier.'''
new = '''because the corresponding weighted sum of diagonal terms is \(o(M)\) for the critical prime shell. Indeed,
\[
\frac{\kappa_{2,a}}{m_a}
=\frac{\sum_q w_{q,a}^2}{D_X\sum_q w_{q,a}}
\le \frac{\max_q w_{q,a}}{D_X},
\]
and Schwartz decay gives \(\sum_{a\ge1}\max_q w_{q,a}=O_\rho(1)\), whereas the prime number theorem gives \(D_X\asymp_\rho |\mathcal Q_X|\asymp H/\log H\). Thus
\[
M(M-1)\sum_{\substack{a\ge1\\m_a>0}}\frac{\kappa_{2,a}}{m_a}
\ll_\rho \frac{M^2\log H}{H}=o(M),
\]
since \(M\asymp X^2/\log^2X\) and \(H\asymp X^2\). Uniform control of every small \(a\) is a convenient sufficient condition, not a necessary quantifier.'''
assert text.count(old) == 1
text = text.replace(old, new)

# 4. Repair the level-set threshold: a fixed X^epsilon cutoff is not X^{o(1)}.
old = '''**Proposition 4.3 (one-sided level-set criterion).** Fix \(\varepsilon>0\). It is sufficient to prove, for dyadic

\[
MX^\varepsilon\le \lambda\le M^2,
\]

that

\[
\mu_{X,a}\{K_X\ge\lambda\}
\ll
\frac{MX^{o(1)}}{\lambda}.
\tag{4.5}
\]

**Proof.** Split \((K_X)_+\) at \(MX^\varepsilon\) and apply the dyadic layer-cake inequality. The low part contributes at most \(MX^\varepsilon\), and each dyadic high level contributes \(MX^{o(1)}\). The logarithmic number of levels is absorbed into \(X^{o(1)}\). \(\square\)'''
new = '''**Proposition 4.3 (one-sided level-set criterion).** Let \(L(X)\ge1\) satisfy \(L(X)=X^{o(1)}\). It is sufficient to prove, for dyadic

\[
ML(X)\le \lambda\le M^2,
\]

that

\[
\mu_{X,a}\{K_X\ge\lambda\}
\ll
\frac{MX^{o(1)}}{\lambda}.
\tag{4.5}
\]

**Proof.** Split \((K_X)_+\) at \(ML(X)\) and apply the dyadic layer-cake inequality. The low part contributes at most \(ML(X)=MX^{o(1)}\), and each dyadic high level contributes \(MX^{o(1)}\). The logarithmic number of levels is absorbed into \(X^{o(1)}\). \(\square\)'''
assert text.count(old) == 1
text = text.replace(old, new)

# 5. Make the even-shift singular-series lower bound explicit.
old = '''Moreover, \(m-n\) is even, so its singular series is bounded below by a positive absolute constant.'''
new = '''Moreover, \(m-n\) is even. For the binary singular series,
\[
\mathfrak S(d)=2C_2\prod_{\substack{p\mid d\\p>2}}\frac{p-1}{p-2}
\qquad(d\ \text{even}),
\]
so \(\mathfrak S(m-n)\ge2C_2>0\) uniformly.'''
assert text.count(old) == 1
text = text.replace(old, new)

# 6. Clarify the moving-interval use of the prime-power estimate in Theorem 8.1.
old = '''Its von Mangoldt mass comes only from proper prime powers. As in Lemma 2.3, their total weight is \(O(\log P_n\log\log P_n)=o(h_n)\), uniformly in \(x\).'''
new = '''Its von Mangoldt mass comes only from proper prime powers. The proof of Lemma 2.3 is translation-uniform throughout this range: each exponent \(k\ge2\) contributes at most one \(k\)-th power because consecutive \(k\)-th powers near \(P_n\) are separated by more than \(h_n\), and its weight is \(O(\log P_n/k)\). Summing over \(k\ll\log P_n\) gives \(O(\log P_n\log\log P_n)=o(h_n)\), uniformly in \(x\).'''
assert text.count(old) == 1
text = text.replace(old, new)

path.write_text(text, encoding='utf-8')
print(hashlib.sha256(text.encode()).hexdigest())
