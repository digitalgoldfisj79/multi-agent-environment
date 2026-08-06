# Fortune formal discovery programme

This directory implements a formal-methods research programme inspired by the public `openai/ten-proofs` workflow, but scoped strictly to the proved Fortune Paper VII package and its cubic true-Frobenius frontier.

The programme does **not** claim that Paper VII is already formalized, that the cubic frontier is solved, that function-field `d=1` follows, or that any result transfers to the integer Fortune conjecture.

## Authoritative base

- Repository: `digitalgoldfisj79/multi-agent-environment`
- Publication base: `publication/fortune-paper-vii-endpoint-incidence-20260731`
- Base commit: `069f47724a3581dc40cfbc9efa3fafd14181ba3e`
- Programme branch: `gpt56/fortune-ten-proofs-formal-v01-20260804`
- Lean toolchain: `leanprover/lean4:v4.32.0`
- mathlib revision: `v4.32.0`

## Purpose

1. Encode the exact mathematical statements and scope boundaries of Paper VII.
2. Replace every Paper VII placeholder with a kernel-checked Lean proof.
3. Reduce the active research frontier to one explicit cubic true-Frobenius theorem.
4. Run parallel discovery only against that frozen theorem statement.
5. require independent reconstruction and Comparator checking before any theorem is promoted.

## Initial state

Stage F0 is a **compiled specification**, not a formal proof. Unproved statements are quarantined in `FortuneFormal/Frontier/Assumptions.lean` and enumerated in `AXIOM_LEDGER.json`. The verifier rejects `sorry`, `admit`, undeclared axioms, hidden imports, and theorem promotion without ledger changes.

See:

- `PROGRAMME.md` — execution protocol and stopping rules;
- `PREREGISTERED_GATES.json` — machine-readable gate contract;
- `CLAIM_LEDGER.md` — exact status boundary;
- `AXIOM_LEDGER.json` — temporary formal obligations;
- `scripts/verify_programme.py` — static integrity verifier.
