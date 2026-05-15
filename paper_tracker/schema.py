from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


PAPER_FIELDS = [
    "paper_id",
    "title",
    "authors",
    "year",
    "venue",
    "source",
    "doi",
    "arxiv_id",
    "paper_url",
    "pdf_url",
    "abstract",
    "arxiv_comment",
    "keywords",
    "is_open_source",
    "code_url",
    "project_url",
    "open_source_evidence",
    "application_scenario",
    "technical_framework",
    "task_type",
    "modality",
    "relevance_score",
    "curation_status",
    "notes",
    "last_checked_at",
]


@dataclass
class Paper:
    paper_id: str
    title: str
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    venue: str = ""
    source: str = ""
    doi: str = ""
    arxiv_id: str = ""
    paper_url: str = ""
    pdf_url: str = ""
    abstract: str = ""
    arxiv_comment: str = ""
    keywords: list[str] = field(default_factory=list)
    is_open_source: bool = False
    code_url: str = ""
    project_url: str = ""
    open_source_evidence: str = ""
    application_scenario: str = "未分类"
    technical_framework: str = "未分类"
    task_type: str = ""
    modality: str = ""
    relevance_score: float = 0.0
    curation_status: str = "inbox"
    notes: str = ""
    last_checked_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict[str, Any]:
        row = asdict(self)
        row["authors"] = "; ".join(self.authors)
        row["keywords"] = "; ".join(self.keywords)
        return row

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Paper":
        clean = {field_name: data.get(field_name, "") for field_name in PAPER_FIELDS}
        if isinstance(clean["authors"], str):
            clean["authors"] = [item.strip() for item in clean["authors"].split(";") if item.strip()]
        if isinstance(clean["keywords"], str):
            clean["keywords"] = [item.strip() for item in clean["keywords"].split(";") if item.strip()]
        if clean["year"] in ("", None):
            clean["year"] = None
        else:
            clean["year"] = int(clean["year"])
        if isinstance(clean["is_open_source"], str):
            clean["is_open_source"] = clean["is_open_source"].lower() in {"true", "1", "yes", "是"}
        if clean["relevance_score"] in ("", None):
            clean["relevance_score"] = 0.0
        else:
            clean["relevance_score"] = float(clean["relevance_score"])
        return cls(**clean)
