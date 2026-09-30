---
title: 状态与持久执行
summary: 支持等待、恢复、重放和跨天任务的运行时基础。
status: evolving
last_verified: 2026-09-30
source_ids: [mcp-spec, google-adk-lifecycle, openai-agents-sdk]
tags: [state, durable-execution]
---

# 状态与持久执行

长任务会遇到人工审批、外部回调、限流和机器故障，因此不能依赖进程内存。持久执行保存任务输入、当前状态、已完成副作用、检查点、等待原因和恢复令牌。

恢复语义应明确定义为至少一次或至多一次；关键写操作用幂等键和补偿事务。模型输出本身不是状态真相，结构化状态机才是。重放时必须避免重复发送邮件、扣款或发布内容。
