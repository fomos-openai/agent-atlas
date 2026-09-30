---
title: Agent 分类法
summary: 从自主性、时间跨度、环境、组织与风险五个轴描述 Agent。
status: evolving
last_verified: 2026-09-30
source_ids: [russell-norvig-aima, anthropic-effective-agents, openai-agents-sdk]
tags: [taxonomy]
---

# Agent 分类法

单一“Agent/非 Agent”标签信息量过低。工程评审应至少记录五个轴：自主性从建议到代执行；时间跨度从单轮到跨天持久任务；环境从纯文本到浏览器、代码与物理世界；组织从单 Agent 到层级或网络式多 Agent；风险从只读到不可逆外部副作用。

分类的用途是决定控制。高自主、长时间、开放环境和高副作用任务，需要更强的身份、审批、沙箱、预算、恢复与审计。一个系统可以在能力上很先进，却因缺乏这些控制而处于低生产成熟度。
