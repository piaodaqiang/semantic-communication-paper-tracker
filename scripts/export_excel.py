from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from paper_tracker.exporters import export_excel
from paper_tracker.storage import load_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Export paper JSON to Excel.")
    parser.add_argument("input_json")
    parser.add_argument("output_xlsx")
    args = parser.parse_args()
    papers = load_json(Path(args.input_json))
    export_excel(Path(args.output_xlsx), papers)
    print(f"Exported {len(papers)} papers -> {args.output_xlsx}")


if __name__ == "__main__":
    main()
