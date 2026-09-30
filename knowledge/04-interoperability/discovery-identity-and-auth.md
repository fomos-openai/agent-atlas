---
title: 发现、身份与授权
summary: 让 Agent 能找到能力，同时保持主体、权限和委托链可验证。
status: evolving
last_verified: 2026-09-30
source_ids: [a2a-spec, mcp-spec, owasp-agent-security]
tags: [identity, authorization]
---

# 发现、身份与授权

能力发现回答“谁能做什么”，身份回答“谁在请求”，授权回答“是否允许在此对象上执行此动作”。三者不能用模型描述互相替代。服务身份、最终用户、调用 Agent 和委托 Agent 应在审计中分开。

使用短期、受众限定、作用域最小的凭据；策略结合用户、Agent、工具、资源、动作和风险。多级委托必须限制深度并保留原始主体。机密只在执行边界注入，不能进入提示、长期记忆或普通轨迹。
