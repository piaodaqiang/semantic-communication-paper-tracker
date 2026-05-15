from __future__ import annotations

from datetime import datetime

from .schema import Paper


def filter_recent(papers: list[Paper], years: int = 6, current_year: int | None = None) -> list[Paper]:
    current_year = current_year or datetime.now().year
    min_year = current_year - years + 1
    return [paper for paper in papers if paper.year and paper.year >= min_year]


def score_relevance(paper: Paper, primary_keywords: list[str], negative_keywords: list[str]) -> Paper:
    text = f"{paper.title} {paper.abstract}".lower()
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
