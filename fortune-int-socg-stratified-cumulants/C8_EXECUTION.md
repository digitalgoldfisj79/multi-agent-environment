# C8 execution — conditional bridge and diagnostics

**Status:** `PASSED_CONDITIONAL_AND_DIAGNOSTIC`

The inherited row-uniform Hardy--Littlewood factorial-moment hypothesis through order `Theta(log X)`, with the registered exponentially small aggregate error, remains a complete conditional bridge to `INT-AOD`. It is not an established theorem for the primorial path.

Exact execution checks include:

- the corrected factorial-to-ordinary Stirling transform;
- output-prime-power subtraction at the `INT-SCME` scale;
- prime-modulus primorial-walk Parseval and collision bounds;
- local edge-kernel diagnostics;
- exact selected-centre occupancy panels for `X=100,150,200,250,300`;
- additive-character traces along the primorial walk for `X=100,200,400,800`.

The selected-centre panels contain no zero row in the tested range. Cumulants vary in sign and magnitude across small strata, confirming that fitted finite-panel temperatures or fixed-order extrapolation are inadmissible. The local edge diagnostic stays well below `X/(log X)^2` on the tested panels. Prime-modulus traces show nontrivial fluctuations, while the exact averaged energy theorem remains valid.

No finite computation is promoted into an asymptotic statement. The diagnostics support the registered decomposition but do not prove `INT-SCME`, `INT-LCSK`, `INT-PWOC` or `INT-SOCG`.
