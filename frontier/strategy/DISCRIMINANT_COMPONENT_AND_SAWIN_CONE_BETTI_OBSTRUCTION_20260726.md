# Ordinary discriminant components and the exact Sawin-cone Betti obstruction

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** function-field Fortune at `d=1`; exact aggregate `h=4` Sawin variety.  
**Status:** the geometric component and cone-transfer statements are **PROVED THEOREMS**. The numerical `p=11` and `p=13` Betti values are **EXACT COMPUTER-ASSISTED THEOREMS**, conditional only on the already committed exact primitive-hook certificates. The aggregate absolute-Betti route is refuted at the admitted prime `p=11`. The crown remains **OPEN**.

## 0. Main ruling

The compactified primitive hook classes computed in the preceding Cayley--Jacobian audit are not classes that a later discriminant boundary map may remove before reaching Sawin's cohomology. Sawin's actual affine variety at the Fortune centre is the diagonal-translation torsor over the affine cone on that same projective surface.

For every nontrivial ordinary `S_p` representation `rho`, if

\[
M_\rho=\operatorname{Hom}_{S_p}(\rho,H^2_{\mathrm{prim}}(Y_p,\mathbf Q_\ell)),
\]

then

\[
\boxed{
H_c^5(X_{p,p-4,0})_\rho\cong M_\rho(-1),
\qquad
H_c^6(X_{p,p-4,0})_\rho\cong M_\rho(-2),
}
\]

and all other `rho`-isotypic compactly supported cohomology groups vanish. Consequently

\[
\boxed{B(\rho)=2\dim M_\rho.}
\]

At `p=11`, the exact primitive profile therefore gives

\[
\boxed{B_{\mathrm{mid}}=82>10=p-1,}
\]

and the full nontrivial-hook contribution to `B_Lambda` is `84`. Hence the sufficient condition `B_Lambda<=p-1`, and also its sign-extracted variant `B_mid<=p-1`, are false for the actual Sawin variety at an admitted prime.

This is a theorem-level obstruction to the aggregate **absolute Betti** proof strategy. It is not a counterexample to the Fortune crown and does not obstruct a direct Frobenius-trace cancellation theorem.

## 1. Sawin's variety at the full cubic-tail interval

For the interval

\[
T^p-T+aT^3+bT^2+cT+d,
\]

the first `p-4` elementary symmetric coefficients of the ordered roots are fixed to zero. Sawin's affine variety is therefore

\[
X_p=X_{p,p-4,\mathbf 0}
=
\{e_1=e_2=\cdots=e_{p-4}=0\}\subset\mathbf A^p.
\]

Because `1,...,p-4` are invertible in characteristic `p`, Newton identities give

\[
X_p
=
\{s_1=s_2=\cdots=s_{p-4}=0\}.
\]

This is exactly the affine sparse ordered-root scheme already used in the programme.

## 2. Translation quotient and affine cone

Put

\[
H=\{s_1=0\},
\qquad
L=\mathbf A^1(1,\ldots,1),
\qquad
W=H/L.
\]

On the nested zero locus `s_1=...=s_(p-4)=0`, every remaining power sum is invariant under diagonal translation. Hence the quotient of `X_p` by `L` is

\[
C_p
=
\{s_2=s_3=\cdots=s_{p-4}=0\}\subset W.
\]

It is the affine cone on

\[
Y_p
=
\{s_2=s_3=\cdots=s_{p-4}=0\}\subset\mathbf P(W).
\]

The map

\[
q:X_p\longrightarrow C_p
\]

is an `S_p`-equivariant torsor under the diagonal additive group. The fibre group is fixed pointwise by `S_p`. Therefore

\[
\boxed{Rq_!\mathbf Q_\ell\cong\mathbf Q_\ell(-1)[-2]}
\]

equivariantly. This construction uses the genuine characteristic-`p` quotient and does not require an ordinary characteristic-zero lift of `W`.

## 3. Primitive cohomology passes into the cone twice

Let `C_p^\times=C_p\setminus\{0\}`. It is the `G_m`-bundle associated to `O_{Y_p}(-1)`. The cone vertex carries only the trivial `S_p` representation, so for nontrivial `rho`,

\[
R\Gamma_c(C_p)_\rho
\cong
R\Gamma_c(C_p^\times)_\rho.
\]

The total space `E=Tot(O_{Y_p}(-1))` has

\[
H_c^i(E)_\rho
\cong
H^{i-2}(Y_p)_\rho(-1).
\]

Use the localization sequence for the zero section `Y_p\subset E`. By the proved global smoothness and Lefschetz theorem, every nontrivial `rho` occurs only in `H^2_prim(Y_p)`. The hyperplane and top classes are trivial representations. It follows exactly that

