---
title: 记忆与数据安全
summary: 防止跨租户泄露、长期投毒和超期保留。
status: evolving
last_verified: 2026-09-30
source_ids: [owasp-agent-security, eu-ai-act]
tags: [security, memory, privacy]
---

# 记忆与数据安全

记忆条目必须有主体、租户、来源、用途、敏感级别、有效期和删除路径。检索先做权限过滤，再做语义相似度；不要从共享向量库中取回无权查看的数据。

写入前验证事实与来源，低信任内容进入隔离区。用户应能查看、更正和删除长期记忆。训练、评测、日志与产品记忆的用途不同，不能默认为互相复用。
