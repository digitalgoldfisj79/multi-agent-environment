# Parity-breaking factor sieve for the d=1 function-field problem

**Date:** 2026-07-21  
**Status:** exact reduction proved.

## 1. Setup

Let \(p\ge5\) be prime and \(a\in\mathbf F_p^*\). Put

\[
F_{c,d}(X)=X^p+aX^3+cX+d
\]

and

\[
H_{c,d}(X)=aX^3+(c+1)X+d.
\]

Let

\[
\mathcal A_a=
\{(c,d)\in\mathbf F_p^2:H_{c,d}\text{ has no root in }\mathbf F_p\}.
\]

The local-squarefreeness theorem in `DISCRIMINANT_MASS.md` gives, for every \((c,d)\in\mathcal A_a\):

1. \(F_{c,d}\) has no linear factor;
2. \(F_{c,d}\) is squarefree;
3. \(\chi(\operatorname{Disc}F_{c,d})\in\{\pm1\}\).

## 2. Exact parity-breaking lemma

### Theorem PS.1

For \((c,d)\in\mathcal A_a\),

\[
\boxed{
F_{c,d}\text{ is irreducible}
\iff
\chi(\operatorname{Disc}F_{c,d})=+1
\text{ and }
F_{c,d}\text{ has no irreducible factor of degree }
2\le k\le\lfloor p/3\rfloor.
}
\]

### Proof

Factor

\[
F_{c,d}=P_1\cdots P_r
\]

into distinct monic irreducibles. Since \(F_{c,d}\) is locally admissible, every \(\deg P_i\ge2\), and

\[
\sum_{i=1}^r\deg P_i=p.
\]

Pellet's formula says

\[
\mu(F_{c,d})=(-1)^p\chi(\operatorname{Disc}F_{c,d}).
\]

As \(p\) is odd and \(F_{c,d}\) is squarefree,

\[
(-1)^r=-\chi(\operatorname{Disc}F_{c,d}),
\]

or equivalently

\[
\chi(\operatorname{Disc}F_{c,d})=(-1)^{r+1}.
\]

Thus positive discriminant character is equivalent to odd \(r\).

If \(F_{c,d}\) is irreducible, then \(r=1\), its discriminant character is positive, and it has no proper factor.

Conversely, suppose the discriminant character is positive and \(F_{c,d}\) is reducible. Then \(r\) is odd and \(r\ge3\). Therefore

\[
\min_i\deg P_i
\le \frac1r\sum_i\deg P_i
=\frac pr
\le\frac p3.
\]

Because the factor degrees are integers and at least two, a factor occurs in the stated range, contradicting the hypothesis. Hence \(r=1\). QED.

## 3. Exact inclusion–exclusion identity

Let

\[
z=\lfloor p/3\rfloor
\]

and let \(\mathscr P_z\) be the set of monic irreducibles over \(\mathbf F_p\) with degrees in \([2,z]\). Let \(\mathscr D_z\) be the squarefree monic products of elements of \(\mathscr P_z\), including \(D=1\).

For squarefree \(F\),

\[
\sum_{\substack{D\in\mathscr D_z\\D\mid F}}\mu(D)
=
\begin{cases}
1,&F\text{ has no factor in }\mathscr P_z,\\
0,&F\text{ has at least one factor in }\mathscr P_z.
\end{cases}
\]

Theorem PS.1 therefore gives the exact identity

\[
\boxed{
I_a(p)
=
\frac12
\sum_{(c,d)\in\mathcal A_a}
\left(1+\chi(\operatorname{Disc}F_{c,d})\right)
\sum_{\substack{D\in\mathscr D_z\\D\mid F_{c,d}}}\mu(D),
}
\]

where \(I_a(p)\) is the number of irreducible members in the slice.

Define

\[
A_a(D)=
\#\{(c,d)\in\mathcal A_a:D\mid F_{c,d}\},
\]

and

\[
B_a(D)=
\sum_{\substack{(c,d)\in\mathcal A_a\\D\mid F_{c,d}}}
\chi(\operatorname{Disc}F_{c,d}).
\]

Interchanging the finite sums yields

\[
\boxed{
I_a(p)
=
\frac12
\sum_{D\in\mathscr D_z}
\mu(D)\bigl(A_a(D)+B_a(D)\bigr).
}
\]

The \(D=1\) terms are already known:

\[
A_a(1)=\frac{p^2-1}{3},
\qquad
B_a(1)=M_a^{\mathrm{loc}}(p).
\]

## 4. Incidence uniqueness

### Lemma PS.2

For every monic \(D\in\mathbf F_p[X]\) with \(\deg D\ge2\),

\[
A_a(D)\le1.
\]

### Proof

If the same \(D\) divided both \(F_{c,d}\) and \(F_{c',d'}\), it would divide their difference

\[
(c-c')X+(d-d').
\]

A nonzero polynomial of degree at most one cannot be divisible by \(D\). Hence \(c=c'\) and \(d=d'\). QED.

Consequently

\[
B_a(D)\in\{-1,0,+1\}
\]

for every \(D\ne1\), and whenever \(A_a(D)=1\),

\[
B_a(D)=
\chi(\operatorname{Disc}F_{c(D),d(D)}).
\]

Thus the remaining theorem is an incidence-distribution problem: determine the signed Möbius sum over those squarefree small-factor products \(D\) that are compatible with the two-parameter sparse family.

## 5. Frobenius hook-character form

For a squarefree degree-\(p\) polynomial \(F\), let \(\sigma_F\in S_p\) denote Frobenius acting on its roots, and let `Std` denote the standard representation of \(S_p\).

### Theorem PS.3

\[
\boxed{
p\,\mathbf1_{F\text{ irreducible}}
=
\det(1-\sigma_F\mid\mathrm{Std})
=
\sum_{j=0}^{p-1}(-1)^j
\chi_{\wedge^j\mathrm{Std}}(\sigma_F).
}
\]

### Proof

If \(\sigma_F\) has \(r>1\) cycles, its permutation representation has eigenvalue \(1\) with multiplicity \(r\), so `Std` has eigenvalue \(1\) and the determinant vanishes.

If \(F\) is irreducible, \(\sigma_F\) is a \(p\)-cycle. Its eigenvalues on `Std` are the nontrivial \(p\)-th roots of unity, hence

\[
\det(1-\sigma_F\mid\mathrm{Std})
=
\prod_{j=1}^{p-1}(1-\zeta_p^j)=p.
\]

The second equality is the characteristic-polynomial expansion of the determinant into exterior-power traces. QED.

The discriminant character is the top exterior-power character only. Theorem PS.3 gives a precise representation-theoretic explanation of the remaining gap: sign information breaks the ordinary sieve parity barrier but does not replace the lower hook traces needed to isolate a single Frobenius cycle.

## 6. Correct next target

A sufficient theorem is any estimate proving

\[
\sum_{D\in\mathscr D_z}
\mu(D)\bigl(A_a(D)+B_a(D)\bigr)>0
\]

for at least one nonzero cubic slice \(a\), uniformly for all sufficiently large primes \(p\). Finite certification can then handle the remaining primes.

The two plausible implementations are:

1. a parity-weighted combinatorial sieve with a level of distribution reaching degree \(p/3\);
2. a geometric trace formula that evaluates the full alternating hook sum as one object rather than bounding its \(p\) terms separately.
