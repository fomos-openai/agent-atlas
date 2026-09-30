---
title: 06 观测与运营
summary: 把轨迹、业务结果、成本和安全事件连接起来。
status: evolving
last_verified: 2026-09-30
source_ids: [openai-agent-evals, google-adk-lifecycle]
tags: [lifecycle, observability]
---

# 06 观测与运营

追踪记录运行、模型调用、工具、交接、护栏、审批和状态转换；指标覆盖成功率、人工接管、重试、延迟、Token、工具费用与风险事件。日志必须脱敏并支持按租户、版本和场景切片。

告警应面向可操作症状，如连续工具失败、费用异常、越权拒绝激增或任务卡死。运营手册定义暂停 Agent、撤销凭据、隔离记忆和恢复任务的步骤。
