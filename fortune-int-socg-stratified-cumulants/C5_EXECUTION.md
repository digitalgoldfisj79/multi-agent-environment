# C5 execution — primorial-walk orbit

**Status:** `PRIME_MODULUS_LARGE_SIEVE_PROVED; COMPOSITE_EXTENSION_OPEN`

Let one stratum contain `n` consecutive terminal primes and write its primorial centres as `P_0,...,P_{n-1}`. For every prime modulus `q>2X`, `q` divides none of the terminal multipliers and

\[
P_k\equiv P_j\pmod q
\iff
q\mid\prod_{r=j+1}^k\ell_r-1.
\]

If `d=k-j`, then

\[
0<\prod_{r=j+1}^k\ell_r-1<(2X)^d.
\]

Hence this integer has fewer than `d` distinct prime divisors exceeding `2X`.

## Exact prime-modulus large-sieve lemma

For arbitrary complex coefficients `a_j`, define

\[
S_q(c)=\sum_{j=0}^{n-1}a_j e(cP_j/q).
\]

Additive-character orthogonality and the collision count above give, for `Q>2X`,

\[
\boxed{
\sum_{\substack{2X<q\le Q\\q\ \mathrm{prime}}}
\sum_{c\bmod q}|S_q(c)|^2
\le
\left(
\sum_{\substack{2X<q\le Q\\q\ \mathrm{prime}}}q
+Qn^2
\right)
\sum_j|a_j|^2.
}
\]

Proof: the diagonal contributes the first term. For `j<k`, the total weight of colliding prime moduli is at most `Q(k-j)`. Then

\[
2\sum_{j<k}(k-j)|a_ja_k|
\le
n^2\sum_j|a_j|^2.
\]

At the natural local range `Q=X^2` and

\[
n\asymp X/(\log X)^{5/2},
\]

the `Qn^2` collision term is below the diagonal prime-modulus term. Thus the selected primorial residues have the expected square-root average energy over prime moduli and all additive frequencies.

`verify_prime_modulus_walk_large_sieve.py` checks Parseval, exact collision counts and the pair budget on finite panels.

## Remaining orbit theorem

Prime-modulus collision is not the C5 obstruction. Source decompositions and all-orders connected products introduce squarefree composite moduli and correlated coefficient families. A divisor of

\[
\prod_{r=j+1}^k\ell_r-1
\]

can have many composite combinations even when the number of large prime factors is at most `k-j`. Extending the lemma with the required coefficient weights and conductor ranges is the unresolved `INT-PWOC` component.
