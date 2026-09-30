---
title: 评测策略
summary: 从业务目标反推任务集、评分器、阈值与发布决策。
status: evolving
last_verified: 2026-09-30
source_ids: [anthropic-evals, openai-agent-evals]
tags: [evaluation, strategy]
---

# 评测策略

先定义决策：是否发布、选择哪个版本、哪里需要人工。再为任务成功、过程合规、安全、延迟和成本设置指标与最低阈值。评分器可组合确定性断言、程序检查、模型评分和人工复核。

评测集应覆盖常规、边界、历史失败和对抗样本，并按真实流量加权。保留一部分盲测集，避免围绕公开样本过拟合。任何总分都必须能下钻到场景与失败类型。
