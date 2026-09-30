---
title: 框架与 SDK
summary: 比较代码优先、图编排、多 Agent 和托管式开发方式。
status: evolving
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, google-adk-lifecycle, anthropic-effective-agents]
tags: [frameworks, sdk]
---

# 框架与 SDK

主流框架通常提供 Agent 定义、工具、状态、流式事件、交接、护栏和追踪。差异集中在控制权、持久执行、部署集成与可观测性。先做最小原型验证抽象是否匹配，而不是依据示例数量选择。

保留自有业务工具和评测数据，框架适配放在边缘。若简单 API 循环已满足需求，不必引入复杂图或多 Agent 框架。
