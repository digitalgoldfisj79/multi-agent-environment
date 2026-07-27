from pathlib import Path
import re

path = Path('publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md')
text = path.read_text(encoding='utf-8')


def sub_once(pattern: str, replacement: str, source: str) -> str:
    updated, count = re.subn(pattern, replacement, source, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f'expected one regex match, found {count}: {pattern[:100]}')
    return updated

proof3 = r'''If two representations satisfy
\[
S_u-S_v=S_{u'}-S_{v'},
\]
then
\[
S_u+S_{v'}=S_{u'}+S_v.
\]
The resulting relation has coefficients bounded by four, so Theorem 2.1 forces
the endpoint multiset identity
\[
u\uplus v'=u'\uplus v.
\]
If \(u\) and \(v\) share an index \(t\), write
\(u=\{i,t\}\) and \(v=\{k,t\}\). Then
\(D=P_i-P_k\). In the multiset identity, the index \(k\) on the right can
occur on the left only inside \(v'\); because \(v'\) has two entries,
\(v'=\{k,s\}\) for a unique \(s\), and cancellation then gives
\(u'=\{i,s\}\). These are exactly the \(N\) sliding representations.
If \(u\cap v=\varnothing\), every entry of \(v\) must be supplied by the
two-entry multiset \(v'\), so \(v'=v\), and then \(u'=u\). This also proves
that no difference outside the sliding family has a second representation.
The pairwise distinctness of the values \(P_i-P_k\) follows by applying
Theorem 2.1 to the resulting coefficient-bounded relation. The fully expanded
case analysis is reproduced independently in Appendix A.2. \(\square\)
'''
text = sub_once(
    r'(# 3\. Difference-multiplicity dichotomy.*?### Proof\n\n).*?(\n# 4\. Exact two-scale energy decomposition)',
    lambda m: m.group(1) + proof3 + m.group(2),
    text,
)

proof5 = r'''Orthogonality counts two ordered \(k\)-tuples of unordered pairs with equal
endpoint sum. The induced integer relation has coefficients bounded by
\(2k\), so Theorem 2.1 forces equality of the total endpoint multiset.
Fix that multiset and replace repeated entries temporarily by distinct labels.
Every unlabelled ordered decomposition has at least one labelled lift, and
different unlabelled decompositions have disjoint sets of labelled lifts.
A labelled \(2k\)-set has \((2k-1)!!\) partitions into \(k\) unordered pairs
and \(k!\) orders of those pairs, hence at most
\[
(2k-1)!!\,k!=\frac{(2k)!}{2^k}
\]
unlabelled ordered decompositions. There are \(M^k\) choices for the first
\(k\)-tuple. This is also the labelled-lift argument recorded in Appendix
A.3. \(\square\)
'''
text = sub_once(
    r'(# 5\. High moments.*?### Proof\n\n).*?(\n# 6\. Sub-Weibull Lebesgue tails)',
    lambda m: m.group(1) + proof5 + m.group(2),
    text,
)

proof6 = r'''Choose \(k=\lfloor\sqrt{s/(2M)}\rfloor\). Since \(s\ge2M\), one has
\(k\ge1\); and since \(|H_2|^2\le M^2\), it is enough to consider
\(s\le M^2\), for which \(k\ll N<X/2\) for all sufficiently large \(X\).
Thus the hypothesis \(X>2k+1\) of Lemma 5.1 is available uniformly.
Markov's inequality gives
\[
\operatorname{meas}\{|H_2|^2\ge s\}
\le \frac{(2k)!}{2^k}\left(\frac Ms\right)^k.
\]
Using \((2k)!\le e(2k)^{2k+1/2}e^{-2k}\) and
\(k^2\le s/(2M)\), the right side is at most
\[
e\sqrt{2k}\,e^{-2k}
\le e^3(2s/M)^{1/4}\exp\!\left(-\sqrt{2s/M}\right),
\]
because \(2k\ge\sqrt{2s/M}-2\). For the centred form take
\(s=M+\lambda\), write \(t=\lambda/M\), and verify that
\[
3+\tfrac14\log(2(t+1))-\sqrt{2(t+1)}+\sqrt t\le0
\]
for \(t\ge121\); its derivative is negative there and the value at \(121\)
is negative. The same details are recorded in Appendix A.3. \(\square\)
'''
text = sub_once(
    r'(# 6\. Sub-Weibull Lebesgue tails.*?### Proof\n\n).*?(\nThe exponent constant)',
    lambda m: m.group(1) + proof6 + m.group(2),
    text,
)

