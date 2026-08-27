# Hostile proof audit — Primorial Incidence Transfer v0.1

Date: 27 August 2026
Disposition: `PASS_AFTER_ONE_OFF_BY_ONE_REPAIR`

## 1. Domain and nonzero denominators — PASS

The modulus `varpi` is prime and exceeds `2X`. Every prime factor of `B_X` and every dyadic generator `q_i` is therefore strictly smaller than `varpi`, so every prefix `P_j` lies in `F_varpi^*`. All divisions by `P_j`, `a`, `b`, and the ratios `b/a` are legitimate.

For `T_{a,d}^{-1}(u)=a^2/(u-da)`, the inverse is asserted only on the image of `T_{a,d}`. If `u=T_{a,d}(x)`, then `u-da=a^2/x !=0`.

## 2. Exact recurrence — PASS

From `P_{j+1}=q_{j+1}P_j` and `P_{j+2}=q_{j+2}P_{j+1}`, with `g_j=q_{j+2}-q_{j+1}`,

`g_j P_{j+1}+P_{j+1}^2/P_j=(q_{j+2}-q_{j+1})P_{j+1}+q_{j+1}P_{j+1}=P_{j+2}`.

This is an integer identity before reduction modulo `varpi`.

## 3. Distinct transition pairs — PASS

If two selected pairs `(P_j,P_{j+1})` and `(P_k,P_{k+1})` coincide modulo `varpi`, their coordinate ratios give `q_{j+1}=q_{k+1} (mod varpi)`. Both primes lie in `[X,2X]` and are strictly below `varpi`, so equality modulo `varpi` is ordinary equality and `j=k`.

Thus each occurrence of the selected prime gap contributes a genuinely distinct transition to `N_d(A)` even when the prefix values themselves have collisions.

## 4. Affine composition — PASS

Solving `u=da+a^2/x` gives `x=a^2/(u-da)`. For `r=b/a`, substitution yields

`T_{b,d}(T_{a,d}^{-1}(u))=r^2 u+d a r(1-r)`.

The calculation has been independently checked symbolically and in every finite panel.

## 5. Line multiplicity — PASS

A line representation has slope `r^2`. Over an odd prime field there are at most two values of `r` for a fixed slope. For a nonidentity representation `r!=1` and `r!=0`; with `d!=0`, the intercept uniquely recovers

`a=tau/[d r(1-r)]`.

Hence every nonidentity line has multiplicity at most two.

For the identity line, slope one gives `r=+/-1`. The zero-intercept condition excludes `r=-1` because `d`, `a`, and `2` are nonzero, leaving only `r=1`, i.e. `a=b`.

## 6. Cauchy--Schwarz to incidence count — PASS

Let `R(x)=#{a in A:T_{a,d}(x) in A}`. Then

`N_d(A)^2 <= |A| sum_x R(x)^2`.

Expanding the second moment produces `sum_{a,b}M(a,b)`. For fixed `(a,b)`, the injectivity of `T_{a,d}` maps each admissible common input `x` to a distinct incidence point `(u,v)` in `A x A` on `ell_{a,b,d}`. Thus `M(a,b)` is bounded by the incidence contribution of that line.

There are `m` diagonal pairs and each contributes at most `m`, giving `m^2`. Every nonidentity line is represented at most twice.

## 7. Stevens--de Zeeuw hypotheses — PASS

Use Theorem 4 of Stevens--de Zeeuw, *An Improved Point-Line Incidence Bound Over Arbitrary Fields* (arXiv:1609.06284), with Cartesian product `A x A` and exactly `n=m^2` distinct affine lines. If the naturally arising line set is smaller, add arbitrary nonvertical lines; this can only increase the incidence count and there are at least `m^2` available because `m<varpi`.

The theorem's first size condition becomes

`|A||A|^2=m^3 <= n^3=m^6`,

which is automatic for `m>=1`.

Its characteristic condition becomes

`|A| n = m^3 << varpi^2`.

Under this condition,

`I(A x A,L) << m^(3/4)m^(1/2)(m^2)^(3/4)+m^2 << m^(11/4)`.

If the characteristic condition fails, `m >> varpi^(2/3)`, already stronger than the target `m >> T^(8/15)` because `T<varpi` and `2/3>8/15`.

No incidence-theorem regime is left untreated.

## 8. Repeated-gap population — PASS AFTER BOOKKEEPING REPAIR

The initial draft referred to `N-2` internal gaps. With `N` primes there are `N-1` gaps; the theorem statement indexed by `j=0,...,N-2` also has `N-1` values. This was an off-by-one bookkeeping error only and has been corrected.

PNT gives `N-1 >= X/(3 log X)` for sufficiently large `X`. The total of all internal gaps is `q_N-q_1<X`. Therefore at least half have length at most `6 log X`. Since the gaps are even and there are at most `3 log X` possible even values in this range, one gap occurs at least

`(N-1)/(6 log X) >> X/(log X)^2`

times.

No bounded-gap conjecture, Polignac conjecture, twin-prime input, or short-interval prime theorem beyond the ordinary PNT is used.

## 9. Exponent arithmetic — PASS

With transition population `T`, Cauchy plus incidence gives

`T^2 << m^(15/4)`.

Therefore `m >> T^(8/15)`. Substituting `T >> X/(log X)^2` gives

`m >> X^(8/15)/(log X)^(16/15)`.

For `2X<varpi<4X`, this is

`m >> varpi^(8/15)/(log varpi)^(16/15)`.

Relative to `sqrt(varpi)`, the ratio is

`varpi^(1/30)/(log varpi)^(16/15) -> infinity`.

So the corollary is genuinely beyond square-root asymptotically despite the logarithmic loss.

## 10. Scope / implication audit — PASS

The theorem concerns the number of distinct residues attained by the deterministic increasing primorial-prefix path modulo an auxiliary prime. It does not:

- estimate the signed reciprocal-frame residual;
- prove a source-to-frame transference theorem;
- give selected-centre prime-pair covariance;
- prove a prime in every Fortune interval;
- prove Fortune's conjecture.

The integer Fortune mainline therefore remains closed.

## Terminal proof disposition

`THEOREM_PROOF_COMPLETE_RELATIVE_TO_STANDARD_PUBLISHED_INPUTS`

The proof uses only elementary algebra, PNT, Bertrand's postulate for the comparable-modulus corollary, and the published Stevens--de Zeeuw incidence theorem. Computational panels are independent regression evidence and are not load-bearing.
