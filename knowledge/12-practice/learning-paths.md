---
title: 学习路径
summary: 从闭环实验逐步学习工具、记忆、评测、安全与生产架构。
status: stable
last_verified: 2026-09-30
source_ids: [react, anthropic-effective-agents, owasp-agent-security]
tags: [practice, learning]
---

# 学习路径

1. 运行 `examples/agent_loop`，理解循环和终止。
2. 运行 `tool_use`，观察 Schema 与工具错误。
3. 运行 `memory`，区分短期状态和长期事实。
4. 运行 `eval_harness`，把成功与轨迹变成分数。
5. 运行 `secure_tool_gateway`，体验策略与审批。
6. 用自己的窄任务替换 Fake Model 输入，先保留离线回归。
