---
title: Coding Agents
summary: 从代码问答走向仓库级理解、修改、测试与评审。
status: evolving
last_verified: 2026-09-30
source_ids: [swebench, openai-agents-sdk]
tags: [coding-agent]
---

# Coding Agents

Coding Agent 通过文件、搜索、补丁、终端和测试形成强反馈闭环。可靠流程先复现问题，最小修改，运行相关测试，再审查 diff。工作树隔离和权限边界是基础。

风险包括命令注入、依赖供应链、密钥泄漏和破坏性操作。基准通过不代表可维护性，仍需代码审查、静态检查和仓库约定。
