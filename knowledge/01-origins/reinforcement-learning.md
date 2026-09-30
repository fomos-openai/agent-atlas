---
title: 强化学习遗产
summary: 奖励、探索、信用分配如何影响 Agent 设计。
status: stable
last_verified: 2026-09-30
source_ids: [sutton-barto-rl, reflexion]
tags: [reinforcement-learning]
---

# 强化学习遗产

强化学习把 Agent 描述为在环境中选择行动、获得回报并改进策略的主体。它贡献了状态、动作、奖励、策略、价值和探索等语言，也揭示了稀疏奖励、延迟信用分配和奖励黑客等难题。

多数生产 LLM Agent 不会在线更新模型权重，但会通过提示、记忆、策略规则或离线优化形成“外环学习”。Reflexion 一类方法用语言反馈影响后续尝试。安全边界是：生产反馈不能未经审查直接变成长期记忆或策略，否则错误与攻击会被放大。
