# PREREG-8: independent verification of the low-rank Airy spectra

**Date:** 2026-07-24  
**Base commit:** `f376dd54df2cabe0ca323d7609b9eaef02afdd4e`  
**Scope:** function-field \(d=1\) Fortune sibling; primes \(p=17,23,29\).  
**Status:** exact computer-assisted verification complete.

## 1. Quarantine design

The spectra in `AIRY_ODD_POWER_SPECTRA_AUDIT_20260723.md` were converted into
six exact integer predictions for
\(\operatorname{Tr}(F^3\mid U_k)\) before the new measurement. Five normalized
first-trace identities were also locked against the pre-existing level-one
integers.

The verifier then used a separately written implementation:

1. an independently selected irreducible cubic for \(\mathbf F_{p^3}\);
2. scalar arithmetic modulo coefficient primes \(\ell\equiv1\pmod p\);
3. a separable three-dimensional \(p\)-ary DFT;
4. the complete-homogeneous recurrence with \(\alpha\beta=p^3\);
5. signed CRT over nine coefficient primes;
6. a tenth coefficient prime excluded from reconstruction.

This is algorithmically independent at the implementation level, although it
shares the mathematical identification of the DFT/recurrence output with the
Airy symmetric-power trace.

## 2. Locked predictions and measurements

| space | predicted and measured \(\operatorname{Tr}(F^3)\) | 10th prime | match |
|---|---:|:---:|:---:|
| \(U_{17}\) | \(-255944298171217376101202104309234\) | pass | pass |
| \(U_{15}\) | \(0\) | pass | pass |
| \(U_{23}\) | \(24420035557874291486685783320490312291163556150933\) | pass | pass |
| \(U_{21}\) | \(1811942529812491726048499913466581810789054457\) | pass | pass |
| \(U_{29}\) | \(-624252554084396763440186646610590357883743693997978553242566200210\) | pass | pass |
| \(U_{27}\) | \(52044691388847887475857027569042615828726415261418059755550020\) | pass | pass |

The DFT anchors
\(D(0,0,0)=0\), \(\sum D=p^3\), and \(\sum D^2=p^6\) passed at all three
primes and all coefficient moduli.

## 3. Independent algebraic checks

The prediction formulas were recomputed independently from exact rational
arithmetic:

- rank two:
  \(p_3=e_1^3-3e_1\);
- rank three with central eigenvalue \(+1\):
  \(p_3=1+t^3-3t\);
- reciprocal rank four:
  \(p_3=-a^3+3ab-3a\).

All six values agree with both checkpoint files and with the spectra already
committed at the base commit.

## 4. Self-duality status

Self-duality is not merely an undocumented assumption. Section 4 of
`AIRY_ODD_POWER_SPECTRA_AUDIT_20260723.md` records the alternating pairing on
odd symmetric powers, the cup-product sign change in degree one, and the
resulting symmetric pairing with similitude \(p^{k+1}\) on \(U_k\). The
\(\mu_3\)-invariant summand is nondegenerate because \(3\) is invertible in the
coefficient field. The reciprocal/palindromic reconstruction therefore has a
stated geometric basis in the repository.

## 5. Statistical correction independently checked

For \(n=4806\) independent standard normals,
\[
 \Pr(\max |Z_i|\le x)=(2\Phi(x)-1)^n.
\]
Direct numerical integration gives
\[
 \mathbb E\max |Z_i|=3.8418852669.
\]
At the observed maximum \(3.4272555277\), the CDF is \(0.05334\). The sweep
therefore gives no directional evidence that the normalized Airy sequence is
unbounded. This confirms the correction already entered in
`AIRY_SWEEP_SIGN_AND_TARGET_AUDIT_20260723.md`.

## 6. Ruling

The rank-\(2,3,4\) spectra are now supported by two exact implementations and
by independent algebraic reconstruction. Residual risk is confined mainly to
a shared conceptual convention in the DFT-to-cohomology trace identification;
the existing \(p=5\) brute-force chain and level-one anchors materially reduce
that risk.

The result strengthens the computational theorem. It does not prove the
uniform absolute trace bound or the application bridge.
