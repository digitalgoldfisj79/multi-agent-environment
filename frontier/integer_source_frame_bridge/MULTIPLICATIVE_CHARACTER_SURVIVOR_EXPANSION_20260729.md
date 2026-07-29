# Multiplicative-character survivor expansion and the signed hybrid boundary

Date: 29 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`

Status: the primitive-character expansion, its exact coefficient energies, the high-conductor source estimate and the multiplicative scalar-factorization no-go are **PROVED EXACTLY**. They expose a new analytic coordinate system for `PCRST(X)`, but do not prove the required deterministic joint transfer.

## 1. Purpose

The complete-CRT survivor Gram proves that the full Euler band has the correct covariance after averaging over the product of nonzero residue classes. The remaining question is how the actual candidate primes sample that product model along the primorial centres.

The natural Fourier basis of

\[
\Omega_R=\prod_{p\in\mathcal P_R}\mathbb F_p^\times
\]

is multiplicative, not additive. In that basis the complete normalized survivor product has a particularly rigid tensor expansion over primitive characters of squarefree conductors supported on the band.

This document:

1. derives that expansion exactly;
2. identifies its finite quadratic energy;
3. proves that the high-conductor source energy is separately small;
4. proves that every multiplicative scalar Cauchy redistribution has exponential centre/source diagonal product;
5. isolates the genuinely joint signed hybrid character theorem which remains.

## 2. Notation

Let

\[
\Pi_R=\prod_{p\in\mathcal P_R}p,
\qquad
V_R=\prod_{p\in\mathcal P_R}\frac{p-2}{p-1}.
\tag{2.1}
\]

For a squarefree divisor `Q\mid\Pi_R`, define

\[
\varphi^\dagger(Q)=\prod_{p\mid Q}(p-2).
\tag{2.2}
\]

For odd squarefree `Q`, this is the number of primitive Dirichlet characters modulo `Q`: primitivity is equivalent to every local component modulo `p\mid Q` being nonprincipal.

Write

\[
\sum_{\chi\bmod Q}^{\dagger}
\]

for the sum over those exact-conductor characters. For `Q=1`, the sum consists of the trivial character.

Throughout Sections 3--6, assume

\[
(mP,\Pi_R)=1.
\tag{2.3}
\]

The self-coordinate case `m=p\in\mathcal P_R` is handled by the exact reduced-band formula already proved in the companion survivor-Gram note.

## 3. Local multiplicative character identity

For `p\in\mathcal P_R`, character orthogonality on `\mathbb F_p^\times` gives

\[
\mathbf1_{m\equiv-P\pmod p}
=
\frac1{p-1}
\sum_{\chi\bmod p}
\chi(m)\overline{\chi(-P)}.
\tag{3.1}
\]

Consequently,

\[
\sum_{\substack{\chi\bmod p\\\chi\ne\chi_0}}
\chi(m)\overline{\chi(-P)}
=
\begin{cases}
p-2,&m\equiv-P\pmod p,\\
-1,&m\not\equiv-P\pmod p.
\end{cases}
\tag{3.2}
\]

The normalized local survivor factor therefore satisfies

\[
\boxed{
\frac{p-1}{p-2}\mathbf1_{p\nmid P+m}
=
1-
\frac1{p-2}
\sum_{\substack{\chi\bmod p\\\chi\ne\chi_0}}
\chi(m)\overline{\chi(-P)}.
}
\tag{3.3}
\]

The constant coordinate and all nonprincipal local characters remain inside one exactly centred identity.

## 4. Full primitive-character expansion

Define

\[
S_{P,R}(m)
=
V_R^{-1}\mathbf1_{(P+m,\Pi_R)=1}
\tag{4.1}
\]

and

\[
g_{P,R}(m)=S_{P,R}(m)-1.
\tag{4.2}
\]

### Theorem 4.1 — exact primitive-character survivor expansion

For `(mP,\Pi_R)=1`,

\[
\boxed{
S_{P,R}(m)
=
\sum_{Q\mid\Pi_R}
\frac{\mu(Q)}{\varphi^\dagger(Q)}
\sum_{\chi\bmod Q}^{\dagger}
\chi(m)\overline{\chi(-P)}.
}
\tag{4.3}
\]

Equivalently,

\[
\boxed{
g_{P,R}(m)
=
\sum_{\substack{Q\mid\Pi_R\\Q>1}}
\frac{\mu(Q)}{\varphi^\dagger(Q)}
\sum_{\chi\bmod Q}^{\dagger}
\chi(m)\overline{\chi(-P)}.
}
\tag{4.4}
\]

### Proof

Multiply (3.3) over `p\in\mathcal P_R`. Choosing the constant term at primes outside a subset and a nonprincipal local character at primes inside it produces a squarefree conductor `Q`. The product character has exact conductor `Q`, and the scalar coefficient is

\[
\prod_{p\mid Q}\frac{-1}{p-2}
=
\frac{\mu(Q)}{\varphi^\dagger(Q)}.
\]

This gives (4.3). Removing the `Q=1` term gives (4.4). `\square`

This is the multiplicative analogue of the exact Ramanujan projector, but it is adapted to the candidate source conditioned to be nonzero modulo every new prime.

## 5. Exact coefficient energies

### Theorem 5.1 — finite quadratic mass

Since there are `\varphi^\dagger(Q)` exact-conductor characters modulo `Q`,

\[
\boxed{
\sum_{Q\mid\Pi_R}
\frac1{\varphi^\dagger(Q)^2}
\sum_{\chi\bmod Q}^{\dagger}1
=
\sum_{Q\mid\Pi_R}\frac1{\varphi^\dagger(Q)}
=
V_R^{-1}.
}
\tag{5.1}
\]

Thus

\[
\boxed{
\sum_{\substack{Q\mid\Pi_R\\Q>1}}
\frac1{\varphi^\dagger(Q)^2}
\sum_{\chi\bmod Q}^{\dagger}1
=
V_R^{-1}-1.
}
\tag{5.2}
\]

This is exactly the diagonal complete-CRT survivor variance.

By contrast, the character-level absolute mass is

\[
\boxed{
\sum_{Q\mid\Pi_R}
\frac1{\varphi^\dagger(Q)}
\sum_{\chi\bmod Q}^{\dagger}1
=
2^{|\mathcal P_R|}.
}
\tag{5.3}
\]

Therefore the expansion is finite-energy but not absolutely summable after the primitive-character multiplicity is exposed. The Möbius signs and cross-conductor covariance are essential.

## 6. Recovery of the complete survivor Gram

Let `P_j,P_k` be two centres. Orthogonality over the complete source product gives

\[
\mathbb E_{\Omega_R}
g_{P_j,R}\overline{g_{P_k,R}}
=
\sum_{\substack{Q\mid\Pi_R\\Q>1}}
\frac1{\varphi^\dagger(Q)^2}
\sum_{\chi\bmod Q}^{\dagger}
\overline{\chi(-P_j)}\chi(-P_k).
\tag{6.1}
\]

At a prime `p`, the local nonprincipal character sum is `p-2` if
`p\mid P_j-P_k` and `-1` otherwise. Multiplication over the band recovers exactly

\[
\prod_{p\mid P_j-P_k}\frac{p-1}{p-2}
\prod_{p\nmid P_j-P_k}\frac{(p-1)(p-3)}{(p-2)^2}
-1.
\tag{6.2}
\]

Hence the primitive-character expansion gives a second exact proof of the all-order survivor Gram.

## 7. Exact source transform

For source coefficients `a_m` supported on integers coprime to `\Pi_R`, put

\[
\mathcal S_Q(\chi)
=
\sum_m a_m\chi(m).
\tag{7.1}
\]

Summing (4.4) over the source gives

\[
\boxed{
\sum_m a_m g_{P_j,R}(m)
=
\sum_{\substack{Q\mid\Pi_R\\Q>1}}
\frac{\mu(Q)}{\varphi^\dagger(Q)}
\sum_{\chi\bmod Q}^{\dagger}
\mathcal S_Q(\chi)\overline{\chi(-P_j)}.
}
\tag{7.2}
\]

For the actual band transfer, the coefficients also contain the earlier-band survivor history and the exact self-coordinate correction. Formula (7.2) remains the spectral core of each ordinary nonzero-residue component.

## 8. Conductor geometry at the Fortune scale

Suppose

\[
H=\eta X^2,\qquad 0<\eta<1,
\]

and every prime in the band exceeds `R\ge X`.

If `Q\mid\Pi_R` has at least two prime factors, then

\[
Q>R^2\ge X^2>H.
\tag{8.1}
\]

Therefore

\[
\boxed{
1<Q\le H
\quad\Longrightarrow\quad
Q=p\in\mathcal P_R.
}
\tag{8.2}
\]

The low-conductor spectrum is exactly the single-prime physical layer. Every genuinely higher Euler order lies at conductor `Q>H`.

This is the multiplicative-character version of the physical/high-quotient split, with no ambiguous intermediate conductor layer.

## 9. High-conductor source energy

Let the source coefficients be supported in an interval of length at most `H`. For `Q>H`, distinct source integers are distinct modulo `Q`. Complete character orthogonality gives

\[
\sum_{\chi\bmod Q}
\left|\sum_m a_m\chi(m)\right|^2
=
\varphi(Q)\sum_m|a_m|^2.
\tag{9.1}
\]

The primitive characters are a subset of all characters, so

\[
\sum_{\chi\bmod Q}^{\dagger}
|\mathcal S_Q(\chi)|^2
\le
\varphi(Q)\sum_m|a_m|^2.
\tag{9.2}
\]

### Theorem 9.1 — weighted high-conductor source bound

\[
\boxed{
\sum_{\substack{Q\mid\Pi_R\\Q>H}}
\frac1{\varphi^\dagger(Q)^2}
\sum_{\chi\bmod Q}^{\dagger}
|\mathcal S_Q(\chi)|^2
\le
\left(
\sum_{\substack{Q\mid\Pi_R\\Q>H}}
\frac{\varphi(Q)}{\varphi^\dagger(Q)^2}
\right)
\sum_m|a_m|^2.
}
\tag{9.3}
\]

Moreover,

\[
\sum_{\substack{Q\mid\Pi_R\\Q>1}}
\frac{\varphi(Q)}{\varphi^\dagger(Q)^2}
=
\prod_{p\in\mathcal P_R}
\left(
1+\frac{p-1}{(p-2)^2}
\right)-1
\ll
\frac1{\log R}.
\tag{9.4}
\]

Hence

\[
\boxed{
\sum_{\substack{Q\mid\Pi_R\\Q>H}}
\frac1{\varphi^\dagger(Q)^2}
\sum_{\chi\bmod Q}^{\dagger}
|\mathcal S_Q(\chi)|^2
\ll
\frac1{\log R}\sum_m|a_m|^2.
}
\tag{9.5}
\]

Thus the higher-order source spectrum is not intrinsically too large when measured in its natural quadratic coefficient norm.

## 10. Exact multiplicative factorization no-go

A separate source/frame proof would split the local coefficient

\[
\frac1{p-2}=a_p b_p
\tag{10.1}
\]

and apply Cauchy--Schwarz between a centre family weighted by `a_p` and a source family weighted by `b_p`.

For a multiplicative split, the two diagonal masses are

\[
\mathfrak C(a)
=
\prod_{p\in\mathcal P_R}
\left(1+(p-2)|a_p|^2\right)
\tag{10.2}
\]

and

\[
\mathfrak S(b)
=
\prod_{p\in\mathcal P_R}
\left(1+(p-2)|b_p|^2\right).
\tag{10.3}
\]

Because `a_pb_p=(p-2)^{-1}`, putting

\[
x_p=(p-2)|a_p|^2
\]

gives

\[
(p-2)|b_p|^2=x_p^{-1}.
\]

Therefore every local product satisfies

\[
(1+x_p)(1+x_p^{-1})\ge4.
\tag{10.4}
\]

### Theorem 10.1 — scalar redistribution obstruction

For every multiplicative scalar redistribution of the primitive-character coefficient,

\[
\boxed{
\mathfrak C(a)\mathfrak S(b)
\ge
4^{|\mathcal P_R|}.
}
\tag{10.5}
\]

Equality occurs at the square-root split.

Thus no scalar placement of the coefficient can make both the centre and source diagonal norms admissible. Putting all the coefficient on the centre recovers the bounded survivor Gram but leaves the unweighted source spectrum. Putting it on the source yields the small bound (9.5) but leaves an exponential centre frame. Every intermediate multiplicative split is at least exponentially bad in product.

This is an exact no-go for factorized Cauchy arguments. It is not a no-go for a genuinely joint signed bilinear theorem.

## 11. Revised analytic target

For one band, dual coefficients `c_j` and source weights `a_{j,m}` lead to the hybrid form

\[
\mathfrak B_R
=
\sum_{\substack{Q\mid\Pi_R\\Q>1}}
\frac{\mu(Q)}{\varphi^\dagger(Q)}
\sum_{\chi\bmod Q}^{\dagger}
\sum_{j\in B}
c_j\overline{\chi(-P_j)}
\sum_m a_{j,m}\chi(m),
\tag{11.1}
\]

together with the exact reduced-band self coordinates and zeroth/self drift.

### Open theorem `SMHLS(X)` — signed Möbius hybrid large sieve

Prove the Fortune-scale bound for (11.1) while retaining jointly:

1. the Möbius sign across conductors;
2. the exact-conductor primitive-character tensor;
3. the common candidate-prime source;
4. the primorial centre phases;
5. previous-band survivor weights;
6. the self-coordinate drift and the zeroth-centred coordinate.

A conductorwise nonnegative large sieve is insufficient: it removes the `\mu(Q)` cancellation and falls under Theorem 10.1. `SMHLS(X)` is a spectral formulation of `PCRST(X)`, not an additional independent conjecture.

## 12. Existing large-sieve technology

Classical and sparse-modulus large sieves control nonnegative sums of character or additive-character energies over prescribed modulus sets. Sparse-modulus theorems additionally require distribution hypotheses on the set of moduli in residue classes.

The present conductor set is the Boolean semigroup of all squarefree products of one dyadic prime band, equipped with the tensor coefficient `\mu(Q)/\varphi^\dagger(Q)`. Its useful cancellation is between conductors. Theorem 10.1 shows that converting it to two separate positive large-sieve norms is exponentially lossy.

No black-box sparse-modulus large-sieve theorem found in the audit supplies the signed cross-conductor hybrid estimate (11.1). This is an applicability conclusion, not a claim that character methods cannot prove it.

## 13. What changed

The high-order spectrum had previously been treated as a sparse physical tail whose cancellation with normalization drift was difficult to preserve. The primitive-character expansion gives three sharper facts:

1. all higher Euler orders are exactly the conductors `Q>H`;
2. their natural weighted source energy is already `O(1/\log R)`;
3. the remaining loss occurs only when source and primorial-centre geometry are separated.

Accordingly, the wall is not uncontrolled high-conductor source energy. It is the absence of a signed joint hybrid estimate which can use that source energy without destroying the bounded complete-survivor centre Gram.

## 14. Boundary

**PROVED EXACTLY**

1. local multiplicative character identity (3.3);
2. full primitive-character expansion (4.3)--(4.4);
3. exact quadratic and absolute character masses (5.1)--(5.3);
4. recovery of the complete survivor Gram;
5. low/high conductor separation (8.2);
6. high-conductor source estimate (9.3);
7. multiplicative scalar-factorization no-go (10.5).

**PROVED USING CLASSICAL PRIME ESTIMATES**

1. the Euler-product bound (9.4).

**COMPUTATIONALLY VERIFIED**

1. the expansion on every unit source residue in a complete finite panel;
2. exact coefficient masses;
3. representative scalar redistributions and the `4^{|\mathcal P_R|}` lower bound;
4. the low/high conductor split and weighted high-conductor coefficient sum.

**OPEN**

1. `SMHLS(X)`, equivalently the spectral form of `PCRST(X)`;
2. arithmetic `NSMT(X)`;
3. the Fortune variance theorem;
4. Fortune's conjecture.
