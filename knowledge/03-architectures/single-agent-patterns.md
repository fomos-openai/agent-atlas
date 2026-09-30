---
title: 单 Agent 模式
summary: 增强调用、路由、规划执行、反思与受控循环。
status: stable
last_verified: 2026-09-30
source_ids: [anthropic-effective-agents, react]
tags: [single-agent, patterns]
---

# 单 Agent 模式

常见模式包括带检索和工具的增强调用、模型路由、规划-执行、评审-修订以及由环境反馈驱动的受控循环。优先使用一个清晰专长、有限工具集和明确输出契约的 Agent。

拆分前先问：失败是否来自上下文过载、工具语义差或评测缺失？若是，增加 Agent 数量只会隐藏问题。单 Agent 更容易共享上下文、调试轨迹和控制成本，是默认起点。
