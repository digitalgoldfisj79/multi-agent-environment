from pathlib import Path

path = Path('publications/fortune-papers-ii-vi-20260724/paper2_revised/manuscript.md')
text = path.read_text(encoding='utf-8')

replacements = [
(
'''The earlier reciprocal pair-sum frame and all of its internal moment, Möbius, character and no-go theorems are retained as independent structural results, but no source-to-frame implication from the corrected detector is claimed. The programme boundary is now a two-sided signed prime-pair transference theorem; work on the unweighted reciprocal frame alone cannot prove Fortune's conjecture.''',
'''The earlier reciprocal pair-sum frame and all of its internal moment, Möbius, character and no-go theorems are retained as independent structural results, but no source-to-frame implication from the corrected detector is claimed. Two corrected transference routes remain open: recenter the one-sided shifted detector at its prime-pair main term and rebuild its principal component, or use the explicit double-von-Mangoldt source retaining both prime weights. The existing unweighted reciprocal estimate would prove Fortune only after one of these missing bridges is established.'''
),
(
'''Second, the preceding programme introduced a principal-cancelled reciprocal frame whose columns are pair sums of consecutive-prime prefixes. Its exact internal kernel is''',
'''Second, the preceding programme introduced a principal-cancelled reciprocal frame whose columns are pair sums of consecutive-prime prefixes. Candidate collapse does not by itself invalidate that one-sided architecture: the shifted detector \(\Psi_j\) is already a weighted prime-pair detector after recentering at \(\mu_j\). What is missing is a new derivation of the frame's principal term and a proof that its residual controls the corrected variance. Its exact internal kernel is'''
),
(
'''If \(P_j+m\) is prime, then \((m,P_j)=1\); otherwise a common
prime divisor would divide the prime output. Lemma 2.2 therefore forces \(m\)
to be prime.''',
'''If \(P_j+m\) is prime, then \((m,P_j)=1\). Indeed, if a prime
\(q\mid(m,P_j)\), then \(q\mid P_j+m\); but \(q\le\ell_j<P_j+m\), so the
output would have a proper divisor and could not be prime. Lemma 2.2 therefore
forces \(m\) to be prime.'''
),
(
'''The remaining von Mangoldt terms are proper
prime powers. Near \(P_j\), consecutive \(k\)-th powers are separated by more
than \(H\); for each \(k\ge2\) there is at most one, with weight
\(O(X/k)\). Summing over \(k\ll X\) gives \(O(X\log X)\). \(\square\)''',
'''The remaining von Mangoldt terms are proper prime powers. If
\(r^k\asymp P_j\), then
\[
(r+1)^k-r^k\ge k r^{k-1}\gg P_j^{(k-1)/k},
\]
which is exponentially large in \(X\) and therefore exceeds
\(H\asymp X^2\), uniformly for every \(k\ge2\), once \(X\) is large. Thus
there is at most one \(k\)-th power in the interval for each exponent. Its
von Mangoldt weight is \(\log r\le \log(2P_j)/k=O(X/k)\). The possible
exponents satisfy \(2^k\le2P_j\), hence \(k=O(X)\), and summing \(X/k\)
gives \(O(X\log X)\). \(\square\)'''
),
(
'''Every nonzero term must have \(P_j+m=r^k\) with \(k\ge2\).
For each exponent \(k\), the interval contains at most one such power.
Moreover \(\Lambda(P_j+m)\ll X/k\) and \(\Lambda(m)\le\log H\ll\log X\).
Summing over \(k\ll X\) gives the result. \(\square\)''',
'''Every nonzero term must have \(P_j+m=r^k\) with \(k\ge2\).
As in Proposition 2.3,
\((r+1)^k-r^k\ge k r^{k-1}\gg P_j^{(k-1)/k}>H\), so the interval contains
at most one such power for each exponent. Moreover
\(\Lambda(P_j+m)=\log r\ll X/k\) and
\(\Lambda(m)\le\log H\ll\log X\). Since \(k=O(X)\), summing
\(X\log X/k\) gives \(O(X(\log X)^2)\). \(\square\)'''
),
(
'''**Proof.** Expanding (2.23), orthogonality forces
\(n-m-P_j=0\), leaving the defining correlation \(T_j\). Squaring, summing
over \(j\), and interchanging the finite sums and integrals gives the first
term in (2.24); the cross term and baseline square are immediate. \(\square\)''',
'''**Proof.** From the definitions,
\[
G_X(\theta)e(-P_j\theta)
=\sum_{m,n}a_H(m)b_X(n)e((n-m-P_j)\theta).
\]
Integration over \([0,1]\) is one precisely when \(n-m-P_j=0\) and zero
otherwise. Hence \(n=P_j+m\), and the surviving sum is exactly
\(\sum_{2\le m\le H}\Lambda(m)\Lambda(P_j+m)=T_j(H)\); this also fixes both
Fourier signs. For the square, insert (2.23) and its complex conjugate:
\[
\sum_j e(-P_j\alpha)e(P_j\beta)=F_X(\beta-\alpha).
\]
Expanding \(\sum_j|T_j-\nu_j|^2\) then gives the double-integral term, the
stated cross term with \(V_X(-\alpha)\), and \(\sum_j\nu_j^2\). All sums are
finite, so the interchanges require no convergence argument. \(\square\)'''
),
(
'''The first exact harmonic object attached to the corrected source is therefore
the single-walk polynomial \(F_X\), with source
\(G_X=A_HB_X\) containing both von Mangoldt factors. Any reciprocal or
divisor-frame transference must preserve both factors and their common offset
variable, or prove a separate signed inequality that removes one of them. The
unweighted pair-sum frame below contains no such source factor and is retained
as a model problem rather than a proved reduction of (2.16).''',
'''For the explicit double-von-Mangoldt route, the first exact harmonic object is
the single-walk polynomial \(F_X\), and the source
\(G_X=A_HB_X\) retains both von Mangoldt factors and their common offset.
There is also a distinct one-sided route: Proposition 2.3 shows that the
shifted detector \(\Psi_j\), after recentering at \(\mu_j\) and controlling
\(R_j\), is already a weighted prime-pair detector. A reciprocal
transference from that source need not introduce an explicit factor \(A_H\),
but it must recompute the principal term at the square-root sieve boundary.
The pair-sum frame below is therefore retained as a model whose connection to
either corrected source remains unproved, not as a route that has been
refuted.'''
),
(
'''Equation (3.6) is not presently derived from Theorems 2.4--2.7. After candidate-collapse correction, the exact source identity (2.24) contains the additional prime-offset factor \(A_H\). Consequently (3.6) is treated only as a deterministic model estimate whose exact internal structure is analysed below. Proving it, including for the increasing order, would not by itself prove Fortune without a new signed two-prime transference theorem.''',
'''Equation (3.6) is not presently derived from Theorems 2.4--2.7. For the
double-von-Mangoldt source, (2.24) contains the additional factor \(A_H\).
For the recentered one-sided source \(\Psi_j-\mu_j\), that factor is implicit
rather than explicit, but the old principal cancellation was calibrated at
\(H\) and has not been rebuilt at \(\mu_j\). Consequently (3.6) is treated as
a deterministic model estimate whose internal structure is analysed below.
Proving it for the increasing order could contribute to Fortune only together
with a new corrected source-to-frame theorem; the present manuscript neither
proves nor rules out such a theorem.'''
),
(
'''- The exact Fourier source is \(G_X=A_HB_X\), and its first geometric kernel is
  the single-walk polynomial \(F_X\).
- The reciprocal pair-sum frame omits \(A_H\). Its internal identities remain
  correct, but its connection to Fortune is unproved and must be reconstructed.''',
'''- The explicit double-von-Mangoldt source is \(G_X=A_HB_X\), and its first
  geometric kernel is the single-walk polynomial \(F_X\).
- The shifted detector \(\Psi_j-\mu_j\) supplies a second, one-sided corrected
  source in which offset primality is encoded by candidate collapse.
- The reciprocal pair-sum frame is not presently derived from either corrected
  source. Its internal identities remain correct, and a recentered principal
  term may still make it relevant, but that transference must be proved.'''
),
(
'''The next theorem obligation is an exact signed decomposition of (2.24) in
which both prime factors remain coupled. Only after such a decomposition is
proved can one determine whether the existing reciprocal frame, the
single-walk energy isolated in Paper III, or a new kernel is the correct
analytic target.''',
'''The next theorem obligation is a corrected source-to-frame theorem along at
least one of two routes. Route A starts from \(\Psi_j-\mu_j\) and must rebuild
the roughness/Buchstab principal term before isolating a reciprocal residual.
Route B starts from (2.24) and seeks a signed decomposition in which both von
Mangoldt factors remain coupled. Only after one of these bridges is proved can
one determine whether the existing reciprocal frame, the single-walk energy
isolated in Paper III, or a new kernel is the load-bearing deterministic
target.'''
),
(
'''The corrected route is now explicit: calibrate the prime-pair main term; prove
the block-variance implication around that main term; derive a signed
source-to-frame identity retaining both prime factors; and only then
attack the resulting deterministic energy. Theorem 2.8 completes the first
exact source step and shows why the single-walk kernel precedes the pair-sum
kernel.''',
'''The corrected route is now explicit: calibrate the prime-pair main term and
prove the block-variance implication around it, then derive a corrected
source-to-frame identity. This may proceed by recentering the one-sided
shifted detector at \(\mu_j\), or by retaining both weights in the
double-von-Mangoldt source. Theorem 2.8 completes the first exact source step
for the latter route and shows why its single-walk kernel precedes any
pair-sum lift.'''
),
]

for old, new in replacements:
    if text.count(old) != 1:
        raise SystemExit(f'expected exactly one match, found {text.count(old)} for:\n{old[:120]}')
    text = text.replace(old, new)

path.write_text(text, encoding='utf-8')
print(path, len(text.splitlines()))
