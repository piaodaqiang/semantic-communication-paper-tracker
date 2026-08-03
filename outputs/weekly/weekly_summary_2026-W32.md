# 语义通信论文周报 2026-W32

论文总数：27
已确认开源论文数：6
待人工复核候选数：1
自动未发现代码数：20
年份分布：2026 19；2025 6；2024 2
场景分布：6G / 无线通信 8；文本语义通信 7；图像语义通信 4；LLM / Agent 辅助语义通信 2；未分类 2；IoT / 边缘智能 1；语音语义通信 1；任务导向通信 1；车联网 / UAV / 工业互联网 1
技术框架分布：Autoencoder / DeepSC 5；Optimization / Resource Allocation 5；Hybrid Classical + Neural Coding 4；Diffusion Model 3；Multi-Agent 3；未分类 2；Semantic-Aware Physical Layer 1；Foundation Model / LLM 1；Transformer 1；CNN / DeepJSCC 1；Reinforcement Learning 1

## 建议精读论文
- Restoration Flow Matching-Based Channel Refinement and Equalization Correction for MIMO Semantic Communications (2026) | 6G / 无线通信 | Diffusion Model | not_detected
- Spatial Semantic Communication: When Semantic Transmission Meets Index Modulation (2026) | 6G / 无线通信 | Semantic-Aware Physical Layer | detected: https://github.com/gxh1106/SSC
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing (2024) | 文本语义通信 | Autoencoder / DeepSC | not_detected
- Semantic Communications in the THz Band (2026) | 6G / 无线通信 | Autoencoder / DeepSC | not_detected
- Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks (2025) | 文本语义通信 | Optimization / Resource Allocation | not_detected
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | 6G / 无线通信 | Hybrid Classical + Neural Coding | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC
- Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning (2024) | 6G / 无线通信 | Optimization / Resource Allocation | detected: https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning
- VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission (2025) | 文本语义通信 | Autoencoder / DeepSC | detected: https://github.com/Molkaat/semantic-communication-refs
- LLM-Enabled Data Transmission in End-to-End Semantic Communication (2025) | 文本语义通信 | Foundation Model / LLM | not_detected

## 开源复核清单

说明：not_detected 只表示自动流程未发现明确代码链接，不等于论文一定未开源。

### 已确认开源
- Spatial Semantic Communication: When Semantic Transmission Meets Index Modulation (2026) | https://github.com/gxh1106/SSC | evidence=metadata
- Image Semantic Communication with Quadtree Partition-based Coding (2025) | https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC | evidence=pdf_link_extract
- Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning (2024) | https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning | evidence=arxiv_comment
- VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission (2025) | https://github.com/Molkaat/semantic-communication-refs | evidence=github_search
- SEM-EDGE-X: INTeNT-aWaRe Semantic Edge Intelligence for Autonomous 6G Vehicular and UAV Communication Networks (2026) | https://github.com/salma-shaik-begum/SEM-EDGE-X | evidence=pdf_link_extract
- Dynamic Semantic Prioritisation and Real-Time Voice Reconstruction for Next-Generation VoIP over 6G Networks (2026) | https://github.com/zenodo/zenodo-rdm | evidence=pdf_link_extract

### 需要人工复核
- Wireless Intelligence Needs a Cerebellum: Score-Based Foundation Models Toward Real-Time Physical-Layer Inference (2026) | candidates=https://github.com/manjunath5496/Artificial-Intelligence | evidence=source_error:papers_with_code

