# 贡献指南

Agent Atlas 接受事实修正、新技术条目、案例、评测数据与最小实验。提交内容必须回答：它解决什么问题、证据是什么、适用边界是什么、何时需要重新核验。

## 内容约定

1. 知识页必须包含 `title`、`summary`、`status`、`last_verified`、`source_ids`、`tags` front matter。
2. `status` 只能为 `stable`、`evolving`、`experimental` 或 `speculative`。
3. 事实优先引用论文、正式规范和官方文档；厂商比较不得把营销声明当成独立证据。
4. 推断必须明确写出依据、置信度和可能推翻它的信号。
5. 示例默认离线、确定性、无需 API Key；真实模型适配必须是可选项。

## 本地检查

运行 `make all`。如改动地图，使用 `maps/README.md` 中固定的 Archify 流程重新 finalize；如改动书稿或知识页，重新生成并逐页检查 PDF。
