#!/usr/bin/env python3
# Analyse the exact finite TFP3 panel without promoting it to a theorem.
from __future__ import annotations
import argparse, json
from pathlib import Path

FROZEN={
5:(0,0),7:(0,0),11:(2,220),13:(0,0),17:(2,544),19:(2,684),23:(0,0),
29:(2,1624),31:(2,1860),37:(4,5328),41:(6,9840),43:(6,10836),
47:(2,4324),53:(6,16536),59:(4,13688),
}
EXTENDED={
61:(6,21960),67:(12,53064),71:(10,49700),73:(8,42048),79:(8,49296),
83:(14,95284),89:(18,140976),97:(16,148992),101:(24,242400),
}

def fit(points: list[tuple[int,int]]) -> dict[str,float]:
    n=len(points); mx=sum(x for x,_ in points)/n; my=sum(y for _,y in points)/n
    sxx=sum((x-mx)**2 for x,_ in points)
    slope=sum((x-mx)*(y-my) for x,y in points)/sxx
    intercept=my-slope*mx
    rss=sum((y-(intercept+slope*x))**2 for x,y in points)
    tss=sum((y-my)**2 for _,y in points)
    return {"slope":slope,"intercept":intercept,"r_squared":1-rss/tss if tss else 1.0}

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("panel",type=Path)
    args=parser.parse_args()
    summaries={}
    text=args.panel.read_text()
    if args.panel.suffix==".json":
        document=json.loads(text)
        for row in document["fields"]:
            summaries[int(row["q"])]=(int(row["true_orbits"]),int(row["incidences"]))
    else:
        for line in text.splitlines():
            if not line.strip(): continue
            row=json.loads(line)
            if row["type"]=="summary":
                summaries[int(row["q"])]=(int(row["true_orbits"]),int(row["incidences"]))
    for q,want in {**FROZEN,**EXTENDED}.items():
        if summaries.get(q)!=want:
            raise AssertionError(f"panel mismatch q={q}: {summaries.get(q)} != {want}")
    fit_points=[(q,summaries[q][0]) for q in sorted(summaries) if q>=29]
    regression=fit(fit_points)
    output={
        "status":"EMPIRICAL_EXACT_FINITE_PANEL",
        "field_range":[min(summaries),max(summaries)],
        "number_of_fields":len(summaries),
        "maximum_true_orbits":{"q":max(summaries,key=lambda q:summaries[q][0]),
                               "count":max(v[0] for v in summaries.values())},
        "linear_fit_q_ge_29":regression,
        "linear_growth_alarm":regression["slope"]>0.1 and regression["r_squared"]>0.6,
        "formal_O1_refutation":False,
        "interpretation":(
            "The exact finite panel strongly disfavours stabilization at the previously observed "
            "ceiling, but no finite panel proves or refutes a uniform O(1) theorem."
        ),
        "next_theorem":(
            "Identify the one-dimensional nondegenerate irreducible component(s), construct the "
            "eight-class Frobenius-sign cover, and prove either positive-density Chebotarev growth "
            "or confinement of the all-positive sign class to a bounded exceptional locus."
        ),
        "counts":{str(q):{"true_orbits":v[0],"incidences":v[1]} for q,v in sorted(summaries.items())},
    }
    print(json.dumps(output,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
