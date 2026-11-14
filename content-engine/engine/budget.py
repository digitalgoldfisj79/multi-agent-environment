#!/usr/bin/env python3
"""Daily Higgsfield spend guard.

Hard cap: $2.25/day = 45 credits (raised from $2 by the owner on 2026-11-14
to pay for Kling 4.0). Credits are converted at USD_PER_CREDIT (default 0.05,
i.e. the ~$5 per 100 credits top-up price reported by third-party pricing
pages -- UNVERIFIED against higgsfield.ai; it is the more expensive of the
reported rates, so the cap errs on the safe side).

Usage:
  python budget.py check <credits>        # exit 0 if affordable today, 1 if not
  python budget.py record <item> <credits>
  python budget.py summary [days]

The ledger is a convenience; the Higgsfield `transactions` tool is the
authoritative record and the daily runbook cross-checks against it.
"""
import datetime as dt
import json
import os
import sys
import tempfile
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "state" / "ledger.json"
USD_CAP = float(os.environ.get("DAILY_USD_CAP", "2.25"))
USD_PER_CREDIT = float(os.environ.get("USD_PER_CREDIT", "0.05"))
CREDIT_CAP = USD_CAP / USD_PER_CREDIT  # 45 credits at defaults


def today() -> str:
    return dt.datetime.now(dt.timezone.utc).date().isoformat()


def load() -> dict:
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return {}


def save(data: dict) -> None:
    # atomic write so a crash never leaves a half-written ledger
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=LEDGER.parent, suffix=".tmp")
    with os.fdopen(fd, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
    os.replace(tmp, LEDGER)


def spent(day: str, data: dict | None = None) -> float:
    data = load() if data is None else data
    return round(sum(e["credits"] for e in data.get(day, [])), 4)


def check(credits: float, day: str | None = None) -> bool:
    day = day or today()
    s = spent(day)
    ok = s + credits <= CREDIT_CAP + 1e-9
    print(json.dumps({
        "day": day, "spent_credits": s, "requested": credits,
        "cap_credits": CREDIT_CAP, "remaining_after": round(CREDIT_CAP - s - credits, 4),
        "spent_usd_est": round(s * USD_PER_CREDIT, 2), "affordable": ok}))
    return ok


def record(item: str, credits: float, day: str | None = None) -> None:
    day = day or today()
    data = load()
    data.setdefault(day, []).append({
        "item": item, "credits": credits,
        "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")})
    save(data)
    print(json.dumps({"day": day, "spent_credits": spent(day, data), "cap_credits": CREDIT_CAP}))


def summary(days: int = 14) -> None:
    data = load()
    rows = sorted(data.items())[-days:]
    print(f"{'day':<12}{'credits':>9}{'usd_est':>9}")
    for day, entries in rows:
        c = sum(e["credits"] for e in entries)
        print(f"{day:<12}{c:>9.2f}{c * USD_PER_CREDIT:>9.2f}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "summary"
    if cmd == "check":
        sys.exit(0 if check(float(sys.argv[2])) else 1)
    elif cmd == "record":
        record(sys.argv[2], float(sys.argv[3]))
    elif cmd == "summary":
        summary(int(sys.argv[2]) if len(sys.argv) > 2 else 14)
    else:
        sys.exit(__doc__)
