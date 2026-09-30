---
title: Agent 威胁模型
summary: 从主体、资产、信任边界和攻击路径系统分析风险。
status: evolving
last_verified: 2026-09-30
source_ids: [owasp-agent-security, nist-ai-rmf]
tags: [security, threat-model]
---

# Agent 威胁模型

盘点用户、Agent、模型提供商、工具、MCP 服务器、数据源和远程 Agent；标出凭据、个人数据、业务对象和外部副作用。威胁包括注入、越权、外泄、记忆投毒、身份混淆、供应链、资源耗尽与审计规避。

每项风险记录前置条件、影响、预防、检测和恢复。模型拒绝只能是纵深防御的一层，真正权限必须由确定性策略与执行边界实施。
