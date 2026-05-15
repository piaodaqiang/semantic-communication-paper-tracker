from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from paper_tracker.classify import classify_paper
from paper_tracker.config import load_classification_rules
from paper_tracker.storage import load_json, save_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify papers from a JSON file.")
    parser.add_argument("input_json")
    parser.add_argument("output_json")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    rules = load_classification_rules(root)
    papers = [classify_paper(paper, rules) for paper in load_json(Path(args.input_json))]
    save_json(Path(args.output_json), papers)
    print(f"Classified {len(papers)} papers -> {args.output_json}")


if __name__ == "__main__":
    main()
