#!/usr/bin/env python3
"""Build the interpretation companion for the daily brief.

The raw brief answers "what happened"; this second piece answers "how should I
read it" without adding new facts. It reads the six topic markdown files and
asks the same OpenAI-compatible chat API to connect them, mark uncertainty, and
list observable next steps.
"""

import argparse
import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request

SYSTEM = """你是一名资深科技编辑，为一位关心时代前沿的读者写“第二份解读”，不是复述简报。
硬性要求：
1. 只依据用户给出的六份原始简报，禁止新增事实、数字、日期、人名、机构动作或结论。
2. 推断必须写明“可能是 / 意味着 / 一种解释是”，不能把推断写成已确认事实。
3. 不写岗位影响、职业建议、投资建议；不评论敏感政治人物、党内人事或政治传闻。
4. 不要复述每条新闻。选 3 条最值得解释的信号，讲清它们之间的关系、变化和二阶影响。
5. 如果各板块之间没有真实连接，直接说“今天各板块之间没有强连接”，不要硬连。
6. 明确区分“已确认的事实”“只有标题级证据”“推断”。
7. 中文，短句，不用“赋能/闭环/抓手”这类空话；纯 Markdown，不要代码块。
8. 输出控制在 1200–1800 字，严格按用户给出的结构。
"""

USER_TEMPLATE = """日期：{date}

下面是今天的六份原始简报。请写一份“解读版”，帮助读者理解这些信号为什么重要、彼此怎么连接、接下来该看什么。

<raw_briefs>
{reports}
</raw_briefs>

请严格按下面结构输出：

# 每日情报 · 解读 {date}

> 基于今日六份原始简报，只做解释与连接，不新增事实。

## 一句话主线
（一句话，讲今天最值得记住的变化；没有就直说“今天没有单一主线”）

## 今天真正变了什么
（3 条，每条：**小标题** + 2–3 句解释；不要复述新闻标题，要讲变化的方向）

## 三条线怎么连起来
（2–3 段，跨板块；如果无真实连接，直说“没有强连接”，不要硬凑）

## 接下来 24–72 小时看什么
（3 条可验证的观察点，例如某个发布会、文件、数据、后续报道；不要预言结果）

## 证据强度与不确定性
（2–3 条：哪些是标题级证据、哪些来源缺失、哪些结论不能下）
"""


def chat(base_url, api_key, model, messages, max_tokens=2600, temperature=0.35):
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "ignore")[:500]
        raise RuntimeError(f"chat API HTTP {exc.code}: {detail}") from exc
    return body["choices"][0]["message"]["content"]


def read_reports(directory, max_chars=40000):
    paths = sorted(glob.glob(os.path.join(directory, "*.md")))
    chunks = []
    total = 0
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            text = fh.read().strip()
        if not text:
            continue
        # Keep one level of hierarchy; the notification layer will demote H1.
        text = re.sub(r"(?m)^# ", "## ", text)
        chunk = f"### 文件：{os.path.basename(path)}\n\n{text}"
        if total + len(chunk) > max_chars:
            print(f"[insight] prompt budget reached at {path}", file=sys.stderr)
            break
        chunks.append(chunk)
        total += len(chunk)
    return "\n\n---\n\n".join(chunks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="当日六份简报所在目录")
    ap.add_argument("--out", required=True, help="解读版 md 输出路径")
    ap.add_argument("--date", default=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"))
    ap.add_argument("--base-url", default=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    ap.add_argument("--model", default=os.environ.get("DEEPSEEK_MODEL", "deepseek-chat"))
    ap.add_argument("--max-chars", type=int, default=40000)
    args = ap.parse_args()

    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        sys.exit("缺少环境变量 DEEPSEEK_API_KEY")

    reports = read_reports(args.dir, args.max_chars)
    if not reports:
        sys.exit(f"[insight] {args.dir} 下没有可用的 md 简报")

    user = USER_TEMPLATE.format(date=args.date, reports=reports)
    try:
        text = chat(args.base_url, api_key, args.model, [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ])
    except Exception as exc:
        sys.exit(f"[insight] 生成失败: {exc}")

    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        text = text.split("\n", 1)[1] if "\n" in text else text
    text = text.strip()

    footer = (
        "\n\n---\n\n"
        f"> 解读版由 {args.model} 基于当日六份简报生成；推断已标注，不构成投资建议。"
        f"生成时间 {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}。\n"
    )
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(text.rstrip() + footer)
    print(f"[insight] written: {args.out} ({len(text)} chars)")


if __name__ == "__main__":
    main()
