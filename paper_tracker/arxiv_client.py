from __future__ import annotations

import hashlib
import re
import ssl
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

from .schema import Paper


ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"


def fetch_arxiv(
    keyword: str,
    base_url: str,
    max_results: int,
    timeout: int = 30,
    max_retries: int = 2,
) -> list[Paper]:
    query = urllib.parse.urlencode(
        {
            "search_query": build_arxiv_query(keyword),
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"{base_url}?{query}"
    request = urllib.request.Request(url, headers={"User-Agent": "semantic-communication-paper-tracker/0.1"})
    xml_text = open_with_retries(request, timeout=timeout, max_retries=max_retries)
    return parse_arxiv_feed(xml_text, keyword)


def open_with_retries(request: urllib.request.Request, timeout: int, max_retries: int) -> bytes:
    last_error: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=ssl_context()) as response:
                return response.read()
        except Exception as exc:
            last_error = exc
            if attempt >= max_retries:
                break
            time.sleep(retry_delay(exc, attempt))
    raise last_error or RuntimeError("request failed")


def retry_delay(exc: Exception, attempt: int) -> float:
    retry_after = getattr(exc, "headers", {}).get("Retry-After") if hasattr(exc, "headers") else None
    if retry_after:
        try:
            return min(float(retry_after), 30.0)
        except ValueError:
            pass
    return min(2.0 * (attempt + 1), 10.0)


def build_arxiv_query(keyword: str) -> str:
    terms = [term for term in re.split(r"\s+", keyword.strip()) if term]
    if len(terms) <= 1:
        return f"all:{keyword}"
    return " AND ".join(f"all:{term}" for term in terms)


def ssl_context() -> ssl.SSLContext | None:
    try:
        import certifi  # type: ignore

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return None


def parse_arxiv_feed(xml_text: bytes | str, keyword: str) -> list[Paper]:
    root = ET.fromstring(xml_text)
    papers = []
    for entry in root.findall(f"{ATOM}entry"):
        title = _clean_text(entry.findtext(f"{ATOM}title"))
        abstract = _clean_text(entry.findtext(f"{ATOM}summary"))
        arxiv_comment = _clean_text(entry.findtext(f"{ARXIV}comment"))
        published = entry.findtext(f"{ATOM}published") or ""
        year = _parse_year(published)
        paper_url = entry.findtext(f"{ATOM}id") or ""
        arxiv_id = paper_url.rsplit("/", 1)[-1]
        pdf_url = ""
        for link in entry.findall(f"{ATOM}link"):
            if link.attrib.get("title") == "pdf" or link.attrib.get("type") == "application/pdf":
                pdf_url = link.attrib.get("href", "")
                break
        authors = [
            _clean_text(author.findtext(f"{ATOM}name"))
            for author in entry.findall(f"{ATOM}author")
            if author.findtext(f"{ATOM}name")
        ]
        doi = entry.findtext(f"{ARXIV}doi") or ""
        paper_id = f"arxiv:{arxiv_id}" if arxiv_id else _stable_id(title)
        papers.append(
            Paper(
                paper_id=paper_id,
                title=title,
                authors=authors,
                year=year,
                venue="arXiv",
                source="arXiv",
                doi=doi,
                arxiv_id=arxiv_id,
                paper_url=paper_url,
                pdf_url=pdf_url,
                abstract=abstract,
                arxiv_comment=arxiv_comment,
                keywords=[keyword],
            )
        )
    return papers


def _clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def _parse_year(value: str) -> int | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).year
    except ValueError:
        match = re.search(r"(19|20)\d{2}", value)
        return int(match.group(0)) if match else None


def _stable_id(title: str) -> str:
    return "title:" + hashlib.sha1(title.lower().encode("utf-8")).hexdigest()[:12]
