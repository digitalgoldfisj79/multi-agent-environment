# Independent audit of the 16-agent Fortune proof-strategy synthesis

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Input:** `FORTUNE_PROOF_STRATEGY_SYNTHESIS_20260726.md` supplied outside the repository.  
**Scope:** load-bearing mathematical and strategic claims, with priority given to Sawin's Proposition 4.2, the function-field packaging thresholds, the local-density inference, the claimed generic Betti obstruction, and the function-field window theorem.  
**Status:** **INDEPENDENT AUDIT.** The synthesis contains several valuable corrections, but three of its central function-field conclusions are false or materially overstated. It must not be treated as an authoritative status file without the corrections below.

## 0. Executive ruling

The synthesis is serious and useful as an adversarial review. Its provenance does not make it reliable: the document itself says it was not uniformly verified, and its most consequential unresolved fork can be settled directly from the primary source.

### Correct and valuable

1. The integer window statement is sufficient for Fortune, not equivalent to it.
2. `T^p-T` is the zero function on `F_p`, not a bijection; the degree-one micro-lemma needs the elementary common-root proof.
3. The fixed-class `h=2` packaging is unsuitable for a generic main-minus-absolute-Betti-bound proof: the Sawin exponent makes the required aggregate Betti constant `<1`.
4. `B_+=0` is not the same as uniform `B_A=0`; the nonsquare boundary is nonzero at several committed primes.
5. The finite `N3` table is important evidence that the raw count is not visibly centred at `p-2` with bounded `sqrt(p)` fluctuations.
6. General-purpose complete-intersection Betti bounds remain exponentially too large in the coupled regime `n=q=p`.
7. The integer problem remains far beyond existing pointwise short-interval technology; averaged theorems have the wrong quantifier for an exponentially sparse prescribed sequence.

### False or materially overstated

1. **The catastrophic Sawin fork is false.** `B(pi)` is defined for an arbitrary representation, and Sawin applies it directly to the two direct sums of even and odd hooks that represent `Lambda`. There is no automatic lower bound of one Betti number per hook and no counting-only conclusion `B>=p-1`.
2. **The exact rootless-tail factor does not prove `B(pi)=o(p)` false.** It is an exact local exclusion count and a compelling singular-series heuristic, not an asymptotic formula for the irreducible count or the von Mangoldt sum.
3. **The full `h=4` theorem can already be stated without pinning a density constant.** The exact sufficient target is an aggregate hook Betti bound `B_Lambda<=p-1`. Whether the observed density tends to `e/3`, `0.842`, or another constant is not needed to state that theorem.
4. **The claimed Wan--Zhang matching lower bound is not a lower bound for this Fortune variety.** It concerns a worst-case class in a general family, so it rules out generic uniform technology, not a structure-specific collapse here.
5. **Relocating the local factor into the main term is not bookkeeping.** It requires a new cohomological or asymptotic theorem identifying an actual top-weight constituent. Without that theorem, the proposed recentering is merely the original count problem in different notation.
6. **A census to `p=400--500` cannot pin an asymptotic constant.** It can discriminate finite-range models and discover structure, but it cannot establish the limiting main term.

The correct verdict is therefore not “the geometric packaging may be void.” The full four-parameter aggregate packaging is valid and sharply stated, but proving its aggregate Betti bound remains a major structure-specific problem.

## 1. Primary-source audit of Sawin's `B(pi)`

Reference: Will Sawin, *Square-root cancellation for sums of factorization functions over short intervals in function fields*, arXiv:1809.05137v2.

### 1.1 Definition

Sawin's Definition 4.1 begins:

> For `pi` a representation of `S_n`, let `B(pi)=...`.

There is no irreducibility hypothesis. Proposition 4.2 is likewise stated for an arbitrary representation `pi`.

Moreover, the definition is compatible with direct sums:

\[
B(\pi_1\oplus\pi_2)=B(\pi_1)+B(\pi_2),
\]

because it is a sum of dimensions of invariant cohomology groups.

### 1.2 What Sawin does for `Lambda`

In the proof of Corollary 4.7 Sawin uses

\[
\Lambda
=
\sum_i(-1)^iF_{\wedge^i\mathrm{std}}
=
F_{\pi_+}-F_{\pi_-},
\]

where

