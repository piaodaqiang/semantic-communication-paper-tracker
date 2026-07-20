# 语义通信论文周报 2026-W30

论文总数：26
已确认开源论文数：4
待人工复核候选数：2
自动未发现代码数：20
年份分布：2026 17；2025 6；2024 3
场景分布：6G / 无线通信 12；文本语义通信 7；IoT / 边缘智能 2；图像语义通信 2；车联网 / UAV / 工业互联网 1；综述类论文 1；任务导向通信 1
技术框架分布：Autoencoder / DeepSC 7；Optimization / Resource Allocation 6；Hybrid Classical + Neural Coding 4；Foundation Model / LLM 3；未分类 2；CNN / DeepJSCC 2；Reinforcement Learning 1；Multi-Agent 1

## 建议精读论文
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing (2024) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- Semantic Communications in the THz Band (2026) | 6G / 无线通信 | Autoencoder / DeepSC | not_detected
- Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks (2025) | 文本语义通信 | Optimization / Resource Allocation | not_detected
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | 6G / 无线通信 | Hybrid Classical + Neural Coding | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC
- World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems (2026) | 车联网 / UAV / 工业互联网 | Reinforcement Learning | not_detected
- Hybrid Bit and Semantic Communications for UAV-Enabled Wireless Power Transfer Networks: A Decision-Assisted Deep Reinforcement Learning Approach (2026) | 6G / 无线通信 | Optimization / Resource Allocation | not_detected
- Semantic Leakage and Privacy Preservation in Relay-Assisted Semantic Communications (2026) | 6G / 无线通信 | 未分类 | not_detected
- Semantic Communication for Intelligent Transmission and Recognition of High-Resolution Satellite Images in Satellite-to-Ground Systems (2026) | 6G / 无线通信 | 未分类 | not_detected
- Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning (2024) | 6G / 无线通信 | Optimization / Resource Allocation | detected: https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning

## 开源复核清单

说明：not_detected 只表示自动流程未发现明确代码链接，不等于论文一定未开源。

### 已确认开源
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC | evidence=pdf_link_extract
- Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning (2024) | https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning | evidence=arxiv_comment
- VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission (2025) | https://github.com/Molkaat/semantic-communication-refs | evidence=github_search
- SEM-EDGE-X: INTeNT-aWaRe Semantic Edge Intelligence for Autonomous 6G Vehicular and UAV Communication Networks (2026) | https://github.com/salma-shaik-begum/SEM-EDGE-X | evidence=github_search

### 需要人工复核
- Generative Semantic Communications for Multimodal Data: Metric Design and Robust Resource Allocation via Bayes-Jackknife GRPO (2026) | candidates=https://code.jquery.com/jquery-1.12.4.min.js | evidence=author_project_page
- Large Language Model-Enhanced Multi-hop Parallel Image Semantic Communication (2026) | candidates=https://github.com/HKUDS/LightRAG | evidence=source_error:papers_with_code

