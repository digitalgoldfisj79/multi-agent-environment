# Route A closed: projective occupancy forces natural sampled mass in degree two

**Date:** 30 July 2026  
**Branch:** `gpt56/fortune-mesoscopic-cotlar-20260728`  
**Programme:** `FERP-0.1`  
**Input head:** `0c9e63ca331554174d5e2e9f69a33750e17cf6d4`

## 0. Result

The exceptional sampled-diagonal route is false in the uniform form required by `SAD_FF`.

For odd `q`, take the endpoint family

- modulus degree `k=2`;
- source degree `m=3=2k-1`;
- ordered distinct monic irreducibles `P,S` of degree two;
- any puncture `L` which is a unit modulo every degree-two `P`, including `L=t^q-t`;
- nonzero scalar completion frequency `theta in F_q^*`.

Write

`M_samp(theta)=sum_{P!=S}|Ahat_P(mu_PS(theta))|^2`

and

`M_full=sum_P sum_{mu!=0}|Ahat_P(mu)|^2`.

Then the exact projective occupancy theorem below gives

`sum_{theta!=0} M_samp(theta) >= (q-3)/2 * M_full`.

Keating--Rudnick, Theorem 2.2(ii), applied literally with source degree `n=3` and irreducible modulus degree two, gives

`M_full = (1/2+o(1)) q^7`

as `q -> infinity` through odd prime powers. Consequently

`max_{theta!=0} M_samp(theta) >= (1/4+o(1)) q^7`.

But the Route A allowance at `k=2` is

`q^(3k) poly(k,m) = q^6 * O(1)`.

Therefore no uniform bound

`M_samp(theta) << q^(3k) poly(k,m)`

can hold for every nonzero canonical `theta` with a `q`-independent implied constant.

**Conclusion:** `SAD_FF` is **FALSIFIED AS A UNIFORM POINTWISE ROUTE**. Route A is closed. This does **not** falsify corrected endpoint `FFPR`; it forces the programme onto the centered bilateral Route B.

## 1. Exact projective occupancy theorem

Let

`P=t^2+b t+c`

be monic irreducible over `F_q`, with nonsquare discriminant

`D=b^2-4c`.

Every other monic quadratic has the unique form

`S=P+r`,  where  `r=u t+v != 0`.

For a projective direction `[r] in P^1(F_q)`, define

`n_P([r]) = #{lambda in F_q^* : P+lambda r is irreducible}`.

### Theorem PO2

For every degree-two irreducible `P`, the `q+1` projective directions split equally:

- `(q+1)/2` directions have occupancy `(q-3)/2`;
- `(q+1)/2` directions have occupancy `(q-1)/2`.

In particular,

`n_P([r]) >= (q-3)/2`

for every projective direction.

### Proof

The discriminant of `P+lambda(ut+v)` is

`D_lambda = D + lambda(2bu-4v) + lambda^2 u^2`.

The polynomial is irreducible exactly when `D_lambda` is a nonsquare.

If `u=0`, the map `lambda -> D-4lambda v` sends `F_q^*` bijectively to `F_q \ {D}`. Since `D` itself is nonsquare, exactly `(q-3)/2` remaining values are nonsquares.

If `u!=0`, the quadratic in `lambda` has nonzero discriminant

`Delta=(2bu-4v)^2-4u^2D`,

because `D` is nonsquare. The standard quadratic-character identity gives

`sum_{lambda in F_q} chi(D_lambda)=-1`.

If `Delta` is square, `D_lambda` has two zeros and there are `(q-1)/2` nonsquare values over all `lambda`; removing `lambda=0`, where `D_0=D` is nonsquare, leaves `(q-3)/2`.

If `Delta` is nonsquare, there are no zeros and `(q+1)/2` nonsquare values over all `lambda`; removing `lambda=0` leaves `(q-1)/2`.

After projectively normalizing `u=1`, the quantity `Delta` is a nonzero square multiple of

`x^2-D`,  with  `x=b-2v`.

As `v` runs through `F_q`, so does `x`, and

`sum_x chi(x^2-D)=-1`.

Hence among the `q` nonconstant directions, `(q-1)/2` have square `Delta` and `(q+1)/2` have nonsquare `Delta`. Adding the constant direction, which has low occupancy, gives `(q+1)/2` directions of each occupancy. QED.

## 2. Transfer from projective occupancy to sampled Fourier mass

For fixed `P`, the sampled frequency is

`mu_PS(theta)=-theta Lbar_P Sbar_P`.

Because `P` and `S` are monic of equal degree,

`S mod P = S-P = r`.

Inversion, multiplication by the unit `Lbar_P`, and multiplication by `theta in F_q^*` each permute the one-dimensional `F_q`-subspaces of `F_q[t]/P`. Thus the multiset of projective occupancies of the sampled frequencies is exactly the multiset in Theorem PO2.

Let

`E_P(ell)=sum_{mu in ell}|Ahat_P(mu)|^2`

