# Dyadic-block calibration of the corrected prime-pair main term

Date: 27 July 2026  
Status: exact finite computation; no asymptotic inference.

For each block `[X,2X)`, set `H=floor(0.8 X^2)`. For every prime endpoint `ell_j` in the block, the computation formed the exact primorial `P_j`, enumerated prime offsets `m` with `ell_j<m<=H`, tested `P_j+m` for primality, and compared the resulting count and weighted detector with

\[
\lambda_j(H)=\mathfrak S(P_j)
\int_{\ell_j}^{H}\frac{dt}{\log t\log(P_j+t)}
\]

and

\[
\mu_j(H)=\mathfrak S(P_j)
\int_{\ell_j}^{H}\frac{dt}{\log t}.
\]

| X | centres N | sum Z | sum lambda | sum Z / sum lambda | weighted / sum mu |
|---:|---:|---:|---:|---:|---:|
| 20 | 4 | 60 | 62.7586 | 0.9560 | 0.9700 |
| 30 | 7 | 156 | 162.3040 | 0.9612 | 0.9660 |
| 50 | 10 | 352 | 367.9310 | 0.9567 | 0.9460 |
| 80 | 15 | 799 | 829.6160 | 0.9631 | 0.9568 |
| 120 | 22 | 1715 | 1758.8410 | 0.9751 | 0.9791 |

The aggregate ratios are stable near one and substantially closer to the corrected singular-series model than to treating the offsets as an unrestricted population. The finite panel validates the scale and normalisation but does not establish the Hardy--Littlewood asymptotic or any variance estimate.

The principal empirical conclusion is limited but useful: there is no finite-data indication that the main-term correction is an artefact of pointwise examples. It persists under complete dyadic-block aggregation across the tested range.
