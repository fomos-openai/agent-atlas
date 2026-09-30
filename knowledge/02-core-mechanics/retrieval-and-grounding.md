---
title: 检索与 Grounding
summary: 让行动基于可追溯证据，而非模型记忆或搜索片段。
status: stable
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, gaia]
tags: [retrieval, grounding]
---

# 检索与 Grounding

检索系统负责发现候选证据，Grounding 则要求输出或行动与证据建立可检查关系。典型流程包括查询改写、权限过滤、混合检索、重排、片段选择、引用和答案验证。

Agent 场景还需防止检索结果携带恶意指令。外部文本只能作为数据，不应覆盖系统策略。对于会触发副作用的结论，应从搜索摘要进入原始来源，核验时间、主体和适用范围。
