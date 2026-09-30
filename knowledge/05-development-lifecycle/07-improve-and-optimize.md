---
title: 07 改进与优化
summary: 用生产证据驱动质量、成本与延迟的可回归改进。
status: evolving
last_verified: 2026-09-30
source_ids: [anthropic-evals, openai-agent-evals]
tags: [lifecycle, optimization]
---

# 07 改进与优化

改进循环从失败聚类开始：任务定义、上下文、工具、模型、策略、检索或环境哪一层出了问题。先修确定性边界，再调整提示或模型。每次变化回放黄金集和历史失败集，并比较总体与关键分群。

成本优化包括缩短上下文、缓存稳定前缀、按步骤选择模型、减少无收益反思、批量或并行独立任务。任何成本下降都要与质量和风险指标一起评估。
