---
title: 学习与适应
summary: 区分会话内适应、记忆更新、提示优化与模型训练。
status: experimental
last_verified: 2026-09-30
source_ids: [reflexion, voyager, anthropic-evals]
tags: [learning, adaptation]
---

# 学习与适应

Agent 的“学习”可能只是当前会话调整，也可能是长期记忆、技能库更新、提示优化、检索索引变化或模型权重训练。设计必须明确哪一层发生变化、谁批准、如何回滚。

安全的改进闭环从生产轨迹采样，经人工或自动评分形成数据集，再离线比较候选变化，最后小流量发布。让生产 Agent 直接把成功经验写入全局策略，会引入数据投毒、局部过拟合和不可审计漂移。
