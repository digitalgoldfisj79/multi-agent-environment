# Primorial-prefix residue anti-concentration

## Setup

Let `X` be large. Write

`q_1<...<q_N`

for the primes in `[X,2X]`, and define

`B_X=product_{p<X}p`, `P_0=B_X`, `P_j=B_X product_{i=1}^j q_i`.

Let `varpi>2X` be prime and put

`A=A_X(varpi)={P_j mod varpi:0<=j<=N} subset F_varpi^*`, `m=|A|`.

All algebra below is in `F_varpi`.

## Lemma 1 — fractional-linear recurrence

For `0<=j<=N-2`, let `g_j=q_{j+2}-q_{j+1}`. Then

`P_{j+2}=g_j P_{j+1}+P_{j+1}^2/P_j`.

Proof: `P_{j+1}=q_{j+1}P_j`, so `P_{j+1}^2/P_j=q_{j+1}P_{j+1}`; adding `g_j P_{j+1}` gives `q_{j+2}P_{j+1}=P_{j+2}`.

For fixed nonzero `d`, define

`T_{a,d}(x)=d a+a^2/x`, for `a,x !=0`.

Every index with `g_j=d` supplies a transition

`T_{P_{j+1},d}(P_j)=P_{j+2}`

inside `A`.

These ordered transition pairs `(P_j,P_{j+1})` are distinct modulo `varpi`: their ratio is `q_{j+1}`, and the distinct integers `q_{j+1}` all lie below `varpi`.

## Lemma 2 — affine linearisation

`T_{a,d}` is injective on `F_varpi^*`, with inverse

`T_{a,d}^{-1}(u)=a^2/(u-da)`

on its image. If `r=b/a`, then

`T_{b,d}(T_{a,d}^{-1}(u)) = r^2 u+d a r(1-r)`.

Thus every ordered pair `(a,b)` defines an affine line

`ell_{a,b,d}: v=r^2 u+d a r(1-r)`.

## Lemma 3 — line multiplicity

Assume `varpi` odd and `d!=0`. The line `ell_{a,b,d}` is the identity line iff `a=b`. Every nonidentity affine line has at most two representations as `ell_{a,b,d}` with `(a,b) in A^2`.

Proof. If `ell:v=sigma u+tau`, each representation gives `r^2=sigma`. There are at most two possible `r`. For a nonidentity representation `r!=1`; also `r!=0`, so `d r(1-r)!=0`, and then `a=tau/(d r(1-r))` is uniquely determined. For the identity line, `r^2=1` and `d a r(1-r)=0`; since `d,a!=0` and the characteristic is odd, `r=-1` is impossible and `r=1`, hence `a=b`.

## Proposition 4 — transition count implies value-set size

Let

`N_d(A)=#{(x,a) in A^2:T_{a,d}(x) in A}`.

If `N_d(A)>=T`, then

`m >> T^(8/15)`

with an absolute implied constant.

Proof. For each `x in A`, let `R(x)=#{a in A:T_{a,d}(x) in A}`. Cauchy--Schwarz gives

`N_d(A)^2 <= m sum_x R(x)^2 = m sum_{a,b} M(a,b)`,

where `M(a,b)` counts common inputs whose two outputs lie in `A`.

By Lemmas 2--3, diagonal pairs contribute at most `m^2`, while nonidentity pairs are bounded by twice the incidence count between `A x A` and the distinct lines `ell_{a,b,d}`. Enlarge the line set to exactly `m^2` nonvertical lines if necessary. This is possible because `m<=N+1<varpi`.

If `m^3<=c_0 varpi^2`, the Stevens--de Zeeuw Cartesian-product incidence theorem in the form used by Hu gives

`I(A x A,L) << m^(11/4)`.

Hence

`T^2 <= N_d(A)^2 << m(m^2+m^(11/4)) << m^(15/4)`,

so `m>>T^(8/15)`.

If `m^3>c_0 varpi^2`, then `m>>varpi^(2/3)`. Since `T<=N< X<varpi`, this is stronger than `m>>T^(8/15)`. Thus the displayed bound holds in both cases.

## Lemma 5 — repeated short prime gap in every dyadic block

For all sufficiently large `X`, there is an even integer `d` with `2<=d<=6 log X` for which

`#{j:0<=j<=N-2, q_{j+2}-q_{j+1}=d} >> X/(log X)^2`.

Proof. By the prime number theorem, for all sufficiently large `X`, `N-2 >= X/(3 log X)`. The sum of the `N-2` gaps `q_{j+2}-q_{j+1}` is at most `X`. Therefore at least half of them are at most `6 log X`; otherwise the sum would exceed `3(N-2)log X >= X`. All internal gaps are even. There are at most `3 log X` possible even values up to `6 log X`, so one value occurs at least `(N-2)/(6 log X) >> X/(log X)^2` times.

## Theorem 6 — primorial-prefix residue anti-concentration

There are absolute constants `c>0` and `X_0` such that for every `X>=X_0` and every prime `varpi>2X`,

`|A_X(varpi)| >= c (X/(log X)^2)^(8/15)`.

Proof. Choose `d` by Lemma 5. Each occurrence of that gap gives a distinct transition by Lemma 1, so `N_d(A)>>X/(log X)^2`. Apply Proposition 4.

## Corollary 7 — beyond square root at a comparable prime modulus

For every sufficiently large `X`, choose by Bertrand a prime `varpi` with `2X<varpi<4X`. Then

`|A_X(varpi)| >> varpi^(8/15)/(log varpi)^(16/15)`.

In particular,

`|A_X(varpi)|/sqrt(varpi) >> varpi^(1/30)/(log varpi)^(16/15) -> infinity`.

Thus the increasing primorial-prefix path has a modular value set that exceeds the square-root scale along a prime modulus comparable with the generating dyadic block.

## Epistemic status

- Lemmas 1--3: elementary exact algebra.
- Proposition 4: conditional only on the published Stevens--de Zeeuw incidence theorem, used in exactly the same parameter regime as Hu's arXiv:2608.01781 proof.
- Lemma 5: unconditional consequence of PNT plus telescoping.
- Theorem 6 / Corollary 7: proof-complete modulo line-by-line verification of the quoted Stevens--de Zeeuw hypothesis form.
- Novelty: not certified. Current cold search found adjacent polynomial-product and factorial value-set literature, but no primorial-prefix theorem of this form.

This result has no direct implication for Fortune's conjecture or the selected-centre prime-pair variance frontier.
