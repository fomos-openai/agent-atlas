---
title: 浏览器与 Computer Use Agents
summary: 操作网站和桌面应用的能力、脆弱性与控制模式。
status: evolving
last_verified: 2026-09-30
source_ids: [webarena, owasp-agent-security]
tags: [browser-agent, computer-use]
---

# 浏览器与 Computer Use Agents

浏览器 Agent 适合跨站检索、表单和缺乏 API 的流程。优先使用结构化 DOM 和稳定选择器，视觉坐标作为补充。每次导航后重新确认页面和账户。

付款、发布、删除和发送等动作必须预览并批准。网页内容视为不可信数据，隔离其指令；下载文件先扫描并限制后续工具权限。
