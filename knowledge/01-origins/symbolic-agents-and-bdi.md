---
title: 符号智能体与 BDI
summary: 经典 Agent 如何用信念、愿望和意图组织行动。
status: stable
last_verified: 2026-09-30
source_ids: [rao-georgeff-bdi, russell-norvig-aima]
tags: [history, bdi]
---

# 符号智能体与 BDI

经典智能体把环境表示为状态，把行为表示为规则、计划或策略。BDI 模型进一步区分 Beliefs、Desires 与 Intentions：系统持有什么世界认知、希望达到什么状态、当前承诺执行什么计划。其价值不是拟人化，而是把目标冲突、承诺维持和重新规划变成可讨论的结构。

LLM Agent 通常没有严格的 BDI 解释器，却重新遇到相同工程问题：上下文是否等于信念、待办是否等于意图、何时放弃旧计划。显式任务状态和策略层能弥补纯文本上下文的不稳定。
