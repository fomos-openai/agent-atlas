# Agent Atlas

[![Agent Atlas 2026 工程知识地图](./artifacts/agent-knowledge-map.png)](./artifacts/agent-knowledge-map.html)

[交互知识地图](./artifacts/agent-knowledge-map.html) · [PDF 样书](./artifacts/agent-atlas-book.zh-CN.pdf)

> 面向资深后端工程师与技术管理者的 Agent 工程技术专著：从范式源流，到系统架构，再到生产生命周期。

**知识截止：2026-10-01** · **阶段：v2 foundation 样章审核** · **中文主文 + English terms**

Agent Atlas v2 不再把知识点压缩成“一主题一页”的索引卡。`content/` 是 HTML 知识站和 PDF 专著的唯一正文源；`labs/` 提供可离线复现的实验；`catalog/` 保存可审计的来源、主张、技术和案例数据。

## 当前审核包

第一阶段只交付目录、构建系统和两篇完整样章，作为批量写作前的质量门：

- [样章：从符号主义、BDI、规划和强化学习到 LLM Agent](./content/01-foundations/02-paradigm-evolution.qmd)
- [样章：工具契约、结构化交互、动态发现与代码执行](./content/02-core-mechanics/06-tools-contracts-and-execution.qmd)
- [实验 01：最小可审计运行循环](./labs/python/stages/01-auditable-loop/README.md)
- [实验 02：带策略判定的工具网关](./labs/python/stages/02-secure-tool-gateway/README.md)
- [Agent Atlas PDF 样书](./artifacts/agent-atlas-book.zh-CN.pdf)
- [交互式知识地图](./artifacts/agent-knowledge-map.html)

样章审核通过后，才按六篇二十七章的目录继续扩写。

## 内容结构

| 篇 | 回答的问题 | 章节范围 |
|---|---|---|
| 范式与基础 | Agent 从哪里来，哪些思想真正延续到了今天？ | 1-4 |
| 核心机制 | 工具、状态、上下文、记忆与环境如何组成闭环？ | 5-9 |
| 工程架构 | Workflow、单 Agent、多 Agent、持久运行和协议如何选型？ | 10-14 |
| 生产工程 | 如何发现、评测、保护、部署和运营 Agent？ | 15-19 |
| 完整案例 | 如何把原理落到可审计的企业系统？ | 20-23 |
| 当下与未来 | 2026 技术栈处于什么阶段，未来信号是什么？ | 24-27 |

完整目录和阶段状态见 [content/README.md](./content/README.md)。

## 本地验证

```bash
make validate       # 目录、元数据、来源、引用、链接和时效
make labs           # Python 与 TypeScript 离线实验
make figures        # 校验图源与已发布图
make site           # 生成可搜索 HTML 书站
make book           # 生成 Typst PDF
make visual-check   # 渲染全部 PDF 页面并执行结构检查
make all            # 完整质量门
```

文档构建固定使用 Quarto 1.10.18 与内置 Typst。默认实验不访问网络、不读取 API Key；真实模型适配器将在后续阶段作为可选依赖加入。

Foundation 样书已具备 Tagged PDF、可搜索文本、书签和可点击引用。正式 `PDF/UA-2` 一致性认证仍是 release 门：Quarto 1.10.18 的 Typst 路径会明确忽略 `pdf-standard: ua-2`，因此本阶段不把“Tagged”冒充为“已通过 PDF/UA-2”。

## 证据与更新

- 稳定原理优先引用论文和经典教材。
- 高时效能力只引用正式规范、官方文档、官方仓库和发布记录。
- 事实、推断和情景在 `catalog/claims.yaml` 中分开记录。
- 技术雷达与厂商能力 30 天复核；协议、框架与安全 90 天复核；稳定理论 365 天复核。

## 许可证

代码采用 [MIT](./LICENSE)；正文、图表与原创教学材料采用 [CC BY 4.0](./LICENSE-CONTENT)。第三方资料只做必要引用与原创转述，详见 [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)。
