# 语义通信论文周报 2026-W29

论文总数：28
已确认开源论文数：6
待人工复核候选数：1
自动未发现代码数：21
年份分布：2026 18；2025 6；2024 4
场景分布：6G / 无线通信 14；文本语义通信 10；车联网 / UAV / 工业互联网 2；IoT / 边缘智能 1；图像语义通信 1
技术框架分布：Optimization / Resource Allocation 8；Autoencoder / DeepSC 7；Foundation Model / LLM 4；未分类 3；CNN / DeepJSCC 3；Hybrid Classical + Neural Coding 1；Reinforcement Learning 1；Transformer 1

## 建议精读论文
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing (2024) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- Semantic Communications in the THz Band (2026) | 6G / 无线通信 | Autoencoder / DeepSC | not_detected
- Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks (2025) | 文本语义通信 | Optimization / Resource Allocation | not_detected
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | 6G / 无线通信 | Hybrid Classical + Neural Coding | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC
- Semantic-Aware Multiple Access via Spatial Redundancy Exploitation for Uplink-Dominant 6G Use Cases (2026) | 6G / 无线通信 | 未分类 | not_detected
- Large-Language-Model Enabled Semantic Communication Systems (2024) | 文本语义通信 | Foundation Model / LLM | detected: https://github.com/gujianhunwang/LLM_com
- World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems (2026) | 车联网 / UAV / 工业互联网 | Reinforcement Learning | not_detected
- Hybrid Bit and Semantic Communications for UAV-Enabled Wireless Power Transfer Networks: A Decision-Assisted Deep Reinforcement Learning Approach (2026) | 6G / 无线通信 | Optimization / Resource Allocation | not_detected
- Minimizing Quantized Semantic Age of Information (QSAoI) in Foundation Model-Based Semantic Communications (2026) | 6G / 无线通信 | Optimization / Resource Allocation | not_detected

## 开源复核清单

说明：not_detected 只表示自动流程未发现明确代码链接，不等于论文一定未开源。

### 已确认开源
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC | evidence=pdf_link_extract
- Large-Language-Model Enabled Semantic Communication Systems (2024) | https://github.com/gujianhunwang/LLM_com | evidence=pdf_link_extract
- Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning (2024) | https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning | evidence=arxiv_comment
- VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission (2025) | https://github.com/Molkaat/semantic-communication-refs | evidence=github_search
- Towards a Joint Task-Oriented and Generative Semantic Communication Framework for 6G Networks (2026) | https://github.com/philpolo/rsgen | evidence=pdf_link_extract
- Equivariant Semantic Communication for Telecom: An Open Research Project (2026) | https://github.com/zenodo/zenodo-rdm | evidence=pdf_link_extract

### 需要人工复核
- Generative Semantic Communications for Multimodal Data: Metric Design and Robust Resource Allocation via Bayes-Jackknife GRPO (2026) | candidates=https://code.jquery.com/jquery-1.12.4.min.js | evidence=author_project_page

