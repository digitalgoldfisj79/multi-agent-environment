# Multiplicative Fourier anatomy

A squarefree additive modulus can be factorised by the Chinese remainder theorem, and additive phases can be expanded in multiplicative characters. This suggests a possible route to independent local averages. The exact character algebra shows why that route fails in the load-bearing sector.

Let

\[
m=\prod_{s=1}^tq_s
\]

be squarefree, and assume every \(P_j\) is a unit modulo \(m\). For a unit \(A\pmod m\), define

\[
F_m(A)=\sum_{j<N}e_m(AP_j),
\qquad
S_m(\chi)=\sum_{j<N}\chi(P_j),
\tag{7.1}
\]

where \(e_m(x)=e(x/m)\). With

\[
\tau_m(\overline\chi)
=
\sum_{u\in(\mathbb Z/m\mathbb Z)^\times}
\overline\chi(u)e_m(u),
\]

multiplicative Fourier inversion gives

\[
F_m(A)=
\frac1{\varphi(m)}
\sum_{\chi\bmod m}
\tau_m(\overline\chi)\chi(A)S_m(\chi).
\tag{7.2}
\]

## The character diagonal

Write

\[
|F_m(A)|^2=\mathfrak D_m+\mathfrak O_m(A),
\]

where \(\mathfrak D_m\) is the equal-character part.

For a unit \(z\pmod m\), define

\[
K_m(z)=
\prod_{q\mid m}
\frac{q\mathbf1_{z\equiv1\, (q)}-1}{q-1}.
\tag{7.3}
\]

**Theorem 7.1 (exact character diagonal).** One has

\[
\boxed{
\mathfrak D_m
=
\sum_{i,j<N}K_m(P_iP_j^{-1}).
}
\tag{7.4}
\]

In particular, \(\mathfrak D_m\) is independent of \(A\). If no off-diagonal pair \(P_i,P_j\) collides modulo any prime factor of \(m\), then for even \(t\),

\[
\mathfrak D_m
=
N+\frac{N(N-1)}{\varphi(m)}.
\tag{7.5}
\]

**Proof.** For one prime \(q\), the principal Gauss sum has squared magnitude one and every nonprincipal Gauss sum has squared magnitude \(q\). Hence

\[
\frac1{(q-1)^2}
\sum_{\chi\bmod q}
|\tau_q(\overline\chi)|^2\chi(z)
=
\frac{q\mathbf1_{z=1}-1}{q-1}.
\]

The character group and the squared Gauss weights factor over the CRT. Summing over \(i,j\) proves (7.4). \(\square\)

The diagonal is close to \(N\) for a product of four large shell primes. It is not the source of the large fluctuations.

## Character-ratio collapse

**Theorem 7.2 (local ratio identity).** Let \(q\) be prime, let \(a,x,y\) be nonzero modulo \(q\), and let \(\rho\) be a multiplicative character. For each character \(\chi\), put \(\psi=\chi\overline\rho\). Then

\[
\boxed{
\frac1{(q-1)^2}
\sum_{\chi\bmod q}
\tau_q(\overline\chi)
\overline{\tau_q(\overline\psi)}
\chi(ax)\overline{\psi(ay)}
=
\begin{cases}
\mathbf1_{\rho=1},&x=y,\\[4pt]
\dfrac{\tau_q(\overline\rho)}{q-1}\rho(a(x-y)),&x\ne y.
\end{cases}}
\tag{7.6}
\]

Summing (7.6) over \(\rho\) reconstructs exactly

\[
e_q(a(x-y)).
\tag{7.7}
\]

**Proof.** Expand the two Gauss sums and sum first over \(\chi\). Character orthogonality forces \(xv\equiv yu\pmod q\). If \(x\ne y\), substitute \(v=yu/x\); the remaining sum is the Gauss sum of \(\rho\) evaluated at \(a(x-y)\). If \(x=y\), only the principal ratio character survives. The final sum over \(\rho\) is multiplicative Fourier inversion. \(\square\)

**Corollary 7.3 (CRT de-tensorisation no-go).** Let \(m=q_1q_2q_3q_4\) and choose two positive and two negative CRT signs. Applying Theorem 7.2 at the four prime factors to the unequal-character sector of \(|F_m(A)|^2\) reconstructs

