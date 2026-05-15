import unittest
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

from paper_tracker.arxiv_client import parse_arxiv_feed
from paper_tracker.classify import classify_paper
from paper_tracker.config import DEFAULT_CLASSIFICATION_RULES
from paper_tracker.open_source import detect_open_source
from paper_tracker.exporters import export_excel, export_word_report
from paper_tracker.openalex_client import parse_openalex_works, reconstruct_abstract
from paper_tracker.pipeline import run_weekly_curated
from paper_tracker.scoring import filter_recent, has_core_semantic_signal, score_relevance
from paper_tracker.schema import Paper
from paper_tracker.storage import dedupe_papers, save_json


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

    def test_parse_openalex_works_extracts_paper(self) -> None:
        payload = {
            "results": [
                {
                    "id": "https://openalex.org/W1",
                    "display_name": "Semantic Communication for Wireless Networks",
                    "publication_year": 2025,
                    "doi": "https://doi.org/10.1234/example",
                    "authorships": [{"author": {"display_name": "Alice"}}],
                    "primary_location": {
                        "landing_page_url": "https://example.org/paper",
                        "pdf_url": "https://example.org/paper.pdf",
                        "source": {"display_name": "Example Venue"},
                    },
                    "abstract_inverted_index": {"Semantic": [0], "communication": [1], "works": [2]},
                }
            ]
        }
        papers = parse_openalex_works(payload, "semantic communication")
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0].source, "OpenAlex")
        self.assertEqual(papers[0].year, 2025)
        self.assertEqual(papers[0].abstract, "Semantic communication works")

    def test_filter_recent_keeps_only_last_six_years(self) -> None:
        papers = [
            Paper(paper_id="a", title="old", year=2019),
            Paper(paper_id="b", title="new", year=2026),
            Paper(paper_id="c", title="future", year=2027),
        ]
        self.assertEqual([paper.paper_id for paper in filter_recent(papers, years=6, current_year=2026)], ["b"])

    def test_dedupe_by_arxiv_id(self) -> None:
        papers = [
            Paper(paper_id="1", title="A", arxiv_id="2601.00001"),
            Paper(paper_id="2", title="A copy", arxiv_id="2601.00001", abstract="copy"),
        ]
        self.assertEqual(len(dedupe_papers(papers)), 1)

    def test_dedupe_by_normalized_title_across_sources(self) -> None:
        papers = [
            Paper(paper_id="arxiv:1", title="Adaptive Dual-Path Framework for Covert Semantic Communication"),
            Paper(
                paper_id="openalex:1",
                title="Adaptive Dual Path Framework for Covert Semantic Communication",
                doi="10.1234/example",
            ),
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

    def test_classify_semantic_physical_layer(self) -> None:
        paper = Paper(
            paper_id="p",
            title="Semantic-Aware NOMA for Pinching-Antenna Systems",
            abstract="A waveguide and semantic spectral efficiency method for pinching antennas.",
        )
        classify_paper(paper, DEFAULT_CLASSIFICATION_RULES)
        self.assertEqual(paper.technical_framework, "Semantic-Aware Physical Layer")

    def test_classify_optimization_framework(self) -> None:
        paper = Paper(
            paper_id="p",
            title="UAV-Enabled Semantic Communications via Genetic Algorithm",
            abstract="Joint optimization of hovering position and resource allocation.",
        )
        classify_paper(paper, DEFAULT_CLASSIFICATION_RULES)
        self.assertEqual(paper.technical_framework, "Optimization / Resource Allocation")

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

    def test_score_relevance_rejects_non_core_semantic_usage(self) -> None:
        paper = Paper(
            paper_id="p",
            title="Semantic segmentation for urban vegetation monitoring",
            abstract="A semantic change detection dataset with communication between modules.",
        )
        score_relevance(paper, ["semantic communication"], [])
        self.assertEqual(paper.relevance_score, 0.0)
        self.assertEqual(paper.curation_status, "candidate")
        self.assertFalse(has_core_semantic_signal(f"{paper.title} {paper.abstract}"))

    def test_weekly_exports_only_curated_papers(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            inbox = root / "data" / "inbox" / "daily_inbox_20260515.json"
            papers = [
                Paper(
                    paper_id="good",
                    title="Semantic Communication for Wireless Networks",
                    year=2026,
                    abstract="Semantic communication improves wireless transmission.",
                ),
                Paper(
                    paper_id="bad",
                    title="Semantic segmentation with open source code",
                    year=2026,
                    abstract="Code is available at https://github.com/example/not-semcom.",
                ),
            ]
            save_json(inbox, papers)
            result = run_weekly_curated(root)
            self.assertEqual(result["count"], 1)

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
        with zipfile.ZipFile(word_path) as docx:
            document_xml = docx.read("word/document.xml").decode("utf-8")
        self.assertIn("逐篇明细", document_xml)
        self.assertGreaterEqual(document_xml.count("<w:tbl>"), 3)


if __name__ == "__main__":
    unittest.main()
