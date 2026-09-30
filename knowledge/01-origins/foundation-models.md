---
title: Foundation Models 转折
summary: Transformer 与大规模预训练为何让通用 Agent 成为可能。
status: stable
last_verified: 2026-09-30
source_ids: [transformer, cot]
tags: [foundation-model, transformer]
---

# Foundation Models 转折

Transformer 提供了高效的序列建模基础，大规模预训练则让模型获得跨领域语言与知识能力。提示与上下文把一个固定参数模型临时配置为不同角色，结构化输出和函数调用又把自然语言决策接到软件系统。

关键变化是接口统一：过去每种任务都需要专用感知器、规划器和规则，现在模型可以在同一上下文中理解目标、读文档、生成代码并选择工具。但概率生成并未消除经典控制问题，反而要求外部运行时提供类型、权限、状态和验证。
