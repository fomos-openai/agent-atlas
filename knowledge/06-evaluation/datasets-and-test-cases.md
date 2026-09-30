---
title: 数据集与测试用例
summary: 建立可复现、分层、版本化且尊重隐私的 Agent 测试集。
status: stable
last_verified: 2026-09-30
source_ids: [anthropic-evals, gaia]
tags: [evaluation, dataset]
---

# 数据集与测试用例

每个用例包括初始状态、用户目标、可用工具、模拟环境、成功条件、禁止行为和评分说明。生产样本进入数据集前要脱敏、去重并获得适当使用权限。

版本记录新增、修正和删除原因。测试环境冻结外部依赖或使用可重放模拟器，避免网站变化污染结论。对非确定模型，多次运行并保存随机性与模型版本。
