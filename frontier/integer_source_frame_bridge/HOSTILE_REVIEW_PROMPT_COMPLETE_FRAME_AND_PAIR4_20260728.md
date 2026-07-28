# Independent hostile mathematical review

Review the two attached notes as a self-contained theorem package:

1. `COMPLETE_PRIME_MODULUS_FRAME_20260728.md`;
2. `PRIMORIAL_PAIR_OF_PAIRS_SINGULAR_SERIES_AVERAGE_20260728.md`.

The review must be adversarial and claim-by-claim.  Do not infer a Fortune proof.

## Mandatory checks

### Complete prime-modulus frame

- Verify all Fourier signs and normalisations in the complete-character identity.
- Check the equivalence
  `q | P_k-P_j <=> q | product_{j<u<=k} ell_u - 1`.
- Check the shell-divisor count and the summation over index gaps.
- Check that the PNT shell cardinality really yields `O(1/log X)`.
- Check the row-sum/operator-norm argument and whether complex residual vectors are allowed.
- Identify every hidden endpoint or uniformity assumption.

### Pair-of-pairs singular-series average

- Re-derive the local factors for `p|P` and `p∤P`.
- Check the exact local mean-one identities, including `p=2`.
- Check convergence of the normalised Euler product.
- Check the uniform weighted residue-class estimate for arbitrary squarefree moduli, including moduli larger than `H`.
- Check both coefficient-sum bounds in the ranges `p<=y` and `y<p<=H`.
- Check the treatment of `p>H`, including exceptional primes dividing `P-h` or `P+h`.
- Check the claimed relative error `O(log X/H)` uniformly for `P=y#`, `X/2<y<2X`.
- Check the passage from the relative error to `O(H(log X)^3)` and its comparison with the Fortune variance allowance.
- Check whether excluding `h=0`, interval endpoints, or repeated linear forms produces additional terms.

## Required output

1. Headline verdict: `PROVED AS STATED`, `REQUIRES AMENDMENT`, or `INVALID`.
2. Claim-by-claim table.
3. Every adverse finding must quote the exact sentence or formula at issue and give either a counterexample or the failed derivation.
4. Separate errors from requests for expanded exposition.
5. State the strongest corrected theorem boundary.
6. Explicitly state whether the actual four-prime correlation error remains open.

Do not classify a theorem as conditional merely because it uses the prime number theorem or Mertens' theorem.  Do not accept finite computation as proof of the asymptotic statements.