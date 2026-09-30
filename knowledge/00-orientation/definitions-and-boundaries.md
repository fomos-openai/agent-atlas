---
title: 定义与边界
summary: 用自主决策、环境行动和闭环反馈区分 Agent、Workflow 与 Chatbot。
status: stable
last_verified: 2026-09-30
source_ids: [russell-norvig-aima, react, anthropic-effective-agents]
tags: [definition, boundary]
---

# 定义与边界

Agent 是在明确约束内，为完成目标而自主选择下一步、调用工具改变环境、观察结果并调整行动的系统。核心不是“用了大模型”，而是存在 **目标 - 决策 - 行动 - 观察 - 终止** 闭环。

Chatbot 主要生成一次响应；Workflow 的控制路径由代码或图预先规定；Agent 允许模型在运行时决定路径。真实产品常是混合体：可预测部分使用 workflow，信息不完备且需要判断的局部使用 agent。自主性不是越高越好；权限、失败成本和可验证性共同决定允许的自主范围。

## 最小判定

- 能否根据观察改变下一步，而不是只按固定脚本执行？
- 是否能对外部环境产生受控行动？
- 是否存在预算、最大步数、成功条件和退出条件？
- 失败后能否暂停、恢复、求助或安全终止？

如果前两项为否，它更可能是生成式功能或 workflow；如果后两项为否，它还不是可运营的 Agent。
