---
title: 生产参考架构
summary: 一个可运营 Agent 平台的控制面、执行面、数据面和保证面。
status: evolving
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, google-adk-lifecycle, owasp-agent-security]
tags: [reference-architecture, production]
---

# 生产参考架构

参考架构分四面：控制面管理 Agent 定义、模型、策略、版本和发布；执行面运行循环、工具、沙箱和持久状态；数据面提供检索、记忆、密钥和业务系统；保证面覆盖身份、审批、评测、追踪、审计和事件响应。

入口先完成身份和风险分级，再创建有预算的运行。每个工具调用经过策略判定，写操作可暂停审批；轨迹与业务结果进入观测和评测，改进通过离线门禁重新发布。该分层避免把所有责任塞进提示词或单一框架。
