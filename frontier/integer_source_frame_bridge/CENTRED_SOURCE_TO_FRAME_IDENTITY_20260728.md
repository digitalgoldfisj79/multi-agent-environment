# Centred source-to-frame identity

Date: 28 July 2026  
Status: exact finite identities proved; arithmetic lower-frame and source estimates open.

## 1. Scope

This note closes the algebraic part of Route A from corrected Paper II.

The starting point is the one-sided shifted detector

\[
\Psi_j(H)=\sum_{2\le m\le H}\Lambda(P_j+m)
\]

with deterministic prime-pair baseline \(\mu_j\asymp H\).  The residual vector is

\[
c_j=\Psi_j(H)-\mu_j.
\]

The essential correction is that \(c_j\) is retained as a column weight throughout
the harmonic transformation.  The principal term is subtracted before any square,
dual-row average or pair lift is taken.

No Hardy--Littlewood asymptotic is proved here.  The baselines may be any
deterministic real numbers of the sizes required by the block criterion.

## 2. The shifted detector itself is load-bearing

Assume \(H=\eta X^2\), \(N\asymp X/\log X\), and

\[
cH\le \mu_j\le CH.
\]

### Theorem 2.1 (one-sided shifted-detector criterion)

If

\[
\sum_{j<N}|\Psi_j(H)-\mu_j|^2
 \ll NHX L(X),
\qquad L(X)=o(\log X),
\]

then every centre in the block has a prime in
\([P_j+2,P_j+H]\) for all sufficiently large \(X\).

### Proof

At a failed centre the prime part of \(\Psi_j\) is absent.  Corrected Paper II,
Proposition 2.3, gives

\[
\Psi_j(H)=R_j(H)=O(X\log X),
\]

where \(R_j\) is supported on proper output prime powers.  Since
\(\mu_j\ge cH\asymp X^2\),

\[
|\Psi_j-\mu_j|\ge \frac c2H
\]

for large \(X\).  If \(B_X\) centres fail, then

\[
B_XH^2\ll NHXL(X),
\]

and hence

\[
B_X\ll \frac{NX}{H}L(X)
 \asymp \frac{L(X)}{\log X}=o(1).
\]

Thus \(B_X=0\).  \(\square\)

This theorem permits the exact Fourier source for \(\Psi_j\) to be used directly.
The proper-prime-power terms do not need to be deleted before the frame is formed.

## 3. Subtract the principal term in source space

Put

\[
D_H(\alpha)=\sum_{2\le m\le H}e(-m\alpha),
\qquad
B_X(\alpha)=\sum_n b_X(n)e(n\alpha),
\]

where \(b_X(n)=\Lambda(n)\) on a finite interval containing every shifted output
and is zero outside it.  Let

\[
U_X(\alpha)=D_H(\alpha)B_X(\alpha).
\]

Then the \(P_j\)-th Fourier coefficient of \(U_X\) is exactly \(\Psi_j(H)\).

Define the baseline polynomial and the centred source

\[
M_X(\alpha)=\sum_{j<N}\mu_j e(P_j\alpha),
\qquad
\mathscr R_X(\alpha)=U_X(\alpha)-M_X(\alpha).
\]

Let

\[
F_X(\theta)=\sum_{j<N}e(P_j\theta),
\qquad
C_X(\theta)=\sum_{j<N}c_j e(P_j\theta).
\]

### Theorem 3.1 (centred source projection)

One has exactly

\[
\boxed{
c_j=\int_0^1\mathscr R_X(\alpha)e(-P_j\alpha)\,d\alpha
}
\tag{3.1}
\]

and

\[
\boxed{
C_X(\theta)
 =\int_0^1\mathscr R_X(\alpha)
   F_X(\theta-\alpha)\,d\alpha.
}
\tag{3.2}
\]

Consequently,

\[
\boxed{
\sum_{j<N}|c_j|^2
 =\int_0^1|C_X(\theta)|^2\,d\theta.
}
\tag{3.3}
\]

### Proof

The \(P_j\)-coefficient of \(U_X\) is \(\Psi_j\), while the \(P_j\)-coefficient
of \(M_X\) is \(\mu_j\), because the centres are distinct.  This proves (3.1).
Insert (3.1) into the definition of \(C_X\), interchange the finite sum and
integral, and obtain (3.2).  Equation (3.3) is Parseval for the distinct
frequencies \(P_j\).  \(\square\)

Equation (3.2) is the exact source-to-walk map.  It retains the nonconstant
baselines \(\mu_j\) without approximation.

## 4. The exact centred reciprocal frame

Use the reciprocal rows of Paper II.  For positive harmonic \(a\), write

