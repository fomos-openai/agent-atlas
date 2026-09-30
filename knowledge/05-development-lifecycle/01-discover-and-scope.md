---
title: 01 发现与定界
summary: 判断问题是否值得使用 Agent，并形成任务与成功契约。
status: stable
last_verified: 2026-09-30
source_ids: [anthropic-effective-agents, nist-ai-rmf]
tags: [lifecycle, discovery]
---

# 01 发现与定界

先定义用户、任务频率、当前流程、失败成本、数据与系统边界。Agent 适合步骤无法完全预定义、需要处理非结构信息、工具反馈能帮助下一步判断的任务。不适合没有客观成功标准或单次错误不可接受且无法审批的场景。

产物包括任务契约、基线流程、成功指标、风险分级、允许工具和不做清单。进入设计阶段前，应有至少 10 个真实代表案例，而不是只用理想化演示。
