"""Offline tests for baidu2gdrive. No network: Baidu is simulated.

Run:  python -m pytest -q baidu2gdrive/tests
"""
import json
import os
import stat
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
import baidu2gdrive as b2g  # noqa: E402


# --------------------------------------------------------------------------
# Link parsing
# --------------------------------------------------------------------------
@pytest.mark.parametrize("text,code,want", [
    ("https://pan.baidu.com/s/1AbC-dE_f", "x1y2",
     ("https://pan.baidu.com/s/1AbC-dE_f", "AbC-dE_f", "x1y2")),
    ("https://pan.baidu.com/s/1AbCdEf?pwd=ab12", None,
     ("https://pan.baidu.com/s/1AbCdEf", "AbCdEf", "ab12")),
    ("链接: https://pan.baidu.com/s/1AbCdEf 提取码: q9w8 --来自百度网盘超级会员", None,
     ("https://pan.baidu.com/s/1AbCdEf", "AbCdEf", "q9w8")),
    ("https://pan.baidu.com/share/init?surl=AbCdEf", "zzzz",
     ("https://pan.baidu.com/s/1AbCdEf", "AbCdEf", "zzzz")),
    ("https://pan.baidu.com/s/1AbCdEf", None,
     ("https://pan.baidu.com/s/1AbCdEf", "AbCdEf", None)),
])
def test_parse_share(text, code, want):
    assert b2g.parse_share(text, code) == want


@pytest.mark.parametrize("bad", ["https://example.com/s/1abc", "not a link"])
def test_parse_share_rejects(bad):
    with pytest.raises(b2g.B2GError):
        b2g.parse_share(bad)


def test_parse_share_bad_code():
    with pytest.raises(b2g.B2GError):
        b2g.parse_share("https://pan.baidu.com/s/1AbCdEf", "toolong")


def test_creds_from_cookie_string(monkeypatch):
    monkeypatch.setenv("BAIDU_COOKIES", "BAIDUID=1; BDUSS=bd; STOKEN=st; x=y")
    monkeypatch.delenv("BAIDU_BDUSS", raising=False)
    monkeypatch.delenv("BAIDU_STOKEN", raising=False)
    c = b2g.Creds.from_env()
    assert (c.bduss, c.stoken) == ("bd", "st")
    assert c.jar()["BAIDUID"] == "1"


def test_creds_missing(monkeypatch):
    for k in ("BAIDU_COOKIES", "BAIDU_BDUSS", "BAIDU_STOKEN"):
        monkeypatch.delenv(k, raising=False)
    with pytest.raises(b2g.B2GError):
        b2g.Creds.from_env()


def test_is_rclone():
    assert b2g.is_rclone("gdrive:Baidu")
    assert b2g.is_rclone("my drive:")
    assert not b2g.is_rclone("/content/drive/MyDrive/Baidu")
    assert not b2g.is_rclone("relative/path")


# --------------------------------------------------------------------------
# Fake Baidu list API (requests.Session replacement)
# --------------------------------------------------------------------------
class FakeResp:
    def __init__(self, data):
        self._d = data

    def raise_for_status(self):
        pass

    def json(self):
        return self._d


def make_fake_session(pan: Path, page=1000, seen=None):
    class FakeSession:
        def __init__(self):
            self.headers = {}

        def get(self, url, params=None, cookies=None, timeout=None):
            assert url == b2g.LIST_URL
            assert cookies.get("BDUSS") and cookies.get("STOKEN")
            if seen is not None:
                seen.append(params)
            d = pan / params["dir"].lstrip("/")
            if not d.is_dir():
                return FakeResp({"errno": -9})
            kids = sorted(d.iterdir())
            start, lim = params["start"], min(params["limit"], page)
            lst = [{"path": "/" + str(k.relative_to(pan)),
                    "isdir": int(k.is_dir()),
                    "size": 0 if k.is_dir() else k.stat().st_size}
                   for k in kids[start:start + lim]]
            return FakeResp({"errno": 0, "list": lst})
    return FakeSession


def test_list_recursive_paginates(tmp_path, monkeypatch):
    pan = tmp_path / "pan"
    root = pan / "stage"
    (root / "sub" / "deeper").mkdir(parents=True)
    for i in range(2500):  # > 2 pages at limit 1000
        (root / f"f{i:04d}.bin").write_bytes(b"")
    (root / "sub" / "deeper" / "x.mkv").write_bytes(b"12345")
    seen = []
    monkeypatch.setenv("BAIDU_BDUSS", "a")
    monkeypatch.setenv("BAIDU_STOKEN", "b")
    files = b2g.list_recursive(b2g.Creds.from_env(), "/stage",
                               session=make_fake_session(pan, seen=seen)())
    assert len(files) == 2501
    x = [f for f in files if f.rel == "sub/deeper/x.mkv"][0]
    assert x.size == 5 and x.path == "/stage/sub/deeper/x.mkv"
    starts = [p["start"] for p in seen if p["dir"] == "/stage"]
    assert starts == [0, 1000, 2000]


def test_list_errno_raises(tmp_path, monkeypatch):
    monkeypatch.setenv("BAIDU_BDUSS", "a")
    monkeypatch.setenv("BAIDU_STOKEN", "b")
    with pytest.raises(b2g.B2GError, match="errno=-9"):
        b2g.list_recursive(b2g.Creds.from_env(), "/missing",
                           session=make_fake_session(tmp_path)())


