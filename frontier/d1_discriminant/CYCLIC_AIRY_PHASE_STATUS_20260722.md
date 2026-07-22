# Cyclic Airy phase status -- 2026-07-22

## Scientific status

The function-field d=1 Fortune crown remains open.

The rank-two Fourier--Airy transform is exact, but the proposed pre-cohomology cyclic effectivity programme is closed. The remaining problem is an after-pushforward cancellation theorem for the q-family.

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

## Routes closed by this phase

Do not resume without a materially new theorem:

- a single nontrivial cyclic projector;
- localisation of arithmetic traces on the geometric cyclic diagonal;
- an `O(p)` effective local-system model before t/v cohomology;
- ordinary convolution-Tannakian rank arguments based on the Airy generic rank two;
- coherent/vector-bundle Adams--Riemann--Roch transplanted directly to the constructible l-adic pushforward.

## Precise surviving theorem

Let

`H_even(q)=direct_sum_(i even) H_c^1(U_bar,V_i)`,

`H_odd(q)=direct_sum_(i odd) H_c^1(U_bar,V_i)`.

Prove that their common semisimple q-line Frobenius constituents cancel, leaving total uncancelled rank and conductor `O(p)` with an absolute constant, including the quadratic Kummer twist and all three q-boundaries.

Equivalently, construct a parity-reversing geometric correspondence between even and odd hook cohomologies with only `O(p)` unpaired vanishing cycles.

This is stronger and more precise than a virtual Euler-characteristic or conductor statement.

## Epistemic classification

- Fourier--Airy rank-two transform: exact theorem.
- Cyclic projector and trace-fibre identities: exact theorem.
- Hook ranks, invariants, Swan conductors and cohomology ledger: exact theorem, conditional only on the already committed fixed-q inertia theorem.
- Numerical audit files: exact finite integer computation.
- Existence of the required parity-reversing correspondence: open claim.
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

## Natural stopping point

The phase has reached a sharply isolated theorem-level obstruction. Continuing with standard cyclic, Fourier, hook, or Adams--Riemann--Roch manipulations would reproduce an exact no-go already recorded above. A new geometric pairing or a new theorem controlling semisimplified cancellation after pushforward is required.