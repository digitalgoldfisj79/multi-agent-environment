# INT-SCME selected-centre mean programme

This directory audits the selected-centre weighted mean `INT-SCME`, which is one necessary input to `INT-SOCG`. It is not a completed reduction of `INT-SOCG` to the mean.

## Review-corrected logical status

The external review in `REVIEW_INT_SCME_PROGRAMME.md` established that the low-level collision, exponent and obstruction calculations are sound, but two high-level claims were wrong:

1. `INT-SCPT` is not an independent subordinate theorem. Given a divisor-band asymptotic from `INT-SCVAR`, it is equivalent to `INT-SCME` up to the registered `o(1)` normalization.
2. `INT-SCME` supplies only the first-cumulant bound. It does not imply `INT-SOCG`, which still requires all-orders connected-cumulant control through `INT-LCSK` and the weighted composite-modulus primorial-walk extension `INT-PWOC`.

The honest frontier is therefore

\[
INT\text{-}SCME+INT\text{-}LCSK+INT\text{-}PWOC
\Longrightarrow INT\text{-}SOCG
\Longrightarrow INT\text{-}AOD
\Longrightarrow \text{eventual Fortune}.
\]

`INT-SCVAR` remains an auxiliary Montgomery-type variance conjecture useful for evaluating a post-terminal divisor band. It does not reduce the prime-detection problem. Issue #61 is closed as equivalent to `INT-SCME` conditional on that band evaluation.

The durable unconditional content of this programme is the selected-residue collision-energy lemma, the conditional exponent ledger, the BDH range correction, the direct asymptotic-sieve scale gap and the unconditional large-sieve obstruction.
