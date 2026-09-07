# 语义通信论文周报 2026-W37

论文总数：26
已确认开源论文数：4
待人工复核候选数：0
自动未发现代码数：22
年份分布：2026 21；2025 5
场景分布：文本语义通信 8；6G / 无线通信 6；图像语义通信 5；多模态语义通信 2；IoT / 边缘智能 1；未分类 1；车联网 / UAV / 工业互联网 1；视频语义通信 1；LLM / Agent 辅助语义通信 1
技术框架分布：Autoencoder / DeepSC 5；Transformer 4；CNN / DeepJSCC 4；Hybrid Classical + Neural Coding 3；Optimization / Resource Allocation 3；未分类 3；Multi-Agent 3；Foundation Model / LLM 1

## 建议精读论文
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- Semantic Communications in the THz Band (2026) | 6G / 无线通信 | Autoencoder / DeepSC | not_detected
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | 6G / 无线通信 | Hybrid Classical + Neural Coding | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC
- Closing the Semantic-Edge Gap: Tiny Language Models for 6G Wireless Intelligence (2026) | 6G / 无线通信 | Hybrid Classical + Neural Coding | not_detected
- Resource-efficient Semantic Coding Schemes with Manifold-constrained Hyper-connections (2026) | 6G / 无线通信 | Optimization / Resource Allocation | not_detected
- Privacy Preserving Semantic Communications in Wireless Edge Networks with Vision Language Models (2026) | 多模态语义通信 | 未分类 | not_detected
- VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission (2025) | 文本语义通信 | Autoencoder / DeepSC | detected: https://github.com/Molkaat/semantic-communication-refs
- LLM-Enabled Data Transmission in End-to-End Semantic Communication (2025) | 文本语义通信 | Foundation Model / LLM | not_detected
- Semantic-Aware Sub-Band Allocation for Terahertz Communications (2026) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- SignDeepSC: A Semantic Signature-based Approach for Robust Semantic Communication (2026) | 文本语义通信 | Transformer | not_detected

## 开源复核清单

说明：not_detected 只表示自动流程未发现明确代码链接，不等于论文一定未开源。

### 已确认开源
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC | evidence=pdf_link_extract
- VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission (2025) | https://github.com/Molkaat/semantic-communication-refs | evidence=github_search
- Air-Ground Collaborative Vision-and-Language Navigation via Shared Bird's-Eye Maps (2026) | https://github.com/ZSN2024/AGC-VLN | evidence=metadata
- Prediction-Aware Semantic Communication for Edge Video Digital Twins: derived results and analysis code (2026) | https://github.com/Davelias/viot-paper-data | evidence=pdf_link_extract

### 需要人工复核
- 本次没有需要人工复核的候选链接。

