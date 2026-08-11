---
title: "Pair-Sum Rigidity for Superincreasing Sequences"
subtitle: "Difference multiplicities, sub-Weibull tails, and a primorial-centre covariance application"
author: "Bozzard, Edward Stewart Anthony (ORCID 0009-0002-4052-0994)"
date: "11 August 2026"
lang: en-GB
bibliography: references.bib
---

**Abstract.** Let \(P_0,\ldots,P_{N-1}\) be a positive superincreasing sequence satisfying \(P_{j+1}\ge X P_j\), and form the pair-sum set \(S_{\{j,k\}}=P_j+P_k\). We prove a rigidity theorem for bounded integer relations and use it to classify every represented nonzero difference of pair sums: the only repeated differences are the single-walk differences \(P_i-P_k\), each occurring with multiplicity exactly \(N\); every other represented difference occurs once. This gives an exact two-scale energy decomposition. The same rigidity principle yields high-moment bounds for the pair-sum exponential sum and, when the sequence length is below the rigidity scale, a sub-Weibull Lebesgue tail for its centred squared modulus.

We then separate this Lebesgue theory from a sparse reciprocal sampling problem and quantify the transfer gap: failure of the desired reciprocal level-set estimate requires polynomially many arithmetic sampling atoms to concentrate on a set of exponentially small Lebesgue measure. Finally, we specialise to consecutive primorial centres. Below the next-prime square threshold, every prime-producing offset is itself prime, so the correct existence variable is a two-prime count. We prove the deterministic variance-to-no-failure implication and expand its second moment exactly into an aggregated four-prime correlation. The Hardy--Littlewood mean used to calibrate this final application is conjectural. No arithmetic sampling theorem, four-prime covariance estimate, or proof of Fortune's conjecture is claimed.

**Keywords:** superincreasing sequences; pair-sum sets; additive energy; exponential sums; sub-Weibull tails; prime pairs; Fortunate numbers.

**MSC 2020:** 11B30, 11B83, 11L07, 11N05, 11N13.

# 1. Introduction and setting

A rapidly growing additive basis has a simple but powerful rigidity property: a bounded integer relation cannot cancel its largest term. For pair sums this turns an apparently large additive-energy problem into two exactly separated multiplicity scales. The purpose of this paper is to develop that structure intrinsically, before considering any arithmetic sampling measure or prime-detection application.

Let
\[
0<P_0<P_1<\cdots<P_{N-1},
\qquad
P_{j+1}\ge X P_j
\tag{1.1}
\]
for a real parameter \(X>1\). Let
\[
\mathcal P_2=\{\{j,k\}:0\le j\le k<N\},
\qquad
M=|\mathcal P_2|=\frac{N(N+1)}2,
\]
where index pairs are multisets, and put
\[
S_{\{j,k\}}=P_j+P_k.
\tag{1.2}
\]
Define
\[
H_2(\theta)=\sum_{u\in\mathcal P_2}e(\theta S_u),
\qquad
e(t)=e^{2\pi i t},
\qquad
K(\theta)=|H_2(\theta)|^2-M.
\tag{1.3}
\]

The structural results through Section 5 need only the ratio condition (1.1). The full-range tail theorem in Section 6 also needs the sequence length to remain below the available rigidity order; the sufficient condition \(X>N+2\) is convenient and is automatic for the primorial block application, where \(N\asymp X/\log X\).

The principal results are these. Theorem 3.2 gives the exact difference-multiplicity dichotomy. Corollary 4.1 turns it into a two-scale decomposition for every nonnegative difference kernel. Lemma 5.1 and Theorem 6.1 give high moments and sub-Weibull Lebesgue tails. Section 8 then shows why such Lebesgue control is not itself an arithmetic sampling theorem. Sections 9--10 specialise the framework to prime-pair detection at primorial centres and isolate an aggregated four-prime covariance problem.

