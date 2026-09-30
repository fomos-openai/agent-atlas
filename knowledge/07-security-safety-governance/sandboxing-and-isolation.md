---
title: 沙箱与隔离
summary: 限制不可信代码、浏览器和工具的系统资源与网络范围。
status: stable
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, owasp-agent-security]
tags: [security, sandbox]
---

# 沙箱与隔离

沙箱默认无宿主凭据、无广泛网络、无永久文件；按任务挂载最小资源并设置 CPU、内存、磁盘、进程和时间限制。多租户运行必须隔离文件、缓存、日志和网络身份。

沙箱快照有助恢复和审计，但可能包含敏感数据，应加密并按策略删除。输出进入可信系统前仍需校验，不能因为代码在沙箱里运行就信任结果。
