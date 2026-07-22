import json
d = json.load(open('results_summary.json'))
d['epsilon_minus_families'] = {
  "p5": "nonsplit slice X^5-(eta q)^{-1}X^3+3q^{-1}X+d towers computed j<=7 (nonsplit_towers_p5.json). q=1: E^-_j = (-1)^j E_j EXACTLY (global quadratic twist). q=3: unique rank-7 fit: Kummer flips (+1->-1), B-factor kept (a=2), D-factors {1,-3} -> {-1,-3} (one factor quadratically twisted). q=4: Kummer flips (-1->+1), B kept (a=-2), D {3,-1} -> {3,1}. RULE: nonsplit family = same surviving object with Kummer class and exactly one D-factor sign-flipped.",
  "p7": "towers j<=6 (nonsplit_towers_p7.json): even-j E^- equals untwisted E exactly (forced: quadratic extension splits the twist), odd-j shows partial factor flips; q=1: [-7,-49,77,119,-147,1631] vs [7,-49,-77,119,637,1631]",
  "consequence": "n_+(q) and n_-(q) are the two Frobenius readings of ONE surviving object per q; p n_+/-(q) = p -/+ E_1-type traces"
}
d['p7']['survivor_rank_lower_bounds_unconditional'] = {
  "method": "(|E_j|-1)/7^{j/2} max over j<=7, Weil weight<=1",
  "q1": 7, "q3": 11, "q4": 7, "q5": 14, "q6": 5,
  "note": "p=5 same method gives 2.0/4.0/4.0 vs true ranks 3/7/7"
}
d['j1_positivity_structure'] = "p=7: q=1,6 (irreducible quintic critical fibers) have ZERO irreducible fibers over F_7 (E_1 = +7 = p); q=3,4,5 have 2 each (E_1 = -7). Pointwise Weil at j=1 is vacuous when surviving rank ~ p; positivity of N_a comes from the q-average (CVN.2), i.e. the crown needs the q-line assembly of the surviving curve families, not per-q bounds."
d['q2_boundary_p7'] = "p=7 q=2 slice (2x^7+x^3-3x+d): disc = -3d^2 (unit square), I_j = [2*7^j + 2*Re((i sqrt7)^j)]/7 exactly (verified j<=4): two Tate classes + supersingular elliptic factor"
json.dump(d, open('results_summary.json','w'), indent=1)
print('updated')
