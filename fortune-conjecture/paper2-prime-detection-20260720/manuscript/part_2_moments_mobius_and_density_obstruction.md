# Exact Lebesgue moments of the pair-sum kernel

The size of the trigonometric kernel itself is not mysterious. Its Lebesgue moments are determined by the superincreasing geometry of the primorial-prefix path.

## Four-copy rigidity

Within the dyadic block, successive prefixes satisfy

\[
P_{j+1}=\ell_{j+1}P_j,
\qquad
\ell_{j+1}\ge X.
\]

For large \(X\),

\[
4\sum_{i<j}P_i<P_j.
\tag{4.1}
\]

**Lemma 4.1 (four-copy rigidity).** For sufficiently large \(X\), an equality

\[
P_i+P_j+P_k+P_\ell
=P_a+P_b+P_c+P_d
\tag{4.2}
\]

holds if and only if the two multisets of endpoint indices are equal.

**Proof.** If the multiplicity vectors differ, let \(t\) be the largest index at which they differ. The coefficient of \(P_t\) in the difference has absolute value at least one and at most four, while the total contribution from smaller indices is less than \(P_t\) by (4.1). Cancellation is impossible. \(\square\)

## Fourth moment

**Theorem 4.2 (exact pair-sum fourth moment).** One has

\[
\boxed{
\int_0^1|H_2(\theta)|^4\,d\theta
=
\frac{N(3N^3-2N^2+2N-1)}2.
}
\tag{4.3}
\]

Consequently,

\[
\boxed{
\int_0^1\bigl(|H_2(\theta)|^2-M\bigr)^2\,d\theta
=
\frac{N(N-1)(5N^2-N+2)}4
=5M^2\bigl(1+O(N^{-1})\bigr).
}
\tag{4.4}
\]

**Proof.** By orthogonality, the fourth moment counts ordered decompositions of an endpoint multiset of size four into two unordered pairs. There are five multiplicity types:

| Endpoint multiplicities | Number of multisets | Ordered decompositions | Contribution |
|---|---:|---:|---:|
| \(1+1+1+1\) | \(\binom N4\) | 6 | \(36\binom N4\) |
| \(2+1+1\) | \(N\binom{N-1}2\) | 4 | \(16N\binom{N-1}2\) |
| \(2+2\) | \(\binom N2\) | 3 | \(9\binom N2\) |
| \(3+1\) | \(N(N-1)\) | 2 | \(4N(N-1)\) |
| \(4\) | \(N\) | 1 | \(N\) |

Summing gives (4.3). Pair-sum injectivity gives \(\int_0^1|H_2|^2=M\), so expanding the centred square gives (4.4). \(\square\)

The theorem solves the kernel-size side of the reciprocal-frame problem. If the arithmetic sampling measure behaved like Lebesgue measure at second moment, the desired scale would follow. The open issue is concentration of the reciprocal prime-pair atoms on the high-value sets of the kernel.

## A strictly weaker level-set target

Let \(\mu_{X,a}\) be the positive measure on \(\mathbb R/\mathbb Z\) assigning mass \(p_{q,a}p_{r,a}\) to

\[
\theta_{q,r}=a\left(\frac1q-\frac1r\right),
\qquad q\ne r,
\]

and put

\[
K_X(\theta)=|H_2(\theta)|^2-M.
\]

The residual is \(\mathcal R_a=\int K_X\,d\mu_{X,a}\). Since only an upper bound is required,

\[
\mathcal R_a\le \int (K_X)_+\,d\mu_{X,a}.
\]

**Proposition 4.3 (one-sided level-set criterion).** Fix \(\varepsilon>0\). It is sufficient to prove, for dyadic

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

**Proof.** Split \((K_X)_+\) at \(MX^\varepsilon\) and apply the dyadic layer-cake inequality. The low part contributes at most \(MX^\varepsilon\), and each dyadic high level contributes \(MX^{o(1)}\). The logarithmic number of levels is absorbed into \(X^{o(1)}\). \(\square\)

This is strictly weaker than the squared-kernel estimate obtained from Chebyshev and Theorem 4.2. It allows an exceptional set of reciprocal pairs of total mass about \(1/M\) to carry the maximal kernel value.

# A globally coupled Möbius detector

A natural attempt to replace the prime-supported shell by a smooth density loses the signed cancellation that distinguishes primes from resonant composites. The exact prime indicator nevertheless admits a useful growing-degree truncation.

Set

\[
H=\frac{X^2}{2},
\qquad
I_X=[H,2H),
\qquad
A_X=\prod_{p<X}p.
\tag{5.1}
\]

For \(n\in I_X\), let

\[
s_X(n)=\omega((n,A_X)).
\]

Since \(n<X^2\), a composite \(n\) coprime to \(A_X\) would have at least two prime factors not smaller than \(X\), which is impossible. Thus

\[
n\text{ prime}\quad\Longleftrightarrow\quad s_X(n)=0.
\tag{5.2}
\]

For an integer \(k\ge0\), define

\[
T_k(n)=
\sum_{\substack{d\mid(n,A_X)\\\omega(d)\le k}}\mu(d).
\tag{5.3}
\]

## Exact degree identity

**Proposition 5.1.** One has

\[
\boxed{
T_k(n)=
\begin{cases}
1,&s_X(n)=0,\\
0,&1\le s_X(n)\le k,\\
(-1)^k\binom{s_X(n)-1}{k},&s_X(n)>k.
\end{cases}}
\tag{5.4}
\]

