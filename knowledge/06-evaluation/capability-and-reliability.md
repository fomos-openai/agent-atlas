---
title: 能力与可靠性
summary: 区分偶尔能完成、稳定完成和在受扰条件下完成。
status: stable
last_verified: 2026-09-30
source_ids: [agentbench, gaia]
tags: [evaluation, reliability]
---

# 能力与可靠性

能力回答系统在理想条件下能否完成，可靠性回答它在输入变化、工具错误、长上下文和多次重复中是否仍能完成。报告 pass@1、重复成功分布、恢复率和最坏分群，而不是只展示最佳案例。

可靠性还包括校准：不确定时能否求助或停止。一个知道边界并升级的 Agent，通常比偶尔高分但自信越权的系统更适合生产。
