from __future__ import annotations

from datetime import datetime
from pathlib import Path
from time import sleep
from typing import Any

from .arxiv_client import fetch_arxiv
from .classify import classify_paper
from .config import load_classification_rules, load_keywords, load_sources
from .exporters import export_excel, export_markdown_summary, export_word_report
from .openalex_client import fetch_openalex
from .open_source import detect_open_source
from .scoring import filter_recent, score_relevance
from .schema import Paper
from .storage import dedupe_papers, ensure_dirs, load_inbox_files, save_csv, save_json


def run_daily_inbox(root: Path, max_results: int | None = None) -> dict[str, Path | int]:
    ensure_dirs(root)
    keywords_config = load_keywords(root)
    sources = load_sources(root)
    arxiv_config = sources.get("arxiv", {})
    openalex_config = sources.get("openalex", {})
    arxiv_base_url = arxiv_config.get("base_url", "https://export.arxiv.org/api/query")
    arxiv_default_max = int(arxiv_config.get("max_results_per_keyword", 50))
    arxiv_timeout = int(arxiv_config.get("request_timeout_seconds", 10))
    arxiv_delay = float(arxiv_config.get("delay_seconds", 3))
    arxiv_retries = int(arxiv_config.get("max_retries", 2))
    openalex_base_url = openalex_config.get("base_url", "https://api.openalex.org/works")
    openalex_default_max = int(openalex_config.get("max_results_per_keyword", 25))
    openalex_timeout = int(openalex_config.get("request_timeout_seconds", 20))
    openalex_delay = float(openalex_config.get("delay_seconds", 2))
    openalex_retries = int(openalex_config.get("max_retries", 3))
    openalex_mailto = openalex_config.get("mailto", "")
    current_year = datetime.now().year
    from_year = current_year - 6 + 1
    collected: list[Paper] = []
    errors: list[dict[str, str]] = []

    for keyword in keywords_config.get("primary_keywords", []):
        if arxiv_config.get("enabled", True):
            try:
                collected.extend(
                    fetch_arxiv(
                        keyword,
                        base_url=arxiv_base_url,
                        max_results=max_results or arxiv_default_max,
                        timeout=arxiv_timeout,
                        max_retries=arxiv_retries,
                    )
                )
            except Exception as exc:
                errors.append({"keyword": f"arXiv:{keyword}", "error": repr(exc)})
            sleep(arxiv_delay)
        if openalex_config.get("enabled", True):
            try:
                collected.extend(
                    fetch_openalex(
                        keyword,
                        base_url=openalex_base_url,
                        max_results=max_results or openalex_default_max,
                        from_year=from_year,
                        timeout=openalex_timeout,
                        mailto=openalex_mailto,
                        max_retries=openalex_retries,
                    )
                )
            except Exception as exc:
                errors.append({"keyword": f"OpenAlex:{keyword}", "error": repr(exc)})
            sleep(openalex_delay)

    recent = filter_recent(collected, years=6, current_year=current_year)
    deduped = dedupe_papers(recent)
    today = datetime.now().strftime("%Y%m%d")
    inbox_json = root / "data" / "inbox" / f"daily_inbox_{today}.json"
    inbox_csv = root / "data" / "inbox" / f"daily_inbox_{today}.csv"
    daily_md = root / "outputs" / "daily" / f"daily_summary_{today}.md"
    save_json(inbox_json, deduped)
    save_csv(inbox_csv, deduped)
    export_daily_summary(daily_md, deduped, errors)
    return {"count": len(deduped), "json": inbox_json, "csv": inbox_csv, "summary": daily_md, "errors": len(errors)}


def run_weekly_curated(root: Path, limit_days: int = 7) -> dict[str, Path | int]:
    ensure_dirs(root)
    keywords_config = load_keywords(root)
    rules = load_classification_rules(root)
    papers = dedupe_papers(load_inbox_files(root, limit_days=limit_days))
    curated: list[Paper] = []
    for paper in papers:
        detect_open_source(paper, fetch_pages=False)
        classify_paper(paper, rules)
        score_relevance(
            paper,
            keywords_config.get("primary_keywords", []),
            keywords_config.get("negative_keywords", []),
        )
        curated.append(paper)
    curated = sorted(curated, key=lambda item: (item.relevance_score, item.year or 0), reverse=True)
    year, week, _ = datetime.now().isocalendar()
    stamp = f"{year}-W{week:02d}"
    curated_json = root / "data" / "curated" / f"weekly_curated_{stamp}.json"
    excel_path = root / "outputs" / "weekly" / f"semantic_communication_papers_{stamp}.xlsx"
    word_path = root / "outputs" / "weekly" / f"semantic_communication_report_{stamp}.docx"
    md_path = root / "outputs" / "weekly" / f"weekly_summary_{stamp}.md"
    save_json(curated_json, curated)
    export_excel(excel_path, curated)
    export_word_report(word_path, curated, f"语义通信论文周报 {stamp}")
    export_markdown_summary(md_path, curated, f"语义通信论文周报 {stamp}")
    return {"count": len(curated), "json": curated_json, "excel": excel_path, "word": word_path, "summary": md_path}


def export_daily_summary(path: Path, papers: list[Paper], errors: list[dict[str, Any]] | None = None) -> None:
    lines = ["# Daily Inbox Summary", "", f"新增/候选论文数量：{len(papers)}", "", "## 候选论文"]
    for paper in papers[:50]:
        lines.append(f"- {paper.title} ({paper.year}) | {paper.paper_url}")
    if errors:
        lines.extend(["", "## 抓取错误"])
        for item in errors:
            lines.append(f"- {item.get('keyword')}: {item.get('error')}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
