# Largest-factor hyperbola source identity

Date: 28 July 2026  
Status: exact source identity and bounded column multiplicity proved; signed hyperbola-energy estimate open.

## 1. The depth barrier was representation-dependent

The standard convolution identity

\[
\boxed{
\Lambda(n)=\sum_{de=n}\mu(d)\log e
}
\tag{1.1}
\]

is exact and has only two factors.  It does not require a truncated or growing-depth
Heath--Brown identity.

The reason (1.1) was previously unattractive is that one of `d,e` can be
exponentially larger than the physical interval `H`.  The primorial-index
shrinking-target theorem changes that assessment: an exponentially large factor
has bounded centre multiplicity.

## 2. Group by the larger complementary divisor

For an unordered divisor pair

\[
DE=n,
\qquad D\ge E,
\]

define

\[
W(D,E)=
\begin{cases}
\mu(D)\log E+\mu(E)\log D,&D>E,\\[2mm]
\mu(D)\log D,&D=E.
\end{cases}
\tag{2.1}
\]

### Theorem 2.1 (largest-factor hyperbola identity)

For every integer `n>=2`,

\[
\boxed{
\Lambda(n)=
\sum_{\substack{DE=n\\D\ge E}}W(D,E).
}
\tag{2.2}
\]

### Proof

In (1.1), each ordered pair `(d,e)` with `d!=e` is grouped with its transpose
`(e,d)`.  Their combined weight is

\[
\mu(D)\log E+\mu(E)\log D.
\]

A diagonal pair `d=e=D` occurs once and has weight `mu(D) log D`.  This gives
(2.2).  \(\square\)

The cancellation that annihilates non-prime-power outputs remains inside the
signed weights `W(D,E)`.

## 3. Shifted outputs

Let

\[
n=P_j+m,
\qquad 2\le m\le H.
\]

Every pair in (2.2) has

\[
D\ge\sqrt n\ge\sqrt{P_0}.
\tag{3.1}
\]

For sufficiently large `X`,

\[
\sqrt{P_0}>H.
\tag{3.2}
\]

Thus every routed largest factor lies in the one-point regime of the shrinking-
target theorem.

For `D>H`, put

\[
E_j(D)=\left\lceil\frac{P_j}{D}\right\rceil,
\qquad
m_j(D)=D E_j(D)-P_j.
\tag{3.3}
\]

There is a factorisation

\[
P_j+m=DE,
\qquad D\ge E,
\qquad 2\le m\le H,
\]

with this fixed largest factor `D` if and only if

\[
2\le m_j(D)\le H,
\qquad
E_j(D)\le D.
\]

The complement and offset are then uniquely

\[
E=E_j(D),
\qquad
m=m_j(D).
\]

## 4. Exact orbit expansion of the one-sided detector

Recall

\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m).
\]

### Theorem 4.1 (largest-factor source identity)

For every sufficiently large `X`,

\[
\boxed{
\Psi_j(H)=
\sum_{D\ge\sqrt{P_j+2}}
\mathbf1_{\substack{2\le m_j(D)\le H\\E_j(D)\le D}}
W\bigl(D,E_j(D)\bigr).
}
\tag{4.1}
\]

Equivalently, the sum may be taken over all `D>H`, since the indicator and
`D>=E_j(D)` force `D>=sqrt(P_j+2)`.

### Proof

Apply (2.2) separately to every `P_j+m` and group the resulting terms by their
largest factor `D`.  Since `D>H`, equation (3.3) shows that a fixed pair `(j,D)`
selects at most one offset.  This is a finite rearrangement of an exact divisor
sum.  \(\square\)

No Fourier approximation, truncated identity, or divisor-switching remainder is
present in (4.1).

## 5. Exact double-source identity

For

\[
T_j(H)=\sum_{2\le m\le H}\Lambda(m)\Lambda(P_j+m),
\]

one has similarly

