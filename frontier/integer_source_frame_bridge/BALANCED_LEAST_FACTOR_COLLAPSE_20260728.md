# Balanced least-factor collapse

Date: 28 July 2026  
Status: exact candidate classification and prime-power bound proved; balanced certificate estimate open.

## 1. Candidate range

Let

\[
P_j=\prod_{r\le p_j}r
\]

be a primorial centre, let `p_j^+` be the next prime, and choose

\[
p_j<H<(p_j^+)^2.
\tag{1.1}
\]

Write

\[
\mathcal P_j(H)=\{p:p_j<p\le H,\ p\text{ prime}\}.
\]

For `p in mathcal P_j(H)` put

\[
n_{j,p}=P_j+p.
\]

Since `gcd(P_j+p,P_j)=1`, every prime factor of `n_{j,p}` exceeds `p_j`.

## 2. Unique least-factor certificate

### Theorem 2.1

For every `p in mathcal P_j(H)`, exactly one of the following holds.

1. `n_{j,p}` is prime.
2. There is a unique prime `q` and a unique integer `k` such that
   
   \[
   \boxed{
   n_{j,p}=qk,
   \qquad
   p_j<q\le\sqrt{n_{j,p}},
   \qquad
   P^-(k)\ge q.
   }
   \tag{2.1}
   \]

Here `P^-(k)` denotes the least prime factor of `k`, with `P^-(1)=+infinity`.

### Proof

If `n_{j,p}` is composite, take `q=P^-(n_{j,p})` and `k=n_{j,p}/q`.
The roughness observation gives `q>p_j`.  The least factor of a composite integer
is at most its square root, and every prime factor of `k` is at least `q`.
Uniqueness follows from the uniqueness of the least prime factor.  Conversely,
(2.1) is a nontrivial factorisation, so the output is composite.  \(\square\)

Thus the composite certificate is positive and unique; no Möbius subset
multiplicity remains.

## 3. Small and balanced certificates

Split the least factor at the physical scale `H`.

### Small certificate

For `p_j<q<=H`, all certified offsets are

\[
p=qk-P_j\in\mathcal P_j(H),
\qquad
k\ge q,
\qquad
P^-(k)\ge q.
\tag{3.1}
\]

A fixed `q` may produce several offsets because the progression spacing is at most
`H`.

### Balanced certificate

For `q>H`, the interval length is smaller than the modulus.  Define

\[
k_j(q)=\left\lceil\frac{P_j}{q}\right\rceil,
\qquad
p_j(q)=qk_j(q)-P_j.
\tag{3.2}
\]

### Corollary 3.1

The large least-factor certificate is exactly

\[
\boxed{
H<q\le\sqrt{P_j+H},
\quad q\text{ prime},
\quad p_j(q)\in\mathcal P_j(H),
\quad P^-(k_j(q))\ge q.
}
\tag{3.3}
\]

Moreover

\[
q\le k_j(q),
\]

so both factors are greater than `H`.  The unresolved large sector is therefore
balanced; the dangerous top-divisor range with a cofactor below `H` does not occur
when one routes to the least prime factor.

For fixed `q>H`, the shrinking-target theorem bounds the number of primorial
centres for which `p_j(q)` lies in the physical interval.  The primality and
least-factor conditions in (3.3) are additional restrictions.

## 4. Exact weighted prime-output identity

Let `b_p` be arbitrary complex weights on `mathcal P_j(H)`.  Define

\[
\begin{aligned}
\mathcal C_{j,\mathrm{small}}(b)
={}&
\sum_{p_j<q\le H\atop q\text{ prime}}
\sum_{k\ge q\atop qk-P_j\in\mathcal P_j(H)}
 b_{qk-P_j}\,\mathbf1_{P^-(k)\ge q},\\
\mathcal C_{j,\mathrm{bal}}(b)
={}&
\sum_{H<q\le\sqrt{P_j+H}\atop q\text{ prime}}
 b_{p_j(q)}
 \mathbf1_{p_j(q)\in\mathcal P_j(H)}
 \mathbf1_{P^-(k_j(q))\ge q}.
\end{aligned}
\tag{4.1}
\]

