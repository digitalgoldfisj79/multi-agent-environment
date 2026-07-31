# TFP3 Round 2: literature-transfer corrections and curve gate

**Date:** 31 July 2026  
**Supersedes:** the `rho` and global sign-cover wording in Round 1.  
**Does not alter:** the exhaustive orbit counts or the exact q-free orientation identity.

## Corrections

1. `rho=1` is permitted. Two q=97 records with `rho=1` satisfy the literal
   true-Frobenius equations and have nonzero common defect of degree 89.
   The verifier now rejects only `rho=0`.
2. The q-free identity `eta_A eta_D=eta_B eta_C` gives two relative-sign
   torsors indexed by the Frobenius base invariant `kappa`. It does not by
   itself construct a globally regular degree-eight cover of the relaxation.
3. The true all-positive class can occur only on the `kappa=+1` locus.
   Componentwise constancy/divisors of `kappa`, etaleness and monodromy are
   new theorem obligations.

## Exact finite-panel geometry

The full coefficient-scheme Jacobian has rank 16 at every audited true point,
so each has tangent dimension one. The fixed-rho Jacobian is generically rank
16 on the panel, with two q=89 rank-15 exceptions. These are candidate branch
points of the rho-map, not a proof of a global curve.

## Literature-driven next theorem

The correct route to effective Chebotarev is:

1. saturate the faithful trace-zero-plane ideal by all nonzero and
   cross-distinct conditions;
2. prove bounded-degree one-dimensional components;
3. normalize them and classify `kappa`;
4. construct the relative-sign torsor on `kappa=+1`;
5. prove finite etaleness and geometric monodromy;
6. apply effective finite-field Chebotarev.

No later amplitude, FFPR, d=1 or Fortune claim follows from this point count
without an additional weighted theorem and an explicit bridge.
