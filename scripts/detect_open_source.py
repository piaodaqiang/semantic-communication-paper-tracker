from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from paper_tracker.open_source import detect_open_source
from paper_tracker.storage import load_json, save_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Detect open-source evidence for papers.")
    parser.add_argument("input_json")
    parser.add_argument("output_json")
    parser.add_argument("--fetch-pages", action="store_true", help="Fetch paper pages for code links.")
    args = parser.parse_args()
    papers = [detect_open_source(paper, fetch_pages=args.fetch_pages) for paper in load_json(Path(args.input_json))]
    save_json(Path(args.output_json), papers)
    print(f"Checked {len(papers)} papers -> {args.output_json}")


if __name__ == "__main__":
    main()
