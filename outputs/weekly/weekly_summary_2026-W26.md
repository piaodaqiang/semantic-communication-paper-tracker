# 语义通信论文周报 2026-W26

论文总数：28
已确认开源论文数：4
待人工复核候选数：1
自动未发现代码数：23
年份分布：2026 18；2025 6；2024 4
场景分布：6G / 无线通信 11；文本语义通信 7；图像语义通信 4；任务导向通信 2；车联网 / UAV / 工业互联网 1；视频语义通信 1；LLM / Agent 辅助语义通信 1；理论与信息论基础 1
技术框架分布：Autoencoder / DeepSC 5；CNN / DeepJSCC 5；Optimization / Resource Allocation 4；未分类 3；Hybrid Classical + Neural Coding 2；Foundation Model / LLM 2；Semantic-Aware Physical Layer 2；Transformer 2；Reinforcement Learning 1；Multi-Agent 1；Information Theory / Semantic Coding 1

## 建议精读论文
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing (2024) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks (2025) | 文本语义通信 | Optimization / Resource Allocation | not_detected
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | 6G / 无线通信 | Hybrid Classical + Neural Coding | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC
- Large-Language-Model Enabled Semantic Communication Systems (2024) | 文本语义通信 | Foundation Model / LLM | detected: https://github.com/gujianhunwang/LLM_com
- Game-Theoretic Latent Space Alignment for Multi-user Semantic MIMO Communications (2026) | 6G / 无线通信 | Optimization / Resource Allocation | needs_review: https://pypi.org/project/timm/
- World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems (2026) | 车联网 / UAV / 工业互联网 | Reinforcement Learning | not_detected
- Not All Symbols Are Equal: Importance-Aware Constellation Design for Semantic Communication (2026) | 任务导向通信 | Semantic-Aware Physical Layer | not_detected
- Hybrid Bit and Semantic Communications for UAV-Enabled Wireless Power Transfer Networks: A Decision-Assisted Deep Reinforcement Learning Approach (2026) | 6G / 无线通信 | Optimization / Resource Allocation | not_detected
- LGVSC: A Large-Model-Driven Generative Video Semantic Communication Framework (2026) | 视频语义通信 | 未分类 | not_detected

## 开源复核清单

说明：not_detected 只表示自动流程未发现明确代码链接，不等于论文一定未开源。

### 已确认开源
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC | evidence=pdf_link_extract
- Large-Language-Model Enabled Semantic Communication Systems (2024) | https://github.com/gujianhunwang/LLM_com | evidence=pdf_link_extract
- Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning (2024) | https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning | evidence=arxiv_comment
- VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission (2025) | https://github.com/Molkaat/semantic-communication-refs | evidence=github_search

### 需要人工复核
- Game-Theoretic Latent Space Alignment for Multi-user Semantic MIMO Communications (2026) | candidates=https://pypi.org/project/timm/ | evidence=pdf_link_extract