\[
e_m(A(P_i-P_j))
\]

exactly. It does not produce four independent modulus averages.

The divisor conditions

\[
q_s\mid P_i-P_j
\quad\Longleftrightarrow\quad
q_s\mid P_j/P_i-1
\]

occur in the zero branches and in the character diagonal. They control a sparse correction sector. The unit branches retain the Gauss-weighted character sums and return the original additive reciprocal phase. This is an exact algebraic closure, not a limitation of a particular inequality.

# A density-one certificate and its spectral obstruction

The direct block criterion of Theorem 2.4 aims at every centre. One may ask whether averaging over the primorial index could first yield a density-one theorem. There is a clean positive certificate, but the expected new zero average is absent.

## Failure forces cubic local energy

Let

\[
y_n=p_{n+1}^2-2,
\qquad
h_n=y_n/2,
\]

and define

\[
J_n=
\int_{P_n+1}^{P_n+1+y_n/4}
\left|
\psi(x+h_n)-\psi(x)-h_n
\right|^2\,dx.
\tag{8.1}
\]

**Theorem 8.1 (Fortune-failure certificate).** For all sufficiently large \(n\),

\[
\boxed{
F_n\text{ composite}
\quad\Longrightarrow\quad
J_n\ge\frac{y_n^3}{64}.
}
\tag{8.2}
\]

Consequently,

\[
\boxed{
\left|\{n\le N:F_n\text{ composite}\}\right|
\le
64\sum_{n\le N}\frac{J_n}{y_n^3}+O(1).
}
\tag{8.3}
\]

**Proof.** If \(F_n\) is composite, then there is no prime at any offset \(2\le m<p_{n+1}^2\). For every \(x\) in the integration range, \((x,x+h_n]\) lies inside that failed interval. Its von Mangoldt mass comes only from proper prime powers. As in Lemma 2.3, their total weight is \(O(\log P_n\log\log P_n)=o(h_n)\), uniformly in \(x\). Thus the absolute error is at least \(h_n/2\) throughout an interval of length \(y_n/4\), giving (8.2). Summing the resulting indicator inequality gives (8.3). \(\square\)

A bound

\[
\sum_{n\le N}\frac{J_n}{y_n^3}=o(N)
\tag{8.4}
\]

would prove Fortune for a density-one set of indices.

## Critical-scale coherence

Let

\[
L_n=\log P_n=\vartheta(p_n),
\qquad
\mathcal Z_N(t)=\sum_{n\le N}e^{itL_n}.
\tag{8.5}
\]

**Theorem 8.2 (primorial-centre coherence).** For every fixed real \(c\),

\[
\boxed{
\frac1N\sum_{n\le N}
\exp\left(ic\frac{L_n}{L_N}\right)
\longrightarrow
\int_0^1e^{icu}\,du
=
\begin{cases}
1,&c=0,\\[3pt]
\dfrac{e^{ic}-1}{ic},&c\ne0.
\end{cases}}
\tag{8.6}
\]

**Proof.** The prime number theorem and the asymptotic for the \(n\)-th prime imply

\[
\frac{L_{\lfloor uN\rfloor}}{L_N}\longrightarrow u
\]

for fixed \(0<u\le1\). The sum is a Riemann sum; the first \(o(N)\) indices are negligible. \(\square\)

At frequency \(t=c/L_N\), the sum is generically of order \(N\), not \(N^{1/2}\). Normalised differences of zeta-zero ordinates have precisely this scale in explicit-formula variance calculations [@goldston-montgomery1987; @chan2003]. The primorial-index average is therefore coherent at the point where pair-correlation cancellation would be needed.

## Conductor migration

For the interval in Theorem 8.1, the natural explicit-formula cutoff is

\[
T_n=\frac{P_n}{p_{n+1}^2-2}.
\tag{8.7}
\]

**Theorem 8.3 (conductor migration).** One has

\[
\boxed{
\frac{T_{n+1}}{T_n}
=
\frac{p_{n+1}(p_{n+1}^2-2)}{p_{n+2}^2-2}
\sim p_{n+1}
\longrightarrow\infty.
}
\tag{8.8}
\]