\[
\boxed{
H_c^3(C_p)_\rho\cong M_\rho,
\qquad
H_c^4(C_p)_\rho\cong M_\rho(-1).
}
\]

Applying the translation torsor gives

\[
\boxed{
H_c^5(X_p)_\rho\cong M_\rho(-1),
\qquad
H_c^6(X_p)_\rho\cong M_\rho(-2).
}
\]

Since `dim X_p=4`, both degrees are included in Sawin's definition of `B(rho)`, which sums through degree `2 dim X_p-1=7`.

### Theorem 3.1 — exact nontrivial Betti transfer

For every nontrivial ordinary `S_p` representation `rho`,

\[
\boxed{
B(\rho)=2\dim\operatorname{Hom}_{S_p}
(\rho,H^2_{\mathrm{prim}}(Y_p)).
}
\]

There is no remaining discriminant or frequency-boundary differential that can reduce this intrinsic cohomology dimension: it is already the cohomology entering Sawin's constant.

## 4. Exact `p=11` obstruction

The committed exact primitive hook profile is

\[
(m_0,\ldots,m_{10})
=(0,0,0,0,0,6,14,12,6,3,1).
\]

Thus

\[
\sum_{i\text{ even}}m_i=21,
\qquad
\sum_{i\text{ odd}}m_i=21.
\]

The actual nontrivial-hook contribution to Sawin's aggregate constant is

\[
\boxed{2(21+21)=84.}
\]

The last hook is the sign representation. Removing it leaves primitive non-sign multiplicity mass `41`, hence

\[
\boxed{B_{\mathrm{mid}}=2\cdot41=82.}
\]

Since

\[
82>10=p-1,
\]

the sign-extracted absolute-Betti condition is false at `p=11`, an admitted prime.

## 5. Exact `p=13` obstruction

The committed exact primitive profile is

\[
(m_0,\ldots,m_{12})
=(0,0,0,0,0,11,35,51,49,34,16,4,0).
\]

Its parity masses are `100` and `100`, with no trivial or sign hook. Therefore

\[
\boxed{B_{\mathrm{mid}}=B_\Lambda=2(100+100)=400>12.}
\]

This is outside the admitted prime class, but it confirms that the large compactified primitive profile is the actual affine Sawin Betti mass, not a page awaiting a `188`-dimensional boundary cancellation.

## 6. Ordinary discriminant components

Let

\[
D_p^{\mathrm{red}}
=
\bigcup_{1\le i<j\le p}D_{ij},
\qquad
D_{ij}=Y_p\cap\{x_i=x_j\}.
\]

### 6.1 Reduction of one collision component

On `D_12`, subtract the common value `x_1=x_2` by diagonal translation. The first two coordinates become zero. Write the remaining `n=p-2` coordinates as `z_1,...,z_n`. They satisfy

\[
\sum_jz_j^m=0
\qquad(1\le m\le n-2).
\]

Newton identities give

\[
e_1(z)=\cdots=e_{n-2}(z)=0,
\]

so their monic root polynomial has the form

\[
\boxed{Z^n+AZ+B.}
\]

### 6.2 Full monodromy

Restrict to the line `A=1`. The family is the splitting cover of

\[
\phi(Z)=Z^n+Z.
\]

Here `n=p-2`, so `p` divides neither `n` nor `n-1`. The derivative

\[
\phi'(Z)=nZ^{n-1}+1
\]

has `n-1` simple roots. At a critical point `alpha`,

\[
\phi(\alpha)=\frac{n-1}{n}\alpha,
\]

so all finite critical values are distinct. Their inertia groups are transpositions. Infinity is tamely totally ramified and supplies an `n`-cycle. The product of the finite transpositions is that `n`-cycle, so their transposition graph is connected; transpositions on the edges of a connected graph generate `S_n`.

Therefore the geometric monodromy is `S_n`, the ordered-root cover is connected, and `D_12` is geometrically irreducible. Every `D_ij` is its `S_p` translate, and the setwise stabilizer is

\[
S_2\times S_{p-2}.
\]

### Theorem 6.1 — discriminant component representation

The irreducible components of the reduced ordinary discriminant are indexed by unordered pairs, and

\[
\boxed{
H^0(D_p^{\mathrm{red}})
\cong
H^2(D_p^{\mathrm{red}})(1)
\cong
\operatorname{Ind}_{S_2\times S_{p-2}}^{S_p}\mathbf1.
}
\]

Young's rule gives

