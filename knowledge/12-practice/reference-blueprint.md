---
title: 参考蓝图
summary: 从入口到策略、运行时、工具、状态、评测和运营的生产路径。
status: stable
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, google-adk-lifecycle, owasp-agent-security]
tags: [practice, blueprint]
---

# 参考蓝图

请求经身份与风险分类进入编排器；编排器加载版本化 Agent、最小上下文和工具；策略网关验证每次行动；持久运行时保存状态；沙箱执行不可信代码；追踪连接业务结果；评测服务决定发布。

从单 Agent、三个以内工具和一个端到端指标开始。所有写操作经过统一网关，高风险动作可暂停审批。
