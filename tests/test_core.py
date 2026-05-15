import unittest
import zipfile
from pathlib import Path

from paper_tracker.arxiv_client import parse_arxiv_feed
from paper_tracker.classify import classify_paper
from paper_tracker.config import DEFAULT_CLASSIFICATION_RULES
from paper_tracker.open_source import detect_open_source
from paper_tracker.exporters import export_excel, export_word_report
from paper_tracker.scoring import filter_recent, score_relevance
from paper_tracker.schema import Paper
from paper_tracker.storage import dedupe_papers


class CoreTests(unittest.TestCase):
    def test_parse_arxiv_feed_extracts_paper(self) -> None:
        xml = b"""<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
          <entry>
            <id>http://arxiv.org/abs/2601.00001v1</id>
            <published>2026-01-01T00:00:00Z</published>
            <title>Semantic Communication for Text Transmission</title>
            <summary>A DeepSC based semantic communication system.</summary>
            <author><name>Alice</name></author>
            <link href="http://arxiv.org/pdf/2601.00001v1" type="application/pdf" title="pdf"/>
          </entry>
        </feed>"""
        papers = parse_arxiv_feed(xml, "semantic communication")
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0].year, 2026)
        self.assertEqual(papers[0].arxiv_id, "2601.00001v1")

    def test_filter_recent_keeps_only_last_six_years(self) -> None:
        papers = [Paper(paper_id="a", title="old", year=2019), Paper(paper_id="b", title="new", year=2026)]
        self.assertEqual([paper.paper_id for paper in filter_recent(papers, years=6, current_year=2026)], ["b"])

    def test_dedupe_by_arxiv_id(self) -> None:
        papers = [
            Paper(paper_id="1", title="A", arxiv_id="2601.00001"),
            Paper(paper_id="2", title="A copy", arxiv_id="2601.00001", abstract="copy"),
        ]
        self.assertEqual(len(dedupe_papers(papers)), 1)

    def test_classify_text_transformer(self) -> None:
        paper = Paper(
            paper_id="p",
            title="Transformer based DeepSC for text semantic communication",
            abstract="A task-oriented semantic communication method for language transmission.",
        )
        classify_paper(paper, DEFAULT_CLASSIFICATION_RULES)
        self.assertEqual(paper.application_scenario, "文本语义通信")
        self.assertIn(paper.technical_framework, {"Autoencoder / DeepSC", "Transformer"})

    def test_detect_open_source_from_abstract(self) -> None:
        paper = Paper(
            paper_id="p",
            title="Open source semantic communication",
            abstract="Code is available at https://github.com/example/semantic-comm.",
        )
        detect_open_source(paper)
        self.assertTrue(paper.is_open_source)
        self.assertEqual(paper.code_url, "https://github.com/example/semantic-comm")

    def test_score_relevance_marks_curated(self) -> None:
        paper = Paper(
            paper_id="p",
            title="Semantic communication for wireless systems",
            abstract="Semantic communication and channel transmission.",
        )
        score_relevance(paper, ["semantic communication"], [])
        self.assertGreaterEqual(paper.relevance_score, 3.0)
        self.assertEqual(paper.curation_status, "curated")

    def test_exports_excel_and_word_files(self) -> None:
        output_dir = Path("tests") / "_artifacts"
        output_dir.mkdir(exist_ok=True)
        paper = Paper(
            paper_id="p",
            title="Semantic communication with open source code",
            year=2026,
            abstract="Code is available at https://github.com/example/semantic-comm.",
            application_scenario="文本语义通信",
            technical_framework="Transformer",
            relevance_score=8.0,
            is_open_source=True,
            code_url="https://github.com/example/semantic-comm",
        )
        excel_path = output_dir / "sample.xlsx"
        word_path = output_dir / "sample.docx"
        export_excel(excel_path, [paper])
        export_word_report(word_path, [paper], "语义通信测试报告")
        self.assertTrue(excel_path.exists() or excel_path.with_suffix(".csv").exists())
        self.assertTrue(word_path.exists())
        self.assertTrue(zipfile.is_zipfile(word_path))


if __name__ == "__main__":
    unittest.main()
