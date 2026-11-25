#!/usr/bin/env python3
"""Push generated briefs to WeChat.

Provider priority:
1. Server酱 Turbo (SERVERCHAN_SENDKEY) — free 5 msg/day, no real-name fee
2. PushPlus      (PUSHPLUS_TOKEN)       — kept as fallback

Default: merge all topic files of the day into ONE message, so a weekly run
costs a single free quota instead of one per topic. Pass --split to send one
message per file.
"""

import argparse
import glob
import json
import os
import re
import sys
import urllib.parse
import urllib.request

SERVERCHAN_ENDPOINT = "https://sctapi.ftqq.com/{key}.send"
PUSHPLUS_ENDPOINT = "https://www.pushplus.plus/send"

MAX_BODY_BYTES = 30000


def post_form(url, fields):
    data = urllib.parse.urlencode(fields).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def post_json(url, payload):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def send_serverchan(key, title, content):
    return post_form(SERVERCHAN_ENDPOINT.format(key=key), {"title": title[:32], "desp": content})


def send_pushplus(token, title, content):
    return post_json(
        PUSHPLUS_ENDPOINT,
        {"token": token, "title": title, "content": content, "template": "markdown", "channel": "wechat"},
    )


def read_brief(path):
    """Read one topic brief and demote its H1s so the merged message keeps one top level."""
    with open(path, encoding="utf-8") as fh:
        body = fh.read().strip()
    return re.sub(r"(?m)^# ", "## ", body)


def build_combined(files, date, label):
    head = f"# {label} {date}".strip()
    bodies = [read_brief(p) for p in files]
    bodies = [b for b in bodies if b]
    if not bodies:
        return ""
    return head + "\n\n---\n\n" + "\n\n---\n\n".join(bodies)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="简报所在目录")
    ap.add_argument("--date", default="")
    ap.add_argument("--label", default="情报简报")
    ap.add_argument("--split", action="store_true", help="每个话题单独发一条（默认合并成一条）")
    args = ap.parse_args()

    sc_key = os.environ.get("SERVERCHAN_SENDKEY")
    pp_token = os.environ.get("PUSHPLUS_TOKEN")
    if not sc_key and not pp_token:
        print("SERVERCHAN_SENDKEY / PUSHPLUS_TOKEN 均未配置，跳过微信推送")
        return 0

    provider = "serverchan" if sc_key else "pushplus"
    print(f"[notify] provider={provider} mode={'split' if args.split else 'combined'}")

    files = sorted(glob.glob(os.path.join(args.dir, "*.md")))
    if not files:
        print("[notify] 目录里没有 md，跳过推送")
        return 0

    failed = 0

    def deliver(title, content, name):
        nonlocal failed
        size = len(content.encode("utf-8"))
        if size > MAX_BODY_BYTES:
            print(f"[notify] {name} 内容 {size} 字节，超过 {MAX_BODY_BYTES}，已截断")
            content = content.encode("utf-8")[:MAX_BODY_BYTES].decode("utf-8", "ignore")
        try:
            if provider == "serverchan":
                r = send_serverchan(sc_key, title, content)
                ok = r.get("code") == 0
            else:
                r = send_pushplus(pp_token, title, content)
                ok = r.get("code") == 200
        except Exception as exc:
            print(f"[notify] {name} 异常: {exc}")
            failed += 1
            return
        print(f"[notify] {name} ok={ok} resp={json.dumps(r, ensure_ascii=False)[:160]}")
        if not ok:
            failed += 1

    if args.split:
        for path in files:
            name = os.path.splitext(os.path.basename(path))[0]
            title = f"{name} {args.label} {args.date}".strip()
            deliver(title, open(path, encoding="utf-8").read(), name)
    else:
        combined = build_combined(files, args.date, args.label)
        title = f"{args.label} {args.date}".strip()
        deliver(title, combined, "combined")

    print(f"[notify] done, failed={failed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
