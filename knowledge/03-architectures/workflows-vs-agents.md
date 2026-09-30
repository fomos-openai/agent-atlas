---
title: Workflow 与 Agent
summary: 根据路径可预测性选择确定性编排或动态决策。
status: stable
last_verified: 2026-09-30
source_ids: [anthropic-effective-agents]
tags: [workflow, agent]
---

# Workflow 与 Agent

Workflow 用代码定义路径，适合步骤已知、合规严格、需要稳定延迟的任务。Agent 让模型动态选择路径，适合信息不完备、分支难枚举、需要探索的任务。最可靠的系统往往把两者组合：确定性外壳控制权限和状态，Agent 只负责局部判断。

选择标准不是“智能程度”，而是错误代价与环境不确定性。若所有合法步骤能在设计时列出，就优先 workflow；若需要根据未知观察不断重规划，再引入 agent loop。