\[
m_a=\sum_{q\in\mathcal Q_X}p_{q,a},
\qquad
\Theta_{a,X}(L)=
 \sum_{q\in\mathcal Q_X}p_{q,a}e(aL/q).
\]

Only harmonics with \(m_a>0\) are used.  Put

\[
\phi_{a,X}(L)=\frac{\Theta_{a,X}(L)}{m_a}.
\]

Thus \(\phi_{a,X}(0)=1\).  Since the full row measure is symmetric,

\[
\sum_{a\ge1}m_a=\frac12.
\]

Define the aggregate autocorrelation kernel

\[
\boxed{
\mathcal K_X(L)
 =2\sum_{\substack{a\ge1\\m_a>0}}
   \frac{|\Theta_{a,X}(L)|^2}{m_a}
 =2\sum_a m_a|\phi_{a,X}(L)|^2.
}
\tag{4.1}
\]

It satisfies

\[
0\le\mathcal K_X(L)\le1,
\qquad
\mathcal K_X(0)=1.
\tag{4.2}
\]

For a residual vector \(c=(c_j)\), define

\[
\boxed{
\begin{aligned}
\mathfrak G_X(c)
={}&2\sum_{\substack{a\ge1\\m_a>0}}\frac1{m_a}
 \sum_{q,r\in\mathcal Q_X}p_{q,a}p_{r,a}\\
&\times
\left|
 C_X\!\left(a\left(\frac1q-\frac1r\right)\right)
\right|^2.
\end{aligned}
}
\tag{4.3}
\]

By (3.2), the quantity inside the absolute value is exactly

\[
\int_0^1\mathscr R_X(\alpha)
 F_X\!\left(
 a\left(\frac1q-\frac1r\right)-\alpha
 \right)d\alpha.
\tag{4.4}
\]

Thus (4.3) is an exact frame of the centred source, not a geometric surrogate.

### Theorem 4.1 (centred dual-row identity)

One has

\[
\boxed{
\mathfrak G_X(c)
 =\sum_{j,k<N}
  c_j\overline{c_k}\,
  \mathcal K_X(P_j-P_k).
}
\tag{4.5}
\]

In particular,

\[
\boxed{
\mathfrak G_X(c)
 =\sum_{j<N}|c_j|^2
 +\sum_{\substack{j,k<N\\j\ne k}}
  c_j\overline{c_k}\,
  \mathcal K_X(P_j-P_k).
}
\tag{4.6}
\]

### Proof

Expand the square in (4.3).  For fixed \(a,j,k\), the two row sums factor as

\[
\sum_{q,r}p_{q,a}p_{r,a}
 e\!\left(
 a\left(\frac1q-\frac1r\right)(P_j-P_k)
 \right)
 =
 |\Theta_{a,X}(P_j-P_k)|^2.
\]

Summing over \(a\) gives (4.5).  Since \(\mathcal K_X(0)=1\), separating
\(j=k\) gives (4.6).  \(\square\)

### Corollary 4.2 (frame-operator form)

Let

\[
\mathbf K_X=
 \bigl(\mathcal K_X(P_j-P_k)\bigr)_{j,k<N}.
\]

Then \(\mathbf K_X\) is Hermitian positive semidefinite, has diagonal entries
one, and

\[
\mathfrak G_X(c)=c^*\mathbf K_Xc.
\tag{4.7}
\]

Therefore

\[
\mathfrak G_X(c)-\|c\|_2^2
 =c^*(\mathbf K_X-I)c.
\tag{4.8}
\]

If, for some fixed \(\kappa>0\),

\[
c^*\mathbf K_Xc\ge\kappa\|c\|_2^2
\tag{4.9}
\]

for the actual detector residual vector, and if

\[
\mathfrak G_X(c)\ll NHXL(X),
\qquad L(X)=o(\log X),
\tag{4.10}
\]

then Theorem 2.1 proves every centre in the block.

A stronger source-independent sufficient condition is

\[
\|\mathbf K_X-I\|_{\mathrm{op}}\le1-\kappa.
\tag{4.11}
\]

The exact open transference problem is now (4.9)--(4.10), not an estimate for
the old coefficient-free pair frame.

## 5. Baseline subtraction cannot be postponed

Write

\[
S_\Psi(\theta)=\sum_j\Psi_j e(P_j\theta),
\qquad
S_\mu(\theta)=\sum_j\mu_j e(P_j\theta).
\]

Then at every row frequency,

\[
\boxed{
|C_X(\theta)|^2
 =
 |S_\Psi(\theta)|^2
 -2\Re\!\left(
 S_\Psi(\theta)\overline{S_\mu(\theta)}
 \right)
 +|S_\mu(\theta)|^2.
}
\tag{5.1}
\]

