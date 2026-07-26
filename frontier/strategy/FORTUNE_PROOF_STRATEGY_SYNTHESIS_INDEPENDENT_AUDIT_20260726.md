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
7. Integer Fortune is far beyond current pointwise short-interval technology.

### False or overstated

1. The proposed catastrophic ambiguity in Sawin's `B(pi)` is not real. `B(pi)` is defined for arbitrary representations, and Sawin applies it directly to the aggregate direct sums of all even and all odd hooks.
2. The exact rootless-tail factor does not prove `B(pi)=o(p)` false. It is a local-factor theorem and a strong density heuristic, not an asymptotic irreducible-count theorem or a cohomological main-term decomposition.
3. The claimed matching generic Betti lower bound does not apply to the Fortune variety. General-purpose near-sharpness says the generic theorem cannot help; it does not lower-bound this structured example.
4. Extending the census cannot determine an asymptotic constant. It can discriminate finite-range models only.
5. Relocating the local factor into a new main term is not bookkeeping. It requires a singular-series theorem or an object-level top-weight decomposition.

### Corrected strategic conclusion

The full `h=4` aggregate route remains mathematically live. Its exact sufficient target is

\[
\boxed{B_\Lambda=B(\pi_+)+B(\pi_-)\le p-1.}
\]

This target is linear, structure-specific and far beyond generic Betti technology, but it is not structurally impossible.

The q-line `h=2` route should be used only for exact cancellation, congruence, arithmetic descent and transport diagnostics—not as the primary absolute-Betti packaging.

## 1. Primary-source reading of Sawin

Sawin's Definition 3.1 introduces trace functions for a representation `pi` of `S_n` and explicitly says that `pi` is not necessarily irreducible. Definition 4.1 then defines

\[
B(\pi)=\sum_{i=0}^{2\dim X-1}\dim\left(H_c^i(X_{n,m,c})\otimes\pi\right)^{S_n}.
\]

In the von Mangoldt application Sawin takes

\[
\pi_+=\bigoplus_{i\ \mathrm{even}}\bigwedge^i\mathrm{Std}_n,
\qquad
\pi_-=\bigoplus_{i\ \mathrm{odd}}\bigwedge^i\mathrm{Std}_n,
\]

and applies the estimate directly to these two reducible representations.

Therefore the synthesis's alternatives

- `B` is aggregate, so the route is live;
- `B` is per irreducible, so summing `p-1` hooks makes the route void

are not two possible readings. The first is the paper's actual formulation.

Furthermore, the claim that the aggregate is at least `p-1` "by counting alone" is false. A representation appearing in `pi_+` or `pi_-` need not appear in the cohomology of `X_{n,m,c}`. There is no one-dimensional contribution forced for each hook.

## 2. Exact full-interval threshold

At

\[
n=p,\qquad m=p-4,\qquad q=p,
\]

Sawin's Proposition 4.2 has error exponent

\[
\frac12\left(
\left\lfloor\frac np\right\rfloor
-
\left\lfloor\frac mp\right\rfloor
+n-m+1
\right)
=3.
\]

Let

\[
B_\Lambda=B(\pi_+)+B(\pi_-).
\]

Then

\[
\left|
\sum_{\deg g<4}\Lambda(T^p-T+g)-p^4
\right|
\le B_\Lambda p^3.
\]

Let `I_4` be the number of irreducibles in the four-parameter interval. The only degree-`p` non-irreducible prime powers in the interval are

\[
(T-a)^p=T^p-a,
\qquad a\in F_p,
\]

and each has von Mangoldt weight `1`. Thus

\[
\boxed{
\sum_{\deg g<4}\Lambda(T^p-T+g)=pI_4+p.
}
\]

The crown is `I_4>p-1`, equivalently the weighted sum is greater than `p^2`. Sawin therefore proves the crown whenever

\[
p^4-B_\Lambda p^3>p^2.
\]

Equivalently,

\[
B_\Lambda<p-\frac1p.
\]

Since `B_Lambda` is an integer, the exact clean sufficient condition is

\[
\boxed{B_\Lambda\le p-1.}
\]

