# Semantic Communication Paper Tracker

语义通信论文自动检索与整理项目。系统用于持续追踪近六年语义通信相关论文，补充论文元数据，标注开源代码线索，并按应用场景和技术框架分类，最终生成 Excel、Word 和 Markdown 汇总文件。

## 当前功能

- Daily Inbox：从 arXiv 和 OpenAlex 检索论文元数据，过滤近六年论文并去重。
- Weekly Curated Set：合并近期 Daily Inbox，筛选高相关论文，生成正式周报。
- 开源代码补查：自动检查论文元数据、arXiv comment、Papers with Code、GitHub、论文页面和 PDF 中的代码线索。
- 分类整理：按应用场景、技术框架、任务类型和模态进行基础分类。
- 结果导出：生成导师可读的 Excel 表格、Word 报告和 Markdown 摘要。
- GitHub Actions：支持每日自动检索、每周自动整理，也支持手动触发 workflow。

## 输出文件

每周整理结果位于 `outputs/weekly/`：

```text
semantic_communication_papers_YYYY-WW.xlsx
semantic_communication_report_YYYY-WW.docx
weekly_summary_YYYY-WW.md
```

Excel 中包含标题、作者、年份、摘要、论文链接、PDF 链接、分类结果、相关性分数、开源状态和代码链接等字段。

开源状态说明：

- `detected`：自动流程检测到较可信的代码仓库链接。
- `needs_review`：发现候选链接，但需要人工复核。
- `not_detected`：自动流程未发现明确代码链接，不代表论文一定未开源。

## 使用方式

安装依赖：

```powershell
pip install -r requirements.txt
```

运行每日检索：

```powershell
python scripts/fetch_daily_inbox.py
```

运行每周整理：

```powershell
python scripts/curate_weekly_set.py
```

在本地 Python 不在 PATH 的情况下，可以使用指定解释器运行：

```powershell
D:\miniconda\envs\ai\python.exe scripts\fetch_daily_inbox.py
D:\miniconda\envs\ai\python.exe scripts\curate_weekly_set.py
```

快速测试时可以限制每个关键词的返回数量：

```powershell
python scripts/fetch_daily_inbox.py --max-results 3 --fail-on-empty
```

## 筛选规则

- 年份范围：默认保留当前年份向前六年的论文，例如 2026 年运行时保留 2021-2026。
- Weekly 输出只包含高相关 `curated` 论文，低相关候选保留在 Daily Inbox。
- 语义通信相关性主要依据标题和摘要中的核心组合词判断，例如 `semantic communication`、`semantic communications`、`SemCom`、`semantic-aware communication`、`task-oriented semantic communication`。
- 开源检测只对高相关 `curated` 论文执行，避免无关论文因包含 GitHub 链接被误标为开源论文。

## 项目结构

```text
configs/                 检索词、数据源和分类规则
paper_tracker/           核心 Python 模块
scripts/                 可执行脚本入口
data/inbox/              Daily Inbox 原始数据
data/curated/            Weekly Curated Set 数据
outputs/daily/           每日新增摘要
outputs/weekly/          每周 Excel / Word / Markdown 输出
docs/                    项目计划、工作流和 Skill 设计说明
```

## 注意事项

- 不提交 `.env`、API key、PDF 缓存和本地临时文件。
- PDF 缓存目录 `cache/` 已被 `.gitignore` 排除。
- GitHub Actions 使用仓库默认 `GITHUB_TOKEN` 提升 GitHub 搜索稳定性，不需要额外配置 Secret。
- 当前版本以脚本自动化为主，Agent 和 Skill 封装放在后续流程稳定后继续扩展。
