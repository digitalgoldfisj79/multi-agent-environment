# Claim ledger — integrated Fortune formal programme

**Date:** 4 August 2026  
**Current state:** Paper VII F4 stabilized; corrected integer spine formalized  
**Formal proof status:** SEVEN CLAIMS KERNEL-CHECKED; ONE PAPER VII AXIOM REMAINS

## Kernel-checked claims

| Lean declaration | Claim | Evidence |
|---|---|---|
| `FortuneFormal.Bilateral.p7_ifa1_concrete` | P7-IFA1 inverse-free equivalence and scalar-witness uniqueness | Clean Lean 4.32.0 build and static trust audit |
| `FortuneFormal.Bilateral.p7_bdd1_concrete` | P7-BDD1 common-defect existence, uniqueness and degree bound | Same build; corrected prime-Frobenius scope |
| `FortuneFormal.Bilateral.p7_bdd2_concrete` | P7-BDD2 zero-defect reflection/translation classification | Same build; corrected odd-prime scope |
| `FortuneFormal.Bilateral.p7_strip_concrete` | P7-STRIP intermediate-strip emptiness | Same build; direct non-truncated degree contradiction |
| `FortuneFormal.Integer.no_failure_of_variance_below_baseline_gap` | Corrected one-failure block criterion | Lean reconstruction of Papers II–III implication |
| `FortuneFormal.Integer.centered_second_moment_identity` | Exact centred variance identity | Lean ring normalization |
| `FortuneFormal.Integer.four_prime_covariance_identity` | Exact four-prime covariance residual identity | Lean substitution of the off-diagonal pair count |

The Paper VII F3 theorem chain also includes prime-field Artin–Schreier irreducibility, the zero-defect normal form, monic factor ordering and explicit reconstruction of the reflection and translation families.

The quadratic final step

`FortuneFormal.Quadratic.certifiedComponent_not_arithmeticOpen`

is kernel checked: on the externally certified component both normalized quadratic discriminants are literal squares, contradicting the genuine arithmetic-open locus.

## Scope corrections found by formalization

- BDD1 requires the literal prime-Frobenius base `L = X^q - X`, prime-field scope and `k < q`.
- BDD2 and strip require odd prime characteristic.
- The strip argument cannot interpret a negative integer degree bound through truncated natural subtraction; it now uses a direct degree contradiction.
- The corrected integer residual is
  `Z^2 - 2*base*Z + base^2 - base` before the four-prime substitution. An experimental transcription containing an additional `-Z` was rejected by Lean and was not committed.

## ASSUMED pending formalization

| Lean declaration | Exact boundary | Status |
|---|---|---|
| `FortuneFormal.p7_k2_certified_normalization` | Every genuine quadratic incidence produces an arithmetic-open q-free model point on the externally certified component | One ledgered external certificate/normalization axiom |

The broad `p7_k2_empty` axiom has been removed. The theorem

`FortuneFormal.p7_k2_empty_from_external_certificate`

is derived in Lean from this one narrower axiom and the kernel-checked discriminant contradiction. It is therefore **not** an axiom-free formalization of P7-K2.

The abandoned `polyrith` certificate draft has been deleted. No unavailable external tactic, hidden axiom, `sorry`, `admit` or `unsafe` declaration is present in the compiled programme.

## Exact integer research frontier

The corrected Papers II–III reconstruction isolates one theorem, `INT-ISC`: an upper bound of size `N X L(X)`, with `L(X)=o(log X)`, for the centred signed four-prime covariance residual on the actual increasing primorial centres.

The finite algebraic implication from that residual to the required variance and the one-failure exclusion is kernel checked. The analytic estimate itself is not proved or declared as an axiom.

## Direct function-field frontier

Replacement Papers V–VI reduce direct `d=1` to `D1-QLINE-NONSAT`, equivalently strict q-line saturation defect or positivity of the specified Kummer quotient open. That nonvanishing theorem remains open and has no proved implication to the integer residual.

## Paper VII expansion boundary

The cubic true-Frobenius theorem is not declared as an axiom and the F5 cubic expansion is frozen. No bridge from Paper VII to direct `d=1` or integer Fortune is known.

## Explicitly not claimed

- an axiom-free proof of Paper VII quadratic emptiness;
- a completed formalization of all seven manuscripts;
- the cubic true-Frobenius theorem or endpoint `FFPR`;
- `INT-ISC` or the required sparse-centre covariance estimate;
- direct function-field `d=1`;
- any function-field-to-integer transfer;
- Fortune's conjecture;
- journal peer review or publication acceptance.
