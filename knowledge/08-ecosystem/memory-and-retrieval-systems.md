---
title: 记忆与检索系统
summary: 比较向量、关键词、图、关系和事件存储在 Agent 中的角色。
status: evolving
last_verified: 2026-09-30
source_ids: [generative-agents, owasp-agent-security]
tags: [memory, retrieval]
---

# 记忆与检索系统

向量检索适合语义相似，关键词适合精确实体，关系数据库保存结构化真相，知识图表达关系，事件存储保留时间序列。生产记忆通常组合多种存储。

选择标准包括权限过滤、更新一致性、来源、删除、时间衰减和可解释性。不要让向量库同时承担用户档案、任务状态和审计日志。
