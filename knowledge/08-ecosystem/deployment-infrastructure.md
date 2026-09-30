---
title: 部署基础设施
summary: 队列、容器、沙箱、状态存储与事件系统如何承载 Agent。
status: stable
last_verified: 2026-09-30
source_ids: [google-adk-lifecycle, openai-agents-sdk]
tags: [deployment, infrastructure]
---

# 部署基础设施

短请求可用无状态服务，长任务需要队列、工作器、检查点和回调。代码执行使用短生命周期沙箱，状态放在外部存储，凭据由密钥系统按运行注入。

基础设施要支持水平扩展、并发限额、取消、优雅停止和跨区恢复。模型 API 限流是容量规划的一部分，不能只看计算资源。
