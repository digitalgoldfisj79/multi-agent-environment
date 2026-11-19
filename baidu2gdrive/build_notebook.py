#!/usr/bin/env python3
"""Regenerates baidu2gdrive_colab.ipynb with baidu2gdrive.py embedded."""
import json
from pathlib import Path

here = Path(__file__).parent
script = (here / "baidu2gdrive.py").read_text()


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.strip("\n")}


def code(text, title=None):
    meta = {"cellView": "form"} if title else {}
    return {"cell_type": "code", "metadata": meta, "execution_count": None,
            "outputs": [], "source": text.strip("\n")}


cells = [
    md("""
# Baidu Pan → Google Drive

Runs on Google's machines: the file goes Baidu → this Colab VM → your Drive, one
file at a time. Nothing goes through your own computer.

**Before you start:** get your Baidu cookies. Log in at https://pan.baidu.com in
Chrome, open DevTools (F12) → Application → Cookies → `https://pan.baidu.com`,
and copy the values of **BDUSS** and **STOKEN** (not `bdstoken`).

Run the cells top to bottom. If Colab disconnects, run them all again: finished
files are skipped (progress is saved on your Drive).
"""),
    code("""
#@title 1. Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')
""", title=True),
    code("""
#@title 2. What to copy
share_link = ""  #@param {type:"string"}
extraction_code = ""  #@param {type:"string"}
#@markdown Folder inside *My Drive* to put the files in:
drive_folder = "Baidu"  #@param {type:"string"}
#@markdown Keep threads = 1 unless you pay for Baidu SVIP (then 10–20).
threads = 1  #@param {type:"integer"}
delete_from_baidu_after = False  #@param {type:"boolean"}
dry_run_list_only = False  #@param {type:"boolean"}
""", title=True),
    code("""
#@title 3. Baidu login (typed in hidden, never saved in the notebook)
#@markdown Uses Colab Secrets `BAIDU_BDUSS` / `BAIDU_STOKEN` if you set them (key icon on the left), otherwise asks.
import os, getpass
def _secret(name):
    try:
        from google.colab import userdata
        return userdata.get(name)
    except Exception:
        return None
os.environ['BAIDU_BDUSS'] = _secret('BAIDU_BDUSS') or getpass.getpass('BDUSS: ')
os.environ['BAIDU_STOKEN'] = _secret('BAIDU_STOKEN') or getpass.getpass('STOKEN: ')
print('Credentials set for this session.')
""", title=True),
    code("%%writefile /content/baidu2gdrive.py\n" + script),
    code("""
#@title 4. Run
import subprocess, sys
sys.path.insert(0, "/content")
from baidu2gdrive import parse_share
_, share_id, _ = parse_share(share_link, extraction_code.strip() or None)
dest = f"/content/drive/MyDrive/{drive_folder.strip('/')}"
# State file lives on Drive so progress survives Colab resets (one per share).
state = f"/content/drive/MyDrive/.baidu2gdrive_state/{share_id}.json"
cmd = [sys.executable, "/content/baidu2gdrive.py", share_link, dest,
       "--install-pcs", "--home", "/content/b2g",
       "--workdir", "/content/b2g_tmp", "--state", state,
       "--threads", str(threads)]
if extraction_code.strip():
    cmd += ["--code", extraction_code.strip()]
if delete_from_baidu_after:
    cmd += ["--delete-from-baidu"]
if dry_run_list_only:
    cmd += ["--dry-run"]
subprocess.run(["pip", "-q", "install", "requests"])
rc = subprocess.call(cmd)
print("\\nExit code:", rc, "(0 = all done; 1 = some files failed, re-run; 2 = error)")
""", title=True),
]

nb = {"nbformat": 4, "nbformat_minor": 0,
      "metadata": {"colab": {"provenance": []},
                   "kernelspec": {"name": "python3", "display_name": "Python 3"}},
      "cells": cells}
out = here / "baidu2gdrive_colab.ipynb"
out.write_text(json.dumps(nb, indent=1, ensure_ascii=False))
print("wrote", out)