proof9 = r'''### Proof

Let \(B_X\) be the number of failed centres. At each such centre \(Z_j=0\),
while \(\lambda_j\ge cX\); hence
\[
B_Xc^2X^2
\le \sum_{j<N}|Z_j-\lambda_j|^2
\ll NXL(X).
\]
Using \(N\asymp X/\log X\) gives
\[
B_X\ll \frac{L(X)}{\log X}=o(1).
\]
Since \(B_X\) is a nonnegative integer, it is eventually zero. Candidate
collapse then makes every corresponding Fortunate offset prime. \(\square\)
'''
text = sub_once(
    r'The proof is the one-failure argument:.*?N\\asymp X/\\log X\)\.',
    proof9.rstrip(),
    text,
)

old = '''Thus the corrected second moment is an aggregated four-linear-form prime
correlation. A two-output model for
\(\Lambda(P_j+m)\Lambda(P_j+m+d)\) alone does not represent it.'''
new = r'''### Proof of the expansion

Expanding \(Z_j^2\) gives an ordered sum over two successful offsets
\((m,n)\). The diagonal \(m=n\) contributes exactly \(Z_j\). Every
off-diagonal ordered pair occurs uniquely as either \((m,m+d)\) or
\((m+d,m)\), with \(d\ge1\), and both orders have the same four indicator
factors. Their combined contribution is therefore
\(2\sum_{1\le d<H}C_j(H;d)\), proving (10.1).

Thus this unweighted formulation of the corrected second moment is an
aggregated four-linear-form prime correlation. A two-output model for
\(\Lambda(P_j+m)\Lambda(P_j+m+d)\) alone does not represent this particular
expansion. The weighted shifted detector of Paper II provides a distinct
one-sided formulation and is not excluded by this observation.'''
if text.count(old) != 1:
    raise SystemExit(f'covariance anchor count {text.count(old)}')
text = text.replace(old, new)

old = '''The new analytic problem is to derive (C1)--(C2), or an equivalent signed
transference theorem, with all four primality conditions coupled until after
centring.'''
new = '''The new analytic problem along this unweighted route is to derive
(C1)--(C2), or an equivalent signed transference theorem, with all four
primality conditions coupled until after centring. A second live route starts
from the recentered weighted shifted detector \(\Psi_j-\mu_j\), where
candidate collapse already encodes offset primality; that route requires a
fresh proof of its principal term and source-to-frame transference rather than
an additional explicit offset-prime factor.'''
if text.count(old) != 1:
    raise SystemExit(f'route anchor count {text.count(old)}')
text = text.replace(old, new)

old = '''The next integer theorem should therefore be an exact signed decomposition of
the prime-pair variance. The single-walk kernel is the first natural harmonic
object, as shown by the corrected Fourier identity in Paper II. Further
pair-sum moments or random-order derandomisation are secondary until that
source bridge is established.'''
new = '''The next integer theorem should therefore be a corrected source-to-frame
transference for at least one of two routes: the unweighted four-form variance
above, or the recentered weighted shifted detector of Paper II. The
single-walk kernel is the first exact harmonic object for the explicit
double-von-Mangoldt source. The older pair-sum frame may still reappear after a
correct principal-term subtraction, but no such implication is presently
proved. Further pair-sum moments or random-order derandomisation are secondary
until one of these bridges is established.'''
if text.count(old) != 1:
    raise SystemExit(f'boundary anchor count {text.count(old)}')
text = text.replace(old, new)

path.write_text(text, encoding='utf-8')
print(path, len(text.splitlines()))
