# d=1 verification scripts (rescued from workbench scratchpad)

Provenance: these scripts were written and run by the seven-agent d=1
workbench (see ../../d1_workbench/) and its adjudication. They are
committed as-is for reproducibility; paths inside them may reference the
original scratchpad locations and need adjustment. Dependencies: python3,
numpy, sympy; the fast N(p) sweeps used python-flint 0.9.0.

- fqlib.py, step1_counts.py, step2_identity.py, step3_p7.py — cubic-ledger
  agent: F_Q arithmetic, identity checks at p=3,5,7, strata evaluations.
- adv_*.py — adversary agent: independent re-derivations (counts, identity,
  N(p) formula, orbits, second moment).
- audit_zero_verify.py, audit_1499.py, audit_own_N.py,
  audit_zero_results.json — audit agent: exhaustive reconfirmation of all
  61 claimed N(p)=0 primes <= 1500 and independent N(p) recomputation.
- judge_*.py, judge_scan*_results.json — adjudication: exhaustive p=5
  checks, second-moment recomputation, independent slice scans to p=181.
- N_checkpoint.json, N3_checkpoint.json, Ndata_3_1200.json — raw sweep
  checkpoints (quadratic N(p), cubic slice counts, N to 1200).
- ff_fortune.py, ffcheck.py, check_identity.py, audit_gap_witness.py —
  further cross-checks and witness certification.

Known reproducibility gaps (from the cold review, acknowledged): no
version lockfile; the committed set is what survived the ephemeral
scratchpad — a clean-room deterministic generator + independent verifier
pair with per-prime witness ledgers and SHA-256 manifests remains to be
built before any publication-grade certification claim. The committed
paper-level claim is limited to all odd p < 1200.