The cross term and baseline square are exact parts of the frame.  They cannot
be replaced by a universal subtraction such as a column count.  In particular,
the nonconstant \(\mu_j\) remain visible in every row.

### Proposition 5.1 (coefficient-erasure no-go)

No coefficient-independent frame depending only on the centres and reciprocal
rows can be an algebraic identity for

\[
\sum_j|\Psi_j-\mu_j|^2
\]

over all finite sources.

### Proof

Fix the centres and rows.  The old unweighted frame is then fixed.  The centred
source may have residual vector \(c=0\), or may be changed at one selected
Fourier coefficient to have \(c=e_t\).  The two block variances are respectively
zero and one, while every coefficient-free frame quantity is unchanged.
Therefore the residual coefficients, or information algebraically equivalent
to them, must occur in any exact identity.  \(\square\)

This proposition does not rule out a deeper analytic theorem specialised to the
von Mangoldt source.  It rules out treating the old raw frame itself as the
source-to-frame identity.

## 6. The source-weighted pair lift

The pair-sum geometry can still be retained, but only with source weights.

Let

\[
S_{jk}=P_j+P_k,
\qquad 0\le j\le k<N.
\]

The literal square of the centred walk is

\[
C_X(\theta)^2
 =\sum_{j\le k}
  (2-\delta_{jk})c_jc_k e(S_{jk}\theta).
\tag{6.1}
\]

For a canonically normalised symmetric-square lift, put

\[
d_{jk}=\sqrt{2-\delta_{jk}}\,c_jc_k.
\tag{6.2}
\]

Then

\[
\sum_{j\le k}|d_{jk}|^2
 =\left(\sum_j|c_j|^2\right)^2.
\tag{6.3}
\]

Define

\[
H_{2,c}^{\mathrm{sym}}(\theta)
 =\sum_{j\le k}d_{jk}e(S_{jk}\theta)
\tag{6.4}
\]

and

\[
\boxed{
\begin{aligned}
\mathfrak P_X(c)
={}&2\sum_{\substack{a\ge1\\m_a>0}}\frac1{m_a}
 \sum_{q,r}p_{q,a}p_{r,a}\\
&\times
\left|
H_{2,c}^{\mathrm{sym}}\!\left(
 a\left(\frac1q-\frac1r\right)
\right)
\right|^2.
\end{aligned}
}
\tag{6.5}
\]

### Theorem 6.1 (source-weighted pair-sum identity)

With pair indices \(u=(j,k)\), one has exactly

\[
\boxed{
\mathfrak P_X(c)
 =\sum_{u,v}
 d_u\overline{d_v}\,
 \mathcal K_X(S_u-S_v).
}
\tag{6.6}
\]

Consequently,

\[
\boxed{
\mathfrak P_X(c)
 =
 \left(\sum_j|c_j|^2\right)^2
 +\sum_{u\ne v}
 d_u\overline{d_v}\,
 \mathcal K_X(S_u-S_v).
}
\tag{6.7}
\]

The proof is the same dual-row expansion as Theorem 4.1.

For the literal square coefficients
\(w_{jk}=(2-\delta_{jk})c_jc_k\), the diagonal coefficient mass is

\[
\sum_{j\le k}|w_{jk}|^2
 =
 2\left(\sum_j|c_j|^2\right)^2
 -\sum_j|c_j|^4.
\tag{6.8}
\]

Thus the pair-sum architecture survives as a source-weighted symmetric-square
frame.  Replacing \(d_{jk}\) by one produces the old unweighted geometric frame
and erases the detector.

## 7. What has and has not been achieved

### Proved

1. The one-sided shifted detector centred at \(\mu_j\) has a direct
   all-centres variance criterion.
2. Principal subtraction can be made exactly in Fourier source space.
3. The residual vector maps exactly to the weighted single-walk frame
   (4.3)--(4.6).
4. The reciprocal frame defect is the explicit quadratic form
   \(c^*(\mathbf K_X-I)c\).
5. The pair-sum lift exists exactly with coefficients
   \(\sqrt{2-\delta_{jk}}c_jc_k\).
6. A coefficient-free frame cannot be the algebraic transference identity.

### Open

1. Prove the lower frame bound (4.9), uniformly or on the actual
   von-Mangoldt residual class.
2. Prove the source-frame upper bound (4.10) at the random variance scale.
3. Determine whether the arithmetic structure of the actual residuals makes
   (4.9) substantially easier than a full operator-norm estimate.
4. Decide whether the weighted pair lift (6.7) permits any of Papers I--IV's
   collision geometry to control the off-diagonal term without erasing the
   weights.

The old unweighted pair frame and its derandomisation remain secondary until
one of these source-weighted estimates is proved.
