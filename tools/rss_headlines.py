#!/usr/bin/env python3
"""Collect event-level headlines from public RSS feeds (no API key needed).

The last30days engine gives community signals; RSS gives dated, attributable
events. These lines are fed to the synthesis model as extra evidence.
"""

import argparse
import datetime as dt
import email.utils
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (compatible; last30days-rss/1.0)"

FEEDS = {
    "ai": [
        ("TechCrunch AI", "https://techcrunch.com/category/artificial-intelligence/feed/"),
        ("The Verge AI", "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"),
        ("arXiv cs.AI", "http://export.arxiv.org/rss/cs.AI"),
        ("Hacker News", "https://hnrss.org/frontpage"),
    ],
    "chips": [
        ("IEEE Spectrum", "https://spectrum.ieee.org/feeds/feed.rss"),
        ("SemiEngineering", "https://semiengineering.com/feed/"),
        ("Tom's Hardware", "https://www.tomshardware.com/feeds/all"),
        ("SemiAnalysis", "https://semianalysis.com/feed/"),
    ],
    "science": [
        ("Nature", "https://www.nature.com/nature.rss"),
        ("Science News", "https://www.science.org/rss/news_current.xml"),
        ("Quanta", "https://www.quantamagazine.org/feed/"),
        ("Phys.org", "https://phys.org/rss-feed/"),
    ],
    "space": [
        ("NASA", "https://www.nasa.gov/rss/dyn/breaking_news.rss"),
        ("SpaceNews", "https://spacenews.com/feed/"),
        ("ESA", "https://www.esa.int/rssfeed/ESA"),
        ("Ars Technica", "https://feeds.arstechnica.com/arstechnica/index"),
    ],
    "world": [
        ("BBC World", "https://feeds.bbci.co.uk/news/world/rss.xml"),
        ("Guardian World", "https://www.theguardian.com/world/rss"),
        ("Al Jazeera", "https://www.aljazeera.com/xml/rss/all.xml"),
        ("Rest of World", "https://restofworld.org/feed/"),
        ("CNBC Top", "https://www.cnbc.com/id/100003114/device/rss/rss.html"),
    ],
    "finance": [
        ("CNBC Top", "https://www.cnbc.com/id/100003114/device/rss/rss.html"),
        ("MarketWatch Top", "https://feeds.content.dowjones.io/public/rss/mw_topstories"),
        ("Fed Press", "https://www.federalreserve.gov/feeds/press_all.xml"),
        ("ECB Press", "https://www.ecb.europa.eu/rss/press.html"),
    ],
    "tech": [
        ("TechCrunch", "https://techcrunch.com/feed/"),
        ("The Verge", "https://www.theverge.com/rss/index.xml"),
        ("Ars Technica", "https://feeds.arstechnica.com/arstechnica/index"),
        ("Hacker News", "https://hnrss.org/frontpage"),
    ],
}

NS = {"atom": "http://www.w3.org/2005/Atom", "dc": "http://purl.org/dc/elements/1.1/"}


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def parse_date(raw):
    raw = (raw or "").strip()
    if not raw:
        return None
    try:
        parsed = email.utils.parsedate_to_datetime(raw)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed.astimezone(dt.timezone.utc)
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
        try:
            parsed = dt.datetime.strptime(raw.replace("Z", "+0000"), fmt)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
        except Exception:
            continue
    return None


def text_of(node, *paths):
    for path in paths:
        found = node.find(path, NS)
        if found is not None and (found.text or "").strip():
            return found.text.strip()
    return ""


def link_of(node):
    plain = text_of(node, "link")
    if plain:
        return plain
    for dead in node.findall("atom:link", NS):
        if dead.get("rel", "alternate") == "alternate" and dead.get("href"):
            return dead.get("href")
    return ""


def parse_feed(xml_bytes, feed_name, cutoff, per_feed):
    root = ET.fromstring(xml_bytes)
    items = root.findall(".//item") or root.findall(".//atom:entry", NS)
    rows = []
    for item in items[: per_feed * 3]:
        title = re.sub(r"\s+", " ", text_of(item, "title", "atom:title")).strip()
        link = link_of(item).strip()
        raw_date = text_of(item, "pubDate", "atom:updated", "atom:published", "dc:date")
        published = parse_date(raw_date)
        if published and published < cutoff:
            continue
        if not title:
            continue
        rows.append(
            {
                "feed": feed_name,
                "title": title,
                "url": link,
                "date": published.strftime("%Y-%m-%d") if published else "日期未知",
                "ts": published.timestamp() if published else 0,
            }
        )
        if len(rows) >= per_feed:
            break
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True, help="ai / chips / science / space / world / finance / tech")
    ap.add_argument("--out", required=True, help="输出 md 路径")
    ap.add_argument("--days", type=int, default=30, help="只保留最近 N 天")
    ap.add_argument("--per-feed", type=int, default=8)
    ap.add_argument("--total", type=int, default=48)
    args = ap.parse_args()

    feeds = FEEDS.get(args.topic)
    if not feeds:
        print(f"[rss] 未知 topic={args.topic}，跳过")
        return 0

    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.days)
    rows, ok, failed = [], [], []
    for name, url in feeds:
        try:
            xml_bytes = fetch(url)
            got = parse_feed(xml_bytes, name, cutoff, args.per_feed)
            rows.extend(got)
            ok.append(f"{name}({len(got)})")
        except Exception as exc:
            failed.append(f"{name}: {type(exc).__name__}")
            print(f"[rss] {name} 失败: {exc}")

    rows.sort(key=lambda r: r["ts"], reverse=True)
    rows = rows[: args.total]

    lines = []
    for r in rows:
        lines.append(f"- {r['date']} | {r['feed']} | {r['title']}\n  {r['url']}")

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + ("\n" if lines else ""))

    print(f"[rss] topic={args.topic} 抓到 {len(rows)} 条 -> {args.out}")
    print(f"[rss] ok: {', '.join(ok) if ok else 'none'}")
    if failed:
        print(f"[rss] failed: {', '.join(failed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
