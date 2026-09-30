---
title: Prompt Injection
summary: 防御用户、网页、文档和工具输出中的恶意指令。
status: evolving
last_verified: 2026-09-30
source_ids: [owasp-agent-security, anthropic-trustworthy]
tags: [security, prompt-injection]
---

# Prompt Injection

直接注入来自用户，间接注入隐藏在 Agent 读取的网页、邮件、文档或工具结果中。仅靠提示告诉模型“忽略恶意内容”不足以形成边界。

防御组合包括数据与指令分层、来源标记、最小上下文、工具白名单、参数验证、敏感动作审批、输出过滤和持续对抗评测。被污染内容不能写入高信任记忆；跨边界复制数据前做策略检查。
