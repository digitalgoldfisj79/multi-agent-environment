# Round 15: k=2 emptiness theorem — certificate package

Sources (chartB_universal.sing is the branch's committed script, run to
completion here; the rest are this round's):

- chartB_universal.sing / chartX_universal.sing: GB + reduce(T) + lift over Q
  for the two localization charts (B != 0 resp. A-C != 0).  Both give
  reduce(T, G) = (0,0,0).
- verify_lift_identities.py: the verification OF RECORD for both lift
  identities T = K*M -- independent parsing of the Singular lift output and
  exact re-expansion over Q with Fraction dict arithmetic (plus mod-1009 and
  mod-10007 checks).  Both charts verify.
- chartX_liftverify.sing: a Singular-native variant of the same check,
  provided for reproducibility; note it recomputes the lift and did NOT
  complete within 25 minutes in this environment -- use
  verify_lift_identities.py on the emitted lift output instead.
- ideal_faithfulness.sing: proves the branch's f0..f3 generate the same
  ideal as my independently derived Round-14 model after inverting U
  (mutual reduction; prints IDEALS_AGREE_ON_U_NONZERO).
- modp_certificates: the same reduce computation in characteristic p for
  p in {3, 5, 7, 11, 31, 163} (the prime support of the Q-lift
  denominators) and both charts — all reduce to zero (see data log).

Together with the disc-square hand identities on T (disc P = (A-C)^2,
disc S = (A-C+2)^2, denominators powers of 2), these certify the k=2
emptiness theorem for every odd prime power q.  See
ROUND15_K2_EMPTINESS_THEOREM_20260803.md.