### 自动未发现
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | evidence=source_error:papers_with_code
- Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing (2024) | evidence=source_error:papers_with_code;source_error:github_search
- Semantic Communications in the THz Band (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks (2025) | evidence=source_error:papers_with_code;source_error:github_search
- Semantic-Aware Multiple Access via Spatial Redundancy Exploitation for Uplink-Dominant 6G Use Cases (2026) | evidence=source_error:papers_with_code;source_error:github_search
- World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems (2026) | evidence=source_error:papers_with_code
- Hybrid Bit and Semantic Communications for UAV-Enabled Wireless Power Transfer Networks: A Decision-Assisted Deep Reinforcement Learning Approach (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Minimizing Quantized Semantic Age of Information (QSAoI) in Foundation Model-Based Semantic Communications (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Wireless Backdoor Attack and Defense for Semantic Communications over Multiple Access Channel (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Semantic Leakage and Privacy Preservation in Relay-Assisted Semantic Communications (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Semantic Video Communication via Multi-Scale Convolution and Dynamic Routing for Next-Generation Networks (2026) | evidence=source_error:papers_with_code
- ATS-ToDMA: Adaptive Token Selection and Token-Domain Multiple Access for Cross-Modal Semantic Communications (2026) | evidence=source_error:papers_with_code
- LLM-Enabled Data Transmission in End-to-End Semantic Communication (2025) | evidence=source_error:papers_with_code
- SAFE: Semantic Adaptive Feature Extraction with Rate Control for 6G Wireless Communications (2024) | evidence=source_error:papers_with_code;source_error:github_search
- A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks (2025) | evidence=source_error:papers_with_code
- Bridging the Semantic Gap in 6G: Tiny Language Models Under the Latency-Accuracy-Size Trilemma (2026) | evidence=source_error:papers_with_code
- A Comprehensive Survey on Semantic Communication in Non-Terrestrial Networks: Architectures, Methodologies, and Challenges (2026) | evidence=source_error:papers_with_code;source_error:github_search
- TONIC: Token-Centric Semantic Communication for Task-Oriented Wireless Systems (2026) | evidence=source_error:papers_with_code;source_error:github_search
- QwenMoE-SC: A Mixture-of-Expert Semantic Communication Model with GNN-Based Unequal Error Protection, NEFTune Technique and Direct Preference Optimization (2026) | evidence=source_error:papers_with_code;source_error:github_search;source_error:pdf_link_extract
- Rate-Splitting Multiple Access Enabled Probabilistic Semantic Communication in UAV Networks (2026) | evidence=source_error:papers_with_code;source_error:github_search
- -8 dB SNR + 90% Packet Loss: MamVSC -- CSI-Guided Semantic Mamba for Extreme-Robust Video Semantic Communication (2026) | evidence=source_error:papers_with_code;source_error:github_search

## 逐篇简表
| 序号 | 题名 | 年份 | 场景 | 技术框架 | 相关性 | 开源状态 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications | 2025 | 文本语义通信 | Autoencoder / DeepSC | 11.5 | not_detected |
| 2 | Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing | 2024 | 文本语义通信 | Autoencoder / DeepSC | 11.5 | not_detected |
| 3 | Semantic Communications in the THz Band | 2026 | 6G / 无线通信 | Autoencoder / DeepSC | 11.0 | not_detected |
| 4 | Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks | 2025 | 文本语义通信 | Optimization / Resource Allocation | 11.0 | not_detected |
| 5 | Image Semantic Communication with Quadtree Partition-based Coding | 2025 | 6G / 无线通信 | Hybrid Classical + Neural Coding | 10.5 | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC |
| 6 | Semantic-Aware Multiple Access via Spatial Redundancy Exploitation for Uplink-Dominant 6G Use Cases | 2026 | 6G / 无线通信 | 未分类 | 10.0 | not_detected |
| 7 | Large-Language-Model Enabled Semantic Communication Systems | 2024 | 文本语义通信 | Foundation Model / LLM | 10.0 | detected: https://github.com/gujianhunwang/LLM_com |
| 8 | World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems | 2026 | 车联网 / UAV / 工业互联网 | Reinforcement Learning | 9.5 | not_detected |
| 9 | Hybrid Bit and Semantic Communications for UAV-Enabled Wireless Power Transfer Networks: A Decision-Assisted Deep Reinforcement Learning Approach | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | not_detected |
| 10 | Minimizing Quantized Semantic Age of Information (QSAoI) in Foundation Model-Based Semantic Communications | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | not_detected |
| 11 | Wireless Backdoor Attack and Defense for Semantic Communications over Multiple Access Channel | 2026 | 6G / 无线通信 | 未分类 | 9.5 | not_detected |
| 12 | Semantic Leakage and Privacy Preservation in Relay-Assisted Semantic Communications | 2026 | 6G / 无线通信 | 未分类 | 9.5 | not_detected |
| 13 | Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning | 2024 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | detected: https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning |
| 14 | Semantic Video Communication via Multi-Scale Convolution and Dynamic Routing for Next-Generation Networks | 2026 | 文本语义通信 | CNN / DeepJSCC | 9.0 | not_detected |
| 15 | ATS-ToDMA: Adaptive Token Selection and Token-Domain Multiple Access for Cross-Modal Semantic Communications | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 9.0 | not_detected |
| 16 | Generative Semantic Communications for Multimodal Data: Metric Design and Robust Resource Allocation via Bayes-Jackknife GRPO | 2026 | IoT / 边缘智能 | Optimization / Resource Allocation | 9.0 | needs_review: https://code.jquery.com/jquery-1.12.4.min.js |
| 17 | VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission | 2025 | 文本语义通信 | Autoencoder / DeepSC | 9.0 | detected: https://github.com/Molkaat/semantic-communication-refs |
| 18 | LLM-Enabled Data Transmission in End-to-End Semantic Communication | 2025 | 文本语义通信 | Foundation Model / LLM | 9.0 | not_detected |
| 19 | SAFE: Semantic Adaptive Feature Extraction with Rate Control for 6G Wireless Communications | 2024 | 6G / 无线通信 | Autoencoder / DeepSC | 9.0 | not_detected |
| 20 | Towards a Joint Task-Oriented and Generative Semantic Communication Framework for 6G Networks | 2026 | 6G / 无线通信 | Autoencoder / DeepSC | 8.5 | detected: https://github.com/philpolo/rsgen |
| 21 | A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks | 2025 | 文本语义通信 | Autoencoder / DeepSC | 8.5 | not_detected |
| 22 | Bridging the Semantic Gap in 6G: Tiny Language Models Under the Latency-Accuracy-Size Trilemma | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 8.0 | not_detected |
| 23 | A Comprehensive Survey on Semantic Communication in Non-Terrestrial Networks: Architectures, Methodologies, and Challenges | 2026 | 6G / 无线通信 | CNN / DeepJSCC | 7.5 | not_detected |
| 24 | TONIC: Token-Centric Semantic Communication for Task-Oriented Wireless Systems | 2026 | 图像语义通信 | Transformer | 7.5 | not_detected |
| 25 | QwenMoE-SC: A Mixture-of-Expert Semantic Communication Model with GNN-Based Unequal Error Protection, NEFTune Technique and Direct Preference Optimization | 2026 | 文本语义通信 | Foundation Model / LLM | 7.0 | not_detected |
| 26 | Rate-Splitting Multiple Access Enabled Probabilistic Semantic Communication in UAV Networks | 2026 | 车联网 / UAV / 工业互联网 | Optimization / Resource Allocation | 7.0 | not_detected |
| 27 | -8 dB SNR + 90% Packet Loss: MamVSC -- CSI-Guided Semantic Mamba for Extreme-Robust Video Semantic Communication | 2026 | 6G / 无线通信 | CNN / DeepJSCC | 7.0 | not_detected |
| 28 | Equivariant Semantic Communication for Telecom: An Open Research Project | 2026 | 文本语义通信 | Foundation Model / LLM | 7.0 | detected: https://github.com/zenodo/zenodo-rdm |
