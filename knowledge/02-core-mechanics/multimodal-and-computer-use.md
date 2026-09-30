---
title: 多模态与 Computer Use
summary: Agent 如何通过视觉、语音和图形界面感知并行动。
status: evolving
last_verified: 2026-09-30
source_ids: [webarena, openai-agents-sdk]
tags: [multimodal, computer-use]
---

# 多模态与 Computer Use

Computer Use 把屏幕、DOM、键鼠和应用状态变成环境。它能覆盖缺乏 API 的长尾流程，却比结构化工具更脆弱：像素和布局会变化，界面文本可能注入指令，误点击可能产生真实副作用。

优先级应是 API/结构化工具、可访问性树或 DOM、最后才是纯视觉坐标。每次高风险操作前重新观察目标、校验窗口与账户、展示动作摘要并请求批准。截图与操作轨迹属于敏感审计数据，应限制留存。
