---
title: Agent-UI 协议
summary: 将流式状态、计划、工具、审批和产物表达给用户界面。
status: experimental
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, a2a-spec]
tags: [ui, protocol]
---

# Agent-UI 协议

Agent UI 不只是聊天流。界面需要接收运行开始、阶段进度、工具请求、审批中断、可恢复状态、部分产物、错误与完成事件。事件应有稳定 ID 和顺序语义，断线重连后能恢复。

协议层应区分模型文本与可信系统状态，避免模型伪造“已批准”或“已完成”。高风险动作使用结构化卡片显示对象、影响与权限。A2UI、AG-UI 等方向仍快速演进，核心知识库关注其共同语义而非绑定单一实现。