This is the corrected theorem target. `sawin_packaging_threshold_verify.py` checks the exponent, the weighted identity and the integer threshold independently.

## 3. The local factor does not imply `B=o(p)` is false

Theorem D1.5 proves that each cubic-tail slice has exactly

\[
\frac{p^2-1}{3}
\]

rootless pairs. Relative to the independent-root baseline, this gives the singular-series factor tending to `e/3`.

This is an exact statement about exclusion of linear factors. It does not prove

\[
I_4=\left(\frac e3+o(1)\right)p^3
\]

or the corresponding asymptotic for the von Mangoldt sum. Higher-degree factors and their correlations remain uncontrolled.

There is a second conflation in the synthesis. A measured trace defect may lower-bound the Betti sum needed to support that trace at an individual prime, but `B(pi)` is a total cohomological dimension, not the normalized trace itself. An empirical linear trace defect does not establish an asymptotic linear lower bound for `B(pi)` without a theorem identifying the relevant weight and constituent.

Accordingly:

- `B=o(p)` is unnecessarily strong for the crown;
- the exact target is `B_Lambda<=p-1`;
- the local factor suggests a sharp-constant phenomenon but does not prove a lower bound on `B_Lambda`.

## 4. Recentring at `sigma_p` is a new theorem

Writing

\[
\sum\Lambda=\sigma_pp^4+\text{residual}
\]

is useful only if `sigma_p p^4` is proved to be a genuine main term. That requires one of:

1. a local-to-global singular-series asymptotic;
2. a cohomological decomposition isolating a top-weight constituent with this trace;
3. an exact mass formula separating local obstructions from the remaining oscillatory complex.

Without such a theorem, selecting `sigma_p` from the rootless-tail heuristic or a numerical fit merely redefines the residual. It does not improve the bound.

Extending the census to `p=400` or `500` can test whether finite data lean towards `e/3` or `0.842`; it cannot determine a limiting constant.

## 5. The fixed-class `h=2` warning is valid

For general interval dimension `h=n-m`, Sawin's error at `n=q=p` is

\[
B p^{(h+2)/2}
\]

against main term `p^h`. Error below main therefore requires

\[
B<p^{h/2-1}.
\]

This gives:

| packaging | required aggregate `B` |
|---|---:|
| full interval, `h=4` | `<p` |
| one coefficient averaged, `h=3` | `<sqrt(p)` |
| fixed cubic class, `h=2` | `<1` |

The `h=2` conclusion is correct for a generic main-minus-absolute-error argument. Since `B` is a nonnegative integer, `<1` means exact vanishing of the non-top isotypic cohomology.

This explains why the q-line projector is self-defeating as the primary generic Betti packaging. It can still be valuable for:

- an exact virtual cancellation;
- a congruence or parity certificate;
- a direct global trace calculation;
- an arithmetic descent projector;
- diagnosing a higher-dimensional comparison.

It does not imply that the `h=4` aggregate packaging is void.

## 6. Generic Betti bounds do not lower-bound this variety

The cited modern general-purpose bounds remain enormous for dimension four cut out from ambient dimension `p` by degrees growing with `p`. Their broad near-sharpness confirms that no generic complete-intersection theorem will prove a linear bound.

It does not follow that the Fortune variety itself has exponential Betti number. The lower-bound examples used to establish near-sharpness are generic or specially constructed worst cases, not the sparse additive/Symmetric-group/Pascal variety here.

The correct conclusion is:

> any proof of `B_Lambda<=p-1` must exploit the specific structure of the Fortune family.

That is a difficulty classification, not a no-go theorem.

## 7. The function-field half-degree window

The synthesis is internally inconsistent about the `ff-window` route: both reviewers downgraded it while Step 6 still called it a short Weil proof.

The short proof appears to be essentially correct. Let `P_d` have degree `n`, and vary offsets in a short interval of dimension `h`. Reversal identifies the interval condition with fixed low coefficients, and orthogonality over even Dirichlet characters gives a weighted prime sum with main term `q^h`. Function-field RH bounds each nonprincipal character sum by `O(nq^{n/2})`, uniformly in the prescribed centre. Thus

