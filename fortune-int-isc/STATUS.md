# Current status

**Programme:** `FORTUNE_INT_ISC_FOCUSED_V0_1`  
**Branch:** `gpt56/fortune-int-isc-focused-v01-20260804`  
**Base:** `deb6bb5468a951bc5485514c5848abcfcf386594`  
**State:** I0–I6 COMPLETED; I7 CLEAN-ROOM VALIDATION  
**Terminal outcome:** `REDUCED_TO_SMALLER_NEW_THEOREM`  
**Primary target:** `INT-PSLT`

## Execution result

The original full covariance target was reduced in two stages:

1. I1 removed the unnecessary upper tail, yielding the one-sided count criterion
   `INT-LTQ`.
2. I4 replaced the four-prime covariance architecture by the one-form shifted-source
   theorem `INT-PSLT`.

The remaining theorem is

\[
\sum_{j<N}(B_X-\Psi_j(H))_+^2=o(B_X^2),
\qquad B_X=c_0X(\log X)^2.
\]

At a failed centre `Psi_j=O(X log X)=o(B_X)`, so INT-PSLT excludes every failure and
implies eventual Fortune by candidate collapse.

## Gate state

- I0 source and target freeze: passed.
- I1 weakest-target audit: passed; lower-tail criterion formalized.
- I2 sparse first moment: closed as non-mandatory and unavailable at the selected scale.
- I3 direct four-prime lane: closed at the `X/L(X)` loss obstruction.
- I4 shifted source: passed with reduction to INT-PSLT.
- I5 source/orbit and PSD: closed at exact smooth-modulus coherence.
- I6 falsification: passed with one-defect no-go models.
- I7 closeout: final clean build and provider sweep in progress.

## Boundary

INT-PSLT, INT-LTQ, INT-ISC and Fortune remain unproved. The programme has completed a
reduction and obstruction classification, not a proof of the conjecture.
