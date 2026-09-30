#!/usr/bin/env python3
"""Build the Agent Atlas book as a fixed, auditable PDF snapshot."""

import json
import os
import re
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, TTFError
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "book/book.yaml").read_text(encoding="utf-8"))
OUTPUT = Path(os.environ["AGENT_ATLAS_BOOK_OUTPUT"]) if os.environ.get(
    "AGENT_ATLAS_BOOK_OUTPUT"
) else ROOT / CONFIG["output"]
W, H = A4
FONT = "STSong-Light"
FONT_CANDIDATES = (
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJKsc-Regular.otf",
)
INK = HexColor("#172033")
MUTED = HexColor("#64748B")
TEAL = HexColor("#0F9F8F")
CYAN = HexColor("#20B8D8")
VIOLET = HexColor("#7C5CFC")
PAPER = HexColor("#F7FAFC")
LINE = HexColor("#DCE6EE")

SECTIONS = [
    ("01", "00-orientation"),
    ("02", "01-origins"),
    ("03", "02-core-mechanics"),
    ("04", "03-architectures", "04-interoperability"),
    ("05", "05-development-lifecycle"),
    ("06", "06-evaluation"),
    ("07", "07-security-safety-governance"),
    ("08", "08-ecosystem", "09-applications"),
    ("09", "10-current-state"),
    ("10", "11-future"),
    ("11", "12-practice"),
]


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    raw, body = text.split("---", 2)[1:]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data, body.strip()


def plain_markdown(text: str) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("# "):
            continue
        line = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", line)
        line = line.replace("**", "").replace("`", "")
        if line.startswith("## "):
            blocks.append(("heading", line[3:]))
        elif line.startswith("- "):
            blocks.append(("bullet", line[2:]))
        else:
            blocks.append(("body", line))
    return blocks


def wrap(text: str, size: float, width: float) -> list[str]:
    lines, current = [], ""
    for ch in text:
        candidate = current + ch
        if pdfmetrics.stringWidth(candidate, FONT, size) <= width or not current:
            current = candidate
        else:
            lines.append(current.rstrip())
            current = ch.lstrip()
    if current:
        lines.append(current)
    return lines


def header(c: canvas.Canvas, section: str, page: int) -> None:
    c.setStrokeColor(LINE)
    c.line(42, H - 42, W - 42, H - 42)
    c.setFont(FONT, 8)
    c.setFillColor(MUTED)
    c.drawString(42, H - 32, section)
    c.drawRightString(W - 42, H - 32, "AGENT ATLAS")
    c.line(42, 36, W - 42, 36)
    c.drawCentredString(W / 2, 22, str(page))


def draw_blocks(c: canvas.Canvas, blocks: list[tuple[str, str]], y: float, max_lines: int = 31) -> None:
    used = 0
    for kind, text in blocks:
        if used >= max_lines:
            break
        if kind == "heading":
            y -= 7
            c.setFillColor(TEAL)
            c.setFont(FONT, 12)
            c.drawString(54, y, text)
            y -= 21
            used += 2
            continue
        prefix = "• " if kind == "bullet" else ""
        size = 10.5
        c.setFont(FONT, size)
        c.setFillColor(INK)
        for idx, line in enumerate(wrap(prefix + text, size, W - 108)):
            if used >= max_lines:
                break
            c.drawString(54 if idx == 0 else 68, y, line)
            y -= 18
            used += 1
        y -= 6


def new_page(c: canvas.Canvas, section: str, page: int) -> None:
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    header(c, section, page)


def topic_files(folders: tuple[str, ...]) -> list[Path]:
    files: list[Path] = []
    for folder in folders:
        files.extend(p for p in sorted((ROOT / "knowledge" / folder).glob("*.md")) if p.name != "README.md")
    return files


