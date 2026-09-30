# 《Agent Atlas》小书

书稿以 `book/manuscript/` 的连续叙事为骨架，并从 `knowledge/` 抽取非索引主题作为一页式深读卡。每页包含返回 GitHub 知识页的可点击链接。

运行 `python3 scripts/build_book.py` 生成 `artifacts/agent-atlas-book.zh-CN.pdf`。构建机需要带 TrueType 轮廓的中文字体（CI 使用 WenQuanYi Zen Hei）；也可通过 `AGENT_ATLAS_FONT` 指定兼容的 TTF/TTC 文件。`AGENT_ATLAS_BOOK_OUTPUT` 可将 CI 冒烟产物写到临时目录，避免不同平台字体造成版本化 PDF 的伪漂移。生成后必须使用 Poppler 渲染全部页面，并对封面、目录、章节页、密集正文页和参考页做视觉检查。
