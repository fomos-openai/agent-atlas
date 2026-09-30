---
title: 失败图谱
summary: 按目标、上下文、模型、工具、状态、环境和治理定位问题。
status: evolving
last_verified: 2026-09-30
source_ids: [anthropic-evals, owasp-agent-security]
tags: [practice, failure]
---

# 失败图谱

失败分类：目标含糊；上下文缺失或污染；模型计划错误；工具选择或参数错误；状态陈旧；环境变化；权限或策略缺陷；恢复失败；评分器误判。先定位层次，再修复。

不要默认“换更大模型”。若错误是权限、Schema 或状态，模型升级不会形成确定性修复。