The paper uses three epistemic classes. Labelled theorems, lemmas, propositions and corollaries are proved in the text. The exact sixth- and centred third-moment formulae in Section 7 are finite combinatorial identities independently checked by exhaustive enumeration and are not used as proof inputs later. The Hardy--Littlewood prime-pair formula in Section 9 is a conjectural calibration, not a proved mean theorem.

# 2. Bounded-coefficient rigidity

**Lemma 2.1 (bounded-coefficient rigidity).** Let \(B\ge1\) be an integer and suppose \(X>B+1\). If integers \(c_0,\ldots,c_{N-1}\) satisfy
\[
|c_t|\le B,
\qquad
\sum_{t<N}c_tP_t=0,
\tag{2.1}
\]
then every \(c_t=0\).

**Proof.** Suppose otherwise and let \(t\) be the largest index with \(c_t\ne0\). From (1.1),
\[
\sum_{i<t}P_i
\le P_{t-1}\sum_{s\ge0}X^{-s}
=P_{t-1}\frac{X}{X-1}
\le\frac{P_t}{X-1}.
\]
Therefore
\[
\left|\sum_{i<t}c_iP_i\right|
\le\frac{B}{X-1}P_t
<P_t
\le |c_t|P_t,
\]
contradicting (2.1). \(\square\)

The value of keeping \(B\) general is that a single lemma controls both difference multiplicities and moments of growing order.

# 3. Difference multiplicities

For a nonzero integer \(D\), define
\[
r(D)=\#\{(u,v)\in\mathcal P_2^2:u\ne v,\ S_u-S_v=D\}.
\tag{3.1}
\]

**Lemma 3.1 (linkage of representations).** Assume \(X>5\). If
\[
S_u-S_v=S_{u'}-S_{v'},
\]
then
\[
u\uplus v'=u'\uplus v
\tag{3.2}
\]
as multisets of four endpoint indices.

**Proof.** Rearranging gives \(S_u+S_{v'}=S_{u'}+S_v\). The coefficient of each \(P_t\) is the multiplicity of \(t\) in \(u\uplus v'\) minus its multiplicity in \(u'\uplus v\), and therefore has absolute value at most four. Lemma 2.1 with \(B=4\) forces every coefficient to vanish. \(\square\)

**Theorem 3.2 (difference-multiplicity dichotomy).** Assume \(X>5\). For every nonzero integer \(D\):

1. if \(D=P_i-P_k\) for some \(i\ne k\), then \(r(D)=N\), and its representations are exactly
   \[
   (u,v)=\bigl(\{i,t\},\{k,t\}\bigr),
   \qquad 0\le t<N;
   \tag{3.3}
   \]
2. otherwise \(r(D)\le1\).

The values \(P_i-P_k\) with \(i\ne k\) are pairwise distinct. Hence there are exactly \(N(N-1)\) multiplicity-\(N\) differences, accounting for \(N^2(N-1)\) ordered pairs \((u,v)\), and every remaining represented nonzero difference has multiplicity one.

