---
title: Model Context Protocol
summary: MCP 如何标准化 AI 应用对工具、资源和上下文的访问。
status: evolving
last_verified: 2026-09-30
source_ids: [mcp-spec]
tags: [mcp, protocol]
---

# Model Context Protocol

MCP 定义客户端、服务器与宿主之间的能力协商，使工具和资源不必为每个模型平台重复适配。2026-07-28 规范强化了无状态核心、多轮请求、扩展、任务和授权能力，适合长期 Agent 工作流。

协议统一不等于安全自动成立。宿主仍需决定哪些服务器可信、向每个调用传递什么身份和上下文、哪些工具需要批准。对远程 MCP，应验证服务器身份、限制令牌受众、过滤工具元数据并记录完整调用轨迹。
