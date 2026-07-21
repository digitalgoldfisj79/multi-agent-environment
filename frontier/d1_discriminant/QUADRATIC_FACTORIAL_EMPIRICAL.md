# Quadratic-factorial sieve empirical sweep

**Date:** 2026-07-21  
**Hugging Face job:** `6a5f8ac6d09dc1f57c6bf811`  
**Range:** every prime `5 <= p < 2000`, both square classes of `a`.

The sweep constructs the exact quadratic-factor multiplicity table for every coefficient pair, verifies `nu_2 <= 3`, applies the local-rootless condition, and records unsigned and discriminant-weighted factorial moments.

The largest observed normalized deviations were:

- `max |Q_(a,2)-p^2/24|/p = 0.821775`, attained at `p=1049`, nonsquare class;
- `max |Q_(a,3)-p^2/144|/p = 0.325714`, at the same point;
- `max |Q_(a,2)^chi|/p = 1.545879`, attained at `p=643`, nonsquare class;
- `max |Q_(a,3)^chi|/p = 0.410576`, at the same point;
- `max |N_(a,no2)-29p^2/144|/p = 0.665111`, attained at `p=1093`, nonsquare class;
- `max |M_(a,no2)|/p = 2.168462`, attained at `p=1579`, square class.

At the last point the exact data were

`Q_(a,1),Q_(a,2),Q_(a,3) = 414568,103702,17182`,

`Q_(a,1)^chi,Q_(a,2)^chi,Q_(a,3)^chi = -1496,634,218`,

`N_(a,no2) = 503032`,

`M_(a,no2) = 3424`.

These data are not used in the proof. They strongly support the sharper estimates

`Q_(a,2) = p^2/24 + O(p)`,

`Q_(a,3) = p^2/144 + O(p)`,

`Q_(a,2)^chi,Q_(a,3)^chi = O(p)`,

and

`N_(a,no2) = 29p^2/144 + O(p)`, `M_(a,no2)=O(p)`.

The rigorous theorem currently retains the fixed-degree Lang-Weil error `O(p^(3/2))` for the new second and third factorial moments.