### 自动未发现
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | evidence=source_error:papers_with_code
- Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing (2024) | evidence=source_error:papers_with_code
- Semantic Communications in the THz Band (2026) | evidence=source_error:papers_with_code
- Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks (2025) | evidence=source_error:papers_with_code
- World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems (2026) | evidence=source_error:papers_with_code
- Hybrid Bit and Semantic Communications for UAV-Enabled Wireless Power Transfer Networks: A Decision-Assisted Deep Reinforcement Learning Approach (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Semantic Leakage and Privacy Preservation in Relay-Assisted Semantic Communications (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Semantic Communication for Intelligent Transmission and Recognition of High-Resolution Satellite Images in Satellite-to-Ground Systems (2026) | evidence=source_error:papers_with_code;source_error:pdf_link_extract
- ATS-ToDMA: Adaptive Token Selection and Token-Domain Multiple Access for Cross-Modal Semantic Communications (2026) | evidence=source_error:papers_with_code;source_error:github_search
- LLM-Enabled Data Transmission in End-to-End Semantic Communication (2025) | evidence=source_error:papers_with_code
- SAFE: Semantic Adaptive Feature Extraction with Rate Control for 6G Wireless Communications (2024) | evidence=source_error:papers_with_code
- A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks (2025) | evidence=source_error:papers_with_code
- Bridging the Semantic Gap in 6G: Tiny Language Models Under the Latency-Accuracy-Size Trilemma (2026) | evidence=source_error:papers_with_code;source_error:github_search
- SkillComm: Skill-Driven Semantic Communication for Sequential Workflows via Incremental Token Transmission (2026) | evidence=source_error:papers_with_code
- Identification Codes and Post-Shannon Communication: Theory, Architectures, and Emerging Applications (2026) | evidence=source_error:papers_with_code
- A VAE-Driven Multi-Task Satellite-Aided Semantic Communication Framework for 6G-Enabled Connected Autonomous Vehicles (2026) | evidence=source_error:papers_with_code
- QwenMoE-SC: A Mixture-of-Expert Semantic Communication Model with GNN-Based Unequal Error Protection, NEFTune Technique and Direct Preference Optimization (2026) | evidence=source_error:papers_with_code;source_error:github_search;source_error:pdf_link_extract
- -8 dB SNR + 90% Packet Loss: MamVSC -- CSI-Guided Semantic Mamba for Extreme-Robust Video Semantic Communication (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Toward Semantic Communication for Real-time Mobile 3D Reconstruction (2026) | evidence=source_error:papers_with_code
- Goal-Oriented Semantic Communication for Distributed ISAC-Enabled Vehicle Coordination (2026) | evidence=source_error:papers_with_code

## 逐篇简表
| 序号 | 题名 | 年份 | 场景 | 技术框架 | 相关性 | 开源状态 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications | 2025 | 文本语义通信 | Autoencoder / DeepSC | 11.5 | not_detected |
| 2 | Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing | 2024 | 文本语义通信 | Autoencoder / DeepSC | 11.5 | not_detected |
| 3 | Semantic Communications in the THz Band | 2026 | 6G / 无线通信 | Autoencoder / DeepSC | 11.0 | not_detected |
| 4 | Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks | 2025 | 文本语义通信 | Optimization / Resource Allocation | 11.0 | not_detected |
| 5 | Image Semantic Communication with Quadtree Partition-based Coding | 2025 | 6G / 无线通信 | Hybrid Classical + Neural Coding | 10.5 | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC |
| 6 | World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems | 2026 | 车联网 / UAV / 工业互联网 | Reinforcement Learning | 9.5 | not_detected |
| 7 | Hybrid Bit and Semantic Communications for UAV-Enabled Wireless Power Transfer Networks: A Decision-Assisted Deep Reinforcement Learning Approach | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | not_detected |
| 8 | Semantic Leakage and Privacy Preservation in Relay-Assisted Semantic Communications | 2026 | 6G / 无线通信 | 未分类 | 9.5 | not_detected |
| 9 | Semantic Communication for Intelligent Transmission and Recognition of High-Resolution Satellite Images in Satellite-to-Ground Systems | 2026 | 6G / 无线通信 | 未分类 | 9.5 | not_detected |
| 10 | Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning | 2024 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | detected: https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning |
| 11 | Generative Semantic Communications for Multimodal Data: Metric Design and Robust Resource Allocation via Bayes-Jackknife GRPO | 2026 | IoT / 边缘智能 | Optimization / Resource Allocation | 9.0 | needs_review: https://code.jquery.com/jquery-1.12.4.min.js |
| 12 | ATS-ToDMA: Adaptive Token Selection and Token-Domain Multiple Access for Cross-Modal Semantic Communications | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 9.0 | not_detected |
| 13 | VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission | 2025 | 文本语义通信 | Autoencoder / DeepSC | 9.0 | detected: https://github.com/Molkaat/semantic-communication-refs |
| 14 | LLM-Enabled Data Transmission in End-to-End Semantic Communication | 2025 | 文本语义通信 | Foundation Model / LLM | 9.0 | not_detected |
| 15 | SAFE: Semantic Adaptive Feature Extraction with Rate Control for 6G Wireless Communications | 2024 | 6G / 无线通信 | Autoencoder / DeepSC | 9.0 | not_detected |
| 16 | SEM-EDGE-X: INTeNT-aWaRe Semantic Edge Intelligence for Autonomous 6G Vehicular and UAV Communication Networks | 2026 | IoT / 边缘智能 | Multi-Agent | 8.5 | detected: https://github.com/salma-shaik-begum/SEM-EDGE-X |
| 17 | A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks | 2025 | 文本语义通信 | Autoencoder / DeepSC | 8.5 | not_detected |
| 18 | Bridging the Semantic Gap in 6G: Tiny Language Models Under the Latency-Accuracy-Size Trilemma | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 8.0 | not_detected |
| 19 | SkillComm: Skill-Driven Semantic Communication for Sequential Workflows via Incremental Token Transmission | 2026 | 图像语义通信 | CNN / DeepJSCC | 8.0 | not_detected |
| 20 | Identification Codes and Post-Shannon Communication: Theory, Architectures, and Emerging Applications | 2026 | 综述类论文 | Hybrid Classical + Neural Coding | 8.0 | not_detected |
| 21 | A VAE-Driven Multi-Task Satellite-Aided Semantic Communication Framework for 6G-Enabled Connected Autonomous Vehicles | 2026 | 6G / 无线通信 | Autoencoder / DeepSC | 7.5 | not_detected |
| 22 | Large Language Model-Enhanced Multi-hop Parallel Image Semantic Communication | 2026 | 6G / 无线通信 | Foundation Model / LLM | 7.5 | needs_review: https://github.com/HKUDS/LightRAG |
| 23 | QwenMoE-SC: A Mixture-of-Expert Semantic Communication Model with GNN-Based Unequal Error Protection, NEFTune Technique and Direct Preference Optimization | 2026 | 文本语义通信 | Foundation Model / LLM | 7.0 | not_detected |
| 24 | -8 dB SNR + 90% Packet Loss: MamVSC -- CSI-Guided Semantic Mamba for Extreme-Robust Video Semantic Communication | 2026 | 6G / 无线通信 | CNN / DeepJSCC | 7.0 | not_detected |
| 25 | Toward Semantic Communication for Real-time Mobile 3D Reconstruction | 2026 | 图像语义通信 | Hybrid Classical + Neural Coding | 7.0 | not_detected |
| 26 | Goal-Oriented Semantic Communication for Distributed ISAC-Enabled Vehicle Coordination | 2026 | 任务导向通信 | Hybrid Classical + Neural Coding | 6.5 | not_detected |
