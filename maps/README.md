# Archify 知识地图

源文件 `agent-knowledge-map.architecture.json` 使用 Archify v3.0.1 architecture schema。为保证复现，本版固定 tag `v3.0.1`，annotated tag object 为 `679f195584e4216fd582c073d8964b3a9f59107e`，对应 commit 为 `2ab3cae7ac2c2a55d7386ca789d03c4fcd31816c`。生成命令：

```bash
node /absolute/path/to/archify/bin/archify.mjs finalize architecture \
  maps/agent-knowledge-map.architecture.json artifacts/agent-knowledge-map.html \
  --quality showcase --json
```

交付前必须保留 finalize 摘要并执行感知审查。地图描述知识体系，不声称对仓库代码做 revision-pinned 架构证明。
