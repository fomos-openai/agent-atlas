---
title: 生产就绪检查表
summary: 上线前检查任务、工具、状态、评测、安全、观测和运营。
status: stable
last_verified: 2026-09-30
source_ids: [google-adk-lifecycle, owasp-agent-security]
tags: [practice, checklist]
---

# 生产就绪检查表

- 目标、成功和终止条件可外部验证。
- 工具最小权限，写操作幂等且可审批。
- 状态可恢复，重试不会重复副作用。
- 代表、边界、历史失败和对抗用例通过门禁。
- 轨迹脱敏并关联业务结果、成本和版本。
- 有暂停、撤权、隔离记忆和事件响应手册。
- 有 Owner、SLO、预算、升级与退役路径。
