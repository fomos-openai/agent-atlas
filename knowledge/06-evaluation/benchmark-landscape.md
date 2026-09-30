---
title: Benchmark 全景
summary: 理解 AgentBench、GAIA、WebArena、SWE-bench 的测量对象与局限。
status: evolving
last_verified: 2026-09-30
source_ids: [agentbench, gaia, webarena, swebench]
tags: [benchmark]
---

# Benchmark 全景

AgentBench 覆盖多环境交互，GAIA 面向通用助理现实问题，WebArena 评测网站操作，SWE-bench 用真实仓库 Issue 衡量软件工程能力。它们适合比较研究进展和发现失败类型，但不能替代业务评测。

基准分数受环境、工具、提示、采样和污染影响。报告时记录完整 harness、模型版本、运行次数和失败分类。生产决策应以内部代表任务与风险约束为主，公共 Benchmark 为辅。
