# Cyclic Airy phase status -- 2026-07-22

## Scientific status

The function-field d=1 Fortune crown remains open.

The rank-two Fourier--Airy transform is exact, but the proposed pre-cohomology cyclic effectivity programme is closed. The subsequent root-cover Koszul descent mechanism has also been decisively refuted. The remaining problem is an after-pushforward cancellation theorem for the q-family.

## Exact results proved in this phase

1. **Correct cyclic Adams class.** For a p-cycle acting on `K^(tensor p)`,

   `psi^p(K)=[e_1K^(tensor p)]-[e_zeta K^(tensor p)]`.

   The irreducibility character is this difference minus `K`.

2. **Exact Fourier--convolution normalisation.** With unnormalised Fourier transform,

   `FT(K^(tensor p))=FT(K)^( *p )(p-1)[2(p-1)]`.

3. **Arithmetic cyclic fixed locus.** Frobenius traces of the cyclic eigendifference are sums over

   `Tr_(F_(Q^p)/F_Q)(y)=s`,

   not over the geometric diagonal.

4. **Pre-cohomology effective-rank lower bound.** For generic `S_p` monodromy, the p-cycle character has minimum semisimple positive and negative ranks

   `2^(p-2)` and `2^(p-2)`.

5. **Exact individual hook cohomology.** For `V_i=exterior^i Std`,

   `dim V_i^(C_p)=(binomial(p-1,i)+(p-1)(-1)^i)/p`,

   `Swan_infinity(V_i)=(p-3)/(p-1)*(rank(V_i)-dim V_i^(C_p))`,

   `dim H_c^1(U,V_i)=rank(V_i)+Swan_infinity(V_i)+1_(i=0)`.

6. **Total raw fixed-q middle cohomology.** The actual total is

   `((2p-3)2^(p-1)+3)/p`,

   whereas the alternating virtual dimension is only `4-p`.

7. **Adams-through-pushforward no-go.** The two relevant traces are

   `sum_(t in U(F_Q)) Tr(F_t^p|L_t)`

   and

   `sum_(t in U(F_(Q^p))) Tr(F_t^p|L_t)`.

   Their difference is global degree-p point data, not a local boundary correction.

8. **Exact root-selected Koszul contraction.** On the degree-p root cover, the tautological vector

   `v_i=e_i-(1/p)sum_j e_j`

   gives an explicit `S_(p-1)`-equivariant differential and contraction on `Lambda^bullet Std_p` satisfying

   `hd+dh=id`.

9. **Generic root-cover descent failure.** On the ordered-distinct-root component of the double cover,

   `v_j-v_i=e_j-e_i`,

   with squared norm `2`. The two root-selected homotopies therefore disagree on a component finite etale and dominant over the generic t-line. The failure is not supported at ramification or q-boundaries.

10. **No generic descended parity map.** The hooks

    `Lambda^i Std_p ~= S^((p-i),1^i)`

    are pairwise nonisomorphic irreducibles. Hence there is no nonzero `S_p`-equivariant map from the even hook sector to the odd hook sector.

11. **Exponential correction lower bound for root descent.** Any generic effective residual representing the descent obstruction has minimum positive and negative ranks

    `2^(p-2)` and `2^(p-2)`,

    hence total rank at least `2^(p-1)`.

12. **Arithmetic meaning of the root-cover failure.** Restriction to `S_(p-1)` forgets every fixed-point-free Frobenius class. Selecting a root therefore erases the derangement sector containing the p-cycle class itself. Recovering it is the global length-p Frobenius-orbit problem already exposed by the Adams pushforward no-go.

## Routes closed by this phase

Do not resume without a materially new theorem:

- a single nontrivial cyclic projector;
- localisation of arithmetic traces on the geometric cyclic diagonal;
- an `O(p)` effective local-system model before t/v cohomology;
- ordinary convolution-Tannakian rank arguments based on the Airy generic rank two;
- coherent/vector-bundle Adams--Riemann--Roch transplanted directly to the constructible l-adic pushforward;
- descent of the tautological root-selected Koszul contraction;
- correction of root-cover descent by terms supported only at `t=+/-1,infinity` or `q=0,2,infinity`;
- an `O(p)` generic residual obtained from root-choice Cech descent.

## Precise surviving theorem

Let

`H_even(q)=direct_sum_(i even) H_c^1(U_bar,V_i)`,

`H_odd(q)=direct_sum_(i odd) H_c^1(U_bar,V_i)`.

Prove that their common semisimple q-line Frobenius constituents cancel, leaving total uncancelled rank and conductor `O(p)` with an absolute constant, including the quadratic Kummer twist and all three q-boundaries.

Equivalently, construct a parity-reversing geometric correspondence **after fixed-q pushforward** between even and odd hook cohomologies with only `O(p)` unpaired vanishing cycles.

The phrase “after fixed-q pushforward” is now essential: no corresponding `O(p)` mechanism exists on the generic root local system or on its root cover.

## Epistemic classification

- Fourier--Airy rank-two transform: exact theorem.
- Cyclic projector and trace-fibre identities: exact theorem.
- Hook ranks, invariants, Swan conductors and cohomology ledger: exact theorem, conditional only on the already committed fixed-q inertia theorem.
- Root-cover Koszul contraction and generic descent no-go: exact theorem.
- Numerical audit files: exact finite integer computation.
- Existence of the required post-pushforward parity-reversing correspondence: open claim.
- Function-field d=1 crown: open.
- Integer Fortune conjecture: separate and open.

## Reproducibility files

- `CYCLIC_AIRY_FORMALISM_AND_NO_GO.md`
- `cyclic_airy_representation_audit.py`
- `cyclic_airy_representation_audit_results.json`
- `HOOK_COHOMOLOGY_EFFECTIVITY_LEDGER.md`
- `hook_cohomology_effectivity_ledger.py`
- `hook_cohomology_effectivity_ledger_results.json`
- `ADAMS_PUSHFORWARD_NO_GO.md`
- `ROOT_COVER_KOSZUL_DESCENT_NO_GO.md`
- `root_cover_koszul_descent_audit.py`
- `root_cover_koszul_descent_audit_results.json`

## Natural stopping point

The root-cover audit has reached its refutation stop rule. Continuing with standard cyclic, Fourier, hook, Adams--Riemann--Roch, root-selection, Cech-descent or boundary-localisation manipulations would reproduce an exact no-go already recorded above.

A further advance requires a genuinely new theorem or correspondence acting on the **post-pushforward semisimplified q-line objects**, rather than on the original root local system.
