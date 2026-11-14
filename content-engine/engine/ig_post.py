#!/usr/bin/env python3
"""Publish a queued day (Reel + carousel) to Instagram via the official API.

Follows Meta's Content Publishing flow (developers.facebook.com/documentation/
instagram-platform/content-publishing): create container(s) -> poll status_code
until FINISHED -> POST media_publish. Every container is created with
is_ai_generated=true so Instagram applies its "AI info" label (carousels: only
on the parent container, per the docs).

Env:
  IG_USER_ID        Instagram professional account ID
  IG_ACCESS_TOKEN   token with instagram_business_content_publish (IG Login)
                    or instagram_content_publish (FB Login)
  IG_GRAPH_HOST     graph.instagram.com (Instagram Login, default) or graph.facebook.com
  IG_API_VERSION    default v27.0 (version used in Meta's current examples)

Usage:
  python ig_post.py <queue/DATE.json> [--only reel|carousel] [--dry-run]
Stdlib only, so it runs on a bare GitHub Actions runner.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTED = ROOT / "state" / "posted.json"
HOST = os.environ.get("IG_GRAPH_HOST", "graph.instagram.com")
VER = os.environ.get("IG_API_VERSION", "v27.0")


def api(method: str, path: str, **params) -> dict:
    params["access_token"] = os.environ["IG_ACCESS_TOKEN"]
    url = f"https://{HOST}/{VER}/{path}"
    data = None
    if method == "GET":
        url += "?" + urllib.parse.urlencode(params)
    else:
        data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise SystemExit(f"Instagram API error {e.code} on {method} {path}: {body}") from None


def wait_ready(container_id: str, timeout_s: int = 900) -> None:
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        st = api("GET", container_id, fields="status_code,status").get("status_code")
        print(f"  container {container_id}: {st}")
        if st == "FINISHED":
            return
        if st in ("ERROR", "EXPIRED"):
            raise SystemExit(f"container {container_id} failed: {st}")
        time.sleep(15)
    raise SystemExit(f"container {container_id} not ready after {timeout_s}s")


def publish(uid: str, creation_id: str) -> str:
    return api("POST", f"{uid}/media_publish", creation_id=creation_id)["id"]


def post_reel(uid: str, m: dict) -> str:
    c = api("POST", f"{uid}/media", media_type="REELS", video_url=m["reel"]["video_url"],
            caption=m["reel"]["caption"], share_to_feed="true", is_ai_generated="true")["id"]
    wait_ready(c)
    return publish(uid, c)


def post_carousel(uid: str, m: dict) -> str:
    kids = []
    for url in m["carousel"]["image_urls"]:
        kid = api("POST", f"{uid}/media", image_url=url, is_carousel_item="true")["id"]
        wait_ready(kid, 300)
        kids.append(kid)
    c = api("POST", f"{uid}/media", media_type="CAROUSEL", children=",".join(kids),
            caption=m["carousel"]["caption"], is_ai_generated="true")["id"]
    wait_ready(c, 300)
    return publish(uid, c)


def load_posted() -> dict:
    return json.loads(POSTED.read_text()) if POSTED.exists() else {}


def mark(day: str, kind: str, media_id: str) -> None:
    d = load_posted()
    d.setdefault(day, {})[kind] = {"media_id": media_id,
                                   "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    POSTED.write_text(json.dumps(d, indent=2, sort_keys=True))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--only", choices=["reel", "carousel"])
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    m = json.loads(Path(a.manifest).read_text())
    day = m["date"]

    if not m.get("compliance", {}).get("passed"):
        print(f"{day}: compliance not marked passed -- refusing to post"); return 1
    kinds = [a.only] if a.only else ["reel", "carousel"]
    done = load_posted().get(day, {})
    todo = [k for k in kinds if k in m and k not in done]
    if not todo:
        print(f"{day}: nothing to post (already posted: {sorted(done)})"); return 0
    if a.dry_run:
        print(json.dumps({"would_post": todo, "host": HOST, "version": VER}, indent=2)); return 0
    if not (os.environ.get("IG_USER_ID") and os.environ.get("IG_ACCESS_TOKEN")):
        print("IG_USER_ID / IG_ACCESS_TOKEN not set -- skipping (finish setup in README)."); return 0

    uid = os.environ["IG_USER_ID"]
    lim = api("GET", f"{uid}/content_publishing_limit", fields="quota_usage,config")
    print("publishing limit:", json.dumps(lim))
    for k in todo:
        print(f"{day}: posting {k}")
        mid = post_reel(uid, m) if k == "reel" else post_carousel(uid, m)
        mark(day, k, mid)
        print(f"{day}: {k} published as {mid}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