\[
\boxed{
\operatorname{Ind}_{S_2\times S_{p-2}}^{S_p}\mathbf1
\cong
S^{(p)}\oplus S^{(p-1,1)}\oplus S^{(p-2,2)}.
}
\]

Its hook multiplicities are

\[
\boxed{(1,1,0,\ldots,0).}
\]

Thus the ordinary pair-collision divisor has no hook support in any degree `i>=2`, and in particular cannot act on the exact primitive profiles supported in degrees `i>=5` at `p=11` and `p=13`.

## 7. Direct Frobenius trace identity

Although the unsigned Betti route is closed, the cone calculation also gives an exact trace reduction. For every nontrivial `rho`,

\[
\sum_j(-1)^j\operatorname{Tr}
(F\mid H_c^j(X_p)_\rho)
=
\boxed{p(p-1)\operatorname{Tr}(F\mid M_\rho)}.
\]

Indeed the two contributions are

\[
-p\operatorname{Tr}(F\mid M_\rho)
+p^2\operatorname{Tr}(F\mid M_\rho).
\]

After trivial and sign extraction, put

\[
T_{\mathrm{mid}}(p)
=
\sum_{i=1}^{p-2}(-1)^i
\operatorname{Tr}
\left(F\mid
\operatorname{Hom}_{S_p}
(\wedge^i\mathrm{Std},H^2_{\mathrm{prim}}(Y_p))
\right).
\]

Then

\[
\boxed{E_{\mathrm{mid}}=p(p-1)T_{\mathrm{mid}}(p).}
\]

If

\[
S_{\mathrm{sgn}}=s_p p^2(p-1),
\qquad s_p\in\{0,+1,-1\},
\]

the crown follows from the direct inequality

\[
\boxed{T_{\mathrm{mid}}(p)>-p(p+1+s_p).}
\]

In particular, the marginal class `p=23 mod 24`, where `s_p=-1`, requires

\[
\boxed{T_{\mathrm{mid}}(p)>-p^2.}
\]

This is now the correct quantitative target.

## 8. Scientific ruling

### PROVED THEOREM

1. Sawin's affine Fortune variety is the diagonal `A^1` torsor over the affine cone on `Y_p`.
2. Every nontrivial primitive hook multiplicity occurs twice in Sawin compactly supported cohomology, in degrees `5` and `6`.
3. `B(rho)=2 dim M_rho` for every nontrivial `rho`.
4. Every ordinary pair-collision component is geometrically irreducible.
5. The ordinary discriminant component representation has hook support only in degrees `0` and `1`.
6. The exact Frobenius trace reduction is `E_mid=p(p-1)T_mid`.

### EXACT COMPUTER-ASSISTED THEOREM

1. At `p=11`, `B_mid=82` and the nontrivial contribution to `B_Lambda` is `84`.
2. At `p=13`, `B_mid=B_Lambda=400` on the nontrivial hooks.
3. The unordered-pair hook profile is exactly `(1,1,0,...)` by exact character inner products at both primes.

### REFUTED

1. The programme can prove `B_Lambda<=p-1` by cancelling the compactified primitive Jacobian mass with a later discriminant/Gysin differential.
2. After sign extraction, the actual mid-hook Sawin constant might equal the `p=11` raw-bar value `10`.
3. The ordinary discriminant divisor can remove any of the high primitive hooks.
4. The exact aggregate absolute-Betti route can prove the crown uniformly: it already fails numerically at the admitted prime `p=11`.

### OPEN

1. A Frobenius-compatible parity correspondence or direct trace theorem for `T_mid(p)`.
2. A Fourier--Cayley/Airy identification capable of proving the displayed `O(p^2)` one-sided trace bound despite the large unsigned Betti mass.
3. The crown.

## 9. Next highest-value theorem

> **Primitive parity Frobenius theorem.** Construct a Frobenius-compatible correspondence, filtration or Fourier--Cayley identity on the even and odd primitive hook multiplicity spaces of `Y_p` and prove
> \[
> T_{\mathrm{mid}}(p)>-p(p+1+s_p)
> \]
> for every admitted prime. In the class `p=23 mod 24`, prove the strict bound `T_mid(p)>-p^2`.

The exact profiles have equal total even and odd primitive multiplicities at `p=11` and `p=13`. This makes a parity-level direct trace theorem structurally plausible, but equality of dimensions alone is not a Frobenius theorem.

## 10. Verification

Run

```bash
python frontier/strategy/discriminant_component_sawin_cone_verify.py
```

It writes

```text
frontier/strategy/discriminant_component_sawin_cone_results_20260726.json
```

and verifies the branch arithmetic, exact unordered-pair hook support, cone/torsor degree bookkeeping, and the `p=11/p=13` Betti obstructions.
