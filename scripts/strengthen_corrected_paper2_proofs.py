from pathlib import Path

path = Path('publications/fortune-papers-ii-vi-20260724/paper2_revised/manuscript.md')
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

replace_once(
    '''The earlier reciprocal pair-sum frame and all of its internal moment, Möbius, character and no-go theorems are retained as independent structural results, but no source-to-frame implication from the corrected detector is claimed. The programme boundary is now a two-sided signed prime-pair transference theorem; work on the unweighted reciprocal frame alone cannot prove Fortune's conjecture.''',
    '''The earlier reciprocal pair-sum frame and all of its internal moment, Möbius, character and no-go theorems are retained as independent structural results, but no source-to-frame implication from the corrected detector is claimed. Two corrected transference routes remain open: recenter the one-sided shifted detector at its prime-pair main term and rebuild its principal component, or use the explicit double-von-Mangoldt source retaining both prime weights. The existing unweighted reciprocal estimate would prove Fortune only after one of these missing bridges is established.'''
)

replace_once(
    '''Second, the preceding programme introduced a principal-cancelled reciprocal frame whose columns are pair sums of consecutive-prime prefixes. Its exact internal kernel is''',
    '''Second, the preceding programme introduced a principal-cancelled reciprocal frame whose columns are pair sums of consecutive-prime prefixes. Candidate collapse does not by itself invalidate that one-sided architecture: the shifted detector \(\Psi_j\) is already a weighted prime-pair detector after recentering at \(\mu_j\). What is missing is a new derivation of the frame's principal term and a proof that its residual controls the corrected variance. Its exact internal kernel is'''
)

insert_before(
    '## Correct block-variance implications',
    r'''### Expanded coprimality and prime-power details

If \(P_j+m\) is prime and a prime \(q\mid(m,P_j)\), then
\(q\mid P_j+m\). Since \(q\le\ell_j<P_j+m\), this would be a proper
divisor of the output, a contradiction. Thus \((m,P_j)=1\), and Lemma 2.2
applies without an additional assumption.

For the remainder in Proposition 2.3, if \(r^k\asymp P_j\), then
\[
(r+1)^k-r^k\ge k r^{k-1}\gg P_j^{(k-1)/k}.
\]
This spacing is exponential in \(X\), hence larger than \(H\asymp X^2\),
uniformly for \(k\ge2\) once \(X\) is large. There is therefore at most one
\(k\)-th power in the interval for each exponent. Its weight is
\(\log r\le\log(2P_j)/k=O(X/k)\); and \(2^k\le2P_j\) gives \(k=O(X)\).
Summing \(X/k\) proves \(R_j(H)=O(X\log X)\).''',
    '### Expanded coprimality and prime-power details',
)

insert_before(
    'The Hardy--Littlewood model predicts the main term',
    r'''The spacing argument above also makes Lemma 2.6 explicit. At a failed
centre, each nonzero term has \(P_j+m=r^k\), and there is at most one such
power for each \(k\). Its two weights contribute at most
\(O((X/k)\log X)\). Summing over \(k=O(X)\) gives
\(O(X(\log X)^2)\).''',
    'The spacing argument above also makes Lemma 2.6 explicit',
)

insert_before(
    'The first exact harmonic object attached to the corrected source is therefore',
    r'''### Expanded Fourier-sign verification

Expanding the integrand in Theorem 2.8 gives
\[
G_X(\theta)e(-P_j\theta)
=\sum_{m,n}a_H(m)b_X(n)e((n-m-P_j)\theta).
\]
Orthogonality forces \(n=P_j+m\), leaving exactly \(T_j(H)\). In the
squared block sum, the conjugate contributes \(e(P_j\beta)\), so
\[
\sum_{j<N}e(-P_j\alpha)e(P_j\beta)=F_X(\beta-\alpha).
\]
This derives both Fourier signs and the single-walk kernel directly; all sums
are finite.''',
    '### Expanded Fourier-sign verification',
)

replace_once(
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
)

replace_once(
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
)

replace_once(
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
)

replace_once(
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
)

replace_once(
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
)

path.write_text(text, encoding='utf-8')
print(path, len(text.splitlines()))
