---
title: 成熟度模型
summary: 以证据而非演示效果划分 Agent 的五级成熟度。
status: evolving
last_verified: 2026-09-30
source_ids: [anthropic-evals, google-adk-lifecycle, nist-ai-rmf]
tags: [maturity, production]
---

# 成熟度模型

| 等级 | 特征 | 进入下一阶段的证据 |
|---|---|---|
| L0 生成式功能 | 单轮输出，无环境行动 | 明确任务与可重复成功标准 |
| L1 受控助手 | 少量只读工具，人在每一步确认 | 离线用例集与工具正确率 |
| L2 有界 Agent | 多步闭环，有预算和沙箱 | 轨迹评测、恢复测试、风险门禁 |
| L3 生产 Agent | 持久状态、审批、可观测、SLO | 线上质量、成本、安全与事件数据 |
| L4 Agent 平台 | 多租户、策略中心、互操作、持续改进 | 跨团队治理和可移植评测 |

成熟度不能由模型名称决定。升级意味着新增可证明的控制和运营能力，而不仅是加入更多工具或更长上下文。
