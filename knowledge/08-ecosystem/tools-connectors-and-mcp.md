---
title: 工具、连接器与 MCP
summary: 从私有函数到开放工具协议的能力层。
status: evolving
last_verified: 2026-09-30
source_ids: [mcp-spec, openai-agents-sdk]
tags: [tools, connectors, mcp]
---

# 工具、连接器与 MCP

连接器封装外部 SaaS 和数据库，MCP 提供统一发现与调用协议。无论接口形式，工具都要有清晰 Schema、身份传播、风险标签和错误分类。

工具目录不是越大越好。运行时按任务搜索并只暴露少量候选，减少误调用和上下文开销。第三方工具进入生产前经过权限、数据和供应链审查。
