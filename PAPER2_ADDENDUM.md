# Addendum to *Prime Detection at Primorial Centres*: the difference-multiplicity dichotomy and sub-Weibull Lebesgue tails for the pair-sum kernel

**Date:** 20 July 2026.
**Relation to Paper II:** notation and numbering references follow
*Prime Detection at Primorial Centres* (Paper II); this addendum is
self-contained given Paper II's Section 3.
**Validation:** every finite claim is checked by `addendum_checks.py`.
No proof of Fortune's conjecture, of PGD2, or of any estimate for the
reciprocal sampling measure is claimed.

**Abstract.** Two exact results about the pair-sum kernel of the
primorial-prefix walk are proved. First, the difference multiset of the
pair-sum set has a strict two-level multiplicity structure: every nonzero
difference \(S_u-S_v\) has multiplicity exactly \(N\) (when it equals a
single-walk difference \(P_i-P_k\)) or exactly \(1\). This yields an exact
two-scale decomposition of every harmonic energy and shows that single-walk
dispersion at scale \(N\) is a necessary sub-target of the pair-sum target
(3.6)/(12.1). Second, the Lebesgue measure of the level sets of the centred
kernel \(K=|H_2|^2-M\) decays sub-Weibull at every level up to the maximum:
\(\operatorname{meas}\{K\ge\lambda\}\le\exp(-\sqrt{\lambda/M})\) for
\(\lambda\ge121M\), with the sharp constant \(\sqrt2\) in the exponent
attainable asymptotically. Consequently the open level-set target of
Paper II, Proposition 4.3, which demands only \(MX^{o(1)}/\lambda\), sits an
exponential factor above the Lebesgue truth; the outstanding problem is a
sparse exceptional-set statement for the reciprocal sampling points. As a
byproduct of the moment method we also record the exact sixth Lebesgue
moment and third centred moment of the kernel.

## A.1 Notation and the rigidity lemma

As in Paper II, Section 2, fix a large parameter \(X\), let
\(X\le\ell_1<\cdots<\ell_N<2X\) be the primes of the dyadic block, and let

\[
Q_0=1,\qquad Q_j=\prod_{u\le j}\ell_u,\qquad P_j=A_XQ_j,
\]

so that

\[
P_{j+1}=\ell_{j+1}P_j\ge XP_j
\qquad(0\le j<N-1).
\tag{A.1}
\]

Let \(\mathcal P_2=\{\{j,k\}:0\le j\le k<N\}\) (index pairs as multisets),
\(M=|\mathcal P_2|=N(N+1)/2\), \(S_{\{j,k\}}=P_j+P_k\), and

\[
H_2(\theta)=\sum_{u\in\mathcal P_2}e(\theta S_u),
\qquad
K(\theta)=|H_2(\theta)|^2-M.
\]

All constants below are absolute. The only structural input is (A.1).
Scope note: the dichotomy (Section A.2) holds verbatim for any
superincreasing sequence with ratio at least \(X\), of any length \(N\).
The tail theorem (Section A.3) additionally uses \(N\ll X\) — automatic in
the prime-block setting, where \(N\asymp X/\log X\) — since the optimal
moment order at top levels is \(k\asymp N\), which must stay below the
rigidity threshold \((X-1)/2\); for an arbitrary superincreasing sequence
with \(N\gtrsim X\), (A.10) holds only for \(\lambda\lesssim(X/N)^2M^2\)-type
restricted ranges.

**Lemma A.1 (\(B\)-rigidity).** Let \(B\ge1\) be an integer and suppose
\(X>B+1\). If \(c_0,\ldots,c_{N-1}\) are integers with \(|c_t|\le B\) and

\[
\sum_{t<N}c_tP_t=0,
\]

then every \(c_t=0\).

**Proof.** Suppose not, and let \(t\) be the largest index with
\(c_t\ne0\). By (A.1), \(P_i\le P_{t-1}X^{-(t-1-i)}\) for \(i\le t-1\), so

\[
\sum_{i<t}P_i\le P_{t-1}\sum_{s\ge0}X^{-s}
=P_{t-1}\frac X{X-1}\le\frac{P_t}{X-1}.
\]

Hence

\[
\Bigl|\sum_{i<t}c_iP_i\Bigr|\le\frac{B}{X-1}P_t<P_t\le|c_t|P_t,
\]

a contradiction. \(\square\)

Taking \(B=4\) recovers Paper II, Lemma 4.1 (four-copy rigidity) with the
explicit threshold \(X>5\); we use general \(B\) in Section A.3.