for a nonzero projective line `ell`. Then

`sum_{theta!=0} sum_{S!=P}|Ahat_P(mu_PS(theta))|^2`

`= sum_{ell in P^1(F_q)} n_P(ell) E_P(ell)`

`>= (q-3)/2 sum_{mu!=0}|Ahat_P(mu)|^2`.

Summing over `P` proves the exact inequality

`sum_{theta!=0} M_samp(theta) >= (q-3)/2 M_full`.

No genericity, random sampling or finite-panel inference enters this step.

## 3. Literal Keating--Rudnick input

For a degree-two irreducible modulus `P`, define

`N_P(A)=sum_{deg f=3, f=A mod P} Lambda(f)`.

Keating--Rudnick Theorem 2.2(ii) states, in the fixed-degree large-field regime, that the reduced-residue variance satisfies

`G(3;P) ~ q^3(deg P-1)=q^3`.

The theorem applies because:

- source degree is fixed at `n=3`;
- `P` is squarefree and has degree two;
- `n >= deg P-1`;
- `q -> infinity` is exactly the theorem's regime.

The asymptotic is uniform over degree-two irreducible `P`: otherwise a sequence of counterexample moduli would contradict the theorem's statement for arbitrary sequences `P=P_q`.

The zero residue has `N_P(0)=0`, since a monic cubic divisible by an irreducible quadratic is a product of that quadratic and a linear polynomial and is not a prime power. If

`V_all(P)=sum_{A mod P}|N_P(A)-q|^2`,

then an exact change of centre gives

`V_all(P)=G(3;P)+q^4/(q^2-1)`.

Plancherel therefore gives

`sum_{mu!=0}|Ahat_P(mu)|^2 = q^2 V_all(P) ~ q^5`.

Finally,

`pi_q(2)=(q^2-q)/2`,

so

`M_full=sum_P sum_{mu!=0}|Ahat_P(mu)|^2=(1/2+o(1))q^7`.

Reference: J. P. Keating and Z. Rudnick, *The variance of the number of prime polynomials in short intervals and in residue classes*, arXiv:1204.0708, Theorem 2.2(ii).

## 4. Machine audit

Verifier:

`fortune-review/scripts/ff_sampled_diagonal_discriminator.py`

Frozen output:

`fortune-review/data/ff_sampled_diagonal_discriminator.json`

The verifier independently checks:

1. Theorem PO2 for every degree-two irreducible at `q=3,5,7,11`;
2. the exact projective occupancy lower inequality;
3. `M_samp`, `M_full`, source diagonal, distinct-source residue coincidences and signed residual in cyclotomic arithmetic;
4. every nonzero `theta` on the CI panels;
5. the true puncture `t^q-t` and a non-affine unit-puncture control.

For the true puncture, the exact CI values include:

| `(q,k,m)` | exact `M_samp(theta)` | `M_samp/q^(3k)` |
|---|---:|---:|
| `(3,2,3)` | `216` | `0.296296...` |
| `(5,2,3)` | `10500` | `0.672` |
| `(7,2,3)` | `148176` | `1.259475...` |
| `(11,2,3)` | `3993000` | `2.253944...` |
| `(3,3,5)` | `21384` | `1.086419...` |
| `(5,3,5)` | `9697500` | `4.96512` |
| `(3,4,7)` | `1907874` | `3.590001...` |

The equality across nonzero `theta` in these true-puncture panels is machine-verified and consistent with the previously proved affine theta-independence. It is not needed for the Route A falsification, which uses only the exact theta average.

## 5. Status ledger

### PROVED EXACTLY

- Theorem PO2;
- the projective occupancy identity and lower inequality;
- the exact relation between reduced-residue and all-residue variance;
- the implication from a natural all-residue variance to a large sampled mass for at least one `theta`.

### PROVED FROM PUBLISHED INPUT

- `M_full=(1/2+o(1))q^7` for `k=2,m=3`, by Keating--Rudnick Theorem 2.2(ii);
- `max_theta M_samp(theta) >= (1/4+o(1))q^7`;
- failure of the uniform `SAD_FF` bound.

### MACHINE-VERIFIED IDENTITY / EMPIRICAL-EXACT FINITE PANEL

- all listed exact cyclotomic panels and occupancy histograms.

### NOT PROVED

- a lower bound for every individual `theta` without using true-puncture affine symmetry;
- an asymptotic for deterministic sampled mass in growing `k` at fixed `q`;
- corrected endpoint `FFPR`;
- any integer theorem.

## 6. Programme consequence

Gate 1 is decisive:

- Route A is closed in the uniform form preregistered by `FERP-0.1`;
- ordinary sampled-frequency variance work is no longer an endpoint proof route;
- Gate 2 and Gate 3 become the sole main line: classify the bilateral incidence and compute the exact signed contribution of every exceptional component;
- Gate 4 must construct the centered bilateral identity before positivity.
