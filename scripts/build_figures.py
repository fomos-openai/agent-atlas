#!/usr/bin/env python3
"""Generate deterministic, text-first SVG figures used by the foundation sample."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "rendered"
FONT = "Noto Sans CJK SC, PingFang SC, Microsoft YaHei, sans-serif"


def page(title: str, subtitle: str, body: str, height: int = 680) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{subtitle}</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#071426"/><stop offset="1" stop-color="#13263b"/></linearGradient><filter id="s"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-opacity=".22"/></filter></defs>
<rect width="1200" height="{height}" rx="28" fill="url(#bg)"/>
<text x="64" y="66" font-family="{FONT}" font-size="30" font-weight="700" fill="#f8fafc">{title}</text>
<text x="64" y="100" font-family="{FONT}" font-size="16" fill="#94a3b8">{subtitle}</text>
{body}
<text x="1136" y="{height-28}" text-anchor="end" font-family="{FONT}" font-size="13" fill="#64748b">Agent Atlas · 2026-10-01</text>
</svg>'''


def box(x: int, y: int, w: int, h: int, title: str, sub: str, color: str) -> str:
    return f'''<g filter="url(#s)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#10243a" stroke="{color}" stroke-width="2"/>
<rect x="{x}" y="{y}" width="8" height="{h}" rx="4" fill="{color}"/>
<text x="{x+24}" y="{y+38}" font-family="{FONT}" font-size="20" font-weight="700" fill="#f8fafc">{title}</text>
<text x="{x+24}" y="{y+68}" font-family="{FONT}" font-size="14" fill="#cbd5e1">{sub}</text></g>'''


def arrow(x1: int, y1: int, x2: int, y2: int, label: str = "") -> str:
    mid = (x1 + x2) // 2
    return f'''<path d="M{x1} {y1} L{x2-14} {y2}" stroke="#60a5fa" stroke-width="3" fill="none"/><path d="M{x2-20} {y2-8} L{x2} {y2} L{x2-20} {y2+8}" fill="none" stroke="#60a5fa" stroke-width="3"/>
<text x="{mid}" y="{y1-12}" text-anchor="middle" font-family="{FONT}" font-size="13" fill="#93c5fd">{label}</text>'''


def paradigm() -> str:
    items = [
        (60, "符号规划", "显式状态与搜索", "#38bdf8"),
        (280, "BDI", "信念、目标与承诺", "#a78bfa"),
        (500, "强化学习", "轨迹、奖励与策略", "#34d399"),
        (720, "基础模型", "开放语义与生成", "#f59e0b"),
        (940, "LLM Agent", "模型 + 工具 + 运行时", "#fb7185"),
    ]
    body = '<path d="M90 365 H1110" stroke="#334155" stroke-width="6"/>'
    for i, (x, title, sub, color) in enumerate(items):
        body += box(x, 170 if i % 2 == 0 else 400, 190, 112, title, sub, color)
        cy = 282 if i % 2 == 0 else 400
        body += f'<path d="M{x+95} {cy} V365" stroke="{color}" stroke-width="3"/><circle cx="{x+95}" cy="365" r="9" fill="{color}"/>'
    body += '<text x="600" y="610" text-anchor="middle" font-family="%s" font-size="18" fill="#e2e8f0">旧范式并未消失：生产系统将语义决策与确定性控制重新组合</text>' % FONT
    return page("Agent 范式演化", "状态表示、决策、反馈和控制权的重组", body)


def allocation() -> str:
    cols = ["状态解释", "计划生成", "动作选择", "约束执行"]
    rows = [("符号规划", [3,3,2,3]), ("BDI", [3,3,2,3]), ("强化学习", [2,1,3,2]), ("LLM Agent", [3,3,3,1]), ("生产混合架构", [3,3,3,3])]
    colors = ["#1e3a5f", "#2563eb", "#22c55e"]
    body = ''
    for c, name in enumerate(cols):
        body += f'<text x="{390+c*170}" y="165" text-anchor="middle" font-family="{FONT}" font-size="16" fill="#cbd5e1">{name}</text>'
    for r, (name, values) in enumerate(rows):
        y = 198+r*82
        body += f'<text x="230" y="{y+34}" text-anchor="end" font-family="{FONT}" font-size="18" fill="#f8fafc">{name}</text>'
        for c, value in enumerate(values):
            x = 310+c*170
            body += f'<rect x="{x}" y="{y}" width="150" height="54" rx="12" fill="{colors[value-1]}"/><text x="{x+75}" y="{y+34}" text-anchor="middle" font-family="{FONT}" font-size="14" fill="#f8fafc">{"低" if value==1 else "中" if value==2 else "高"}</text>'
    body += '<text x="600" y="636" text-anchor="middle" font-family="%s" font-size="15" fill="#94a3b8">深色代表该范式在该层承担更多动态决策；混合架构保留独立的确定性保证层</text>' % FONT
    return page("控制权分配矩阵", "不同范式把复杂性放在不同系统层", body)


def tool_boundary() -> str:
    nodes = [
        (50, 255, "模型", "提出 ToolCall", "#a78bfa"),
        (270, 255, "运行时", "校验 · 预算 · 状态", "#38bdf8"),
        (510, 255, "策略网关", "授权 · 审批", "#fb7185"),
        (750, 255, "隔离执行器", "超时 · 幂等 · 沙箱", "#f59e0b"),
        (970, 255, "外部系统", "真实副作用", "#34d399"),
    ]
    body = ''
    for x, y, title, sub, color in nodes:
        body += box(x, y, 180, 112, title, sub, color)
    for i in range(len(nodes)-1):
        body += arrow(nodes[i][0]+180, 311, nodes[i+1][0], 311, ["提议", "判定", "授权", "执行"][i])
    body += box(420, 470, 360, 100, "审计轨迹与状态存储", "事件、检查点、结果与策略版本", "#64748b")
    for x in [360, 600, 840]:
        body += f'<path d="M{x} 370 Q{x} 430 520 470" stroke="#64748b" stroke-width="2" stroke-dasharray="7 6" fill="none"/>'
    body += '<text x="600" y="190" text-anchor="middle" font-family="%s" font-size="18" fill="#e2e8f0">提议权 ≠ 授权权 ≠ 效果权</text>' % FONT
    return page("工具调用的系统边界", "五份契约把概率决策与真实环境隔开", body)


def tool_lifecycle() -> str:
    items = [
        (55, 180, "1  提议", "结构化 ToolCall", "#a78bfa"),
        (285, 180, "2  验证", "schema + 业务语义", "#38bdf8"),
        (515, 180, "3  策略", "allow / deny / approval", "#fb7185"),
        (745, 180, "4  执行", "幂等 + 超时 + 隔离", "#f59e0b"),
        (975, 180, "5  提交", "结果 + 状态 + 事件", "#34d399"),
    ]
    body = ''
    for x, y, title, sub, color in items:
        body += box(x, y, 170, 112, title, sub, color)
    for i in range(4): body += arrow(items[i][0]+170, 236, items[i+1][0], 236)
    body += box(455, 410, 290, 105, "WAITING_APPROVAL", "持久化调用参数与策略版本", "#fb7185")
    body += '<path d="M600 292 V410" stroke="#fb7185" stroke-width="3"/><path d="M600 410 L590 392 M600 410 L610 392" stroke="#fb7185" stroke-width="3"/>'
    body += '<path d="M745 463 H850 Q890 463 890 420 V300" stroke="#60a5fa" stroke-width="3" fill="none" stroke-dasharray="8 6"/><text x="790" y="448" font-family="%s" font-size="13" fill="#93c5fd">批准后恢复原调用</text>' % FONT
    body += '<text x="600" y="600" text-anchor="middle" font-family="%s" font-size="16" fill="#cbd5e1">失败不是一段异常文本，而是可恢复状态机中的显式分支</text>' % FONT
    return page("工具调用生命周期", "审批、幂等和恢复都是运行状态的一部分", body)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    figures = {
        "paradigm-evolution.svg": paradigm(),
        "control-allocation.svg": allocation(),
        "tool-boundary.svg": tool_boundary(),
        "tool-call-lifecycle.svg": tool_lifecycle(),
    }
    for name, svg in figures.items():
        (OUT / name).write_text(svg, encoding="utf-8")
    print(f"generated {len(figures)} deterministic SVG figures")


if __name__ == "__main__":
    main()
