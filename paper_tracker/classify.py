from __future__ import annotations

import re
from collections.abc import Mapping

from .schema import Paper


def classify_paper(paper: Paper, rules: Mapping[str, Mapping[str, list[str]]]) -> Paper:
    text = f"{paper.title} {paper.abstract}".lower()
    paper.application_scenario = best_label(text, rules.get("application_scenarios", {}))
    paper.technical_framework = best_label(text, rules.get("technical_frameworks", {}))
    paper.task_type = infer_task_type(text)
    paper.modality = infer_modality(paper.application_scenario, text)
    return paper


def best_label(text: str, label_rules: Mapping[str, list[str]]) -> str:
    best = ("未分类", 0)
    for label, keywords in label_rules.items():
        score = sum(keyword_score(text, keyword) for keyword in keywords)
        if score > best[1]:
            best = (label, score)
    return best[0]


def keyword_score(text: str, keyword: str) -> int:
    keyword = keyword.lower().strip()
    if not keyword:
        return 0
    if re.fullmatch(r"[a-z0-9]+", keyword):
        return 1 if re.search(rf"\b{re.escape(keyword)}\b", text) else 0
    return 1 if keyword in text else 0


def infer_task_type(text: str) -> str:
    if "survey" in text or "review" in text or "tutorial" in text:
        return "综述"
    if "classification" in text or "recognition" in text:
        return "分类/识别"
    if "generation" in text or "synthesis" in text:
        return "生成"
    if "transmission" in text or "communication" in text:
        return "传输"
    return "未标注"


def infer_modality(application_scenario: str, text: str) -> str:
    if "文本" in application_scenario:
        return "Text"
    if "图像" in application_scenario:
        return "Image"
    if "语音" in application_scenario:
        return "Speech"
    if "视频" in application_scenario:
        return "Video"
    if "多模态" in application_scenario:
        return "Multimodal"
    match = re.search(r"\b(text|image|speech|audio|video|multimodal)\b", text)
    return match.group(1).title() if match else "未标注"
