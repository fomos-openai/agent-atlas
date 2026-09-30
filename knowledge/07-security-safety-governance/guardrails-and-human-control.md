---
title: Guardrails 与人类控制
summary: 在输入、输出、工具和高风险决策处组合自动控制与人工审批。
status: evolving
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, anthropic-trustworthy]
tags: [guardrail, human-control]
---

# Guardrails 与人类控制

输入护栏阻断非法目标，工具护栏校验参数与权限，输出护栏处理泄露和政策问题。人工审批用于不可逆、高价值或语境复杂的动作。护栏结果要进入轨迹并支持恢复。

控制权应可见、及时且可操作：用户能暂停、取消、修改范围和拒绝单项动作。审批不能只显示模糊描述，而要展示对象、参数、影响与可逆性。
