# Exact normal-form cell ledger for the two arithmetic classes

**Date:** 2026-07-24  
**Branch:** `gpt56/d1-main-twisted-descent-20260724`  
**Scope:** finite normalization layer in the function-field `d=1` application theorem.  
**Status:** all algebraic statements below are **PROVED**. This closes the generic coefficient-orbit normalization; the cohomological vanishing-cycle comparison and the boundary traces remain **OPEN**.

## 0. Setup

Fix an odd prime `p>=5`, a nonzero cubic coefficient

\[
a\in\mathbf F_p^*,
\]

and the depressed sparse family

\[
F_{a,c,d}(X)
=X^p+aX^3+cX+d.
\]

The irreducible count

\[
N_a(p)
=
\#\{(c,d)\in\mathbf F_p^2:F_{a,c,d}\text{ irreducible}\}
\]

depends only on the square class

\[
A=\chi(a)\in\{+1,-1\}.
\]

Choose once and for all a nonsquare

\[
\eta\in\mathbf F_p^*.
\]

## 1. The `q` coordinate

For `c!=0`, define

\[
\boxed{q=-3/c.}
\]

This is a bijection

\[
\mathbf F_p^*\longleftrightarrow\mathbf F_p^*.
\]

Put

\[
r=-\frac{c}{3a}=\frac1{aq}.
\]

The arithmetic cell sign is

\[
\boxed{
\varepsilon=\chi(r)=\chi(aq)=A\chi(q).
}
\]

Thus, for a fixed arithmetic class `A`, the nonzero-`c` coefficients occupy exactly the graph

\[
\varepsilon=A\chi(q)
\]

inside the `2(p-1)` pairs `(q,epsilon)`. The two values `A=+1,-1` partition all cells exactly once.

## 2. Split cell

Suppose

\[
\varepsilon=+1.
\]

Choose

\[
\lambda\in\mathbf F_p^*,
\qquad
\lambda^2=r=\frac1{aq}.
\]

Substitute

\[
X=\lambda Z
\]

and divide by `lambda`. Since `lambda^p=lambda`,

\[
\frac{F_{a,c,d}(\lambda Z)}{\lambda}
=Z^p+a\lambda^2Z^3+cZ+d/\lambda.
\]

Using

\[
a\lambda^2=q^{-1},
\qquad
c=-3q^{-1},
\]

one obtains

\[
\boxed{
G_{q,+,\delta}(Z)
=Z^p+q^{-1}Z^3-3q^{-1}Z+\delta,
\qquad
\delta=d/\lambda.
}
\]

The map `d -> delta` is a bijection of `F_p`. Root scaling and multiplication by a nonzero scalar preserve irreducibility. Hence

\[
\#\{d:F_{a,c,d}\text{ irreducible}\}
=
\#\{\delta:G_{q,+,\delta}\text{ irreducible}\}.
\]

Multiplying by `q` and, when `q!=2`, reparametrizing the constant as

\[
-(q-2)t
\]

gives the standard split cover

\[
qZ^p+Z^3-3Z-(q-2)t.
\]

## 3. Nonsplit cell

Suppose

\[
\varepsilon=-1.
\]

Then `r/eta` is a square. Choose

\[
s\in\mathbf F_p^*,
\qquad
r=\eta s^2.
\]

Substitute

\[
X=sZ
\]

and divide by `s`. Since

\[
a s^2=(\eta q)^{-1},
\qquad
c=-3q^{-1},
\]

one obtains the `F_p`-rational nonsplit normal form

\[
\boxed{
G_{q,-,\delta}(Z)
=Z^p+(\eta q)^{-1}Z^3-3q^{-1}Z+\delta,
\qquad
\delta=d/s.
}
\]

Again `d -> delta` is a bijection and

\[
\#\{d:F_{a,c,d}\text{ irreducible}\}
=
\#\{\delta:G_{q,-,\delta}\text{ irreducible}\}.
\]

Over `F_{p^2}`, adjoining `sqrt(eta)` identifies this family with the split family by root scaling. The nontrivial Galois element changes the square root's sign, producing the arithmetic quadratic twist recorded in the hook ledger.

The precise signs in alternative nonsplit formulas depend on replacing `eta` by another fixed nonsquare or changing `Z` to `-Z`; the cell count and the character rule `epsilon=A chi(q)` are invariant.

## 4. Exact assembly of `N_A`

Define

\[
I_\varepsilon(q)
=
\#\{\delta\in\mathbf F_p:
G_{q,\varepsilon,\delta}\text{ irreducible}\}.
\]

Let

\[
I_A(\infty)
=
\#\{d:X^p+aX^3+d\text{ irreducible}\},
\qquad \chi(a)=A.
\]

Then

\[
\boxed{
N_A(p)
=I_A(\infty)
+
\sum_{q\in\mathbf F_p^*}
I_{A\chi(q)}(q).
}
\]

This identity includes the algebraic `q=2` cell. For the cohomological generic chart one separates it:

\[
\boxed{
N_A(p)
=I_A(\infty)
+I_{A\chi(2)}(2)
+
\sum_{q\in\mathbf F_p^*\setminus\{2\}}
I_{A\chi(q)}(q).
}
\]

Thus the finite normalization from the geometric cell system to either arithmetic coefficient class is exact and coefficient-free.

## 5. Relation with the fixed-`q` hook trace

For `q!=2`, multiply `G_{q,+,delta}` by `q` and write the constant as `-(q-2)t`. The map `delta -> t` is bijective. The alternating hook local system on the root cover has trace `p` on irreducible fibres and zero otherwise. Therefore its `F_p` point sum is exactly

\[
p I_+(q).
\]

The nonsplit cell is the corresponding quadratic-twist reading of the same geometric root cover. Hence the two arithmetic classes are assembled by selecting, at each `q`, the reading

\[
\varepsilon=A\chi(q).
\]

This is the exact finite character projector that the final Airy-to-hook comparison must carry.

## 6. Boundary meanings

The two non-generic coefficient loci now have unambiguous meanings.

### `q=infinity`

This is exactly

\[
c=0,
\]

with count `I_A(infinity)`.

### `q=2`

This is exactly

\[
c=-3/2.
\]

The change from `delta` to the critical-value coordinate `t` degenerates because `q-2=0`; the cell remains an ordinary finite coefficient slice and must be attached separately.

The discriminant fibres `t=+1,-1` belong to the compactification of every generic split root cover. The nonsplit reading carries their quadratic arithmetic descent.

## 7. What this closes

### PROVED

1. The exact coefficient map `c <-> q`.
2. The exact split/nonsplit criterion `epsilon=A chi(q)`.
3. Explicit `F_p`-rational normal forms for both readings.
4. Bijection of constant parameters and preservation of irreducibility.
5. The complete finite assembly of each arithmetic class from the `q` cells and `q=infinity`.

### STILL OPEN

1. The iterated vanishing-cycle comparison identifying the Airy virtual module with the load-bearing hook surface term.
2. Exact cohomological signs and Tate twists of `q=2`, `q=infinity`, discriminant and punctual cones.
3. The final quantitative implication from the transported trace estimate to `N_A notin 2p Z`.

## 8. Verification

`normal_form_cell_verify.py` independently checks at `p=5,7,11` that:

- every pair `(A,c!=0)` maps to a unique `(q,epsilon)` and the two classes partition all `2(p-1)` cells;
- direct irreducible counts agree before and after the split or nonsplit normalization for every cell;
- the assembled counts reproduce the committed values of `N_A`.

This is a structural regression of the formulas, not a new prime sweep.
