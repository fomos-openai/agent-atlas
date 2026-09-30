---
title: 工具与 Function Calling
summary: 设计清晰、最小权限、可验证、幂等的 Agent 工具。
status: evolving
last_verified: 2026-09-30
source_ids: [toolformer, openai-agents-sdk, mcp-spec]
tags: [tools, function-calling]
---

# 工具与 Function Calling

工具是 Agent 改变环境的能力边界。高质量工具有窄职责、清晰名称、严格参数 Schema、结构化结果、稳定错误语义和可区分的读写风险。不要用一个“万能 API”隐藏权限和副作用。

写操作应支持幂等键、预览、审批、超时和补偿；读操作应做作用域和租户过滤。工具结果必须区分业务失败、权限失败、暂时故障和参数错误，让模型能选择正确恢复策略。
