from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from paper_tracker.exporters import export_word_report
from paper_tracker.storage import load_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Export paper JSON to Word report.")
    parser.add_argument("input_json")
    parser.add_argument("output_docx")
    parser.add_argument("--title", default="语义通信论文整理报告")
    args = parser.parse_args()
    papers = load_json(Path(args.input_json))
    export_word_report(Path(args.output_docx), papers, args.title)
    print(f"Exported {len(papers)} papers -> {args.output_docx}")


if __name__ == "__main__":
    main()