\[
\sum_{\deg m<h}\Lambda(P_d+m)
=q^h+O(nq^{n/2}).
\]

After subtracting prime-power contamination of the same square-root scale, an irreducible exists when

\[
q^h\gg nq^{n/2},
\]

or

\[
\boxed{
h>\frac n2+\log_qn+O(1).
}
\]

Combining this with the rough-offset lemma should give the centre-preserving theorem that the Fortunate element is irreducible or has degree in

\[
[2d+2,\ n/2+\log_qn+O(1)].
\]

This is far wider than the `d=1` crown and should be advertised only as a benchmark theorem. Before publication, the reversal convention, even-character count, endpoint, and prime-power constants should be written out fully.

## 8. Integer Fortune

The synthesis's strategic conclusion is broadly sound: no existing pointwise prime-gap theorem approaches a `(log N)^2` interval at prescribed primorial centres, and averaged theorems have the wrong quantifier.

The exact statements should remain narrower than some of the rhetoric:

- the short-window implication is stronger than Fortune, not equivalent;
- current sieve inputs based only on divisor counts have no residual room beyond the free primorial roughness;
- Maynard-Tao and almost-all results do not address a single prescribed centre;
- Maier obstructs naive uniform logarithmic-scale asymptotics;
- none of this proves that every conceivable centre-specific method is impossible.

The rational allocation decision remains: do not prioritise integer Fortune while the function-field crown has a concrete geometric target.

## 9. Revised programme

### Phase A — correct the record

1. Replace the false degree-one bijectivity explanation.
2. Label the integer window as sufficient, not equivalent.
3. Correct `B_+=0` versus `B_-=0` statements.
4. Remove claims that the local factor proves `B=o(p)` false.
5. Replace the standing `B=o(p)` target by `B_Lambda<=p-1`.

### Phase B — publish the centre-preserving half-degree theorem

Write and audit the `n/2+log_q n` theorem separately. It is a real result but not a crown strategy.

### Phase C — attack the full `h=4` aggregate geometry

The object is the pair of aggregate even/odd hook complexes. The target is total non-top Betti mass at most `p-1`.

The existing Fourier-Cayley, Pascal, Smith and quantum-bar work should be reinterpreted at this aggregate level. In particular, determine whether their terminal two-line skeleton is a statement about the actual nonnegative cohomology or only a virtual alternating trace.

### Phase D — retain q-line only for exact mechanisms

Use the fixed-class q-line for exact transport, congruence, sign, Tate-normalization and arithmetic projector calculations. Do not seek a generic `B<1` estimate.

### Phase E — singular-series programme must earn its main term

Attempt an object-level or local-to-global proof of the `e/3` constituent. Do not recenter on empirical grounds alone.

## 10. Highest-value next action — completed

The primary-source ambiguity in Sawin has been settled. The next decisive action was to test whether the rank-two braided object underlying the aggregate hook detector remains within the linear Betti budget before virtual signs are applied.

That computation is now recorded in:

- `CWEDGE_TERMINAL_BAR_PROBE_20260726.md`;
- `cwedge_terminal_bar_probe.py`;
- `AGGREGATE_H4_BETTI_PROGRAMME_20260726.md`.

The full `C_wedge` terminal homology has dimensions `4,4,12` at `p=3,5,7` in stable finite-field computations, with exact cyclotomic `H_1` confirmation at those primes. At `p=11`, stable modular first homology alone has dimension `22`, exceeding the doubled Sawin budget `20`.

This does not refute the aggregate route. It proves that the scalar two-line skeleton does not automatically control the unsigned aggregate Betti sum. The immediate next theorem is the characteristic-zero lift at `p=11` and identification of the excess terminal classes.

## 11. Final ruling

The synthesis's broad pessimism about integer Fortune is reasonable. Its proposed retirement of the full function-field packaging is not.

The corrected scientific position is:

\[
\boxed{
\text{the full }h=4\text{ route is live, with exact target }B_\Lambda\le p-1,
}
\]

but a virtual Airy/Pascal identity is insufficient. The next wall is an unsigned, parity-separated Betti comparison, and the first rank-two computation shows that an additional quotient, differential or weight exclusion may be required from `p=11` onward.
