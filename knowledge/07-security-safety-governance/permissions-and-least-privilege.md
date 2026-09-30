---
title: 权限与最小特权
summary: 按用户、Agent、工具、对象和动作缩小授权范围。
status: stable
last_verified: 2026-09-30
source_ids: [owasp-agent-security, mcp-spec]
tags: [security, authorization]
---

# 权限与最小特权

Agent 继承用户意图，不应自动继承用户所有权限。读与写、草稿与发送、查询与转账必须拆成不同能力。短期凭据限定受众、租户、资源和动作，并在运行结束后撤销。

授权在执行时重新判断，不能信任模型声称“用户已同意”。高风险工具支持预览和逐项批准，审批记录绑定具体参数，参数变化后重新审批。
