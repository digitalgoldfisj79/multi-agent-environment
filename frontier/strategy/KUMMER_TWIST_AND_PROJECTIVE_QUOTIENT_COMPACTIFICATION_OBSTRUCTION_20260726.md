# Kummer square-class twists and the projective quotient compactification obstruction

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Scope:** proposed paired square-class compactification after the secondary Hattori--Stallings/Artin--Schreier construction.  
**Status:** the Kummer classification, sign-twist criterion, common quotient, fixed-locus theorem, general-type quotient and point-count ledgers below are **PROVED**. The function-field `d=1` crown remains **OPEN**.

## 1. Fixed cubic slices and scalar weights

Put

\[
n=p-3
\]

and let `X_a` be the fixed depressed ordered-root slice

\[
e_1=\cdots=e_{p-4}=0,
\qquad e_{p-3}=a\ne0,
\qquad e_{p-2}=0.
\]

The remaining coefficients are

\[
e_{p-1}=c,
\qquad e_p=-d.
\]

Scalar dilation sends

\[
x_i\longmapsto \lambda x_i.
\]

Hence

\[
a\longmapsto \lambda^{p-3}a=\lambda^n a,
\]

and, on a fixed `a`-fibre, the stabilizer `mu_n` acts by

\[
\boxed{
 c\longmapsto \zeta^2c,
 \qquad
 d\longmapsto \zeta^3d
}
\qquad(\zeta^n=1).
\]

The cyclic transfer `t` used in the Artin--Schreier coordinate has degree `n`. Therefore both `t/a` and

\[
y=-a^{-1}\sum_jj\sigma^j(t)
\]

are invariant under scalar transport between fibres. Thus

\[
g=y^p-y
\]

is invariant under the full Kummer scaling group.

For admitted primes `p=5 mod 6`, one has

\[
\gcd(3,n)=1.
\]

Every irreducible member has `d != 0`, so the `mu_n` action is free on the irreducibility level `g=1`.

## 2. The two arithmetic classes are Kummer twists

The geometric fibres `X_a` are forms of one another under `mu_n`. Kummer theory gives

\[
H^1(\mathbf F_p,\mu_n)
\cong
\mathbf F_p^*/(\mathbf F_p^*)^n.
\]

Since

\[
\gcd(n,p-1)=\gcd(p-3,p-1)=2,
\]

this group has exactly two elements. They are precisely the square and nonsquare classes of `a`.

Choose `lambda` with

\[
\lambda^n=a.
\]

The descent cocycle is

\[
\gamma=\lambda^{p-1}\in\mu_n.
\]

In exponent notation `mu_n ~= Z/n`, Frobenius coboundaries are multiples of

\[
p-1\equiv2\pmod n.
\]

Thus the two cohomology classes are the even and odd exponent classes.

### Theorem 2.1 -- exact sign-twist criterion

The sign element `-1 in mu_n` has exponent

\[
\frac n2=\frac{p-3}{2}.
\]

It represents the nontrivial square-class form if and only if this exponent is odd, equivalently

\[
\boxed{p\equiv1\pmod4.}
\]

For

\[
\boxed{p\equiv3\pmod4,}
\]

the sign cocycle is a coboundary. The nonsquare fibre is not the quadratic sign twist of the square fibre; it requires an odd-exponent element of `mu_n`, necessarily of order greater than two.

Consequently the previously proposed universal two-eigenspace quadratic-twist picture is false on half of the admitted primes. In particular, it cannot explain the empirical switch between class sum and class difference according to `p mod 12`.

## 3. The correct common quotient

Let

\[
R_a=X_a/C_p
\]

be the root-cycle quotient, and let

\[
C_{a,1}=\{g=1\}\subset R_a.
\]

The full Kummer group `mu_n` acts on the geometric square-class model and preserves `g`. Put

\[
U_p=R_1/\mu_n,
\qquad
D_p=C_{1,1}/\mu_n.
\]

For a rational point of either quotient, the fibre is a `mu_n`-torsor. Its class lies in the two-element group

\[
H^1(\mathbf F_p,\mu_n).
\]

