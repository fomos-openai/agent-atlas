---
title: 多 Agent 模式
summary: 主管-专家、对等协作、辩论与市场式调度的适用边界。
status: evolving
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, a2a-spec]
tags: [multi-agent]
---

# 多 Agent 模式

多 Agent 的真实收益来自并行独立探索、专业权限隔离和上下文分区。常见模式是主管分派专家、对等交接、生成者-评审者，以及按能力发现远程 Agent。

代价包括消息膨胀、责任模糊、循环委派、共享状态冲突和更难的全局评测。每个 Agent 必须有明确所有权、输入输出契约、预算和停止条件；调度器应能检测循环并保留完整跨 Agent 轨迹。
