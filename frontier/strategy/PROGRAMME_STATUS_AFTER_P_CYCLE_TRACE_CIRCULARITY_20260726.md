# Programme status after the p-cycle trace circularity theorem

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** function-field Fortune `d=1`.  
**Crown:** **OPEN**.  
**Aggregate absolute-Betti route:** **CLOSED**.  
**Primitive p-cycle fixed-point route:** **CLOSED AS AN INDEPENDENT REDUCTION**.

## 1. New decisive theorem

The alternating hook projector is the exact `p`-cycle projector, but its affine fixed locus is the original irreducible count:

\[
\sum_i(-1)^i\operatorname{Tr}(F\mid M_i)
=\operatorname{Tr}(F\sigma\mid H^2_{prim}(Y_p)),
\]

\[
\#\operatorname{Fix}(F\sigma\mid X_p)=pI_4+p.
\]

Consequently

\[
T_{mid}=\frac{I_4+1-p^3}{p-1}-s_pp,
\]

and

\[
\boxed{
T_{mid}>-p(p+1+s_p)
\iff I_4>p-1.
}
\]

The proposed primitive trace inequality is exactly the crown, not a reduced theorem.

## 2. Exact quantization

Let `N2` be the quadratic normal-form count and `N+`, `N-` the two depressed cubic counts. Then

\[
I_4=(p-1)+p(p-1)N_2+\frac{p(p-1)}2(N_++N_-),
\]

so

\[
\boxed{
T_{mid}=p\left(N_2+\frac{N_++N_-}{2}-(p+1+s_p)\right).
}
\]

The crown is exactly

\[
N_2+\frac{N_++N_-}{2}>0.
\]

A failure prime would have to satisfy the simultaneous exact vanishing

\[
N_2=N_+=N_-=0.
\]

## 3. Exact q-line synthesis

The invariant q-line projector satisfies

\[
\boxed{
T_{mid}
=p\left(N_2-3-s_p+\frac{B_++B_-}{2}\right)-\frac{S_0}{2}.
}
\]

Thus the aggregate direct-trace route and the previously isolated invariant q-line error problem are the same wall. The anti-invariant trace `S_chi` cancels from the full aggregate formula.

## 4. Airy comparison

At `p=11`, `T_mid=22` equals the normalized cubic Airy trace. Exact regressions refute this as a uniform identity:

\[
p=17:\quad -17\ne29,
\]

\[
p=23:\quad -92\ne-561/23.
\]

Any surviving Fourier--Cayley relation must include a substantial complementary generic q-line term.

## 5. Exhausted routes

Do not continue with:

- aggregate unsigned Betti bounds;
- discriminant cancellation of the actual Sawin Betti mass;
- another alternating-hook projector calculation;
- direct `F sigma` fixed-point enumeration as though it were a reduction;
- identifying the `p=11` Airy coincidence uniformly;
- relative configuration face maps between different hook labels;
- fixed boundary or fixed low-height q cells;
- low-degree Artin--Schreier Tschirnhaus transforms;
- raw prime censuses as evidence for a uniform theorem.

## 6. Honest remaining mathematical wall

A genuine advance must prove one of the following without reconstructing the unknown count tautologically:

1. **Invariant q-line nonsaturation:** exclude
   \[
   S_0=p\bigl(2(p-2)+B_++B_-\bigr)
   \]
   whenever `N2=0`.
2. **Characteristic-p Frobenius correlation / integral Smith defect:** pair the large even and odd modules at the level of Frobenius traces with a strict residual saving.
3. **Mass formula or exact invariant:** exclude simultaneous vanishing of `N2`, `N+`, and `N-`.
4. **Constructive theorem:** produce one cubic-tail irreducible uniformly by a genuinely new construction.

All presently available routes in the repository either reduce to one of these statements or have an exact no-go theorem. This is the decisive stopping point for the current programme.

## 7. Verification

```bash
python frontier/strategy/p_cycle_projector_fixed_point_bridge_verify.py

g++ -O3 -std=c++17 \
  frontier/strategy/p_cycle_fixed_point_census_verify.cpp \
  -o /tmp/p_cycle_census
/tmp/p_cycle_census --extended
```

The exhaustive census passes at `p=5,7,11,13,17,23`.
