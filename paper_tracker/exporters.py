from __future__ import annotations

import html
import zipfile
from collections import Counter
from pathlib import Path

from .schema import PAPER_FIELDS, Paper


def export_excel(path: Path, papers: list[Paper]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill
        from openpyxl.utils import get_column_letter
    except ModuleNotFoundError:
        fallback = path.with_suffix(".csv")
        from .storage import save_csv

        save_csv(fallback, papers)
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "papers"
    ws.append(PAPER_FIELDS)
    header_fill = PatternFill("solid", fgColor="D9EAF7")
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.fill = header_fill
    for paper in papers:
        row = paper.to_dict()
        ws.append([row.get(field, "") for field in PAPER_FIELDS])
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    for index, field in enumerate(PAPER_FIELDS, start=1):
        width = 14
        if field in {"title", "abstract", "paper_url", "pdf_url", "code_url", "project_url"}:
            width = 42
        elif field in {"authors", "application_scenario", "technical_framework"}:
            width = 24
        ws.column_dimensions[get_column_letter(index)].width = width
    wb.save(path)


def export_markdown_summary(path: Path, papers: list[Paper], title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {title}", ""]
    lines.extend(build_summary_lines(papers))
    lines.append("")
    lines.append("## 建议精读论文")
    for paper in sorted(papers, key=lambda item: item.relevance_score, reverse=True)[:10]:
        code = "开源" if paper.is_open_source else "未发现开源"
        lines.append(f"- {paper.title} ({paper.year}) | {paper.application_scenario} | {paper.technical_framework} | {code}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def export_word_report(path: Path, papers: list[Paper], title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        from docx import Document
    except ModuleNotFoundError:
        write_minimal_docx(path, papers, title)
        return

    doc = Document()
    doc.add_heading(title, level=0)
    for line in build_summary_lines(papers):
        doc.add_paragraph(line)
    doc.add_heading("建议精读论文", level=1)
    for paper in sorted(papers, key=lambda item: item.relevance_score, reverse=True)[:10]:
        doc.add_paragraph(
            f"{paper.title}（{paper.year}）｜{paper.application_scenario}｜{paper.technical_framework}｜相关性 {paper.relevance_score}",
            style="List Bullet",
        )
    doc.add_heading("开源论文", level=1)
    for paper in [item for item in papers if item.is_open_source][:20]:
        doc.add_paragraph(f"{paper.title}：{paper.code_url}", style="List Bullet")
    doc.save(path)


def build_summary_lines(papers: list[Paper]) -> list[str]:
    year_counter = Counter(str(paper.year) for paper in papers if paper.year)
    scenario_counter = Counter(paper.application_scenario for paper in papers)
    framework_counter = Counter(paper.technical_framework for paper in papers)
    open_count = sum(1 for paper in papers if paper.is_open_source)
    return [
        f"论文总数：{len(papers)}",
        f"开源论文数：{open_count}",
        "年份分布：" + format_counter(year_counter),
        "场景分布：" + format_counter(scenario_counter),
        "技术框架分布：" + format_counter(framework_counter),
    ]


def format_counter(counter: Counter[str]) -> str:
    if not counter:
        return "无"
    return "；".join(f"{key} {value}" for key, value in counter.most_common())


def write_minimal_docx(path: Path, papers: list[Paper], title: str) -> None:
    paragraphs = [title, *build_summary_lines(papers), "建议精读论文"]
    for paper in sorted(papers, key=lambda item: item.relevance_score, reverse=True)[:10]:
        paragraphs.append(f"{paper.title}（{paper.year}）｜{paper.application_scenario}｜{paper.technical_framework}")
    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'
        + "".join(_docx_paragraph(text) for text in paragraphs)
        + "<w:sectPr/></w:body></w:document>"
    )
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", RELS)
        docx.writestr("word/document.xml", document_xml)


def _docx_paragraph(text: str) -> str:
    return f"<w:p><w:r><w:t>{html.escape(text)}</w:t></w:r></w:p>"


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""
