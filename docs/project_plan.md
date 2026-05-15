# 项目总 Plan

本项目按“脚本 MVP -> 自动化更新 -> Agent 辅助精选 -> Skill 封装”的顺序推进。

## 阶段

1. Phase 0：创建仓库骨架、配置、文档和忽略规则。
2. Phase 1：实现 arXiv 检索、近六年过滤、去重、JSON/CSV/Excel 输出。
3. Phase 2：实现开源标注、应用场景分类、技术框架分类和相关性分数。
4. Phase 3：生成 Word 汇报文件。
5. Phase 4：接入 GitHub Actions 定时更新。
6. Phase 5：在流程稳定后封装 Agent 和 Skill。

## 边界

- 第一版不依赖 LLM。
- 第一版不强制依赖 API key。
- PDF 可缓存到本地，但不提交仓库。
- 如需删除文件，只能一次删除一个明确路径，禁止批量删除目录或文件。