\[
\pi_+=\bigoplus_{i\ \mathrm{even}}\wedge^i\mathrm{std},
\qquad
\pi_-=\bigoplus_{i\ \mathrm{odd}}\wedge^i\mathrm{std}.
\]

He explicitly observes that each is a sum of distinct irreducibles and hence a subrepresentation of the regular representation. Corollary 4.4 is then applied directly to each aggregate representation.

Therefore the synthesis's proposed dichotomy

> if `B` is per irreducible, the `p-1` nontrivial hooks force aggregate `B>=p-1`

is invalid. Even if one decomposes the direct sums, a nonzero representation does not force its corresponding isotypic compactly supported cohomology to have dimension at least one. The relevant term can vanish. Counting representation summands is not a lower bound for `B`.

### 1.3 Correct aggregate object

Define

\[
B_\Lambda=B(\pi_+)+B(\pi_-).
\]

This is the exact nonnegative integer controlling the triangle-inequality application of Proposition 4.2 to the von Mangoldt function.

It is this aggregate object—not a hypothetical per-hook minimum—that the full function-field crown programme must control.

## 2. Exact `h=4` packaging threshold

Set

\[
n=q=p,
\qquad h=4,
\qquad m=n-h=p-4,
\]

and take the short interval centred at `T^p-T`:

\[
\mathcal I_4=
\{T^p-T+aT^3+bT^2+cT+d:(a,b,c,d)\in F_p^4\}.
\]

Sawin's exponent is

\[
\frac12\left(
 n-m+\left\lfloor\frac np\right\rfloor
 -\left\lfloor\frac mp\right\rfloor+1
\right)
=
\frac12(4+1-0+1)=3.
\]

Thus Proposition 4.2 gives

\[
\boxed{
\left|
\sum_{f\in\mathcal I_4}\Lambda(f)-p^4
\right|
\le B_\Lambda p^3.
}
\]

### 2.1 Exact weighted-count identity

Because `p` is prime, a degree-`p` prime power is either:

1. an irreducible polynomial of degree `p`, carrying von Mangoldt weight `p`; or
2. the `p`-th power of a monic linear polynomial.

Inside this interval the second family is exactly

\[
(T-a)^p=T^p-a,
\qquad a\in F_p,
\]

and each carries weight one. Therefore, if `I_4` denotes the number of irreducible polynomials in the interval,

\[
\boxed{
\sum_{f\in\mathcal I_4}\Lambda(f)=pI_4+p.
}
\]

The crown condition is

\[
I_4>p-1,
\]

which is equivalent to

\[
pI_4+p>p^2.
\]

The Sawin lower bound closes this whenever

\[
p^4-B_\Lambda p^3>p^2,
\]

i.e.

\[
B_\Lambda<p-\frac1p.
\]

Since `B_Lambda` is an integer, the exact clean sufficient theorem is

\[
\boxed{B_\Lambda\le p-1.}
\]

This is the correct geometric crown target. It is linear and sharp at the scale relevant to this method. It does not require `B_Lambda=o(p)`, and it does not require an empirical limiting density to be known first.

## 3. The packaging table: what survives

For general interval dimension `h`, with `n=q=p` and `m=p-h`, Sawin's exponent is

\[
\frac{h+2}{2}
\]

as long as `1<=h<p`. Comparing `B p^{(h+2)/2}` with main term `p^h` gives the sufficient scale

\[
B<p^{h/2-1}.
\]

Hence:

| packaging | triangle-bound requirement | audit ruling |
|---|---:|---|
| full `h=4` | `B<p` | valid and live; exact integer target `B_Lambda<=p-1` |
| cubic-averaged `h=3` | `B<sqrt(p)` | valid but harder normalization/projector details must be stated |
| fixed-class `h=2` | `B<1` | generic absolute-Betti route cannot work unless the relevant aggregate cohomology vanishes |

The synthesis is therefore right that the fixed-class q-line packaging is self-defeating for a straightforward Weil-plus-total-Betti argument. It is wrong to propagate that conclusion upward to the full `h=4` aggregate interval.

The q-line remains valuable for exact identities, arithmetic projectors, congruences and structural diagnostics. It should not be treated as the most favourable packaging for an absolute cohomological estimate.

## 4. Local factor and deviation: evidence is not a theorem

