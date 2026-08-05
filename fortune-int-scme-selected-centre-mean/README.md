# INT-SCME selected-centre mean programme

This directory executes issue #58 from the completed `INT-SOCG -> INT-SCME` reduction.

The programme separates four statements:

1. the weighted prime-pair mean `INT-SCME`;
2. `INT-SCVAR`, a post-terminal prime-progression variance estimate;
3. the conditional first post-terminal prime-divisor-band asymptotic supplied by `INT-SCVAR`;
4. `INT-SCPT`, the remaining signed parity tail.

The first execution draft incorrectly applied classical BDH outside its unconditional modulus range. The corrected programme proves an explicit large-sieve obstruction and retains only the conditional implication

\[
INT\text{-}SCVAR+INT\text{-}SCPT\Longrightarrow INT\text{-}SCME.
\]

The directory is governed by `PROGRAMME.md`, `PREREGISTERED_GATES.json`, `CLAIM_MATRIX.json` and the executable scripts under `scripts/`.