# Cold audit of the d=1 cohomological no-go stack

**Date:** 2026-07-22.
**Target:** the no-go theorems on live branch
`gpt56/consolidated-fortune-20260721` that reduce the function-field d=1
Fortune crown to one surviving open statement.
**Method:** 5-agent adversarial audit (worktree-isolated), exact finite
computation for p = 5,7,11,13, with independent literature retrieval.
Agent outputs: `workbench/`. One agent (cohomology ledger) returned a
placeholder stub and failed to run; the adjudicator performed that
verification in its place (noted as a caveat below).

## Verdict: the "one narrow door" picture SURVIVES — no wall cracked

Every no-go is exact, correctly scoped to a *pre-pushforward* (or
same-space) object, and none overclaims the crown. All cheaper routes are
genuinely walled off; the sole surviving route is the post-fixed-q-
pushforward even/odd hook-cohomology Frobenius cancellation. My earlier
"one narrow door, same global-long-orbit wall in cohomological form" read
is confirmed by exact computation.

## Per-wall rulings

- **Wall A — pre-cohomology effectivity (CONFIRMED, unconditional).**
  Λ_p = Σᵢ(−1)ⁱ Λⁱ Std has character det(1−g|Std) = p on a single p-cycle
  and 0 on every other class (the irreducibility indicator, ×p);
  Σ_{i even} C(p−1,i) = Σ_{i odd} C(p−1,i) = 2^{p−2}; the hooks
  Λⁱ Std ≅ S^{(p−i,1ⁱ)} are pairwise-distinct irreducibles. Hence any
  honest semisimple presentation of Λ_p has min ± rank 2^{p−2} — an exact
  rep-theoretic exponential floor. Kills any O(p) pre-cohomology model and
  any equivariant even→odd parity map (Schur). Double-checked: HCE.1 also
  confirmed independently by the rep-theory agent.

- **Wall B — cohomology dimension ledger (CONFIRMED, CONDITIONAL).**
  HCE.1 dim V_i^{C_p} = (C(p−1,i)+(p−1)(−1)ⁱ)/p = #zero-sum i-subsets of
  F_p^*; Swan_∞(V_i) = (p−3)/(p−1)·(rank−invariants); h¹_c = rank+Swan+
  [i=0]; total h¹_c = ((2p−3)2^{p−1}+3)/p; even/odd sectors each ~2^{p−2};
  virtual (alternating) dimension exactly 4−p. This is not itself a no-go
  — it *quantifies* the surviving problem (exponential actual cohomology
  vs linear virtual dimension) and thereby closes the "use the Euler
  characteristic / virtual rank" shortcut. **Conditional** on the fixed-q
  wild-inertia theorem (below). *Verification caveat:* the assigned agent
  failed; only the adjudicator verified this wall — it is the single
  weakest-checked wall in this audit.

- **Wall C — root-cover Koszul descent (CONFIRMED, pre-pushforward).**
  The homotopy hd+dh=id holds on Λ^•V; the root-selected homotopies
  disagree on the dominant off-diagonal component (v_j−v_i = e_j−e_i,
  norm² 2), so the failure is generic, not boundary-supported;
  restriction to S_{p−1}=Stab(root) annihilates the entire derangement/
  p-cycle sector. Load-bearing result is the 2^{p−1} exponential floor
  (RKD.4), matching Wall A. Correctly limited to the pre-pushforward
  object.

- **Wall D — Adams-through-pushforward (CONFIRMED, unconditional).**
  RΓ_c(ψᵖL) sums Tr(F_t^p) over U(F_Q); ψᵖRΓ_c sums over U(F_{Q^p}); the
  difference is a global ~Q^p−Q extension-point sum that no O(p) boundary
  correction at {+1,−1,∞} can absorb (clean Grothendieck–Lefschetz). The
  cited ARR theorems (Pink–Rößler 0812.0254; Maxim–Schürmann 1602.06546)
  were retrieved and are correctly *declined*, not misapplied — the
  latter's cyclic fixed-point sum is over U(F_{Q^p}), agreeing with the
  side that does NOT commute. GOS and Katz rigid-local-system / middle-
  convolution / Airy machinery confirmed real and in-scope.

## The one conditional input

Everything numeric in Wall B rests on the **fixed-q wild-inertia
theorem**: I_∞ = C_p ⋊ C_{(p−1)/2} with a single lower ramification jump
j = (p−3)/2 (doc: `WILD_INFINITY_INERTIA.md`). This was outside all four
auditors' stated scope; the adjudicator states it independently
re-derived it. It remains the single load-bearing input not verified by a
dedicated independent agent, and the natural target of any follow-up
audit.

## The surviving open door (genuinely open)

The post-fixed-q-pushforward even/odd hook-cohomology cancellation to
O(p) — equivalently a parity-reversing correspondence with only O(p)
unpaired vanishing cycles — is **not closed by any no-go** (they all act
pre-pushforward or on the same-space pushforward; the open claim concerns
the different objects H_even(q), H_odd(q) over the q-line). Whether
Katz-style rigidity / middle convolution can *decide* it is honestly
rated UNVERIFIABLE — a reasonable-in-principle toolbox, but no argument
that it settles the parity correspondence.

## Bottom line

The walls hold. The problem is genuinely down to one narrow, hard door,
and that door is the cohomological shadow of the same "detect a single
length-p Frobenius orbit, no local shortcut" obstruction that blocks the
whole programme. Two honest soft spots remain for a future pass: (i) an
independent re-audit of Wall B's Swan/GOS ledger, and (ii) the fixed-q
wild-inertia theorem it depends on. Neither is evidence of a crack — just
the places this audit did not independently double-cover. Unchanged
boundary: this is the function-field sibling; integer Fortune is untouched.
