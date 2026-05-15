from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from typing import Any

from .arxiv_client import open_with_retries
from .schema import Paper


def fetch_openalex(
    keyword: str,
    base_url: str,
    max_results: int,
    from_year: int,
    timeout: int = 30,
    mailto: str = "",
    max_retries: int = 3,
) -> list[Paper]:
    params = {
        "search": keyword,
        "filter": f"from_publication_date:{from_year}-01-01",
        "sort": "publication_date:desc",
        "per-page": max_results,
    }
    if mailto:
        params["mailto"] = mailto
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "semantic-communication-paper-tracker/0.1"})
    payload = json.loads(open_with_retries(request, timeout=timeout, max_retries=max_retries).decode("utf-8"))
    return parse_openalex_works(payload, keyword)


def parse_openalex_works(payload: dict[str, Any], keyword: str) -> list[Paper]:
    papers: list[Paper] = []
    for item in payload.get("results", []):
        title = clean_text(item.get("display_name", ""))
        if not title:
            continue
        authors = [
            clean_text(authorship.get("author", {}).get("display_name", ""))
            for authorship in item.get("authorships", [])
            if authorship.get("author", {}).get("display_name")
        ]
        primary_location = item.get("primary_location") or {}
        source = primary_location.get("source") or {}
        open_access = item.get("open_access") or {}
        ids = item.get("ids") or {}
        best_oa_location = item.get("best_oa_location") or {}
        paper_url = primary_location.get("landing_page_url") or item.get("id") or ""
        pdf_url = primary_location.get("pdf_url") or best_oa_location.get("pdf_url") or open_access.get("oa_url") or ""
        arxiv_id = extract_arxiv_id(ids, paper_url, pdf_url)
        papers.append(
            Paper(
                paper_id=f"openalex:{item.get('id', title)}",
                title=title,
                authors=authors,
                year=item.get("publication_year"),
                venue=clean_text(source.get("display_name", "")),
                source="OpenAlex",
                doi=(ids.get("doi") or item.get("doi") or "").replace("https://doi.org/", ""),
                arxiv_id=arxiv_id,
                paper_url=paper_url,
                pdf_url=pdf_url,
                abstract=reconstruct_abstract(item.get("abstract_inverted_index") or {}),
                keywords=[keyword],
                open_source_evidence="open_access_pdf" if pdf_url else "",
            )
        )
    return papers


def reconstruct_abstract(inverted_index: dict[str, list[int]]) -> str:
    if not inverted_index:
        return ""
    positioned: list[tuple[int, str]] = []
    for word, positions in inverted_index.items():
        for position in positions:
            positioned.append((int(position), word))
    return " ".join(word for _, word in sorted(positioned))


def extract_arxiv_id(ids: dict[str, Any], *urls: str) -> str:
    for value in [ids.get("arxiv"), *urls]:
        if not value:
            continue
        match = re.search(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", str(value), re.IGNORECASE)
        if match:
            return match.group(1).removesuffix(".pdf")
    return ""


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()
