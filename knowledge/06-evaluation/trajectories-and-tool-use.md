---
title: 轨迹与工具使用评测
summary: 检查工具选择、参数、顺序、恢复与不必要动作。
status: evolving
last_verified: 2026-09-30
source_ids: [anthropic-evals, openai-agent-evals]
tags: [evaluation, trajectory, tools]
---

# 轨迹与工具使用评测

最终结果可能偶然正确，但过程使用了错误数据、越权工具或不可接受成本。轨迹评测检查是否选择正确工具、参数是否满足 Schema、是否引用观察、是否重复调用、是否在失败后采取合理恢复。

不要求轨迹完全匹配一条黄金路径，因为复杂任务可能有多条合法方案。应评估关键不变量和禁止行为，并把可接受替代路径显式编码。
