from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from paper_tracker.pipeline import run_daily_inbox


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch QueueA Daily Inbox papers.")
    parser.add_argument("--root", default=".", help="Project root directory.")
    parser.add_argument("--max-results", type=int, default=None, help="Max arXiv results per keyword.")
    parser.add_argument("--fail-on-empty", action="store_true", help="Exit with code 2 when no papers are found.")
    args = parser.parse_args()
    result = run_daily_inbox(Path(args.root).resolve(), max_results=args.max_results)
    print(f"Daily Inbox complete: {result['count']} papers")
    print(f"Fetch errors: {result['errors']}")
    print(f"JSON: {result['json']}")
    print(f"CSV: {result['csv']}")
    print(f"Summary: {result['summary']}")
    if args.fail_on_empty and int(result["count"]) == 0:
        raise SystemExit("Daily Inbox found 0 papers; failing to avoid publishing empty outputs.")


if __name__ == "__main__":
    main()