### 自动未发现
- Restoration Flow Matching-Based Channel Refinement and Equalization Correction for MIMO Semantic Communications (2026) | evidence=source_error:papers_with_code
- Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications (2025) | evidence=source_error:papers_with_code
- Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing (2024) | evidence=source_error:papers_with_code;source_error:github_search
- Semantic Communications in the THz Band (2026) | evidence=source_error:papers_with_code
- Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks (2025) | evidence=source_error:papers_with_code
- LLM-Enabled Data Transmission in End-to-End Semantic Communication (2025) | evidence=source_error:papers_with_code
- SignDeepSC: A Semantic Signature-based Approach for Robust Semantic Communication (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Active Movable-Element RIS Assisted Vehicular Semantic Communications: Modeling and Optimization (2026) | evidence=source_error:papers_with_code;source_error:github_search
- When Robots Exchange Meaning: A Demo of Goal-Oriented Semantic Communications for Collaborative Robotics (2026) | evidence=source_error:papers_with_code;source_error:github_search
- A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks (2025) | evidence=source_error:papers_with_code
- SkillComm: Skill-Driven Semantic Communication for Sequential Workflows via Incremental Token Transmission (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Toward Semantic Communication for Real-time Mobile 3D Reconstruction (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Compositional Semantic Communication for Physical AI: Category Theory Meets Game Theory (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Optimization of Collaborative Semantic Communication Network Performance with Channel and Content Preference Feedback (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Low-Latency Generative Semantic Communication via Channel-Realization Flow Matching (2026) | evidence=source_error:papers_with_code;source_error:github_search
- The Price of Meaning: Quantifying Semantic Communication Overheads in Practice (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Goal-Oriented Semantic Communication for Distributed ISAC-Enabled Vehicle Coordination (2026) | evidence=source_error:papers_with_code
- Semantic-Aware Task Clustering for Constructive and Cooperative Multi-Tasking (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Development of UAV Swarm Ad-Hoc Network Communication Technology for Emergency Scenarios: A Review (2026) | evidence=source_error:papers_with_code;source_error:github_search
- Generalized Query-Oriented Image Semantic Coding Empowered by Large AI Models and Semantic-Aware Hybrid Beamforming (2026) | evidence=source_error:papers_with_code;source_error:github_search

## 逐篇简表
| 序号 | 题名 | 年份 | 场景 | 技术框架 | 相关性 | 开源状态 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Restoration Flow Matching-Based Channel Refinement and Equalization Correction for MIMO Semantic Communications | 2026 | 6G / 无线通信 | Diffusion Model | 11.5 | not_detected |
| 2 | Spatial Semantic Communication: When Semantic Transmission Meets Index Modulation | 2026 | 6G / 无线通信 | Semantic-Aware Physical Layer | 11.5 | detected: https://github.com/gxh1106/SSC |
| 3 | Over-the-Air ODE-Inspired Neural Network for Dual Task-Oriented Semantic Communications | 2025 | 文本语义通信 | Autoencoder / DeepSC | 11.5 | not_detected |
| 4 | Editable-DeepSC: Reliable Cross-Modal Semantic Communications for Facial Editing | 2024 | 文本语义通信 | Autoencoder / DeepSC | 11.5 | not_detected |
| 5 | Semantic Communications in the THz Band | 2026 | 6G / 无线通信 | Autoencoder / DeepSC | 11.0 | not_detected |
| 6 | Power-Efficient Optimization for Coexisting Semantic and Bit-Based Users in NOMA Networks | 2025 | 文本语义通信 | Optimization / Resource Allocation | 11.0 | not_detected |
| 7 | Image Semantic Communication with Quadtree Partition-based Coding | 2025 | 6G / 无线通信 | Hybrid Classical + Neural Coding | 10.5 | detected: https://github.com/hyh-bingo/Quad-LIC_Quad-DeepSC |
| 8 | Semantic-Aware Resource Management for C-V2X Platooning via Multi-Agent Reinforcement Learning | 2024 | 6G / 无线通信 | Optimization / Resource Allocation | 9.5 | detected: https://github.com/qiongwu86/Semantic-Aware-Resource-Management-for-C-V2X-Platooning-via-Multi-Agent-Reinforcement-Learning |
| 9 | VQ-VAE Based Digital Semantic Communication with Importance-Aware OFDM Transmission | 2025 | 文本语义通信 | Autoencoder / DeepSC | 9.0 | detected: https://github.com/Molkaat/semantic-communication-refs |
| 10 | LLM-Enabled Data Transmission in End-to-End Semantic Communication | 2025 | 文本语义通信 | Foundation Model / LLM | 9.0 | not_detected |
| 11 | SEM-EDGE-X: INTeNT-aWaRe Semantic Edge Intelligence for Autonomous 6G Vehicular and UAV Communication Networks | 2026 | IoT / 边缘智能 | Multi-Agent | 8.5 | detected: https://github.com/salma-shaik-begum/SEM-EDGE-X |
| 12 | SignDeepSC: A Semantic Signature-based Approach for Robust Semantic Communication | 2026 | 文本语义通信 | Transformer | 8.5 | not_detected |
| 13 | Active Movable-Element RIS Assisted Vehicular Semantic Communications: Modeling and Optimization | 2026 | 6G / 无线通信 | Optimization / Resource Allocation | 8.5 | not_detected |
| 14 | When Robots Exchange Meaning: A Demo of Goal-Oriented Semantic Communications for Collaborative Robotics | 2026 | 图像语义通信 | 未分类 | 8.5 | not_detected |
| 15 | A Semantic Approach to Successive Interference Cancellation for Multiple Access Networks | 2025 | 文本语义通信 | Autoencoder / DeepSC | 8.5 | not_detected |
| 16 | SkillComm: Skill-Driven Semantic Communication for Sequential Workflows via Incremental Token Transmission | 2026 | 图像语义通信 | CNN / DeepJSCC | 8.0 | not_detected |
| 17 | Wireless Intelligence Needs a Cerebellum: Score-Based Foundation Models Toward Real-Time Physical-Layer Inference | 2026 | 6G / 无线通信 | Diffusion Model | 7.5 | needs_review: https://github.com/manjunath5496/Artificial-Intelligence |
| 18 | Toward Semantic Communication for Real-time Mobile 3D Reconstruction | 2026 | 图像语义通信 | Hybrid Classical + Neural Coding | 7.0 | not_detected |
| 19 | Compositional Semantic Communication for Physical AI: Category Theory Meets Game Theory | 2026 | LLM / Agent 辅助语义通信 | Multi-Agent | 7.0 | not_detected |
| 20 | Optimization of Collaborative Semantic Communication Network Performance with Channel and Content Preference Feedback | 2026 | LLM / Agent 辅助语义通信 | Multi-Agent | 7.0 | not_detected |
| 21 | Low-Latency Generative Semantic Communication via Channel-Realization Flow Matching | 2026 | 6G / 无线通信 | Diffusion Model | 7.0 | not_detected |
| 22 | The Price of Meaning: Quantifying Semantic Communication Overheads in Practice | 2026 | 未分类 | 未分类 | 7.0 | not_detected |
| 23 | Dynamic Semantic Prioritisation and Real-Time Voice Reconstruction for Next-Generation VoIP over 6G Networks | 2026 | 语音语义通信 | Reinforcement Learning | 7.0 | detected: https://github.com/zenodo/zenodo-rdm |
| 24 | Goal-Oriented Semantic Communication for Distributed ISAC-Enabled Vehicle Coordination | 2026 | 任务导向通信 | Hybrid Classical + Neural Coding | 6.5 | not_detected |
| 25 | Semantic-Aware Task Clustering for Constructive and Cooperative Multi-Tasking | 2026 | 未分类 | Optimization / Resource Allocation | 6.5 | not_detected |
| 26 | Development of UAV Swarm Ad-Hoc Network Communication Technology for Emergency Scenarios: A Review | 2026 | 车联网 / UAV / 工业互联网 | Optimization / Resource Allocation | 6.5 | not_detected |
| 27 | Generalized Query-Oriented Image Semantic Coding Empowered by Large AI Models and Semantic-Aware Hybrid Beamforming | 2026 | 图像语义通信 | Hybrid Classical + Neural Coding | 6.5 | not_detected |
