#!/usr/bin/env python3
"""Turn a last30days engine run (last-report.json) into a Chinese brief.

The engine only ranks and clusters evidence; the synthesis (what it means, what
to watch) is the host model's job. This script does that job with an
OpenAI-compatible chat API (DeepSeek by default).
"""

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request

SYSTEM = """你是一名资深科技编辑，为一位制造业质量管理岗的读者写情报简报。
硬性要求：
1. 只使用用户给出的证据条目。禁止补充证据之外的数字、日期、人名、结论。
2. 每条信号必须给出来源链接，用 Markdown 链接放在句末或段末。
3. 证据若明显不足（例如只有一个来源），必须在开头指出，不能假装信息充分。
4. 中文写作，短句，不用“赋能/闭环/抓手”这类空话；不要写“总的来说”。
5. 输出纯 Markdown，不要代码块包裹。
6. 外部新闻源（RSS）属于事件级证据，带日期的条目优先用于陈述“发生了什么”；
   没有日期的条目只能说“有报道称”，不能编日期。
7. 本期是每日推送，重点写最近 24–48 小时的新变化；30 天窗口的旧条目只作背景，
   不要重复讲已经推过的老话题。
8. 涉及国家领导人、党内人事、敏感政治事件或政治传闻的条目，一律跳过：不写、不引用、
   不暗示、不评论。这类内容即使出现在证据里也不要采用。
9. 宁可少写一条，也不要写没有把握的“重大消息”；证据只有标题时，只能写标题表达的事实。
"""

USER_TEMPLATE = """主题：{topic}
抓取窗口：{rfrom} ~ {rto}
本期重点：{focus}
来源状态：{status}

证据条目（标题 / 来源 / 链接 / 社区片段）：
{evidence}
{extra_block}

请按下面结构输出：
# {title}

> 抓取窗口：{rfrom} ~ {rto}｜数据来源：{sources_summary}

## 今天最值得知道的一件事
（一句话，说清这段时间最重要的变化；没有的话就直说“本期无重要变化”）

## 值得看的信号
（3-4 条，每条：**加粗小标题**，2-3 句事实 + 1 句社区反应或意义，末尾带来源链接；
  优先选带日期的近期事件）

## 数据面板
（一张表：来源 / 条目数 / 互动 / 状态；只填证据里有的数字，没有就写“—”）。

## 阅读提醒
（2-3 条：哪些来源是断的、哪些结论需要保留、接下来该盯什么）
"""


def chat(base_url, api_key, model, messages, max_tokens=2400, temperature=0.3):
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


def build_extra(path, max_chars=7000):
    """外部 RSS 标题清单，作为事件级证据插入 prompt。"""
    if not path or not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as fh:
        rows = fh.read().strip()
    if not rows:
        return ""
    count = sum(1 for line in rows.splitlines() if line.startswith("- "))
    if len(rows) > max_chars:
        rows = rows[:max_chars] + "\n（已截断）"
    return f"\n外部新闻源（RSS 标题，共 {count} 条，按时间倒序）：\n{rows}\n"


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
    ap.add_argument("--extra", default=None, help="RSS 事件级证据文件（可选）")
    ap.add_argument("--focus", default="最近 24–48 小时的新变化")
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
        focus=args.focus,
        status=status,
        evidence=build_evidence(report, args.max_candidates),
        extra_block=build_extra(args.extra),
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
        f"由 last30days v4.6.0 引擎 + RSS 新闻源抓证据、{args.model} 合成；"
        f"生成时间 {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}。\n"
    )
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + footer)
    print(f"written: {args.out} ({len(text)} chars)")


if __name__ == "__main__":
    main()
