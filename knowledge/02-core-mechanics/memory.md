---
title: 记忆
summary: 区分工作记忆、情节记忆、语义记忆和结构化用户状态。
status: evolving
last_verified: 2026-09-30
source_ids: [generative-agents, openai-agents-sdk, owasp-agent-security]
tags: [memory]
---

# 记忆

工作记忆服务当前步骤；情节记忆记录过去事件；语义记忆沉淀稳定知识；程序性记忆保存技能或策略。生产系统还需要结构化任务状态和用户档案，两者不应与自由文本混淆。

写入比读取更危险。每条长期记忆应有来源、租户、主体、有效期、敏感级别和删除能力。未经验证的外部内容不能自动变成高信任记忆。检索命中也不代表事实正确，模型仍需看到来源与时间。