Exactly one of the two arithmetic forms has rational lifts, and the number of such lifts is

\[
\#\mu_n(\mathbf F_p)=\gcd(n,p-1)=2.
\]

Therefore:

### Theorem 3.1 -- common Kummer quotient counts

\[
\boxed{
\#D_p(\mathbf F_p)=\frac{N_++N_-}{2}
}
\]

and

\[
\boxed{
\#U_p(\mathbf F_p)=\frac{p-1}{2}(N_++N_-).
}
\]

Thus the common quotient does package the positivity target, but only as the existing class-sum count. A rational-point theorem for `D_p` is exactly the assertion that at least one cubic square class contains an irreducible.

The class difference is not ordinary cohomology of this quotient. It is a Kummer-local-system trace on `U_p`. Complete averaging in the cubic coefficient has only the two arithmetic Mellin modes

\[
N_++N_-
\qquad\text{and}\qquad
N_+-N_-.
\]

Using the proved q-line ledger,

\[
N_++N_-
=2(p-2)+B_++B_--\frac{S_0}{p},
\]

\[
N_+-N_-
=B_+-B_--\frac{S_\chi}{p}.
\]

Hence the corrected Kummer decomposition is exactly the previously isolated invariant/anti-invariant q-line decomposition. It creates no third or smaller Frobenius target.

## 4. Natural projective compactification

Let

\[
\mathscr Y_p
=
\{s_2=s_3=\cdots=s_{p-4}=0\}
\subset\mathbf P(W)
\]

be the smooth projective sparse ordered-root surface. The homogeneous function

\[
A=s_{p-3}
\]

is well-defined on the translation quotient because all lower power sums vanish. The open set `A != 0`, after quotient by the root cycle, is the common Kummer quotient `U_p` above.

Put

\[
\mathscr Q_p=\mathscr Y_p/C_p.
\]

This is the natural proper compactification of `U_p`.

## 5. The root cycle has one projective fixed point

Let `sigma` be the standard `p`-cycle. In characteristic `p`, its action on

\[
W=\{\sum x_i=0\}/\mathbf F_p(1,\ldots,1)
\]

has a one-dimensional fixed space. Indeed, a fixed class satisfies

\[
x_{i+1}-x_i=t
\]

for one constant `t`. Modulo diagonal translation and projective scaling, the unique nonzero solution is

\[
\boxed{q=[0,1,2,\ldots,p-1].}
\]

For every `1 <= m <= p-2`,

\[
\sum_{i\in\mathbf F_p}i^m=0.
\]

Therefore `q` lies on `mathscr Y_p`, and it is the complete fixed locus of every nonidentity element of `C_p`.

### Theorem 5.1 -- quasi-etale general-type quotient

The quotient map

\[
\mathscr Y_p\longrightarrow\mathscr Q_p
\]

is free in codimension one and ramified only at `q`. Hence it is quasi-etale in codimension one.

The canonical class of the smooth complete intersection is

\[
K_{\mathscr Y_p}
=
\mathcal O_{\mathscr Y_p}
\left(\frac{(p-7)(p-2)}2\right).
\]

For every admitted prime `p>=11` this is ample. Since there is no divisorial ramification,

\[
K_{\mathscr Y_p}=\pi^*K_{\mathscr Q_p}
\]

as rational canonical divisors. It follows that `K_(mathscr Q_p)` is ample and

\[
\boxed{\kappa(\mathscr Q_p)=2.}
\]

Every regular proper compactification of the same function field is therefore birationally of general type. There is no alternative Fano or rationally connected compactification of the common quotient hiding behind a different boundary choice.

## 6. Exact compactified point-count ledger

A rational point of `mathscr Q_p` is a `C_p`-orbit on `mathscr Y_p` stable under Frobenius.

Away from `q`, the action is free. Such a point has a unique shift

\[
r\in\mathbf F_p
\]

with

\[
F(x)=\sigma^r x.
\]

For `r != 0`, it is an irreducible affine-equivalence class. For each fixed `r != 0`, every nonlinear irreducible affine orbit contributes exactly one quotient point.

