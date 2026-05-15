from __future__ import annotations

import re
import urllib.parse
import urllib.request

from .schema import Paper


CODE_PATTERNS = [
    re.compile(r"https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", re.IGNORECASE),
    re.compile(r"https?://gitlab\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", re.IGNORECASE),
    re.compile(r"https?://bitbucket\.org/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", re.IGNORECASE),
]

PROJECT_PATTERNS = [
    re.compile(r"https?://[^\s\"'>]*(?:project|demo|code|software)[^\s\"'>]*", re.IGNORECASE),
]


def detect_open_source(paper: Paper, fetch_pages: bool = False, timeout: int = 15) -> Paper:
    haystack = f"{paper.title}\n{paper.abstract}\n{paper.paper_url}\n{paper.pdf_url}"
    code_url = find_first(CODE_PATTERNS, haystack)
    project_url = find_first(PROJECT_PATTERNS, haystack)

    if fetch_pages and not code_url and paper.paper_url:
        page_text = safe_fetch_text(paper.paper_url, timeout=timeout)
        code_url = find_first(CODE_PATTERNS, page_text)
        project_url = project_url or find_first(PROJECT_PATTERNS, page_text)

    paper.code_url = code_url
    paper.project_url = project_url
    paper.is_open_source = bool(code_url)
    paper.open_source_evidence = "code_url_detected" if code_url else "not_detected"
    return paper


def build_github_search_url(title: str) -> str:
    query = urllib.parse.quote_plus(title)
    return f"https://github.com/search?q={query}&type=repositories"


def find_first(patterns: list[re.Pattern[str]], text: str) -> str:
    for pattern in patterns:
        match = pattern.search(text or "")
        if match:
            return match.group(0).rstrip(".,)")
    return ""


def safe_fetch_text(url: str, timeout: int = 15) -> str:
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "semantic-communication-paper-tracker/0.1"})
        with urllib.request.urlopen(request, timeout=timeout) as response:
            content_type = response.headers.get("content-type", "")
            if "text" not in content_type and "html" not in content_type:
                return ""
            return response.read(500_000).decode("utf-8", errors="ignore")
    except Exception:
        return ""
