"""Mock-API test of ig_insights.collect/report and ig_post.verify. Usage: python test_insights.py <copy_of_content-engine>"""
import sys, json, datetime as dt, pathlib
root = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(root / "engine"))
import ig_post, ig_insights
calls = []
def fake_api(method, path, **p):
    calls.append((method, path, p))
    if path.endswith("/insights"):
        m = p["metric"]
        if m == "reels_skip_rate": raise SystemExit("Instagram API error 400: metric in development")
        if m == "shares": return {"data": []}                       # unavailable -> must be None, not 0
        if m == "views": return {"data": [{"name": "views", "values": [{"value": 1234}]}]}
        return {"data": [{"name": m, "total_value": {"value": 7}}]}
    if path in ("M_REEL", "M_CAR"):
        return {"is_ai_generated": path == "M_REEL", "media_product_type": "REELS", "permalink": "https://x/p/1"}
    raise AssertionError(path)
ig_post.api = fake_api
(root / "state/posted.json").write_text(json.dumps({"2026-11-14": {
  "reel": {"media_id": "M_REEL", "at": "2026-11-14T12:00:00Z"},
  "carousel": {"media_id": "M_CAR", "at": "2026-11-14T15:00:00Z"}}}))
# t+50h: reel gets d2, carousel (47h old) gets nothing
s = ig_insights.collect(dt.datetime(2026, 11, 16, 14, 0, tzinfo=dt.timezone.utc))
r = s["2026-11-14"]["reel"]
assert "d2" in r and "d7" not in r, r
assert r["d2"]["metrics"]["views"] == 1234 and r["d2"]["metrics"]["likes"] == 7
assert r["d2"]["metrics"]["shares"] is None, "empty data must be None"
assert "error" in r["d2"]["metrics"]["reels_skip_rate"], "per-metric failure isolated"
assert "d2" not in s["2026-11-14"]["carousel"], "carousel <48h must be skipped"
n = len(calls)
# rerun same time: idempotent, no new calls
ig_insights.collect(dt.datetime(2026, 11, 16, 14, 0, tzinfo=dt.timezone.utc)); assert len(calls) == n
# t+8d: reel d7 + carousel d2 + d7
s = ig_insights.collect(dt.datetime(2026, 11, 22, 16, 0, tzinfo=dt.timezone.utc))
assert {"d2", "d7"} <= set(s["2026-11-14"]["carousel"]) and "d7" in s["2026-11-14"]["reel"]
ig_insights.report(s)
# verify(): warning when label missing
print(ig_post.verify("M_CAR")); print(ig_post.verify("M_REEL"))
print("ALL TESTS PASSED")
