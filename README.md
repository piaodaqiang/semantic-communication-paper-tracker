# Semantic Communication Paper Tracker

语义通信论文自动检索与整理项目，用于持续追踪近六年论文、标注开源情况、按场景和技术框架分类，并输出导师可读的 Excel / Word 汇报文件。

## 当前能力

- QueueA Daily Inbox：从 arXiv 拉取原始论文元数据，过滤近六年，去重后保存。
- OpenAlex 兜底检索：当 arXiv 结果不足时补充更宽的论文元数据来源。
- QueueB Weekly Curated Set：合并 Inbox，严格筛选高相关论文，检测开源线索，分类并导出周报。
- Weekly 输出只包含 `curated` 论文；低相关候选保留在 Daily Inbox 供人工复核。
- 输出格式：
  - Excel：`outputs/weekly/semantic_communication_papers_YYYY-WW.xlsx`
  - Word：`outputs/weekly/semantic_communication_report_YYYY-WW.docx`
  - Markdown 摘要：`outputs/weekly/weekly_summary_YYYY-WW.md`
- 没有 LLM、没有 API key 时也能运行基础流程。

## 筛选边界

- 年份窗口默认只允许当前年份向前 6 年，例如 2026 年运行时保留 `2021-2026`，自动排除未来年份和异常年份。
- Weekly 精选要求标题或摘要出现语义通信核心组合词，例如 `semantic communication`、`semantic communications`、`SemCom`、`semantic-aware communication`、`task-oriented semantic communication`。
- 开源标注只在高相关 `curated` 论文上执行，避免无关论文因为包含 GitHub 链接而被误计入开源论文。
- arXiv 和 OpenAlex 的重复项会优先按规范化标题合并。

## 快速开始

本机如果 `python` 不在 PATH，可使用：

```powershell
D:\miniconda\envs\ai\python.exe scripts\fetch_daily_inbox.py
D:\miniconda\envs\ai\python.exe scripts\curate_weekly_set.py
```

快速验证时建议先限制每个关键词的 arXiv 返回量：

```powershell
D:\miniconda\envs\ai\python.exe scripts\fetch_daily_inbox.py --max-results 3 --fail-on-empty
```

如果本机网络或证书环境导致 arXiv 访问失败，脚本会在每日 Markdown 摘要的“抓取错误”中记录原因；GitHub Actions 环境通常不会遇到本机 Conda 证书问题。

也可以安装依赖后使用普通 Python：

```powershell
pip install -r requirements.txt
python scripts/fetch_daily_inbox.py
python scripts/curate_weekly_set.py
```

## 项目结构

```text
configs/                 检索词、数据源、分类规则
paper_tracker/           核心 Python 包
scripts/                 可执行脚本入口
data/inbox/              Daily Inbox 原始流
data/curated/            Weekly Curated Set 精华流
outputs/daily/           每日新增摘要
outputs/weekly/          每周 Excel / Word / Markdown 输出
docs/                    项目说明、工作流、Skill 设计
```

## 注意

- 仓库可以公开，但不要提交 `.env`、API key、PDF 缓存和大体积临时文件。
- PDF 缓存目录 `cache/` 已被 `.gitignore` 排除。
- 本项目第一版是脚本系统，Agent 和 Skill 等流程稳定后再封装。
