---
title: Agent-to-Agent 协议
summary: A2A 的能力发现、任务协作、消息与产物交换模型。
status: evolving
last_verified: 2026-09-30
source_ids: [a2a-spec]
tags: [a2a, protocol]
---

# Agent-to-Agent 协议

A2A 面向独立且可能不透明的 Agent 系统。参与者通过 Agent Card 描述能力与端点，围绕任务交换消息、状态和产物，而不要求共享内部记忆或工具。它适合跨框架、跨团队甚至跨组织协作。

工程重点是任务所有权、身份传播、数据边界、超时与取消。远程 Agent 的自然语言声明不能替代契约或授权；调用方应验证返回产物、限制委托链深度，并保留跨域关联 ID。
