---
title: 规划、搜索与控制
summary: 从状态空间搜索到模型驱动的动态规划。
status: stable
last_verified: 2026-09-30
source_ids: [russell-norvig-aima, react]
tags: [planning, search]
---

# 规划、搜索与控制

规划是在动作模型和约束下寻找从当前状态到目标状态的路径。经典方法强调可枚举状态、动作前置条件和代价；LLM Agent 则常在不完整模型中生成候选步骤，再通过工具观察修正。

工程上应把“模型建议”与“执行控制”分开：模型负责提出下一步，运行时负责校验参数、权限、预算和状态转换。对路径稳定的任务，确定性 workflow 更可靠；对分支无法预先枚举的任务，才使用动态规划。
