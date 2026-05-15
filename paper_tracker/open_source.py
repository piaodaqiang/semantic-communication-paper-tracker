from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from typing import Any

from .arxiv_client import open_with_retries
from .schema import Paper


CODE_PATTERNS = [
    re.compile(r"https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", re.IGNORECASE),
    re.compile(r"https?://gitlab\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", re.IGNORECASE),
    re.compile(r"https?://bitbucket\.org/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", re.IGNORECASE),
]

PROJECT_PATTERNS = [
    re.compile(r"https?://[^\s\"'<>)\]]*(?:project|demo|code|software)[^\s\"'<>)\]]*", re.IGNORECASE),
]


DEFAULT_OPTIONS = {
    "papers_with_code_enabled": True,
    "papers_with_code_base_url": "https://paperswithcode.com/api/v1/search/",
    "github_search_enabled": True,
    "github_search_url": "https://api.github.com/search/repositories",
    "pdf_extract_enabled": True,
    "request_timeout_seconds": 12,
    "max_pdf_bytes": 750000,
    "github_max_results": 3,
}


def detect_open_source(
    paper: Paper,
    fetch_pages: bool = False,
    timeout: int = 15,
    options: dict[str, Any] | None = None,
) -> Paper:
    opts = {**DEFAULT_OPTIONS, **(options or {})}
    timeout = int(opts.get("request_timeout_seconds", timeout))
    errors: list[str] = []

    result = detect_from_text(paper)
    if not result and fetch_pages and paper.paper_url:
        page_text = safe_fetch_text(paper.paper_url, timeout=timeout)
        result = detect_from_text_blob(page_text, "paper_page")

    if not result and opts.get("papers_with_code_enabled", True):
        result, error = detect_from_papers_with_code(paper, opts, timeout)
        if error:
            errors.append(f"source_error:papers_with_code:{error}")

    if not result and opts.get("github_search_enabled", True):
        result, error = detect_from_github_search(paper, opts, timeout)
        if error:
            errors.append(f"source_error:github_search:{error}")

    if not result and opts.get("pdf_extract_enabled", True):
        result, error = detect_from_pdf(paper, opts, timeout)
        if error:
            errors.append(f"source_error:pdf_link_extract:{error}")

    if result:
        paper.code_url = result.get("code_url", "")
        paper.project_url = result.get("project_url", "")
        paper.is_open_source = bool(paper.code_url)
        paper.open_source_evidence = result.get("evidence", "metadata")
    else:
        paper.code_url = ""
        paper.project_url = ""
        paper.is_open_source = False
        paper.open_source_evidence = compact_errors(errors) if errors else "not_detected"
    return paper


def detect_from_text(paper: Paper) -> dict[str, str] | None:
    metadata = f"{paper.title}\n{paper.abstract}\n{paper.paper_url}\n{paper.pdf_url}"
    result = detect_from_text_blob(metadata, "metadata")
    if result:
        return result
    comment = getattr(paper, "arxiv_comment", "")
    if comment:
        return detect_from_text_blob(comment, "arxiv_comment")
    return None


def detect_from_text_blob(text: str, evidence: str) -> dict[str, str] | None:
    code_url = find_first(CODE_PATTERNS, text)
    project_url = find_first(PROJECT_PATTERNS, text)
    if code_url:
        return {"code_url": code_url, "project_url": project_url, "evidence": evidence}
    if project_url:
        return {"code_url": "", "project_url": project_url, "evidence": evidence}
    return None


def detect_from_papers_with_code(
    paper: Paper,
    options: dict[str, Any],
    timeout: int,
) -> tuple[dict[str, str] | None, str | None]:
    try:
        query = urllib.parse.urlencode({"q": paper.title})
        url = f"{options['papers_with_code_base_url']}?{query}"
        payload = fetch_json(url, timeout=timeout)
        candidates = payload.get("results", []) if isinstance(payload, dict) else []
        for item in candidates:
            title = str(item.get("paper_title") or item.get("title") or "")
            if title_similarity(paper.title, title) < 0.82:
                continue
            repo_url = str(item.get("repository") or item.get("code_url") or item.get("url_abs") or "")
            code_url = find_first(CODE_PATTERNS, repo_url)
            project_url = str(item.get("paper_url") or item.get("url_abs") or "")
            if code_url:
                return {"code_url": code_url, "project_url": project_url, "evidence": "papers_with_code"}, None
        return None, None
    except Exception as exc:
        return None, normalize_error(exc)


