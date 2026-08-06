# D6 — asymptotic-sieve and switching audit

## Row sequence

For a fixed centre `j`, define

\[
a_{j,n}=1_{\ell_j<n-P_j\le H}
1_{\mathbb P}(n-P_j).
\]

Detecting prime values of `n` in this sequence is exactly detecting the prime pairs counted by `Z_j`.

For a modulus `d`, the divisor sum is

\[
A_j(d)=
\sum_{\ell_j<m\le H\atop m\text{ prime}}
1_{d\mid P_j+m}.
\]

Thus the basic remainder problem is distribution of primes `m` in the single progression

\[
m\equiv-P_j\pmod d
\]

inside an interval of length `H`.

## Friedlander–Iwaniec asymptotic sieve

The asymptotic sieve breaks the parity barrier only after adding an extra analytic axiom, implemented as a bilinear-form hypothesis in addition to classical divisor-sum information. It does not manufacture that input.

For the present row sequence, a direct application would require:

1. row-uniform divisor-sum asymptotics `A_j(d)=g_j(d)A_j(1)+r_j(d)`;
2. an averaged remainder estimate strong enough to retain a single selected row;
3. the parity-breaking bilinear hypothesis for the same row-local sequence.

The first factors relevant to complete coverage satisfy

\[
d>\ell_j>\sqrt H.
\]

At those moduli, the variable interval contains fewer than `sqrt(H)` possible representatives and can contain at most `H/d+1` members of a residue class. No inherited theorem supplies the required row-uniform prime distribution or bilinear estimate in this post-level range.

Aggregating over `j` does not repair the missing hypothesis: D4 shows that fixed-order aggregate data can preserve a failed row, and the programme has no selector inequality converting an averaged asymptotic-sieve conclusion into one-row resolution.

## Weighted switching

Modern weighted switching arguments assume usable levels of distribution in both the original and switched coordinates and are designed to detect a prime together with an almost-prime. In the present geometry:

- the original least factor already begins beyond `sqrt(H)`;
- switching `P_j+m=rs` leaves the additive variable `m=rs-P_j` in a length-`H` strip while the factors range on the exponential output scale;
- no positive distribution level has been established for the switched row sequence;
- an almost-prime output is insufficient, because candidate collapse requires an actual prime output.

Accordingly, switching does not yield a verified theorem at the required one-row margin.

## Buchstab variants

Recent variants of Buchstab's identity refine iteration rules and sieve-function inequalities. They do not by themselves supply the post-level distribution or parity-breaking input missing here. Since `INT-PFLI` collapses exactly to the lower tail of `Z_j`, a rearrangement of the complete Buchstab partition cannot create new information unless accompanied by a new signed analytic estimate.

## Ruling

The following lanes are closed as direct applications:

- the classical or asymptotic sieve without a new row-uniform bilinear axiom;
- weighted switching without verified levels of distribution in both coordinates;
- finite Buchstab iteration without a new signed post-level estimate;
- any fixed-order moment implementation, by D4–D5.

The exact remaining input is an all-orders or non-moment theorem controlling the adaptive occupancy generating function on the actual increasing primorial centres.

## Primary sources audited

- John Friedlander and Henryk Iwaniec, *Asymptotic sieve for primes*, Annals of Mathematics 148 (1998), 1041–1065, arXiv:math/9811186.
- Kaisa Matomäki and Sebastian Zuniga-Alterman, *Weighted sieves with switching*, arXiv:2405.19063; published in Mathematical Proceedings of the Cambridge Philosophical Society.
- Runbo Li, *A note on variants of Buchstab's identity*, arXiv:2504.07974.
