# Fortune Zeta23 transfer programme v0.1 — final status

## Primary terminal state

`FORMAL_ASSURANCE_GAIN__INTEGER_TRANSFER_CLOSED`

The bounded Zeta23-inspired experiment produced one substantive formal-assurance gain and one clean integer-side no-go result. It does not prove Fortune's conjecture and does not reopen the frozen integer mainline.

## Lane F — Paper VII formal trust architecture

### Result

`COMPARATOR_ARCHITECTURE_PASS__SIX_POWER_LIFTS_KERNEL_CHECKED__GLOBAL_NORMALIZATION_AXIOM_REMAINS`

The new comparator layer independently states Paper VII quadratic emptiness from Mathlib-only definitions, translates the datum literally into the implementation, and proves the independent challenge conditional on `K2CertifiedNormalizationStatement` supplied as a theorem parameter.

The conditional bridge's `#print axioms` output contains only:

- `propext`;
- `Classical.choice`;
- `Quot.sound`.

It does not contain `p7_k2_certified_normalization`. The comparator layer contains no `axiom`, `sorry`, `admit` or `unsafe` declaration. The full package continues to contain exactly one custom axiom: `FortuneFormal.p7_k2_certified_normalization`.

A successful full build recorded 8,688 Lean jobs.

### Certificate kernelization

All six compact q-free power-lift identities have now been checked by Lean over `MvPolynomial (Fin 4) Z` after exact denominator clearing:

- B chart: targets `U-1`, `B+2`, `(A-C)^2+4A`;
- X chart: targets `U-1`, `B+2`, `(A-C)^2+4A`.

The four identities that normalize efficiently passed in the all-chart workflow. The B1/B2 monolithic normalization was too expensive; a split-normalization generator checked the same exact identities in smaller product-expansion lemmas. Both B1 and B2 passed in GitHub Actions run `31484014359`, jobs `93755158829` and `93755158760`.

`FortuneFormal/Quadratic/CertificateBridge.lean` is also kernel checked. It proves that, on the arithmetic-open locus, the six chart identities force the published `CertifiedComponent` conditions.

This means the finite q-free certificate computation is no longer a reason to keep the broad Paper VII axiom. What remains is genuine arithmetic normalization plus characteristic specialization.

### Remaining formal boundary

The sole project axiom is **not removed**. To remove it honestly still requires:

1. direct kernel certificates in characteristics 3 and 5;
2. specialization of the integer certificates in all other odd characteristics;
3. affine normalization of arbitrary monic irreducible quadratics;
4. reduction of `X^q-X` modulo those normalized quadratics;
5. transport and coefficient extraction for the four inverse-free incidences;
6. transfer of distinctness/irreducibility into the model's arithmetic-open conditions.

The first two items are finite certificate engineering. Items 3–6 are the real normalization theorem.

## Lane S — finite compression / stable rank

### Result

`S5_FAIL__PSD_COMPRESSION_NO_STRICT_ARITHMETIC_GAIN`

For nonnegative row occupancies `Z_j`, diagonal stable rank gives the exact criterion

`(sum Z_j)^2 > (R-1) sum Z_j^2`

for excluding every zero row. This is exactly the existing one-failure second-moment mechanism in spectral notation; it does not lower the arithmetic correlation order.

Exact primorial panels showed that terminal-prime stratification improves the deterministic one-failure variance allowance, and every tested stratum passed the finite diagnostic. But the averaging population shrinks by the same polylogarithmic factor, so obtaining the improved allowance requires a new uniform localized four-prime covariance theorem. No weaker available analytic input was exposed.

### PSD Gram no-go

If `G = B B*` and `a_j = ||B_j||^2`, then

`tr(G^2) = sum a_j^2 + sum_{j != k} |<B_j,B_k>|^2 >= sum a_j^2`.

Therefore the diagonal matrix with the same row energies maximizes the ordinary stable-rank lower bound. Enriching the incidence matrix with off-diagonal PSD overlaps can only worsen this certificate and introduces additional prime-correlation terms.

### Indefinite correction test

A genuinely Zeta23-like mechanism would require an indefinite Hermitian correction with independently small positive index. The natural centered Gram correction does not inherit such a bound from Paper I's collision graph sparsity or Smith/rank structure: even a path-graph adjacency matrix is tree-supported yet has positive index of order half its dimension.

No natural signed correction with controlled inertia emerged from the exact Fortune detector in this run.

Accordingly the integer Fortune frontier remains `CLOSED`.

A future finite-compression proposal may reopen this decision only if it supplies a concrete indefinite arithmetic correction with a provable inertia bound and genuinely weaker trace/Frobenius inputs than the frozen four-prime/logarithmic-order barriers.

## Fortune status

- Fortune's conjecture: **not proved**.
- Integer mainline: **CLOSED**.
- New unconditional integer mechanism: **none**.
- Paper VII q-free certificate identities: **KERNEL_CHECKED**.
- Paper VII unconditional K2 theorem inside Lean: **still derived through one explicitly ledgered custom normalization axiom**.

## Net assessment

The Zeta23 comparison was worth running. It improved the formal trust architecture and removed external computation from an important finite portion of Paper VII, while falsifying the naive transfer of the rank-trace idea to Fortune's integer detector.

The next highest-value formal task is now narrower than before: finish characteristic 3/5 plus field specialization, prove `CertificateStatement` without an axiom, and then attack the remaining datum-normalization theorem. The next highest-value publication task remains specialist literature/priority review of the theorem portfolio.
