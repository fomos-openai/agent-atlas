---
title: Agent 架构
summary: 从简单 workflow 到持久、多 Agent、事件驱动系统的组合方式。
status: evolving
last_verified: 2026-09-30
source_ids: [anthropic-effective-agents, openai-agents-sdk]
tags: [architecture]
---

# Agent 架构

架构选择应从最简单可验证形态开始。单次增强调用、串并行 workflow、路由、单 Agent、多 Agent 都是工具，不是成熟度等级。复杂度只有在提高可分解性、隔离或可验证性时才值得。