**Proof.** For \(D=P_i-P_k\), each pair in (3.3) is a representation, so \(r(D)\ge N\). Conversely, compare an arbitrary representation \((u',v')\) with the member \((\{i,i\},\{k,i\})\) of (3.3). Lemma 3.1 gives
\[
\{i,i\}\uplus v'=u'\uplus\{k,i\}.
\tag{3.4}
\]
Since \(k\ne i\), the occurrence of \(k\) on the right must be supplied by \(v'\) on the left. Thus \(v'=\{k,t\}\) for some \(t\); cancelling the common endpoint multiplicities then gives \(u'=\{i,t\}\). These are exactly the \(N\) representations in (3.3).

Now suppose \(D\) is not of the form \(P_i-P_k\) and that \((u,v)\) represents it. Then \(u\) and \(v\) cannot share an endpoint: if \(u=\{i,t\}\) and \(v=\{k,t\}\), then \(D=P_i-P_k\). Hence \(u\cap v=\varnothing\) as multisets. If \((u',v')\) is a second representation, Lemma 3.1 gives \(u\uplus v'=u'\uplus v\). Because no endpoint of \(v\) occurs in \(u\), both endpoints of \(v\), with multiplicity, must be supplied by the two-element multiset \(v'\). Thus \(v'=v\), and then \(u'=u\). Hence \(r(D)\le1\).

Finally, an equality \(P_i-P_k=P_{i'}-P_{k'}\) is a bounded integer relation with coefficients of absolute value at most two. Lemma 2.1 implies equality of the ordered endpoint pairs, so the \(N(N-1)\) single-walk differences are distinct. The pair count follows because \(|\mathcal P_2|=M\). \(\square\)

The distinction \(r(D)\le1\), rather than \(r(D)=1\), is essential: integers not represented as pair-sum differences have multiplicity zero.

# 4. Exact two-scale energy

Let \(\mathcal D_1\) denote the set of represented nonzero differences of multiplicity one.

**Corollary 4.1 (exact two-scale decomposition).** For any function \(T\) on the nonzero integers,
\[
\boxed{
\sum_{\substack{u,v\in\mathcal P_2\\u\ne v}}T(S_u-S_v)
=
N\sum_{i\ne k}T(P_i-P_k)
+
\sum_{D\in\mathcal D_1}T(D).
}
\tag{4.1}
\]
Moreover
\[
|\mathcal D_1|=M(M-1)-N^2(N-1).
\tag{4.2}
\]
If \(T\ge0\) and
\[
\mathcal E(T)=\sum_{u\ne v}T(S_u-S_v),
\qquad
\mathcal G(T)=\sum_{i\ne k}T(P_i-P_k),
\]
then
\[
\mathcal E(T)=N\mathcal G(T)+\mathcal S(T),
\qquad \mathcal S(T)\ge0,
\tag{4.3}
\]
and consequently
\[
\mathcal E(T)\le M X^{o(1)}
\quad\Longrightarrow\quad
\mathcal G(T)\le \frac{M}{N}X^{o(1)}\ll N X^{o(1)}.
\tag{4.4}
\]

**Proof.** Group the left side of (4.1) by the represented value \(D=S_u-S_v\) and apply Theorem 3.2. There are \(N(N-1)\) multiplicity-\(N\) values and hence \(N^2(N-1)\) ordered pairs of the first type; subtracting these from the total \(M(M-1)\) ordered pairs gives (4.2). Equations (4.3)--(4.4) follow immediately when \(T\ge0\). \(\square\)

Thus there is no intermediate multiplicity scale: any positive pair-sum energy estimate automatically contains a single-walk energy problem at scale \(M/N\), plus a multiplicity-free remainder at scale \(M\).

# 5. High moments of the pair-sum polynomial

**Lemma 5.1 (moment bound).** Let \(k\ge1\) and assume \(X>2k+1\). Then
\[
\boxed{
\int_0^1|H_2(\theta)|^{2k}\,d\theta
\le \frac{(2k)!}{2^k}M^k.
}
\tag{5.1}
\]

**Proof.** By orthogonality, the integral counts tuples
\((u_1,\ldots,u_k,v_1,\ldots,v_k)\in\mathcal P_2^{2k}\) satisfying
\[
\sum_{i=1}^kS_{u_i}=\sum_{i=1}^kS_{v_i}.
\]
The resulting relation among the \(P_t\) has coefficients bounded by \(2k\). Lemma 2.1 therefore forces equality of the total endpoint multisets
\[
u_1\uplus\cdots\uplus u_k
=v_1\uplus\cdots\uplus v_k=:W.
\tag{5.2}
\]
There are \(M^k\) choices of the first ordered \(k\)-tuple. For a fixed endpoint multiset \(W\) of size \(2k\), temporarily distinguish its repeated occurrences by labels. A labelled \(2k\)-set has \((2k-1)!!\) pair partitions and \(k!\) orders of those pairs, hence
\[
(2k-1)!!\,k!=\frac{(2k)!}{2^k}
\]
ordered decompositions into unordered pairs. Every unlabelled decomposition has at least one labelled lift, and distinct unlabelled decompositions have disjoint sets of lifts. Thus the number of possible second \(k\)-tuples is at most \((2k)!/2^k\). \(\square\)

# 6. Sub-Weibull Lebesgue tails

**Theorem 6.1 (sub-Weibull tail).** Assume \(X>N+2\). For every real \(s\ge2M\),
\[
\operatorname{meas}\{\theta\in[0,1):|H_2(\theta)|^2\ge s\}
\le
e^3\left(\frac{2s}{M}\right)^{1/4}
\exp\left(-\sqrt{\frac{2s}{M}}\right).
\tag{6.1}
\]
In particular, for \(121M\le\lambda\le M^2\),
\[
\boxed{
\operatorname{meas}\{\theta:K(\theta)\ge\lambda\}
\le\exp\left(-\sqrt{\lambda/M}\right).
}
\tag{6.2}
\]

**Proof.** For \(s>M^2\) the level set is empty, so suppose \(2M\le s\le M^2\) and choose
\[
k=\left\lfloor\sqrt{\frac{s}{2M}}\right\rfloor\ge1.
\]
Since \(2k+1\le \sqrt{2M}+1<N+2<X\), Lemma 5.1 applies. Markov's inequality gives
\[
\operatorname{meas}\{|H_2|^2\ge s\}
\le
\frac{(2k)!}{2^k}\left(\frac{M}{s}\right)^k.
\]
Using the elementary Stirling bound \((2k)!\le e(2k)^{2k+1/2}e^{-2k}\),
\[
\frac{(2k)!}{2^k}\left(\frac{M}{s}\right)^k
\le e\sqrt{2k}\left(\frac{2k^2M}{e^2s}\right)^k
\le e\sqrt{2k}\,e^{-2k}.
\]
The choice of \(k\) gives \(2k\ge\sqrt{2s/M}-2\), which yields (6.1).

For (6.2), put \(s=M+\lambda\) and \(t=\lambda/M\ge121\). After taking logarithms it is enough to verify
\[
3+\frac14\log(2(t+1))-\sqrt{2(t+1)}+\sqrt t\le0.
\]
The left side is negative at \(t=121\) and decreasing thereafter, giving (6.2). \(\square\)

The theorem is a statement about Lebesgue measure on the circle. It does not imply that an arithmetically defined sparse sampling set is equidistributed across these level sets.

# 7. Higher-moment identities and limiting scale

The rigidity argument also implies that, for each fixed \(k\), \(\int_0^1|H_2|^{2k}\) is a polynomial in \(N\) once \(X>2k+1\). The leading term comes from endpoint multisets with \(2k\) distinct labels: there are \(\binom N{2k}\) such multisets and \((2k)!/2^k\) ordered decompositions into \(k\) unordered pairs. Consequently
\[
\int_0^1|H_2(\theta)|^{2k}\,d\theta
=
\frac{(2k)!}{4^k}N^{2k}\bigl(1+O_k(N^{-1})\bigr).
\tag{7.1}
\]

A complete endpoint-partition census gives the exact sixth moment
\[
\int_0^1|H_2|^6\,d\theta
=
\frac{45N^6-189N^5+438N^4-597N^3+443N^2-136N}{4},
\tag{7.2}
\]
and, after centring,
\[
\int_0^1K(\theta)^3\,d\theta
=
\frac{N(N-1)^2(37N^3-115N^2+174N-136)}4
=
74M^3\bigl(1+O(N^{-1})\bigr).
\tag{7.3}
\]
These two exact polynomial identities have been independently reproduced by exhaustive finite enumeration at more values of \(N\) than are required to determine the corresponding polynomials. They are included as exact combinatorial evidence and are not used in the proof of the arithmetic application below.

The leading moments in (7.1) coincide with those of \(g^2/\sqrt2\), where \(g\) is standard complex Gaussian. This explains the \(\sqrt{\lambda/M}\) scale in Theorem 6.1, but no uniform moderate-deviation limit is claimed.

# 8. Sparse reciprocal sampling and the transfer gap

To make the distinction between Lebesgue measure and arithmetic sampling explicit, now specialise the growth parameter to a large \(X\), set \(H\asymp X^2\), and let \(\mathcal Q_X\) be the primes in \([H,2H)\). Fix a nonnegative even Schwartz function \(\rho\), and for a fixed nonzero integer harmonic \(a\) define
\[
w_{q,a}=\rho(Ha/q),
\qquad
D_X=\sum_{q\in\mathcal Q_X}\sum_{b\ne0}\rho(Hb/q),
\qquad
p_{q,a}=\frac{w_{q,a}}{D_X}.
\tag{8.1}
\]
Let \(\mu_{X,a}\) be the finite positive measure placing mass \(p_{q,a}p_{r,a}\) at
\[
\theta_{q,r}=a\left(\frac1q-\frac1r\right)\pmod1,
\qquad q,r\in\mathcal Q_X,
\quad q\ne r.
\tag{8.2}
\]
For fixed \(a\) in the effective support of \(\rho\), the prime number theorem gives at most \(X^{4+o(1)}\) atoms and individual masses at most \(X^{-4+o(1)}\).

A natural one-sided reciprocal level-set target is
\[
\mu_{X,a}\{K\ge\lambda\}
\ll\frac{M X^{o(1)}}{\lambda},
\qquad 121M\le\lambda\le M^2.
\tag{8.3}
\]

**Corollary 8.1 (quantified transfer gap).** If (8.3) fails at \(\lambda=tM\), \(121\le t\le M\), then at least
\[
X^{4+o(1)}t^{-1}
\tag{8.4}
\]
sampling atoms lie in a set of Lebesgue measure at most
\[
\exp(-\sqrt t).
\tag{8.5}
\]

**Proof.** Theorem 6.1 bounds the Lebesgue measure of the level set by (8.5). Failure of (8.3) means the sampling mass of that level set exceeds \(t^{-1}X^{o(1)}\). Since each atom has mass at most \(X^{-4+o(1)}\), at least (8.4) atoms are required. \(\square\)

Thus the missing statement is not an improvement of the Lebesgue tail. It is an arithmetic non-concentration theorem preventing polynomially many reciprocal atoms from accumulating on exponentially small high-value sets. Nothing in Sections 2--7 supplies such a theorem.

# 9. Primorial-centre prime-pair application

We now specialise the superincreasing sequence to consecutive primorial centres and derive the application from first principles. Let
\[
A_X=\prod_{p<X}p,
\qquad
X\le\ell_1<\ell_2<\cdots<\ell_N<2X
\]
be the primes of a dyadic block, define
\[
Q_0=1,
\qquad
Q_j=\prod_{u=1}^j\ell_u,
\qquad
P_j=A_XQ_j,
\tag{9.1}
\]
and fix \(0<\eta<1\) with
\[
H=\eta X^2.
\tag{9.2}
\]
Then \(N\asymp X/\log X\), \(P_{j+1}\ge XP_j\), and for sufficiently large \(X\), \(H<\ell_{j+1}^2\) throughout the interior of the block.

Recall that the \(n\)-th Fortunate number is the least \(F_n>1\) for which \(p_n\# +F_n\) is prime [@guy2004]. Every prime divisor of \(F_n\) exceeds \(p_n\), so a composite \(F_n\) satisfies \(F_n\ge p_{n+1}^2\). Thus a prime within the next-prime square window forces the corresponding Fortunate number to be prime.

**Lemma 9.1 (candidate collapse).** Suppose
\[
1<m<\ell_{j+1}^2,
\qquad
(m,P_j)=1.
\]
Then \(m\) is prime. In particular, if \(P_j+m\) is prime with \(1<m<H\), then \(m\) is prime.

**Proof.** Every prime divisor of \(m\) is coprime to \(P_j\), hence exceeds \(\ell_j\) and is at least \(\ell_{j+1}\). If \(m\) were composite, it would have at least two prime factors counted with multiplicity and therefore \(m\ge\ell_{j+1}^2\), a contradiction. If \(P_j+m\) is prime then \((m,P_j)=1\), because a common prime divisor would also divide the prime output. \(\square\)

Define the exact two-prime existence count
\[
Z_j(H)=\sum_{2\le m\le H}
\mathbf1_{\mathbb P}(m)
\mathbf1_{\mathbb P}(P_j+m).
\tag{9.3}
\]
By Lemma 9.1, \(Z_j(H)>0\) exactly when the interval \([P_j+2,P_j+H]\) contains a prime.

For calibration, the Hardy--Littlewood prime-pair heuristic [@hardy-littlewood1923] suggests
\[
\lambda_j(H)=
\mathfrak S(P_j)
\int_{\ell_j}^{H}
\frac{dt}{\log t\,\log(P_j+t)},
\qquad
\mathfrak S(P_j)=2C_2\prod_{2<p\le\ell_j}\frac{p-1}{p-2},
\tag{9.4}
\]
which is of order \(X\) in the block. Equation (9.4) is a conjectural baseline only.

**Theorem 9.2 (all-centres variance criterion).** Let deterministic baselines \(\lambda_j\) satisfy
\[
cX\le\lambda_j\le CX
\tag{9.5}
\]
for fixed \(c,C>0\). If
\[
\sum_{j<N}|Z_j(H)-\lambda_j|^2
\ll NXL(X),
\qquad
L(X)=o(\log X),
\tag{9.6}
\]
then every centre in the block succeeds for all sufficiently large \(X\), and the corresponding Fortunate numbers are prime.

**Proof.** Let \(B_X\) be the number of failed centres. At each failure \(Z_j=0\), so
\[
B_Xc^2X^2
\le\sum_{j<N}|Z_j-\lambda_j|^2
\ll NXL(X).
\]
Since \(N\asymp X/\log X\),
\[
B_X\ll\frac{L(X)}{\log X}=o(1).
\]
The integer \(B_X\) is therefore eventually zero. Lemma 9.1 and the Fortunate-number square threshold give the final implication. \(\square\)

Theorem 9.2 is deterministic. It does not prove that baselines of size \(X\) satisfy (9.6), nor does it prove the Hardy--Littlewood calibration (9.4).

# 10. Exact covariance expansion and open arithmetic boundary

**Proposition 10.1 (four-prime second-moment expansion).** For \(1\le d<H\), define
\[
C_j(H;d)=
\sum_{\substack{2\le m\\m+d\le H}}
\mathbf1_{\mathbb P}(m)
\mathbf1_{\mathbb P}(m+d)
\mathbf1_{\mathbb P}(P_j+m)
\mathbf1_{\mathbb P}(P_j+m+d).
\tag{10.1}
\]
Then exactly
\[
\boxed{
Z_j(H)^2
=Z_j(H)+2\sum_{1\le d<H}C_j(H;d).
}
\tag{10.2}
\]

**Proof.** Expanding \(Z_j^2\) gives ordered pairs \((m,n)\) of successful offsets. The diagonal \(m=n\) contributes \(Z_j\). Every off-diagonal pair occurs uniquely as \((m,m+d)\) or \((m+d,m)\) for some \(d\ge1\), and the two orders contribute the same four prime indicators. \(\square\)

This identifies the unweighted second moment as an aggregated four-linear-form prime correlation. The variance theorem does not require a uniform asymptotic for every displacement \(d\); the required information can remain aggregated.

For example, the following two block estimates would be sufficient:
\[
\sum_{j<N}\lambda_jZ_j
=
\sum_{j<N}\lambda_j^2+O(NXL(X)),
\tag{10.3}
\]
and
\[
\sum_{j<N}\left(Z_j+2\sum_{d<H}C_j(H;d)\right)
=
\sum_{j<N}(\lambda_j^2+\lambda_j)+O(NXL(X)).
\tag{10.4}
\]
Indeed, (10.2)--(10.4) give
\[
\sum_{j<N}|Z_j-\lambda_j|^2
=
\sum_{j<N}\lambda_j+O(NXL(X))
\ll NXL(X)
\tag{10.5}
\]
for \(L(X)\ge1\). If \(L(X)=o(\log X)\), Theorem 9.2 then excludes every failure.

The open analytic problem is therefore to prove an estimate such as (9.6), or equivalently sufficient signed aggregate information such as (10.3)--(10.4), while retaining all four primality conditions until after centring. The sub-Weibull Lebesgue theorem does not supply this arithmetic covariance estimate, and Corollary 8.1 quantifies the non-concentration statement that would be needed to transfer one particular reciprocal model.

No such arithmetic non-concentration theorem, four-prime covariance estimate, or equivalent signed transference theorem is proved here.

# 11. Computational validation and evidence boundary

The proofs of Lemmas 2.1, 3.1 and 5.1, Theorem 3.2, Corollary 4.1, Theorem 6.1, Corollary 8.1, Lemma 9.1, Theorem 9.2 and Proposition 10.1 are analytic/combinatorial arguments in the manuscript. Finite computation is not needed for their logical validity.

The accompanying validator performs independent finite checks of the kernel theory:

- at \(N=8,9\), the difference-multiplicity histogram is exactly
  \[
  \{1:M(M-1)-N^2(N-1),\;N:N(N-1)\};
  \]
- exact moment counts for \(k=2,3,4\) and \(N\le9\) satisfy Lemma 5.1;
- the polynomial identities (7.2)--(7.3) reproduce exhaustive counts at held-out values of \(N\);
- sampled modular phases at \(N=24\) are diagnostic checks of the tail scale only and are not proof inputs.

The finite checks do not establish an asymptotic sampling theorem or a prime-pair result. Their role is reproducibility and error detection.

# 12. Conclusion

For pair sums of a superincreasing sequence, additive collisions are completely rigid at the represented-difference level: one family of differences has multiplicity \(N\), and every other represented difference has multiplicity one. This yields an exact single-walk-plus-Sidon decomposition and a transparent moment theory. Under the natural length condition, the resulting exponential sum has a sub-Weibull Lebesgue tail.

The arithmetic difficulty begins only when Lebesgue measure is replaced by a sparse reciprocal measure. The transfer-gap corollary makes the missing non-concentration quantitative but does not prove it. In the primorial specialisation, candidate collapse independently shows that the actual existence problem is a prime-pair problem. Its second moment is an aggregated four-prime correlation, and a variance estimate with loss \(o(\log X)\) would exclude every failed centre.

These statements are deliberately separated. The superincreasing kernel theorems are unconditional; the Hardy--Littlewood baseline is conjectural; the required arithmetic covariance/non-concentration theorem is open. Fortune's conjecture is not proved.

# AI-assistance disclosure

Large language models were used for literature triage, symbolic and computational cross-checking, adversarial review, software drafting, and editorial assembly. The standalone rebuild also used the fuller frozen appendix of the source manuscript to remove duplicated statements and repair a main-text multiplicity overstatement. The named author takes responsibility for the mathematical content, citations, code and final presentation.

# References

::: {#refs}
:::