def register_cjk_font() -> Path:
    configured = os.environ.get("AGENT_ATLAS_FONT")
    candidates = ((configured,) if configured else ()) + FONT_CANDIDATES
    errors: list[str] = []
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            try:
                pdfmetrics.registerFont(
                    TTFont(FONT, candidate, asciiReadable=True)
                )
                return Path(candidate)
            except TTFError as exc:
                errors.append(f"{candidate}: {exc}")
    raise RuntimeError(
        "compatible CJK TrueType font not found; install WenQuanYi Zen Hei or set "
        "AGENT_ATLAS_FONT to a TrueType-outline TTF/TTC file. Tried: " + "; ".join(errors)
    )


def build() -> None:
    register_cjk_font()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1, invariant=1)
    c.setTitle(CONFIG["title"])
    c.setAuthor("Agent Atlas Contributors")
    c.setSubject(CONFIG["subtitle"])

    # Cover
    c.setFillColor(HexColor("#071220"))
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(CYAN)
    c.circle(70, H - 88, 8, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont(FONT, 34)
    c.drawString(54, H - 160, "Agent Atlas")
    c.setFont(FONT, 18)
    for i, line in enumerate(wrap(CONFIG["subtitle"], 18, W - 108)):
        c.drawString(54, H - 205 - i * 28, line)
    y = H - 360
    nodes = [("从哪里来", CYAN), ("当下在哪里", TEAL), ("未来去哪里", VIOLET)]
    for idx, (label, color) in enumerate(nodes):
        x = 55 + idx * 172
        c.setFillColor(Color(color.red, color.green, color.blue, alpha=0.16))
        c.roundRect(x, y, 142, 72, 10, fill=1, stroke=0)
        c.setStrokeColor(color)
        c.roundRect(x, y, 142, 72, 10, fill=0, stroke=1)
        c.setFillColor(white)
        c.setFont(FONT, 13)
        c.drawCentredString(x + 71, y + 31, label)
        if idx < 2:
            c.setStrokeColor(white)
            c.line(x + 142, y + 36, x + 172, y + 36)
    c.setFont(FONT, 10)
    c.setFillColor(HexColor("#AFC6D5"))
    c.drawString(54, 72, f"v{CONFIG['version']}  ·  知识截止 {CONFIG['cutoff']}  ·  中文主文 + English terms")
    c.bookmarkPage("cover")
    c.addOutlineEntry("封面", "cover", 0)
    c.showPage()

    page = 2
    # Preface
    new_page(c, "写在前面", page)
    preface = (ROOT / "book/manuscript/00-frontmatter.md").read_text(encoding="utf-8")
    c.setFillColor(INK); c.setFont(FONT, 25); c.drawString(54, H - 100, "写在前面")
    draw_blocks(c, plain_markdown(preface), H - 145)
    c.showPage(); page += 1

    entries = []
    calculated = page + 4
    for chapter, *folders in SECTIONS:
        manuscript = sorted((ROOT / "book/manuscript").glob(f"{chapter}-*.md"))[0]
        chapter_title = manuscript.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
        entries.append((chapter_title, calculated, True))
        calculated += 1
        for path in topic_files(tuple(folders)):
            meta, _ = frontmatter(path.read_text(encoding="utf-8"))
            entries.append((meta["title"], calculated, False))
            calculated += 1

    # Four fixed TOC pages.
    chunks = [entries[i:i + 28] for i in range(0, len(entries), 28)]
    while len(chunks) < 4:
        chunks.append([])
    for index, chunk in enumerate(chunks[:4], start=1):
        new_page(c, "目录", page)
        c.setFillColor(INK); c.setFont(FONT, 24); c.drawString(54, H - 88, f"目录 {index}/4")
        y = H - 126
        for title, target_page, is_chapter in chunk:
            c.setFont(FONT, 10.5 if is_chapter else 9)
            c.setFillColor(TEAL if is_chapter else INK)
            c.drawString(54 if is_chapter else 68, y, title[:35])
            c.setFillColor(MUTED); c.drawRightString(W - 54, y, str(target_page))
            y -= 22 if is_chapter else 18
        c.showPage(); page += 1

    repo = CONFIG["repository"]
    for chapter, *folders in SECTIONS:
        manuscript = sorted((ROOT / "book/manuscript").glob(f"{chapter}-*.md"))[0]
        raw = manuscript.read_text(encoding="utf-8")
        title = raw.splitlines()[0].lstrip("# ")
        anchor = f"chapter-{chapter}"
        new_page(c, title, page)
        c.bookmarkPage(anchor); c.addOutlineEntry(title, anchor, 0)
        c.setFillColor(TEAL); c.setFont(FONT, 13); c.drawString(54, H - 100, f"CHAPTER {chapter}")
        c.setFillColor(INK); c.setFont(FONT, 26)
        for idx, line in enumerate(wrap(title, 26, W - 108)):
            c.drawString(54, H - 142 - idx * 34, line)
        draw_blocks(c, plain_markdown(raw), H - 220)
        c.showPage(); page += 1

        for path in topic_files(tuple(folders)):
            meta, body = frontmatter(path.read_text(encoding="utf-8"))
            new_page(c, title, page)
            topic_anchor = "topic-" + path.stem + "-" + chapter
            c.bookmarkPage(topic_anchor); c.addOutlineEntry(meta["title"], topic_anchor, 1)
            c.setFillColor(CYAN); c.setFont(FONT, 9); c.drawString(54, H - 78, meta.get("status", ""))
            c.setFillColor(INK); c.setFont(FONT, 22)
            for idx, line in enumerate(wrap(meta["title"], 22, W - 108)):
                c.drawString(54, H - 110 - idx * 28, line)
            c.setFillColor(MUTED); c.setFont(FONT, 10)
            summary_y = H - 148 - max(0, len(wrap(meta["title"], 22, W - 108)) - 1) * 28
            for line in wrap(meta.get("summary", ""), 10, W - 108):
                c.drawString(54, summary_y, line); summary_y -= 16
            c.setFillColor(white); c.setStrokeColor(LINE)
            c.roundRect(44, 92, W - 88, summary_y - 112, 8, fill=1, stroke=1)
            draw_blocks(c, plain_markdown(body), summary_y - 22, max_lines=27)
            rel = path.relative_to(ROOT).as_posix()
            url = f"{repo}/blob/main/{rel}"
            c.setFillColor(VIOLET); c.setFont(FONT, 8.5)
            c.drawString(54, 66, "扩展阅读：仓库中的完整章节与持续更新（点击打开）")
            c.linkURL(url, (52, 60, W - 52, 76), relative=0)
            c.showPage(); page += 1

    sources = json.loads((ROOT / "catalog/sources.yaml").read_text(encoding="utf-8"))
    for ref_page, chunk in enumerate((sources[:13], sources[13:]), start=1):
        new_page(c, "参考资料", page)
        c.setFillColor(INK); c.setFont(FONT, 23); c.drawString(54, H - 88, f"参考资料 {ref_page}/2")
        y = H - 126
        for item in chunk:
            c.setFillColor(TEAL); c.setFont(FONT, 9); c.drawString(54, y, item["id"])
            y -= 14
            c.setFillColor(INK); c.setFont(FONT, 9)
            for line in wrap(item["title"], 9, W - 108):
                c.drawString(54, y, line); y -= 14
            c.setFillColor(MUTED); c.setFont(FONT, 7.5); c.drawString(54, y, item["url"][:105])
            c.linkURL(item["url"], (52, y - 2, W - 52, y + 10), relative=0)
            y -= 24
        c.showPage(); page += 1

    c.save()
    reader = PdfReader(str(OUTPUT))
    count = len(reader.pages)
    if not 80 <= count <= 120:
        raise RuntimeError(f"expected 80-120 pages, got {count}")
    print(f"book built: {OUTPUT} ({count} pages)")


if __name__ == "__main__":
    build()
