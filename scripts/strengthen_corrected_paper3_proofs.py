from pathlib import Path

path = Path('publications/fortune-papers-ii-vi-20260724/paper3_pair_sum/manuscript.md')
text = path.read_text(encoding='utf-8')


def insert_before(anchor: str, block: str, marker: str) -> None:
    global text
    if marker in text:
        return
    if text.count(anchor) != 1:
        raise SystemExit(f'anchor count {text.count(anchor)} for {anchor!r}')
    text = text.replace(anchor, block.rstrip() + '\n\n' + anchor)


def replace_once(old: str, new: str) -> None:
    global text
    if new in text:
        return
    if text.count(old) != 1:
        raise SystemExit(f'anchor count {text.count(old)} for {old[:100]!r}')
    text = text.replace(old, new)

insert_before(
    '# 4. Exact two-scale energy decomposition',
    r'''### Expanded multiplicity proof

The endpoint-multiset identity gives the full classification directly. If
\(u=\{i,t\}\) and \(v=\{k,t\}\) share an index, then
\(D=P_i-P_k\). In
\(u\uplus v'=u'\uplus v\), the occurrence of \(k\) on the right can be
supplied on the left only by \(v'\), so \(v'=\{k,s\}\) for a unique
\(s\), and cancellation gives \(u'=\{i,s\}\). These are exactly the
\(N\) sliding representations. If \(u\cap v=\varnothing\), both entries of
\(v\) must be supplied by the two-entry multiset \(v'\); hence \(v'=v\)
and then \(u'=u\). Finally, equality
\(P_i-P_k=P_{i'}-P_{k'}\) is itself a coefficient-bounded relation, so
Theorem 2.1 makes the ordered endpoint pairs equal. This proves the count and
the pairwise distinctness. Appendix A.2 records the same case analysis in the
frozen numbering.''',
    '### Expanded multiplicity proof',
)

insert_before(
    '# 6. Sub-Weibull Lebesgue tails',
    r'''### Expanded labelled-lift count

For completeness, repeated endpoint indices cause no loss in Lemma 5.1.
Replace the occurrences in the common \(2k\)-multiset temporarily by distinct
labels. Every unlabelled ordered decomposition into pairs has at least one
labelled lift, while two different unlabelled decompositions have disjoint
sets of lifts. A labelled \(2k\)-set has \((2k-1)!!\) pair partitions and
\(k!\) orders of the pairs, giving at most
\((2k-1)!!k!=(2k)!/2^k\) unlabelled ordered decompositions. Appendix A.3
gives the identical argument in full.''',
    '### Expanded labelled-lift count',
)

insert_before(
    'The exponent constant \\(\\sqrt2\\) is sharp',
    r'''### Uniformity in the moment order

In Theorem 6.1, levels above \(M^2\) are empty. For
\(2M\le s\le M^2\), the selected order
\(k=\lfloor\sqrt{s/(2M)}\rfloor\) satisfies \(k\ll N<X/2\), so
\(X>2k+1\) holds for all sufficiently large \(X\). Stirling gives
\[
\frac{(2k)!}{2^k}(M/s)^k
\le e\sqrt{2k}\left(\frac{2k^2M}{e^2s}\right)^k
\le e\sqrt{2k}\,e^{-2k}.
\]
Since \(2k\ge\sqrt{2s/M}-2\), this is the stated bound. For
\(s=M+\lambda\), the remaining inequality is
\[
3+\tfrac14\log(2(t+1))-\sqrt{2(t+1)}+\sqrt t\le0,
\quad t=\lambda/M\ge121;
\]
it is negative at \(121\) and decreasing thereafter.''',
    '### Uniformity in the moment order',
)

insert_before(
    '# 10. The corrected covariance problem',
    r'''### Proof of Theorem 9.1

Let \(B_X\) count failed centres. At each failure \(Z_j=0\) and
\(\lambda_j\ge cX\), so
\[
B_Xc^2X^2\le\sum_{j<N}|Z_j-\lambda_j|^2\ll NXL(X).
\]
As \(N\asymp X/\log X\), this gives
\(B_X\ll L(X)/\log X=o(1)\). The integer \(B_X\) is therefore eventually
zero, and candidate collapse completes the implication.''',
    '### Proof of Theorem 9.1',
)

insert_before(
    'Thus the corrected second moment is an aggregated four-linear-form prime',
    r'''### Proof of (10.1)

Expanding \(Z_j^2\) gives ordered pairs \((m,n)\) of successful offsets.
The diagonal \(m=n\) contributes \(Z_j\). Every off-diagonal ordered pair is
uniquely \((m,m+d)\) or \((m+d,m)\) with \(d\ge1\); the two orders carry
the same four prime indicators. Hence the off-diagonal contribution is
\(2\sum_{1\le d<H}C_j(H;d)\), proving (10.1).''',
    '### Proof of (10.1)',
)

replace_once(
    '''Thus the corrected second moment is an aggregated four-linear-form prime
correlation. A two-output model for
\(\Lambda(P_j+m)\Lambda(P_j+m+d)\) alone does not represent it.''',
    '''Thus this unweighted formulation of the corrected second moment is an
aggregated four-linear-form prime correlation. A two-output model for
\(\Lambda(P_j+m)\Lambda(P_j+m+d)\) alone does not represent this particular
expansion. The weighted shifted detector of Paper II supplies a distinct
one-sided formulation and is not excluded by this observation.'''
)

replace_once(
    '''The new analytic problem is to derive (C1)--(C2), or an equivalent signed
transference theorem, with all four primality conditions coupled until after
centring.''',
    '''The new analytic problem along this unweighted route is to derive
(C1)--(C2), or an equivalent signed transference theorem, with all four
primality conditions coupled until after centring. A second live route starts
from the recentered weighted shifted detector \(\Psi_j-\mu_j\), where
candidate collapse already encodes offset primality; that route requires a
fresh proof of its principal term and source-to-frame transference rather than
an additional explicit offset-prime factor.'''
)

replace_once(
    '''The next integer theorem should therefore be an exact signed decomposition of
the prime-pair variance. The single-walk kernel is the first natural harmonic
object, as shown by the corrected Fourier identity in Paper II. Further
pair-sum moments or random-order derandomisation are secondary until that
source bridge is established.''',
    '''The next integer theorem should therefore be a corrected source-to-frame
transference for at least one of two routes: the unweighted four-form variance
above, or the recentered weighted shifted detector of Paper II. The
single-walk kernel is the first exact harmonic object for the explicit
double-von-Mangoldt source. The older pair-sum frame may still reappear after a
correct principal-term subtraction, but no such implication is presently
proved. Further pair-sum moments or random-order derandomisation are secondary
until one of these bridges is established.'''
)

path.write_text(text, encoding='utf-8')
print(path, len(text.splitlines()))
