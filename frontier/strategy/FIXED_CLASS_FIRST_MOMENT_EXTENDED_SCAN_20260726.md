# Fixed-class first Cartier moment: exact extension through p=683

**Date:** 2026-07-26  
**Branch:** `gpt56/fortune-strategy-synthesis-audit-20260726`  
**Classification:** **EXACT COMPUTER-ASSISTED RESULT**.  
**Scope:** primes `p = 5 mod 6` with `383 <= p <= 683`, extending the predecessor exact moment scan through `p=379`.

## 1. Definitions

For a representative `a` of either square class in `F_p^*`, put

\[
N_a(p)=\#\{(c,d)\in\mathbf F_p^2:X^p+aX^3+cX+d\text{ irreducible}\},
\]

and

\[
M_a(p)=\sum_{X^p+aX^3+cX+d\ \mathrm{irreducible}}c\pmod p.
\]

Write `N_+,M_+` for `a=1` and `N_-,M_-` for the smallest quadratic nonresidue.

The diagnostic mod-12 mode is

\[
D_p=\begin{cases}
N_+-N_-\pmod p,&p\equiv5\pmod{12},\\
N_++N_-\pmod p,&p\equiv11\pmod{12}.
\end{cases}
\]

No theorem is asserted for `D_p`; it is recorded only because it survived the earlier exact range.

## 2. Exact results

| `p` | `N_+` | `N_-` | `M_+` | `M_-` | active mode | `D_p` |
|---:|---:|---:|---:|---:|:---:|---:|
| 383 | 316 | 328 | 271 | 166 | sum | 261 |
| 389 | 356 | 372 | 347 | 207 | difference | 373 |
| 401 | 362 | 370 | 75 | 56 | difference | 393 |
| 419 | 404 | 380 | 379 | 24 | sum | 365 |
| 431 | 422 | 322 | 108 | 112 | sum | 313 |
| 443 | 384 | 416 | 326 | 396 | sum | 357 |
| 449 | 408 | 424 | 443 | 119 | difference | 433 |
| 461 | 420 | 400 | 28 | 41 | difference | 20 |
| 467 | 444 | 410 | 458 | 329 | sum | 387 |
| 479 | 438 | 412 | 307 | 203 | sum | 371 |
| 491 | 504 | 456 | 276 | 441 | sum | 469 |
| 503 | 480 | 466 | 496 | 409 | sum | 443 |
| 509 | 470 | 468 | 207 | 333 | difference | 2 |
| 521 | 478 | 518 | 408 | 106 | difference | 481 |
| 557 | 506 | 528 | 104 | 521 | difference | 535 |
| 563 | 518 | 502 | 354 | 34 | sum | 457 |
| 569 | 542 | 436 | 258 | 155 | difference | 106 |
| 587 | 596 | 516 | 297 | 117 | sum | 525 |
| 593 | 520 | 514 | 574 | 119 | difference | 6 |
| 599 | 496 | 510 | 379 | 264 | sum | 407 |
| 617 | 488 | 600 | 299 | 151 | difference | 505 |
| 641 | 564 | 544 | 34 | 225 | difference | 20 |
| 647 | 536 | 618 | 354 | 8 | sum | 507 |
| 653 | 634 | 602 | 511 | 397 | difference | 32 |
| 659 | 570 | 602 | 28 | 472 | sum | 513 |
| 677 | 666 | 556 | 265 | 494 | difference | 110 |
| 683 | 624 | 622 | 510 | 65 | sum | 563 |

## 3. Ruling

For every one of the 54 class-slices in this extension,

\[
N_a(p)\not\equiv0\pmod p
\qquad\text{and}\qquad
M_a(p)\ne0.
\]

Thus the following empirical targets survive through `p=683`:

1. each fixed cubic square class has nonzero count residue modulo `p`;
2. each fixed class has nonzero first `c`-moment;
3. the mod-12 selected count mode `D_p` is nonzero.

The mod-12 mode comes close to zero:

\[
D_{509}=2,
\qquad
D_{593}=6.
\]

This weakens any expectation of a uniform size lower bound and reinforces that only exact nonvanishing could be relevant.

No result here proves uniform nonvanishing. The crown remains open.

## 4. Correctness and reproducibility

The scanner uses three exact layers:

1. `d -> -d` pairs fibres, with `d=0` excluded as reducible;
2. root and Frobenius-iterate gcd prefilters reject only fibres carrying an exhibited proper factor;
3. every survivor is fully factored by `python-flint`.

Hence the prefilters affect runtime only, not correctness.

Committed scanner:

`frontier/strategy/fixed_class_first_moment_extended_scan.py`

Remote jobs:

- `6a6648a4db23d7a7ec1ce911` — range `383..550`;
- `6a6648c17ef3c08464969df3` — range `551..700`.

A benchmark at `p=383`, square class, rejected `20,910` of `24,448` rootless half-fibres by exact small-degree gcd certificates before final factorisation and recovered

\[
N_+=316,
\qquad M_+=271.
\]

## 5. Scientific status

The extension strengthens the empirical credibility of the first-moment target but does not make the remaining theorem easier. The proved reduction in

`FIXED_CLASS_FIRST_MOMENT_AND_CYCLOTOMIC_TANGENT_WALL_20260726.md`

shows that uniform first-moment nonvanishing requires a genuinely new first-order cyclotomic/integral-Smith theorem, or an equivalent direct nonvanishing theorem for the two full-family Cartier boundary coefficients. Parity, discriminant mass, q-line cross-ratio symmetry and the refuted small-prime Cartier support cutoff do not supply it.