### Theorem 4.1

One has exactly

\[
\boxed{
\sum_{p\in\mathcal P_j(H)}
 b_p\,\mathbf1_{P_j+p\text{ prime}}
=
\sum_{p\in\mathcal P_j(H)}b_p
-
\mathcal C_{j,\mathrm{small}}(b)
-
\mathcal C_{j,\mathrm{bal}}(b).
}
\tag{4.2}
\]

### Proof

Apply Theorem 2.1 offset by offset.  Every composite output is counted once by
its unique least prime factor, in exactly one of the two ranges.  \(\square\)

This is the exact parity-breaking identity behind the reduced Fortune problem.
The small part has one polynomial prime modulus.  The balanced part is a
one-point prime-modulus orbit with a rough complementary factor.

## 5. Proper prime powers are negligible for von Mangoldt detectors

The identity (4.2) concerns the prime indicator.  A von Mangoldt detector also
sees proper prime powers.

### Theorem 5.1

For every sufficiently large primorial centre,

\[
\boxed{
\sum_{2\le m\le H\atop P_j+m=r^a,\ a\ge2}
\Lambda(P_j+m)
\ll X\log X=o(H),
}
\tag{5.1}
\]

uniformly in the dyadic block `p_j asymp X`.  If each offset is additionally
weighted by at most `O(log H)`, the bound is

\[
O(X(\log X)^2)=o(H).
\tag{5.2}
\]

### Proof

Any base `r` is greater than `p_j`, since a prime divisor at most `p_j` would also
divide `P_j`.  Hence the exponent satisfies

\[
a\le\frac{\log(P_j+H)}{\log p_j}=O(X/\log X).
\]

For each fixed `a>=2`, the gap between consecutive `a`th powers near `P_j` is at
least a constant multiple of `sqrt{P_j}`, which exceeds `H`; therefore the
interval contains at most one `a`th power.  Its von Mangoldt weight is

\[
\log r=\frac1a\log(r^a)\ll X/a.
\]

Summing over `a` gives `O(X log X)`.  Multiplication by `O(log H)` gives (5.2).
\(\square\)

Thus proper powers cannot supply the positive main term required by the Fortune
detector.

## 6. Computational diagnostic

Exact factorisation over complete finite candidate panels shows that the balanced
sector is not numerically negligible.  In the tested blocks through `X=37`, the
fraction of prime offsets producing composites with every prime factor greater
than `H` ranges from roughly 12% to 50%, depending on the centre.  Proper prime
powers did not occur in the panel.

This is empirical evidence only.  Its strategic implication is that a proof which
controls only the small-modulus sector cannot close Fortune.

## 7. Revised load-bearing estimate

The remaining analytic theorem can now be stated without Möbius ambiguity:
control the centred fluctuation of the unique certificate sum

\[
\mathcal C_{j,\mathrm{small}}+
\mathcal C_{j,\mathrm{bal}}
\]

at a scale strong enough that no centre can lose its full expected prime-output
mass.

The balanced term is the new critical object:

\[
\boxed{
\sum_{H<q\le\sqrt{P_j+H}\atop q\text{ prime}}
 b_{q\lceil P_j/q\rceil-P_j}
 \mathbf1_{q\lceil P_j/q\rceil-P_j\text{ prime}}
 \mathbf1_{P^-(\lceil P_j/q\rceil)\ge q}.
}
\tag{7.1}
\]

It is a fixed-complexity, balanced, least-prime-factor orbit sum.  It is not the
old unweighted frame and it contains no growing Heath--Brown depth.

## 8. Boundary

Proved:

1. unique least-prime-factor classification;
2. exact split into small and balanced certificates;
3. absence of the top-divisor range in the least-factor routing;
4. exact weighted identity (4.2);
5. negligible proper-prime-power contribution.

Open:

1. the centred small-certificate estimate;
2. the balanced orbit estimate (7.1);
3. the joint all-centres variance theorem;
4. Fortune's conjecture.
