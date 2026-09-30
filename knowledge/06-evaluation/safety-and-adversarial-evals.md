---
title: 安全与对抗评测
summary: 验证注入、越权、外泄、记忆投毒与资源滥用防线。
status: evolving
last_verified: 2026-09-30
source_ids: [owasp-agent-security, nist-ai-rmf]
tags: [evaluation, security, red-team]
---

# 安全与对抗评测

对抗用例覆盖恶意用户输入、网页或文件中的间接注入、工具元数据欺骗、跨租户检索、记忆污染、凭据诱导和无限循环。目标不仅是模型拒绝，还要证明执行层策略无法被模型绕过。

记录攻击前置条件、预期控制、实际轨迹和残余风险。Red Team 结果进入回归集；修复后复测相邻攻击面，避免只阻断某个字符串。
