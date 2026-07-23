# Unique top-weight extraction for the Adams irreducibility complex

**Date:** 2026-07-23  
**Status:** exact theorem for every prime `p>=5`, every `a in F_p^*`, and every extension field `F_(p^r)`. It proves that the normalized error `pN_a(p^r)-p^(2r)` is a Frobenius trace of weights at most three. The remaining open problem is a uniform bound on the effective virtual Betti degree, not the weight.

## 1. Original depressed cover

Let

`B_a=A^2_(c,d)`

and let `U_a` be the étale locus of

`X^p+aX^3+cX+d=0`.

On `U_a`, let `P_a` be the rank-`p` permutation sheaf on the roots and put

`W_a=psi^p(P_a)-P_a`.

For every unramified fibre with Frobenius permutation `sigma`,

`Tr(sigma|W_a)=p` if `sigma` is a `p`-cycle and `0` otherwise.

Therefore, over every `F_q` with `q=p^r`,

`boxed( pN_a(q)=Tr(Frob_q | RGamma_c(U_a,W_a)). )`  (1.1)

This is the original-cover version of the cyclic-Adams count bridge; no square-value projector is required.

## 2. Exact hook expansion

Let `V_i=exterior^i Std_p`, the hook representation indexed by

`(p-i,1^i)`,  `0<=i<=p-1`.

The Murnaghan–Nakayama rule gives

`chi_(V_i)(p-cycle)=(-1)^i`,

and every non-hook irreducible character vanishes on the `p`-cycle class. Since the Adams character is `p` on that class and zero elsewhere, character orthogonality gives:

### Theorem ATW.1 — exact Adams hook class

`boxed( W=sum_(i=0)^(p-1)(-1)^i V_i )`

in the rational representation ring of `S_p`.

In particular, the multiplicity of the trivial representation `V_0` is exactly one. The sign representation `V_(p-1)` also occurs once because `p-1` is even, but it is nontrivial under geometric `S_p` monodromy and does not contribute to top compactly supported cohomology on the original base.

## 3. Top compactly supported cohomology

The geometric monodromy of the depressed root cover is `S_p`. For a smooth geometrically connected surface and a finite-monodromy semisimple local system `L`, Poincare duality gives

`H_c^4(U_bar,L)=(L_bar_eta)_(pi_1)(-2)`,

where the subscript denotes geometric coinvariants. For semisimple finite monodromy, coinvariants and invariants have the same dimension.

By ATW.1,

`dim W^(S_p)=1`.

The corresponding constituent is the arithmetic trivial representation. Hence:

### Theorem ATW.2 — unique weight-four term

`boxed( H_c^4(U_(a,bar F_p),W_a)=Q_l(-2) )`

in the Grothendieck group, and

`Tr(Frob_(p^r)|H_c^4)=p^(2r).`

There is no other weight-four constituent.

## 4. Exact weight-three normalization

The virtual sheaf `W_a` is pure of weight zero: it is a virtual combination of finite-monodromy root local systems. Deligne's weight theorem gives weights at most `i` on `H_c^i(U_a,W_a)`.

Remove the unique top class and define

`C_a=RGamma_c(U_a,W_a)-Q_l(-2)[-4]`

in the Grothendieck group of arithmetic Frobenius complexes. Then every eigenvalue in `C_a` has weight at most three.

Combining with (1.1):

### Theorem ATW.3 — exact weight-three error complex

For every `r>=1`,

`boxed( pN_a(p^r)-p^(2r)=Tr(Frob_p^r|C_a), )`

where `C_a` has weights at most three.

Thus

`|pN_a(p^r)-p^(2r)|<=B_a(p) p^(3r/2)`

with `B_a(p)` equal to the effective total virtual Betti degree of `C_a`. The weight exponent `3/2` is a theorem; only uniform control of `B_a(p)` remains open.

## 5. Relation to the extremal/middle ledger

The exact Kummer, pair, and `D` sectors are explicit direct summands or virtual summands of `C_a` with effective `O(p)` traces. After subtracting them, the primitive middle residual remains a weight-at-most-three trace automatically.

Consequently the former Cyclic-Adams Weight-Three Lemma separates into:

1. **Weight statement:** now proved by ATW.3;
2. **Uniform complexity statement:** prove an absolute bound for the effective virtual Betti degree after the known extremal classes and elementary boundary classes are removed.

No further extension-field data are required to decide the weight.

## 6. Audit

`adams_top_weight_audit.py` verifies the complete hook expansion, trivial multiplicity, sign multiplicity, and p-cycle character identity by exact symmetric-group character calculations for every prime in its audit range. The extension-field census already checks numerically that the normalization in ATW.3 is exactly `pN_a(q)-q^2`.

## 7. Epistemic classification

- Adams p-cycle character: exact;
- hook expansion: exact character theory;
- unique trivial constituent: exact;
- top compactly supported Tate class: exact Poincare duality and finite monodromy;
- weights at most three after subtracting `q^2`: exact Deligne weight theorem;
- uniform effective virtual Betti bound: open;
- function-field `d=1` crown: open.
