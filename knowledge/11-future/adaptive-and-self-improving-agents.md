---
title: 自适应与自我改进 Agent
summary: 从轨迹中改进提示、技能、记忆和策略的受控闭环。
status: experimental
last_verified: 2026-09-30
source_ids: [reflexion, voyager, anthropic-evals]
tags: [future, self-improvement]
---

# 自适应与自我改进 Agent

近期可行形态是外环改进：从轨迹发现失败，生成候选规则或技能，离线评测后由人批准发布。直接在线修改核心策略风险很高。

关键研究是防数据投毒、跨任务泛化、信用分配和安全回滚。若改进无法在保留集持续复现，就不应称为学习。
