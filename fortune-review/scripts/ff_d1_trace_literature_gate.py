#!/usr/bin/env python3
"""Exact rank/conductor-scale gate for importing short-trace theorems."""
from __future__ import annotations
import argparse,json,math

def prime(n:int)->bool:return n>=5 and all(n%d for d in range(2,int(n**0.5)+1))
def row(p:int)->dict:
    if not prime(p):raise ValueError(p)
    raw_sector=2**(p-2)
    total=((2*p-3)*2**(p-1)+3)//p
    model_collapsed=8*p
    return {
      "p":p,
      "hook_total_h1":total,
      "raw_parity_sector_lower_bound":raw_sector,
      "raw_rank_penalty_log_p":math.log(2*raw_sector,p),
      "model_O_p_rank":model_collapsed,
      "model_rank_penalty_log_p":math.log(2*model_collapsed,p),
    }
def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('primes',nargs='*',type=int,default=[5,7,11,13,17,23,29,43,61,101]);a=ap.parse_args()
    rows=[row(p) for p in a.primes]
    print(json.dumps({
      "status":"EXACT_SCALE_AUDIT",
      "rows":rows,
      "ruling":"The published short-trace bound cannot be applied to the uncollapsed exponential-rank hook object. Even an O(p)-rank collapse leaves a critical rank/conductor penalty and does not by itself win the crown constant.",
      "required_new_input":["post-pushforward O(p) collapse or another effective presentation","explicit conductor and slope audit","absence of trivial and Artin-Schreier factors","additional cancellation or exact Tate subtraction beyond the generic theorem"],
    },indent=2,sort_keys=True))
if __name__=='__main__':main()
