#!/usr/bin/env python3
"""
baidu2gdrive — copy a Baidu Pan (百度网盘) share link into Google Drive,
one file at a time, so you never hold the whole multi-GB share locally.

Pipeline for one share link
---------------------------
  1. login      BaiduPCS-Go logs in with your Baidu cookies (BDUSS + STOKEN).
  2. transfer   The share is saved (转存) into a staging folder in YOUR Baidu Pan:
                /b2g_staging/<share-id>
  3. list       The staging folder is listed recursively (Baidu web API, JSON).
  4. per file   download -> verify size -> move to Google Drive -> record in
                state file -> delete local temp copy (-> optionally delete the
                Baidu staging copy).

Peak local disk use = the size of the largest single file, not the whole share.

Google Drive destination can be either
  * a local path, e.g. the Colab mount  /content/drive/MyDrive/Baidu
  * an rclone remote, e.g.              gdrive:Baidu        (needs `rclone`)

Resumable: progress is written atomically to a JSON state file after every
file. Re-running the same command skips files already done.

Requires: Python 3.8+, `requests`, and the BaiduPCS-Go binary (auto-installed
on Linux x86_64/arm64 with --install-pcs). Secrets are read from environment
variables so they do not end up in shell history:
  BAIDU_COOKIES   full cookie string from pan.baidu.com   (recommended), or
  BAIDU_BDUSS + BAIDU_STOKEN
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.parse
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

# ----------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------
PCS_VERSION = "v4.0.2"  # verified on github.com/qjfoidnh/BaiduPCS-Go releases
PCS_URL = ("https://github.com/qjfoidnh/BaiduPCS-Go/releases/download/"
           "{v}/BaiduPCS-Go-{v}-linux-{arch}.zip")
# sha256 listed on the release page for the linux-amd64 asset.
PCS_SHA256 = {
    "amd64": "b5f51388b510433668ca22fa5a1cb8840fb4d9725c5edc830554645010a62339",
}
STAGING_ROOT = "/b2g_staging"
LIST_URL = "https://pan.baidu.com/api/list"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def log(msg: str) -> None:
    print(time.strftime("[%H:%M:%S] ") + msg, flush=True)


class B2GError(RuntimeError):
    pass


# ----------------------------------------------------------------------------
# Share link parsing
# ----------------------------------------------------------------------------
_SURL_RE = re.compile(r"pan\.baidu\.com/(?:s/1?|share/init\?surl=)([A-Za-z0-9_-]+)")


def parse_share(link: str, code: str | None = None) -> tuple[str, str, str | None]:
    """Return (normalised_link, share_id, extraction_code).

    Accepts:
      https://pan.baidu.com/s/1AbCdEf          (+ separate code)
      https://pan.baidu.com/s/1AbCdEf?pwd=abcd
      https://pan.baidu.com/share/init?surl=AbCdEf
      a pasted blurb like "链接: https://pan.baidu.com/s/1AbC 提取码: abcd"
    """
    text = link.strip()
    m = re.search(r"https?://pan\.baidu\.com/\S+", text)
    if not m:
        raise B2GError(f"No pan.baidu.com link found in: {link!r}")
    url = m.group(0).rstrip("。，,;)")
    sm = _SURL_RE.search(url)
    if not sm:
        raise B2GError(f"Could not find share id in: {url!r}")
    share_id = sm.group(1)

    q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
    found = code or (q.get("pwd") or [None])[0]
    if not found:
        cm = re.search(r"(?:提取码|密码|code|pwd)\s*[:：=]?\s*([A-Za-z0-9]{4})", text)
        if cm:
            found = cm.group(1)
    if found and not re.fullmatch(r"[A-Za-z0-9]{4}", found):
        raise B2GError(f"Extraction code should be 4 letters/digits, got {found!r}")

    base = url.split("?")[0].split("#")[0]
    if "share/init" in base:
        base = f"https://pan.baidu.com/s/1{share_id}"
    return base, share_id, found


# ----------------------------------------------------------------------------
# Credentials
# ----------------------------------------------------------------------------
@dataclass
class Creds:
    cookies: str | None
    bduss: str
    stoken: str

    @classmethod
    def from_env(cls) -> "Creds":
        cookies = os.environ.get("BAIDU_COOKIES", "").strip() or None
        bduss = os.environ.get("BAIDU_BDUSS", "").strip()
        stoken = os.environ.get("BAIDU_STOKEN", "").strip()
        if cookies:
            jar = cookie_dict(cookies)
            bduss = bduss or jar.get("BDUSS", "")
            stoken = stoken or jar.get("STOKEN", "")
        if not bduss or not stoken:
            raise B2GError(
                "Need Baidu credentials. Set BAIDU_COOKIES (full cookie string "
                "from pan.baidu.com, must contain BDUSS and STOKEN) or both "
                "BAIDU_BDUSS and BAIDU_STOKEN. STOKEN must come from the "
                "pan.baidu.com page (it is NOT bdstoken).")
        return cls(cookies, bduss, stoken)

    def jar(self) -> dict[str, str]:
        d = cookie_dict(self.cookies) if self.cookies else {}
        d.setdefault("BDUSS", self.bduss)
        d.setdefault("STOKEN", self.stoken)
        return d


def cookie_dict(s: str) -> dict[str, str]:
    out = {}
    for part in s.split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = v.strip()
    return out


# ----------------------------------------------------------------------------
# BaiduPCS-Go wrapper
# ----------------------------------------------------------------------------
def install_pcs(dest_dir: Path) -> Path:
    """Download + sha256-verify BaiduPCS-Go into dest_dir. Returns binary path."""
    import requests

    machine = platform.machine().lower()
    arch = {"x86_64": "amd64", "amd64": "amd64",
            "aarch64": "arm64", "arm64": "arm64"}.get(machine)
    if platform.system() != "Linux" or not arch:
        raise B2GError("Auto-install supports Linux x86_64/arm64 only; "
                       "install BaiduPCS-Go yourself and pass --pcs PATH.")
    binary = dest_dir / "BaiduPCS-Go"
    if binary.exists():
        return binary
    dest_dir.mkdir(parents=True, exist_ok=True)
    url = PCS_URL.format(v=PCS_VERSION, arch=arch)
    log(f"Downloading BaiduPCS-Go {PCS_VERSION} ({arch}) ...")
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    digest = hashlib.sha256(r.content).hexdigest()
    want = PCS_SHA256.get(arch)
    if want and digest != want:
        raise B2GError(f"BaiduPCS-Go checksum mismatch: got {digest}, want {want}")
    if not want:
        log(f"WARNING: no pinned checksum for {arch}; sha256={digest}")
    zpath = dest_dir / "pcs.zip"
    zpath.write_bytes(r.content)
    with zipfile.ZipFile(zpath) as zf:
        member = next(n for n in zf.namelist()
                      if n.endswith("/BaiduPCS-Go") or n == "BaiduPCS-Go")
        binary.write_bytes(zf.read(member))
    zpath.unlink()
    binary.chmod(0o755)
    return binary


class PCS:
    def __init__(self, binary: str, config_dir: Path, verbose: bool = False):
        self.binary = binary
        self.env = dict(os.environ)
        # BaiduPCS-Go reads its config dir from this env var; keeping it
        # separate means this tool never touches a personal BaiduPCS-Go setup.
        self.env["BAIDUPCS_GO_CONFIG_DIR"] = str(config_dir)
        config_dir.mkdir(parents=True, exist_ok=True)
        self.verbose = verbose

    def run(self, *args: str, check: bool = True, secret: bool = False,
            stream: bool = False) -> str:
        shown = args[0] + " <hidden>" if secret else " ".join(args)
        if self.verbose or stream:
            log(f"$ BaiduPCS-Go {shown}")
        if stream:
            # Let BaiduPCS-Go draw its own progress bar.
            p = subprocess.run([self.binary, *args], env=self.env)
            out = ""
        else:
            p = subprocess.run([self.binary, *args], env=self.env,
                               capture_output=True, text=True)
            out = (p.stdout or "") + (p.stderr or "")
            if self.verbose:
                print(out)
        if check and p.returncode != 0:
            raise B2GError(f"BaiduPCS-Go {shown} failed (exit {p.returncode}):\n{out}")
        return out

    def login(self, c: Creds) -> None:
        if c.cookies:
            out = self.run("login", f"-cookies={c.cookies}", secret=True, check=False)
        else:
            out = self.run("login", f"-bduss={c.bduss}", f"-stoken={c.stoken}",
                           secret=True, check=False)
        if re.search(r"(失败|错误|error|fail)", out, re.I):
            raise B2GError("Baidu login failed:\n" + out)
        log("Logged in to Baidu.")

    def cd(self, path: str) -> None:
        self.run("cd", path)
        # One-shot mode must persist the working dir in config for `transfer`
        # (which always saves to the CWD). Verify rather than assume.
        pwd = self.run("pwd").strip().splitlines()
        if not pwd or pwd[-1].strip().rstrip("/") != path.rstrip("/"):
            raise B2GError(f"`cd {path}` did not stick (pwd says {pwd!r}); "
                           "cannot control where the share is transferred to.")


# ----------------------------------------------------------------------------
# Baidu listing (JSON web API, uses the same cookies)
# ----------------------------------------------------------------------------
@dataclass
class RemoteFile:
    path: str
    size: int
    rel: str  # path relative to the staging folder


def list_recursive(creds: Creds, root: str, session=None) -> list[RemoteFile]:
    import requests

    s = session or requests.Session()
    s.headers.update({"User-Agent": UA, "Referer": "https://pan.baidu.com/disk/home"})
    jar = creds.jar()
    files: list[RemoteFile] = []
    stack = [root]
    while stack:
        d = stack.pop()
        start = 0
        while True:
            r = s.get(LIST_URL, params={"dir": d, "order": "name", "desc": 0,
                                        "start": start, "limit": 1000,
                                        "web": 1, "showempty": 1},
                      cookies=jar, timeout=60)
            r.raise_for_status()
            data = r.json()
            if data.get("errno") != 0:
                raise B2GError(f"Baidu list {d!r} returned errno={data.get('errno')} "
                               "(-6 usually means bad/expired cookies, -9 = not found)")
            items = data.get("list") or []
            for it in items:
                if int(it.get("isdir", 0)):
                    stack.append(it["path"])
                else:
                    p = it["path"]
                    files.append(RemoteFile(p, int(it.get("size", 0)),
                                            p[len(root):].lstrip("/")))
            if len(items) < 1000:
                break
            start += 1000
    files.sort(key=lambda f: f.rel)
    return files


# ----------------------------------------------------------------------------
# Destination (Google Drive)
# ----------------------------------------------------------------------------
def is_rclone(dest: str) -> bool:
    return bool(re.match(r"^[A-Za-z0-9_\- ]+:", dest)) and not os.path.isabs(dest)


class Dest:
    def __init__(self, dest: str, rclone_bin: str = "rclone"):
        self.dest = dest.rstrip("/")
        self.rclone = is_rclone(dest)
        self.rclone_bin = rclone_bin
        if self.rclone and not shutil.which(rclone_bin):
            raise B2GError("Destination looks like an rclone remote but `rclone` "
                           "is not installed (https://rclone.org/install/).")
        if not self.rclone:
            Path(self.dest).mkdir(parents=True, exist_ok=True)

    def target(self, rel: str) -> str:
        return f"{self.dest}/{rel}"

    def existing_size(self, rel: str) -> int | None:
        t = self.target(rel)
        if not self.rclone:
            return os.path.getsize(t) if os.path.isfile(t) else None
        p = subprocess.run([self.rclone_bin, "lsjson", "--files-only", t],
                           capture_output=True, text=True)
        if p.returncode != 0:
            return None
        try:
            items = json.loads(p.stdout or "[]")
        except json.JSONDecodeError:
            return None
        return int(items[0]["Size"]) if items else None

    def put(self, local: Path, rel: str) -> None:
        t = self.target(rel)
        if self.rclone:
            p = subprocess.run([self.rclone_bin, "moveto", str(local), t,
                                "--retries", "5", "--stats-one-line", "-P"])
            if p.returncode != 0:
                raise B2GError(f"rclone moveto failed for {rel}")
        else:
            Path(t).parent.mkdir(parents=True, exist_ok=True)
            part = t + ".b2g-partial"
            shutil.copyfile(local, part)          # copy, then atomic rename
            os.replace(part, t)
            local.unlink()


# ----------------------------------------------------------------------------
# Resumable state
# ----------------------------------------------------------------------------
@dataclass
class State:
    path: Path
    data: dict = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path) -> "State":
        if path.exists():
            return cls(path, json.loads(path.read_text()))
        return cls(path, {"transferred": False, "done": {}, "failed": {}})

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.data, indent=2, ensure_ascii=False))
        os.replace(tmp, self.path)  # atomic


# ----------------------------------------------------------------------------
# Main pipeline
# ----------------------------------------------------------------------------
def human(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def download_one(pcs: PCS, f: RemoteFile, work: Path, threads: int,
                 retries: int) -> tuple[Path, Path]:
    """Returns (downloaded_file, its_temp_root). Caller deletes temp_root."""
    for attempt in range(1, retries + 1):
        tmp = Path(tempfile.mkdtemp(prefix="dl-", dir=work))
        pcs.run("download", f.path, "--saveto", str(tmp), "-p", str(threads),
                "-l", "1", check=False, stream=True)
        # BaiduPCS-Go may nest the file (SaveTo/PreBase/name) and may leave a
        # resume-state sidecar, so match on basename + exact size, anywhere.
        name = f.path.rsplit("/", 1)[-1]
        got = [p for p in tmp.rglob("*") if p.is_file()]
        hits = [p for p in got if p.name == name and p.stat().st_size == f.size]
        if hits:
            return hits[0], tmp
        seen = [(str(p.relative_to(tmp)), p.stat().st_size) for p in got]
        log(f"  attempt {attempt}/{retries}: no complete '{name}' "
            f"({f.size} B) in download dir; found {seen}")
        shutil.rmtree(tmp, ignore_errors=True)
        time.sleep(min(60, 5 * attempt))
    raise B2GError(f"download failed after {retries} attempts: {f.path}")


def run(args: argparse.Namespace) -> int:
    link, share_id, code = parse_share(args.link, args.code)
    log(f"Share {share_id} (code: {'yes' if code else 'none'})")
    creds = Creds.from_env()

    home = Path(args.home).expanduser()
    work = Path(args.workdir).expanduser() if args.workdir else home / "tmp"
    work.mkdir(parents=True, exist_ok=True)
    state = State.load(Path(args.state).expanduser() if args.state
                       else home / "state" / f"{share_id}.json")
    dest = Dest(args.dest, args.rclone)

    binary = args.pcs or shutil.which("BaiduPCS-Go")
    if not binary:
        if not args.install_pcs:
            raise B2GError("BaiduPCS-Go not found: pass --install-pcs or --pcs PATH")
        binary = str(install_pcs(home / "bin"))
    pcs = PCS(binary, home / "pcs-config", verbose=args.verbose)
    pcs.login(creds)

    staging = f"{STAGING_ROOT}/{share_id}"
    if not state.data["transferred"]:
        pcs.run("mkdir", STAGING_ROOT, check=False)
        pcs.run("mkdir", staging, check=False)
        pcs.cd(staging)
        log(f"Transferring share into your Baidu Pan at {staging} ...")
        targs = ["transfer", link] + ([code] if code else [])
        out = pcs.run(*targs, check=False)
        print(out.strip())
        state.data["transferred"] = True
        state.data["staging"] = staging
        state.save()
    else:
        log(f"Share already transferred to {staging} (from state file).")

    files = list_recursive(creds, staging)
    if not files:
        state.data["transferred"] = False
        state.save()
        raise B2GError(f"Nothing found in {staging} after transfer. Check the "
                       "link/code, that your Baidu Pan has free space, and the "
                       "transfer output above.")
    total = sum(f.size for f in files)
    log(f"{len(files)} file(s), {human(total)} total; largest "
        f"{human(max(f.size for f in files))} (= peak local disk needed)")
    if args.dry_run:
        for f in files:
            print(f"  {human(f.size):>10}  {f.rel}")
        return 0

    free = shutil.disk_usage(work).free
    biggest = max(f.size for f in files)
    if biggest > free:
        raise B2GError(f"Largest file {human(biggest)} > free space {human(free)} in {work}")

    failed = 0
    for i, f in enumerate(files, 1):
        tag = f"[{i}/{len(files)}] {f.rel} ({human(f.size)})"
        if state.data["done"].get(f.rel) == f.size:
            log(f"{tag} already done, skipping")
            continue
        if dest.existing_size(f.rel) == f.size:
            log(f"{tag} already at destination, marking done")
            state.data["done"][f.rel] = f.size
            state.save()
            continue
        log(f"{tag} downloading ...")
        t0 = time.time()
        try:
            local, tmproot = download_one(pcs, f, work, args.threads, args.retries)
            dt = max(time.time() - t0, 1e-6)
            log(f"{tag} downloaded at {human(f.size / dt)}/s; moving to Drive ...")
            try:
                dest.put(local, f.rel)
            finally:
                shutil.rmtree(tmproot, ignore_errors=True)  # incl. sidecars
            state.data["done"][f.rel] = f.size
            state.data["failed"].pop(f.rel, None)
            state.save()
            if args.delete_from_baidu:
                pcs.run("rm", f.path, check=False)
            log(f"{tag} done -> {dest.target(f.rel)}")
        except B2GError as e:
            failed += 1
            state.data["failed"][f.rel] = str(e)[:500]
            state.save()
            log(f"{tag} FAILED: {e}")

    done = len(state.data["done"])
    log(f"Finished: {done}/{len(files)} done, {failed} failed this run. "
        f"State: {state.path}")
    if failed:
        log("Re-run the same command to retry failed files.")
    return 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Copy a Baidu Pan share link into Google Drive, file by file.")
    ap.add_argument("link", help="Baidu share link (may include ?pwd=xxxx)")
    ap.add_argument("dest", help="Drive folder: local path (Colab mount) or "
                                 "rclone remote like gdrive:Baidu")
    ap.add_argument("--code", help="4-char extraction code (提取码)")
    ap.add_argument("--home", default="~/.baidu2gdrive",
                    help="where the tool keeps its binary/config/state")
    ap.add_argument("--workdir", help="local temp dir for one file at a time")
    ap.add_argument("--state", help="state file path (put it on Drive in Colab)")
    ap.add_argument("--pcs", help="path to BaiduPCS-Go binary")
    ap.add_argument("--install-pcs", action="store_true",
                    help=f"download BaiduPCS-Go {PCS_VERSION} if not found")
    ap.add_argument("--rclone", default="rclone", help="rclone binary")
    ap.add_argument("--threads", type=int, default=1,
                    help="download threads per file. Keep 1 unless you have "
                         "SVIP: BaiduPCS-Go docs warn >1 gets non-SVIP "
                         "accounts throttled. SVIP: 10-20.")
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--delete-from-baidu", action="store_true",
                    help="delete each file from the Baidu staging folder after "
                         "it reaches Drive (goes to Baidu recycle bin)")
    ap.add_argument("--dry-run", action="store_true",
                    help="transfer + list files, but do not download")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)
    try:
        return run(args)
    except B2GError as e:
        log(f"ERROR: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
