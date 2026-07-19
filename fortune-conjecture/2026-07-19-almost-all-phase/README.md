# Fortune almost-all phase (2026-07-19)

This package tests the proposed density-one Fortune route through local Selberg energy and zeta-zero averaging over primorial centres.

## Verdict

- Failure certificate: **proved**.
- Almost-all theorem: **not proved**.
- Primorial-index square-root cancellation at the natural zero-spacing scale: **disproved** by an exact limit theorem.
- Common fixed-conductor zero average across indices: **absent**, because the cutoff ratio tends to infinity.
- Route decision: **STOP** for the proposed explicit-formula mechanism.

## Reproduce

```bash
python code/audit_failure_certificate.py
python code/audit_primorial_zero_kernel.py
python code/run_all_checks.py
```

The normalized zero-gap CSV is shipped in the complete Library package so reproduction does not require recomputing zeta zeros. Delete it to regenerate the gaps with `mpmath.zetazero`.

Complete package SHA-256: `7ccb56a263408b4edfd9f86595174459741910d86c37fed7e0600d03a5b7930e`.
