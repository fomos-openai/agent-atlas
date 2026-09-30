---
title: Sandbox 与运行时
summary: 将模型决策与受限文件、网络、代码和凭据环境隔离。
status: evolving
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, owasp-agent-security]
tags: [sandbox, runtime]
---

# Sandbox 与运行时

运行时负责工具注册、上下文构建、策略执行、状态持久化和轨迹记录；Sandbox 则限制不可信代码和工具的文件、网络、进程、资源与生命周期。两者共同构成模型之外的可信计算基。

默认拒绝网络和宿主文件，按任务挂载最小目录与短期凭据。保留资源上限、进程树清理、输出大小限制和超时。Sandbox 不能替代应用层授权：被允许运行的代码仍可能通过合法 API 产生越权副作用。
