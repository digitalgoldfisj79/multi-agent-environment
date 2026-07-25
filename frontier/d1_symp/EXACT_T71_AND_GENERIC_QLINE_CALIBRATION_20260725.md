# Exact T_71 and generic-only q-line calibration

**Date:** 2026-07-25  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Classification:** **EXACT COMPUTER-ASSISTED RESULT**.  
**Scope:** targeted Airy/q-line calibration at the first recorded prime with a completely zero finite-boundary ledger.

## 1. Exact local Airy computation

For

\[
t_u=-\sum_{x\in\mathbf F_{71}}\zeta_{71}^{x^3+ux},
\qquad
f_{71}(u)=D_{71}(t_u,71),
\]

the exact cyclotomic calculation gives

\[
\sum_{u\in\mathbf F_{71}}f_{71}(u)
=
-2607645185442448528174099331904108712984617191997478594165081742864.
\]

Using

\[
\sum_u f_{71}(u)=-71T_{71},
\]

one obtains

\[
\boxed{
T_{71}
=
36727396978062655326395765238086038211050946366161670340353263984.
}
\]

This uses only exact arithmetic in `Z[zeta_71]` and the rank-two Dickson recurrence. It does not enumerate `F_(71^71)`.

## 2. Hasse calibration

Here

\[
\frac{p+4}{3}=25.
\]

The exact integer satisfies

\[
\boxed{v_{71}(T_{71})=25.}
\]

Moreover

\[
\frac{T_{71}}{71^{25}}
=
1921017986668211984
\]

and

\[
\boxed{
rac{T_{71}}{71^{25}}
\equiv32\pmod{71}.
}
\]

This agrees with the divided-Adams Hasse/Rayleigh coefficient computed independently from its recurrence.

## 3. Archimedean normalization

The target-scale ratio is

\[
\boxed{
\frac{T_{71}}{71^{35}}
=
\frac{1921017986668211984}{3255243551009881201}
=0.5901303409608938\ldots
}
\]

Thus the exact value lies comfortably inside the working absolute-constant conjecture.

On the weight-two q-line scale,

\[
\frac{T_{71}}{71^{34}}
=
\frac{1921017986668211984}{45848500718449031}.
\]

## 4. Simultaneous q-line calibration

The complete finite-boundary census gives

\[
B_+=B_-=0
\]

at `p=71`. The independent generic q-line census gives

\[
N_+=72,
\qquad
N_-=76,
\]

and hence

\[
\boxed{S_0=-710,\qquad S_\chi=284.}
\]

Therefore the crown at `p=71` is entirely generic-q-line, while the Airy trace has the exact value above.

This is a strong out-of-sample rejection of any proposed formula identifying either projector with the normalized Airy trace plus only finite-boundary terms: there are no finite-boundary terms at all, yet neither projector equals the Airy value under any uniform elementary normalization visible in the previous calibrations.

## 5. Scientific status

### Exact computer-assisted

- the displayed cyclotomic sum;
- the exact integer `T_71`;
- its p-adic valuation and normalized residue;
- the target-scale ratio;
- the simultaneous generic q-line projectors.

### Not proved uniformly

- the absolute Airy bound for all admitted primes;
- a generic q-line/Airy comparison theorem;
- the crown.

## 6. Verification

`exact_t71_airy_dickson_verify.py` recomputes `T_71`, verifies the Hasse residue and checks the exact rational normalizations.

Remote job: `6a64e739db23d7a7ec1cc5e0`.
