---
title: 身份、委托与供应链
summary: 管理非人身份、委托链和第三方工具依赖。
status: evolving
last_verified: 2026-09-30
source_ids: [a2a-spec, mcp-spec, owasp-agent-security]
tags: [security, identity, supply-chain]
---

# 身份、委托与供应链

区分用户身份、Agent 工作负载身份、工具服务身份和远程 Agent 身份。委托令牌保留原始主体、限制能力和深度，避免“代表用户”退化为长期共享密钥。

第三方 MCP、插件、模型与依赖都是供应链。固定版本、验证来源、审查权限和更新差异；能力描述变化应触发重新批准。停用组件时撤销密钥并检查残留任务。
