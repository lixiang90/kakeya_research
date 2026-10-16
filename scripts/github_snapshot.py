"""Credential-free local half of the GitHub connector synchronization flow.

The connected GitHub tools perform network operations. This helper exports only
the staged Git snapshot and can verify/import the exact returned commit object.
No tokens, secrets, forced updates, or shell-built commands are used.
"""
import argparse
import base64
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHUNK = 600_000


def git(*args, data=None):
    return subprocess.check_output(["git", *args], cwd=ROOT, input=data)


def manifest():
    records = git("ls-files", "--stage", "-z").split(b"\0")
    entries = []
    for record in records:
        if not record:
            continue
        header, name = record.split(b"\t", 1)
        mode, sha, stage = header.decode().split()
        if stage != "0":
            raise RuntimeError("Unresolved staged conflict")
        path = name.decode("utf-8")
        if path.startswith((".git/", "tmp/", "sync-private/")) or Path(path).name.startswith(".env"):
            raise RuntimeError(f"Unexpected staged path: {path}")
        content = git("cat-file", "blob", sha)
        entries.append({"path": path, "mode": mode, "type": "blob", "sha": sha,
                        "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest(),
                        "chunks": max(1, (len(content) + CHUNK - 1) // CHUNK)})
    print(json.dumps({"tree": git("write-tree").decode().strip(), "entries": entries}, ensure_ascii=True))


def chunk(sha, index):
    if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
        raise ValueError("Expected a Git blob SHA")
    content = git("cat-file", "blob", sha)
    part = content[index * CHUNK:(index + 1) * CHUNK]
    print(base64.b64encode(part).decode("ascii"))


def import_commit(path):
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    if obj.get("verification", {}).get("signature"):
        payload = obj["verification"].get("payload")
        raise RuntimeError("Signed commit requires exact raw signature reconstruction: " + str(bool(payload)))
    lines = ["tree " + obj["tree"]["sha"]]
    lines += ["parent " + p["sha"] for p in obj.get("parents", [])]
    identities = []
    for role in ("author", "committer"):
        person = obj[role]
        stamp = int(datetime.fromisoformat(person["date"].replace("Z", "+00:00")).timestamp())
        identities.append(f"{role} {person['name']} <{person['email']}> {stamp}")
    # The Git API normalizes dates to UTC and omits the original offsets.
    # Recover only by exact object hash, never by guessing a matching history.
    zones = ["+0000", "-0000"] + [f"{'+' if m >= 0 else '-'}{abs(m)//60:02}{abs(m)%60:02}"
                for m in range(-12*60, 14*60+1, 15) if m]
    for za in zones:
        for zc in zones:
            base = "\n".join(lines + [identities[0]+" "+za, identities[1]+" "+zc]) + "\n\n" + obj["message"]
            for suffix in ("", "\n", "\n\n"):
                raw = (base + suffix).encode("utf-8")
                sha = hashlib.sha1(f"commit {len(raw)}\0".encode() + raw).hexdigest()
                if sha == obj["sha"]:
                    git("hash-object", "-t", "commit", "-w", "--stdin", data=raw)
                    print(json.dumps({"imported_sha": sha, "tree": obj["tree"]["sha"]}))
                    return
    raise RuntimeError("Commit bytes did not match remote SHA; do not update local refs")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("manifest")
    c = sub.add_parser("chunk")
    c.add_argument("sha")
    c.add_argument("index", type=int)
    i = sub.add_parser("import-commit")
    i.add_argument("path")
    args = parser.parse_args()
    if args.command == "manifest":
        manifest()
    elif args.command == "chunk":
        chunk(args.sha, args.index)
    else:
        import_commit(args.path)
