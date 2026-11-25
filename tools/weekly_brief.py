#!/usr/bin/env python3
"""Turn a last30days engine run (last-report.json) into a Chinese weekly brief.

The engine only ranks and clusters evidence; the synthesis (what it means, what
to watch) is the host model's job. This script does that job with an
OpenAI-compatible chat API (DeepSeek by default).
"""

import argparse
import datetime as dt
import json
import os
import sys
import urllib.request

SYSTEM = """你是一名资深科技编辑，为一位制造业质量管理岗的读者写每周情报简报。
硬性要求：
1. 只使用用户给出的证据条目。禁止补充证据之外的数字、日期、人名、结论。
2. 每条信号必须给出来源链接，用 Markdown 链接放在句末或段末。
3. 证据若明显不足（例如只有一个来源），必须在开头指出，不能假装信息充分。
4. 中文写作，短句，不用“赋能/闭环/抓手”这类空话；不要写“总的来说”。
5. 输出纯 Markdown，不要代码块包裹。
"""

USER_TEMPLATE = """主题：{topic}
抓取窗口：{rfrom} ~ {rto}
来源状态：{status}

证据条目（标题 / 来源 / 链接 / 社区片段）：
{evidence}

请按下面结构输出：
# {title}

> 抓取窗口：{rfrom} ~ {rto}｜数据来源：{sources_summary}

## 一句话结论
（一句话，说清本周最重要的变化）

## 值得看的信号
（3-5 条，每条：**加粗小标题**，2-3 句事实 + 1 句社区反应或意义，末尾带来源链接）

## 数据面板
（一张表：来源 / 条目数 / 互动 / 状态；只填证据里有的数字，没有就写“—”）

## 阅读提醒
（2-3 条：哪些来源是断的、哪些结论需要保留、下期该盯什么）
"""


def chat(base_url, api_key, model, messages, max_tokens=2200, temperature=0.3):
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
    with urllib.request.urlopen(req, timeout=180) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body["choices"][0]["message"]["content"]


def build_evidence(report, limit=12, snippet_chars=260):
    rows = []
    for c in (report.get("ranked_candidates") or [])[:limit]:
        title = (c.get("title") or "").strip()
        url = (c.get("url") or "").strip()
        source = (c.get("source") or "").strip()
        snippet = " ".join((c.get("snippet") or "").split())[:snippet_chars]
        rows.append(f"- [{source}] {title}\n  {url}\n  {snippet}")
    return "\n".join(rows) if rows else "（引擎未返回任何候选条目）"


def summarize_sources(report):
    parts = []
    stats = report.get("items_by_source") or {}
    for src, items in stats.items():
        n = len(items) if isinstance(items, list) else items
        parts.append(f"{src} {n} 条")
    return "、".join(parts) if parts else "未知"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", required=True, help="engine 的 last-report.json 路径")
    ap.add_argument("--out", required=True, help="输出 md 路径")
    ap.add_argument("--title", default=None)
    ap.add_argument("--base-url", default=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    ap.add_argument("--model", default=os.environ.get("DEEPSEEK_MODEL", "deepseek-chat"))
    ap.add_argument("--max-candidates", type=int, default=12)
    args = ap.parse_args()

    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        sys.exit("缺少环境变量 DEEPSEEK_API_KEY")

    with open(args.report, encoding="utf-8") as f:
        payload = json.load(f)
    report = payload["reports"][0]["report"]

    topic = report.get("topic") or args.title or "未命名主题"
    rfrom = report.get("range_from", "—")
    rto = report.get("range_to", "—")
    status = json.dumps(report.get("source_status") or {}, ensure_ascii=False)

    user = USER_TEMPLATE.format(
        topic=topic,
        title=args.title or topic,
        rfrom=rfrom,
        rto=rto,
        status=status,
        evidence=build_evidence(report, args.max_candidates),
        sources_summary=summarize_sources(report),
    )

    text = chat(args.base_url, api_key, args.model, [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user},
    ])

    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        text = text.split("\n", 1)[1] if "\n" in text else text

    footer = (
        "\n\n---\n\n"
        f"由 last30days v4.6.0 引擎抓取证据、{args.model} 合成；"
        f"生成时间 {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}。\n"
    )
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + footer)
    print(f"written: {args.out} ({len(text)} chars)")


if __name__ == "__main__":
    main()