### 自动未发现
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | evidence=source_error:papers_with_code
- Semantic Communications in the THz Band (2026) | evidence=source_error:papers_with_code
- Closing the Semantic-Edge Gap: Tiny Language Models for 6G Wireless Intelligence (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Resource-efficient Semantic Coding Schemes with Manifold-constrained Hyper-connections (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Privacy Preserving Semantic Communications in Wireless Edge Networks with Vision Language Models (2026) | evidence=source_error:papers_with_code;source_error:github_search
- LLM-Enabled Data Transmission in End-to-End Semantic Communication (2025) | evidence=source_error:papers_with_code
- Semantic-Aware Sub-Band Allocation for Terahertz Communications (2026) | evidence=source_error:papers_with_code
- SignDeepSC: A Semantic Signature-based Approach for Robust Semantic Communication (2026) | evidence=source_error:papers_with_code
- A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks (2025) | evidence=source_error:papers_with_code;source_error:github_search
- Rethinking Communication Metrics: How Should We Measure Meaning? (2026) | evidence=source_error:papers_with_code
- FlowSem: Flow Matching for Adaptive Wireless Image Transmission in Semantic Communication (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Differential Privacy in Feature Reconstruction Aided Federated Learning for Agent's Semantic Communication Model Update (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Token-Oriented Semantic Communication with Pretrained Vision Transformers (2026) | evidence=source_error:papers_with_code
- Ada-TokenCom: Rate-Adaptive Token Communications via Large-Model-Driven Token Compression and Generation (2026) | evidence=source_error:papers_with_code
- Document-Level Transformer-Based Text Semantic Communication System (2026) | evidence=source_error:papers_with_code;source_error:github_search;source_error:pdf_link_extract
- Adaptive federated edge intelligence with semantic communication and trust-aware optimization for heterogeneous IoT networks (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Knowledge Distillation Driven Semantic NOMA with GAN Refinement for 6G Robotic Vehicle Networks (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Cooperative Multi-Task Semantic Communication for Joint Classification and Regression Tasks (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Generalized Query-Oriented Image Semantic Coding Empowered by Large AI Models and Semantic-Aware Hybrid Beamforming (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Heterogeneity-Aware Belief Synchronization for Semantic Communication in AI-Native 6G Networks (2026) | evidence=source_error:papers_with_code;source_error:github_search
- GAN-Based Semantic Communication for Image Transmission in IoV (2026) | evidence=source_error:papers_with_code;source_error:github_search
- A Semantic-Aware Multiple Access Scheme Leveraging Spatial Redundancy for Uplink-Dominant Network Services (2026) | evidence=source_error:papers_with_code;source_error:github_search

## 逐篇简表
| 序号 | 题名 | 年份 | 场景 | 技术框架 | 相关性 | 开源状态 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications | 2025 | 文本语义通信 | Autoencoder / DeepSC | 11.5 | not_detected |
| 2 | Semantic Communications in the THz Band | 2026 | 6G / 无线通信 | Autoencoder / DeepSC | 11.0 | not_detected |
| 3 | Image Semantic Communication with Quadtree Partition-based Coding | 2025 | 6G / 无线通信 | Hybrid Classical + Neural Coding | 10.5 | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC |
| 4 | Closing the Semantic-Edge Gap: Tiny Language Models for 6G Wireless Intelligence | 2026 | 6G / 无线通信 | Hybrid Classical + Neural Coding | 10.0 | not_detected |
| 5 | Resource-efficient Semantic Coding Schemes with Manifold-constrained Hyper-connections | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | not_detected |
| 6 | Privacy Preserving Semantic Communications in Wireless Edge Networks with Vision Language Models | 2026 | 多模态语义通信 | 未分类 | 9.5 | not_detected |
| 7 | VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission | 2025 | 文本语义通信 | Autoencoder / DeepSC | 9.0 | detected: https://github.com/Molkaat/semantic-communication-refs |
| 8 | LLM-Enabled Data Transmission in End-to-End Semantic Communication | 2025 | 文本语义通信 | Foundation Model / LLM | 9.0 | not_detected |
| 9 | Semantic-Aware Sub-Band Allocation for Terahertz Communications | 2026 | 文本语义通信 | Autoencoder / DeepSC | 8.5 | not_detected |
| 10 | SignDeepSC: A Semantic Signature-based Approach for Robust Semantic Communication | 2026 | 文本语义通信 | Transformer | 8.5 | not_detected |
| 11 | A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks | 2025 | 文本语义通信 | Autoencoder / DeepSC | 8.5 | not_detected |
| 12 | Rethinking Communication Metrics: How Should We Measure Meaning? | 2026 | 文本语义通信 | Optimization / Resource Allocation | 7.5 | not_detected |
| 13 | FlowSem: Flow Matching for Adaptive Wireless Image Transmission in Semantic Communication | 2026 | 图像语义通信 | CNN / DeepJSCC | 7.5 | not_detected |
| 14 | Differential Privacy in Feature Reconstruction Aided Federated Learning for Agent's Semantic Communication Model Update | 2026 | 6G / 无线通信 | CNN / DeepJSCC | 7.5 | not_detected |
| 15 | Token-Oriented Semantic Communication with Pretrained Vision Transformers | 2026 | 图像语义通信 | Transformer | 7.0 | not_detected |
| 16 | Ada-TokenCom: Rate-Adaptive Token Communications via Large-Model-Driven Token Compression and Generation | 2026 | 多模态语义通信 | CNN / DeepJSCC | 7.0 | not_detected |
| 17 | Document-Level Transformer-Based Text Semantic Communication System | 2026 | 文本语义通信 | Transformer | 7.0 | not_detected |
| 18 | Adaptive federated edge intelligence with semantic communication and trust-aware optimization for heterogeneous IoT networks | 2026 | IoT / 边缘智能 | Optimization / Resource Allocation | 7.0 | not_detected |
| 19 | Knowledge Distillation Driven Semantic NOMA with GAN Refinement for 6G Robotic Vehicle Networks | 2026 | 图像语义通信 | CNN / DeepJSCC | 7.0 | not_detected |
| 20 | Cooperative Multi-Task Semantic Communication for Joint Classification and Regression Tasks | 2026 | 未分类 | 未分类 | 7.0 | not_detected |
| 21 | Air-Ground Collaborative Vision-and-Language Navigation via Shared Bird's-Eye Maps | 2026 | 车联网 / UAV / 工业互联网 | Multi-Agent | 7.0 | detected: https://github.com/ZSN2024/AGC-VLN |
| 22 | Generalized Query-Oriented Image Semantic Coding Empowered by Large AI Models and Semantic-Aware Hybrid Beamforming | 2026 | 图像语义通信 | Hybrid Classical + Neural Coding | 6.5 | not_detected |
| 23 | Prediction-Aware Semantic Communication for Edge Video Digital Twins: derived results and analysis code | 2026 | 视频语义通信 | 未分类 | 6.5 | detected: https://github.com/Davelias/viot-paper-data |
| 24 | Heterogeneity-Aware Belief Synchronization for Semantic Communication in AI-Native 6G Networks | 2026 | 6G / 无线通信 | Multi-Agent | 6.0 | not_detected |
| 25 | GAN-Based Semantic Communication for Image Transmission in IoV | 2026 | 图像语义通信 | Transformer | 5.0 | not_detected |
| 26 | A Semantic-Aware Multiple Access Scheme Leveraging Spatial Redundancy for Uplink-Dominant Network Services | 2026 | LLM / Agent 辅助语义通信 | Multi-Agent | 3.5 | not_detected |
