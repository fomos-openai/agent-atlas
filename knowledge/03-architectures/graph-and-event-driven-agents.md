---
title: 图与事件驱动 Agent
summary: 用显式节点、边、事件和检查点组织复杂运行。
status: evolving
last_verified: 2026-09-30
source_ids: [google-adk-lifecycle, openai-agents-sdk]
tags: [graph, event-driven]
---

# 图与事件驱动 Agent

图结构把模型步骤、工具、审批和分支表示为可观察节点，使循环、并行和恢复比隐式 while loop 更清晰。事件驱动架构则让外部消息触发、暂停或继续任务，适合跨系统长流程。

图不应成为视觉化的意大利面。节点要对应稳定职责，边要表达真实状态转换，副作用要有幂等和重放策略。模型生成的临时计划可以作为数据，不应动态改写未经校验的生产执行图。