**Lemma A.2 (linkage of representations).** Let \(X>5\). If
\(u,v,u',v'\in\mathcal P_2\) satisfy \(S_u-S_v=S_{u'}-S_{v'}\), then

\[
u\uplus v'=u'\uplus v
\tag{A.2}
\]

as multisets of four indices, where \(\uplus\) denotes multiset union.

**Proof.** The relation \(S_u+S_{v'}=S_{u'}+S_v\) is an integer relation
\(\sum_tc_tP_t=0\) in which each coefficient is the multiplicity of \(t\) in
\(u\uplus v'\) minus its multiplicity in \(u'\uplus v\); hence
\(|c_t|\le4\). Lemma A.1 with \(B=4\) forces every \(c_t=0\), which is
(A.2). \(\square\)

## A.2 The difference-multiplicity dichotomy

For a nonzero integer \(D\) let

\[
r(D)=\#\{(u,v)\in\mathcal P_2^2:\ u\ne v,\ S_u-S_v=D\}.
\]

**Theorem A.3 (dichotomy).** Let \(X>5\). Then for every nonzero \(D\):

1. If \(D=P_i-P_k\) for some \(i\ne k\), then \(r(D)=N\), and the
   representations are exactly the *sliding family*

   \[
   (u,v)=\bigl(\{i,t\},\{k,t\}\bigr),\qquad t=0,1,\ldots,N-1.
   \tag{A.3}
   \]

2. Otherwise \(r(D)\le1\).

Moreover the values in case 1 are pairwise distinct, there are exactly
\(N(N-1)\) of them, and the number of ordered pairs \((u,v)\), \(u\ne v\),
whose difference is of the second kind is \(M(M-1)-N^2(N-1)\).

**Proof.** *Case 1: representations of \(D=P_i-P_k\).* Each pair in (A.3)
satisfies \(S_{\{i,t\}}-S_{\{k,t\}}=P_i-P_k\), the pairs are distinct for
distinct \(t\) (as unordered pairs), and \(u\ne v\) throughout since
\(i\ne k\). So \(r(D)\ge N\).

Conversely, let \((u',v')\) be any representation and apply Lemma A.2 to
the pair of representations \((\{i,i\},\{k,i\})\) — which lies in (A.3)
with \(t=i\) — and \((u',v')\):

\[
\{i,i\}\uplus v'=u'\uplus\{k,i\}.
\tag{A.4}
\]

