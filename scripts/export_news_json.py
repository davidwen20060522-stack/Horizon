
import json
import subprocess
from datetime import datetime
from pathlib import Path

SUMMARY_DIR = Path("data/summaries")
OUTPUT_DIR = Path("docs/news")


def get_previous_archive():
    result = subprocess.run(
        ["git", "show", "origin/gh-pages:news/archive.json"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return []

    try:
        data = json.loads(result.stdout)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def main():
    files = sorted(SUMMARY_DIR.glob("horizon-*-zh.md"))

    if not files:
        raise SystemExit("No Chinese summary found. Publishing stopped.")

    source = files[-1]
    date = source.name[len("horizon-"):-len("-zh.md")]

    datetime.strptime(date, "%Y-%m-%d")

    markdown = source.read_text(encoding="utf-8")

    payload = {
        "date": date,
        "title": f"Horizon 每日速递 · {date}",
        "language": "zh",
        "markdown": markdown,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for filename in ["latest.json", f"{date}.json"]:
        (OUTPUT_DIR / filename).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    archive = get_previous_archive()
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
    print(f"Archive entries: {len(archive)}")


if __name__ == "__main__":
    main()