### 自动未发现
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | evidence=source_error:papers_with_code
- Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing (2024) | evidence=source_error:papers_with_code;source_error:github_search
- Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks (2025) | evidence=source_error:papers_with_code;source_error:github_search
- World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems (2026) | evidence=source_error:papers_with_code
- Not All Symbols Are Equal: Importance-Aware Constellation Design for Semantic Communication (2026) | evidence=source_error:papers_with_code
- Hybrid Bit and Semantic Communications for UAV-Enabled Wireless Power Transfer Networks: A Decision-Assisted Deep Reinforcement Learning Approach (2026) | evidence=source_error:papers_with_code;source_error:github_search
- LGVSC: A Large-Model-Driven Generative Video Semantic Communication Framework (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Adapting Diffusion Language Models for Lossless Pixel-Level Image Transmission (2026) | evidence=source_error:papers_with_code;source_error:github_search
- STCC: A Unified Source-Channel Semantic Token Coding Framework for Semantic Communications (2026) | evidence=source_error:papers_with_code;source_error:github_search
- SA-RA-JSCC: SNR-Adaptive and Semantic-Rate-Aware Joint Source-Channel Coding (2026) | evidence=source_error:papers_with_code;source_error:github_search
- LLM-Enabled Data Transmission in End-to-End Semantic Communication (2025) | evidence=source_error:papers_with_code
- SAFE: Semantic Adaptive Feature Extraction with Rate Control for 6G Wireless Communications (2024) | evidence=source_error:papers_with_code;source_error:github_search
- Designed-Source Reductions and a Dual-Purpose Feasibility Band for Semantic Rate-Distortion (2026) | evidence=source_error:papers_with_code
- A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks (2025) | evidence=source_error:papers_with_code;source_error:github_search
- Toward Reliable Semantic Communication: Beyond Average Performance (2026) | evidence=source_error:papers_with_code;source_error:github_search
- A Comprehensive Survey on Semantic Communication in Non-Terrestrial Networks: Architectures, Methodologies, and Challenges (2026) | evidence=source_error:papers_with_code;source_error:github_search
- TONIC: Token-Centric Semantic Communication for Task-Oriented Wireless Systems (2026) | evidence=source_error:papers_with_code;source_error:github_search
- ChronoSC: Task-Oriented Semantic Communication via Temporal-to-Color Encoding (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Research on Multi-Agent Semantic Communication Framework Based on Comparative Learning Joint Optimization (2026) | evidence=source_error:papers_with_code;source_error:github_search;source_error:pdf_link_extract
- Goal-Oriented Semantic Communication for Logical Decision Making (2026) | evidence=source_error:papers_with_code
- Spacing-Based Coupling Radiation Control in Pinching-Antennas Systems for Heterogeneous NOMA Users (2026) | evidence=source_error:papers_with_code;source_error:github_search
- GenED-SC: Generative Editing Semantic Communication with Integrated Multi-Modal LLMs (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Implicit Semantic-Aware Communication Based on Hypergraph Reasoning (2026) | evidence=source_error:papers_with_code;source_error:github_search

## 逐篇简表
| 序号 | 题名 | 年份 | 场景 | 技术框架 | 相关性 | 开源状态 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications | 2025 | 文本语义通信 | Autoencoder / DeepSC | 11.5 | not_detected |
| 2 | Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing | 2024 | 文本语义通信 | Autoencoder / DeepSC | 11.5 | not_detected |
| 3 | Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks | 2025 | 文本语义通信 | Optimization / Resource Allocation | 11.0 | not_detected |
| 4 | Image Semantic Communication with Quadtree Partition-based Coding | 2025 | 6G / 无线通信 | Hybrid Classical + Neural Coding | 10.5 | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC |
| 5 | Large-Language-Model Enabled Semantic Communication Systems | 2024 | 文本语义通信 | Foundation Model / LLM | 10.0 | detected: https://github.com/gujianhunwang/LLM_com |
| 6 | Game-Theoretic Latent Space Alignment for Multi-user Semantic MIMO Communications | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | needs_review: https://pypi.org/project/timm/ |
| 7 | World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems | 2026 | 车联网 / UAV / 工业互联网 | Reinforcement Learning | 9.5 | not_detected |
| 8 | Not All Symbols Are Equal: Importance-Aware Constellation Design for Semantic Communication | 2026 | 任务导向通信 | Semantic-Aware Physical Layer | 9.5 | not_detected |
| 9 | Hybrid Bit and Semantic Communications for UAV-Enabled Wireless Power Transfer Networks: A Decision-Assisted Deep Reinforcement Learning Approach | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | not_detected |
| 10 | LGVSC: A Large-Model-Driven Generative Video Semantic Communication Framework | 2026 | 视频语义通信 | 未分类 | 9.5 | not_detected |
| 11 | Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning | 2024 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | detected: https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning |
| 12 | Adapting Diffusion Language Models for Lossless Pixel-Level Image Transmission | 2026 | 6G / 无线通信 | Transformer | 9.0 | not_detected |
| 13 | STCC: A Unified Source-Channel Semantic Token Coding Framework for Semantic Communications | 2026 | 6G / 无线通信 | CNN / DeepJSCC | 9.0 | not_detected |
| 14 | SA-RA-JSCC: SNR-Adaptive and Semantic-Rate-Aware Joint Source-Channel Coding | 2026 | 图像语义通信 | CNN / DeepJSCC | 9.0 | not_detected |
| 15 | VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission | 2025 | 文本语义通信 | Autoencoder / DeepSC | 9.0 | detected: https://github.com/Molkaat/semantic-communication-refs |
| 16 | LLM-Enabled Data Transmission in End-to-End Semantic Communication | 2025 | 文本语义通信 | Foundation Model / LLM | 9.0 | not_detected |
| 17 | SAFE: Semantic Adaptive Feature Extraction with Rate Control for 6G Wireless Communications | 2024 | 6G / 无线通信 | Autoencoder / DeepSC | 9.0 | not_detected |
| 18 | Designed-Source Reductions and a Dual-Purpose Feasibility Band for Semantic Rate-Distortion | 2026 | 任务导向通信 | 未分类 | 8.5 | not_detected |
| 19 | A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks | 2025 | 文本语义通信 | Autoencoder / DeepSC | 8.5 | not_detected |
| 20 | Toward Reliable Semantic Communication: Beyond Average Performance | 2026 | 6G / 无线通信 | Hybrid Classical + Neural Coding | 8.0 | not_detected |
| 21 | A Comprehensive Survey on Semantic Communication in Non-Terrestrial Networks: Architectures, Methodologies, and Challenges | 2026 | 6G / 无线通信 | CNN / DeepJSCC | 7.5 | not_detected |
| 22 | TONIC: Token-Centric Semantic Communication for Task-Oriented Wireless Systems | 2026 | 图像语义通信 | Transformer | 7.5 | not_detected |
| 23 | ChronoSC: Task-Oriented Semantic Communication via Temporal-to-Color Encoding | 2026 | 图像语义通信 | CNN / DeepJSCC | 7.5 | not_detected |
| 24 | Research on Multi-Agent Semantic Communication Framework Based on Comparative Learning Joint Optimization | 2026 | LLM / Agent 辅助语义通信 | Multi-Agent | 7.5 | not_detected |
| 25 | Goal-Oriented Semantic Communication for Logical Decision Making | 2026 | 理论与信息论基础 | 未分类 | 7.0 | not_detected |
| 26 | Spacing-Based Coupling Radiation Control in Pinching-Antennas Systems for Heterogeneous NOMA Users | 2026 | 6G / 无线通信 | Semantic-Aware Physical Layer | 7.0 | not_detected |
| 27 | GenED-SC: Generative Editing Semantic Communication with Integrated Multi-Modal LLMs | 2026 | 图像语义通信 | CNN / DeepJSCC | 7.0 | not_detected |
| 28 | Implicit Semantic-Aware Communication Based on Hypergraph Reasoning | 2026 | 6G / 无线通信 | Information Theory / Semantic Coding | 4.0 | not_detected |
