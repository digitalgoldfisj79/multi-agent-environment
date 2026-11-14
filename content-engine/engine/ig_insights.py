#!/usr/bin/env python3
"""Pull per-post Instagram insights for everything in state/posted.json.

Source: Instagram Media Insights reference (GET /<IG_MEDIA_ID>/insights,
host graph.instagram.com for Instagram Login, latest version v27.0).
Doc constraints this script respects:
  * data can lag up to 48 h -> snapshots taken at >=48 h ("d2") and >=7 d ("d7")
  * empty data set (not 0) when unavailable -> stored as null, never as 0
  * carousel CHILDREN have no insights -> only the parent media is queried
  * requesting an unsupported metric fails the whole call -> metrics are
    requested one by one so a single bad metric can't hide the others
Requires permission instagram_business_manage_insights.

Usage: python ig_insights.py [--now ISO8601]     (writes state/insights.json)
       python ig_insights.py --report            (prints the table, no API calls)
"""
import argparse
import datetime as dt
import json
import os
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ig_post  # reuse api(); same host/version/env vars

ROOT = Path(__file__).resolve().parent.parent
POSTED = ROOT / "state" / "posted.json"
INSIGHTS = ROOT / "state" / "insights.json"
QUEUE = ROOT / "queue"

METRICS = {
    "reel": ["views", "reach", "likes", "comments", "saved", "shares",
             "total_interactions", "ig_reels_avg_watch_time", "reels_skip_rate"],
    "carousel": ["views", "reach", "likes", "comments", "saved", "shares",
                 "total_interactions"],
}
SNAPSHOTS = {"d2": dt.timedelta(hours=48), "d7": dt.timedelta(days=7)}


def fetch_metric(media_id: str, metric: str):
    try:
        r = ig_post.api("GET", f"{media_id}/insights", metric=metric)
    except SystemExit as e:  # api() raises SystemExit on HTTP errors
        return {"error": str(e)[:300]}
    data = r.get("data") or []
    if not data:
        return None  # doc: empty set means unavailable, NOT zero
    d = data[0]
    if "total_value" in d:
        return d["total_value"].get("value")
    vals = d.get("values") or []
    return vals[0].get("value") if vals else None


def collect(now: dt.datetime) -> dict:
    posted = json.loads(POSTED.read_text()) if POSTED.exists() else {}
    store = json.loads(INSIGHTS.read_text()) if INSIGHTS.exists() else {}
    for day, kinds in sorted(posted.items()):
        for kind, rec in kinds.items():
            at = dt.datetime.fromisoformat(rec["at"].replace("Z", "+00:00"))
            slot = store.setdefault(day, {}).setdefault(kind, {"media_id": rec["media_id"]})
            for snap, age in SNAPSHOTS.items():
                if snap in slot or now - at < age:
                    continue
                vals = {m: fetch_metric(rec["media_id"], m) for m in METRICS[kind]}
                slot[snap] = {"taken": now.isoformat(timespec="seconds"), "metrics": vals}
                print(f"{day} {kind} {snap}: {json.dumps(vals)}")
    INSIGHTS.write_text(json.dumps(store, indent=2, sort_keys=True))
    return store


def report(store: dict) -> None:
    """Descriptive table only. No ranking claims until n is large enough (see RUNBOOK)."""
    cats = {}
    for f in QUEUE.glob("*.json"):
        m = json.loads(f.read_text())
        cats[m["date"]] = m.get("trend", {}).get("category", "uncategorised")
    rows = []
    for day, kinds in sorted(store.items()):
        for kind, slot in kinds.items():
            snap = slot.get("d7") or slot.get("d2")
            if not snap:
                continue
            mm = snap["metrics"]
            rows.append((day, kind, cats.get(day, "?"), "d7" if "d7" in slot else "d2",
                         mm.get("views"), mm.get("reach"), mm.get("saved"), mm.get("shares"),
                         mm.get("reels_skip_rate")))
    print(f"{'day':<11}{'kind':<9}{'category':<16}{'snap':<5}{'views':>8}{'reach':>8}"
          f"{'saved':>7}{'shares':>7}{'skip%':>7}")
    for r in rows:
        print(f"{r[0]:<11}{r[1]:<9}{r[2]:<16}{r[3]:<5}" +
              "".join(f"{('-' if v is None or isinstance(v, dict) else v)!s:>{w}}"
                      for v, w in zip(r[4:], (8, 8, 7, 7, 7))))
    for kind in ("reel", "carousel"):
        views = [r[4] for r in rows if r[1] == kind and isinstance(r[4], (int, float))]
        if len(views) >= 2:
            q = statistics.quantiles(views, n=4)
            print(f"{kind}: n={len(views)} median views={statistics.median(views):.0f} "
                  f"IQR={q[2] - q[0]:.0f}")
        else:
            print(f"{kind}: n={len(views)} (too few for any summary)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--now")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    if a.report:
        report(json.loads(INSIGHTS.read_text()) if INSIGHTS.exists() else {})
        return 0
    if not (os.environ.get("IG_USER_ID") and os.environ.get("IG_ACCESS_TOKEN")):
        print("IG secrets not set -- skipping insights."); return 0
    now = (dt.datetime.fromisoformat(a.now) if a.now
           else dt.datetime.now(dt.timezone.utc))
    report(collect(now))
    return 0


if __name__ == "__main__":
    sys.exit(main())