`D1_ATTACK.md`, Theorem D1.5, proves an exact degree-one local statement: for each relevant slice, the number of `(c,d)` pairs whose cubic tail has no `F_p` root is

\[
\frac{p^2-1}{3}.
\]

After the standard independent-local-factor heuristic, this predicts a leading density involving

\[
\frac e3\approx0.906.
\]

The committed finite data are consistent with a persistent linear deficit from the naive main term. That is important evidence and should affect strategy.

It does **not** prove any of the following:

\[
I_4\sim\frac e3p^3,
\qquad
\sum_{f\in\mathcal I_4}\Lambda(f)\sim\frac e3p^4,
\qquad
B_\Lambda\ge\left(1-\frac e3\right)p
\quad\text{for all large }p.
\]

The first implication would require control of all higher-degree factor obstructions and their correlations. The exact rootless count only removes linear factors.

The third implication additionally conflates two distinct quantities:

- the observed normalized Frobenius trace defect
  \[
  \frac{|\sum\Lambda-p^4|}{p^3};
  \]
- the nonnegative total Betti dimension `B_Lambda` that bounds that trace.

Finite data give lower bounds on `B_Lambda` at those individual primes through the trace inequality, but do not prove an asymptotic lower bound.

Accordingly:

- `B_Lambda=o(p)` is strongly disfavoured by current data;
- it has **not** been disproved by Theorem D1.5;
- and it is not the necessary target in any case, because `B_Lambda<=p-1` suffices.

## 5. Why “move the local factor into the main term” is new mathematics

The synthesis proposes writing

\[
\sum\Lambda=\sigma_pp^4+\text{residual}
\]

and then bounding the residual on a smaller scale.

This is legitimate only after proving one of:

1. an asymptotic singular-series theorem for the full irreducible count;
2. a cohomological decomposition isolating a top-weight constituent with trace `sigma_p p^4`;
3. an exact inclusion-exclusion or mass formula separating the local obstruction from the oscillatory remainder.

None follows from the rootless-tail count alone. Without such a theorem, choosing `sigma_p` from finite data or a heuristic and calling the remainder an error is a tautological recentering.

Thus Step 2 of the synthesis is not bookkeeping. It is potentially a major theorem, and may be essentially as hard as the crown.

## 6. Audit of the Wan--Zhang claim

Wan and Zhang's 2025 paper gives general upper bounds for total Betti numbers of affine varieties/exponential sums and discusses lower bounds showing that their general dependence is close to optimal in a worst-case class.

That supports the strategic conclusion:

> no generic complete-intersection Betti theorem is likely to turn an exponential `p^{O(p)}` bound into the required linear bound for every family.

It does **not** show that the specific Fortune interval variety has Betti number at least `(d-1)^n`, nor that a structure-specific linear collapse is impossible. The synthesis's wording must distinguish a worst-case lower bound for a class from a lower bound on this object.

The Pascal, hook and quantum-bar structure is precisely why a special collapse remains logically possible.

## 7. The function-field window theorem

The synthesis contains an internal contradiction: two adversarial reviewers downgrade the window route to “needs major breakthrough,” while Step 6 says it is a short Weil-RH argument.

The mathematical core of Step 6 appears correct.

Let `P_d` have degree `n`, and vary offsets `m` with `deg m<h`. Reversal turns the short interval into one congruence class for the even characters modulo a power of `T`. Character orthogonality and the function-field Riemann hypothesis give a weighted prime-polynomial estimate of the form

\[
\sum_{\deg m<h}\Lambda(P_d+m)
=
q^h+O(nq^{n/2}),
\]

uniformly in the centre, with harmless convention-dependent constants. Prime-power contamination is also `O(nq^{n/2})`.

Therefore positivity of an irreducible contribution follows once

\[
q^h\gg nq^{n/2},
\]

i.e.

\[
\boxed{h>\frac n2+\log_qn+O(1).}
\]

Combining this with the elementary reduction that a reducible offset coprime to `P_d` has degree at least `2d+2` gives the genuine theorem shape:

> the minimal offset is irreducible, or has degree in
> \[
> [\,2d+2,\ n/2+\log_qn+O(1)\,].
> \]

For `d=1`, `q=p`, `n=p`, this is a centre-preserving window of degree approximately `p/2`, far above the crown's degree-three target but still a valid unconditional Fortune-type result.

