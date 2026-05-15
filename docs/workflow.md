# 工作流说明

## QueueA：Daily Inbox

每日运行：

```powershell
D:\miniconda\envs\ai\python.exe scripts\fetch_daily_inbox.py
```

作用：

- 从 arXiv 检索语义通信相关论文。
- 只保留近六年论文。
- 去重。
- 保存到 `data/inbox/`。
- 生成 `outputs/daily/` 摘要。

## QueueB：Weekly Curated Set

每周运行：

```powershell
D:\miniconda\envs\ai\python.exe scripts\curate_weekly_set.py
```

作用：

- 合并近期 Inbox。
- 只保留 `curated` 高相关论文进入正式周报。
- 检测开源线索。
- 按场景和技术框架分类。
- 计算相关性分数。
- 输出 Excel、Word 和 Markdown 周报。

## 质量控制

- Daily Inbox 是原始候选流，允许保留低相关候选供复核。
- Weekly Curated Set 是导师汇报流，只输出高相关论文。
- 年份窗口默认是当前年份向前 6 年，未来年份会被排除。
- 开源检测只对高相关论文执行。
