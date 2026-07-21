# FF-Fortune d=1: decisive numerical dataset (2026-07-21)

Definitions: N(p) = #{d in F_p : x^p + x^2 + d irreducible over F_p} (quadratic normal form, one per b!=0 affine orbit). N3_a(p) = #{(e,d) in F_p^2 : x^p + a x^3 + e x + d irreducible}, for a = 1 and a = r = smallest quadratic nonresidue mod p (the two affine classes of a != 0, since scaling moves a by squares: a -> a*lambda^2). Computed with python-flint 0.9.0 (nmod_poly), prefilter = QR test on 1-4d (linear factors) + exact small-degree Frobenius-iterate gcd tests, survivors fully factored.

## Headline results

1. **N(p) = 0 HAPPENS, AND OFTEN: 61 of the 238 odd primes p <= 1500 (25.6%)** have NO irreducible x^p + x^2 + d. The quadratic family alone can NEVER prove FF-Fortune d=1; the cubic family is essential. First failures: p = 31, 41, 59, 71, 97. Full list below.
2. **The cubic family never fails on the tested range**: for every prime 5 <= p <= 293, both classes are separately nonzero: min N3_1 = 4 (p=5), min N3_r = 6 (p=5), min total = 10 (p=5). For p >= 7 the total is >= 16 and grows like ~2p (consistent with density-1/p heuristic over 2p^2 normal forms). No prime <= 300 has quadratic AND cubic both empty; in fact no prime <= 300 has cubic empty at all.
3. **Orbit formula verified**: #irred_2 = p(p-1)N(p) + (p-1) holds exactly for p = 3,5,7,11,13 by exhaustive count over all p^3 triples (b,c,d), and the b=0 contribution is exactly the p-1 Artin-Schreier polynomials.

## N(p) = 0 primes (61 of 238)

    31, 41, 59, 71, 97, 113, 131, 151, 157, 163, 197, 229, 239, 257, 271, 277, 283, 307, 379, 397, 401, 419, 439, 449, 457, 461, 499, 523, 547, 557, 593, 653, 673, 743, 769, 773, 809, 821, 829, 853, 881, 883, 907, 953, 971, 1009, 1021, 1051, 1061, 1069, 1091, 1097, 1151, 1231, 1237, 1303, 1367, 1423, 1439, 1453, 1481

## Distribution of N(p) vs Poisson

| N | observed | Poisson(lambda=1.181) expected |
|---|---|---|
| 0 | 61 | 73.1 |
| 1 | 105 | 86.3 |
| 2 | 46 | 50.9 |
| 3 | 20 | 20.0 |
| >=4 | 6 | 7.6 |

mean = 1.181, variance = 0.980, var/mean = 0.830 (underdispersed). Chi-square vs Poisson(mean) = 6.89 on 3 dof (p ~ 0.09): weakly non-Poisson — a deficit of zeros and excess of ones relative to Poisson, i.e. the Kloosterman-type sum S(p) avoids the N=0 region slightly more than a random-phase model predicts, but the effect is only ~1.7 sigma in aggregate. The mean 1.18 > 1 is itself notable.

## Correlations (indicator N(p) >= 2, rate by class)

| condition | classes (count, hits, rate) |
|---|---|
| p mod 4 | 1: (116, 28, 0.241); 3: (122, 44, 0.361) |
| p mod 3 | 1: (115, 35, 0.304); 2: (122, 37, 0.303) |
| p mod 8 | 1: (55, 13, 0.236); 3: (60, 23, 0.383); 5: (61, 15, 0.246); 7: (62, 21, 0.339) |
| p mod 12 | 1: (54, 15, 0.278); 5: (62, 13, 0.210); 7: (61, 20, 0.328); 11: (60, 24, 0.400) |

Largest effects: p mod 4 (rate .241 for p=1 mod 4 vs .361 for p=3 mod 4, chi2=%.1f, ~2 sigma) and p mod 8 / mod 12 refinements of the same (class 1 lowest, class 3 / 11 highest). Legendre symbols of 2,3,5,-1 and cubic-residue conditions on 2,3: no effect beyond ~1 sigma. For N(p)=0 the same mod-4 tilt appears with opposite sign (.285 vs .230). Verdict: suggestive mod-4 asymmetry, not decisive at this sample size.