def detect_from_github_search(
    paper: Paper,
    options: dict[str, Any],
    timeout: int,
) -> tuple[dict[str, str] | None, str | None]:
    try:
        query = urllib.parse.urlencode(
            {
                "q": f'"{paper.title}" in:readme,description',
                "sort": "stars",
                "order": "desc",
                "per_page": int(options.get("github_max_results", 3)),
            }
        )
        payload = fetch_json(f"{options['github_search_url']}?{query}", timeout=timeout)
        for item in payload.get("items", []):
            repo_url = str(item.get("html_url") or "")
            searchable = " ".join(
                [
                    str(item.get("name") or ""),
                    str(item.get("full_name") or ""),
                    str(item.get("description") or ""),
                    str(item.get("topics") or ""),
                ]
            )
            if title_similarity(paper.title, searchable) >= 0.45 or core_terms_overlap(paper.title, searchable) >= 3:
                code_url = find_first(CODE_PATTERNS, repo_url)
                if code_url:
                    return {"code_url": code_url, "project_url": repo_url, "evidence": "github_search"}, None
        return None, None
    except Exception as exc:
        return None, normalize_error(exc)


def detect_from_pdf(
    paper: Paper,
    options: dict[str, Any],
    timeout: int,
) -> tuple[dict[str, str] | None, str | None]:
    if not paper.pdf_url:
        return None, None
    try:
        text = safe_fetch_binary_as_text(
            paper.pdf_url,
            timeout=timeout,
            max_bytes=int(options.get("max_pdf_bytes", 750000)),
        )
        return detect_from_text_blob(text, "pdf_link_extract"), None
    except Exception as exc:
        return None, normalize_error(exc)


def compact_errors(errors: list[str]) -> str:
    if not errors:
        return "not_detected"
    unique = []
    for error in errors:
        source = ":".join(error.split(":")[:2])
        if source not in unique:
            unique.append(source)
    return ";".join(unique)


def normalize_error(exc: Exception) -> str:
    name = exc.__class__.__name__
    if name in {"JSONDecodeError", "UnicodeDecodeError"}:
        return "invalid_response"
    return name


def fetch_json(url: str, timeout: int) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": "semantic-communication-paper-tracker/0.1"})
    data = open_with_retries(request, timeout=timeout, max_retries=1)
    return json.loads(data.decode("utf-8", errors="ignore"))


def safe_fetch_text(url: str, timeout: int = 15) -> str:
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "semantic-communication-paper-tracker/0.1"})
        data = open_with_retries(request, timeout=timeout, max_retries=1)
        return data[:500_000].decode("utf-8", errors="ignore")
    except Exception:
        return ""


def safe_fetch_binary_as_text(url: str, timeout: int, max_bytes: int) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "semantic-communication-paper-tracker/0.1"})
    data = open_with_retries(request, timeout=timeout, max_retries=1)
    return data[:max_bytes].decode("latin-1", errors="ignore")


def build_github_search_url(title: str) -> str:
    query = urllib.parse.quote_plus(title)
    return f"https://github.com/search?q={query}&type=repositories"


def find_first(patterns: list[re.Pattern[str]], text: str) -> str:
    for pattern in patterns:
        match = pattern.search(text or "")
        if match:
            return clean_url(match.group(0))
    return ""


def clean_url(url: str) -> str:
    return url.rstrip(".,);]}'\"")


def title_similarity(left: str, right: str) -> float:
    return SequenceMatcher(None, normalize(left), normalize(right)).ratio()


def core_terms_overlap(title: str, candidate: str) -> int:
    title_terms = set(normalize(title).split())
    candidate_terms = set(normalize(candidate).split())
    stopwords = {"for", "and", "the", "with", "of", "in", "on", "to", "a", "an"}
    return len((title_terms - stopwords) & (candidate_terms - stopwords))


def normalize(value: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value.lower()).split())
