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
- 检测开源线索。
- 按场景和技术框架分类。
- 计算相关性分数。
- 输出 Excel、Word 和 Markdown 周报。
