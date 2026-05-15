from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Iterable

from .schema import PAPER_FIELDS, Paper


def ensure_dirs(root: Path) -> None:
    for relative in [
        "data/raw",
        "data/inbox",
        "data/curated",
        "outputs/daily",
        "outputs/weekly",
        "cache/pdfs",
    ]:
        (root / relative).mkdir(parents=True, exist_ok=True)


def save_json(path: Path, papers: Iterable[Paper]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [paper.to_dict() for paper in papers]
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_json(path: Path) -> list[Paper]:
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [Paper.from_dict(item) for item in payload]


def save_csv(path: Path, papers: Iterable[Paper]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [paper.to_dict() for paper in papers]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=PAPER_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in PAPER_FIELDS})


def load_inbox_files(root: Path, limit_days: int | None = None) -> list[Paper]:
    files = sorted((root / "data" / "inbox").glob("*.json"))
    if limit_days:
        files = files[-limit_days:]
    papers: list[Paper] = []
    for file in files:
        papers.extend(load_json(file))
    return papers


def dedupe_papers(papers: Iterable[Paper]) -> list[Paper]:
    seen: dict[str, Paper] = {}
    for paper in papers:
        key = _dedupe_key(paper)
        if key not in seen:
            seen[key] = paper
            continue
        seen[key] = _merge_paper(seen[key], paper)
    return list(seen.values())


def _dedupe_key(paper: Paper) -> str:
    normalized_title = normalize_title(paper.title)
    if len(normalized_title) >= 20:
        return f"title:{normalized_title}"
    if paper.doi:
        return f"doi:{paper.doi.lower()}"
    if paper.arxiv_id:
        return f"arxiv:{paper.arxiv_id.lower()}"
    return f"title:{normalized_title}"


def normalize_title(title: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", " ", title.lower())
    return " ".join(normalized.split())


def _merge_paper(left: Paper, right: Paper) -> Paper:
    merged = Paper.from_dict(left.to_dict())
    for field in PAPER_FIELDS:
        current = getattr(merged, field)
        candidate = getattr(right, field)
        if field in {"authors", "keywords"}:
            combined = []
            for item in list(current) + list(candidate):
                if item and item not in combined:
                    combined.append(item)
            setattr(merged, field, combined)
        elif field == "is_open_source":
            setattr(merged, field, bool(current or candidate))
        elif field == "relevance_score":
            setattr(merged, field, max(float(current or 0), float(candidate or 0)))
        elif not current and candidate:
            setattr(merged, field, candidate)
    return merged