The index \(k\) appears in the right side of (A.4); on the left it can
appear only inside \(v'\) (as \(k\ne i\)). So \(v'=\{k,t\}\) for some
\(t\), and then (A.4) gives \(u'=(\{i,i,k,t\})\setminus\{k,i\}=\{i,t\}\).
Thus \((u',v')\) lies in the family (A.3), and \(r(D)=N\).

*Case 2: all other differences.* Let \((u,v)\) be a representation of a
difference \(D\) not of the form \(P_i-P_k\). We first observe that the
multiset intersection \(u\cap v\) must be empty. Indeed, if \(u\) and \(v\)
share an index \(t\), write \(u=\{i,t\}\), \(v=\{k,t\}\); then
\(D=P_i-P_k\) with \(i\ne k\) (since \(u\ne v\) and \(D\neq0\)),
contradicting the case assumption.

So \(u=\{a,b\}\) and \(v=\{c,d\}\) with \(u\cap v=\varnothing\). Let
\((u',v')\) be any representation of the same \(D\). Lemma A.2 gives
\(u\uplus v'=u'\uplus v\). Each index of \(v\) appears in \(u'\uplus v\)
with its multiplicity in \(v\) plus possibly more; on the left side, since
\(u\cap v=\varnothing\), the indices of \(v\) can be supplied only by
\(v'\). As both \(v\) and \(v'\) are 2-multisets, this forces \(v'=v\), and
then \(u'=u\). Hence \(r(D)=1\).

*Counting.* The values \(P_i-P_k\) (\(i\ne k\)) are pairwise distinct and
nonzero by Lemma A.1 with \(B\le2\) (a coincidence
\(P_i-P_k=P_{i'}-P_{k'}\) is a relation with coefficients bounded by 2),
giving \(N(N-1)\) values of the first
kind, contributing \(N(N-1)\cdot N=N^2(N-1)\) ordered pairs. The total
number of ordered pairs with \(u\ne v\) is \(M(M-1)\); the remainder,
\(M(M-1)-N^2(N-1)\), consists of multiplicity-one differences. \(\square\)

*Validation.* At \(N=9\) the multiplicity histogram of the difference
multiset is exactly \(\{1:1332,\ 9:72\}\) with \(72=N(N-1)\) and
\(1332=M(M-1)-N^2(N-1)\), and the multiplicity-\(N\) representation sets
coincide with (A.3) element by element (`addendum_checks.py`, check 1).

**Corollary A.4 (exact two-scale energy decomposition).** Let \(X>5\).
For any function \(T\) on the nonzero integers (in particular
\(T=|\Psi_a|^2\) or \(T=|\Phi_X|^2\) of Paper II, Section 3),

\[
\sum_{\substack{u,v\in\mathcal P_2\\u\ne v}}T(S_u-S_v)
=
N\sum_{i\ne k}T(P_i-P_k)
+
\sum_{D\in\mathcal D_1}T(D),
\tag{A.5}
\]

where \(\mathcal D_1\) is the set of multiplicity-one differences,
\(|\mathcal D_1|=M(M-1)-N^2(N-1)\). In particular, with
\(\mathcal G_a=\sum_{i\ne k}|\Psi_a(P_i-P_k)|^2\),

\[
\boxed{
\mathcal E_a=N\,\mathcal G_a+\mathcal S_a,\qquad \mathcal S_a\ge0,
}
\tag{A.6}
\]

and therefore

\[
\mathcal E_a\le MX^{o(1)}
\quad\Longrightarrow\quad
\mathcal G_a\le \frac MN X^{o(1)}\ll NX^{o(1)}.
\tag{A.7}
\]

**Remark A.5.** (A.7) is a *necessary* condition inside the sufficient
architecture: any mechanism proposed for the pair-sum target (12.1) must in
particular control the single-walk energy \(\mathcal G_a\) — an object with
\(N^2\asymp X^2/\log^2X\) terms instead of \(M^2\asymp X^4/\log^4X\) — at
scale \(N\). This refines the endpoint-sector collapse recorded in the
archived phase reports into an exact multiplicity statement: there is no
intermediate multiplicity level between \(N\) and \(1\). Conversely (A.6)
splits the target (12.1) into the single-walk part, needed at scale
\(M/N\), and a multiplicity-free (Sidon-type) part, needed at scale \(M\).

## A.3 Moments and the sub-Weibull tail theorem

**Lemma A.6 (moment bound).** Let \(k\ge1\) be an integer with
\(X>2k+1\). Then

\[
\int_0^1|H_2(\theta)|^{2k}\,d\theta
\le
\frac{(2k)!}{2^k}\,M^k.
\tag{A.8}
\]

**Proof.** By orthogonality the integral counts tuples
\((u_1,\ldots,u_k,v_1,\ldots,v_k)\in\mathcal P_2^{2k}\) with
\(\sum_iS_{u_i}=\sum_iS_{v_i}\). Such a relation has integer coefficients
bounded by \(2k\) in absolute value, so Lemma A.1 (with \(B=2k\), legitimate
as \(X>2k+1\)) forces the multiset identity

\[
u_1\uplus\cdots\uplus u_k=v_1\uplus\cdots\uplus v_k=:W.
\]

There are \(M^k\) choices of \((u_1,\ldots,u_k)\). It remains to bound, for
a fixed \(2k\)-multiset \(W\), the number of ordered \(k\)-tuples of
unordered pairs whose union is \(W\), by \((2k)!/2^k\).

Fix a labelled set \(\widetilde W\) of \(2k\) elements together with a
projection \(\pi:\widetilde W\to\operatorname{supp}(W)\) whose fibre over
each index has size equal to its multiplicity in \(W\). Every decomposition
of the multiset \(W\) into an ordered tuple of pairs is the image under
\(\pi\) of at least one decomposition of the labelled set \(\widetilde W\)
(distribute the elements of each fibre among the pair-slots that the
multiset decomposition assigns to that index). Distinct multiset
decompositions have disjoint, nonempty sets of labelled preimages, so their
number is at most the number of decompositions of a labelled \(2k\)-set into
an ordered tuple of \(k\) unordered pairs, which is

\[
(2k-1)!!\cdot k!=\frac{(2k)!}{2^kk!}\cdot k!=\frac{(2k)!}{2^k}.
\]

This proves (A.8). \(\square\)

**Theorem A.7 (sub-Weibull Lebesgue tail).** There is an absolute constant
\(X_0\) such that for all \(X\ge X_0\) the following holds. For every real
\(s\ge2M\),

\[
\operatorname{meas}\{\theta\in[0,1):|H_2(\theta)|^2\ge s\}
\le
e^3\Bigl(\frac{2s}M\Bigr)^{1/4}
\exp\Bigl(-\sqrt{\tfrac{2s}M}\Bigr).
\tag{A.9}
\]

In particular, for every \(\lambda\) with \(121M\le\lambda\le M^2\),

\[
\boxed{
\operatorname{meas}\{\theta:K(\theta)\ge\lambda\}
\le
\exp\Bigl(-\sqrt{\lambda/M}\Bigr).
}
\tag{A.10}
\]

(For \(\lambda>M^2-M\) the level set is empty, since
\(\max K=M^2-M\).)

**Proof.** Fix \(s\ge2M\) and put \(k=\lfloor\sqrt{s/(2M)}\rfloor\ge1\).
Since \(k\le\sqrt{s/(2M)}\le\sqrt{(M^2+M)/(2M)}\ll N\ll X/\log X\), the
hypothesis \(X>2k+1\) of Lemma A.6 holds for all \(X\ge X_0\) with \(X_0\)
absolute, uniformly in \(s\) in the stated range. (For
\(s> M^2+M\ge\max|H_2|^2\) the set is empty and there is nothing to prove.)

Chebyshev's inequality and Lemma A.6 give

\[
\operatorname{meas}\{|H_2|^2\ge s\}
\le
s^{-k}\int_0^1|H_2|^{2k}
\le
\frac{(2k)!}{2^k}\Bigl(\frac Ms\Bigr)^k.
\]

Using \(n!\le e\,n^{n+1/2}e^{-n}\) with \(n=2k\),

\[
\frac{(2k)!}{2^k}\Bigl(\frac Ms\Bigr)^k
\le
e\sqrt{2k}\,\Bigl(\frac{2k^2M}{e^2s}\Bigr)^{k}.
\]

By the choice of \(k\), \(k^2\le s/(2M)\), so the bracket is at most
\(e^{-2}\), and \(2k\ge\sqrt{2s/M}-2\), whence

\[
\operatorname{meas}\{|H_2|^2\ge s\}
\le
e\sqrt{2k}\,e^{-2k}
\le
e^3\,(2s/M)^{1/4}\exp\bigl(-\sqrt{2s/M}\bigr),
\]

which is (A.9).

For (A.10), apply (A.9) with \(s=M+\lambda\) and set \(t=\lambda/M\ge121\).
It suffices that

\[
f(t):=3+\tfrac14\log\bigl(2(t+1)\bigr)-\sqrt{2(t+1)}+\sqrt t\le0
\quad\text{for }t\ge121.
\]

One computes \(f(121)=3+\tfrac14\log244-\sqrt{244}+11<-0.24\), and

\[
f'(t)=\frac1{4(t+1)}-\frac1{\sqrt{2(t+1)}}+\frac1{2\sqrt t}<0
\qquad(t\ge121),
\]

because \(1/(2\sqrt t)<1/\sqrt{2(t+1)}\) for \(t\ge2\) with margin
exceeding \(1/(4(t+1))\) for \(t\ge121\). Hence \(f\le f(121)<0\) on the
range, proving (A.10). \(\square\)

**Remark A.8 (sharpness at fixed levels).** The constant \(\sqrt2\) in
(A.9) cannot be improved *at fixed levels*, in the following iterated-limit
sense. The even moments of \(H_2/\sqrt M\) match those of \(g^2/\sqrt2\)
(\(g\) standard complex Gaussian) to leading order at every fixed order
(Remark A.9); the limit law \(|g|^4/2\) is moment-determinate (its \(k\)-th
moment \((2k)!/2^k\) satisfies Carleman's condition), so for each fixed
\(t>0\),
\(\operatorname{meas}\{K\ge tM\}\to
\Pr\bigl(|g|^2\ge\sqrt{2(t+1)}\bigr)=\exp(-\sqrt{2(t+1)})\)
as \(X\to\infty\). Hence no bound of the form
\(\exp(-c\sqrt{\lambda/M})\) with \(c>\sqrt2\) can hold uniformly at fixed
levels. Sharpness *uniformly over the whole range* \(\lambda\le M^2\)
(the moderate/large-deviation regime) is **not** claimed and would require
a separate argument. Empirically (check 4) the ratio
\(-\log\operatorname{meas}/\sqrt{\lambda/M}\) is stable near \(1.5\) at
\(N=24\) for \(\lambda/M\in[2,64]\), consistent with \(\sqrt2\) plus
finite-size corrections; the measured tail respects (A.9) at every level.

**Remark A.9 (exact sixth moment).** The moment method also yields exact
formulas. By Lemma A.1 with \(B=6\) (valid for \(X>7\)), the sixth-moment
count \(\int_0^1|H_2|^6\) equals
\(\sum_\tau c_\tau(N)d_\tau^2\), where \(\tau\) runs over the partitions of
\(6\), \(d_\tau\) is the (constant) number of ordered triples of unordered
pairs realizing a fixed endpoint multiset of type \(\tau\), and
\(c_\tau(N)\), the number of index multisets of type \(\tau\), is a
polynomial in \(N\) of degree equal to the number of **parts** of
\(\tau\) — equivalently, of distinct endpoint labels: for \(\tau\) with
\(\ell\) parts and part-size multiplicities \(m_r\),
\(c_\tau(N)=N(N-1)\cdots(N-\ell+1)/\prod_r m_r!\) — vanishing at the
integers below \(\ell\). (Note: *parts*, not distinct part-sizes; e.g.
\(\tau=(3,3)\) has \(\ell=2\) and contributes degree 2.) Hence the count is a
single polynomial in \(N\) of degree at most \(6\), valid for all
\(N\ge0\); it is therefore determined by its values at seven points.
Exhaustive counting at \(N=2,\ldots,9\) (eight points) with verification at
the held-out points \(N=10,11\) gives

\[
\int_0^1|H_2(\theta)|^6\,d\theta
=
\frac{45N^6-189N^5+438N^4-597N^3+443N^2-136N}4,
\tag{A.11}
\]

and, combining with Paper II, Theorem 4.2 and \(\int|H_2|^2=M\),

\[
\int_0^1K(\theta)^3\,d\theta
=
\frac{N(N-1)^2\,(37N^3-115N^2+174N-136)}4
=
74M^3\bigl(1+O(N^{-1})\bigr).
\tag{A.12}
\]

The leading coefficients \(45/4=6!/4^3\) and \(74\) equal the
half-squared-Gaussian model values, extending the pattern
\(5M^2\) of Paper II, Theorem 4.2 to the third cumulant. The general law
\(\int|H_2|^{2k}=\bigl((2k)!/4^k\bigr)N^{2k}(1+O_k(N^{-1}))\) follows from
the same classification for every fixed \(k\) with \(X>2k+1\).

## A.4 Consequence for the level-set target

**Corollary A.10 (transfer gap).** Let \(\mu_{X,a}\) be the reciprocal
prime-pair measure of Paper II, Proposition 4.3, supported on at most
\(\pi(2H)^2=X^{4+o(1)}\) atoms of mass at most \(X^{-4+o(1)}\) each. If the
level-set target (4.5) fails at a level \(\lambda=tM\) with
\(121\le t\le M\), then at least

\[
X^{4+o(1)}\,t^{-1}
\]

atoms of \(\mu_{X,a}\) lie in a set of Lebesgue measure at most
\(\exp(-\sqrt t)\).

**Proof.** Immediate from (A.10), the target
\(\mu\{K\ge\lambda\}\ll MX^{o(1)}/\lambda\), and the atom bounds. \(\square\)

Thus the outstanding statement is not a transfer of the Lebesgue bound but
a far weaker sparse exceptional-set property: the arithmetic sampling
points must merely fail to concentrate, with density \(t^{-1}X^{o(1)}\), on
sets whose Lebesgue measure is exponentially small in \(\sqrt t\). The
allowed overshoot of \(\mu_{X,a}\) relative to Lebesgue measure at level
\(tM\) is a factor \(e^{\sqrt t}\,t^{-1}X^{o(1)}\). No mechanism for
proving such a bound is proposed here.

## A.5 Validation summary

`addendum_checks.py` performs:

1. **Dichotomy** (Theorem A.3): at \(N=8,9\), the difference-multiplicity
   histogram is exactly \(\{1:M(M-1)-N^2(N-1),\ N:N(N-1)\}\), and the
   representation set of every multiplicity-\(N\) difference equals the
   sliding family (A.3) element by element.
2. **Moment bound** (Lemma A.6): exact collision counts at
   \(k=2,3,4\), \(N\le9\) satisfy (A.8).
3. **Exact moments** (Remark A.9): (A.11) reproduces exhaustive counts at
   \(N=2,\ldots,11\) and (A.12) at \(N=3,5,7\).
4. **Tail bound** (Theorem A.7): with exact modular phase arithmetic at
   \(N=24\) (200{,}000 samples), the empirical tail respects (A.9) at every
   measurable level \(\lambda/M\in\{2,4,8,16,32,64\}\), and the empirical
   exponent constant is \(\approx1.5\), consistent with Remark A.8.