# --------------------------------------------------------------------------
# End-to-end with stub BaiduPCS-Go
# --------------------------------------------------------------------------
@pytest.fixture
def world(tmp_path, monkeypatch):
    pan = tmp_path / "pan"; pan.mkdir()
    share = tmp_path / "share"
    (share / "Season 1").mkdir(parents=True)
    files = {"movie.mkv": os.urandom(300_000),
             "Season 1/ep01.mp4": os.urandom(120_000),
             "Season 1/ep02.mp4": os.urandom(150_000),
             "readme.txt": b"hello"}
    for rel, data in files.items():
        (share / rel).write_bytes(data)
    pcs = tmp_path / "BaiduPCS-Go"
    pcs.write_text(f"#!/bin/sh\nexec {sys.executable} {HERE/'fake_pcs.py'} \"$@\"\n")
    pcs.chmod(pcs.stat().st_mode | stat.S_IEXEC)
    rcl = tmp_path / "rclone"
    rcl.write_text(f"#!/bin/sh\nexec {sys.executable} {HERE/'fake_rclone.py'} \"$@\"\n")
    rcl.chmod(rcl.stat().st_mode | stat.S_IEXEC)
    monkeypatch.setenv("FAKE_PAN", str(pan))
    monkeypatch.setenv("FAKE_SHARE", str(share))
    monkeypatch.setenv("FAKE_DRIVE", str(tmp_path / "gdrive"))
    monkeypatch.setenv("BAIDU_COOKIES", "BDUSS=bd; STOKEN=st")
    import requests
    monkeypatch.setattr(requests, "Session", make_fake_session(pan))
    monkeypatch.setattr(b2g.time, "sleep", lambda s: None)
    return dict(tmp=tmp_path, pan=pan, files=files, pcs=str(pcs), rclone=str(rcl))


def run_tool(w, dest, *extra):
    return b2g.main(["https://pan.baidu.com/s/1TestShare?pwd=ab12", dest,
                     "--pcs", w["pcs"], "--rclone", w["rclone"],
                     "--home", str(w["tmp"] / "home"), *extra])


def calls(w):
    return (w["tmp"] / "home" / "pcs-config" / "calls.log").read_text().splitlines()


def test_end_to_end_local_dest(world):
    dest = world["tmp"] / "MyDrive" / "Baidu"
    assert run_tool(world, str(dest)) == 0
    for rel, data in world["files"].items():
        assert (dest / rel).read_bytes() == data, rel
    # transfer landed in the staging dir, with the code
    assert any(c == "transfer https://pan.baidu.com/s/1TestShare ab12" for c in calls(world))
    assert (world["pan"] / "b2g_staging" / "TestShare" / "movie.mkv").exists()
    # secrets never logged
    assert not any("bd" in c.split("=")[-1] and "-cookies" in c for c in calls(world)
                   if "***" not in c)
    # local temp emptied (only empty dirs may remain)
    tmpd = world["tmp"] / "home" / "tmp"
    assert not [p for p in tmpd.rglob("*") if p.is_file()]
    st = json.loads((world["tmp"] / "home" / "state" / "TestShare.json").read_text())
    assert st["transferred"] and len(st["done"]) == 4 and not st["failed"]


def test_resume_skips_done_and_no_retransfer(world):
    dest = world["tmp"] / "out"
    assert run_tool(world, str(dest)) == 0
    n_before = len(calls(world))
    assert run_tool(world, str(dest)) == 0
    new = calls(world)[n_before:]
    assert not any(c.startswith(("transfer", "download")) for c in new), new


def test_retry_on_truncated_download(world, monkeypatch):
    monkeypatch.setenv("FAKE_FAIL_ONCE", "movie.mkv")
    dest = world["tmp"] / "out"
    assert run_tool(world, str(dest)) == 0
    assert (dest / "movie.mkv").read_bytes() == world["files"]["movie.mkv"]
    assert sum(c.startswith("download /b2g_staging/TestShare/movie.mkv")
               for c in calls(world)) == 2


def test_rclone_dest_and_delete_from_baidu(world):
    assert run_tool(world, "gdrive:Baidu/Stuff", "--delete-from-baidu") == 0
    for rel, data in world["files"].items():
        assert (world["tmp"] / "gdrive" / "Baidu" / "Stuff" / rel).read_bytes() == data
    stage = world["pan"] / "b2g_staging" / "TestShare"
    assert not [p for p in stage.rglob("*") if p.is_file()]


def test_dry_run_downloads_nothing(world):
    dest = world["tmp"] / "out"
    assert run_tool(world, str(dest), "--dry-run") == 0
    assert not any(c.startswith("download") for c in calls(world))
    assert not [p for p in dest.rglob("*") if p.is_file()]


def test_existing_at_destination_is_skipped(world):
    dest = world["tmp"] / "out"
    (dest / "Season 1").mkdir(parents=True)
    (dest / "Season 1" / "ep01.mp4").write_bytes(world["files"]["Season 1/ep01.mp4"])
    assert run_tool(world, str(dest)) == 0
    assert not any("ep01" in c for c in calls(world) if c.startswith("download"))


def test_empty_transfer_errors(world, monkeypatch, tmp_path):
    empty = tmp_path / "emptyshare"; empty.mkdir()
    monkeypatch.setenv("FAKE_SHARE", str(empty))
    assert run_tool(world, str(tmp_path / "out")) == 2
    st = json.loads((world["tmp"] / "home" / "state" / "TestShare.json").read_text())
    assert st["transferred"] is False  # so the next run retries the transfer
