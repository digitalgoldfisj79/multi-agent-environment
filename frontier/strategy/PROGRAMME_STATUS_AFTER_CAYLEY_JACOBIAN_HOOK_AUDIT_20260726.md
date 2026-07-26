# Programme status after the exact Cayley--Jacobian hook audit

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** function-field Fortune `d=1` only.  
**Crown status:** **OPEN**.

## 1. New stopping-point result

The requested `p=11/p=13` equivariant Cayley--Jacobian calculation has been completed far enough to determine the next theorem.

### PUBLISHED THEOREM

The three primitive Jacobian components are exactly

\[
J_{(\kappa,0)},\quad J_{(\kappa,1)},\quad J_{(\kappa,2)},
\qquad
\kappa=\frac{(p-7)(p-2)}2,
\]

with top Dwork degrees `p-5,p-4,p-3`.

### PROVED THEOREM

The modular root space `W=ker(sum)/<1>` has no ordinary `S_p`-equivariant characteristic-zero lift. On a `p`-cycle it is one Jordan block of length `p-2`, while every ordinary representation of dimension `p-2` is a sum of trivial/sign lines.

The naïve integral quotient is also obstructed by

\[
(\mathrm{sum})\circ(\mathrm{diag})=p.
\]

### EXACT COMPUTER-ASSISTED THEOREM

At both regression primes:

- `J_(kappa,0)` and `J_(kappa,2)` have unique ordinary character extensions;
- `J_(kappa,1)` has no genuine ordinary character extension;
- the recombined total `2J_0+J_1` has a unique ordinary character extension;
- after the residue sign twist, this gives the exact compactified primitive `H^2` hook character.

## 2. Exact primitive hook profiles

### `p=11`

\[
\boxed{(m_0,\ldots,m_{10})=(0,0,0,0,0,6,14,12,6,3,1).}
\]

All occur in projective cohomological degree `2`.

\[
B_{even}^{prim}=21,
\qquad
B_{odd}^{prim}=21.
\]

The sign hook is one-dimensional. Removing it leaves `41` non-sign multiplicity dimensions. To reach the admitted budget `10`, the open/discriminant boundary map must remove at least `31`.

### `p=13`

\[
\boxed{(m_0,\ldots,m_{12})=(0,0,0,0,0,11,35,51,49,34,16,4,0).}
\]

Again all occur in degree `2`.

\[
B_{even}^{prim}=100,
\qquad
B_{odd}^{prim}=100.
\]

There is no sign hook. To reach a comparison budget `12`, the boundary map would have to remove at least `188` hook multiplicity dimensions.

## 3. Routes closed by the audit

### REFUTED

1. Replace `W` by the ordinary standard representation.
2. Lift the three Jacobian degrees separately as ordinary `S_p` representations.
3. Use the compactified primitive Jacobian ring as the final Sawin Betti page.
4. Treat the `p=13` regression as requiring only five cancellations.
5. Ignore the discriminant/open-boundary Gysin map after computing the smooth compactification.

## 4. Correct surviving route

The three Jacobian degrees must be retained in a characteristic-`p` Dwork/divided-power or full-permutation-lattice complex and recombined before ordinary hook extraction.

The load-bearing object is now the localization map

\[
R\Gamma(D_p)(-1)[-2]
\longrightarrow
R\Gamma(Y_p),
\]

where `D_p` includes the discriminant and must be augmented by root infinity, frequency infinity, `q=0`, `q=2`, `q=infinity`, translation, scaling and punctual cones.

The mixed Cayley derivatives define the algebraic differential, but the exact cancellation is a global residue/Gysin calculation.

## 5. Next highest-value theorem

> **Equivariant discriminant-Gysin cancellation theorem.** Construct the parity-separated `S_p`-equivariant boundary complex and its map to `H^2_prim(Y_p)`. Prove that, after exact sign extraction, its image has sufficient hook rank to leave at most `p-1` multiplicity dimensions. The hard regressions are rank at least `31` at `p=11` and at least `188` at `p=13`.

This theorem must also identify Frobenius and the open-boundary cones, not only dimensions.

## 6. Distance from `d=1`

The programme has not proved the aggregate bound

\[
B_\Lambda\le p-1.
\]

It has replaced the former mixed-Cayley ambiguity by a concrete map and exact rank requirements. One major theorem remains on the application side:

\[
\boxed{\text{uniform equivariant discriminant/Gysin cancellation with Frobenius.}}
\]

After that, the already isolated sign saturation issue for `p=23 mod 24` remains unless the boundary theorem supplies a one-unit improvement or a non-extremal phase.

## 7. Verification

```bash
python frontier/strategy/cayley_jacobian_hook_lift_verify.py
python frontier/strategy/modular_root_space_lift_obstruction_verify.py
```

Machine-readable output:

```text
frontier/strategy/cayley_jacobian_hook_results_20260726.json
```
