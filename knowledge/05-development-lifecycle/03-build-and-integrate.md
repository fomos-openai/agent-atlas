---
title: 03 构建与集成
summary: 从单 Agent 和窄工具集开始，建立类型化边界与确定性测试。
status: stable
last_verified: 2026-09-30
source_ids: [anthropic-effective-agents, openai-agents-sdk]
tags: [lifecycle, build]
---

# 03 构建与集成

先实现一个端到端窄切片：清晰指令、少量高质量工具、结构化状态和显式终止。用 Fake Model 与工具替身测试控制流，再接真实模型。提示、工具 Schema、模型参数和策略均版本化。

所有副作用经统一执行网关，加入幂等、超时、审批和审计。不要在早期引入多 Agent，除非任务确实能独立并行或需要权限隔离。
