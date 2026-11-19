#!/usr/bin/env python3
"""Stub BaiduPCS-Go for tests. Simulates the commands baidu2gdrive uses.

Fake Baidu Pan = directory $FAKE_PAN. Fake share = directory $FAKE_SHARE.
Workdir persisted in $BAIDUPCS_GO_CONFIG_DIR/pcs_config.json (like the real one).
$FAKE_FAIL_ONCE=<basename>: first download of that file is truncated.
Download output is nested as SaveTo/<parent>/<name> plus a sidecar file, to
mimic the unverified real layout.
"""
import json
import os
import shutil
import sys
from pathlib import Path

pan = Path(os.environ["FAKE_PAN"])
cfg_dir = Path(os.environ["BAIDUPCS_GO_CONFIG_DIR"])
cfg = cfg_dir / "pcs_config.json"
state = json.loads(cfg.read_text()) if cfg.exists() else {"workdir": "/"}
log = cfg_dir / "calls.log"


def save():
    cfg.write_text(json.dumps(state))


def local(p):
    return pan / p.lstrip("/")


args = sys.argv[1:]
with log.open("a") as fh:
    fh.write(" ".join(a if not a.startswith(("-cookies", "-bduss", "-stoken"))
                      else a.split("=")[0] + "=***" for a in args) + "\n")
cmd = args[0]
if cmd == "login":
    print("百度帐号登录成功: tester")
elif cmd == "mkdir":
    local(args[1]).mkdir(parents=True, exist_ok=True)
elif cmd == "cd":
    if not local(args[1]).is_dir():
        print("目录不存在"); sys.exit(1)
    state["workdir"] = args[1]; save()
elif cmd == "pwd":
    print(state["workdir"])
elif cmd == "transfer":
    src = Path(os.environ["FAKE_SHARE"])
    for item in src.iterdir():
        dst = local(state["workdir"]) / item.name
        (shutil.copytree if item.is_dir() else shutil.copyfile)(item, dst)
    print("转存成功, 保存了 share 到当前目录")
elif cmd == "download":
    remote = args[1]
    saveto = Path(args[args.index("--saveto") + 1])
    srcf = local(remote)
    out = saveto / srcf.parent.name / srcf.name
    out.parent.mkdir(parents=True, exist_ok=True)
    data = srcf.read_bytes()
    flag = cfg_dir / ("failed_" + srcf.name)
    if os.environ.get("FAKE_FAIL_ONCE") == srcf.name and not flag.exists():
        flag.touch(); data = data[: len(data) // 2]
    out.write_bytes(data)
    (saveto / "resume.state").write_bytes(b"x" * len(data))  # same size decoy
elif cmd == "rm":
    for a in args[1:]:
        p = local(a)
        shutil.rmtree(p) if p.is_dir() else p.unlink()
else:
    print("unknown command", cmd); sys.exit(1)
