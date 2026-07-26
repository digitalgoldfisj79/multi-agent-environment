# Retractions and corrections to the Fortune strategy assessment

**Date:** 2026-07-26
**Branch:** `claude/airy-next-after-circularity-8jlrek`
**Status:** three claims I made are withdrawn; two repository claims are shown false.

A five-route design pass with two independent adversarial reviews per route
(16 agents) overturned part of my own assessment. The corrections below are
the ones I re-verified myself.

## 1. Withdrawn: the window statement is *not* equivalent to Fortune

I stated

> Fortune <=> there is a prime in `(p_n#, p_n# + p_{n+1}^2)`.

Only one direction holds. If `1 < m < p_{n+1}^2` is composite its least prime
factor is `<= sqrt m < p_{n+1}`, hence `<= p_n`, hence divides `p_n#` and
`p_n# + m`. So a prime in the window forces `F_n` prime. **The converse
fails:** Fortune permits `F_n >= p_{n+1}^2` and prime. The window statement is
*strictly stronger* than Fortune.

This matters because "sufficient condition strictly stronger than the target"
is exactly the failure mode that has already consumed several routes in this
repository. Every known approach targets the stronger statement; it must be
labelled as such.

## 2. Withdrawn: Cramer's conjecture does not imply Fortune

I wrote that Fortune "follows immediately from Cramer". It does not.

Admissible offsets are `1` together with the primes in `(p_n, p_{n+1}^2]`, a
Buchstab survivor set at `u = log H / log p_n -> 2`, where `omega(2) = 1/2`
rather than `e^{-gamma} = 0.5615`. The expected count in the window is

\[
e^{\gamma}\omega(2)\frac H{\log N}=\frac{e^{\gamma}}2 p_n=0.8905\log N,
\]

which is about **11% fewer** primes than a generic interval of the same
length: the free primorial sieve is a net *penalty*, not a bonus. The
reciprocal `1/(e^gamma/2) = 2e^{-gamma} = 1.1229` is exactly Granville's
refinement of Cramer's constant. Since Granville conjectures
`limsup gap/(log p)^2 >= 1.1229 > 1`, and primorials are precisely the
highly-divisible centres where that effect is extremal, **Cramer with constant
1 does not give the window at these centres.** Any proof must be local to
primorial centres.

## 3. Withdrawn: the deviation is not `~1.5 sqrt p`, and the `C <= 34` endgame fails

I proposed that since FF-Fortune(p,1) is machine-certified below `p = 1200`,
a bound `deviation <= C sqrt p` with `C <= 34` would close the crown outright,
and reported an observed effective constant `<= 1.05`.

That was read off six primes (`p <= 71`). On the committed 60-prime table
`frontier/d1_data/scripts/N3_checkpoint.json` (`5 <= p <= 293`), which
reproduces my independent census exactly at every overlapping prime, I measure:

| window | mean `max_A dev/sqrt p` | mean `max_A dev/(p-2)` | mean `min_A dev/(p-2)` |
|---|---:|---:|---:|
| `[5,50)` | `1.295` | `0.397` | `0.163` |
| `[50,120)` | `1.650` | `0.186` | `0.080` |
| `[120,200)` | `1.916` | `0.153` | `0.073` |
| `[200,300)` | `2.637` | `0.168` | `0.075` |

Log-log slope of the deviation against `p`: **0.698** (max class), **0.738**
(min class). Not `0.5`. The ratio to `sqrt p` *grows*; the ratio to `p`
*settles* near `0.075`.

So no bound of the form `C sqrt p` is even true, and the proposed endgame is
withdrawn. The correct shape is a sharp-constant statement against `p`, and
the constant is currently unpinned.

## 4. `FRONTIER.md`'s stated target `B(pi) = o(p)` is false, not merely open

Theorem D1.5 already *proves* the degree-1 local factor `(p^2-1)/3`, leading
constant `e/3 = 0.906`, and `D1_ATTACK.md:95` records the relative error
`~ -0.16`. On the proved local factor alone, any true bound
`|Sum_I Lambda - p^4| <= B p^3` forces

\[
B\ \ge\ \left(1-\tfrac e3\right)p\ =\ 0.094\,p .
\]

So `FRONTIER.md` §2 and §5(4)(b) state a sufficient condition that cannot
hold. The target must be restated in sharp-constant form `B <= (1-delta)p`,
with `delta` between `0.094` (proved local factor) and `0.158` (limit of the
committed density fit `0.842 + 0.618/sqrt p`). **The theorem statement cannot
be written down until that constant is pinned.**

## 5. `FRONTIER.md`'s justification of the degree-1 micro-lemma is wrong

`FRONTIER.md:151-153` justifies "no degree-one offset ever works at `d=1`" by
"the affine additive map `T^p - T` is bijective". It is the **zero** map on
`F_p`: `x^p - x = 0` for every `x in F_p`, verified at `p = 5,7,11`.

The lemma is true; the reason is different and simpler. A linear
`m = aT + b` with `a != 0` vanishes at `x = -b/a in F_p`, and so does the
centre, so `T^p - T + m` has a root in `F_p`. This also shows the lemma holds
at every multiple of `T^p - T`.

## 6. The gating question, from the review

At the fixed-arithmetic-class packaging — the `N_A` q-line ledger I have been
measuring — the required Betti constant is `< 1`, below the minimum any Betti
sum can take. If that reading is right, **that packaging admits no
Weil / Lang-Weil / Chebotarev proof in principle**, only an exact cancellation
or congruence theorem. The review further flags that Sawin's Proposition 4.2
may quantify `B(pi)` *per irreducible*, whereas `Lambda`'s `p`-cycle class
function decomposes over `p` hook representations; if the error aggregates,
`B >= p-1` by counting alone and the 4-dimensional route as posed is void.

I have not verified either point against the source. Settling what `B(pi)`
quantifies in arXiv:1809.05137 Prop 4.2 is a half-day check that determines
whether the crown has a well-posed target at all, and it should be done before
any further Betti or census effort.

## 7. What survives

- The ledger, the census, and the reconciliation at `p = 11..29` (unchanged).
- The Airy boulder remains retired: the transported contribution is
  `O(p^{3/2})` against a `p^2` scale.
- The measured deviation is `o(p)` empirically, so the crown is very likely
  true; what is withdrawn is my claim about *which bound shape would prove it*.