The proved affine-orbit decomposition shows that the nonlinear irreducible affine orbits are counted by

\[
W_p=N_2+\frac{N_++N_-}{2}.
\]

For `p>5`, there is no free `r=0` orbit. Indeed, if

\[
f=X^p+aX^3+bX^2+cX+d
\]

splits and

\[
h(X)=aX^3+bX^2+(c+1)X+d
\]

is nonzero, all distinct roots of `f` lie among the at most three roots of `h`. The logarithmic-derivative argument gives a left side of degree at most five and a right side of degree at least `p`, impossible for `p>5`. If `h=0`, the unique projective configuration is `X^p-X`, namely `q`. Purely inseparable diagonal configurations disappear in the translation quotient.

The entire linear Artin--Schreier orbit also compactifies to the single fixed point `q`; its different Frobenius cocycles are not distinct coarse quotient points because the stabilizer is all of `C_p`.

Therefore:

### Theorem 6.1 -- compactified quotient count

For every `p>5`,

\[
\boxed{
\#\mathscr Q_p(\mathbf F_p)
=1+(p-1)W_p.
}
\]

The boundary `A=0` has

\[
\boxed{
\#(\mathscr Q_p\setminus U_p)(\mathbf F_p)
=1+(p-1)N_2,
}
\]

while

\[
\boxed{
\#U_p(\mathbf F_p)
=\frac{p-1}{2}(N_++N_-).
}
\]

These three formulas are mutually exact.

## 7. Why the standard point-congruence route does not prove the crown

The compactified formula gives

\[
\#\mathscr Q_p(\mathbf F_p)
\equiv1-W_p\pmod p.
\]

Thus a standard Esnault/Witt-type congruence

\[
\#\mathscr Q_p(\mathbf F_p)\equiv1\pmod p
\]

would imply only

\[
W_p\equiv0\pmod p.
\]

That is compatible with the failure value `W_p=0`. It is also compatible with positive values: the exact census at `p=17` has

\[
W_{17}=17
\]

and therefore

\[
\#\mathscr Q_{17}(\mathbf F_{17})
=273
\equiv1\pmod{17}.
\]

Hence even a successful standard proper-point congruence would not distinguish the crown from its exact failure configuration.

A boundary-subtracted congruence gives only

\[
\#U_p(\mathbf F_p)
=\frac{p-1}{2}(N_++N_-),
\]

which is the original positivity target and, through the q-line ledger, exactly strict invariant nonsaturation.

## 8. Decisive ruling

### Proved

1. The square classes are the two Kummer forms in `H^1(F_p,mu_(p-3))`.
2. The nonsquare class is a sign twist only for `p=1 mod 4`.
3. The correct common quotient has point count `(N_++N_-)/2` on the irreducibility level.
4. Its class difference is a Kummer-local-system trace, not an ordinary compactification eigenspace.
5. The natural proper quotient has exactly one wild fixed point and is of general type.
6. Its exact point count is `1+(p-1)W_p`.
7. A standard mod-`p` rational-point congruence cannot exclude `W_p=0`.

### Closed

1. A universal quadratic-twist compactification with two ordinary Frobenius eigenspaces.
2. Explaining the mod-12 active mode by the scalar sign involution.
3. Obtaining the crown from a Fano/rationally connected compactification of the common quotient.
4. Obtaining the crown from a standard `#X = 1 mod p` theorem.
5. Treating the common quotient point problem as smaller than invariant q-line nonsaturation.

### Remaining theorem

The common quotient remains a valid geometric carrier, but its required statement is exactly

\[
\boxed{\#U_p(\mathbf F_p)>0,}
\]

or equivalently

\[
\boxed{N_++N_->0.}
\]

A useful continuation would need a genuinely new one-sided compactly-supported Frobenius theorem for this specific general-type Kummer quotient. Ordinary twist decomposition, proper point congruences and boundary bookkeeping do not provide it.

## 9. Verification

Run

```bash
python frontier/strategy/kummer_twist_compactification_verify.py
```

The frozen output is

`frontier/strategy/kummer_twist_compactification_results_20260726.json`.