The exact modulus convention and constants should be written carefully, but no major new theorem appears necessary. The appendix downgrade is unsupported unless the reviewers were evaluating a stronger statement.

## 8. Integer side: serious but not a theorem-level closure

The following points are sound:

1. A prime in the interval of length `p_{n+1}^2` is a sufficient condition for Fortune, not an equivalent reformulation.
2. Current pointwise prime-gap technology is enormously too weak for a `(log N)^2` interval at a prescribed primorial centre.
3. Almost-all short-interval theorems do not control an exponentially sparse prescribed sequence unless their exceptional set is empty.
4. The Baker--Harman--Pintz pointwise exponent `0.525` and the newer Guth--Maynard asymptotic exponent `17/30` remain polynomial-window results, nowhere near polylogarithmic length.
5. Maier's phenomenon warns that a uniform short-interval asymptotic at logarithmic scales is false and that primorial moduli are not generic.

The synthesis's strategic recommendation to stop attacking integer Fortune with the present toolkit is reasonable.

However, phrases such as “categorically dead,” “no sieve can do this,” or “Maier rules it out” are not mathematical no-go theorems for the prescribed primorial centres. Maier obstructs uniform or naive generic asymptotics; a centre-specific identity or new transference principle is not logically excluded.

The integer section should therefore be labelled a technology audit and resource-allocation verdict, not a proof of impossibility.

## 9. Revised programme

### Phase A — correct the record

1. Replace the standing `B(pi)=o(p)` formulation by the exact aggregate sufficient target
   \[
   B_\Lambda\le p-1.
   \]
2. Retain the finite-density measurements as empirical evidence, not a proof of a limiting linear defect.
3. Correct the degree-one micro-lemma and the one-way integer implication.
4. Record explicitly that the q-line `h=2` package is not the favourable package for an absolute Betti estimate.

### Phase B — write the theorem that is already available

Write the centre-preserving function-field window theorem with

\[
h>n/2+\log_qn+O(1).
\]

This is useful publication-grade context, but not progress from degree `p/2` to degree three.

### Phase C — return to the full `h=4` aggregate geometry

Construct the actual aggregate objects

\[
\pi_+=\bigoplus_{i\ even}\wedge^i\mathrm{std},
\qquad
\pi_-=\bigoplus_{i\ odd}\wedge^i\mathrm{std},
\]

and target

\[
B(\pi_+)+B(\pi_-)\le p-1.
\]

The Pascal oscillator and terminal quantum-bar theorems are potentially relevant here because they predict massive cancellation/vanishing across the aggregate hook complex. They should not be forced through the fixed-class q-line packaging unless the comparison theorem naturally lands there.

### Phase D — use the q-line only for mechanisms it can support

Continue q-line work only where it supplies:

- exact projector identities;
- a congruence or parity certificate;
- a canonical transport comparison;
- direct global trace cancellation not obtained by summing fibrewise absolute bounds.

Do not seek a generic `B<1` theorem by ordinary Weil estimates.

### Phase E — singular-series work must earn its main term

Before recentering at `e/3` or another constant, prove a genuine local-to-global theorem or identify the corresponding top-weight cohomological constituent. Further census work should be tied to discriminating explicit structural models, not advertised as pinning an asymptotic constant.

## 10. Final ruling

The synthesis materially improves the strategic picture, especially on the integer/function-field separation, the fixed-class packaging penalty and the need to treat empirical linear drift seriously.

Its central proposed gate, however, was misread:

\[
\boxed{
\text{Sawin already packages }\Lambda\text{ using the aggregate even/odd hook representations.}
}
\]

Therefore the full `h=4` route is not void. Its correct theorem-level target is

\[
\boxed{B(\pi_+)+B(\pi_-)\le p-1.}
\]

That target remains extremely difficult, but it is precise, internally consistent and does not depend on pinning a heuristic density constant.

The revised scientific position is:

- integer Fortune: strategically out of reach with current methods, not formally impossible;
- function-field window: apparently provable by standard RH machinery and should be written separately;
- function-field crown: live at the aggregate `h=4` level, with the actual wall an exponential-to-linear aggregate hook-cohomology collapse;
- fixed-class q-line: valuable for exact cancellation and congruence, not for a generic absolute Betti bound;
- singular-series constant: important empirical hypothesis, not yet a proved main term.
