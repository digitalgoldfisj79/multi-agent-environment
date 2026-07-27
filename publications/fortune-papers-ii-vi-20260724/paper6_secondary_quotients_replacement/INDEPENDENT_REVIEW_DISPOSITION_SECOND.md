# Disposition of the second Paper VI referee review

**Job:** `6a670a3e7ef3c0846496a431`  
**Verdict:** `CONDITIONALLY CORRECT`

## Finding 1: compactified count versus positivity

**Ruling:** rejected as a theorem objection. Theorem 13.1 asserts an exact identity, not `W_p>0`; the terminal section explicitly states positivity is open. Requiring proof of the crown to validate the count identity is a scope error.  
**Action:** add one sentence after the proof: the identity is valid for `W_p=0` as well as positive `W_p` and makes no positivity claim.

## Finding 2: divided-hook virtual character

**Ruling:** the amended proof already states that the representation ring is free abelian on irreducible characters and that virtual multiplicities are integral.  
**Action:** add the explicit Fourier inner-product formula for the multiplicities so no coordinate computation is implicit.

## Finding 3: degree of the derivative

**Ruling:** the manuscript gives `f'=3aX^2+c` with `a!=0`; for `p>5` this has degree exactly two.  
**Action:** state `deg f'=2<p` verbatim.

## Finding 4: Kummer quotient fibres

**Ruling:** valid compression finding.  
**Action:** prove the `mu_n` action is free on the irreducibility level: irreducibility gives `d!=0`; a stabiliser element satisfies `zeta^3 d=d`; and `gcd(3,n)=1` for admitted primes, so `zeta=1`. The geometric quotient fibre is therefore a `mu_n`-torsor.

## Finding 5: irreducibility-level bijection

**Ruling:** valid compression finding.  
**Action:** spell out that for each nonzero `r`, the roots can be ordered so Frobenius advances by `r` positions; the `p` choices of initial root differ exactly by cyclic rotation, leaving one quotient point.

## Reset ruling

The source will be amended. The second review is therefore superseded. A third exact-hash review will be run with an explicit instruction that exact identities are not to be graded as positivity theorems they do not claim.