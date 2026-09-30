---
title: 04 测试、评测与 Red Team
summary: 结合确定性测试、轨迹评分、人工复核和对抗场景。
status: evolving
last_verified: 2026-09-30
source_ids: [anthropic-evals, openai-agent-evals, owasp-agent-security]
tags: [lifecycle, evaluation, red-team]
---

# 04 测试、评测与 Red Team

测试分层：单元测试验证工具和策略；场景评测验证端到端任务；轨迹评分检查工具选择、参数、交接和违规；人工复核发现评分器遗漏；Red Team 验证注入、越权和外泄防线。

发布门禁使用版本固定的数据集、环境和评分标准。对非确定输出运行多次，报告分布而非单值。失败样本必须分类，不能只调提示追求总分。
