# Cheap probe of the p=23 modular-minor mechanism

**Date:** 2026-07-22. **Scope:** cost-capped inline probe (no fan-out).

## What was checked and what it says

The latest phase report (pasted by the user; **not yet pushed to the
gpt56 branch** — branch HEAD is still the Koszul phase c9b61c4)
reframes the Cartier support-law gap as a modular-divisibility statement
about binomial/factorial-Schur minors, with a concrete diagnostic: the
elementary assignment bound first permits an apparent survivor-support
violation at p=23, but "the corresponding leading binomial alternant is
zero modulo 23."

### CONFIRMED (independent computation)

1. **The new determinant theorem holds.** For
   \(A_p(G)_{n,e}=[X^e]G(X)^n\), \(G=aX^3+cX+d\), rows \(n=1..p-1\),
   columns \(\{0..p-1\}\setminus\{p-3\}\):
   \[
   \det A_p(G) = -\,c^{p(p-3)/2}\,d^{p-3}\bigl((p-3)ad^2-c^3\bigr)\quad(\bmod p),
   \]
   verified exactly for p = 5,7,11,13,17,19,23,29 (random a∈F_p^*, c,d∈F_p),
   `determinant_check.py`.
2. **Its (1,2)-weighted degree is exactly (p²+p−4)/2**, as the report
   states — sitting (p−3)/2 = 1,2,4,5,7,8,10,13,… above (p²−1)/2.

This is the foundational, load-bearing claim of the Cartier reframing,
and it is solid. Together with an earlier by-hand verification of the
report's core hook identity
\(\sum_k(p-k)(-1)^k\mathrm{Tr}(\sigma|\Lambda^kP)=p\,\mathbf1_{p\text{-cycle}}\)
(correct: the weighted sum collapses to \(g'(-1)\), \(g(t)=\prod_{\text{cyc}}(1-(-t)^\ell)\),
which is p for a single p-cycle and 0 otherwise), the phase report's
arithmetic backbone checks out — consistent with the reliability seen in
prior audits.

### NOT tested here (needs un-pushed definitions)

The decisive claim — **the leading binomial alternant vanishes mod 23**,
and more generally "apparent assignment-bound violation ⇔ leading
alternant ≡ 0 mod p" — could **not** be cleanly tested, because the
precise definitions of the *assignment bound* and of *which* identity-
selected minor is the *leading binomial alternant* live in the phase
report's docs, which are not committed to the branch. Reconstructing them
by guesswork risks testing the wrong object and reporting a misleading
result, so it was not attempted within this cheap probe.

## Verdict

- The reframing rests on a **real, independently confirmed** determinant
  theorem. That materially raises confidence that the "modular
  divisibility" diagnosis is pointing at something real rather than a
  fitting artifact.
- The specific p=23 mechanism is **untested**: it requires the phase's
  un-pushed definitions. To test it properly, either (a) push the phase
  docs defining the assignment bound + leading binomial alternant, or
  (b) authorize a focused agent to reverse-engineer them from the
  determinant structure and run the p=23 (and next-violation-prime)
  check.

## Honest boundary (unchanged)

Even a fully confirmed modular mechanism proves only the **support law**
(where the surviving coefficients live). The terminal problem — that the
boundary survivor sum \(S_a=3aN_a\) is nonzero mod p — is untouched, and
last round's closed-form hunt for exactly that quantity was **negative**
(289 elliptic curves, 180 hypergeometrics). And the separately-diagnosed
cohomological route is now known to be **exact but circular** for
positivity. So the reframing improves structure; the nonvanishing
endgame remains genuinely open. Still the function-field sibling —
integer Fortune untouched.