\[
\boxed{
T_j(H)=
\sum_{D>H}
\mathbf1_{\substack{2\le m_j(D)\le H\\E_j(D)\le D}}
\Lambda\bigl(m_j(D)\bigr)
W\bigl(D,E_j(D)\bigr).
}
\tag{5.1}
\]

The prime-offset main part is obtained by restricting to

\[
X<m_j(D)\le H.
\]

Offsets at most `X` contribute only the previously separated proper-prime-power
contamination to the shifted output.

## 6. Bounded column multiplicity

For a fixed numerical `D`, define its prime-offset support

\[
\mathcal J_D
=
\left\{
 j:
 X<m_j(D)\le H,
 E_j(D)\le D
\right\}.
\]

Since `D>=sqrt(P_0)`, the shrinking-target theorem gives

\[
|\mathcal J_D|
\le
1+
\left\lfloor
\frac{N-1}{
\left\lceil
\dfrac{\log(\sqrt{P_0}/H)}{\log(2X)}
\right\rceil}
\right\rfloor.
\tag{6.1}
\]

Using

\[
\log P_0\sim X,
\qquad
N\sim X/\log X,
\]

the denominator in (6.1) is asymptotic to `N/2`.  Hence:

### Corollary 6.1

Uniformly in the largest factor `D`,

\[
\boxed{
|\mathcal J_D|=O(1).
}
\tag{6.2}
\]

More precisely, the displayed bound is eventually at most three.

Thus (4.1) and (5.1) are sparse-column source representations: each largest-factor
column touches only boundedly many primorial centres, although a centre may meet
many columns.

## 7. The exact centred hyperbola source

Let `mu_j` be the deterministic prime-pair baseline and put

\[
c_j=\Psi_j(H)-\mu_j.
\]

Define

\[
X_{j,D}=
\mathbf1_{\substack{2\le m_j(D)\le H\\E_j(D)\le D}}
W\bigl(D,E_j(D)\bigr).
\tag{7.1}
\]

Then

\[
\boxed{
c_j=\sum_D X_{j,D}-\mu_j.
}
\tag{7.2}
\]

The Möbius signs in `W(D,E)` are load-bearing.  Squaring individual columns or
replacing `W` by its absolute value destroys the exact cancellation that makes
(2.2) equal to `Lambda`.

## 8. Consequence for the research programme

The former choice was framed as:

- use growing depth so that every divisor variable is physically small; or
- accept exponentially large variables with no usable average.

The exact alternative is now:

1. use the fixed two-factor identity `Lambda=mu*log`;
2. route each complementary divisor pair to its largest factor;
3. use the one-point orbit representation (3.3);
4. exploit the bounded centre multiplicity (6.2);
5. retain the signed Möbius cancellation across largest-factor columns.

This removes the growing-depth combinatorial explosion entirely.

## 9. New theorem boundary

The load-bearing estimate is now a signed sparse-column hyperbola inequality for

\[
\sum_j
\left|
\sum_D X_{j,D}-\mu_j
\right|^2.
\tag{9.1}
\]

The bounded column multiplicity recovers the factor `N` lost by a centre-by-centre
large-divisor treatment.  What remains is to control the interaction of the many
columns meeting a fixed centre without erasing the Möbius signs.

A sufficient next theorem is a centred large-factor dispersion estimate of the
form

\[
\sum_j
\left|
\sum_D X_{j,D}-\mu_j
\right|^2
\ll NHX L(X),
\qquad L(X)=o(\log X).
\tag{9.2}
\]

This is the original Fortune variance target, but its arithmetic source is now a
fixed-complexity sparse orbit transform rather than a growing-depth convolution.

## 10. Boundary

Proved:

1. exact grouped hyperbola identity (2.2);
2. exact one-sided and double-source orbit expansions (4.1), (5.1);
3. every routed largest factor exceeds `H`;
4. every largest-factor column has uniformly bounded centre multiplicity;
5. the previous growing-depth necessity is removed.

Open:

1. signed cancellation across the largest-factor columns;
2. construction of the baseline directly in the hyperbola representation;
3. the variance estimate (9.2);
4. Fortune's conjecture.
