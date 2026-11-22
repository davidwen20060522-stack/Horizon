#!/usr/bin/env python3
"""Export Horizon Chinese daily summary to structured JSON for Pages + personal site.

v2 (2A): HANDOFF 6.2 schema — date/title/timezone/total/categories[].items[]，
保留原 markdown 字段兜底；schema 校验失败或条目数为 0 时拒绝写出（保住 gh-pages
上一份有效 latest.json）。archive.json 同日去重逻辑保留。
"""
import hashlib
import html
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SUMMARY_DIR = Path("data/summaries")
OUTPUT_DIR = Path("docs/news")
PROFILES_DIR = Path("profiles")

_ITEM_HEAD = re.compile(
    r'^### \[((?:\\.|[^\\\]])+)\]\((\S+?)\) ⭐️ ([\d.]+|\?)/10$', re.MULTILINE)
_GROUP_HEAD = re.compile(r'^## (.+)$', re.MULTILINE)
_CN_TIME = re.compile(r'(\d{1,2})月(\d{1,2})日\s+(\d{2}:\d{2})')


def _unescape(text: str) -> str:
    return html.unescape(re.sub(r'\\([\\`*_{}\[\]()#+\-.!|])', r'\1', text)).strip()


def _display_name_map() -> dict:
    """profile display name (zh/en) -> profile id."""
    mapping = {}
    for pfile in PROFILES_DIR.glob("*/profile.json"):
        try:
            data = json.loads(pfile.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        pid = data.get("id") or pfile.parent.name
        mapping[pid] = pid
        if data.get("name"):
            mapping[data["name"]] = pid
        for _lang, disp in (data.get("display_names") or {}).items():
            mapping[disp] = pid
    return mapping


def _parse_summary(markdown: str, date: str):
    """Return list of category dicts with structured items."""
    names = _display_name_map()
    year = int(date.split("-")[0])

    groups = []
    for m in _GROUP_HEAD.finditer(markdown):
        groups.append((m.end(), _unescape(m.group(1))))

    results = []
    for gi, (head_end, raw_name) in enumerate(groups):
        body = markdown[head_end:_grp_end(markdown, head_end)]
        cat_id = names.get(raw_name, raw_name)

        items = []
        heads = list(_ITEM_HEAD.finditer(body))
        for ii, hm in enumerate(heads):
            chunk = body[hm.end():heads[ii + 1].start() if ii + 1 < len(heads) else len(body)]
            title = _unescape(hm.group(1))
            url = html.unescape(hm.group(2))
            score_raw = hm.group(3)
            importance = float(score_raw) if score_raw != "?" else None

            paras = [p.strip() for p in re.split(r"\n\s*\n", chunk) if p.strip()]
            paras = [p for p in paras if not p.startswith("<a id=")]
            summary = _unescape(re.sub(r"\n", " ", paras[0])) if paras else ""

            source, published_at = None, None
            for p in paras:
                if " · " in p and not p.startswith("**") and not p.startswith("<"):
                    parts = [x.strip() for x in p.split(" · ")]
                    src_bits = [x for x in parts
                                if not _CN_TIME.search(x) and not x.startswith("[")]
                    if src_bits:
                        source = " · ".join(src_bits[:2])
                    tm = _CN_TIME.search(p)
                    if tm:
                        try:
                            dt = datetime(year, int(tm.group(1)), int(tm.group(2)),
                                         int(tm.group(3)[:2]), int(tm.group(3)[3:5]))
                            published_at = dt.isoformat() + "+00:00"
                        except ValueError:
                            pass
                    break

            items.append({
                "id": hashlib.sha1(url.encode("utf-8")).hexdigest()[:12],
                "title": title,
                "source": source,
                "published_at": published_at,
                "url": url,
                "summary": summary,
                "importance": importance,
                "category": cat_id,
            })
        if items:
            results.append({"id": cat_id, "name": raw_name, "items": items})
    return results


def _grp_end(markdown: str, pos: int) -> int:
    m = _GROUP_HEAD.search(markdown, pos)
    return m.start() if m else len(markdown)


def _validate(payload: dict):
    if payload["total"] < 1:
        return "0 news items — refusing to overwrite last valid digest"
    if payload["total"] != sum(len(c["items"]) for c in payload["categories"]):
        return "total mismatch"
    for cat in payload["categories"]:
        for it in cat["items"]:
            if not it["title"] or not it["summary"]:
                return f"item missing title/summary: {it['id']}"
            if not it["url"].startswith(("http://", "https://")):
                return f"bad url: {it['url'][:60]}"
    datetime.strptime(payload["date"], "%Y-%m-%d")
    return None


def get_previous_archive():
    """Read previous archive from gh-pages with EXPLICIT failure semantics.

    - gh-pages branch absent (first-ever deploy) -> [] is correct.
    - branch exists but ref/blob unreadable -> raise: the silent
      archive-shrink path (git show rc!=0 without proof of absence) is banned.
    """
    probe = subprocess.run(["git", "ls-remote", "--heads", "origin", "gh-pages"],
                           capture_output=True, text=True)
    if probe.returncode != 0:
        raise RuntimeError("cannot probe origin/gh-pages (ls-remote failed): "
                           + probe.stderr.strip()[:200])
    if not probe.stdout.strip():
        print("archive: no gh-pages branch yet (first deploy) — starting fresh")
        return []

    # ensure a real remote-tracking ref: bare `git fetch origin gh-pages` only
    # writes FETCH_HEAD, which `git show origin/gh-pages:...` cannot resolve
    if subprocess.run(["git", "rev-parse", "--verify", "origin/gh-pages"],
                      capture_output=True).returncode != 0:
        fetched = subprocess.run(
            ["git", "fetch", "origin",
             "+refs/heads/gh-pages:refs/remotes/origin/gh-pages"],
            capture_output=True, text=True)
        if fetched.returncode != 0:
            raise RuntimeError("gh-pages exists on origin but fetch failed: "
                               + fetched.stderr.strip()[:200])

    blob = subprocess.run(["git", "cat-file", "-e", "origin/gh-pages:news/archive.json"],
                          capture_output=True)
    if blob.returncode == 0:
        result = subprocess.run(
            ["git", "show", "origin/gh-pages:news/archive.json"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("git show failed on existing archive blob: "
                               + result.stderr.strip()[:200])
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"previous archive.json unparseable: {exc}")
        if not isinstance(data, list):
            raise RuntimeError("previous archive.json is not a list")
        print(f"archive: merged onto previous ({len(data)} entries)")
        return data

    print("archive: gh-pages has no news/archive.json yet — starting fresh")
    return []


def main():
    files = sorted(SUMMARY_DIR.glob("horizon-*-zh.md"))

    if not files:
        raise SystemExit("No Chinese summary found. Publishing stopped.")

    source = files[-1]
    date = source.name[len("horizon-"):-len("-zh.md")]

    datetime.strptime(date, "%Y-%m-%d")

    markdown = source.read_text(encoding="utf-8")
    categories = _parse_summary(markdown, date)
    total = sum(len(c["items"]) for c in categories)

    payload = {
        "date": date,
        "title": f"Horizon 每日简报 · {date}",
        "timezone": "Asia/Shanghai",
        "total": total,
        "categories": categories,
        "markdown": markdown,
    }

    error = _validate(payload)
    if error:
        raise SystemExit(f"Schema validation failed: {error}")

    # archive read BEFORE any write: if gh-pages state is broken we fail
    # without having produced partial outputs
    archive = get_previous_archive()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for filename in ["latest.json", f"{date}.json"]:
        (OUTPUT_DIR / filename).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    archive = [
        item for item in archive
        if item.get("date") != date
    ]

    archive.insert(0, {
        "date": date,
        "title": payload["title"],
        "url": f"{date}.json",
    })

    archive.sort(
        key=lambda item: item.get("date", ""),
        reverse=True,
    )

    (OUTPUT_DIR / "archive.json").write_text(
        json.dumps(archive, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"News exported: {date}")
    print(f"Structured items: {total} across {len(categories)} categories")
    print(f"Archive entries: {len(archive)}")


if __name__ == "__main__":
    main()
