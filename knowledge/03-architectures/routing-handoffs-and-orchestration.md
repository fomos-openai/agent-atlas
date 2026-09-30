---
title: 路由、Handoff 与编排
summary: 区分任务分类、工具式调用和控制权交接。
status: evolving
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, a2a-spec]
tags: [routing, handoff]
---

# 路由、Handoff 与编排

路由决定由谁处理请求；把专家当工具调用时，主 Agent 保留控制权；Handoff 则把后续对话和任务所有权交给另一个 Agent。三者必须在轨迹中可区分。

编排层维护能力目录、上下文裁剪、超时、重试、并发、预算和汇总。交接只传递必要信息，并带上来源与未解决问题；不要复制全部历史。跨组织交接还需要身份、授权和数据最小化。