Consequently, for every fixed \(A>1\), the bands \([T_n/A,AT_n]\) are pairwise disjoint for all sufficiently large \(n\).

**Proof.** Substitute \(P_{n+1}=p_{n+1}P_n\) and use \(p_{n+2}/p_{n+1}\to1\). \(\square\)

Thus the dominant high-zero range is not sampled repeatedly across a long block of primorial indices. A density-one proof through the explicit formula would require a bespoke sparse-centre, moving-conductor theorem, not a direct transfer of continuous Selberg-integral or pair-correlation results.

# Harmonic scale conservation

The exact aggregate reduction in Proposition 3.1 raises the possibility of manufacturing a long average over the numerator harmonic \(a\). At the critical shell this possibility is illusory for structural reasons.

## Shortening and translation

For an interval of length \(h\), its additive transform modulo \(q\) occupies approximately \(q/h\) frequencies. To obtain \(A\) effective harmonics while keeping \(q\asymp H\), one might shorten the physical window to \(h=H/A\) and cover the original interval by \(A\) translates.

**Proposition 9.1 (Fourier-scale conservation).** Assume \(H=Ah\) with integers \(A,h\). For every \(q\) and \(a\),

\[
\boxed{
\sum_{b=0}^{A-1}
\sum_{m=bh}^{(b+1)h-1}e(am/q)
=
\sum_{m=0}^{H-1}e(am/q).
}
\tag{9.1}
\]

Thus the broad transform of one short window, multiplied by the translation sum, reconstructs the original length-\(H\) transform exactly.

The identity is tautological, but its consequence is important. Summing the translates with their phases returns the original bounded-harmonic kernel. Bounding the translates separately pays an \(A\)-fold Cauchy or triangle loss and cancels the apparent frequency gain.

One may instead move to a larger modulus shell \(Q=BH\), which gives \(B\) effective harmonics. The natural low-frequency shell scale is then \(Q/\log Q\), not \(H/\log H\); polynomially growing \(B\) introduces a polynomial loss and squares the pair conductor. Moreover, the exact prime-detection decomposition still contains the mandatory shell \(Q\asymp H\). A larger shell is additional, not a replacement.

## Large values do not force narrow alignment

The level-set criterion in Proposition 4.3 suggests attacking only very large values. Put

\[
K_X(\theta)=|H_2(\theta)|^2-M.
\]

If

\[
K_X(\theta)\ge M^{2-\delta},
\]

then, using \(2|H_2|\le |F|^2+N\) and \(M\asymp N^2\),

\[
|F(\theta)|\gg N^{1-\delta/2}.
\tag{9.2}
\]

This is large relative to \(\sqrt N\), but the normalised resultant tends to zero.

**Lemma 9.2 (projection bound).** Let \(z_1,\ldots,z_N\) be unit complex numbers and suppose

\[
\left|\sum_{j=1}^Nz_j\right|=\mu N.
\]

For every \(0<\tau<\mu\), at least

\[
\frac{(\mu-\tau)N}{1-\tau}
\tag{9.3}
\]

of the phases have projection at least \(\tau\) in the direction of the resultant.

**Proof.** Rotate so that the resultant is positive real. If \(K\) phases have real part at least \(\tau\), then the total real part is at most \(K+(N-K)\tau\). Comparing with \(\mu N\) proves the claim. \(\square\)

Taking \(\tau=\mu/2\) in the regime (9.2) guarantees only \(\asymp N^{1-\delta/2}\) phases in an arc of half-width \(\arccos(\mu/2)=\pi/2-o(1)\). This is a diffuse bias, not a narrow modular-arc certificate.

Even if two narrow constraints

\[
\|\theta L_i\|\le\varepsilon,
\qquad
\theta=\frac{a(r-q)}{qr}
\]

were available, eliminating \(a(r-q)\) yields integers \(n_i\) satisfying

\[
|n_1L_2-n_2L_1|
\le
\varepsilon(|L_1|+|L_2|).
\tag{9.4}
\]

The \(L_i\) are primorial-sized. For (9.4) to force an exact integer relation, \(\varepsilon\) must be exponentially small in \(X\). A power-scale large-value estimate gives no such precision. Consequently, large amplitude alone cannot produce the divisor pinning required by a finite determinant argument.
