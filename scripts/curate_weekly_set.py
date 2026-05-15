from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from paper_tracker.pipeline import run_weekly_curated


def main() -> None:
    parser = argparse.ArgumentParser(description="Build QueueB Weekly Curated Set.")
    parser.add_argument("--root", default=".", help="Project root directory.")
    parser.add_argument("--limit-days", type=int, default=7, help="How many latest inbox files to read.")
    args = parser.parse_args()
    result = run_weekly_curated(Path(args.root).resolve(), limit_days=args.limit_days)
    print(f"Weekly Curated Set complete: {result['count']} papers")
    print(f"JSON: {result['json']}")
    print(f"Excel: {result['excel']}")
    print(f"Word: {result['word']}")
    print(f"Summary: {result['summary']}")


if __name__ == "__main__":
    main()
