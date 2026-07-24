# Fresh bridge assessment: bookkeeping versus new theorem

**Date:** 2026-07-24  
**Method:** cold dependency audit of the committed ledgers, without assuming
that the Airy and hook reductions are already connected.  
**Status:** the bridge contains a genuine theorem-hard core. It is not merely
unfinished bookkeeping.

## 1. Source and target objects

The Airy side controls the trace-zero cubic distribution
\[
 N_b=\#\{x\in\mathbf F_{p^p}:
       \operatorname{Tr}(x)=0,\ \operatorname{Tr}(x^3)=b\}
\]
and its deviation \(D_b\), equivalently the Frobenius trace on the
characteristic-boundary pair \(U_p-U_{p-2}(-1)\).

The Fortune side controls an irreducible-fibre count in a sparse polynomial
family, expressed either through the aggregate incidence sums \(R_a\) or the
post-pushforward even--odd hook complex over the \(q\)-line.

Both reductions are exact. No committed construction identifies these two
objects in a Grothendieck group, derived category, characteristic-cycle
ledger, or explicit point-count identity with all boundary terms.

## 2. Obligation classification

| obligation | classification | reason |
|---|---|---|
| Construct a functorial map from the cubic trace/Airy complex to the post-pushforward hook complex | **theorem-hard** | no source-to-target morphism is present; equality of one trace cannot create it |
| Identify main, Tate and excluded Artin--Schreier lines | care-hard after the map | signs, twists and already-counted summands are finite ledger work once the objects are connected |
| Transport \(D_0=-(p-1)D_*\) as a nearby-cycle statement | **theorem-hard** | a first-trace identity does not determine punctual complexes, higher traces or boundary maps |
| Carry the parameter-dependent arithmetic quadratic twist at infinity | mixed, mainly care-hard after the map | local arithmetic monodromy is known, but its Frobenius sign must be propagated through the comparison |
| Add \(q=2\) and \(q=\infty\) boundary cells | care-hard | exact finite calculations exist; the missing task is assembly with the correct normalization |
| Derive the final positivity/certificate implication | care-hard | elementary once the exact transported formula and its error coefficient are known |

## 3. Minimal application theorem

A sufficient bridge theorem should state an equality in a trace-sensitive
category, not only at the level of first numerical traces. One acceptable
form is:

> After removing the explicitly listed Tate and Artin--Schreier summands,
> the load-bearing graded piece of the even--odd hook pushforward is
> isomorphic, up to the stated Tate twist and arithmetic quadratic character,
> to the cubic Airy boundary complex, with the \(q=2\) and \(q=\infty\)
> cones explicitly attached.

A weaker but still sufficient form is an exact identity for every extension
degree \(m\), including all boundary terms, because equality of all Frobenius
power traces determines the semisimplified virtual object.

The current \(F\) and \(F^3\) spectra are useful falsification data for a
candidate comparison, but cannot replace such a theorem.

## 4. Decision

Claude's description of the bridge as a second theorem is substantively
correct. More precisely:

- it contains at least one essential new comparison theorem;
- punctual transport is a second theorem-hard component unless absorbed into
  that comparison;
- the remaining four tasks are difficult bookkeeping, not independent
  research walls.

The programme therefore terminates at **two theorem packages**:

1. the global Airy cross-symmetric-power correlation estimate;
2. the object-level application comparison, followed by finite ledger
   assembly.

This classification halves neither problem, but it makes external requests
precise and prevents experts being asked to debug an undefined implication.
