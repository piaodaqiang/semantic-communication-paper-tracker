from __future__ import annotations

from pathlib import Path
from typing import Any


DEFAULT_KEYWORDS = {
    "primary_keywords": [
        "semantic communication",
        "semantic communications",
        "task-oriented communication",
        "goal-oriented communication",
        "DeepSC",
        "semantic-aware communication",
        "semantic transmission",
        "semantic encoding",
        "semantic channel coding",
    ],
    "negative_keywords": ["lexical semantics", "semantic web", "semantic segmentation"],
}

DEFAULT_SOURCES = {
    "arxiv": {
        "enabled": True,
        "base_url": "https://export.arxiv.org/api/query",
        "max_results_per_keyword": 50,
        "request_timeout_seconds": 10,
    }
}

DEFAULT_CLASSIFICATION_RULES = {
    "application_scenarios": {
        "文本语义通信": ["text", "sentence", "language", "natural language", "machine translation", "deepsc"],
        "图像语义通信": ["image", "visual", "picture", "computer vision", "deepjscc"],
        "语音语义通信": ["speech", "audio", "voice", "spoken"],
        "视频语义通信": ["video", "streaming"],
        "多模态语义通信": ["multimodal", "multi-modal", "vision-language"],
        "任务导向通信": ["task-oriented", "goal-oriented", "task oriented", "goal oriented"],
        "6G / 无线通信": ["6g", "wireless", "channel", "fading", "mimo"],
        "IoT / 边缘智能": ["iot", "internet of things", "edge", "edge intelligence"],
        "车联网 / UAV / 工业互联网": ["vehicular", "vehicle", "uav", "drone", "industrial internet"],
        "LLM / Agent 辅助语义通信": ["large language model", "llm", "agent", "multi-agent", "foundation model"],
        "综述类论文": ["survey", "tutorial", "overview", "review"],
        "理论与信息论基础": ["information theory", "rate-distortion", "semantic entropy", "semantic information"],
    },
    "technical_frameworks": {
        "Autoencoder / DeepSC": ["autoencoder", "encoder-decoder", "deepsc"],
        "Transformer": ["transformer", "attention", "bert"],
        "CNN / DeepJSCC": ["cnn", "convolution", "deepjscc", "joint source-channel coding"],
        "RNN / Seq2Seq": ["rnn", "lstm", "gru", "seq2seq"],
        "Reinforcement Learning": ["reinforcement learning", "rl", "markov decision"],
        "Knowledge Graph": ["knowledge graph", "ontology"],
        "Diffusion Model": ["diffusion", "score-based"],
        "Foundation Model / LLM": ["foundation model", "large language model", "llm", "gpt"],
        "Multi-Agent": ["multi-agent", "agent"],
        "Hybrid Classical + Neural Coding": ["hybrid", "classical", "channel coding", "source coding"],
    },
}


def load_yaml(path: Path, fallback: dict[str, Any]) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        return fallback
    if not path.exists():
        return fallback
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data


def load_keywords(root: Path) -> dict[str, Any]:
    return load_yaml(root / "configs" / "keywords.yaml", DEFAULT_KEYWORDS)


def load_sources(root: Path) -> dict[str, Any]:
    return load_yaml(root / "configs" / "sources.yaml", DEFAULT_SOURCES)


def load_classification_rules(root: Path) -> dict[str, Any]:
    return load_yaml(root / "configs" / "classification_rules.yaml", DEFAULT_CLASSIFICATION_RULES)
