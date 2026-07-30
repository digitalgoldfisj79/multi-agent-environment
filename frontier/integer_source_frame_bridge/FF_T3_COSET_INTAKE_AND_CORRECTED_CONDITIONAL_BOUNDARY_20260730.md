# Function-field T3 coset intake and corrected conditional boundary

Date: 30 July 2026  
Branch: `gpt56/fortune-mesoscopic-cotlar-20260728`  
Reviewed contribution: PR #33 issue comment `5127649720` and `fortune-review/FF_T3_COSET_NOTE_20260730.md` on branch `claude/fortunes-conjecture-mechanisms-fuuz4z`.

## Executive decision

The function-field coset attack contains a genuine structural advance. Theorems A, B and C, together with the soft-bound no-go, are accepted. The stated conditional Theorem D is not accepted in its present form because its exponent ledger inserts an additional `q^{-m}` saving which is not supplied by `FFPS` as stated.

The corrected conclusion is:

1. the coset family makes `PORS_FF` exact;
2. exact subspace completion converts the cross-modulus term into an explicit finite-ring Kloosterman-fraction sum;
3. fixed-source square-root cancellation over the prime pair is not sufficient;
4. the load-bearing new input is a **Lambda-signed joint source/modulus cancellation theorem**.

Fortune's conjecture and the function-field first-band theorem remain **OPEN**.

## 1. Accepted exact structure

### 1.1 Coset fairness

For `R>=k`, multiplication by a puncture `L` coprime to a degree-`k` irreducible `P` and reduction modulo `P` map the monic degree-`R` family exactly `q^{R-k}`-to-one onto every residue. Hence

\[
\sum_{\deg M=R}D_P(-LM)^2
=q^{R-k}\sum_{a\bmod P}D_P(a)^2.
\]

This is an identity. On the full coset family, `PORS_FF` has no remaining analytic content.

### 1.2 Same-modulus orthogonality

For two distinct multiplicative characters modulo the same degree-`k` prime, the quotient character is nontrivial and its `L`-polynomial has degree at most `k-1`. Therefore its degree-`R` coefficient vanishes for `R>=k`. The within-modulus cross-character contribution is exactly zero.

### 1.3 Soft-bound no-go

The dual sampling Gram is positive semidefinite and has diagonal of order `q^{2k}/k`. Consequently its operator norm is at least that size. Arbitrary-coefficient Bessel or duality estimates cannot exploit the sparse coset family. Any successful estimate must use the actual von Mangoldt coefficients.

### 1.4 Exact subspace completion

For distinct sources `f,f'` and distinct degree-`k` primes `P,S`, let `c(f,f';P,S)` be the CRT point satisfying

\[
c\equiv-fL^{-1}\pmod P,
\qquad
c\equiv-f'L^{-1}\pmod S.
\]

The monic degree-`R` family is the affine subspace `t^R+V`, where `V={deg<R}` inside `F_q[t]/(PS)`. If `V^perp` is its additive-character annihilator, then

\[
\mathbf 1_{c\in t^R+V}
=q^{R-2k}\sum_{\theta\in V^\perp}\psi_\theta(c-t^R).
\]

The zero frequency gives the density term and cancels the centred main term. The residual contains the CRT inverses `S^{-1} mod P` and `P^{-1} mod S`, producing an explicit function-field Kloosterman-fraction phase. This is the first point at which the previously unusable integer completion route becomes a well-posed finite-ring exponential-sum problem.

## 2. Correction to conditional Theorem D

The contribution defines, for fixed nonzero `theta` and fixed sources `f,f'`,

