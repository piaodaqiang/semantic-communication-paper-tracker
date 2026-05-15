from __future__ import annotations

from datetime import datetime
import re

from .schema import Paper


def filter_recent(papers: list[Paper], years: int = 6, current_year: int | None = None) -> list[Paper]:
    current_year = current_year or datetime.now().year
    min_year = current_year - years + 1
    return [paper for paper in papers if paper.year and min_year <= paper.year <= current_year]


def score_relevance(paper: Paper, primary_keywords: list[str], negative_keywords: list[str]) -> Paper:
    text = f"{paper.title} {paper.abstract}".lower()
    if not has_core_semantic_signal(text):
        paper.relevance_score = 0.0
        paper.curation_status = "candidate"
        paper.notes = "缺少语义通信核心组合词，需要人工复核"
        return paper

    score = 0.0
    for keyword in primary_keywords:
        if keyword.lower() in text:
            score += 2.0
    for soft_term in ["wireless", "communication", "semantic", "transmission", "channel", "task"]:
        if soft_term in text:
            score += 0.5
    for keyword in negative_keywords:
        if keyword.lower() in text:
            score -= 2.0
    if "semantic communication" in text or "semantic communications" in text:
        score += 3.0
    if paper.is_open_source:
        score += 0.5
    paper.relevance_score = round(max(score, 0.0), 2)
    paper.curation_status = "curated" if paper.relevance_score >= 3.0 else "candidate"
    if paper.relevance_score < 3.0:
        paper.notes = "低相关性候选，需要人工复核"
    return paper


def has_core_semantic_signal(text: str) -> bool:
    normalized = " ".join(text.lower().split())
    core_patterns = [
        r"\bsemantic communications?\b",
        r"\bsemcom\b",
        r"\bsemantic-aware\s+(?:communication|communications|transmission|coding)\b",
        r"\b(?:task|goal)-oriented\s+semantic\s+(?:communication|communications)\b",
        r"\bsemantic\s+(?:source|channel)\s+coding\b",
    ]
    return any(re.search(pattern, normalized) for pattern in core_patterns)
