---
title: 成本、延迟与质量
summary: 用 Pareto 前沿而非单指标比较 Agent 方案。
status: stable
last_verified: 2026-09-30
source_ids: [openai-agent-evals, google-adk-lifecycle]
tags: [evaluation, cost, latency]
---

# 成本、延迟与质量

总成本包含模型 Token、工具、搜索、沙箱、存储、人工审批和失败返工。延迟拆为首响应、模型、工具等待、审批和尾延迟。质量要按任务价值和风险加权。

比较方案时绘制质量-成本-延迟 Pareto 前沿。便宜但需要大量人工返工并不经济；高分但 P99 超时也不可用。预算控制是运行时功能，超出时应降级、缩小任务或暂停。