\[
S_\theta(f,f')
=
\sum_{\substack{P\ne S\\\deg P=\deg S=k}}
\psi_\theta(c(f,f';P,S)-t^R).
\]

The stated input `FFPS` is

\[
|S_\theta(f,f')|
\ll
\#\{(P,S)\}\,q^{-k/2}\,\operatorname{poly}(k,m,\deg L).
\]

Since the number of ordered prime pairs is of order `q^{2k}/k^2`, this gives

\[
|S_\theta(f,f')|
\ll q^{3k/2}\operatorname{poly}(k,m,\deg L).
\]

The exact completed residual is

\[
q^{R-2k}
\sum_{\theta\in V^\perp\setminus\{0\}}
\sum_{f\ne f'}
\Lambda(f)\Lambda(f')S_\theta(f,f').
\]

There are `q^{2k-R}` nonzero frequencies up to constants, while

\[
\sum_{\deg f=m}\Lambda(f)=q^m.
\]

Taking absolute values in the source variables therefore yields

\[
|T_3-\mathrm{centering}|
\ll
q^{2m+3k/2}\operatorname{poly}(k,m,\deg L).
\]

The diagonal has scale `q^{R+m}`. Thus `FFPS` as stated gives only

\[
\boxed{
\frac{|T_3-\mathrm{centering}|}{\mathrm{DIAG}}
\ll
q^{m+3k/2-R}\operatorname{poly}(k,m,\deg L).
}
\]

It does **not** give `q^{3k/2-R}`. The displayed ledger in the reviewed note contains an unexplained factor `q^{-m}`. That factor is exactly the missing cancellation across the signed source-pair sum.

Accordingly:

- conditional Theorem D is **RETRACTED AS STATED**;
- the claimed exponent becomes valid only under a strengthened Lambda-signed hypothesis.

## 3. Corrected conditional target

Define `FFLKS(k,R,m,L)` by requiring, uniformly for nonzero `theta`,

\[
\boxed{
\left|
\sum_{f\ne f'}
\Lambda(f)\Lambda(f')S_\theta(f,f')
\right|
\ll
q^{m+3k/2}\operatorname{poly}(k,m,\deg L).
}
\]

This saves `q^{-m}` against the absolute source-pair mass and `q^{-k/2}` against the prime-pair mass. Under `FFLKS`, summing the `q^{2k-R}` frequencies and restoring the completion factor gives

\[
|T_3-\mathrm{centering}|
\ll q^{m+3k/2}\operatorname{poly}(k,m,\deg L),
\]

hence

\[
\boxed{
\frac{|T_3-\mathrm{centering}|}{\mathrm{DIAG}}
\ll q^{3k/2-R}\operatorname{poly}(k,m,\deg L).
}
\]

The original claimed power saving for `R>3k/2` is therefore a valid consequence of `FFLKS`, not of fixed-source `FFPS` alone.

A weaker averaged formulation over `theta` is also sufficient:

\[
\sum_{\theta\ne0}
\left|
\sum_{f\ne f'}
\Lambda(f)\Lambda(f')S_\theta(f,f')
\right|
\ll
q^{2k-R}q^{m+3k/2}\operatorname{poly}(k,m,\deg L).
\]

## 4. Literature mapping

The Sawin and Sawin--Shusterman results establish powerful square-root or near-square-root cancellation for factorization functions in squarefree progressions, short affine subspaces, and inverse-additive-character sums. They are highly relevant inputs and proof templates.

They do not directly state `FFLKS`:

- their standard progression results fix the modulus while summing the arithmetic function;
- the present phase varies two prime moduli simultaneously;
- the CRT inverses couple `P`, `S`, `f` and `f'` in one four-variable trace function;
- uniformity in the puncture `L=t^q-t` must be tracked as `q` grows.

The next task is therefore a literal sheaf construction and conductor/degeneracy audit for the joint parameter space, not a citation-level application of an existing theorem.

## 5. Revised next programme

### Gate FF4.1 -- phase geometry

Write the CRT phase explicitly as a rational function on the parameter space of `(P,S,f,f')`. Identify poles, diagonal degeneracies, Artin--Schreier trivial loci and dependence on `L`.

### Gate FF4.2 -- one-variable tests

Prove or falsify square-root cancellation when summing successively over:

1. `P` with `S,f,f'` fixed;
2. `S` with `P,f,f'` fixed;
3. `f` with `P,S,f'` fixed;
4. `f'` with `P,S,f` fixed.

These tests locate which variable supplies the missing `q^{-m}`.

### Gate FF4.3 -- Lambda-signed joint theorem

Attack `FFLKS` using the factorization-function sheaf machinery. The theorem must retain both the source signs and the two-prime CRT-inverse phase.

### Gate FF4.4 -- puncture uniformity

Obtain conductor bounds polynomial in `deg L`, and then specialize to `L=t^q-t`.

### Gate FF4.5 -- thinning

Only after the coset theorem is closed should the programme pass from all monic degree-`R` centres to algebraic squarefree-product families and finally to a thin ordered walk analogue.

## 6. Corrected boundary

### PROVED

- coset `PORS_FF` fairness identity;
- exact same-modulus character orthogonality;
- soft-bound operator-norm no-go;
- exact affine-subspace completion;
- exact cancellation of the zero-frequency density term;
- explicit Kloosterman-fraction prime-pair representation.

### COMPUTATIONALLY VERIFIED

- the exact identities on the committed small-field panels;
- cross/diagonal and fixed-source prime-pair diagnostics.

### EMPIRICAL

- decay of the complete coset cross term at `k=2,R=3,m=3`;
- compatibility of the fixed and `t^q-t` punctures on those panels;
- fixed-source prime-pair sums at the `q^{-k/2}` scale.

### RETRACTED OR CORRECTED

- Theorem D under fixed-source `FFPS` alone;
- the unexplained `q^{-m}` factor in its exponent ledger.

### OPEN

- `FFLKS` or an equivalent Lambda-signed four-variable trace estimate;
- puncture-uniform conductor control;
- coset `PORC_FF` beyond the conditional range;
- thinning to squarefree-product families and walks;
- the function-field first-band theorem;
- every integer-side orbit and higher-conductor theorem;
- Fortune's conjecture.

## Verdict

Claude's exact structural discovery is retained and is important. It turns the function-field cross-modulus obstruction into a concrete sheaf-theoretic problem. The claimed conditional power saving, however, requires simultaneous cancellation in the von Mangoldt source variables and the prime-modulus variables. The corrected load-bearing target is `FFLKS`, not fixed-source `FFPS`.