---
title: 上下文工程
summary: 为每一步选择最小、相关、可信且有边界的上下文。
status: evolving
last_verified: 2026-09-30
source_ids: [openai-agents-sdk, anthropic-effective-agents]
tags: [context]
---

# 上下文工程

上下文工程不等于把更多文本塞进窗口。它负责选择指令、任务状态、用户偏好、检索证据、工具定义和历史摘要，并明确各自优先级与信任级别。

上下文越长，注意力竞争、过期信息和注入面越大。推荐把稳定策略保留在受控指令层，把业务事实放在带来源的数据层，把可变历史压缩成可追溯摘要。每次工具调用只暴露完成当前步骤所需的最小上下文。