**Proof.** If \(s=s_X(n)\), then

\[
T_k(n)=\sum_{j=0}^{\min(k,s)}(-1)^j\binom sj.
\]

For \(0<s\le k\) this is \((1-1)^s=0\); for \(s>k\) it is the standard partial alternating-binomial identity. \(\square\)

Write

\[
\mathbf1_{n\text{ prime}}=T_k(n)-R_k(n),
\qquad
R_k(n)=T_k(n)\mathbf1_{s_X(n)>k}.
\tag{5.5}
\]

## Negligible high-degree tail

**Theorem 5.2 (growing-degree truncation).** Let \(\eta>0\) and

\[
k=\left\lceil(1+\eta)\frac{\log X}{\log\log X}\right\rceil.
\tag{5.6}
\]

Then

\[
\sum_{n<2H}|R_k(n)|
\le HX^{-1-\eta+o(1)}.
\tag{5.7}
\]

Moreover, for any matrix-valued shell operator of the form

\[
\mathcal C(c)=
\sum_{n\in I_X}\gamma_n c(n)B_n,
\qquad
|\gamma_n|\ll\frac{\log H}{H},
\qquad
\|B_n\|_F\le M,
\tag{5.8}
\]

one has

\[
\boxed{
\|\mathcal C(R_k)\|_F^2
\le MX^{-2\eta+o(1)}
}
\tag{5.9}
\]

whenever \(M=X^{2+o(1)}\).

**Proof.** For \(s>k\),

\[
|T_k(n)|=\binom{s-1}{k}\le\binom{s}{k+1}.
\]

Hence

\[
\sum_{n<2H}|R_k(n)|
\le
2H\sum_{\substack{d\mid A_X\\\omega(d)=k+1}}\frac1d
\le
\frac{2H}{(k+1)!}
\left(\sum_{p<X}\frac1p\right)^{k+1}.
\]

Mertens' theorem and Stirling's formula give (5.7). The triangle inequality in (5.8) gives

\[
\|\mathcal C(R_k)\|_F
\ll
\frac{M\log H}{H}\sum_{n<2H}|R_k(n)|
\le MX^{-1-\eta+o(1)},
\]

and squaring yields (5.9). \(\square\)

The theorem removes the high-Möbius-degree tail. It does not justify estimating the retained degrees separately. In exact finite panels, splitting the retained detector by degree or divisor size produces norms tens to thousands of times larger than the recombined prime operator. The theorem boundary is therefore a *globally coupled* detector of growing degree.

# A density main-term obstruction

The previous section shows that high degree is not the obstacle. The obstacle is the cancellation among the retained signed terms. A positive Hardy--Littlewood density model fails dramatically because it assigns large mass to composite moduli that are perfectly resonant with every primorial centre.

For \(n\in I_X\), let \(w_a(n)\) be a fixed positive smooth harmonic weight and define

\[
D_\rho=
\sum_{n\in I_X}\frac1{\log n}\sum_{b\ne0}w_b(n),
\qquad
\widetilde p_{n,a}=
\frac{w_a(n)}{D_\rho\log n}.
\tag{6.1}
\]

Consider the Hardy--Littlewood density surrogate

\[
\mathcal R_a^{\mathrm{HL}}
=
\sum_{\substack{n,m\in I_X\\n\ne m}}
\widetilde p_{n,a}\widetilde p_{m,a}
\mathfrak S(m-n)
\left(
\left|H_2\!\left(a\left(\frac1n-\frac1m\right)\right)\right|^2-M
\right),
\tag{6.2}
\]

where \(\mathfrak S\) is the binary singular series.

Define

\[
\mathcal A_X=
\{pr:X/\sqrt2\le p<r<X,\ p,r\text{ prime}\}.
\tag{6.3}
\]

**Theorem 6.1 (semiprime resonance obstruction).** One has

\[
\boxed{
\mathcal R_a^{\mathrm{HL}}
\gg
\frac{M^2}{\log^4X}-MX^{o(1)}.
}
\tag{6.4}
\]

In particular, the density surrogate is polynomially larger than the required \(MX^{o(1)}\) scale.

**Proof.** Every \(n=pr\in\mathcal A_X\) lies in \([X^2/2,X^2)\) and divides \(A_X\), hence divides every centre \(P_j\). Therefore, for distinct \(n,m\in\mathcal A_X\),

\[
e(P_j/n)=e(P_j/m)=1
\]

for every \(j\), and

\[
H_2\!\left(a\left(\frac1n-\frac1m\right)\right)=M.
\]

The kernel equals \(M^2-M\). Moreover, \(m-n\) is even, so its singular series is bounded below by a positive absolute constant. The prime number theorem gives

\[
|\mathcal A_X|\asymp\frac{X^2}{\log^2X}\asymp M,
\qquad
\widetilde p_{n,a}\asymp H^{-1}
\]

on this family. Its positive contribution is therefore

\[
\gg(M^2-M)\frac{|\mathcal A_X|^2}{H^2}
\asymp\frac{M^2}{\log^4X}.
\]

The kernel is bounded below by \(-M\), and the maximum singular series is subpolynomial, so all negative terms together are \(\gg-MX^{o(1)}\). \(\square\)

Thus a decomposition

\[
\text{prime-pair measure}
=
\text{positive density main term}
+
\text{small error}
\]

cannot prove the centred reciprocal estimate. The error would need to cancel a polynomially large resonant-composite contribution. The prime detector must remain signed until after the reciprocal kernel is formed.
