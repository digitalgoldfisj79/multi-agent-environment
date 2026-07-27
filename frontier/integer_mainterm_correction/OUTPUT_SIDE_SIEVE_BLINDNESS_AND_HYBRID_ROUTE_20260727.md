# Output-side sieve blindness and the hybrid corrected route

Date: 27 July 2026  
Status: exact no-go theorem proved; symmetric two-sided truncation removed from the critical path.

## The elementary blindness theorem

Let

\[
P_j=\prod_{q\le \ell_j}q
\]

and suppose that

\[
\ell_j<m<\ell_{j+1}^2,
\qquad P_j+m\text{ is a candidate output}.
\]

Candidate collapse says that any successful offset in this range is prime. For every such prime offset `m` and every prime `q<=ell_j`,

\[
P_j+m\equiv m\not\equiv0\pmod q.
\]

Hence

\[
\boxed{(P_j+m,P_j)=1.}
\]

This holds whether `P_j+m` is prime or composite.

Therefore every sieve statistic depending only on divisibility by primes already contained in the primorial is constant on the candidate-output set. In particular, no cumulative Mobius detector supported only on products of primes at most `ell_j` can distinguish a prime output from a composite output.

## Consequence for the exact two-sided divisor frame

The exact frame

\[
T_j(H)=
\sum_{d,e}\mu(d)\mu(e)\log d\log e\,C_j(d,e;H)
\]

is valid, but a symmetric polynomial-range truncation is not a viable pointwise reduction:

- the offset variable has size `m<=H asymp X^2`, so its divisor structure can be exposed at polynomial scale;
- the output variable has size `P_j+m=exp(Theta(X))` and is already free of every prime up to `ell_j asymp X`;
- an output-side truncation confined to the primorial prime set is exactly blind;
- taking the output divisor range large enough to decide primality reintroduces exponential conductor.

This explains why the one-sided reciprocal architecture could not supply the missing prime-offset condition and why simply adding a second copy of the same shell cannot repair it.

## Corrected hybrid route

The only presently justified route is asymmetric:

1. retain the exact offset-prime condition, or expand it using a divisor identity at scale `H`;
2. retain the output von Mangoldt function as a genuine prime observable rather than replacing it by a small-prime sieve density;
3. subtract the primorial prime-pair singular-series main term before applying absolute values;
4. average over the primorial block only after the two prime variables remain coupled.

The first positive target is the corrected block first moment

\[
\sum_{j<N}T_j(H)
=H\sum_{j<N}\mathfrak S(P_j)
+o(NH\log X),
\]

or, in unweighted form,

\[
\sum_{j<N}Z_j(H)
\sim\sum_{j<N}\lambda_j(H).
\]

The all-centres target remains the corrected covariance estimate

\[
\sum_{j<N}|Z_j(H)-\lambda_j(H)|^2
\ll NX L(X),
\qquad L(X)=o(\log X).
\]

Its off-diagonal expansion is an aggregated four-linear-form prime correlation. No theorem in Papers I--IV currently supplies that estimate.

## Research ruling

Closed as primary routes:

- recentering the old one-output detector at `H`;
- positive density replacement for the offset-prime condition;
- an output sieve using only primes in the primorial;
- a symmetric polynomial-scale two-sided divisor truncation;
- proceeding directly to HTE4 or Paper IV derandomisation before a corrected source bridge exists.

Open:

- a hybrid sparse-centre prime-pair first moment;
- an aggregated four-prime covariance theorem;
- a signed identity or inequality connecting either target to a tractable deterministic kernel.

This is the current theorem-level stopping point of the corrected integer programme.