## N(p) full table (p: N)

    3:1, 5:1, 7:1, 11:1, 13:2, 17:1, 19:2, 23:2, 29:1, 31:0, 37:1, 41:0, 43:3, 47:2, 53:1, 59:0, 61:2, 67:3, 71:0, 73:1, 79:2, 83:2, 89:2, 97:0, 101:1, 103:4, 107:1, 109:1, 113:0, 127:1, 131:0, 137:2, 139:3, 149:1, 151:0, 157:0, 163:0, 167:1, 173:1, 179:3, 181:3, 191:2, 193:4, 197:0, 199:1, 211:2, 223:4, 227:2, 229:0, 233:1, 239:0, 241:1, 251:2, 257:0, 263:1, 269:1, 271:0, 277:0, 281:2, 283:0, 293:1, 307:0, 311:1, 313:1, 317:1, 331:1, 337:1, 347:1, 349:1, 353:1, 359:2, 367:3, 373:1, 379:0, 383:1, 389:3, 397:0, 401:0, 409:2, 419:0, 421:1, 431:1, 433:1, 439:0, 443:2, 449:0, 457:0, 461:0, 463:1, 467:1, 479:3, 487:1, 491:3, 499:0, 503:1, 509:4, 521:2, 523:0, 541:2, 547:0, 557:0, 563:1, 569:1, 571:2, 577:1, 587:1, 593:0, 599:3, 601:1, 607:1, 613:1, 617:2, 619:1, 631:1, 641:1, 643:1, 647:1, 653:0, 659:1, 661:3, 673:0, 677:1, 683:2, 691:1, 701:1, 709:1, 719:2, 727:1, 733:4, 739:1, 743:0, 751:1, 757:3, 761:1, 769:0, 773:0, 787:1, 797:2, 809:0, 811:2, 821:0, 823:1, 827:1, 829:0, 839:1, 853:0, 857:2, 859:3, 863:1, 877:3, 881:0, 883:0, 887:2, 907:0, 911:2, 919:2, 929:1, 937:1, 941:3, 947:1, 953:0, 967:2, 971:0, 977:1, 983:1, 991:1, 997:2, 1009:0, 1013:1, 1019:2, 1021:0, 1031:3, 1033:2, 1039:1, 1049:1, 1051:0, 1061:0, 1063:1, 1069:0, 1087:1, 1091:0, 1093:1, 1097:0, 1103:2, 1109:1, 1117:1, 1123:1, 1129:1, 1151:0, 1153:1, 1163:1, 1171:2, 1181:2, 1187:1, 1193:1, 1201:1, 1213:1, 1217:1, 1223:2, 1229:1, 1231:0, 1237:0, 1249:3, 1259:4, 1277:1, 1279:3, 1283:2, 1289:1, 1291:1, 1297:1, 1301:1, 1303:0, 1307:1, 1319:1, 1321:1, 1327:2, 1361:2, 1367:0, 1373:1, 1381:1, 1399:1, 1409:1, 1423:0, 1427:2, 1429:2, 1433:3, 1439:0, 1447:1, 1451:2, 1453:0, 1459:2, 1471:2, 1481:0, 1483:2, 1487:1, 1489:3, 1493:1, 1499:1

## N3 table (p: N3_1, N3_r, total), 5 <= p <= 293

    5:(4,6,10), 7:(10,8,18), 11:(14,14,28), 13:(10,6,16), 17:(18,14,32), 19:(22,16,38), 23:(12,22,34), 29:(36,28,64), 31:(30,38,68), 37:(36,36,72), 41:(50,34,84), 43:(42,36,78), 47:(38,40,78), 53:(56,38,94), 59:(46,52,98), 61:(42,54,96), 67:(62,80,142), 71:(72,76,148), 73:(74,66,140), 79:(80,64,144), 83:(86,82,168), 89:(64,78,142), 97:(84,82,166), 101:(76,116,192), 103:(88,90,178), 107:(90,104,194), 109:(78,112,190), 113:(90,84,174), 127:(156,116,272), 131:(110,122,232), 137:(150,126,276), 139:(126,132,258), 149:(106,168,274), 151:(118,142,260), 157:(146,150,296), 163:(140,142,282), 167:(104,118,222), 173:(158,130,288), 179:(156,170,326), 181:(184,184,368), 191:(192,176,368), 193:(170,194,364), 197:(176,184,360), 199:(166,180,346), 211:(184,190,374), 223:(164,198,362), 227:(186,206,392), 229:(170,226,396), 233:(208,204,412), 239:(198,212,410), 241:(184,188,372), 251:(224,222,446), 257:(222,224,446), 263:(260,196,456), 269:(220,250,470), 271:(264,262,526), 277:(224,260,484), 281:(228,262,490), 283:(274,242,516), 293:(240,276,516)

## Verification / epistemic status

- [proved, machine-verified] N(31)=N(41)=N(59)=0 re-verified by exhaustive flint factorization of all p polynomials with no prefilter (independent code path).
- [proved, machine-verified] p=1499, d=349 (the unique irreducible) re-verified by an independent Rabin test: 1-4d nonresidue and x^(p^p) = x mod f via the recursion h_{k+1} = -(h_k^2+d) mod f.
- [proved, machine-verified] N3 spot-checks p=7 (10,8) and p=13 (10,6) by exhaustive factorization with no prefilter.
- [proved, machine-verified] orbit formula for p <= 13 (table in JSON).
- [proved] correctness of the prefilter: x^p = -(x^2+d) mod f gives x^(p^k) mod f = k-fold composite of g, exact (degree 2^k < p, no reduction); gcd(f, h_k - x) != 1 iff f has an irreducible factor of degree dividing k; roots in F_p iff 1-4d is a square (incl. 0). Survivors are fully factored by flint, so the final decision never relies on the filter alone being complete — the filter only ever declares REDUCIBLE, and each such declaration exhibits a nontrivial gcd or h_k = x.
- [provable-sketch] cubic normal-form reduction: a != 0 orbits under x -> lambda x + alpha split into two classes a in {1, r} (lambda^(3-p) = lambda^2 on a), b killed by alpha = -b/(3a) for p >= 5. p = 3 excluded (deg 3 = p degeneracy); FF-Fortune at p=3 already holds via N(3)=1.
- [unverified/heuristic] Poisson comparison and the mod-4 effect are descriptive statistics, not theorems.

## Consequence for the target theorem

The quadratic route is dead as a uniform strategy (fails for 25.6% of primes, presumably infinitely often). The cubic ledger is the only viable route, and the data is maximally encouraging: total cubic count ~ 2p with observed minimum 10, never within a factor ~5 of zero for p in [7, 293]. Everything is consistent with #irred_cubic-normal-forms = 2p(1 + O(p^(-1/2))) as the exact-identity + Weil-average analysis predicts.