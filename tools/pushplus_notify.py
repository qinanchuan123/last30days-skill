#!/usr/bin/env python3
"""Push generated briefs to WeChat via PushPlus (one message per topic)."""

import argparse
import glob
import json
import os
import sys
import urllib.request

DEFAULT_ENDPOINT = "https://www.pushplus.plus/send"


def send(endpoint, token, title, content):
    payload = {
        "token": token,
        "title": title,
        "content": content,
        "template": "markdown",
        "channel": "wechat",
    }
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", default=os.environ.get("PUSHPLUS_TOKEN"))
    ap.add_argument("--dir", required=True, help="简报所在目录")
    ap.add_argument("--date", default="")
    ap.add_argument("--endpoint", default=os.environ.get("PUSHPLUS_ENDPOINT", DEFAULT_ENDPOINT))
    args = ap.parse_args()

    if not args.token:
        print("PUSHPLUS_TOKEN 未配置，跳过微信推送")
        return 0

    files = sorted(glob.glob(os.path.join(args.dir, "*.md")))
    if not files:
        print("目录里没有 md，跳过推送")
        return 0

    failed = 0
    for path in files:
        name = os.path.splitext(os.path.basename(path))[0]
        title = f"{name} 情报简报 {args.date}".strip()
        content = open(path, encoding="utf-8").read()
        try:
            r = send(args.endpoint, args.token, title, content)
        except Exception as exc:  # network / auth
            print(f"[pushplus] {name} 发送异常: {exc}")
            failed += 1
            continue
        code = r.get("code")
        print(f"[pushplus] {name} code={code} msg={r.get('msg')}")
        if code != 200:
            failed += 1
    print(f"[pushplus] done, failed={failed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
