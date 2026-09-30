---
title: 可移植性与兼容性
summary: 避免把 Agent 定义、状态和评测锁死在单一模型或框架。
status: evolving
last_verified: 2026-09-30
source_ids: [mcp-spec, a2a-spec, openai-agents-sdk]
tags: [portability]
---

# 可移植性与兼容性

可移植性包含工具协议、消息与状态 Schema、模型适配、追踪语义和评测数据。完全抽象往往压平厂商特性；完全绑定又提高迁移成本。合理边界是稳定业务契约加显式能力探测。

版本升级应运行同一离线评测集，比较质量、工具行为、延迟和成本。不要假设不同模型的系统指令、并行工具、结构化输出和上下文截断语义相同。协议版本与 Agent 定义版本都应进入轨迹。
