---
title: 05 部署与发布
summary: 用分阶段流量、版本绑定、回滚和权限门禁发布 Agent。
status: stable
last_verified: 2026-09-30
source_ids: [google-adk-lifecycle, openai-agents-sdk]
tags: [lifecycle, deploy]
---

# 05 部署与发布

发布包应绑定 Agent 定义、模型、工具版本、策略、检索索引和评测结果。先影子运行，再内部用户、小流量和逐步扩展。每一阶段都有质量、成本、安全和人工升级阈值。

回滚不仅是代码回滚，还要处理已写入状态、已启动外部任务和新记忆。高风险工具默认关闭，通过配置和身份分组逐步开放。
